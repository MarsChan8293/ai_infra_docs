---
schema_version: software-v0.1
name: msModelSlim
object_type: project
category: other
organization: Ascend
status: active
repo: null
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - model-compression
  - quantization
integrations: []
backends:
  - ascend
updated: 2026-09-15
---
# msModelSlim

> Ascend 生态中的模型压缩与量化工具链。

## 核心能力

关注量化、压缩与部署前模型优化，用于降低推理资源占用并适配 Ascend 执行路径。

## 边界

它是模型优化工具，不是 serving engine 或集群控制面。

## 集成与后端

与 [[software/projects/mindie-llm|MindIE-LLM]]、[[software/projects/mindie-sd|MindIE-SD]] 构成模型优化到推理执行的上下游关系。

## 关联项目

- [[software/projects/mindie-llm|MindIE-LLM]]
- [[software/projects/mindie-sd|MindIE-SD]]
- [[software/projects/vllm-ascend|vLLM-Ascend]]

## 版本快照

本页以 2026-09-15 前 Ascend 公开生态资料为快照；未确认独立 canonical GitHub 仓库。

## 直接来源

- https://github.com/Ascend
