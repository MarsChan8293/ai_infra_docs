---
schema_version: system-v0.1
name: Expert Routing / Load Balance
object_type: concept
category: moe
inputs:
  - model.expert_count
  - model.top_k
  - workload.tokens_per_step
  - routing.expert_assignments
  - parallelism.expert_placement
constraints:
  - expert-capacity
  - load-imbalance
  - all-to-all
  - locality
  - tail-latency
outputs:
  - expert_load_distribution
  - rank_load_distribution
  - imbalance_factor
  - remote_routing_ratio
  - overflow_tokens
assumptions:
  - 平均 expert load 不能替代真实 routing distribution
  - capacity factor 是 admission 约束，不等于观测负载
related_layers:
  - model
  - workload
  - compute
  - memory
  - parallelism
  - communication
  - topology
  - scheduling
evidence: {}
updated: 2026-09-25
tags: [system, moe, routing, load-balance]
---
# Expert Routing / Load Balance

> MoE 的平均负载可能很好看，但一步执行时间往往由最忙的 expert 或 rank 决定。Routing 模型要保留真实 token→expert 分布，而不是只保留平均值。

## Expert Load

对 expert i：

```text
load_i
= number of token assignments to expert_i
```

如果 top-k > 1，一个 token 会贡献多个 assignment。

平均：

```text
avg_load = total_assignments / expert_count
```

热点：

```text
max_load = max(load_i)
```

简单 imbalance 指标：

```text
imbalance_factor = max_load / avg_load
```

## Rank Load

多个 experts 可能放在同一 rank，因此真正设备负载：

```text
rank_load_r
= sum(load_i for experts on rank r)
```

Expert balance 好不代表 rank balance 好，placement 同样重要。

## Remote Routing

定义：

```text
remote_routing_ratio
= remote expert assignments / total assignments
```

它把 routing 与 [[system/parallelism/expert-parallelism|Expert Parallelism]]、[[system/communication/all-to-all|All-to-All]] 连接起来。

## Capacity / Overflow

若 expert capacity 为 C：

```text
overflow_i = max(0, load_i - C)
```

Overflow 之后可能 drop、reroute 或排队，不同策略会改变质量、compute 与通信，不能静默忽略。

## Tail Latency

MoE step 通常需要等待相关 rank 完成，因此：

```text
T_step
>= max_r(T_rank_r)
```

这使负载长尾直接进入 step latency。

## Locality-aware Placement

如果高概率互相相关的 token/expert traffic 可以留在局部 topology，可能降低 scale-out pressure。

但 placement 同时受 expert weight capacity 与 failure domain 约束。

## 输出

- `expert_load_distribution`
- `rank_load_distribution`
- `imbalance_factor`
- `remote_routing_ratio`
- `overflow_tokens`

## 直接来源

本页定义通用 MoE routing/load-balance 指标，不引入具体模型 routing 分布，因此 `evidence: {}`。
