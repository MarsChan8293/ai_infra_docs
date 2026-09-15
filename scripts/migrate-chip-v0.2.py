#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import yaml

URL_RE = re.compile(r"https?://[^\s)>\]]+")
OBJECT_TYPE_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EXCLUDED_NAMES = {"SCHEMA.md", "MIGRATION.md", "00-project-index.md"}
NUMERIC_SUFFIXES = ("_gb", "_tb_s", "_gb_s", "_tflops", "_tops", "_w", "_kw", "_nm", "_mhz", "_ghz")
SLASH_NUMBERS_RE = re.compile(r"^\d+(?:\.\d+)?(?:/\d+(?:\.\d+)?)+$")


def parse_frontmatter(text: str) -> tuple[dict, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    data = yaml.safe_load(text[4:end]) or {}
    if not isinstance(data, dict):
        return None
    return data, text[end + 5 :]


def section(text: str, heading: str) -> str:
    match = re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.M)
    if not match:
        return ""
    start = match.end()
    nxt = re.search(r"^##\s+", text[start:], re.M)
    end = start + nxt.start() if nxt else len(text)
    return text[start:end]


def source_urls(body: str) -> list[str]:
    sec = section(body, "直接来源")
    out: list[str] = []
    for url in URL_RE.findall(sec):
        url = url.rstrip(".,;，；")
        if url not in out:
            out.append(url)
    return out


def canonical_object_type(value: object) -> tuple[str, str | None]:
    original = str(value or "unknown").strip()
    raw = original.lower().replace("_", "-").replace(" ", "-")
    raw = re.sub(r"-+", "-", raw).strip("-") or "unknown"
    if OBJECT_TYPE_RE.match(raw):
        return raw, None
    return "unknown", original or None


def infer_layer(object_type: str) -> str:
    value = object_type.casefold()
    if "family" in value or "architecture" in value or value == "generation":
        return "family"
    if any(k in value for k in ("network", "switch", "nic")):
        return "network"
    if any(k in value for k in ("memory", "hbm")):
        return "memory"
    if "soc" in value:
        return "soc"
    if value in {"ip", "core", "accelerator-ip"} or value.endswith("-ip"):
        return "ip"
    if any(k in value for k in ("cluster", "pod", "supercluster")):
        return "cluster"
    if "rack" in value:
        return "rack"
    if any(k in value for k in ("baseboard", "board", "accelerator-group")):
        return "board"
    if any(k in value for k in ("module", "package", "superchip")):
        return "module"
    if any(k in value for k in ("server", "system", "appliance")):
        return "system"
    if any(k in value for k in ("accelerator", "card", "device")):
        return "accelerator"
    if value in {"gpu", "npu", "tpu", "xpu", "lpu", "ppu"}:
        return "chip"
    if any(k in value for k in ("chip", "processor", "asic", "wafer")):
        return "chip"
    return "unknown"


def normalized_status(value: object) -> tuple[str, str | None]:
    original = str(value or "unknown").strip()
    raw = original.lower().replace("_", "-").replace(" ", "-")
    raw = re.sub(r"-+", "-", raw).strip("-") or "unknown"
    allowed = {"roadmap", "announced", "sampling", "pre-deployment", "production", "shipping", "current-catalog", "product", "ga", "legacy", "eol", "unknown"}
    aliases = {
        "planned": "roadmap", "future": "roadmap", "preview": "announced",
        "sample": "sampling", "samples": "sampling", "prototype": "sampling", "pre-production": "sampling",
        "in-production": "production", "mass-production": "production", "mass-produced": "production", "production-ramp": "production",
        "available": "ga", "current": "ga", "commercial": "ga", "launched": "ga", "released": "ga",
        "deployed": "production", "retired": "eol", "discontinued": "eol", "end-of-life": "eol",
    }
    canonical = aliases.get(raw, raw)
    if canonical in allowed:
        return canonical, None if canonical == raw else original
    return "unknown", original or None


def default_block(fm: dict, key: str) -> None:
    if key not in fm:
        fm[key] = {}


