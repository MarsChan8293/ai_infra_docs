#!/usr/bin/env python3
"""Build a lightweight knowledge graph from repository Markdown.

The graph is intentionally source-driven: Markdown files are nodes and
Obsidian wiki links / local Markdown links are edges. No third-party Python
packages are required, so the script can run in GitHub Actions and locally.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
from collections import defaultdict

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+\.md(?:#[^)]+)?)\)")
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)

EXCLUDED_DIRS = {
    ".git",
    ".github",
    ".obsidian",
    ".codex",
    "generated",
    "scripts",
    "node_modules",
}


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
    block = text[4:end].splitlines()
    result: dict[str, object] = {}
    current_list: str | None = None
    for raw in block:
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if re.match(r"^\s+-\s+", line) and current_list:
            result.setdefault(current_list, [])
            assert isinstance(result[current_list], list)
            result[current_list].append(re.sub(r"^\s+-\s+", "", line).strip().strip("'\""))
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not match:
            continue
        key, value = match.group(1), match.group(2).strip()
        current_list = None
        if value == "":
            result[key] = []
            current_list = key
        elif value.startswith("[") and value.endswith("]"):
            items = [item.strip().strip("'\"") for item in value[1:-1].split(",") if item.strip()]
            result[key] = items
        else:
            result[key] = value.strip("'\"")
    return result


def node_domain(rel: pathlib.PurePosixPath) -> str:
    if not rel.parts:
        return "root"
    if rel.parts[0] in {"chip", "software", "models"}:
        return rel.parts[0]
    return "root"


def node_kind(rel: pathlib.PurePosixPath, frontmatter: dict) -> str:
    tags = frontmatter.get("tags") or []
    if isinstance(tags, str):
        tags = [tags]
    tags = {str(tag).casefold() for tag in tags}
    stem = rel.stem.casefold()

    if "moc" in tags or stem in {"readme", "00-ai-infra-map", "00-project-index"}:
        return "moc"
    if "concept" in tags or "concepts" in rel.parts:
        return "concept"
    if rel.parts and rel.parts[0] == "chip":
        if stem.endswith("overview") or "概览" in rel.stem:
            return "vendor"
        if len(rel.parts) >= 3:
            return "chip"
        return "hardware-note"
    if rel.parts and rel.parts[0] == "software":
        if len(rel.parts) >= 3:
            return rel.parts[1].replace("_", "-")
        return "software"
    if rel.parts and rel.parts[0] == "models":
        return "model"
    return "note"


def display_name(rel: pathlib.PurePosixPath, text: str, frontmatter: dict) -> str:
    title = frontmatter.get("title")
    if isinstance(title, str) and title.strip():
        return title.strip()
    match = H1_RE.search(text)
    if match:
        return match.group(1).strip()
    return rel.stem


def markdown_files(root: pathlib.Path) -> list[pathlib.Path]:
    items = []
    for path in root.rglob("*.md"):
        rel = path.relative_to(root)
        if any(part in EXCLUDED_DIRS for part in rel.parts[:-1]):
            continue
        items.append(path)
    return sorted(items)


def resolve_target(
    target: str,
    source_id: str,
    ids: set[str],
    by_basename: dict[str, list[str]],
) -> tuple[str | None, str | None]:
    raw = strip_md(target)
    if not raw:
        return None, "empty"

    candidates: list[str] = []
    if raw in ids:
        candidates.append(raw)

    source_parent = pathlib.PurePosixPath(source_id).parent
    relative = strip_md(str(source_parent / raw))
    if relative in ids and relative not in candidates:
        candidates.append(relative)

    basename = pathlib.PurePosixPath(raw).name
    for item in by_basename.get(basename.casefold(), []):
        if item not in candidates:
            candidates.append(item)

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
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output", default="generated")
    args = parser.parse_args()

    root = pathlib.Path(args.root).resolve()
    output = root / args.output
    output.mkdir(parents=True, exist_ok=True)

    files = markdown_files(root)
    records: dict[str, dict] = {}
    texts: dict[str, str] = {}
    by_basename: dict[str, list[str]] = defaultdict(list)

    for path in files:
        rel = pathlib.PurePosixPath(path.relative_to(root).as_posix())
        node_id = rel.with_suffix("").as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        frontmatter = parse_frontmatter(text)
        node = {
            "id": node_id,
            "path": rel.as_posix(),
            "name": display_name(rel, text, frontmatter),
            "domain": node_domain(rel),
            "kind": node_kind(rel, frontmatter),
            "frontmatter": frontmatter,
        }
        records[node_id] = node
        texts[node_id] = text
        by_basename[rel.stem.casefold()].append(node_id)
        aliases = frontmatter.get("aliases") or []
        if isinstance(aliases, str):
            aliases = [aliases]
        for alias in aliases:
            by_basename[str(alias).casefold()].append(node_id)

    ids = set(records)
    edge_map: dict[tuple[str, str], dict] = {}
    unresolved = []

    for source_id, text in texts.items():
        raw_targets: list[tuple[str, str]] = []
        for match in WIKILINK_RE.finditer(text):
            body = match.group(1).strip()
            target = body.split("|", 1)[0].strip()
            raw_targets.append((target, "wikilink"))
        for match in MD_LINK_RE.finditer(text):
            raw_targets.append((match.group(1).strip(), "markdown-link"))

        for raw_target, syntax in raw_targets:
            if raw_target.startswith(("http://", "https://", "mailto:")):
                continue
            target_id, reason = resolve_target(raw_target, source_id, ids, by_basename)
            if target_id is None:
                unresolved.append({
                    "source": source_id,
                    "target": raw_target,
                    "reason": reason,
                    "syntax": syntax,
                })
                continue
            if target_id == source_id:
                continue
            pair = (source_id, target_id)
            edge = edge_map.setdefault(pair, {
                "source": source_id,
                "target": target_id,
                "syntaxes": [],
                "relation": classify_edge(records[source_id], records[target_id]),
            })
            if syntax not in edge["syntaxes"]:
                edge["syntaxes"].append(syntax)

    edges = sorted(edge_map.values(), key=lambda e: (e["source"], e["target"]))

    incoming = defaultdict(int)
    outgoing = defaultdict(int)
    cross = defaultdict(int)
    neighbors: dict[str, set[str]] = defaultdict(set)
    for edge in edges:
        outgoing[edge["source"]] += 1
        incoming[edge["target"]] += 1
        neighbors[edge["source"]].add(edge["target"])
        neighbors[edge["target"]].add(edge["source"])
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
        nodes.append({**node, **metric})

    (output / "nodes.json").write_text(json.dumps(nodes, ensure_ascii=False, indent=2), encoding="utf-8")
    (output / "edges.json").write_text(json.dumps(edges, ensure_ascii=False, indent=2), encoding="utf-8")
    (output / "metrics.json").write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8")
    (output / "unresolved-links.json").write_text(json.dumps(unresolved, ensure_ascii=False, indent=2), encoding="utf-8")

    domains = defaultdict(int)
    kinds = defaultdict(int)
    relations = defaultdict(int)
    isolated = []
    for node in nodes:
        domains[node["domain"]] += 1
        kinds[node["kind"]] += 1
        if node["degree"] == 0:
            isolated.append(node["id"])
    for edge in edges:
        relations[edge["relation"]] += 1

    top_nodes = sorted(nodes, key=lambda n: (n["bridge_score"], n["degree"]), reverse=True)[:25]
    summary = [
        "---",
        "title: AI Infra 知识图谱构建报告",
        "tags:",
        "  - generated",
        "  - knowledge-graph",
        "---",
        "",
        "# AI Infra 知识图谱构建报告",
        "",
        f"- 节点数：**{len(nodes)}**",
        f"- 有向边数：**{len(edges)}**",
        f"- 未解析内部链接：**{len(unresolved)}**",
        f"- 孤立节点：**{len(isolated)}**",
        "",
        "## 按领域",
        "",
    ]
    for key, value in sorted(domains.items()):
        summary.append(f"- `{key}`：{value}")
    summary.extend(["", "## 按节点类型", ""])
    for key, value in sorted(kinds.items(), key=lambda x: (-x[1], x[0])):
        summary.append(f"- `{key}`：{value}")
    summary.extend(["", "## 按关系类型", ""])
    for key, value in sorted(relations.items(), key=lambda x: (-x[1], x[0])):
        summary.append(f"- `{key}`：{value}")
    summary.extend(["", "## 高连接度 / 桥接节点", "", "| 节点 | Degree | Cross-domain | Bridge score |", "| --- | ---: | ---: | ---: |"])
    for node in top_nodes:
        summary.append(f"| `[[{node['id']}|{node['name']}]]` | {node['degree']} | {node['cross_domain']} | {node['bridge_score']} |")
    summary.extend([
        "",
        "## 说明",
        "",
        "该报告由 `scripts/build-knowledge-graph.py` 自动生成。不要手工编辑 `generated/` 下的图谱派生文件。",
        "在线关系探索器由 GitHub Actions 在 Quartz 站点构建阶段生成。",
        "",
    ])
    (output / "graph-summary.md").write_text("\n".join(summary), encoding="utf-8")

    print(f"nodes={len(nodes)} edges={len(edges)} unresolved={len(unresolved)} isolated={len(isolated)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
