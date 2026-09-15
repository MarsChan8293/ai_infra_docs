---
schema_version: software-v0.1
name: vLLM-Ascend
object_type: project
category: inference-engine
organization: vllm-project
status: active
repo: https://github.com/vllm-project/vllm-ascend
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - vllm-ascend-backend
  - ascend-inference
integrations:
  - vllm
backends:
  - ascend
updated: 2026-09-15
---
# vLLM-Ascend

> 把 vLLM 推理栈适配到华为 Ascend/CANN 生态的开源项目。

## 核心能力

项目承接 vLLM 的 serving/runtime 抽象，并把设备执行、算子与通信路径适配到 Ascend 后端。

## 边界

它不是独立于 vLLM 的全新 serving 架构；很多上层语义仍来自 [[software/projects/vllm|vLLM]]，硬件能力则受 Ascend/CANN 软件栈约束。

## 集成与后端

- 上游：[[software/projects/vllm|vLLM]]。
- Ascend 侧可与 [[software/projects/mindie-llm|MindIE-LLM]]、[[software/projects/ops-transformer|ops-transformer]] 做路线对照。

## 关联项目

- [[software/projects/vllm|vLLM]]
- [[software/projects/mindie-llm|MindIE-LLM]]
- [[software/projects/ops-transformer|ops-transformer]]

## 版本快照

Ascend 后端支持变化较快，本页以 2026-09-15 前公开资料为快照，不默认与 CUDA 路径功能完全对齐。

## 直接来源

- https://github.com/vllm-project/vllm-ascend
