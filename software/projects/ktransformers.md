---
schema_version: software-v0.1
name: KTransformers
object_type: project
category: inference-engine
organization: kvcache-ai
status: active
repo: https://github.com/kvcache-ai/ktransformers
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - heterogeneous-inference
  - cpu-gpu-offload
  - moe-inference
integrations: []
backends:
  - cpu
  - nvidia
updated: 2026-09-15
---
# KTransformers

> 面向大模型特别是 MoE 场景的异构 CPU/GPU 推理与算子优化项目。

## 核心能力

重点研究权重、专家与计算在 CPU/GPU 等资源之间的放置，以及在有限 GPU 显存下运行大模型的工程路径。

## 边界

KTransformers 的主线是异构执行与内存/计算协同，不等价于通用 Kubernetes serving control plane。

## 集成与后端

- 与 [[software/projects/llama-cpp|llama.cpp]] 都代表非纯数据中心 GPU 的推理路线。
- 与 [[software/projects/vllm|vLLM]]、[[software/projects/sglang|SGLang]] 可用于比较不同执行和内存管理策略。

## 关联项目

- [[software/projects/vllm|vLLM]]
- [[software/projects/sglang|SGLang]]
- [[software/projects/llama-cpp|llama.cpp]]
- [[software/projects/deepep|DeepEP]]

## 版本快照

本页以 2026-09-15 前公开资料为快照。

## 直接来源

- https://github.com/kvcache-ai/ktransformers
