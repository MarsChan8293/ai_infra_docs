---
schema_version: system-v0.1
name: Collective Performance Model
object_type: concept
category: communication-model
inputs:
  - communication.collective_type
  - communication.algorithm
  - communication.participant_count
  - communication.payload_bytes_per_rank
  - communication.algorithm_steps
  - communication.critical_path_bytes
  - topology.fabric_effective_bandwidth
  - topology.collective_effective_bandwidth
  - topology.step_latency
constraints:
  - algorithm-steps
  - critical-path-bytes
  - effective-bandwidth
  - bisection-bandwidth
  - synchronization
  - topology-mapping
outputs:
  - algorithm_steps
  - critical_path_bytes
  - algorithmic_traffic_factor
  - effective_bandwidth
  - serialization_lower_bound
  - step_latency_lower_bound
  - collective_time_lower_bound
  - payload_goodput
assumptions:
  - 不定义跨算法通用的固定 collective efficiency 百分比
  - Ring 的 steps 与 critical-path bytes 只在语义明确的 collective 上自动派生
  - Tree 的具体数据量依实现而异，必须由 algorithm profile 显式给出
  - All-to-All 的并发路径与 bisection 不能由单条 P2P path bandwidth 自动推断
related_layers:
  - communication
  - topology
  - parallelism
  - accelerator
  - network
evidence: {}
updated: 2026-10-05
tags:
  - system
  - communication
  - collective
  - performance
---
# Collective Performance Model

> Collective Performance Model 把 [[system/communication/fabric-performance-model|Fabric Performance Model]] 的 path primitive 向上组合成 collective lower bound。它不使用“NVLink 效率 85%”之类全局经验常数，而是保留算法、数据量、拓扑和带宽来源。

## 为什么不定义一个通用 Collective Efficiency

“collective efficiency”经常把几种完全不同的东西混在一起：

- protocol / link utilization；
- algorithmic traffic amplification；
- startup / step latency；
- topology mapping；
- bisection / oversubscription；
- implementation quality；
- application observed goodput。

因此本库不维护：

```text
collective_efficiency = 0.85
```

这种脱离上下文的常数。

可比较的最小分解是：

```text
collective
→ participant count
→ algorithm
→ sequential steps
→ critical-path bytes
→ effective bandwidth source
→ step latency source
→ lower-bound time
```

## Payload 语义

统一字段：

```text
payload_bytes_per_rank
```

但不同 collective 的语义不同。

### All-Reduce

每个 rank 在入口处持有完整 payload：

```text
M = payload_bytes_per_rank
```

### Reduce-Scatter

每个 rank 在入口处持有完整 payload，最终只保留一个 shard。

### All-Gather

每个 rank 在入口处持有自己的 local shard：

```text
S = payload_bytes_per_rank
```

最终逻辑结果大小为：

```text
N × S
```

### All-to-All

每个 rank 的 `payload_bytes_per_rank` 表示该 rank 准备分发给所有目的 rank 的总 outbound payload。

如果启用 uniform partition baseline，self-destination 不经过网络，则网络发送量可写成：

```text
M × (N - 1) / N
```

真实 MoE routing 应优先使用 destination matrix，而不是均匀 baseline。

## Ring

对于 N 个参与者。

### Ring Reduce-Scatter

```text
steps = N - 1

critical_path_bytes
= M × (N - 1) / N
```

### Ring All-Gather

若每 rank 初始 shard 为 S：

```text
steps = N - 1

critical_path_bytes
= S × (N - 1)
```

### Ring All-Reduce

把 Reduce-Scatter + All-Gather 组合：

```text
steps
= 2 × (N - 1)

critical_path_bytes
= 2 × M × (N - 1) / N
```

这里的 critical-path bytes 是模型中的 per-rank serialized traffic baseline，不等于全 fabric wire bytes。

## Tree

“Tree All-Reduce”不是一个足够精确的算法定义。

实际可能是：

