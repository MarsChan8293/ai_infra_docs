---
schema_version: software-v0.1
name: 3FS
object_type: project
category: storage
organization: deepseek-ai
status: active
repo: https://github.com/deepseek-ai/3FS
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - distributed-file-system
  - high-throughput-storage
integrations: []
backends:
  - linux
updated: 2026-09-16
---
# 3FS

> DeepSeek 开源的高性能分布式文件系统。

## 核心能力

面向 AI/HPC 数据路径提供高吞吐、分布式存储能力，是训练数据、checkpoint 与基础设施数据面值得关注的节点。[S1]

## 边界

3FS 是存储系统，不是 KV Cache runtime，也不直接负责模型计算。

## 集成与后端

在软件图谱中可与 [[software/projects/mooncake|Mooncake]]、[[software/projects/lmcache|LMCache]] 区分：前者更偏通用文件/存储数据面，后两者更贴近推理 KV 生命周期。

## 关联项目

- [[software/projects/deepseek-infra|DeepSeek-Infra]]
- [[software/projects/mooncake|Mooncake]]
- [[software/projects/lmcache|LMCache]]

## 版本快照

本页以 2026-09-15 前公开资料为快照。

## 直接来源

- [S1] https://github.com/deepseek-ai/3FS
