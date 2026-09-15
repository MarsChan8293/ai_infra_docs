---
schema_version: software-v0.1
name: MindIE-Motor
object_type: project
category: runtime
organization: Ascend
status: active
repo: null
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - inference-runtime
  - ascend-runtime
integrations: []
backends:
  - ascend
updated: 2026-09-15
---
# MindIE-Motor

> Ascend/MindIE 生态中的推理 runtime / 执行组件。

## 核心能力

关注模型推理执行与运行时能力，为 Ascend 上层模型服务提供执行基础。

## 边界

它不是 Kubernetes 调度器，也不是通用跨厂商推理引擎。

## 集成与后端

与 [[software/projects/mindie-llm|MindIE-LLM]]、[[software/projects/ops-transformer|ops-transformer]] 共同构成 Ascend 推理软件链。

## 关联项目

- [[software/projects/mindie-llm|MindIE-LLM]]
- [[software/projects/ops-transformer|ops-transformer]]
- [[software/projects/vllm-ascend|vLLM-Ascend]]

## 版本快照

本页以 2026-09-15 前 Ascend 公开生态资料为快照；未确认独立 canonical GitHub 仓库。

## 直接来源

- https://github.com/Ascend
