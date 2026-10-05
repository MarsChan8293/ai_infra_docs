#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import io
import json
import pathlib
from collections import Counter

import yaml

EXCLUDED_NAMES = {"SCHEMA.md", "MIGRATION.md", "00-project-index.md"}

CLASS_BY_TYPE = {
    "accelerator-interconnect": "accelerator-interconnect",
    "interconnect-standard": "interconnect-standard",
    "network-switch-generation": "switch-generation",
    "network-asic": "switch-asic",
    "switch-system": "switch-system",
    "cpo-switch": "cpo-switch",
    "npo-optical-engine": "optical-engine",
    "optical-engine": "optical-engine",
    "optical-transceiver": "optical-transceiver",
    "network-adapter": "endpoint",
    "hca": "endpoint",
    "nic": "endpoint",
    "nic-silicon": "endpoint",
    "dpu": "endpoint",
}

OPTICAL_PACKAGING_BY_TYPE = {
    "cpo-switch": "CPO",
    "npo-optical-engine": "NPO",
}

SCALE_FIELDS = {
    "max_domain_gpus",
    "supported_domain_gpus",
    "max_accelerators",
    "scale_up_xpus",
    "two_tier_scale_xpus",
    "target_scale",
    "node_gpus",
    "mi300x_node_gpus",
}

RATE_SUFFIXES = (
    ("_gbps", "Gb/s", 1.0),
    ("_gb_s", "GB/s", 8.0),
    ("_tb_s", "TB/s", 8000.0),
    ("_tbit_s", "Tb/s", 1000.0),
)


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    try:
        data = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


