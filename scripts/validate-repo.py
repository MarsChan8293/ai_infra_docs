#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
from collections import defaultdict
from urllib.parse import urlparse

import yaml

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
EVIDENCE_REF_RE = re.compile(r"\[(S\d+)\]")
EVIDENCE_DEF_RE = re.compile(r"^\s*-\s*\[(S\d+)\]\s+(https?://\S+)\s*$", re.M)
URL_RE = re.compile(r"https?://[^\s)>]+")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

EXCLUDED_DIRS = {".git", ".github", ".obsidian", ".codex", "generated", "node_modules"}
MODEL_STATUSES = {"preview", "released", "deprecated", "retired", "unknown"}
MODEL_MODALITIES = {"text", "image", "audio", "video"}
SYSTEM_RELATED_LAYERS = {
    "model", "workload", "compute", "memory", "parallelism", "communication",
    "topology", "scheduling", "accelerator", "network", "storage", "power", "reliability",
}
SOURCE_ID_RE = re.compile(r"^S\d+$")
KEBAB_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
STRICT_ROOT_NODES = {"README", "00-ai-infra-map", "AGENTS", "ROADMAP", "TASKS"}


def markdown_files(root: pathlib.Path) -> list[pathlib.Path]:
    out = []
    for path in root.rglob("*.md"):
        rel = path.relative_to(root)
        if any(part in EXCLUDED_DIRS for part in rel.parts[:-1]):
            continue
        out.append(path)
    return sorted(out)


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


def link_scan_text(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def strip_md(value: str) -> str:
    value = value.strip().replace("\\", "/").split("#", 1)[0].strip()
    if value.endswith(".md"):
        value = value[:-3]
    return value.strip("/")


def valid_url(value: object) -> bool:
    if value is None:
        return True
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def valid_date(value: object, *, allow_null: bool = False) -> bool:
    if value is None:
        return allow_null
    if isinstance(value, dt.date):
        return True
    return isinstance(value, str) and bool(DATE_RE.match(value))


def section(text: str, heading: str) -> str:
    match = re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.M)
    if not match:
        return ""
    start = match.end()
    nxt = re.search(r"^##\s+", text[start:], re.M)
    end = start + nxt.start() if nxt else len(text)
    return text[start:end]


def evidence_info(text: str, headings: tuple[str, ...]) -> tuple[set[str], dict[str, str], list[str]]:
    refs: set[str] = set()
    for heading in headings:
        refs.update(EVIDENCE_REF_RE.findall(section(text, heading)))
    source_sec = section(text, "直接来源")
    defs = {m.group(1): m.group(2) for m in EVIDENCE_DEF_RE.finditer(source_sec)}
    urls = URL_RE.findall(source_sec)
    return refs, defs, urls


def int_or_null(value: object) -> bool:
    return value is None or (isinstance(value, int) and not isinstance(value, bool) and value >= 0)


