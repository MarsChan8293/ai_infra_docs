#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
from urllib.parse import urlparse

import yaml

URL_RE = re.compile(r"https?://[^\s)>\]]+")
ID_RE = re.compile(r"^S\d+$")
KEBAB_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
LAYERS = {"family", "chip", "accelerator", "board", "module", "system", "rack", "cluster", "network", "memory", "storage", "soc", "ip", "unknown"}
STATUSES = {"roadmap", "announced", "sampling", "pre-deployment", "production", "shipping", "current-catalog", "product", "ga", "legacy", "eol", "unknown"}
RELATIONS = {"architecture-of", "variant-of", "successor-of", "predecessor-of", "packaged-in", "used-in", "part-of", "connects-via", "compatible-with", "related"}
SOURCE_TYPES = {"official", "datasheet", "conference", "cloud", "independent", "analysis", "other"}
REQUIRED = {"schema_version", "title", "vendor", "object_type", "layer", "status", "architecture", "process", "memory", "compute", "interconnect", "power", "lifecycle", "relations", "evidence", "evidence_map", "updated"}
AGGREGATE_KEYS_FOR_CHIP = {"gpus", "gpu_count", "accelerators", "accelerator_count", "nodes", "node_count", "servers", "server_count", "rack_power_kw", "system_power_kw", "cluster_size"}
NUMERIC_SUFFIXES = ("_gb", "_tb_s", "_gb_s", "_tflops", "_tops", "_w", "_kw", "_nm", "_mhz", "_ghz")
EXCLUDED_NAMES = {"SCHEMA.md", "MIGRATION.md", "00-project-index.md"}


def parse_frontmatter(text: str, path: str, errors: list[str]) -> dict:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        errors.append(f"{path}: frontmatter 未闭合")
        return {}
    try:
        data = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError as exc:
        errors.append(f"{path}: YAML 解析失败: {exc}")
        return {}
    if not isinstance(data, dict):
        errors.append(f"{path}: frontmatter 必须是 mapping")
        return {}
    return data


def section(text: str, heading: str) -> str:
    match = re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.M)
    if not match:
        return ""
    start = match.end()
    nxt = re.search(r"^##\s+", text[start:], re.M)
    end = start + nxt.start() if nxt else len(text)
    return text[start:end]


def valid_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def valid_date(value: object) -> bool:
    if isinstance(value, dt.date):
        return True
    return isinstance(value, str) and bool(DATE_RE.match(value))


def flatten(value: object, prefix: str = "") -> dict[str, object]:
    out: dict[str, object] = {}
    if isinstance(value, dict):
        for key, child in value.items():
            path = f"{prefix}.{key}" if prefix else str(key)
            if isinstance(child, dict):
                out.update(flatten(child, path))
            else:
                out[path] = child
    return out


def is_numericish(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, bool):
        return False
    if isinstance(value, (int, float)):
        return True
    if isinstance(value, list):
        return all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in value)
    return False


