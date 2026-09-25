---
schema_version: system-v0.1
name: Context Parallelism
object_type: concept
category: parallelism
inputs:
  - model.attention
  - workload.sequence_length
  - workload.batch_size
  - parallelism.cp_degree
  - memory.kv_layout
constraints:
  - sequence-memory
  - attention-dependency
  - communication
  - topology
outputs:
  - sequence_partition
  - per_rank_context_tokens
  - per_rank_kv_partition
  - cp_communication_pattern
  - cp_scaling_limits
assumptions:
  - sequence shard 不意味着 attention 完全独立
  - 具体通信量必须绑定 attention algorithm 和 KV layout
related_layers:
  - model
  - workload
  - compute
  - memory
  - parallelism
  - communication
  - topology
  - accelerator
  - network
evidence: {}
updated: 2026-09-25
tags:
  - system
  - parallelism
  - context-parallel
  - long-context
---
# Context Parallelism

> Context Parallelism 沿 sequence/context 维度切分长上下文。它可以降低单 rank 的 sequence-dependent state 与 compute 压力，但 attention dependency 决定了 rank 之间仍需要交换信息。

## Sequence Partition

设单序列长度为 `S`，CP degree 为 `C`。

均匀 token shard baseline：

```text
local_sequence_tokens
≈ S / C
```

但实际分片可能按：

- contiguous blocks
- striped tokens
- attention block
- ring order
- head/context hybrid

组织。

## KV Partition

若 growing KV 可按 context shard：

```text
local_kv_payload
≈ global_kv_payload / C
```

只在均匀且无复制的情况下成立。

实际还可能：

- replicate boundary/state
- exchange remote KV
- cache remote blocks
- use local window + global tokens

因此 per-device KV 仍需 [[system/memory/kv-cache-model|KV Cache Model]] 按实际 layout 计算。

## Attention Dependency

Full attention 中，一个 query 需要访问可见 context。

sequence 被切到多个 rank 后，必须解决：

```text
local query
needs information from remote context
```

不同算法可能交换：

- K/V blocks
- Q blocks
- partial attention statistics
- partial outputs

因此没有一个对所有 CP 算法通用的固定 communication bytes 公式。

## Compute

CP 可以分摊 context-related attention work，但也会引入：

- communication
- synchronization
- numerical combine
- smaller local shapes

所以：

```text
local attention FLOPs ↓
```

不自动推出：

```text
step time ∝ 1 / C
```

## Long Context Capacity

CP 的主要价值之一是把：

- KV
- attention state
- activation

沿 context 分散到多个设备。

但是否真的解除 capacity 限制，取决于 replicated state 与 communication buffer。

## Topology

长上下文 attention 往往需要多轮 context exchange。

因此 CP group 应关注：

- bandwidth
- latency
- topology symmetry
- rank order
- scale-up domain

如果 CP 跨 scale-out，通信成本可能快速上升。

## CP × TP

TP 切 hidden/tensor，CP 切 sequence。

组合后可能形成二维 process grid：

```text
TP dimension × CP dimension
```

每个维度有不同 collective/data dependency。

调度器需要保留 group identity，而不是只看到 world size。

## Decode

Decode 时 query token 很少，但历史 context 很大。

CP 可能让 KV 分布到多个 rank，但每步仍需完成跨 shard attention combine。

因此它可能缓解 capacity，却增加 per-token communication latency。

## 输出

- `sequence_partition`
- `per_rank_context_tokens`
- `per_rank_kv_partition`
- `cp_communication_pattern`
- `cp_scaling_limits`

## 直接来源

本页定义通用 Context Parallel 边界和 dependency，不绑定具体 attention 算法实现，因此 `evidence: {}`。
