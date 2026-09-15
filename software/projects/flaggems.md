---
schema_version: software-v0.1
name: FlagGems
object_type: project
category: runtime
organization: flagos-ai
status: active
repo: https://github.com/flagos-ai/FlagGems
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - operator-library
  - heterogeneous-kernels
integrations: []
backends: []
updated: 2026-09-15
---
# FlagGems

> FlagOS 生态中的异构算子与高性能 kernel 库。

## 核心能力

聚焦不同加速器上的算子实现与性能优化，为上层训练和推理框架提供可复用 kernel 能力。

## 边界

FlagGems 不承担完整 serving runtime 或训练控制面。

## 集成与后端

适合与 [[software/projects/flashinfer|FlashInfer]]、[[software/projects/deepgemm|DeepGEMM]]、[[software/projects/cutlass|CUTLASS]] 对照不同 kernel 库定位。

## 关联项目

- [[software/projects/flagos|FlagOS]]
- [[software/projects/flagscale|FlagScale]]
- [[software/projects/flagattention|FlagAttention]]
- [[software/projects/flagtree|FlagTree]]
- [[software/projects/flashinfer|FlashInfer]]

## 版本快照

本页以 2026-09-15 前公开资料为快照。

## 直接来源

- https://github.com/flagos-ai/FlagGems
