#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any


def metric(
    value: Any,
    unit: str,
    formula: str,
    inputs: dict[str, Any],
    assumptions: list[str] | None = None,
    classification: str = "derived",
) -> dict[str, Any]:
    return {
        "value": value,
        "unit": unit,
        "formula": formula,
        "inputs": inputs,
        "assumptions": assumptions or [],
        "classification": classification,
    }


def number(value: Any) -> float | int | None:
    if isinstance(value, bool):
        return None
    return value if isinstance(value, (int, float)) else None


def nested(mapping: Any, *keys: str) -> Any:
    cur = mapping
    for key in keys:
        if not isinstance(cur, dict):
            return None
        cur = cur.get(key)
    return cur


def world_size(parallelism: dict[str, Any]) -> int:
    out = 1
    for key in ("tp", "pp", "ep", "dp", "cp"):
        value = parallelism.get(key)
        if not isinstance(value, int) or isinstance(value, bool) or value < 1:
            raise ValueError(f"parallelism.{key} must be an integer >= 1")
        out *= value
    return out


def build(profile: dict[str, Any]) -> dict[str, Any]:
    if profile.get("schema_version") != "workload-profile-v0.1":
        raise ValueError("expected workload-profile-v0.1")

    model = profile["model"]["facts"]
    hardware = nested(profile, "hardware", "facts") or {}
    workload = profile["workload"]
    execution = profile["execution"]
    parallelism = profile["parallelism"]
    assumptions = list(profile.get("assumptions") or [])
    unknowns = list(profile.get("unknowns") or [])
    warnings = list(profile.get("warnings") or [])

    metrics: dict[str, Any] = {
        "memory": {},
        "compute": {},
        "communication": {},
        "combined": {},
    }

    total_params = number(nested(model, "parameters", "total"))
    active_params = number(nested(model, "parameters", "active"))
    bytes_per_param = number(execution.get("weight_bytes_per_parameter"))
    stored_equal = execution.get("assume_total_parameters_equal_stored_parameters") is True

    weight_bytes = None
    if total_params is not None and bytes_per_param is not None and stored_equal:
        weight_bytes = total_params * bytes_per_param
        metrics["memory"]["logical_weight_payload_bytes"] = metric(
            weight_bytes,
            "byte",
            "parameters.total * execution.weight_bytes_per_parameter",
            {
                "parameters.total": total_params,
                "weight_bytes_per_parameter": bytes_per_param,
            },
            [
                "assume_total_parameters_equal_stored_parameters=true",
                "quantization metadata, runtime transformed copies and allocator overhead excluded",
            ],
            "scenario-derived lower-fidelity payload",
        )
    else:
        unknowns.append(
            "weight payload requires parameters.total, weight_bytes_per_parameter and explicit stored-parameter equality assumption"
        )

    kv_bytes_per_scalar = number(execution.get("kv_bytes_per_scalar"))
    growing_layers = number(nested(model, "structure", "attention", "growing_layers"))
    kv_heads = number(nested(model, "structure", "attention", "num_key_value_heads"))
    head_dim = number(nested(model, "structure", "attention", "head_dim"))
    kv_per_token = None
    if all(x is not None for x in (kv_bytes_per_scalar, growing_layers, kv_heads, head_dim)):
        kv_per_token = growing_layers * 2 * kv_heads * head_dim * kv_bytes_per_scalar
        metrics["memory"]["growing_kv_payload_bytes_per_token"] = metric(
            kv_per_token,
            "byte/token",
            "growing_layers * 2(K+V) * num_key_value_heads * head_dim * kv_bytes_per_scalar",
            {
                "growing_layers": growing_layers,
                "num_key_value_heads": kv_heads,
                "head_dim": head_dim,
                "kv_bytes_per_scalar": kv_bytes_per_scalar,
            },
            ["fixed recurrent state and allocator/quantization metadata excluded"],
            "model+scenario-derived payload",
        )
    else:
        unknowns.append("growing KV bytes/token requires growing_layers, kv_heads, head_dim and kv_bytes_per_scalar")

    context_tokens = number(workload.get("context_tokens"))
    kv_sequence = None
    if kv_per_token is not None and context_tokens is not None:
        kv_sequence = kv_per_token * context_tokens
        metrics["memory"]["growing_kv_payload_bytes_for_context"] = metric(
            kv_sequence,
            "byte",
            "growing_kv_payload_bytes_per_token * context_tokens",
            {"kv_bytes_per_token": kv_per_token, "context_tokens": context_tokens},
            ["logical growing KV payload; fixed recurrent state excluded"],
            "scenario-derived payload",
        )

    known_resident = None
    if weight_bytes is not None and kv_sequence is not None:
        known_resident = weight_bytes + kv_sequence
        metrics["memory"]["known_resident_lower_bound_bytes"] = metric(
            known_resident,
            "byte",
            "logical_weight_payload_bytes + growing_kv_payload_bytes_for_context",
            {"weight_bytes": weight_bytes, "growing_kv_bytes": kv_sequence},
            [
                "activation, workspace, communication buffers, allocator overhead, runtime reserve and fixed recurrent state excluded"
            ],
            "known-component lower bound",
        )

    capacity_gb = number(nested(hardware, "memory", "capacity_gb"))
    if capacity_gb is not None:
        capacity_bytes = capacity_gb * 1_000_000_000
        metrics["memory"]["hardware_memory_capacity_bytes"] = metric(
            capacity_bytes,
            "byte",
            "memory.capacity_gb * 1e9",
            {"memory.capacity_gb": capacity_gb},
            [],
            "hardware-fact conversion",
        )
        if known_resident is not None:
            headroom = capacity_bytes - known_resident
            metrics["memory"]["known_headroom_before_unknowns_bytes"] = metric(
                headroom,
                "byte",
                "hardware_memory_capacity_bytes - known_resident_lower_bound_bytes",
                {"capacity_bytes": capacity_bytes, "known_resident_lower_bound_bytes": known_resident},
                ["positive value does not prove deployment feasibility because excluded unknown memory remains"],
                "scenario-derived partial headroom",
            )

    if active_params is not None:
        linear_flops = 2 * active_params
        metrics["compute"]["linear_flops_per_token_approx"] = metric(
            linear_flops,
            "FLOP/token",
            "2 * parameters.active",
            {"parameters.active": active_params},
            [
                "FMA counted as 2 FLOPs",
                "attention, recurrent-state, normalization, sampling and runtime overhead excluded",
            ],
            "low-fidelity compute approximation",
        )
    else:
        linear_flops = None
        unknowns.append("linear FLOPs/token approximation requires parameters.active")

    traffic = execution.get("traffic_model") or {}
    hbm_bytes = 0
    traffic_inputs: dict[str, Any] = {}
    traffic_assumptions: list[str] = []
    traffic_known = False
    if traffic.get("read_full_weight_each_decode_step") is True and weight_bytes is not None:
        hbm_bytes += weight_bytes
        traffic_inputs["weight_bytes"] = weight_bytes
        traffic_assumptions.append("full weight payload is read from HBM each decode step")
        traffic_known = True
    if traffic.get("read_full_growing_kv_each_decode_step") is True and kv_sequence is not None:
        hbm_bytes += kv_sequence
        traffic_inputs["growing_kv_bytes"] = kv_sequence
        traffic_assumptions.append("full growing KV payload is read from HBM each decode step")
        traffic_known = True

    if workload.get("phase") == "decode" and traffic_known:
        metrics["memory"]["assumed_hbm_bytes_per_decode_token"] = metric(
            hbm_bytes,
            "byte/token",
            "sum(explicitly enabled traffic-model components)",
            traffic_inputs,
            traffic_assumptions + ["additional activation/workspace/read-write traffic excluded"],
            "scenario traffic assumption",
        )

        bandwidth_tb_s = number(nested(hardware, "memory", "bandwidth_tb_s"))
        if bandwidth_tb_s is not None and bandwidth_tb_s > 0:
            bandwidth_b_s = bandwidth_tb_s * 1_000_000_000_000
            t_mem = hbm_bytes / bandwidth_b_s
            tps = bandwidth_b_s / hbm_bytes if hbm_bytes > 0 else None
            metrics["memory"]["peak_hbm_time_lower_bound_s_per_token"] = metric(
                t_mem,
                "s/token",
                "assumed_hbm_bytes_per_decode_token / (memory.bandwidth_tb_s * 1e12)",
                {"bytes_per_token": hbm_bytes, "bandwidth_tb_s": bandwidth_tb_s},
                ["uses vendor peak bandwidth, not achieved application bandwidth"],
                "theoretical peak-bandwidth lower bound",
            )
            metrics["memory"]["peak_hbm_only_token_ceiling"] = metric(
                tps,
                "token/s",
                "(memory.bandwidth_tb_s * 1e12) / assumed_hbm_bytes_per_decode_token",
                {"bytes_per_token": hbm_bytes, "bandwidth_tb_s": bandwidth_tb_s},
                ["not a performance prediction"],
                "theoretical peak-bandwidth ceiling",
            )
            if linear_flops is not None and hbm_bytes > 0:
                ai = linear_flops / hbm_bytes
                metrics["combined"]["linear_arithmetic_intensity"] = metric(
                    ai,
                    "FLOP/byte",
                    "linear_flops_per_token_approx / assumed_hbm_bytes_per_decode_token",
                    {"linear_flops": linear_flops, "hbm_bytes": hbm_bytes},
                    ["same low-fidelity compute and traffic scope used in numerator/denominator"],
                    "scenario-derived approximation",
                )

    size = world_size(parallelism)
    metrics["communication"]["world_size"] = metric(
        size,
        "rank",
        "tp * pp * ep * dp * cp",
        parallelism,
        [],
        "workload configuration",
    )
    if size == 1:
        metrics["communication"]["inter_accelerator_payload_bytes"] = metric(
            0,
            "byte/step",
            "0 because world_size == 1",
            {"world_size": size},
            ["no inter-accelerator parallel group exists in this scenario"],
            "workload-defined",
        )
    else:
        unknowns.append(
            "world_size > 1: communication payload requires tensor shapes, algorithm and placement; no automatic zero or equal-shard assumption"
        )

    compute_block = hardware.get("compute") or {}
    numeric_compute = {
        key: value
        for key, value in compute_block.items()
        if isinstance(value, (int, float)) and not isinstance(value, bool)
    } if isinstance(compute_block, dict) else {}
    if not numeric_compute:
        unknowns.append(
            "hardware compute throughput is unavailable; ridge point and compute-vs-memory Roofline classification remain unknown"
        )

    return {
        "schema_version": "system-requirements-v0.1",
        "profile_source": profile.get("source"),
        "model": profile["model"],
        "hardware": profile.get("hardware"),
        "workload": workload,
        "parallelism": parallelism,
        "assumptions": assumptions,
        "metrics": metrics,
        "unknowns": sorted(set(unknowns)),
        "warnings": sorted(set(warnings)),
    }


