---
schema_version: software-v0.1
name: FlagTree
object_type: project
category: compiler
organization: flagos-ai
status: active
repo: https://github.com/flagos-ai/FlagTree
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - kernel-dsl
  - compiler
  - heterogeneous-codegen
integrations: []
backends: []
updated: 2026-09-15
---
# FlagTree

> FlagOS 生态中的异构 kernel DSL / compiler 项目。

## 核心能力

用于表达和生成面向不同加速器的高性能 kernel，是异构编译路线的重要观察对象。

## 边界

FlagTree 处于编译层，不承担模型 serving 或训练调度。

## 集成与后端

适合与 [[software/projects/triton|Triton]]、[[software/projects/tilelang|TileLang]]、[[software/projects/deepjit|DeepJIT]] 比较 DSL 和 codegen 模型。

## 关联项目

- [[software/projects/flagos|FlagOS]]
- [[software/projects/flaggems|FlagGems]]
- [[software/projects/triton|Triton]]
- [[software/projects/tilelang|TileLang]]
- [[software/projects/deepjit|DeepJIT]]

## 版本快照

本页以 2026-09-15 前公开资料为快照。

## 直接来源

- https://github.com/flagos-ai/FlagTree
