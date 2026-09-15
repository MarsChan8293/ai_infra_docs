---
schema_version: software-v0.1
name: Colossal-AI
object_type: project
category: other
organization: hpcaitech
status: active
repo: https://github.com/hpcaitech/ColossalAI
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - distributed-training
  - parallelism
  - large-model-training
integrations: []
backends:
  - nvidia
updated: 2026-09-15
---
# Colossal-AI

> 面向大模型训练与分布式并行的开源系统。

## 核心能力

覆盖分布式训练、并行策略、内存优化等，是当前软件图谱从推理向训练侧延伸的重要入口。

## 边界

Colossal-AI 主线是训练与大模型系统，不应和 [[software/projects/vllm|vLLM]] 这类在线推理引擎混为一类。

## 集成与后端

与 [[software/projects/oneflow|OneFlow]]、[[software/projects/flagscale|FlagScale]] 构成训练/分布式系统对照组。

## 关联项目

- [[software/projects/oneflow|OneFlow]]
- [[software/projects/flagscale|FlagScale]]
- [[software/projects/nccl|NCCL]]

## 版本快照

本页以 2026-09-15 前公开资料为快照。

## 直接来源

- https://github.com/hpcaitech/ColossalAI
