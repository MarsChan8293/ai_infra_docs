---
schema_version: system-v0.1
name: All-Reduce / All-Gather / Reduce-Scatter
object_type: concept
category: communication-model
inputs:
  - communication.collective_type
  - communication.logical_tensor_bytes
  - communication.participant_count
  - communication.algorithm
  - topology.effective_bandwidth
  - topology.per_step_latency
constraints:
  - startup-latency
  - transfer-bandwidth
  - synchronization
  - topology
outputs:
  - per_rank_bytes
  - algorithm_steps
  - communication_time_lower_bound
  - scaling_behavior
assumptions:
  - 公式必须先定义 logical tensor size 的含义
  - Ring 公式只描述理想均衡 baseline，不代表任意实现
related_layers:
  - parallelism
  - communication
  - topology
  - accelerator
  - network
evidence: {}
updated: 2026-09-25
tags:
  - system
  - communication
  - collective
---
# All-Reduce / All-Gather / Reduce-Scatter

> 这三个 collective 是 TP、DP 和参数/activation 分片最常见的通信构件。分析时必须先固定 tensor size 的定义，再谈每 rank bytes 和时间。

## 统一符号

设：

- `N`：participant count
- `M`：完整逻辑 tensor 的大小，单位 bytes
- `alpha`：每个必须串行 communication step 的固定时延
- `B`：critical path 上的 effective bandwidth

这里 `M` 的定义在三种 collective 中保持一致：都表示完整逻辑结果的 tensor size。

## All-Gather

每个 rank 起始拥有约：

```text
M / N
```

最终每个 rank 拥有完整 `M`。

因此每 rank 至少需要接收其他 shard：

```text
bytes_received_per_rank
= (N - 1) / N × M
```

理想 ring baseline 下，发送量同阶：

```text
bytes_sent_per_rank
≈ (N - 1) / N × M
```

若 ring 有 `N-1` 个串行 step：

```text
T_ring_allgather
≈ (N - 1) × alpha
+ ((N - 1) / N × M) / B
```

这是 lower-fidelity baseline，不含 contention 和不均匀 topology。

## Reduce-Scatter

每个 rank 参与对完整逻辑 tensor 的 reduction，最终只保留约 `M/N`。

理想 ring baseline：

```text
bytes_per_rank
≈ (N - 1) / N × M
```

时间骨架同样可写为：

```text
T_ring_reducescatter
≈ (N - 1) × alpha
+ ((N - 1) / N × M) / B
```

实际 reduction compute、protocol 和 chunking 可能增加额外成本。

## All-Reduce

常见分解：

```text
All-Reduce
= Reduce-Scatter
+ All-Gather
```

因此理想 ring baseline 的 per-rank transferred payload 约：

```text
bytes_per_rank
≈ 2 × (N - 1) / N × M
```

时间：

```text
T_ring_allreduce
≈ 2 × (N - 1) × alpha
+ [2 × (N - 1) / N × M] / B
```

这个公式的价值是展示两个 scaling 项：

- latency steps 随 `N` 增长
- bandwidth term 在大 `N` 时趋近 `2M/B`

## Tree 与分层算法

Tree 风格算法可以降低某些 latency step 数量，概念上接近：

```text
O(log N)
```

但实际 traffic、root/link pressure 和 reduction placement 与 ring 不同。

在 node 内与 node 间带宽差异很大时，还可能使用 hierarchical collective：

```text
intra-domain phase
→ inter-domain phase
→ intra-domain phase
```

因此算法选择必须绑定 [[system/topology/scale-up-vs-scale-out|Scale-up / Scale-out]] topology。

## TP 与 DP

[[system/parallelism/tensor-parallelism|Tensor Parallelism]] 往往把 collective 放在 layer critical path 上，因此更敏感于 latency。

[[system/parallelism/data-parallelism|Data Parallelism]] 的 gradient sync 通常消息更大，但可以尝试 chunk / overlap。

同一个 All-Reduce 在两种 workload 中的性能含义不同。

## 输出

- `per_rank_bytes`
- `algorithm_steps`
- `communication_time_lower_bound`
- `scaling_behavior`

实际时间统一进入 [[system/communication/communication-cost-model|Communication Cost Model]]。

## 直接来源

本页公式来自 collective 数据守恒与 ring baseline 的第一性原理分解，没有引入具体实现 benchmark，因此 `evidence: {}`。