- binary tree；
- k-ary tree；
- recursive doubling；
- reduce + broadcast；
- pipelined tree；
- hierarchical tree；
- switch-assisted reduction。

因此模型不会仅凭：

```text
algorithm: tree
```

就猜测数据量。

Tree profile 必须显式提供：

```text
algorithm_steps
critical_path_bytes
```

生成结果会保留：

```text
steps_source = explicit
critical_path_bytes_source = explicit
```

这样算法假设可审计。

## All-to-All

All-to-All 的主要约束往往不是单条 path，而是：

- endpoint injection；
- destination matrix；
- bisection；
- oversubscription；
- incast；
- receive hotspot。

因此脚本不会把 FAB-002 的单 path effective bandwidth 自动用于 All-to-All timing。

若要计算 All-to-All lower bound，profile 必须显式给：

```text
collective_effective_bandwidth_gbps
```

这个值可以来自：

- topology-aware bisection model；
- benchmark；
- validated simulator；
- 显式系统假设。

其来源应在调用方/profile 中说明。

## Step Latency

对于 Ring / explicit Tree：

若 profile 自己给出：

```text
step_latency_ns
```

则优先使用。

否则可以消费 FAB-002 输出的完整：

```text
path_fixed_latency_ns
```

作为每个 sequential step 的 fixed-path baseline。

于是：

```text
T_steps
=
algorithm_steps × step_latency
```

这仍是 lower-bound approximation，不包含 runtime launch、barrier、straggler 和 retry。

## Serialization

当 critical-path bytes 和 effective bandwidth 都已知：

```text
T_serialization
=
8 × critical_path_bytes
/ effective_bandwidth
```

Collective lower bound：

```text
T_collective_lower_bound
=
T_serialization
+ T_steps
```

仅在两部分都可计算时输出完整 lower bound。

## Algorithmic Traffic Factor

为暴露算法本身的数据移动：

```text
algorithmic_traffic_factor
=
critical_path_bytes
/ payload_bytes_per_rank
```

它不是“效率”。

例如 Ring All-Reduce 随 N 增大趋近：

```text
2
```

表示 critical path 上接近 2× per-rank payload 的序列化数据，而不是“效率 200%”。

## Payload Goodput

若 lower-bound time 已知，可以给出一个语义明确的：

```text
payload_goodput_gbps
=
8 × payload_bytes_per_rank
/ T_collective_lower_bound
```

它只表示 per-rank 输入 payload 除以模型时间。

不同 collective 的 payload 语义不同，因此不能直接把该值当成统一的 network bandwidth benchmark。

## Source Traceability

每个关键派生值都带来源：

- `steps_source`
- `critical_path_bytes_source`
- `effective_bandwidth_source`
- `step_latency_source`

典型值：

```text
derived-ring
explicit
fabric-profile-effective-path
explicit-collective
fabric-profile-fixed-path
unavailable
```

## 可执行实现

Ring All-Reduce：

```bash
python3 scripts/build-collective-performance.py \
  --input examples/collectives/ring-allreduce-reference.yaml \
  --fabric-profile generated/executable/fabric-reference.json \
  --output generated/executable/collective-ring-allreduce-reference.json \
  --markdown-output system/derived/collective-ring-allreduce-reference.md
```

## 与现有模型关系

- 通用语义：[[system/communication/collective-communication|Collective Communication]]
- Ring / Tree 语义：[[system/communication/all-reduce-all-gather-reduce-scatter|All-Reduce / All-Gather / Reduce-Scatter]]
- All-to-All：[[system/communication/all-to-all|All-to-All]]
- Path effective bandwidth：[[system/communication/fabric-performance-model|Fabric Performance Model]]
- 总通信成本：[[system/communication/communication-cost-model|Communication Cost Model]]

## 直接来源

本页定义仓库内部算法与系统建模语义，没有引入具体厂商 benchmark 数值，因此 `evidence: {}`。
