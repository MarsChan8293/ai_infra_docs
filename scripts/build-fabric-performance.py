#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

import yaml

SCHEMA_VERSION = "fabric-path-v0.1"
EFFICIENCY_FIELDS = (
    "protocol_efficiency",
    "utilization",
    "contention_efficiency",
)


def require_number(value: Any, field: str, *, positive: bool = False) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise ValueError(f"{field} must be numeric")
    value = float(value)
    if positive and value <= 0:
        raise ValueError(f"{field} must be > 0")
    return value


def optional_efficiency(stage: dict[str, Any], field: str) -> float | None:
    value = stage.get(field)
    if value is None:
        return None
    value = require_number(value, field, positive=True)
    if value > 1:
        raise ValueError(f"{field} must be <= 1")
    return value


def stage_record(stage: dict[str, Any], index: int) -> dict[str, Any]:
    name = str(stage.get("name") or f"stage-{index}")
    nominal = require_number(
        stage.get("nominal_bandwidth_gbps"),
        f"path[{index}].nominal_bandwidth_gbps",
        positive=True,
    )

    explicit_effective = stage.get("effective_bandwidth_gbps")
    if explicit_effective is not None:
        explicit_effective = require_number(
            explicit_effective,
            f"path[{index}].effective_bandwidth_gbps",
            positive=True,
        )
        if explicit_effective > nominal:
            raise ValueError(
                f"path[{index}].effective_bandwidth_gbps cannot exceed nominal bandwidth"
            )

    efficiencies = {
        field: optional_efficiency(stage, field)
        for field in EFFICIENCY_FIELDS
    }

    derived_effective = None
    if explicit_effective is None and all(
        value is not None for value in efficiencies.values()
    ):
        derived_effective = nominal
        for value in efficiencies.values():
            derived_effective *= float(value)

    latency_ns = stage.get("fixed_latency_ns")
    if latency_ns is not None:
        latency_ns = require_number(
            latency_ns,
            f"path[{index}].fixed_latency_ns",
            positive=False,
        )
        if latency_ns < 0:
            raise ValueError(f"path[{index}].fixed_latency_ns must be >= 0")

    effective = explicit_effective if explicit_effective is not None else derived_effective
    source = (
        "explicit"
        if explicit_effective is not None
        else "derived"
        if derived_effective is not None
        else "unknown"
    )

    return {
        "name": name,
        "nominal_bandwidth_gbps": nominal,
        "effective_bandwidth_gbps": effective,
        "effective_bandwidth_source": source,
        **efficiencies,
        "fixed_latency_ns": latency_ns,
    }


def seconds_for_bytes(payload_bytes: float, bandwidth_gbps: float) -> float:
    return payload_bytes * 8.0 / (bandwidth_gbps * 1e9)


def fmt_ms(seconds: float | None) -> str:
    if seconds is None:
        return "unknown"
    return f"{seconds * 1e3:.6f} ms"


