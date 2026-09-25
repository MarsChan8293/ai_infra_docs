---
schema_version: system-v0.1
name: MoE System Model
object_type: concept
category: moe
inputs:
  - model.parameters.total
  - model.parameters.active
  - model.expert_count
  - model.top_k
  - workload.tokens_per_step
  - parallelism.ep_degree
  - topology
constraints:
  - expert-memory
  - routing
  - all-to-all
  - load-imbalance
  - capacity
outputs:
  - active_compute
  - resident_expert_memory
  - routing_matrix
  - dispatch_bytes
  - moe_bottleneck_candidates
assumptions:
  - total parameters、active parameters 与 resident parameters 分开
  - routing distribution 不能用均匀分布静默替代
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
  - moe
---
# MoE System Model

> MoE 把“模型很大”和“每 token 只激活一部分参数”同时成立。系统层必须同时处理 active compute、resident expert weights、routing 和 All-to-All。

## 三个 Parameter 概念

必须区分：

```text
total parameters
active parameters per token
resident parameters per rank
```

三者解决不同问题。

- total：模型整体规模
- active：每 token 计算规模
- resident：每设备容量压力

## Routing

每个 token 先产生 expert destination。

抽象为：

```text
token
→ router
→ top-k experts
```

routing 输出决定：

- active compute
- dispatch destination
- rank load
- locality

## Expert Placement

Expert placement 由：

[[system/parallelism/expert-parallelism|Expert Parallelism]]

建模。

需要联合：

- expert weight size
- EP degree
- scale-up domain
- memory capacity
- routing locality

## Communication

远端 expert 需要 token dispatch / combine。

核心原语：

[[system/communication/all-to-all|All-to-All]]

通信量取决于 hidden payload、top-k、local/remote expert hit 和 token distribution。

## Load Imbalance

平均 expert load 不能代表 critical path。

需要至少观察：

```text
max rank tokens
average rank tokens
```

以及 hottest expert。

## Capacity Factor

如果系统对 expert token 容量设限，需要分开：

- offered load
- accepted load
- overflow policy

不能把配置 capacity 当成实际 routing distribution。

## Shared Expert

Shared expert 与 routed expert 分开记账：

- compute
- residency
- communication

shared expert 可能每 token 都执行，却不一定产生同样的 All-to-All。

## Compute

MoE linear work 应基于 active experts，而不是 total expert weights。

见 [[system/compute/transformer-compute-model|Transformer Compute Model]]。

## Memory

Weight capacity 使用 resident experts，而非 active parameter count。

见 [[system/memory/weight-memory|Weight Memory Model]]。

## 输出

- `active_compute`
- `resident_expert_memory`
- `routing_matrix`
- `dispatch_bytes`
- `moe_bottleneck_candidates`

## 直接来源

本页定义通用 MoE 系统分解，不引入具体模型配置，因此 `evidence: {}`。