def fmt(value: Any) -> str:
    if isinstance(value, float):
        if abs(value) >= 1_000_000:
            return f"{value:,.3f}"
        if abs(value) >= 1:
            return f"{value:.6f}".rstrip("0").rstrip(".")
        return f"{value:.9f}".rstrip("0").rstrip(".")
    if isinstance(value, int):
        return f"{value:,}"
    return str(value)


def wiki_from_md(path: str) -> str:
    return path[:-3] if path.endswith(".md") else path


def markdown(report: dict[str, Any]) -> str:
    model_path = report["model"]["path"]
    model_name = nested(report, "model", "facts", "name") or model_path
    hardware_path = nested(report, "hardware", "path")
    hardware_name = nested(report, "hardware", "facts", "title") or hardware_path or "None"

    lines = [
        "---",
        "title: Executable Model → System → Hardware Report",
        "tags:",
        "  - generated",
        "  - executable",
        "  - system-requirements",
        "updated: 2026-09-25",
        "---",
        "# Executable Model → System → Hardware Report",
        "",
        "> 此页由脚本从 canonical Model / Chip frontmatter 与显式 workload assumptions 生成，不手工维护。数字是公式派生、理论下界或显式场景假设，不是 benchmark。",
        "",
        "## 输入",
        "",
        f"- Model：[[{wiki_from_md(model_path)}|{model_name}]]",
    ]
    if hardware_path:
        lines.append(f"- Hardware：[[{wiki_from_md(hardware_path)}|{hardware_name}]]")
    lines.extend([
        f"- Workload phase：`{report['workload'].get('phase')}`",
        f"- Parallel world size：`{nested(report, 'metrics', 'communication', 'world_size', 'value')}`",
        "",
        "## 派生结果",
        "",
        "| Domain | Metric | Value | Classification |",
        "|---|---|---:|---|",
    ])

    for domain, domain_metrics in report["metrics"].items():
        for name, item in domain_metrics.items():
            lines.append(
                f"| {domain} | `{name}` | {fmt(item['value'])} {item['unit']} | {item['classification']} |"
            )

    lines.extend(["", "## 公式追溯", ""])
    for domain, domain_metrics in report["metrics"].items():
        for name, item in domain_metrics.items():
            lines.extend([
                f"### {domain}.{name}",
                "",
                f"- Formula: `{item['formula']}`",
                f"- Inputs: `{json.dumps(item['inputs'], ensure_ascii=False, sort_keys=True)}`",
                f"- Assumptions: `{json.dumps(item['assumptions'], ensure_ascii=False)}`",
                f"- Classification: `{item['classification']}`",
                "",
            ])

    lines.extend(["## 显式未知项", ""])
    if report["unknowns"]:
        lines.extend([f"- {item}" for item in report["unknowns"]])
    else:
        lines.append("- None recorded.")

    lines.extend(["", "## System 公式入口", "",
        "- [[system/workload/workload-profile-v0.1|Workload Profile V0.1]]",
        "- [[system/memory/model-memory-accounting|Model Memory Accounting]]",
        "- [[system/memory/kv-cache-model|KV Cache Model]]",
        "- [[system/memory/memory-bandwidth-model|Memory Bandwidth Model]]",
        "- [[system/compute/transformer-compute-model|Transformer Compute Model]]",
        "- [[system/compute/roofline-and-arithmetic-intensity|Roofline 与 Arithmetic Intensity]]",
        "- [[system/communication/communication-cost-model|Communication Cost Model]]",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--profile", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--markdown-output", default=None)
    args = ap.parse_args()

    root = pathlib.Path(args.root).resolve()
    profile_path = (root / args.profile).resolve()
    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    report = build(profile)

    output = (root / args.output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    if args.markdown_output:
        md_path = (root / args.markdown_output).resolve()
        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(markdown(report), encoding="utf-8")

    total_metrics = sum(len(v) for v in report["metrics"].values())
    print(
        f"system_requirements={output.relative_to(root)} metrics={total_metrics} "
        f"unknowns={len(report['unknowns'])} warnings={len(report['warnings'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
