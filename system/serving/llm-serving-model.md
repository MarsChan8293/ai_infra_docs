---
schema_version: system-v0.1
name: LLM Serving Model
object_type: concept
category: serving
inputs:
  - workload.inference
  - model.architecture
  - compute.prefill
  - compute.decode
  - memory.kv
  - memory.weights
  - topology
constraints:
  - ttft
  - tpot
  - throughput
  - memory-capacity
  - queueing
  - communication
outputs:
  - serving_pipeline
  - replica_capacity
  - queue_budget
  - resource_role_mapping
  - serving_bottleneck_candidates
assumptions:
  - Serving 性能属于 Model × Workload × Runtime × Hardware × Topology 联合结果
  - 在线服务必须同时建模 latency 与 throughput
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
  - reliability
evidence: {}
updated: 2026-09-25
tags:
  - system
  - serving
  - inference
---
# LLM Serving Model

> LLM Serving Model 把请求生命周期、排队、Prefill、Decode、KV、batch 和资源角色串成一个服务系统，而不是用单个 tokens/s 概括一切。

## 请求生命周期

典型逻辑链：

```text
arrival
→ admission / queue
→ prefix lookup
→ prefill
→ decode scheduling loop
→ output / finish
```

每一段都可能贡献 latency。

## 两条主预算

在线服务至少同时有：

```text
latency budget
throughput / capacity budget
```

只优化 throughput 可能恶化 TTFT/TPOT；只压低 latency 可能牺牲 batch 和设备利用率。

## Queueing

请求到达率记为 `lambda`，系统服务能力记为 `mu`。

当长期：

```text
lambda >= mu
```

queue 会持续增长。

所以 capacity planning 不能只看“单请求最快速度”，还要看稳态 arrival envelope 和服务率。

## Prefill / Decode

阶段差异见：

[[system/compute/prefill-vs-decode|Prefill vs Decode]]

Serving 层需要决定：

- 是否同一资源池执行
- 是否采用不同 batch policy
- 是否允许角色分离
- KV 如何跨阶段保留/迁移

## KV 生命周期

KV 从 Prefill 产生，并在 Decode 中持续增长和访问。

需要联合：

- [[system/memory/kv-cache-model|KV Cache Model]]
- [[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层级]]

做 capacity 与 placement。

## Replica Capacity

一个 replica 的 capacity 受：

- weight resident bytes
- KV capacity
- activation/workspace
- compute throughput
- memory bandwidth
- scheduler batch
- SLA

共同约束。

所以：

```text
max_concurrency
```

不是由 HBM capacity 单独决定。

## Batching

Batch 是服务策略变量。

更大 batch 可能：

- 提升 weight reuse
- 提升 GEMM efficiency
- 增加等待
- 增加 KV/activation pressure
- 放大 tail latency

因此 batch policy 应由 workload/SLA 决定。

## Prefix Reuse

Prefix cache 命中可以减少 Prefill work，但会增加：

- cache capacity
- lookup/placement
- lifecycle
- tenant isolation

收益最终要比较：

```text
saved_prefill_cost
vs
cache_storage + retrieve + management cost
```

## Resource Role

Serving 可以把硬件角色描述为：

- prefill-capable pool
- decode-capable pool
- shared pool
- KV / memory tier
- transfer/network resource

“适合 Prefill/Decode”是派生属性，不是芯片固有标签。

## Reliability

在线服务还需要：

- replica redundancy
- failed request retry
- KV loss semantics
- degraded capacity
- failure-domain spread

因此 serving capacity 还要留 reliability headroom。

## 输出

- `serving_pipeline`
- `replica_capacity`
- `queue_budget`
- `resource_role_mapping`
- `serving_bottleneck_candidates`

## 直接来源

本页定义通用 LLM serving 系统边界，不引入具体 runtime 行为或 benchmark，因此 `evidence: {}`。
