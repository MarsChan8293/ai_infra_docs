#!/usr/bin/env python3
"""Build the AI Infra knowledge graph from Markdown + YAML frontmatter."""
from __future__ import annotations

import argparse
import json
import pathlib
import re
from collections import defaultdict

import yaml

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+\.md(?:#[^)]+)?)\)")
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)
URL_RE = re.compile(r"https?://[^\s)>]+")
EVIDENCE_REF_RE = re.compile(r"\[(S\d+)\]")
EVIDENCE_DEF_RE = re.compile(r"^\s*-\s*\[(S\d+)\]\s+(https?://\S+)\s*$", re.M)
EXCLUDED_DIRS = {".git", ".github", ".obsidian", ".codex", "generated", "scripts", "node_modules"}
GENERIC_RELATIONS = {"wikilink", "navigation", "vendor-chip", "concept-link", "cross-domain"}


def link_scan_text(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", "", text)
    return text


def strip_md(value: str) -> str:
    value = value.strip().replace("\\", "/")
    value = value.split("#", 1)[0].strip()
    if value.endswith(".md"):
        value = value[:-3]
    return value.strip("/")


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    try:
        value = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError:
        return {}
    return value if isinstance(value, dict) else {}


def section(text: str, heading: str) -> str:
    match = re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.M)
    if not match:
        return ""
    start = match.end()
    nxt = re.search(r"^##\s+", text[start:], re.M)
    end = start + nxt.start() if nxt else len(text)
    return text[start:end]


def extract_sources(text: str) -> list[dict]:
    sec = section(text, "直接来源")
    explicit = {m.group(1): m.group(2) for m in EVIDENCE_DEF_RE.finditer(sec)}
    if explicit:
        return [{"id": k, "url": v, "explicit": True} for k, v in sorted(explicit.items())]
    return [{"id": f"S{i}", "url": url, "explicit": False} for i, url in enumerate(URL_RE.findall(sec), 1)]


def claim_evidence_ids(text: str) -> list[str]:
    return sorted(set(EVIDENCE_REF_RE.findall(section(text, "核心能力"))))


def relation_entries(value: object) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    if isinstance(value, dict):
        for rel, targets in value.items():
            if isinstance(targets, str):
                targets = [targets]
            if isinstance(targets, list):
                out.extend((str(rel), str(t)) for t in targets)
    elif isinstance(value, list):
        for item in value:
            if isinstance(item, dict) and "type" in item and "target" in item:
                out.append((str(item["type"]), str(item["target"])))
    return out


def node_domain(rel: pathlib.PurePosixPath) -> str:
    if not rel.parts:
        return "root"
    return rel.parts[0] if rel.parts[0] in {"chip", "software", "models"} else "root"


def node_kind(rel: pathlib.PurePosixPath, fm: dict) -> str:
    object_type = fm.get("object_type")
    if rel.parts[:2] == ("software", "projects") and object_type == "project":
        return str(fm.get("category") or "project")
    if rel.parts[:2] == ("software", "concepts") or object_type == "concept":
        return "concept"
    tags = fm.get("tags") or []
    if isinstance(tags, str):
        tags = [tags]
    tags = {str(tag).casefold() for tag in tags}
    stem = rel.stem.casefold()
    if "moc" in tags or stem in {"readme", "00-ai-infra-map", "00-project-index"}:
        return "moc"
    if rel.parts and rel.parts[0] == "chip":
        if stem.endswith("overview") or "概览" in rel.stem:
            return "vendor"
        if len(rel.parts) >= 3:
            return "chip"
        return "hardware-note"
    if rel.parts and rel.parts[0] == "software":
        return rel.parts[1].replace("_", "-") if len(rel.parts) >= 3 else "software"
    if rel.parts and rel.parts[0] == "models":
        return "model"
    return "note"


def display_name(rel: pathlib.PurePosixPath, text: str, fm: dict) -> str:
    for key in ("name", "title"):
        value = fm.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    match = H1_RE.search(text)
    return match.group(1).strip() if match else rel.stem


def markdown_files(root: pathlib.Path) -> list[pathlib.Path]:
    items = []
    for path in root.rglob("*.md"):
        rel = path.relative_to(root)
        if any(part in EXCLUDED_DIRS for part in rel.parts[:-1]):
            continue
        items.append(path)
    return sorted(items)


