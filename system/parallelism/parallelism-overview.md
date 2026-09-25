---
schema_version: system-v0.1
name: Parallelism Overview
object_type: concept
category: parallelism
inputs:
  - model.architecture
  - model.parameters
  - workload.batch_size
  - workload.sequence_length
  - workload.concurrency
  - hardware.accelerator_count
  - hardware.memory.capacity
  - topology
constraints:
  - device-memory
  - compute-throughput
  - communication
  - synchronization
  - pipeline-bubble
  - load-imbalance
outputs:
  - parallelism_dimensions
  - per_device_partition
  - communication_pattern
  - placement_requirements
  - scaling_limits
assumptions:
  - 并行策略首先是 work/state partition，不等同于线性加速
  - 全局数学 work、per-device work 与通信开销分别建模
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
---
# Parallelism Overview

> 并行不是“卡越多越快”的同义词。它首先定义 **模型、token、batch、layer、expert 或 sequence 如何切分到多个 rank**，随后才产生 per-device compute、memory、communication、bubble 和 placement 成本。

## 为什么需要统一 Parallelism Model

同一个模型可以同时使用：

```text
DP × TP × PP × EP × CP
```

这些维度解决的是不同问题，不能只记录一个“GPU count”。

系统分析至少要回答：

1. 什么被切分；
2. 什么仍然复制；
3. 每个设备保留什么状态；
4. 产生什么通信；
5. 要求什么 topology；
6. 扩展到更多设备时新瓶颈是什么。

## 五个主要维度

| 维度 | 主要切分对象 | 常见复制对象 | 典型通信 | 主要目标 |
|---|---|---|---|---|
| DP | batch / samples / requests | 模型或模型 shard | gradient aggregation / 独立推理 | 扩吞吐 |
| TP | 单层 tensor / weight / activation | 部分 layer state | collective | 让单层跨设备 |
| PP | layers / stages | stage 内局部状态 | P2P activation | 让模型深度跨设备 |
| EP | experts | shared layers / router 等 | All-to-All | 分布 MoE experts |
| CP | sequence / context | 部分模型权重 | attention/KV 相关交换 | 分布长上下文状态与计算 |

表中只是稳定语义，不代表具体框架实现。

## Data Parallel

Data Parallel 主要把不同样本或请求分到不同 replica / rank。

训练时，若每个 replica 都产生 parameter gradients，则通常需要某种 gradient aggregation。

推理时，多个 replica 可以独立服务不同请求，不一定需要每 token 同步。

因此：

```text
training DP communication
≠ inference replica scaling
```

后续 `PAR-005` 单独展开。

## Tensor Parallel

Tensor Parallel 在单层内部切分权重、activation 或算子 work。

它的优势通常是：

- 降低单设备权重/activation 压力；
- 并行执行单层大矩阵运算。

代价是 layer 内更频繁的 collective，通常更敏感于：

- latency；
- scale-up bandwidth；
- rank locality；
- collective algorithm。

所以 TP placement 不能只看“有 N 张空卡”。

后续 `PAR-002` 展开。

## Pipeline Parallel

Pipeline Parallel 把 layer 序列切成多个 stage。

主要交换：

```text
stage i output
→ stage i+1 input
```

它减少每 stage 驻留的 layer 数，但引入：

- stage imbalance；
- pipeline fill/drain；
- microbatch scheduling；
- bubble；
- P2P dependency。

单纯把模型均分成 N 段不保证每段时间相等。

后续 `PAR-003` 展开。

## Expert Parallel

MoE 中可把不同 experts 放到不同 rank。

这会把“expert weight capacity”从单设备扩展到多设备，但 token 必须根据 routing 结果发送到对应 expert。

因此核心代价往往包含：

```text
token dispatch
→ expert compute
→ token combine
```

以及由此产生的 All-to-All 和 load imbalance。

后续 `PAR-004` 展开。

## Context Parallel

