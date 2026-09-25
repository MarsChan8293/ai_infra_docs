---
schema_version: system-v0.1
name: Prefix Caching
object_type: concept
category: serving
inputs:
  - workload.logical_prompt_tokens
  - workload.reused_prompt_tokens
  - workload.request_rate
  - memory.kv_bytes_per_token
  - memory.cache_capacity
  - topology.cache_location
constraints:
  - cache-capacity
  - lookup-latency
  - retrieval-bandwidth
  - invalidation
  - isolation
outputs:
  - recomputed_prompt_tokens
  - prefix_hit_ratio
  - saved_prefill_work
  - cache_resident_bytes
  - cache_break_even
assumptions:
  - 命中率必须由 workload 或测量给出，不能因为启用 cache 就默认为高命中
  - token reuse、request hit 和 byte hit 是不同指标
related_layers:
  - workload
  - compute
  - memory
  - topology
  - scheduling
  - storage
evidence: {}
updated: 2026-09-25
tags: [system, serving, prefix-cache]
---
# Prefix Caching

> Prefix Caching 用已计算过的上下文状态换取新的 Prefill 计算。系统收益取决于真实复用、状态容量、lookup/retrieval 成本和生命周期，而不是“有缓存就一定更快”。

## Token 口径

定义：

```text
logical_prompt_tokens
= reused_prompt_tokens + recomputed_prompt_tokens
```

因此：

```text
recomputed_prompt_tokens
= logical_prompt_tokens - reused_prompt_tokens
```

Token-based reuse ratio：

```text
reuse_ratio
= reused_prompt_tokens / logical_prompt_tokens
```

它与 request hit ratio 不同。

## Saved Work

在架构和实现允许复用的前提下：

```text
saved_prefill_work
≈ work(logical prompt)
 - work(recomputed prompt)
```

长上下文 attention 可能是非线性 work，因此不能总用 reused token 比例直接等比例估 FLOPs。

## Cache Cost

缓存会消耗：

- KV / recurrent state capacity
- metadata
- lookup
- eviction
- remote retrieval bandwidth
- tenant isolation bookkeeping

若 cache 不在本地，还需通过 [[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层级]] 计算 retrieve 路径。

## Break-even

最基本收益条件：

```text
T_lookup + T_retrieve + T_restore
<
T_recompute_saved
```

并且命中后的端到端时间仍需满足 SLA。

## Eviction

Eviction 需要考虑：

- recency/frequency
- state bytes
- expected reuse
- tenant/session boundary
- cost to recompute
- remote tier availability

单纯按 entry 数量比较不够，因为不同 prefix 长度的 byte cost 差异很大。

## Isolation / Invalidation

复用状态必须有清晰的：

- identity/key
- model/version boundary
- tenant/session boundary
- invalidation semantics

系统层只记录这些约束，项目级实现仍由 relationship 仓库维护。

## 输出

- `recomputed_prompt_tokens`
- `prefix_hit_ratio`
- `saved_prefill_work`
- `cache_resident_bytes`
- `cache_break_even`

## 直接来源

本页定义通用 prefix-cache 成本模型，不绑定具体推理引擎，因此 `evidence: {}`。