def resolve_target(target: str, source_id: str, ids: set[str], by_basename: dict[str, list[str]]) -> tuple[str | None, str | None]:
    raw = strip_md(target)
    if not raw:
        return None, "empty"
    if raw in ids:
        return raw, None
    relative = strip_md(str(pathlib.PurePosixPath(source_id).parent / raw))
    if relative in ids:
        return relative, None
    candidates = list(dict.fromkeys(by_basename.get(pathlib.PurePosixPath(raw).name.casefold(), [])))
    if len(candidates) == 1:
        return candidates[0], None
    if len(candidates) > 1:
        return None, "ambiguous"
    return None, "missing"


def classify_edge(source: dict, target: dict) -> str:
    if source["domain"] != target["domain"]:
        return "cross-domain"
    if "concept" in {source["kind"], target["kind"]}:
        return "concept-link"
    if "moc" in {source["kind"], target["kind"]}:
        return "navigation"
    if source["kind"] == "vendor" and target["kind"] == "chip":
        return "vendor-chip"
    if source["kind"] == "chip" and target["kind"] == "vendor":
        return "vendor-chip"
    return "wikilink"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--output", default="generated")
    args = ap.parse_args()
    root = pathlib.Path(args.root).resolve()
    output = root / args.output
    output.mkdir(parents=True, exist_ok=True)

    records: dict[str, dict] = {}
    texts: dict[str, str] = {}
    by_basename: dict[str, list[str]] = defaultdict(list)
    project_by_slug: dict[str, str] = {}

    for path in markdown_files(root):
        rel = pathlib.PurePosixPath(path.relative_to(root).as_posix())
        node_id = rel.with_suffix("").as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text)
        node = {
            "id": node_id,
            "path": rel.as_posix(),
            "name": display_name(rel, text, fm),
            "domain": node_domain(rel),
            "kind": node_kind(rel, fm),
            "frontmatter": fm,
            "sources": extract_sources(text),
            "claim_evidence_ids": claim_evidence_ids(text),
        }
        node["evidence_level"] = "claim" if node["claim_evidence_ids"] else ("page" if node["sources"] else "none")
        records[node_id] = node
        texts[node_id] = text
        by_basename[rel.stem.casefold()].append(node_id)
        if rel.parts[:2] == ("software", "projects"):
            project_by_slug[rel.stem] = node_id
        aliases = fm.get("aliases") or []
        if isinstance(aliases, str):
            aliases = [aliases]
        if isinstance(aliases, list):
            for alias in aliases:
                by_basename[str(alias).casefold()].append(node_id)

    ids = set(records)
    edge_map: dict[tuple[str, str, str], dict] = {}
    unresolved = []

    def add_edge(source: str, target: str, relation: str, syntax: str) -> None:
        key = (source, target, relation)
        edge = edge_map.setdefault(key, {"source": source, "target": target, "syntaxes": [], "relation": relation})
        if syntax not in edge["syntaxes"]:
            edge["syntaxes"].append(syntax)

    for source_id, text in texts.items():
        scan = link_scan_text(text)
        for match in WIKILINK_RE.finditer(scan):
            target = match.group(1).split("|", 1)[0].strip()
            target_id, reason = resolve_target(target, source_id, ids, by_basename)
            if target_id is None:
                unresolved.append({"source": source_id, "target": target, "reason": reason, "syntax": "wikilink"})
            elif target_id != source_id:
                add_edge(source_id, target_id, classify_edge(records[source_id], records[target_id]), "wikilink")
        for match in MD_LINK_RE.finditer(scan):
            target = match.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            target_id, reason = resolve_target(target, source_id, ids, by_basename)
            if target_id is None:
                unresolved.append({"source": source_id, "target": target, "reason": reason, "syntax": "markdown-link"})
            elif target_id != source_id:
                add_edge(source_id, target_id, classify_edge(records[source_id], records[target_id]), "markdown-link")

    for source_id, node in records.items():
        if not source_id.startswith("software/projects/"):
            continue
        fm = node["frontmatter"]
        typed: list[tuple[str, str]] = []
        integrations = fm.get("integrations") or []
        if isinstance(integrations, list):
            typed.extend(("integrates-with", str(t)) for t in integrations)
        typed.extend(relation_entries(fm.get("relations")))
        for relation, slug in typed:
            target_id = project_by_slug.get(slug)
            if not target_id or target_id == source_id:
                continue
            for key in list(edge_map):
                if key[0] == source_id and key[1] == target_id and key[2] in GENERIC_RELATIONS:
                    del edge_map[key]
            add_edge(source_id, target_id, relation, "frontmatter")

    edges = sorted(edge_map.values(), key=lambda e: (e["source"], e["target"], e["relation"]))
    incoming = defaultdict(int)
    outgoing = defaultdict(int)
    cross = defaultdict(int)
    neighbors: dict[str, set[str]] = defaultdict(set)
    backlinks: dict[str, set[str]] = defaultdict(set)
    for edge in edges:
        outgoing[edge["source"]] += 1
        incoming[edge["target"]] += 1
        neighbors[edge["source"]].add(edge["target"])
        neighbors[edge["target"]].add(edge["source"])
        backlinks[edge["target"]].add(edge["source"])
        if edge["relation"] == "cross-domain":
            cross[edge["source"]] += 1
            cross[edge["target"]] += 1

    metrics = {}
    nodes = []
    for node_id, node in sorted(records.items()):
        degree = len(neighbors[node_id])
        metric = {
            "degree": degree,
            "incoming": incoming[node_id],
            "outgoing": outgoing[node_id],
            "cross_domain": cross[node_id],
            "bridge_score": degree + 3 * cross[node_id],
        }
        metrics[node_id] = metric
        nodes.append({**node, **metric, "backlinks": sorted(backlinks[node_id])})

    (output / "nodes.json").write_text(json.dumps(nodes, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    (output / "edges.json").write_text(json.dumps(edges, ensure_ascii=False, indent=2), encoding="utf-8")
    (output / "metrics.json").write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8")
    (output / "unresolved-links.json").write_text(json.dumps(unresolved, ensure_ascii=False, indent=2), encoding="utf-8")

    domains = defaultdict(int)
    kinds = defaultdict(int)
    relations = defaultdict(int)
    evidence = defaultdict(int)
    isolated = []
    for node in nodes:
        domains[node["domain"]] += 1
        kinds[node["kind"]] += 1
        evidence[node["evidence_level"]] += 1
        if node["degree"] == 0:
            isolated.append(node["id"])
    for edge in edges:
        relations[edge["relation"]] += 1

    top_nodes = sorted(nodes, key=lambda n: (n["bridge_score"], n["degree"]), reverse=True)[:25]
    summary = [
        "---", "title: AI Infra 知识图谱构建报告", "tags:", "  - generated", "  - knowledge-graph", "---", "",
        "# AI Infra 知识图谱构建报告", "",
        f"- 节点数：**{len(nodes)}**", f"- 有向边数：**{len(edges)}**", f"- 未解析内部链接：**{len(unresolved)}**", f"- 孤立节点：**{len(isolated)}**", "",
        "## 按领域", "",
    ]
    for key, value in sorted(domains.items()):
        summary.append(f"- `{key}`：{value}")
    summary.extend(["", "## 按节点类型", ""])
    for key, value in sorted(kinds.items(), key=lambda x: (-x[1], x[0])):
        summary.append(f"- `{key}`：{value}")
    summary.extend(["", "## 按关系类型", ""])
    for key, value in sorted(relations.items(), key=lambda x: (-x[1], x[0])):
        summary.append(f"- `{key}`：{value}")
    summary.extend(["", "## Evidence coverage", ""])
    for key, value in sorted(evidence.items()):
        summary.append(f"- `{key}`：{value}")
    summary.extend(["", "## 高连接度 / 桥接节点", "", "| 节点 | Degree | Cross-domain | Bridge score |", "| --- | ---: | ---: | ---: |"])
    for node in top_nodes:
        summary.append(f"| `[[{node['id']}|{node['name']}]]` | {node['degree']} | {node['cross_domain']} | {node['bridge_score']} |")
    summary.extend(["", "## 说明", "", "该报告由 `scripts/build-knowledge-graph.py` 自动生成；Markdown/YAML 仍是唯一事实源。", ""])
    (output / "graph-summary.md").write_text("\n".join(summary), encoding="utf-8")

    print(f"nodes={len(nodes)} edges={len(edges)} unresolved={len(unresolved)} isolated={len(isolated)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
