---
schema_version: software-v0.1
name: FlagPerf
object_type: project
category: benchmark
organization: flagos-ai
status: active
repo: https://github.com/flagos-ai/FlagPerf
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - ai-benchmark
  - heterogeneous-benchmark
integrations: []
backends: []
updated: 2026-09-16
---
# FlagPerf

> 面向异构 AI 系统与模型的性能评测项目。

## 核心能力

提供跨软件栈、跨硬件的性能评测入口，适合把理论能力和实际 workload 表现连接起来。[S1]

## 边界

FlagPerf 是 benchmark/评测项目，不负责模型执行或资源调度。

## 集成与后端

可用于观察 [[software/projects/vllm|vLLM]]、[[software/projects/sglang|SGLang]] 等引擎在不同硬件栈上的真实性能差异。

## 关联项目

- [[software/projects/flagos|FlagOS]]
- [[software/projects/flagrelease|FlagRelease]]
- [[software/projects/vllm|vLLM]]
- [[software/projects/sglang|SGLang]]

## 版本快照

本页以 2026-09-15 前公开资料为快照。

## 直接来源

- [S1] https://github.com/flagos-ai/FlagPerf
