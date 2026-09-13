---
title: KV Cache 生命周期
aliases:
  - KV Cache Lifecycle
  - KV 缓存生命周期
tags:
  - concept
  - kv-cache
  - inference
---

# KV Cache 生命周期

KV Cache 不是单一“缓存文件”，而是一条贯穿生成、驻留、复用、迁移、卸载和回收的生命周期。理解这条链路，是判断 prefix cache、外部 KV、P/D 分离是否值得的基础。

## 生命周期

```text
Prompt
  → [[software/inference-engine/vllm|vLLM]] Prefill 生成 KV
  → GPU HBM 中驻留
  → 命中时直接复用
  → [[software/kv-cache/lmcache|LMCache]] 外部化 / 卸载 / 迁移
  → [[software/distributed-serving/llm-d|llm-d]] 根据 KV 状态进行请求路由
  → 冷却、淘汰或请求结束后释放
```

## 关键问题

任何 KV 方案都应回答四件事：命中率是否足够高、搬运是否比重算更便宜、元数据是否能准确定位缓存、失效与多租户隔离是否可靠。只看“能不能存 KV”很容易得到一座昂贵的缓存仓库，却没有真正降低 TTFT。

## 关联

- [[software/concepts/pd-disaggregation|Prefill / Decode 分离]] 会把 KV 传输从可选优化变成关键数据路径。
- [[software/concepts/topology-aware-scheduling|拓扑感知调度]] 决定 GPU、CPU 内存和 NIC 之间的搬运成本。
- [[software/concepts/llm-serving-stack|LLM Serving 软件栈]] 给出 KV 在整体软件栈中的位置。

返回 [[software/README|AI Infra 软件栈地图]]。
