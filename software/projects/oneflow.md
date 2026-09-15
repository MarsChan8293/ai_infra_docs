---
schema_version: software-v0.1
name: OneFlow
object_type: project
category: other
organization: Oneflow-Inc
status: active
repo: https://github.com/Oneflow-Inc/oneflow
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - deep-learning-framework
  - distributed-training
  - tensor-runtime
integrations: []
backends:
  - nvidia
  - cpu
updated: 2026-09-15
---
# OneFlow

> 面向深度学习与分布式训练的开源框架和 tensor runtime。

## 核心能力

提供 tensor 计算、自动求导与分布式执行能力，是 AI Infra 中训练 runtime / framework 侧的重要节点。

## 边界

OneFlow 不是 LLM serving control plane；在本仓库中主要用于补足训练与 runtime 方向。

## 集成与后端

与 [[software/projects/colossal-ai|Colossal-AI]]、[[software/projects/flagscale|FlagScale]] 做训练框架与分布式执行对照。

## 关联项目

- [[software/projects/colossal-ai|Colossal-AI]]
- [[software/projects/flagscale|FlagScale]]
- [[software/projects/nccl|NCCL]]

## 版本快照

本页以 2026-09-15 前公开资料为快照。

## 直接来源

- https://github.com/Oneflow-Inc/oneflow