def build_markdown(result: dict[str, Any]) -> str:
    metrics = result["metrics"]
    unknowns = result["unknowns"]

    lines = [
        "---",
        f"title: Fabric Performance - {result['name']}",
        "tags:",
        "  - generated",
        "  - fabric",
        "  - performance",
        "---",
        "",
        f"# Fabric Performance — {result['name']}",
        "",
        "> Auto-generated from an explicit fabric-path profile. This is a derived system model, not a vendor hardware fact.",
        "",
        "## Inputs",
        "",
        f"- Critical-path bytes: {result['critical_path_bytes']:,}",
        f"- Path stages: {len(result['stages'])}",
        "",
        "## Stage breakdown",
        "",
        "| Stage | Nominal | Effective | Source | Fixed latency |",
        "|---|---:|---:|---|---:|",
    ]

    for stage in result["stages"]:
        effective = stage["effective_bandwidth_gbps"]
        effective_text = (
            f"{effective:.6f} Gb/s" if effective is not None else "unknown"
        )
        latency = stage["fixed_latency_ns"]
        latency_text = f"{latency:.3f} ns" if latency is not None else "unknown"
        lines.append(
            f"| {stage['name']} | {stage['nominal_bandwidth_gbps']:.6f} Gb/s "
            f"| {effective_text} | {stage['effective_bandwidth_source']} "
            f"| {latency_text} |"
        )

    lines.extend([
        "",
        "## Derived metrics",
        "",
        f"- Nominal path bottleneck: {metrics['nominal_path_bottleneck_gbps']:.6f} Gb/s ({metrics['nominal_bottleneck_stage']})",
        (
            f"- Effective path bandwidth: {metrics['effective_path_bandwidth_gbps']:.6f} Gb/s "
            f"({metrics['effective_bottleneck_stage']})"
            if metrics["effective_path_bandwidth_gbps"] is not None
            else "- Effective path bandwidth: unknown"
        ),
        f"- Nominal serialization lower bound: {fmt_ms(metrics['nominal_serialization_seconds'])}",
        f"- Effective serialization lower bound: {fmt_ms(metrics['effective_serialization_seconds'])}",
        (
            f"- Fixed path latency: {metrics['path_fixed_latency_ns']:.3f} ns"
            if metrics["path_fixed_latency_ns"] is not None
            else "- Fixed path latency: unknown"
        ),
        f"- P2P transfer lower bound: {fmt_ms(metrics['p2p_transfer_lower_bound_seconds'])}",
        "",
        "## Unknowns",
        "",
    ])

    if unknowns:
        lines.extend(f"- {item}" for item in unknowns)
    else:
        lines.append("- none")

    lines.extend([
        "",
        "## Interpretation",
        "",
        "- Nominal bandwidth is a hardware/interface upper bound.",
        "- Effective bandwidth is derived only from explicit stage measurements or fully specified efficiency factors.",
        "- The P2P lower bound excludes software dispatch, synchronization, retry, queueing and other unmodeled costs.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--markdown-output")
    args = ap.parse_args()

    input_path = pathlib.Path(args.input)
    data = yaml.safe_load(input_path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ValueError("input must be a mapping")
    if data.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(f"schema_version must be {SCHEMA_VERSION}")

    name = str(data.get("name") or input_path.stem)
    critical_path_bytes = require_number(
        data.get("critical_path_bytes"),
        "critical_path_bytes",
        positive=True,
    )

    raw_path = data.get("path")
    if not isinstance(raw_path, list) or not raw_path:
        raise ValueError("path must be a non-empty list")

    stages = []
    for i, raw_stage in enumerate(raw_path):
        if not isinstance(raw_stage, dict):
            raise ValueError(f"path[{i}] must be a mapping")
        stages.append(stage_record(raw_stage, i))

    nominal_bottleneck = min(
        stages,
        key=lambda stage: stage["nominal_bandwidth_gbps"],
    )
    nominal_path_bottleneck = nominal_bottleneck["nominal_bandwidth_gbps"]

    effective_known = all(
        stage["effective_bandwidth_gbps"] is not None for stage in stages
    )
    effective_bottleneck = None
    if effective_known:
        effective_bottleneck = min(
            stages,
            key=lambda stage: float(stage["effective_bandwidth_gbps"]),
        )

    latency_known = all(stage["fixed_latency_ns"] is not None for stage in stages)
    path_fixed_latency_ns = (
        sum(float(stage["fixed_latency_ns"]) for stage in stages)
        if latency_known
        else None
    )

    nominal_serialization = seconds_for_bytes(
        critical_path_bytes,
        nominal_path_bottleneck,
    )

    effective_path_bandwidth = (
        float(effective_bottleneck["effective_bandwidth_gbps"])
        if effective_bottleneck is not None
        else None
    )
    effective_serialization = (
        seconds_for_bytes(critical_path_bytes, effective_path_bandwidth)
        if effective_path_bandwidth is not None
        else None
    )

    p2p_lower_bound = None
    if effective_serialization is not None and path_fixed_latency_ns is not None:
        p2p_lower_bound = effective_serialization + path_fixed_latency_ns * 1e-9

    unknowns: list[str] = []
    for stage in stages:
        if stage["effective_bandwidth_gbps"] is None:
            missing = [
                field for field in EFFICIENCY_FIELDS if stage[field] is None
            ]
            unknowns.append(
                f"{stage['name']}: effective bandwidth unavailable; "
                f"missing explicit effective bandwidth or factors {missing}"
            )
        if stage["fixed_latency_ns"] is None:
            unknowns.append(
                f"{stage['name']}: fixed latency unavailable"
            )

    result = {
        "schema_version": SCHEMA_VERSION,
        "name": name,
        "source_profile": input_path.as_posix(),
        "critical_path_bytes": int(critical_path_bytes),
        "stages": stages,
        "metrics": {
            "nominal_path_bottleneck_gbps": nominal_path_bottleneck,
            "nominal_bottleneck_stage": nominal_bottleneck["name"],
            "effective_path_bandwidth_gbps": effective_path_bandwidth,
            "effective_bottleneck_stage": (
                effective_bottleneck["name"] if effective_bottleneck else None
            ),
            "nominal_serialization_seconds": nominal_serialization,
            "effective_serialization_seconds": effective_serialization,
            "path_fixed_latency_ns": path_fixed_latency_ns,
            "p2p_transfer_lower_bound_seconds": p2p_lower_bound,
        },
        "unknowns": unknowns,
        "model_notes": [
            "No default efficiency factors are injected.",
            "Bandwidth inputs must already match the transfer direction and scope.",
            "P2P lower bound excludes software dispatch, synchronization, retry and queueing.",
        ],
    }

    output_path = pathlib.Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    if args.markdown_output:
        markdown_path = pathlib.Path(args.markdown_output)
        markdown_path.parent.mkdir(parents=True, exist_ok=True)
        markdown_path.write_text(build_markdown(result), encoding="utf-8")

    print(
        f"fabric_stages={len(stages)} "
        f"nominal_bottleneck_gbps={nominal_path_bottleneck:.6f} "
        f"effective_bottleneck_gbps="
        f"{effective_path_bandwidth if effective_path_bandwidth is not None else 'unknown'}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