def nonempty_string_list(value: object) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(isinstance(item, str) and bool(item.strip()) for item in value)
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--report", default=None)
    args = ap.parse_args()

    root = pathlib.Path(args.root).resolve()
    errors: list[str] = []
    warnings: list[str] = []
    records: dict[str, dict] = {}
    texts: dict[str, str] = {}
    by_basename: dict[str, list[str]] = defaultdict(list)

    for path in markdown_files(root):
        rel = pathlib.PurePosixPath(path.relative_to(root).as_posix())
        node_id = rel.with_suffix("").as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text, rel.as_posix(), errors)
        records[node_id] = {"path": rel, "frontmatter": fm}
        texts[node_id] = text
        by_basename[rel.stem.casefold()].append(node_id)
        aliases = fm.get("aliases") or []
        if isinstance(aliases, str):
            aliases = [aliases]
        if isinstance(aliases, list):
            for alias in aliases:
                by_basename[str(alias).casefold()].append(node_id)

    system_concepts = {
        node_id: rec for node_id, rec in records.items()
        if rec["path"].parts and rec["path"].parts[0] == "system"
        and rec["frontmatter"].get("object_type") == "concept"
    }
    system_names: dict[str, str] = {}
    system_required = {
        "schema_version", "name", "object_type", "category", "inputs", "constraints",
        "outputs", "assumptions", "related_layers", "evidence", "updated",
    }
    for node_id, rec in sorted(system_concepts.items()):
        path = rec["path"].as_posix()
        fm = rec["frontmatter"]
        text = texts[node_id]
        missing = sorted(system_required - set(fm))
        if missing:
            errors.append(f"{path}: 缺少 System Concept 字段 {', '.join(missing)}")
            continue
        if fm.get("schema_version") != "system-v0.1":
            errors.append(f"{path}: schema_version 必须为 system-v0.1")
        if fm.get("object_type") != "concept":
            errors.append(f"{path}: object_type 必须为 concept")

        name = fm.get("name")
        if not isinstance(name, str) or not name.strip():
            errors.append(f"{path}: name 必须为非空字符串")
        elif name.casefold() in system_names:
            errors.append(f"{path}: system concept name 与 {system_names[name.casefold()]} 重复: {name}")
        else:
            system_names[name.casefold()] = path

        category = fm.get("category")
        if not isinstance(category, str) or not KEBAB_RE.fullmatch(category):
            errors.append(f"{path}: category 必须为非空 kebab-case 字符串")

        for field in ("inputs", "constraints", "outputs"):
            if not nonempty_string_list(fm.get(field)):
                errors.append(f"{path}: {field} 必须是非空字符串 list")

        assumptions = fm.get("assumptions")
        if not isinstance(assumptions, list):
            errors.append(f"{path}: assumptions 必须是 list")
        else:
            for i, item in enumerate(assumptions):
                if isinstance(item, str):
                    if not item.strip():
                        errors.append(f"{path}: assumptions[{i}] 不能为空字符串")
                elif isinstance(item, dict):
                    if not isinstance(item.get("name"), str) or not item["name"].strip():
                        errors.append(f"{path}: assumptions[{i}].name 必须为非空字符串")
                else:
                    errors.append(f"{path}: assumptions[{i}] 必须是字符串或 mapping")

        related_layers = fm.get("related_layers")
        if not nonempty_string_list(related_layers):
            errors.append(f"{path}: related_layers 必须是非空字符串 list")
        else:
            invalid_layers = sorted(set(related_layers) - SYSTEM_RELATED_LAYERS)
            if invalid_layers:
                errors.append(f"{path}: 非法 related_layers: {', '.join(invalid_layers)}")

        evidence = fm.get("evidence")
        evidence_ids: set[str] = set()
        if not isinstance(evidence, dict):
            errors.append(f"{path}: evidence 必须是 mapping")
        else:
            for source_id, source in evidence.items():
                source_id = str(source_id)
                evidence_ids.add(source_id)
                if not SOURCE_ID_RE.fullmatch(source_id):
                    errors.append(f"{path}: 非法 System Evidence ID {source_id!r}")
                if not isinstance(source, dict):
                    errors.append(f"{path}: evidence.{source_id} 必须是 mapping")
                    continue
                if not valid_url(source.get("url")) or source.get("url") is None:
                    errors.append(f"{path}: evidence.{source_id}.url 必须是 http(s) URL")
                if "source_type" in source and (
                    not isinstance(source.get("source_type"), str) or not source["source_type"].strip()
                ):
                    errors.append(f"{path}: evidence.{source_id}.source_type 必须为非空字符串")
                if "accessed" in source and not valid_date(source.get("accessed")):
                    errors.append(f"{path}: evidence.{source_id}.accessed 必须是 YYYY-MM-DD")

        claim_refs = set(EVIDENCE_REF_RE.findall(link_scan_text(text)))
        missing_evidence = sorted(claim_refs - evidence_ids)
        if missing_evidence:
            errors.append(f"{path}: 未定义 System Evidence ID: {', '.join(missing_evidence)}")
        unused_evidence = sorted(evidence_ids - claim_refs)
        if unused_evidence:
            warnings.append(f"{path}: 未使用 System Evidence ID: {', '.join(unused_evidence)}")

        if not valid_date(fm.get("updated")):
            errors.append(f"{path}: updated 必须是 YYYY-MM-DD")

    models = {
        node_id: rec for node_id, rec in records.items()
        if rec["path"].parts and rec["path"].parts[0] == "models"
        and rec["frontmatter"].get("object_type") == "model"
    }
    model_names: dict[str, str] = {}
    model_page_evidence = 0
    model_claim_evidence = 0
    model_required = {
        "schema_version", "name", "object_type", "organization", "family", "status",
        "release_date", "architecture", "parameters", "context_length",
        "kv_cache_64k_fp8_bytes", "modalities", "weights", "snapshot", "updated",
    }

    for node_id, rec in sorted(models.items()):
        path = rec["path"].as_posix()
        fm = rec["frontmatter"]
        text = texts[node_id]
        missing = sorted(model_required - set(fm))
        if missing:
            errors.append(f"{path}: 缺少 Model 字段 {', '.join(missing)}")
            continue
        if fm.get("schema_version") != "model-v0.1":
            errors.append(f"{path}: schema_version 必须为 model-v0.1")
        if fm.get("object_type") != "model":
            errors.append(f"{path}: object_type 必须为 model")
        if not isinstance(fm.get("organization"), str) or not fm["organization"].strip():
            errors.append(f"{path}: organization 必须为非空字符串")
        if fm.get("family") is not None and not isinstance(fm.get("family"), str):
            errors.append(f"{path}: family 必须为字符串或 null")
        if fm.get("status") not in MODEL_STATUSES:
            errors.append(f"{path}: 非法 model status={fm.get('status')!r}")
        if not valid_date(fm.get("release_date"), allow_null=True):
            errors.append(f"{path}: release_date 必须为 YYYY-MM-DD 或 null")

        architecture = fm.get("architecture")
        if not isinstance(architecture, dict):
            errors.append(f"{path}: architecture 必须是 mapping")
        else:
            for key in ("backbone", "sparsity", "attention"):
                if key not in architecture:
                    errors.append(f"{path}: architecture 缺少 {key}")
                elif architecture[key] is not None and not isinstance(architecture[key], str):
                    errors.append(f"{path}: architecture.{key} 必须为字符串或 null")

        parameters = fm.get("parameters")
        if not isinstance(parameters, dict):
            errors.append(f"{path}: parameters 必须是 mapping")
        else:
            for key in ("total", "active"):
                if key not in parameters:
                    errors.append(f"{path}: parameters 缺少 {key}")
                elif not int_or_null(parameters[key]):
                    errors.append(f"{path}: parameters.{key} 必须为非负整数或 null")

        context_length = fm.get("context_length")
        cache_bytes = fm.get("kv_cache_64k_fp8_bytes")
        if not int_or_null(context_length):
            errors.append(f"{path}: context_length 必须为非负整数或 null")
        if not int_or_null(cache_bytes):
            errors.append(f"{path}: kv_cache_64k_fp8_bytes 必须为非负整数或 null")
        if isinstance(cache_bytes, int) and cache_bytes > 0 and isinstance(context_length, int) and context_length < 65536:
            errors.append(f"{path}: context_length < 64K 时不能填写 64K KV cache 派生值")

        modalities = fm.get("modalities")
        if not isinstance(modalities, list) or not modalities:
            errors.append(f"{path}: modalities 必须是非空 list")
        else:
            for item in modalities:
                if item not in MODEL_MODALITIES:
                    errors.append(f"{path}: 非法 modality={item!r}")
        if not valid_url(fm.get("weights")):
            errors.append(f"{path}: weights 必须为 http(s) URL 或 null")

        snapshot = fm.get("snapshot")
        if not isinstance(snapshot, dict):
            errors.append(f"{path}: snapshot 必须是 mapping")
        else:
            if "revision" not in snapshot:
                errors.append(f"{path}: snapshot 缺少 revision")
            if not valid_date(snapshot.get("as_of")):
                errors.append(f"{path}: snapshot.as_of 必须是 YYYY-MM-DD")
        if not valid_date(fm.get("updated")):
            errors.append(f"{path}: updated 必须是 YYYY-MM-DD")

        name = str(fm.get("name", "")).strip()
        if not name:
            errors.append(f"{path}: name 不能为空")
        elif name.casefold() in model_names:
            errors.append(f"{path}: model name 与 {model_names[name.casefold()]} 重复: {name}")
        else:
            model_names[name.casefold()] = path

        refs, defs, urls = evidence_info(text, ("核心规格", "架构特征", "AI Infra 关注点"))
        if urls:
            model_page_evidence += 1
        else:
            errors.append(f"{path}: ## 直接来源 至少需要一个 http(s) URL")
        if not refs:
            errors.append(f"{path}: Model V0.1 必须使用 [S1] claim-level evidence")
        if not defs:
            errors.append(f"{path}: Model V0.1 的 ## 直接来源 必须定义 [S1] 形式 Evidence")
        else:
            missing_defs = sorted(refs - set(defs))
            if missing_defs:
                errors.append(f"{path}: 未定义模型证据 ID: {', '.join(missing_defs)}")
            unused_defs = sorted(set(defs) - refs)
            if unused_defs:
                warnings.append(f"{path}: 未使用模型证据 ID: {', '.join(unused_defs)}")
            if refs:
                model_claim_evidence += 1

    ids = set(records)
    incoming = defaultdict(int)
    unresolved = []
    for source_id, text in texts.items():
        scan = link_scan_text(text)
        for match in WIKILINK_RE.finditer(scan):
            raw = strip_md(match.group(1).split("|", 1)[0])
            if not raw:
                continue
            if raw in ids:
                incoming[raw] += 1
                continue
            relative = strip_md(str(pathlib.PurePosixPath(source_id).parent / raw))
            if relative in ids:
                incoming[relative] += 1
                continue
            candidates = list(dict.fromkeys(by_basename.get(pathlib.PurePosixPath(raw).name.casefold(), [])))
            if len(candidates) == 1:
                incoming[candidates[0]] += 1
                continue
            strict = source_id.startswith(("system/", "models/")) or source_id in STRICT_ROOT_NODES
            if strict:
                unresolved.append({
                    "source": source_id,
                    "target": raw,
                    "reason": "ambiguous" if candidates else "missing",
                })

    for item in unresolved:
        errors.append(f"{item['source']}: unresolved Wiki Link -> {item['target']} ({item['reason']})")
    for node_id in system_concepts:
        if incoming[node_id] == 0:
            warnings.append(f"{node_id}: System Concept 没有任何内部入边，可能是孤岛节点")
    for node_id in models:
        if incoming[node_id] == 0:
            warnings.append(f"{node_id}: Model 没有任何内部入边，可能是孤岛节点")

    summary = {
        "system_concepts": len(system_concepts),
        "models": len(models),
        "model_page_evidence": model_page_evidence,
        "model_claim_evidence": model_claim_evidence,
        "errors": errors,
        "warnings": warnings,
    }
    if args.report:
        report = root / args.report
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print(
        "system_concepts={} models={} model_page_evidence={} model_claim_evidence={} errors={} warnings={}".format(
            len(system_concepts), len(models), model_page_evidence, model_claim_evidence,
            len(errors), len(warnings)
        )
    )
    for msg in errors:
        print(f"ERROR: {msg}")
    for msg in warnings:
        print(f"WARN: {msg}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
