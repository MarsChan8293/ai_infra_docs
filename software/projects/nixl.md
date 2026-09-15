---
schema_version: software-v0.1
name: NIXL
object_type: project
category: communication
organization: ai-dynamo / NVIDIA
status: active
repo: https://github.com/ai-dynamo/nixl
docs: https://github.com/ai-dynamo/nixl/blob/main/docs/nixl.md
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - point-to-point-transfer
  - memory-storage-abstraction
  - plugin-backends
  - gpu-direct
integrations:
  - nvidia-dynamo
  - lmcache
  - ucx
backends:
  - nvidia
  - cpu
  - storage
updated: 2026-09-15
---
# NIXL

> 面向分布式 AI 推理的数据传输抽象层，统一 HBM、DRAM 与存储数据路径。

## 核心能力

| 能力 | 说明 |
|---|---|
| P2P Transfer | 提供高带宽、低延迟点到点传输 API |
| Memory / Storage Abstraction | 统一 HBM、DRAM、SSD 等数据位置 |
| Plugin Backend | 通过插件连接 UCX、GDS 等后端 |
| Inference Data Plane | 服务于 KV、权重和其他推理数据移动 |

## 边界

NIXL 是数据移动库，不做请求路由、模型执行或集群资源 placement。

## 集成与后端

- [[software/projects/nvidia-dynamo|NVIDIA Dynamo]]：NIXL 面向的分布式推理框架之一。
- [[software/projects/lmcache|LMCache]]：KV 传输路径之一。
- [[software/projects/ucx|UCX]]：NIXL 的通信 backend 之一。

## 关联项目

- KV-centric 数据系统：[[software/projects/mooncake|Mooncake]]。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前官方仓库为快照。

## 直接来源

- https://github.com/ai-dynamo/nixl
- https://github.com/ai-dynamo/nixl/blob/main/docs/nixl.md
