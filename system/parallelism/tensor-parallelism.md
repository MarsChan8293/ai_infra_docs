---
schema_version: system-v0.1
name: Tensor Parallelism
object_type: concept
category: parallelism
inputs:
  - model.layer_weights
  - model.hidden_size
  - workload.batch_size
  - workload.sequence_length
  - parallelism.tp_degree
  - topology.scale_up_domain
constraints:
  - communication-latency
  - collective-bandwidth
  - memory-capacity
  - shape-efficiency
outputs:
  - per_rank_weight_partition
  - per_rank_activation_partition
  - tp_collective_pattern
  - tp_communication_bytes
  - tp_placement_requirements
assumptions:
  - TP degree 不自动等于 speedup
  - 不同 tensor 可以采用不同 shard/replication rule
  - layer critical path 上的 collective 必须单独建模
related_layers:
  - model
  - workload
  - compute
  - memory
  - parallelism
  - communication
  - topology
  - scheduling
  - accelerator
  - network
evidence: {}
updated: 2026-09-25
tags:
  - system
  - parallelism
  - tensor-parallel
---
# Tensor Parallelism

> Tensor Parallelism 在单个 layer 内切分权重、activation 或算子 work。它解决“单层太大或单卡算不完”的问题，同时把 collective 放进 layer critical path。

## 基本对象

设 TP degree 为 `T`。

一个 tensor 的 partition 可能是：

```text
global tensor
→ T local shards
```

也可能：

```text
global tensor
→ partially sharded
+ replicated components
```

因此 per-rank memory 不能无条件写成 global / T。

## Column / Row 方向

对线性层：

```text
Y = X W
```

可以按 W 的不同维度切分。

不同切法会决定：

- input 是否复制或分片
- output 是否分片
- 后续是否需要 All-Gather
- 是否需要 Reduce-Scatter / All-Reduce

本仓库不把某个框架的具体实现设成唯一标准，只记录数据依赖。

## Communication

TP 常用的通信原语见：

[[system/communication/all-reduce-all-gather-reduce-scatter|All-Reduce / All-Gather / Reduce-Scatter]]

如果某个 layer 每次 forward 都需要 collective，则通信频率约与 layer 数和 token step 数共同增长。

因此即使消息不大，startup latency 也可能进入 critical path。

## Per-rank Compute

理想均匀 shard 下，某些矩阵 work 可以近似：

```text
local_FLOPs ≈ global_FLOPs / T
```

但实际还会受：

- replicated work
- uneven dimensions
- padding
- kernel shape degradation
- collective dependency

影响。

所以不能直接用 `global FLOPs / T` 当作 step time。

## Weight Memory

TP 可降低部分 local weight bytes，但需要明确：

- 哪些 tensor shard
- 哪些 tensor replicate
- quant metadata 是否 replicate
- runtime transformed copy

统一进入 [[system/memory/weight-memory|Weight Memory Model]]。

## Activation

Activation 也可能：

- shard
- gather
- reduce-scatter
- temporarily replicate

所以 local activation peak 需要和 collective buffer 一起看。

见 [[system/memory/activation-memory|Activation Memory Model]]。

## Topology

TP 通常是高频、同步敏感的 group。

placement 应优先评估：

- 同一 scale-up domain 是否可容纳整个 TP group
- collective latency
- effective bandwidth
- non-uniform link
- failure domain

见 [[system/topology/scale-up-vs-scale-out|Scale-up vs Scale-out]]。

## Decode 敏感度

Decode 中 batch 较小时，compute shard 后每 rank 的 matrix shape 可能进一步变小，而 collective latency 仍然存在。

因此增加 TP degree 可能：

```text
memory pressure ↓
local compute ↓
communication fraction ↑
```

是否值得增加 TP 必须绑定 workload。

## 输出

- `per_rank_weight_partition`
- `per_rank_activation_partition`
- `tp_collective_pattern`
- `tp_communication_bytes`
- `tp_placement_requirements`

## 直接来源

本页定义通用 tensor partition 与 collective 关系，没有引入特定框架实现或 benchmark，因此 `evidence: {}`。
