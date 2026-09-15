---
schema_version: software-v0.1
name: FlagScale
object_type: project
category: training
organization: flagos-ai
status: active
repo: https://github.com/flagos-ai/FlagScale
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - distributed-training
  - large-model-training
integrations: []
backends: []
updated: 2026-09-16
---
# FlagScale

> FlagOS 生态中的大模型训练与规模化系统项目。

## 核心能力

关注大模型训练、并行与异构资源上的规模化执行，是软件图谱训练侧的重要节点。[S1]

## 边界

FlagScale 主线是训练系统，不属于在线 LLM serving engine。

## 集成与后端

与 [[software/projects/colossal-ai|Colossal-AI]]、[[software/projects/oneflow|OneFlow]] 构成训练系统对照组，并与 [[software/projects/flagcx|FlagCX]] 等底层通信组件形成上下游关系。

## 关联项目

- [[software/projects/flagos|FlagOS]]
- [[software/projects/colossal-ai|Colossal-AI]]
- [[software/projects/oneflow|OneFlow]]
- [[software/projects/flagcx|FlagCX]]
- [[software/projects/flaggems|FlagGems]]

## 版本快照

本页以 2026-09-15 前公开资料为快照。

## 直接来源

- [S1] https://github.com/flagos-ai/FlagScale