Context Parallel 把长 sequence / context 维度切分到多个 rank。

它可以降低某些 sequence-dependent 状态和计算的 per-device 压力，但 attention dependency 意味着 rank 之间仍需交换必要信息。

所以 CP 不是“sequence 除以设备数后完全独立”。

后续 `PAR-006` 展开。

## Parallelism 改变什么

### Per-device Memory

并行可以切分：

- weights；
- KV；
- activations；
- optimizer / gradients；
- expert weights。

但也可能复制：

- embeddings；
- norms；
- shared experts；
- metadata；
- communication buffers。

因此 per-device memory 必须通过 [[system/memory/model-memory-accounting|Model Memory Accounting]] 按实际 partition 重新计算。

### Per-device Compute

理想情况下某些 work 可以分摊，但：

```text
per-device mathematical work
≠ global work / device_count
```

除非切分完全均衡且没有重复 work。

MoE expert imbalance、pipeline stage imbalance、padding、replicated computation 都可能破坏简单除法。

### Communication

并行策略会生成通信依赖：

- TP → collectives；
- PP → P2P；
- EP → All-to-All；
- training DP → gradient aggregation；
- CP → attention/context exchange。

统一通信语义见 [[system/communication/collective-communication|Collective Communication]]。

## 并行度不是性能结论

记某个维度的 degree 为 `N`：

```text
parallel_degree = N
```

并不推出：

```text
speedup = N
```

端到端时间至少还受：

```text
compute
+ communication
+ synchronization
+ imbalance
+ bubble
+ memory traffic
```

影响。

Scaling efficiency 必须在明确 workload、hardware 和 topology 后评估。

## 多维并行

实际系统可能使用：

```text
world_size
= DP × TP × PP × EP × CP
```

但这个乘积公式只有在这些维度形成清晰的正交 rank group 时才成立。某些系统会复用 rank、采用不规则 expert placement 或动态角色分工，因此必须以真实 process/rank topology 为准。

## Placement

并行 group 应映射到合适的物理 topology。

通常需要比较：

```text
communication frequency
× message size
× synchronization sensitivity
```

与：

```text
available topology bandwidth / latency / failure domain
```

例如高频、细粒度同步的 group 更依赖局部高带宽低时延路径；低频、大消息同步可能有不同权衡。

具体 topology 分类见 [[system/topology/scale-up-vs-scale-out|Scale-up vs Scale-out]]。

## 调度

调度器真正需要消费的不只是：

```text
accelerator_count = N
```

而是：

- parallel group structure；
- memory requirement per rank；
- topology affinity；
- NIC/fabric requirement；
- failure-domain policy；
- role，例如 Prefill / Decode / expert / pipeline stage。

这与 [[system/resource/accelerator-resource-model|加速器资源模型]] 和 [[system/scheduling/topology-aware-scheduling|拓扑感知调度]] 相连。

## 输出

Parallelism Model 输出：

- `parallelism_dimensions`
- `per_device_partition`
- `communication_pattern`
- `placement_requirements`
- `scaling_limits`

每个输出必须绑定：

```text
model
+ workload
+ degrees
+ rank groups
+ placement assumptions
```

## 与其他层的关系

- Workload：[[system/workload/ai-workload-model|AI Workload Model]]
- Compute：[[system/compute/transformer-compute-model|Transformer Compute Model]]
- Memory：[[system/memory/model-memory-accounting|Model Memory Accounting]]
- Communication：[[system/communication/collective-communication|Collective Communication]]
- Topology：[[system/topology/README|Topology Model]]
- Scheduling：[[system/scheduling/topology-aware-scheduling|拓扑感知调度]]
- Hardware：[[chip/00-project-index|AI 芯片与基础设施资料库]]
- Schema：[[system/SCHEMA|System Schema V0.1]]

## 直接来源

本页定义仓库内部的并行维度和系统分析边界，没有引入特定框架版本、厂商规格或 benchmark 数值，因此 `evidence: {}`。
