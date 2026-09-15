---
schema_version: software-v0.1
name: Prefill / Decode 分离
object_type: concept
category: serving-architecture
updated: 2026-09-15
---
# Prefill / Decode 分离

> 将 Prefill 与 Decode 放到不同 worker 或资源池，以分别优化两种不同资源特征的阶段。

## 问题

Prefill 通常更偏计算密集，Decode 通常更依赖 HBM 带宽和低逐 token 延迟。混在同一资源池时，两类请求容易互相干扰。

## 核心机制

```text
Request
  → [[software/projects/llm-d|llm-d]] 选择 P / D worker
  → [[software/projects/vllm|vLLM]] Prefill 生成 KV
  → [[software/projects/lmcache|LMCache]] / transport 搬运 KV
  → Decode worker 继续生成 token
```

## 判断要点

- KV 搬运成本必须低于重新计算或混跑造成的损失。
- 同时观察 TTFT、TPOT、KV 大小、网络带宽、排队和失败恢复。
- worker 如何放置是集群调度问题，请结合 [[software/concepts/topology-aware-scheduling|拓扑感知调度]]。

## 相关项目与概念

- [[software/projects/vllm|vLLM]]
- [[software/projects/lmcache|LMCache]]
- [[software/projects/llm-d|llm-d]]
- [[software/concepts/kv-cache-lifecycle|KV Cache 生命周期]]
