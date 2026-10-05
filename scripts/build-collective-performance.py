#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

import yaml

SCHEMA_VERSION = "collective-profile-v0.1"
COLLECTIVES = {"all-reduce", "reduce-scatter", "all-gather", "all-to-all"}
ALGORITHMS = {"ring", "tree", "direct"}


def require_number(value: Any, field: str, *, positive: bool = False) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise ValueError(f"{field} must be numeric")
    value = float(value)
    if positive and value <= 0:
        raise ValueError(f"{field} must be > 0")
    return value


def require_int(value: Any, field: str, *, minimum: int | None = None) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError(f"{field} must be an integer")
    if minimum is not None and value < minimum:
        raise ValueError(f"{field} must be >= {minimum}")
    return value


def optional_positive_number(data: dict[str, Any], field: str) -> float | None:
    value = data.get(field)
    if value is None:
        return None
    return require_number(value, field, positive=True)


def derive_ring(
    collective: str,
    participants: int,
    payload_bytes_per_rank: float,
) -> tuple[int, float, dict[str, Any]]:
    n = participants
    m = payload_bytes_per_rank

    if collective == "all-reduce":
        steps = 2 * (n - 1)
        critical = 2.0 * m * (n - 1) / n
        details = {
            "ring_phases": ["reduce-scatter", "all-gather"],
            "chunk_bytes": m / n,
            "formula": "2 * payload * (N - 1) / N",
        }
        return steps, critical, details

    if collective == "reduce-scatter":
        steps = n - 1
        critical = m * (n - 1) / n
        details = {
            "ring_phases": ["reduce-scatter"],
            "chunk_bytes": m / n,
            "formula": "payload * (N - 1) / N",
        }
        return steps, critical, details

    if collective == "all-gather":
        steps = n - 1
        critical = m * (n - 1)
        details = {
            "ring_phases": ["all-gather"],
            "local_shard_bytes": m,
            "final_logical_bytes": m * n,
            "formula": "local_shard * (N - 1)",
        }
        return steps, critical, details

    raise ValueError("ring derivation does not support all-to-all")


def load_fabric_profile(path: pathlib.Path | None) -> dict[str, Any] | None:
    if path is None:
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("fabric profile must be a JSON object")
    metrics = data.get("metrics")
    if not isinstance(metrics, dict):
        raise ValueError("fabric profile must contain metrics")
    return data


def seconds_for_bytes(payload_bytes: float, bandwidth_gbps: float) -> float:
    return payload_bytes * 8.0 / (bandwidth_gbps * 1e9)


def fmt_ms(seconds: float | None) -> str:
    if seconds is None:
        return "unknown"
    return f"{seconds * 1e3:.6f} ms"


