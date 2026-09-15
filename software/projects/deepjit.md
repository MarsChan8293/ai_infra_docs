---
schema_version: software-v0.1
name: DeepJIT
object_type: project
category: compiler
organization: deepseek-ai
status: active
repo: https://github.com/deepseek-ai/DeepJIT
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - jit-compilation
  - gpu-kernel-generation
integrations: []
backends:
  - gpu
updated: 2026-09-15
---
# DeepJIT

> DeepSeek 开源的 GPU kernel JIT / 编译探索项目。

## 核心能力

关注高性能 kernel 的即时生成和编译执行，为模型算子提供更灵活的性能优化路径。

## 边界

DeepJIT 位于编译与 kernel 层，不负责 serving、路由或集群调度。

## 集成与后端

适合与 [[software/projects/triton|Triton]]、[[software/projects/tilelang|TileLang]]、[[software/projects/flagtree|FlagTree]] 对比不同 kernel DSL / compiler 路线。

## 关联项目

- [[software/projects/deepseek-infra|DeepSeek-Infra]]
- [[software/projects/triton|Triton]]
- [[software/projects/tilelang|TileLang]]
- [[software/projects/deepgemm|DeepGEMM]]

## 版本快照

本页以 2026-09-15 前公开资料为快照。

## 直接来源

- https://github.com/deepseek-ai/DeepJIT
