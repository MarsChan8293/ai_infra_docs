---
schema_version: system-v0.1
name: Expert Parallelism
object_type: concept
category: parallelism
inputs:
  - model.expert_count
  - model.active_experts
  - model.shared_experts
  - workload.tokens_per_step
  - parallelism.ep_degree
  - routing.destination_distribution
constraints:
  - all-to-all
  - expert-memory
  - load-imbalance
  - topology
  - capacity-factor
outputs:
  - expert_placement
  - token_dispatch_bytes
  - token_combine_bytes
  - expert_load_distribution
  - ep_scaling_limits
assumptions:
  - active expert count 与 resident expert count 分开
  - 平均 token load 不能替代 hottest-rank load
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
  - expert-parallel
  - moe
---
# Expert Parallelism

> Expert Parallelism 把不同 MoE experts 放到不同 rank。它能扩展 expert weight capacity，但把 routing 结果转换成 All-to-All、热点和 placement 问题。

## Expert Placement

设：

- total experts = `E`
- EP degree = `P`

均匀 baseline 可写成：

```text
experts_per_rank
≈ E / P
```

但 shared experts、replication、冗余 placement 或异构设备都会破坏简单除法。

## Active vs Resident

每 token 激活 `k` 个 routed experts：

```text
active_experts_per_token = k
```

不代表每 rank 只需驻留 k 个 experts。

必须区分：

```text
active expert weights
resident expert weights
total model expert weights
```

这直接连接 [[system/memory/weight-memory|Weight Memory Model]]。

## Token Dispatch

每个 token 根据 router 输出被发送到 expert 所在 rank。

若 token representation payload 为 `H_bytes`，远端 fan-out 为 `k_remote`：

```text
dispatch_payload_per_token
≈ H_bytes × k_remote
```

这是 payload baseline。

实际还可能有：

- routing metadata
- alignment/padding
- duplicate expert assignment
- batching
- combine return payload

## All-to-All

EP 通信核心见：

[[system/communication/all-to-all|All-to-All]]

必须记录 destination matrix，而不是只记录平均 bytes/rank。

因为 routing skew 会导致：

```text
max_recv_bytes
>> average_recv_bytes
```

critical path 常由热点 expert/rank 决定。

## Capacity / Dropping

某些系统会给 expert 设置 token capacity。

系统分析应区分：

- offered tokens
- admitted tokens
- overflow / reroute / drop

不能用配置 capacity 反推真实 token distribution。

## Shared Experts

Shared experts 通常每 token 都参与，因此：

- compute pattern 不同于 routed experts
- weight residency 可能复制
- 不一定进入同样的 All-to-All

需要单独记账。

## Locality

如果 source token 与 destination expert 同 rank 或同 scale-up domain，可以减少 scale-out traffic。

所以 expert placement 需要联合：

- routing statistics
- scale-up size
- memory capacity
- failure domain

而不是只按 expert ID 均匀铺开。

## Load Imbalance

可以定义：

```text
expert_load_i
= tokens assigned to expert_i

rank_load_r
= Σ expert_load_i on rank_r
```

简单 imbalance indicator：

```text
max_rank_load / average_rank_load
```

但 time imbalance 还取决于 expert shape 和 hardware。

## EP × TP

一个 expert 自身仍可能太大，需要 TP：

```text
EP group
  └─ TP subgroup per expert / expert set
```

这会同时产生：

- inter-expert All-to-All
- intra-expert collective

拓扑映射必须分层。

## 输出

- `expert_placement`
- `token_dispatch_bytes`
- `token_combine_bytes`
- `expert_load_distribution`
- `ep_scaling_limits`

## 直接来源

本页定义通用 Expert Parallel 数据流和约束，没有引入具体 MoE 模型或框架 benchmark，因此 `evidence: {}`。
