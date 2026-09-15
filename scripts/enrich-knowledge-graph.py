#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import pathlib
from collections import Counter, defaultdict

GENERIC_RELATIONS = {"wikilink", "navigation", "vendor-chip", "concept-link", "cross-domain"}


def relation_entries(value: object) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    if isinstance(value, dict):
        for rel, targets in value.items():
            if isinstance(targets, str):
                targets = [targets]
            if isinstance(targets, list):
                out.extend((str(rel), str(target)) for target in targets)
    return out


def rewrite_summary(path: pathlib.Path, relations: Counter, evidence: Counter) -> None:
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    rel_start = text.find("## 按关系类型")
    ev_start = text.find("## Evidence coverage")
    after_ev = text.find("## 高连接度", ev_start) if ev_start >= 0 else -1
    if rel_start < 0 or ev_start < 0 or after_ev < 0:
        return
    rel_lines = ["## 按关系类型", ""]
    for key, value in sorted(relations.items(), key=lambda item: (-item[1], item[0])):
        rel_lines.append(f"- `{key}`：{value}")
    rel_lines.append("")
    ev_lines = ["## Evidence coverage", ""]
    for key, value in sorted(evidence.items()):
        ev_lines.append(f"- `{key}`：{value}")
    ev_lines.append("")
    new_text = text[:rel_start] + "\n".join(rel_lines + ev_lines) + text[after_ev:]
    path.write_text(new_text, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--generated", default="generated")
    args = ap.parse_args()
    generated = pathlib.Path(args.generated)
    nodes_path = generated / "nodes.json"
    edges_path = generated / "edges.json"
    metrics_path = generated / "metrics.json"
    nodes = json.loads(nodes_path.read_text(encoding="utf-8"))
    edges = json.loads(edges_path.read_text(encoding="utf-8"))
    by_id = {node["id"]: node for node in nodes}

    edge_map: dict[tuple[str, str, str], dict] = {}
    for edge in edges:
        edge_map[(edge["source"], edge["target"], edge["relation"])] = edge

    added = 0
    for node in nodes:
        if node.get("domain") != "chip":
            continue
        source_id = node["id"]
        fm = node.get("frontmatter") or {}
        for relation, target_id in relation_entries(fm.get("relations")):
            if target_id not in by_id or target_id == source_id:
                continue
            for key in list(edge_map):
                if key[0] == source_id and key[1] == target_id and key[2] in GENERIC_RELATIONS:
                    del edge_map[key]
            key = (source_id, target_id, relation)
            if key not in edge_map:
                edge_map[key] = {"source": source_id, "target": target_id, "syntaxes": ["frontmatter"], "relation": relation}
                added += 1

        evidence_map = fm.get("evidence_map")
        if isinstance(evidence_map, dict) and any(key != "__page__" for key in evidence_map):
            node["evidence_level"] = "field"
        elif isinstance(fm.get("evidence"), dict) and fm.get("evidence"):
            node["evidence_level"] = "page"

    edges = sorted(edge_map.values(), key=lambda edge: (edge["source"], edge["target"], edge["relation"]))
    incoming = defaultdict(int)
    outgoing = defaultdict(int)
    cross = defaultdict(int)
    neighbors: dict[str, set[str]] = defaultdict(set)
    backlinks: dict[str, set[str]] = defaultdict(set)
    for edge in edges:
        source, target = edge["source"], edge["target"]
        outgoing[source] += 1
        incoming[target] += 1
        neighbors[source].add(target)
        neighbors[target].add(source)
        backlinks[target].add(source)
        if by_id[source].get("domain") != by_id[target].get("domain"):
            cross[source] += 1
            cross[target] += 1

    metrics = {}
    for node in nodes:
        node_id = node["id"]
        metric = {
            "degree": len(neighbors[node_id]),
            "incoming": incoming[node_id],
            "outgoing": outgoing[node_id],
            "cross_domain": cross[node_id],
            "bridge_score": len(neighbors[node_id]) + 3 * cross[node_id],
        }
        metrics[node_id] = metric
        node.update(metric)
        node["backlinks"] = sorted(backlinks[node_id])

    nodes_path.write_text(json.dumps(nodes, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    edges_path.write_text(json.dumps(edges, ensure_ascii=False, indent=2), encoding="utf-8")
    metrics_path.write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8")

    relation_counts = Counter(edge["relation"] for edge in edges)
    evidence_counts = Counter(node.get("evidence_level", "none") for node in nodes)
    rewrite_summary(generated / "graph-summary.md", relation_counts, evidence_counts)
    print(f"typed_edges_added={added} edges={len(edges)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
