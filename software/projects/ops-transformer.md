---
schema_version: software-v0.1
name: ops-transformer
object_type: project
category: runtime
organization: Ascend
status: active
repo: https://github.com/Ascend/ops-transformer
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - transformer-operators
  - ascend-kernels
integrations: []
backends:
  - ascend
updated: 2026-09-15
---
# ops-transformer

> 面向 Ascend Transformer 模型的算子与 kernel 优化项目。

## 核心能力

提供 Transformer 相关算子实现与优化，是 Ascend 推理 runtime 下方的重要 kernel 层节点。

## 边界

ops-transformer 不承担完整 serving runtime 或请求路由。

## 集成与后端

与 [[software/projects/mindie-llm|MindIE-LLM]]、[[software/projects/vllm-ascend|vLLM-Ascend]] 形成上层引擎与底层算子的关系。

## 关联项目

- [[software/projects/mindie-llm|MindIE-LLM]]
- [[software/projects/vllm-ascend|vLLM-Ascend]]
- [[software/projects/mindie-motor|MindIE-Motor]]

## 版本快照

本页以 2026-09-15 前公开资料为快照。

## 直接来源

- https://github.com/Ascend/ops-transformer
