#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import json
import pathlib
from collections import Counter

import yaml

EXCLUDED_NAMES = {"SCHEMA.md", "MIGRATION.md", "00-project-index.md"}
FACT_BLOCKS = ("architecture", "process", "memory", "compute", "interconnect", "power", "lifecycle")


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


def populated(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return bool(value)
    return True


def first_leaf(fm: dict, suffix: str) -> object:
    for block in ("memory", "compute", "interconnect", "power"):
        value = fm.get(block)
        if isinstance(value, dict):
            for path, leaf in flatten(value, block).items():
                if path.endswith(suffix) and populated(leaf):
                    return leaf
    return None


def architecture_name(value: object) -> object:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        for key in ("name", "architecture", "family", "description"):
            if populated(value.get(key)):
                return value[key]
    return None


def parse_date(value: object) -> dt.date | None:
    if isinstance(value, dt.date):
        return value
    if isinstance(value, str):
        try:
            return dt.date.fromisoformat(value)
        except ValueError:
            return None
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--output", default="generated")
    ap.add_argument("--as-of", default=dt.date.today().isoformat())
    args = ap.parse_args()
    root = pathlib.Path(args.root).resolve()
    output = root / args.output
    output.mkdir(parents=True, exist_ok=True)
    as_of = dt.date.fromisoformat(args.as_of)

    records: list[dict] = []
    for path in sorted((root / "chip").rglob("*.md")):
        if path.name in EXCLUDED_NAMES:
            continue
        rel = path.relative_to(root).as_posix()
        fm = parse_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
        if not fm.get("vendor") or not fm.get("object_type") or fm.get("object_type") == "vendor-overview":
            continue
        node_id = pathlib.PurePosixPath(rel).with_suffix("").as_posix()
        facts: dict[str, object] = {}
        for block in FACT_BLOCKS:
            value = fm.get(block)
            if isinstance(value, dict):
                facts.update(flatten(value, block))
            elif populated(value):
                facts[block] = value
        evidence = fm.get("evidence") if isinstance(fm.get("evidence"), dict) else {}
        evidence_map = fm.get("evidence_map") if isinstance(fm.get("evidence_map"), dict) else {}
        explicit_paths = {str(key) for key in evidence_map if key != "__page__"}
        fact_paths = {key for key, value in facts.items() if populated(value)}
        evidenced_paths = fact_paths & explicit_paths
        updated = parse_date(fm.get("updated"))
        stale = bool(updated and (as_of - updated).days > 180)
        records.append({
            "id": node_id,
            "path": rel,
            "title": fm.get("title"),
            "vendor": fm.get("vendor"),
            "object_type": fm.get("object_type"),
            "layer": fm.get("layer"),
            "status": fm.get("status"),
            "schema_version": fm.get("schema_version"),
            "architecture": architecture_name(fm.get("architecture")),
            "memory_type": first_leaf(fm, ".type") if isinstance(fm.get("memory"), dict) else None,
            "memory_capacity_gb": first_leaf(fm, "capacity_gb"),
            "memory_bandwidth_tb_s": first_leaf(fm, "bandwidth_tb_s"),
            "power_w": first_leaf(fm, "value_w"),
            "updated": str(fm.get("updated")) if fm.get("updated") is not None else None,
            "stale_gt_180d": stale,
            "source_count": len(evidence),
            "fact_field_count": len(fact_paths),
            "field_evidence_count": len(evidenced_paths),
            "field_evidence_ratio": round(len(evidenced_paths) / len(fact_paths), 4) if fact_paths else 1.0,
            "relation_count": sum(len(v) if isinstance(v, list) else 1 for v in (fm.get("relations") or {}).values()) if isinstance(fm.get("relations"), dict) else 0,
            "frontmatter": fm,
        })

    (output / "chip-catalog.json").write_text(json.dumps(records, ensure_ascii=False, indent=2, default=str), encoding="utf-8")

    columns = [
        "id", "title", "vendor", "object_type", "layer", "status", "architecture",
        "memory_type", "memory_capacity_gb", "memory_bandwidth_tb_s", "power_w",
        "updated", "stale_gt_180d", "source_count", "field_evidence_ratio", "relation_count",
    ]
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=columns, extrasaction="ignore")
    writer.writeheader()
    for record in records:
        writer.writerow(record)
    (output / "chip-comparison.csv").write_text(buf.getvalue(), encoding="utf-8")

    def cell(value: object) -> str:
        if value is None:
            return ""
        if isinstance(value, list):
            value = "/".join(str(x) for x in value)
        return str(value).replace("|", "\\|")

    comparison = [
        "---", "title: Chip 横向比较", "tags:", "  - generated", "  - chip", "  - comparison", "---", "",
        "# Chip 横向比较", "",
        "> 由 `scripts/build-chip-catalog.py` 自动生成。只展示可机器比较的结构化字段；空白表示未确认。", "",
        "| 对象 | 厂商 | Layer | Status | 架构 | Memory GB | BW TB/s | Power W |",
        "|---|---|---|---|---|---:|---:|---:|",
    ]
    for r in records:
        comparison.append(
            f"| [[{r['id']}|{cell(r['title'])}]] | {cell(r['vendor'])} | {cell(r['layer'])} | {cell(r['status'])} | "
            f"{cell(r['architecture'])} | {cell(r['memory_capacity_gb'])} | {cell(r['memory_bandwidth_tb_s'])} | {cell(r['power_w'])} |"
        )
    comparison.append("")
    (output / "chip-comparison.md").write_text("\n".join(comparison), encoding="utf-8")

    total = len(records)
    def count_block(block: str) -> int:
        return sum(1 for r in records if populated(r["frontmatter"].get(block)))

    total_fact_fields = sum(r["fact_field_count"] for r in records)
    total_evidenced_fields = sum(r["field_evidence_count"] for r in records)
    health = {
        "as_of": args.as_of,
        "objects": total,
        "schema_v0_2": sum(1 for r in records if r["schema_version"] == "chip-v0.2"),
        "schema_coverage": round(sum(1 for r in records if r["schema_version"] == "chip-v0.2") / total, 4) if total else 1.0,
        "page_source_coverage": round(sum(1 for r in records if r["source_count"] > 0) / total, 4) if total else 1.0,
        "field_evidence_coverage": round(total_evidenced_fields / total_fact_fields, 4) if total_fact_fields else 1.0,
        "memory_completeness": round(count_block("memory") / total, 4) if total else 1.0,
        "compute_completeness": round(count_block("compute") / total, 4) if total else 1.0,
        "interconnect_completeness": round(count_block("interconnect") / total, 4) if total else 1.0,
        "power_completeness": round(count_block("power") / total, 4) if total else 1.0,
        "lifecycle_completeness": round(count_block("lifecycle") / total, 4) if total else 1.0,
        "stale_gt_180d": sum(1 for r in records if r["stale_gt_180d"]),
        "typed_relation_edges": sum(r["relation_count"] for r in records),
        "layers": dict(sorted(Counter(str(r["layer"]) for r in records).items())),
        "vendors": dict(sorted(Counter(str(r["vendor"]) for r in records).items())),
    }
    (output / "chip-health.json").write_text(json.dumps(health, ensure_ascii=False, indent=2), encoding="utf-8")

    pct = lambda x: f"{x * 100:.1f}%"
    lines = [
        "---", "title: Chip 数据健康度", "tags:", "  - generated", "  - chip", "  - data-quality", "---", "",
        "# Chip 数据健康度", "",
        f"> 自动生成于 `{args.as_of}`。Markdown/frontmatter 是唯一事实源，本页不手工维护。", "",
        "| 指标 | 值 |", "|---|---:|",
        f"| 硬件对象 | {health['objects']} |",
        f"| Chip V0.2 覆盖 | {pct(health['schema_coverage'])} |",
        f"| 页面级来源覆盖 | {pct(health['page_source_coverage'])} |",
        f"| 字段级 Evidence 覆盖 | {pct(health['field_evidence_coverage'])} |",
        f"| Memory 完整度 | {pct(health['memory_completeness'])} |",
        f"| Compute 完整度 | {pct(health['compute_completeness'])} |",
        f"| Interconnect 完整度 | {pct(health['interconnect_completeness'])} |",
        f"| Power 完整度 | {pct(health['power_completeness'])} |",
        f"| Lifecycle 完整度 | {pct(health['lifecycle_completeness'])} |",
        f"| 超过 180 天未更新 | {health['stale_gt_180d']} |",
        f"| Typed relation edges | {health['typed_relation_edges']} |", "",
        "## 解释", "",
        "- 页面级来源覆盖只说明页面存在直接来源。",
        "- 字段级 Evidence 覆盖只统计 `evidence_map` 中显式绑定到字段路径的事实，`__page__` 不计入。",
        "- 完整度只表示结构化块存在，不代表字段内容已被独立验证。",
        "- 低覆盖是待研究清单，不应通过猜测或复制相邻 SKU 数据来抬高。", "",
    ]
    (output / "chip-health.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"chip_objects={total} schema_coverage={health['schema_coverage']:.3f} field_evidence={health['field_evidence_coverage']:.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