def normalize_numeric_fields(value: object) -> None:
    if not isinstance(value, dict):
        return
    pending_notes: dict[str, str] = {}
    for key, child in list(value.items()):
        if isinstance(child, dict):
            normalize_numeric_fields(child)
            continue
        if not key.endswith(NUMERIC_SUFFIXES) or not isinstance(child, str):
            continue
        raw = child.strip()
        if SLASH_NUMBERS_RE.match(raw):
            items = []
            for part in raw.split("/"):
                number = float(part) if "." in part else int(part)
                items.append(number)
            value[key] = items
        elif "numeric unknown" in raw.casefold():
            value[key] = None
            stem = key
            for suffix in NUMERIC_SUFFIXES:
                if stem.endswith(suffix):
                    stem = stem[: -len(suffix)]
                    break
            pending_notes[f"{stem}_note"] = raw
    value.update(pending_notes)


def fact_paths(fm: dict) -> list[str]:
    out: list[str] = []
    for root_key in ("architecture", "process", "memory", "compute", "interconnect", "power", "lifecycle"):
        root_value = fm.get(root_key)
        if root_value is None or root_value == {} or root_value == [] or root_value == "":
            continue
        if isinstance(root_value, dict):
            stack = [(root_key, root_value)]
            while stack:
                prefix, mapping = stack.pop()
                for key, child in mapping.items():
                    path = f"{prefix}.{key}"
                    if isinstance(child, dict):
                        stack.append((path, child))
                    elif child is not None and child != "" and child != []:
                        out.append(path)
        else:
            out.append(root_key)
    return sorted(set(out))


def migrate_file(path: pathlib.Path, accessed: str) -> bool:
    text = path.read_text(encoding="utf-8")
    parsed = parse_frontmatter(text)
    if not parsed:
        return False
    fm, body = parsed
    if not fm.get("vendor") or not fm.get("object_type") or fm.get("object_type") == "vendor-overview":
        return False

    before = text
    fm["schema_version"] = "chip-v0.2"
    object_type, legacy_object_type = canonical_object_type(fm.get("object_type"))
    fm["object_type"] = object_type
    if legacy_object_type:
        fm.setdefault("legacy_object_type", legacy_object_type)
    fm["layer"] = infer_layer(fm["object_type"])
    status, legacy_status = normalized_status(fm.get("status"))
    fm["status"] = status
    if legacy_status:
        fm.setdefault("legacy_status", legacy_status)
    for key in ("architecture", "process"):
        if key not in fm:
            fm[key] = None
    for key in ("memory", "compute", "interconnect", "power", "lifecycle"):
        default_block(fm, key)
        normalize_numeric_fields(fm.get(key))
    if not isinstance(fm.get("relations"), dict):
        fm["relations"] = {}

    urls = source_urls(body)
    existing_evidence = fm.get("evidence")
    evidence: dict[str, dict] = existing_evidence if isinstance(existing_evidence, dict) else {}
    known_urls = {
        str(item.get("url")): key
        for key, item in evidence.items()
        if isinstance(item, dict) and item.get("url")
    }
    next_id = 1
    for url in urls:
        if url in known_urls:
            continue
        while f"S{next_id}" in evidence:
            next_id += 1
        evidence[f"S{next_id}"] = {"url": url, "source_type": "other", "accessed": accessed}
        next_id += 1
    fm["evidence"] = evidence

    evidence_map = fm.get("evidence_map") if isinstance(fm.get("evidence_map"), dict) else {}
    if "__page__" not in evidence_map:
        evidence_map["__page__"] = list(evidence)
    if len(evidence) == 1 and not any(key != "__page__" for key in evidence_map):
        only_source = next(iter(evidence))
        for field_path in fact_paths(fm):
            evidence_map[field_path] = [only_source]
    fm["evidence_map"] = evidence_map

    if "updated" not in fm:
        fm["updated"] = accessed

    dumped = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, default_flow_style=False, width=120).rstrip()
    new_text = f"---\n{dumped}\n---\n{body.lstrip()}"
    if new_text != before:
        path.write_text(new_text, encoding="utf-8")
        return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--accessed", default=dt.date.today().isoformat())
    args = ap.parse_args()
    root = pathlib.Path(args.root).resolve()
    changed = 0
    objects = 0
    for path in sorted((root / "chip").rglob("*.md")):
        if path.name in EXCLUDED_NAMES:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        parsed = parse_frontmatter(text)
        if not parsed:
            continue
        fm, _ = parsed
        if not fm.get("vendor") or not fm.get("object_type") or fm.get("object_type") == "vendor-overview":
            continue
        objects += 1
        if migrate_file(path, args.accessed):
            changed += 1
    print(f"chip_objects={objects} migrated={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
