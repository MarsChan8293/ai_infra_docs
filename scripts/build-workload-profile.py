#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import pathlib
from typing import Any

import yaml

PROFILE_VERSION = "workload-profile-v0.1"


def load_yaml(path: pathlib.Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path}: YAML root must be a mapping")
    return data


def frontmatter(path: pathlib.Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"{path}: unclosed YAML frontmatter")
    data = yaml.safe_load(text[4:end]) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path}: frontmatter must be a mapping")
    return data


def json_safe(value: Any) -> Any:
    if isinstance(value, (dt.date, dt.datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {str(k): json_safe(v) for k, v in value.items()}
    if isinstance(value, list):
        return [json_safe(v) for v in value]
    if isinstance(value, tuple):
        return [json_safe(v) for v in value]
    return value


def require_positive_int(value: Any, label: str, *, allow_zero: bool = False) -> None:
    if value is None:
        return
    minimum = 0 if allow_zero else 1
    if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
        raise ValueError(f"{label} must be an integer >= {minimum}")


def require_nonnegative_number(value: Any, label: str) -> None:
    if value is None:
        return
    if isinstance(value, bool) or not isinstance(value, (int, float)) or value < 0:
        raise ValueError(f"{label} must be a non-negative number or null")


def model_snapshot(fm: dict[str, Any]) -> dict[str, Any]:
    keys = (
        "schema_version", "name", "organization", "family", "architecture",
        "parameters", "structure", "context_length", "kv_cache_64k_fp8_bytes",
        "snapshot", "updated",
    )
    return {key: fm.get(key) for key in keys}


def hardware_snapshot(fm: dict[str, Any]) -> dict[str, Any]:
    keys = (
        "schema_version", "title", "vendor", "object_type", "layer", "status",
        "architecture", "memory", "compute", "interconnect", "power", "updated",
    )
    return {key: fm.get(key) for key in keys}


def validate_profile(profile: dict[str, Any]) -> None:
    if profile.get("schema_version") != PROFILE_VERSION:
        raise ValueError(f"schema_version must be {PROFILE_VERSION}")

    model = profile.get("model")
    workload = profile.get("workload")
    execution = profile.get("execution")
    parallelism = profile.get("parallelism")
    assumptions = profile.get("assumptions")

    if not isinstance(model, dict) or not isinstance(model.get("path"), str):
        raise ValueError("model.path is required")
    if not isinstance(workload, dict) or workload.get("type") not in {"inference", "training"}:
        raise ValueError("workload.type must be inference or training")
    if not isinstance(execution, dict):
        raise ValueError("execution must be a mapping")
    if not isinstance(parallelism, dict):
        raise ValueError("parallelism must be a mapping")
    if not isinstance(assumptions, list) or not all(isinstance(x, str) for x in assumptions):
        raise ValueError("assumptions must be a list of strings")

    for key in ("tp", "pp", "ep", "dp", "cp"):
        require_positive_int(parallelism.get(key), f"parallelism.{key}")
        if key not in parallelism:
            raise ValueError(f"parallelism.{key} is required")

    if workload["type"] == "inference":
        for key in ("prompt_tokens", "output_tokens", "context_tokens"):
            require_positive_int(workload.get(key), f"workload.{key}", allow_zero=True)
        for key in ("batch_size", "concurrency"):
            require_positive_int(workload.get(key), f"workload.{key}")
        require_nonnegative_number(workload.get("request_rate_rps"), "workload.request_rate_rps")
        ratio = workload.get("prefix_reuse_ratio")
        if ratio is not None and (
            isinstance(ratio, bool) or not isinstance(ratio, (int, float)) or ratio < 0 or ratio > 1
        ):
            raise ValueError("workload.prefix_reuse_ratio must be in [0, 1] or null")
    else:
        for key in (
            "global_batch_size", "micro_batch_size", "gradient_accumulation_steps",
            "sequence_length", "checkpoint_interval_steps",
        ):
            require_positive_int(workload.get(key), f"workload.{key}")

    for key in ("weight_bytes_per_parameter", "kv_bytes_per_scalar"):
        value = execution.get(key)
        if value is not None and (
            isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0
        ):
            raise ValueError(f"execution.{key} must be > 0 or null")


def derive_workload(workload: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    derived: dict[str, Any] = {}
    unknowns: list[str] = []
    if workload["type"] == "inference":
        p = workload.get("prompt_tokens")
        o = workload.get("output_tokens")
        reuse = workload.get("prefix_reuse_ratio")
        if p is not None and o is not None:
            derived["tokens_per_request"] = p + o
        else:
            unknowns.append("tokens_per_request requires prompt_tokens and output_tokens")
        if p is not None and reuse is not None:
            reused = int(round(p * reuse))
            derived["reused_prompt_tokens"] = reused
            derived["recomputed_prompt_tokens"] = p - reused
        else:
            unknowns.append("prefix-derived prompt work requires prompt_tokens and prefix_reuse_ratio")
        if o is not None:
            derived["decode_steps_baseline"] = o
        if workload.get("request_rate_rps") is None:
            unknowns.append("request_rate_rps is unknown")
        if workload.get("batch_size") is None:
            unknowns.append("batch_size is unknown")
        if workload.get("concurrency") is None:
            unknowns.append("concurrency is unknown")
        sla = workload.get("sla") or {}
        if not any(v is not None for v in sla.values()):
            unknowns.append("SLA targets are unknown")
    else:
        gb = workload.get("global_batch_size")
        seq = workload.get("sequence_length")
        if gb is not None and seq is not None:
            derived["allocated_tokens_per_step_baseline"] = gb * seq
        else:
            unknowns.append("allocated_tokens_per_step requires global_batch_size and sequence_length")
    return derived, unknowns


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    root = pathlib.Path(args.root).resolve()
    source = (root / args.input).resolve()
    output = (root / args.output).resolve()
    profile = load_yaml(source)
    validate_profile(profile)

    model_path = profile["model"]["path"]
    if not model_path.startswith("models/") or not model_path.endswith(".md"):
        raise ValueError("model.path must point to models/*.md")
    model_fm = frontmatter(root / model_path)
    if model_fm.get("schema_version") != "model-v0.2" or model_fm.get("object_type") != "model":
        raise ValueError(f"{model_path}: expected Model V0.2")

    hardware_spec = profile.get("hardware")
    hardware_out = None
    if hardware_spec is not None:
        if not isinstance(hardware_spec, dict) or not isinstance(hardware_spec.get("path"), str):
            raise ValueError("hardware.path must be a string when hardware is provided")
        hardware_path = hardware_spec["path"]
        if not hardware_path.startswith("chip/") or not hardware_path.endswith(".md"):
            raise ValueError("hardware.path must point to chip/*.md")
        hardware_fm = frontmatter(root / hardware_path)
        if hardware_fm.get("schema_version") != "chip-v0.2":
            raise ValueError(f"{hardware_path}: expected Chip V0.2")
        hardware_out = {"path": hardware_path, "facts": hardware_snapshot(hardware_fm)}

    workload = profile["workload"]
    derived, unknowns = derive_workload(workload)
    warnings: list[str] = []

    context_tokens = workload.get("context_tokens")
    native_context = model_fm.get("context_length")
    if (
        isinstance(context_tokens, int)
        and isinstance(native_context, int)
        and context_tokens > native_context
    ):
        warnings.append(
            f"context_tokens={context_tokens} exceeds model native context_length={native_context}"
        )

    normalized = {
        "schema_version": PROFILE_VERSION,
        "source": args.input,
        "model": {"path": model_path, "facts": model_snapshot(model_fm)},
        "hardware": hardware_out,
        "workload": workload,
        "execution": profile["execution"],
        "parallelism": profile["parallelism"],
        "assumptions": profile["assumptions"],
        "derived": derived,
        "warnings": warnings,
        "unknowns": unknowns,
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(json_safe(normalized), ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"workload_profile={output.relative_to(root)} warnings={len(warnings)} unknowns={len(unknowns)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