def populated(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return bool(value)
    return True


def flatten(value: object, prefix: str = "") -> dict[str, object]:
    out: dict[str, object] = {}
    if isinstance(value, dict):
        for key, child in value.items():
            path = f"{prefix}.{key}" if prefix else str(key)
            if isinstance(child, dict):
                out.update(flatten(child, path))
            else:
                out[path] = child
    elif prefix:
        out[prefix] = value
    return out


def rate_meta(field: str) -> tuple[str, float] | None:
    leaf = field.rsplit(".", 1)[-1].lower()
    for suffix, unit, multiplier in RATE_SUFFIXES:
        if leaf.endswith(suffix):
            return unit, multiplier
    return None


def infer_scope(field: str, object_class: str) -> str:
    leaf = field.rsplit(".", 1)[-1].lower()

    if "lane" in leaf:
        return "lane"
    if "engine" in leaf:
        return "engine"
    if "station" in leaf:
        return "station"
    if "domain" in leaf or "nvl72" in leaf:
        return "domain"
    if "switch_capacity" in leaf:
        return "switch"
    if "per_link" in leaf:
        return "link"

    device_tokens = (
        "per_gpu",
        "gpu_to_gpu",
        "p2p",
        "per_chip",
        "total_bandwidth",
        "ethernet_max",
        "infiniband_max",
    )
    if any(token in leaf for token in device_tokens):
        return "device"

    if "link" in leaf and not leaf.startswith(("links_", "max_links_", "peer_links_")):
        return "link"

    if object_class == "endpoint":
        return "device"
    if object_class in {"switch-asic", "switch-generation", "switch-system", "cpo-switch"} and "capacity" in leaf:
        return "switch"

    return "unknown"


def infer_direction(field: str) -> str:
    leaf = field.rsplit(".", 1)[-1].lower()
    if "bidirectional" in leaf:
        return "bidirectional"
    if "_tx_" in f"_{leaf}_" or leaf.startswith("tx_") or leaf.endswith("_tx"):
        return "tx"
    if "_rx_" in f"_{leaf}_" or leaf.startswith("rx_") or leaf.endswith("_rx"):
        return "rx"
    return "unknown"


def infer_aggregation(field: str, scope: str) -> str:
    leaf = field.rsplit(".", 1)[-1].lower()
    if "aggregate" in leaf or "total" in leaf or "switch_capacity" in leaf:
        return "aggregate"
    if "per_" in leaf or scope in {"lane", "link", "engine", "station"}:
        return "per-unit"
    return "unknown"


def object_class(object_type: str) -> str:
    return CLASS_BY_TYPE.get(object_type, object_type or "unknown")


def optical_packaging(fm: dict, interconnect: dict) -> str | None:
    object_type = str(fm.get("object_type") or "")
    if object_type in OPTICAL_PACKAGING_BY_TYPE:
        return OPTICAL_PACKAGING_BY_TYPE[object_type]
    value = interconnect.get("optical_packaging")
    if isinstance(value, str) and value.strip():
        return value.strip().upper()
    kind = interconnect.get("type")
    if isinstance(kind, str):
        upper = kind.upper()
        for token in ("CPO", "NPO", "LPO"):
            if token in upper:
                return token
    return None


def medium_summary(fm: dict, interconnect: dict, packaging: str | None) -> str | None:
    values: list[str] = []
    flat = flatten(interconnect, "interconnect")
    for path, value in flat.items():
        leaf = path.rsplit(".", 1)[-1].lower()
        if leaf.endswith("medium") and populated(value):
            values.append(str(value))
    if interconnect.get("optical_interconnect") is True:
        values.append("optical-capable")
    if packaging in {"CPO", "NPO", "LPO"}:
        values.append("optical")
    unique: list[str] = []
    for value in values:
        if value not in unique:
            unique.append(value)
    return " / ".join(unique) if unique else None


def collect_named(interconnect: dict, predicate) -> list[dict]:
    out: list[dict] = []
    for path, value in flatten(interconnect, "interconnect").items():
        if populated(value) and predicate(path.rsplit(".", 1)[-1].lower()):
            out.append({"field": path, "value": value})
    return out


def bandwidth_entries(fm: dict, interconnect: dict) -> list[dict]:
    cls = object_class(str(fm.get("object_type") or ""))
    out: list[dict] = []
    for path, value in flatten(interconnect, "interconnect").items():
        meta = rate_meta(path)
        if meta is None:
            continue
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            continue
        unit, multiplier = meta
        scope = infer_scope(path, cls)
        out.append({
            "field": path,
            "value": value,
            "unit": unit,
            "normalized_gbps": round(float(value) * multiplier, 6),
            "scope": scope,
            "direction": infer_direction(path),
            "aggregation": infer_aggregation(path, scope),
        })
    return out


def compact_value(value: object) -> str:
    if isinstance(value, list):
        return "/".join(str(x) for x in value)
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def rate_display(entries: list[dict], scope: str) -> str:
    parts: list[str] = []
    for entry in entries:
        if entry["scope"] != scope:
            continue
        leaf = entry["field"].rsplit(".", 1)[-1]
        direction = {
            "bidirectional": " ↔",
            "tx": " TX",
            "rx": " RX",
        }.get(entry["direction"], "")
        parts.append(f"{leaf}={entry['value']} {entry['unit']}{direction}")
    return "; ".join(parts) if parts else "unknown"


def named_display(entries: list[dict]) -> str:
    if not entries:
        return "unknown"
    return "; ".join(
        f"{entry['field'].rsplit('.', 1)[-1]}={compact_value(entry['value'])}"
        for entry in entries
    )


def md_cell(value: object) -> str:
    if value is None:
        return "unknown"
    return str(value).replace("|", "\\|")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--output", default="generated")
    args = ap.parse_args()

    root = pathlib.Path(args.root).resolve()
    output = root / args.output
    output.mkdir(parents=True, exist_ok=True)

    records: list[dict] = []
    total_interconnect_facts = 0
    total_evidenced_interconnect_facts = 0

    for path in sorted((root / "chip").rglob("*.md")):
        if path.name in EXCLUDED_NAMES:
            continue
        rel = path.relative_to(root).as_posix()
        fm = parse_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
        interconnect = fm.get("interconnect")
        if fm.get("layer") != "network" or not isinstance(interconnect, dict) or not interconnect:
            continue
        if fm.get("object_type") == "vendor-overview":
            continue

        node_id = pathlib.PurePosixPath(rel).with_suffix("").as_posix()
        packaging = optical_packaging(fm, interconnect)
        cls = object_class(str(fm.get("object_type") or ""))
        rates = bandwidth_entries(fm, interconnect)
        topology = collect_named(interconnect, lambda leaf: "topology" in leaf)
        scale = collect_named(interconnect, lambda leaf: leaf in SCALE_FIELDS)
        latency = collect_named(interconnect, lambda leaf: "latency" in leaf or "rtt" in leaf)

        evidence = fm.get("evidence") if isinstance(fm.get("evidence"), dict) else {}
        evidence_map = fm.get("evidence_map") if isinstance(fm.get("evidence_map"), dict) else {}
        flat = flatten(interconnect, "interconnect")
        fact_paths = {path for path, value in flat.items() if populated(value)}
        explicit_paths = {str(key) for key in evidence_map if key != "__page__"}
        evidenced = fact_paths & explicit_paths
        total_interconnect_facts += len(fact_paths)
        total_evidenced_interconnect_facts += len(evidenced)

        records.append({
            "id": node_id,
            "path": rel,
            "title": fm.get("title"),
            "vendor": fm.get("vendor"),
            "object_type": fm.get("object_type"),
            "object_class": cls,
            "status": fm.get("status"),
            "architecture": fm.get("architecture"),
            "medium": medium_summary(fm, interconnect, packaging),
            "optical_packaging": packaging,
            "rates": rates,
            "topology": topology,
            "scale": scale,
            "latency": latency,
            "source_count": len(evidence),
            "interconnect_fact_count": len(fact_paths),
            "interconnect_field_evidence_count": len(evidenced),
            "interconnect_field_evidence_ratio": round(len(evidenced) / len(fact_paths), 4) if fact_paths else 1.0,
            "updated": str(fm.get("updated")) if fm.get("updated") is not None else None,
        })

    records.sort(key=lambda r: (str(r["object_class"]), str(r["vendor"]), str(r["title"])))
    (output / "interconnect-catalog.json").write_text(
        json.dumps(records, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    csv_columns = [
        "id", "title", "vendor", "object_type", "object_class", "status",
        "medium", "optical_packaging", "lane_bandwidth", "link_bandwidth",
        "station_bandwidth", "device_bandwidth", "engine_bandwidth",
        "switch_bandwidth", "domain_bandwidth", "scale", "topology", "latency",
        "source_count", "interconnect_field_evidence_ratio", "updated",
    ]
    csv_buf = io.StringIO()
    writer = csv.DictWriter(csv_buf, fieldnames=csv_columns)
    writer.writeheader()
    for record in records:
        writer.writerow({
            "id": record["id"],
            "title": record["title"],
            "vendor": record["vendor"],
            "object_type": record["object_type"],
            "object_class": record["object_class"],
            "status": record["status"],
            "medium": record["medium"] or "",
            "optical_packaging": record["optical_packaging"] or "",
            "lane_bandwidth": rate_display(record["rates"], "lane"),
            "link_bandwidth": rate_display(record["rates"], "link"),
            "station_bandwidth": rate_display(record["rates"], "station"),
            "device_bandwidth": rate_display(record["rates"], "device"),
            "engine_bandwidth": rate_display(record["rates"], "engine"),
            "switch_bandwidth": rate_display(record["rates"], "switch"),
            "domain_bandwidth": rate_display(record["rates"], "domain"),
            "scale": named_display(record["scale"]),
            "topology": named_display(record["topology"]),
            "latency": named_display(record["latency"]),
            "source_count": record["source_count"],
            "interconnect_field_evidence_ratio": record["interconnect_field_evidence_ratio"],
            "updated": record["updated"],
        })
    (output / "interconnect-comparison.csv").write_text(csv_buf.getvalue(), encoding="utf-8")

    comparison = [
        "---",
        "title: Interconnect / Fabric / Optical I/O 横向比较",
        "tags:",
        "  - generated",
        "  - interconnect",
        "  - fabric",
        "  - optical",
        "---",
        "",
        "# Interconnect / Fabric / Optical I/O 横向比较",
        "",
        "> 由 `scripts/build-interconnect-catalog.py` 自动生成。只对字段名能够明确映射 scope 的速率进行归类；无法安全归类的值保持 unknown，不按 0 补齐。",
        "",
        "## Scope 规则",
        "",
        "- Lane / Link / Station / Device / Engine / Switch / Domain 是不同 scope，不允许直接互换。",
        "- GB/s 与 Gb/s 只在 JSON 中提供 decimal normalized_gbps 辅助值；Markdown 保留厂商原始单位。",
        "- CPO / NPO 是 optical packaging / I/O implementation，不是网络协议。",
        "- direction 只有字段明确包含 bidirectional / TX / RX 时才标注。",
        "",
        "| 对象 | Class | Medium | Optical | Lane | Link | Station | Device | Engine | Switch | Domain | Scale | Topology |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for record in records:
        comparison.append(
            f"| [[{record['id']}|{md_cell(record['title'])}]] "
            f"| {md_cell(record['object_class'])} "
            f"| {md_cell(record['medium'])} "
            f"| {md_cell(record['optical_packaging'])} "
            f"| {md_cell(rate_display(record['rates'], 'lane'))} "
            f"| {md_cell(rate_display(record['rates'], 'link'))} "
            f"| {md_cell(rate_display(record['rates'], 'station'))} "
            f"| {md_cell(rate_display(record['rates'], 'device'))} "
            f"| {md_cell(rate_display(record['rates'], 'engine'))} "
            f"| {md_cell(rate_display(record['rates'], 'switch'))} "
            f"| {md_cell(rate_display(record['rates'], 'domain'))} "
            f"| {md_cell(named_display(record['scale']))} "
            f"| {md_cell(named_display(record['topology']))} |"
        )
    comparison.extend([
        "",
        "## 阅读注意",
        "",
        "- 同一列只表示 scope 相同，不代表 protocol semantics、方向、拓扑和有效 payload efficiency 相同。",
        "- Device 栏可以包含 GPU/OAM/chip/NIC/DPU 的设备级 aggregate 或 P2P 口径，具体语义必须回到对象页和原字段。",
        "- Domain 栏只收明确带 domain / system-name aggregate 语义的带宽字段；系统实际 collective bandwidth 仍由 System 层建模。",
        "",
    ])
    (output / "interconnect-comparison.md").write_text("\n".join(comparison), encoding="utf-8")

    scope_names = ("lane", "link", "station", "device", "engine", "switch", "domain")
    object_scope_counts = {
        scope: sum(1 for record in records if any(rate["scope"] == scope for rate in record["rates"]))
        for scope in scope_names
    }
    unscoped = [
        {
            "id": record["id"],
            "field": rate["field"],
            "value": rate["value"],
            "unit": rate["unit"],
        }
        for record in records
        for rate in record["rates"]
        if rate["scope"] == "unknown"
    ]
    unknown_direction = [
        {
            "id": record["id"],
            "field": rate["field"],
            "scope": rate["scope"],
        }
        for record in records
        for rate in record["rates"]
        if rate["direction"] == "unknown"
    ]

    total = len(records)
    health = {
        "objects": total,
        "classes": dict(sorted(Counter(str(r["object_class"]) for r in records).items())),
        "vendors": dict(sorted(Counter(str(r["vendor"]) for r in records).items())),
        "objects_with_medium": sum(1 for r in records if r["medium"]),
        "objects_with_optical_packaging": sum(1 for r in records if r["optical_packaging"]),
        "objects_with_scale": sum(1 for r in records if r["scale"]),
        "objects_with_topology": sum(1 for r in records if r["topology"]),
        "objects_with_latency": sum(1 for r in records if r["latency"]),
        "objects_by_bandwidth_scope": object_scope_counts,
        "page_source_coverage": round(sum(1 for r in records if r["source_count"] > 0) / total, 4) if total else 1.0,
        "interconnect_field_evidence_coverage": round(
            total_evidenced_interconnect_facts / total_interconnect_facts, 4
        ) if total_interconnect_facts else 1.0,
        "unscoped_bandwidth_fields": unscoped,
        "unknown_direction_bandwidth_fields": unknown_direction,
    }
    (output / "interconnect-health.json").write_text(
        json.dumps(health, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    pct = lambda n, d: f"{(100.0 * n / d) if d else 100.0:.1f}%"
    health_md = [
        "---",
        "title: Interconnect 数据健康度",
        "tags:",
        "  - generated",
        "  - interconnect",
        "  - data-quality",
        "---",
        "",
        "# Interconnect 数据健康度",
        "",
        "> 由结构化 frontmatter 自动生成。本页衡量可比较性和 Evidence，不用猜测填补缺失字段。",
        "",
        "| 指标 | 值 |",
        "|---|---:|",
        f"| Network/interconnect 对象 | {total} |",
        f"| 页面直接来源覆盖 | {health['page_source_coverage'] * 100:.1f}% |",
        f"| Interconnect 字段级 Evidence 覆盖 | {health['interconnect_field_evidence_coverage'] * 100:.1f}% |",
        f"| Medium 已明确 | {health['objects_with_medium']} / {total} ({pct(health['objects_with_medium'], total)}) |",
        f"| Optical packaging 已明确 | {health['objects_with_optical_packaging']} / {total} ({pct(health['objects_with_optical_packaging'], total)}) |",
        f"| Scale/domain 信息已明确 | {health['objects_with_scale']} / {total} ({pct(health['objects_with_scale'], total)}) |",
        f"| Topology 信息已明确 | {health['objects_with_topology']} / {total} ({pct(health['objects_with_topology'], total)}) |",
        f"| Latency/RTT 信息已明确 | {health['objects_with_latency']} / {total} ({pct(health['objects_with_latency'], total)}) |",
        "",
        "## Bandwidth scope 覆盖",
        "",
        "| Scope | 有该 scope 的对象数 |",
        "|---|---:|",
    ]
    for scope in scope_names:
        health_md.append(f"| {scope} | {object_scope_counts[scope]} |")

    health_md.extend([
        "",
        "## Scope 待清理字段",
        "",
    ])
    if unscoped:
        health_md.extend([
            "| 对象 | 字段 | 值 |",
            "|---|---|---:|",
        ])
        for item in unscoped:
            health_md.append(
                f"| [[{item['id']}]] | `{item['field']}` | {item['value']} {item['unit']} |"
            )
    else:
        health_md.append("当前没有无法归类 scope 的结构化 bandwidth/rate 字段。")

    health_md.extend([
        "",
        "## 解释",
        "",
        "- Medium、Topology、Latency 缺失表示公开结构化事实不足，不表示产品不具备该能力。",
        "- unknown direction 不作为错误；只有来源字段明确时才写 bidirectional / TX / RX。",
        "- unscoped bandwidth 字段是后续 Schema/对象页规范化的优先清单，但不会由生成器自行猜测 scope。",
        "",
    ])
    (output / "interconnect-health.md").write_text("\n".join(health_md), encoding="utf-8")

    print(
        "interconnect_objects="
        f"{total} field_evidence={health['interconnect_field_evidence_coverage']:.3f} "
        f"unscoped_bandwidth={len(unscoped)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
