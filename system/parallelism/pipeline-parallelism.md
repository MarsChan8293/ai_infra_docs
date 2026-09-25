---
schema_version: system-v0.1
name: Pipeline Parallelism
object_type: concept
category: parallelism
inputs:
  - model.layers
  - parallelism.pp_degree
  - workload.micro_batch_size
  - workload.microbatch_count
  - compute.stage_time
  - activation.stage_boundary_bytes
constraints:
  - pipeline-bubble
  - stage-imbalance
  - p2p-bandwidth
  - p2p-latency
  - activation-memory
outputs:
  - stage_partition
  - stage_compute_time
  - boundary_activation_bytes
  - pipeline_bubble
  - pp_p2p_pattern
assumptions:
  - stage 数相等不代表 stage compute 相等
  - bubble 必须绑定具体 microbatch schedule
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
  - pipeline-parallel
---
# Pipeline Parallelism

> Pipeline Parallelism 沿模型深度把 layers 分成多个 stage。它降低单 stage 的 weight/activation responsibility，但引入 stage boundary P2P、microbatch schedule 和 pipeline bubble。

## Stage Partition

设 PP degree 为 `P`：

```text
layers
→ stage_0 ... stage_(P-1)
```

每个 stage 需要记录：

- resident weights
- compute time
- activation input/output
- workspace
- device placement

“层数均匀”不等于“时间均匀”。

## Critical Stage

理想 steady state throughput 受最慢 stage 限制：

```text
pipeline_cycle_time
>= max(stage_time_i)
```

所以一个明显慢 stage 会让其他 stage 等待。

## Microbatch

为了让多个 stage 同时工作，需要把 batch 切成 microbatches。

如果 microbatch 太少：

- pipeline fill / drain 占比高
- utilization 低

microbatch 太多则可能增加：

- activation residency
- scheduling overhead
- queue/buffer

因此需要联合 memory 和 compute。

## Forward-only 简化 Bubble

在等 stage time、forward-only、`M` 个 microbatches、`P` 个 stages 的最简 pipeline 中，总 slot 约：

```text
M + P - 1
```

因此理想 stage utilization baseline：

```text
utilization
≈ M / (M + P - 1)
```

这只是教学 baseline，不代表训练 1F1B 或 interleaved schedule。

真实训练必须按具体 schedule 计算。

## P2P Boundary

stage i 与 i+1 之间需要传 activation：

```text
stage_i_output
→ stage_(i+1)_input
```

其时间用：

[[system/communication/point-to-point|Point-to-Point Communication]]

计算。

Payload 取决于：

- microbatch
- sequence
- hidden / tensor shape
- precision
- TP/CP interaction

## Activation Memory

Pipeline schedule 决定有多少 microbatch activation 同时存活。

因此 PP activation peak 不能只看单 microbatch。

见 [[system/memory/activation-memory|Activation Memory Model]]。

## Stage Imbalance

不平衡来源包括：

- 不同 layer compute
- embedding/output head
- MoE layer
- multimodal block
- communication boundary
- heterogeneous hardware

所以 partition 目标通常是平衡 critical path，而不是机械均分 layer count。

## PP × TP

常见多维结构：

```text
Pipeline stage
  └─ TP group inside stage
```

此时：

- PP 产生 stage P2P
- TP 产生 stage 内 collective

两类通信对 topology 的要求不同。

## Topology

PP 邻接 stage 的 P2P 通常希望：

- path 稳定
- bandwidth 足够
- latency 可预测

但它的同步粒度与 TP 不同，因此 placement 策略也不应相同。

## 输出

- `stage_partition`
- `stage_compute_time`
- `boundary_activation_bytes`
- `pipeline_bubble`
- `pp_p2p_pattern`

## 直接来源

本页定义通用 pipeline partition、bubble baseline 和 P2P 关系，没有引入特定框架 benchmark，因此 `evidence: {}`。