def relation_entries(value: object) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    if isinstance(value, dict):
        for rel, targets in value.items():
            if isinstance(targets, str):
                targets = [targets]
            if isinstance(targets, list):
                out.extend((str(rel), str(target)) for target in targets)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--report", default=None)
    args = ap.parse_args()
    root = pathlib.Path(args.root).resolve()
    errors: list[str] = []
    warnings: list[str] = []
    objects: dict[str, tuple[dict, str]] = {}
    ids: set[str] = set()
    title_paths: dict[str, str] = {}

    for path in sorted((root / "chip").rglob("*.md")):
        if path.name in EXCLUDED_NAMES:
            continue
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text, rel, errors)
        if not fm.get("vendor") or not fm.get("object_type") or fm.get("object_type") == "vendor-overview":
            continue
        node_id = pathlib.PurePosixPath(rel).with_suffix("").as_posix()
        objects[node_id] = (fm, text)
        ids.add(node_id)

    field_evidence_pages = 0
    page_evidence_pages = 0
    numeric_warnings = 0

    for node_id, (fm, text) in sorted(objects.items()):
        path = f"{node_id}.md"
        missing = sorted(REQUIRED - set(fm))
        if missing:
            errors.append(f"{path}: 缺少 Chip V0.2 字段 {', '.join(missing)}")
            continue
        if fm.get("schema_version") != "chip-v0.2":
            errors.append(f"{path}: schema_version 必须为 chip-v0.2")
        title = fm.get("title")
        vendor = fm.get("vendor")
        object_type = fm.get("object_type")
        if not isinstance(title, str) or not title.strip():
            errors.append(f"{path}: title 必须为非空字符串")
        else:
            folded = title.casefold().strip()
            if folded in title_paths:
                errors.append(f"{path}: title 与 {title_paths[folded]} 重复: {title}")
            else:
                title_paths[folded] = path
        if not isinstance(vendor, str) or not vendor.strip():
            errors.append(f"{path}: vendor 必须为非空字符串")
        if not isinstance(object_type, str) or not KEBAB_RE.match(object_type):
            errors.append(f"{path}: object_type 必须为 kebab-case")
        if fm.get("layer") not in LAYERS:
            errors.append(f"{path}: 非法 layer={fm.get('layer')!r}")
        if fm.get("status") not in STATUSES:
            errors.append(f"{path}: 非法 status={fm.get('status')!r}")
        if not valid_date(fm.get("updated")):
            errors.append(f"{path}: updated 必须为 YYYY-MM-DD")

        if fm.get("architecture") is not None and not isinstance(fm.get("architecture"), (str, dict)):
            errors.append(f"{path}: architecture 必须是字符串、mapping 或 null")
        if fm.get("process") is not None and not isinstance(fm.get("process"), (str, dict)):
            errors.append(f"{path}: process 必须是字符串、mapping 或 null")
        for key in ("memory", "compute", "interconnect", "power", "lifecycle", "relations", "evidence", "evidence_map"):
            if fm.get(key) is not None and not isinstance(fm.get(key), dict):
                errors.append(f"{path}: {key} 必须为 mapping 或 null")

        flat = {}
        for key in ("memory", "compute", "interconnect", "power", "lifecycle"):
            value = fm.get(key)
            if isinstance(value, dict):
                flat.update(flatten(value, key))
        for field_path, value in flat.items():
            leaf = field_path.rsplit(".", 1)[-1]
            if leaf.endswith(NUMERIC_SUFFIXES) and not is_numericish(value):
                numeric_warnings += 1
                warnings.append(f"{path}: {field_path} 应为 number/list[number]/null，当前={value!r}")

        layer = fm.get("layer")
        if layer == "chip":
            illegal = sorted(AGGREGATE_KEYS_FOR_CHIP & set(fm))
            if illegal:
                errors.append(f"{path}: chip 层出现系统/机架聚合字段 {', '.join(illegal)}")
            power = fm.get("power")
            if isinstance(power, dict) and power.get("scope") in {"system", "rack", "cluster"}:
                errors.append(f"{path}: chip 层 power.scope 不能是 {power.get('scope')!r}")

        source_sec = section(text, "直接来源")
        direct_urls = {url.rstrip(".,;，；") for url in URL_RE.findall(source_sec)}
        if not direct_urls:
            errors.append(f"{path}: ## 直接来源 至少需要一个 http(s) URL")

        evidence = fm.get("evidence")
        evidence_ids: set[str] = set()
        if not isinstance(evidence, dict) or not evidence:
            errors.append(f"{path}: evidence 必须至少包含一个 Source ID")
        else:
            for evidence_id, meta in evidence.items():
                evidence_id = str(evidence_id)
                if not ID_RE.match(evidence_id):
                    errors.append(f"{path}: 非法 Evidence ID {evidence_id!r}")
                evidence_ids.add(evidence_id)
                if not isinstance(meta, dict):
                    errors.append(f"{path}: evidence.{evidence_id} 必须为 mapping")
                    continue
                url = meta.get("url")
                if not valid_url(url):
                    errors.append(f"{path}: evidence.{evidence_id}.url 必须为 http(s) URL")
                elif url not in direct_urls:
                    errors.append(f"{path}: evidence.{evidence_id}.url 未出现在 ## 直接来源")
                st = meta.get("source_type")
                if st is not None and st not in SOURCE_TYPES:
                    errors.append(f"{path}: evidence.{evidence_id}.source_type 非法: {st!r}")
                accessed = meta.get("accessed")
                if accessed is not None and not valid_date(accessed):
                    errors.append(f"{path}: evidence.{evidence_id}.accessed 必须为 YYYY-MM-DD")

        evidence_map = fm.get("evidence_map")
        explicit_fields = 0
        if not isinstance(evidence_map, dict) or "__page__" not in evidence_map:
            errors.append(f"{path}: evidence_map 必须包含 __page__")
        else:
            page_refs = evidence_map.get("__page__")
            if not isinstance(page_refs, list) or not page_refs:
                errors.append(f"{path}: evidence_map.__page__ 必须是非空 Source ID 列表")
            else:
                page_evidence_pages += 1
            for field_path, refs in evidence_map.items():
                if not isinstance(refs, list) or not refs:
                    errors.append(f"{path}: evidence_map.{field_path} 必须是非空 Source ID 列表")
                    continue
                for ref in refs:
                    if str(ref) not in evidence_ids:
                        errors.append(f"{path}: evidence_map.{field_path} 引用了未定义 Evidence ID {ref!r}")
                if field_path != "__page__":
                    explicit_fields += 1
                    if field_path not in flat and not field_path.startswith(("architecture", "process")):
                        warnings.append(f"{path}: evidence_map 字段路径当前无法在事实块定位: {field_path}")
            if explicit_fields:
                field_evidence_pages += 1

        relations = fm.get("relations")
        for relation, target in relation_entries(relations):
            if relation not in RELATIONS:
                errors.append(f"{path}: 非法 chip relation={relation!r}")
            if target == node_id:
                errors.append(f"{path}: relation 不能指向自身")
            elif target not in ids:
                errors.append(f"{path}: relation 目标不存在: {target}")

    summary = {
        "schema_version": "chip-v0.2",
        "objects": len(objects),
        "page_evidence_pages": page_evidence_pages,
        "field_evidence_pages": field_evidence_pages,
        "numeric_type_warnings": numeric_warnings,
        "errors": errors,
        "warnings": warnings,
    }
    if args.report:
        report = root / args.report
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"chip_objects={len(objects)} page_evidence={page_evidence_pages} field_evidence={field_evidence_pages} errors={len(errors)} warnings={len(warnings)}")
    for msg in errors:
        print(f"ERROR: {msg}")
    for msg in warnings:
        print(f"WARN: {msg}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
