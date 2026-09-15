---
schema_version: software-v0.1
name: VCCL
object_type: project
category: communication
organization: sii-research
status: active
repo: https://github.com/sii-research/vccl
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - collective-communication
  - accelerator-communication
integrations: []
backends: []
updated: 2026-09-15
---
# VCCL

> 面向 AI 加速器的集合通信研究与实现项目。

## 核心能力

关注多设备集合通信与异构加速器通信路径，可作为 NCCL/RCCL 之外的通信实现观察对象。

## 边界

VCCL 处在通信层，不负责模型执行、请求调度或 Kubernetes placement。

## 集成与后端

可与 [[software/projects/nccl|NCCL]]、[[software/projects/rccl|RCCL]]、[[software/projects/flagcx|FlagCX]] 做横向比较。

## 关联项目

- [[software/projects/nccl|NCCL]]
- [[software/projects/rccl|RCCL]]
- [[software/projects/flagcx|FlagCX]]
- [[software/projects/ucx|UCX]]

## 版本快照

本页以 2026-09-15 前公开资料为快照。

## 直接来源

- https://github.com/sii-research/vccl
