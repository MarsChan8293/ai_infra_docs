---
schema_version: system-v0.1
name: Distributed Training Model
object_type: concept
category: training
inputs:
  - workload.training
  - model.architecture
  - model.trainable_parameters
  - parallelism
  - topology
constraints:
  - compute
  - memory-capacity
  - gradient-communication
  - pipeline-bubble
  - checkpoint
  - failure-recovery
outputs:
  - training_step_graph
  - per_rank_work
  - training_memory_components
  - communication_schedule
  - step_time_components
assumptions:
  - forward、backward、optimizer 与通信分阶段记录
  - 不使用固定倍数从 inference FLOPs 推 training FLOPs
related_layers:
  - model
  - workload
  - compute
  - memory
  - parallelism
  - communication
  - topology
  - storage
  - reliability
  - accelerator
evidence: {}
updated: 2026-09-25
tags:
  - system
  - training
  - distributed-training
---
# Distributed Training Model

> Distributed Training Model 把一个 optimizer step 分成 forward、backward、gradient communication、optimizer、checkpoint 与调度依赖，再映射到 DP/TP/PP/EP/CP。

## Step Graph

概念上：

```text
microbatch forward
→ saved/recomputed activations
→ backward
→ gradient synchronization
→ optimizer update
→ optional checkpoint
```

不同并行策略会改变依赖顺序。

## Workload

基础输入来自：

[[system/workload/training-workload|Training Workload]]

必须明确：

- global batch
- micro batch
- gradient accumulation
- sequence / packing
- checkpoint cadence

## Forward / Backward

Training FLOPs 不能用一个全仓固定“inference × 3”等倍数代替。

Backward 包含：

- activation gradients
- weight gradients
- possible recomputation

具体 work 由架构和 checkpointing 决定。

## Memory

训练主要状态：

```text
weights
+ gradients
+ optimizer states
+ possible master weights
+ saved activations
+ workspace
+ communication buffers
```

完整模型由后续 `TRN-002` 展开。

## Parallelism

可组合：

```text
DP × TP × PP × EP × CP
```

但真实 rank group 未必规则。

各维度入口见 [[system/parallelism/parallelism-overview|Parallelism Overview]]。

## Communication

训练常见：

- DP gradient collective
- TP layer collective
- PP activation P2P
- EP All-to-All
- CP context exchange

通信要按 dependency 决定是否能与 compute overlap。

## Step Time

不能机械求和所有峰值。

更合理地保留：

```text
forward critical path
backward critical path
exposed communication
optimizer
checkpoint amortization
bubble
```

然后按真实 dependency 组合。

## Checkpoint

Checkpoint 不是单纯 storage task，它影响：

- pause / async traffic
- recovery point
- lost work
- network/storage contention

后续 `REL-001` 建模。

## Failure

训练 job 越大、越长，越需要考虑 failure scope 和 recovery。

failure domain 见 [[system/reliability/accelerator-and-network-failure-domain|Accelerator / Network Failure Domain]]。

## 输出

- `training_step_graph`
- `per_rank_work`
- `training_memory_components`
- `communication_schedule`
- `step_time_components`

## 直接来源

本页定义通用 distributed training 系统分解，不引入具体 framework 或 training run，因此 `evidence: {}`。