def build_markdown(result: dict[str, Any]) -> str:
    metrics = result["metrics"]
    sources = result["sources"]
    unknowns = result["unknowns"]

    lines = [
        "---",
        f"title: Collective Performance - {result['name']}",
        "tags:",
        "  - generated",
        "  - collective",
        "  - performance",
        "---",
        "",
        f"# Collective Performance — {result['name']}",
        "",
        "> Derived system model. Inputs and algorithm assumptions are explicit; this is not a vendor benchmark.",
        "",
        "## Collective",
        "",
        f"- Type: {result['collective']}",
        f"- Algorithm: {result['algorithm']}",
        f"- Participants: {result['participant_count']}",
        f"- Payload bytes / rank: {result['payload_bytes_per_rank']:,}",
        "",
        "## Algorithm decomposition",
        "",
        (
            f"- Sequential steps: {metrics['algorithm_steps']} "
            f"({sources['steps_source']})"
            if metrics["algorithm_steps"] is not None
            else f"- Sequential steps: unknown ({sources['steps_source']})"
        ),
        (
            f"- Critical-path bytes: {metrics['critical_path_bytes']:,} "
            f"({sources['critical_path_bytes_source']})"
            if metrics["critical_path_bytes"] is not None
            else f"- Critical-path bytes: unknown ({sources['critical_path_bytes_source']})"
        ),
        (
            f"- Algorithmic traffic factor: {metrics['algorithmic_traffic_factor']:.6f}"
            if metrics["algorithmic_traffic_factor"] is not None
            else "- Algorithmic traffic factor: unknown"
        ),
        "",
        "## Bandwidth and latency",
        "",
        (
            f"- Nominal bandwidth: {metrics['nominal_bandwidth_gbps']:.6f} Gb/s"
            if metrics["nominal_bandwidth_gbps"] is not None
            else "- Nominal bandwidth: unknown"
        ),
        (
            f"- Effective bandwidth: {metrics['effective_bandwidth_gbps']:.6f} Gb/s "
            f"({sources['effective_bandwidth_source']})"
            if metrics["effective_bandwidth_gbps"] is not None
            else f"- Effective bandwidth: unknown ({sources['effective_bandwidth_source']})"
        ),
        (
            f"- Step latency: {metrics['step_latency_ns']:.3f} ns "
            f"({sources['step_latency_source']})"
            if metrics["step_latency_ns"] is not None
            else f"- Step latency: unknown ({sources['step_latency_source']})"
        ),
        "",
        "## Lower bounds",
        "",
        f"- Serialization: {fmt_ms(metrics['serialization_seconds'])}",
        f"- Sequential step latency: {fmt_ms(metrics['step_latency_seconds'])}",
        f"- Collective time lower bound: {fmt_ms(metrics['collective_time_lower_bound_seconds'])}",
        (
            f"- Payload goodput: {metrics['payload_goodput_gbps']:.6f} Gb/s"
            if metrics["payload_goodput_gbps"] is not None
            else "- Payload goodput: unknown"
        ),
        "",
        "## Unknowns",
        "",
    ]

    if unknowns:
        lines.extend(f"- {item}" for item in unknowns)
    else:
        lines.append("- none")

    lines.extend([
        "",
        "## Interpretation",
        "",
        "- algorithmic traffic factor is data movement amplification, not an efficiency percentage.",
        "- payload goodput uses the per-rank input payload semantic; compare it only across compatible collective definitions.",
        "- the lower bound excludes synchronization beyond modeled steps, stragglers, retry, queueing, compute overlap and unmodeled bisection effects.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--fabric-profile")
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
    collective = str(data.get("collective") or "")
    algorithm = str(data.get("algorithm") or "")
    if collective not in COLLECTIVES:
        raise ValueError(f"collective must be one of {sorted(COLLECTIVES)}")
    if algorithm not in ALGORITHMS:
        raise ValueError(f"algorithm must be one of {sorted(ALGORITHMS)}")

    participants = require_int(
        data.get("participant_count"),
        "participant_count",
        minimum=2,
    )
    payload = require_number(
        data.get("payload_bytes_per_rank"),
        "payload_bytes_per_rank",
        positive=True,
    )

    explicit_steps = data.get("algorithm_steps")
    if explicit_steps is not None:
        explicit_steps = require_int(explicit_steps, "algorithm_steps", minimum=1)

    explicit_critical = data.get("critical_path_bytes")
    if explicit_critical is not None:
        explicit_critical = require_number(
            explicit_critical,
            "critical_path_bytes",
            positive=True,
        )

    steps: int | None = None
    critical: float | None = None
    algorithm_details: dict[str, Any] = {}
    steps_source = "unavailable"
    critical_source = "unavailable"

    if algorithm == "ring":
        if explicit_steps is not None or explicit_critical is not None:
            raise ValueError(
                "ring steps/critical bytes are derived; do not override them"
            )
        steps, critical, algorithm_details = derive_ring(
            collective,
            participants,
            payload,
        )
        steps_source = "derived-ring"
        critical_source = "derived-ring"

    elif algorithm == "tree":
        if collective != "all-reduce":
            raise ValueError("tree mode currently supports all-reduce only")
        steps = explicit_steps
        critical = explicit_critical
        steps_source = "explicit" if steps is not None else "unavailable"
        critical_source = "explicit" if critical is not None else "unavailable"
        algorithm_details = {
            "note": (
                "Tree topology/implementation is not inferred. "
                "steps and critical-path bytes are explicit profile inputs."
            )
        }

    elif algorithm == "direct":
        if collective != "all-to-all":
            raise ValueError("direct mode currently supports all-to-all only")
        uniform_partition = data.get("uniform_partition")
        if not isinstance(uniform_partition, bool):
            raise ValueError("direct all-to-all requires uniform_partition boolean")
        network_send_bytes = (
            payload * (participants - 1) / participants
            if uniform_partition
            else None
        )
        steps = explicit_steps
        critical = explicit_critical
        steps_source = "explicit" if steps is not None else "unavailable"
        critical_source = "explicit" if critical is not None else "unavailable"
        algorithm_details = {
            "uniform_partition": uniform_partition,
            "uniform_network_send_bytes_per_rank": network_send_bytes,
            "note": (
                "All-to-All timing does not reuse a single P2P fabric path. "
                "Use explicit topology-aware collective bandwidth."
            ),
        }

    fabric = load_fabric_profile(
        pathlib.Path(args.fabric_profile) if args.fabric_profile else None
    )
    fabric_metrics = fabric.get("metrics", {}) if fabric else {}

    nominal_bandwidth = None
    if fabric:
        value = fabric_metrics.get("nominal_path_bottleneck_gbps")
        if value is not None:
            nominal_bandwidth = require_number(
                value,
                "fabric.metrics.nominal_path_bottleneck_gbps",
                positive=True,
            )

    explicit_collective_bw = optional_positive_number(
        data,
        "collective_effective_bandwidth_gbps",
    )

    effective_bandwidth = None
    effective_bw_source = "unavailable"

    if explicit_collective_bw is not None:
        effective_bandwidth = explicit_collective_bw
        effective_bw_source = "explicit-collective"
    elif algorithm in {"ring", "tree"} and fabric:
        value = fabric_metrics.get("effective_path_bandwidth_gbps")
        if value is not None:
            effective_bandwidth = require_number(
                value,
                "fabric.metrics.effective_path_bandwidth_gbps",
                positive=True,
            )
            effective_bw_source = "fabric-profile-effective-path"

    explicit_step_latency = optional_positive_number(data, "step_latency_ns")
    step_latency_ns = None
    step_latency_source = "unavailable"

    if explicit_step_latency is not None:
        step_latency_ns = explicit_step_latency
        step_latency_source = "explicit"
    elif algorithm in {"ring", "tree"} and fabric:
        value = fabric_metrics.get("path_fixed_latency_ns")
        if value is not None:
            value = require_number(
                value,
                "fabric.metrics.path_fixed_latency_ns",
                positive=False,
            )
            if value < 0:
                raise ValueError("fabric path_fixed_latency_ns must be >= 0")
            step_latency_ns = value
            step_latency_source = "fabric-profile-fixed-path"

    serialization = None
    if critical is not None and effective_bandwidth is not None:
        serialization = seconds_for_bytes(critical, effective_bandwidth)

    step_latency_seconds = None
    if steps is not None and step_latency_ns is not None:
        step_latency_seconds = steps * step_latency_ns * 1e-9

    total_lower_bound = None
    if serialization is not None and step_latency_seconds is not None:
        total_lower_bound = serialization + step_latency_seconds

    traffic_factor = critical / payload if critical is not None else None
    payload_goodput = (
        payload * 8.0 / total_lower_bound / 1e9
        if total_lower_bound is not None
        else None
    )

    unknowns: list[str] = []
    if steps is None:
        unknowns.append("algorithm steps unavailable")
    if critical is None:
        unknowns.append("critical-path bytes unavailable")
    if effective_bandwidth is None:
        if algorithm == "direct" and collective == "all-to-all":
            unknowns.append(
                "collective effective bandwidth unavailable; "
                "All-to-All does not inherit single-path P2P bandwidth"
            )
        else:
            unknowns.append("effective bandwidth unavailable")
    if step_latency_ns is None:
        unknowns.append("step latency unavailable")
    if total_lower_bound is None:
        unknowns.append(
            "complete collective lower bound unavailable because one or more required components are unknown"
        )

    result = {
        "schema_version": SCHEMA_VERSION,
        "name": name,
        "source_profile": input_path.as_posix(),
        "fabric_profile": args.fabric_profile,
        "collective": collective,
        "algorithm": algorithm,
        "participant_count": participants,
        "payload_bytes_per_rank": int(payload),
        "algorithm_details": algorithm_details,
        "sources": {
            "steps_source": steps_source,
            "critical_path_bytes_source": critical_source,
            "effective_bandwidth_source": effective_bw_source,
            "step_latency_source": step_latency_source,
        },
        "metrics": {
            "algorithm_steps": steps,
            "critical_path_bytes": int(critical) if critical is not None else None,
            "algorithmic_traffic_factor": traffic_factor,
            "nominal_bandwidth_gbps": nominal_bandwidth,
            "effective_bandwidth_gbps": effective_bandwidth,
            "step_latency_ns": step_latency_ns,
            "serialization_seconds": serialization,
            "step_latency_seconds": step_latency_seconds,
            "collective_time_lower_bound_seconds": total_lower_bound,
            "payload_goodput_gbps": payload_goodput,
        },
        "unknowns": unknowns,
        "model_notes": [
            "No fixed collective efficiency constant is injected.",
            "Ring formulas are derived only for supported collective semantics.",
            "Tree steps and critical-path bytes are explicit because tree implementations differ.",
            "All-to-All requires explicit topology-aware collective bandwidth for timing.",
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
        f"collective={collective} algorithm={algorithm} participants={participants} "
        f"steps={steps if steps is not None else 'unknown'} "
        f"critical_path_bytes={int(critical) if critical is not None else 'unknown'} "
        f"effective_bandwidth_gbps="
        f"{effective_bandwidth if effective_bandwidth is not None else 'unknown'}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
