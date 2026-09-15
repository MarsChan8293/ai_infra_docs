---
schema_version: software-v0.1
name: TileLang
object_type: project
category: compiler
organization: tile-ai
status: active
repo: https://github.com/tile-ai/tilelang
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - kernel-dsl
  - gpu-kernel-generation
integrations: []
backends:
  - gpu
updated: 2026-09-15
---
# TileLang

> 面向高性能 GPU kernel 开发的 tile-oriented DSL / compiler 路线。

## 核心能力

用于更高层地表达矩阵、attention 等计算，并生成面向 GPU 的高性能实现。

## 边界

TileLang 位于 kernel 编译层，不负责模型 serving 或请求调度。

## 集成与后端

适合与 [[software/projects/triton|Triton]]、[[software/projects/cutlass|CUTLASS]]、[[software/projects/flashinfer|FlashInfer]] 进行 kernel 编程模型对比。

## 关联项目

- [[software/projects/triton|Triton]]
- [[software/projects/cutlass|CUTLASS]]
- [[software/projects/flashinfer|FlashInfer]]
- [[software/projects/deepjit|DeepJIT]]
- [[software/projects/flagtree|FlagTree]]

## 版本快照

本页以 2026-09-15 前公开资料为快照。

## 直接来源

- https://github.com/tile-ai/tilelang
