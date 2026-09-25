---
schema_version: system-v0.1
name: Data Parallelism
object_type: concept
category: parallelism
inputs:
  - training.global_batch_size
  - training.micro_batch_size
  - parallelism.dp_degree
  - model.trainable_parameters
  - execution.gradient_precision
constraints:
  - gradient-communication
  - model-replication
  - optimizer-memory
  - synchronization
outputs:
  - per_replica_batch
  - gradient_payload_bytes
  - dp_collective_pattern
  - replica_memory_cost
  - dp_scaling_limits
assumptions:
  - 训练 DP 与推理 replica scaling 分开建模
  - replicated DP baseline 不代表所有 sharded data-parallel variants
related_layers:
  - workload
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
  - data-parallel
---
# Data Parallelism

> Data Parallelism 主要沿 batch / sample 维度扩展。训练时关键成本是模型/状态复制与 gradient synchronization；推理时多个 replica 可以独立服务不同请求，两者不能混成一个模型。

## Training DP

设 DP degree 为 `D`。

在均匀分配的简单场景：

```text
per_replica_global_batch_share
≈ global_batch / D
```

更具体的 global batch 关系见 [[system/workload/training-workload|Training Workload]]。

## Replicated Baseline

经典 replicated DP 中，每个 replica 通常需要自己的：

- model weights
- gradients
- optimizer-related state

因此扩大 DP degree 不会自动降低单 rank model memory。

如果使用状态分片，则应把：

```text
replicated state
vs
sharded state
```

单独列出，不把所有 data-parallel 方法都称为“完全复制”。

## Gradient Payload

如果有 `P_trainable` 个需要同步的参数，每个 gradient element 为 `b_grad` bytes，则逻辑 gradient payload baseline：

```text
gradient_payload_bytes
≈ P_trainable × b_grad
```

实际通信还受：

- bucket
- compression
- unused/frozen params
- sharding
- overlap

影响。

## All-Reduce

replicated DP 的 gradient aggregation 常可映射为 All-Reduce。

理想 ring per-rank traffic baseline 见：

[[system/communication/all-reduce-all-gather-reduce-scatter|All-Reduce / All-Gather / Reduce-Scatter]]

通信时间不能用 gradient bytes / 单链路峰值直接替代。

## Overlap

Gradient 可以分 bucket，并在 backward 过程中逐步发起通信。

如果某 bucket 的 gradient 已 ready，可与其他层 backward compute overlap。

但最后仍可能有：

```text
exposed tail communication
```

所以 DP scaling 需要关注 non-overlapped communication，而不是总通信量 alone。

## Global Batch Scaling

增加 DP degree 常伴随增大全局 batch，但二者不是必须绑定。

需要显式记录：

- micro batch per replica
- gradient accumulation
- DP degree
- resulting global batch

否则系统 scaling 会悄悄改变训练算法 workload。

## Inference Replica Scaling

推理时多个 replica 可独立处理不同请求：

```text
request stream
→ replica 1 / 2 / ... / D
```

这类 scaling 的主要问题是：

- load balancing
- KV locality
- model weight replication
- queueing

通常不需要每 token gradient collective。

因此不要把 training DP 公式直接套到 serving replica。

## Topology

大规模 training DP group 可能跨 scale-out fabric。

需要评估：

- gradient payload
- collective algorithm
- bisection
- NIC injection
- rack/rail placement

见 [[system/topology/scale-up-vs-scale-out|Scale-up vs Scale-out]]。

## 输出

- `per_replica_batch`
- `gradient_payload_bytes`
- `dp_collective_pattern`
- `replica_memory_cost`
- `dp_scaling_limits`

## 直接来源

本页定义通用 data-parallel workload 与同步关系，没有引入特定框架实现，因此 `evidence: {}`。
