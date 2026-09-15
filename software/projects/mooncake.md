---
schema_version: software-v0.1
name: Mooncake
object_type: project
category: kv-cache
organization: KVCache.AI / Moonshot ecosystem
status: active
repo: https://github.com/kvcache-ai/Mooncake
docs: https://github.com/kvcache-ai/Mooncake
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - transfer-engine
  - distributed-kv-store
  - rdma
  - kv-cache-sharing
integrations:
  - vllm
  - sglang
backends:
  - nvidia
  - cambricon
  - hygon
  - iluvatar
updated: 2026-09-15
---
# Mooncake

> 面向 KVCache-centric serving 的高性能数据传输与分布式 KV 存储系统。

## 核心能力

| 能力 | 说明 |
|---|---|
| Transfer Engine | 在 GPU、DRAM 等位置间搬运大块数据 |
| Mooncake Store | 提供分布式 KV Cache 存储能力 |
| RDMA / GPUDirect | 面向高吞吐、低拷贝的数据路径 |
| Serving Integration | 与主流 LLM serving 引擎衔接 |

## 边界

Mooncake 的主战场是 KV 与数据面，不负责完整模型 forward 或通用 Kubernetes 调度。

## 集成与后端

- [[software/projects/vllm|vLLM]]、[[software/projects/sglang|SGLang]]：已存在明确的 serving / 数据传输集成路径。

## 关联项目

- KV 管理：[[software/projects/lmcache|LMCache]]。
- 数据传输抽象：[[software/projects/nixl|NIXL]]。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前官方仓库为快照。

## 直接来源

- https://github.com/kvcache-ai/Mooncake
