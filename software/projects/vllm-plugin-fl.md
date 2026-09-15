---
schema_version: software-v0.1
name: vllm-plugin-FL
object_type: project
category: runtime
organization: flagos-ai
status: active
repo: https://github.com/flagos-ai/vllm-plugin-FL
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - vllm-plugin
  - heterogeneous-backend
integrations:
  - vllm
backends: []
updated: 2026-09-15
---
# vllm-plugin-FL

> FlagOS 生态面向 vLLM 的异构适配插件。

## 核心能力

通过插件方式把 FlagOS/异构后端能力接入 vLLM，避免所有适配都直接侵入上游核心代码。

## 边界

它依赖 [[software/projects/vllm|vLLM]] 的插件/后端接口，不是独立推理引擎。

## 集成与后端

- 上游：[[software/projects/vllm|vLLM]]。
- 社区：[[software/projects/flagos|FlagOS]]。

## 关联项目

- [[software/projects/vllm|vLLM]]
- [[software/projects/flagos|FlagOS]]
- [[software/projects/sglang-plugin-fl|sglang-plugin-FL]]

## 版本快照

本页以 2026-09-15 前公开资料为快照。

## 直接来源

- https://github.com/flagos-ai/vllm-plugin-FL
