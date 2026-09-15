---
schema_version: software-v0.1
name: MindIE-LLM
object_type: project
category: inference-engine
organization: Ascend
status: active
repo: null
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - llm-inference
  - ascend-inference
integrations: []
backends:
  - ascend
updated: 2026-09-15
---
# MindIE-LLM

> 华为 Ascend/MindIE 生态中的大模型推理执行与服务组件。

## 核心能力

用于 Ascend 平台上的大模型推理、模型执行与相关 serving 能力，是国产 NPU 推理栈的重要路线。

## 边界

MindIE-LLM 属于 Ascend 原生推理生态，与 [[software/projects/vllm-ascend|vLLM-Ascend]] 的社区适配路线不同，不应简单视作同一实现。

## 集成与后端

- Ascend 后端。
- 与 [[software/projects/mindie-motor|MindIE-Motor]]、[[software/projects/ops-transformer|ops-transformer]] 同属 Ascend 推理优化生态。

## 关联项目

- [[software/projects/vllm-ascend|vLLM-Ascend]]
- [[software/projects/mindie-motor|MindIE-Motor]]
- [[software/projects/ops-transformer|ops-transformer]]
- [[software/projects/msmodelslim|msModelSlim]]

## 版本快照

本页以 2026-09-15 前 Ascend 公开生态资料为快照；未确认独立 canonical GitHub 仓库，因此 `repo` 保持 null。

## 直接来源

- https://github.com/Ascend
