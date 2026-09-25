---
schema_version: system-v0.1
name: All-to-All
object_type: concept
category: communication-model
inputs:
  - communication.outbound_bytes_per_rank
  - communication.participant_count
  - communication.destination_distribution
  - topology.effective_bandwidth
  - topology.bisection_bandwidth
constraints:
  - injection-bandwidth
  - bisection-bandwidth
  - incast
  - imbalance
  - synchronization
outputs:
  - per_rank_send_bytes
  - per_rank_receive_bytes
  - destination_matrix
  - all_to_all_time_lower_bound
  - imbalance_factor
assumptions:
  - 均匀 All-to-All baseline 与真实 token routing 必须分开
  - 总发送字节相同不代表相同网络压力，destination distribution 同样重要
related_layers:
  - workload
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
  - all-to-all
---
# All-to-All

> All-to-All 的困难不只是“每个 rank 发多少数据”，而是数据被发往哪里。MoE token routing 会让通信矩阵、热点和 bisection pressure 直接进入性能模型。

## 通信矩阵

设 `D_ij` 为 rank i 发给 rank j 的 bytes。

则：

```text
send_bytes_i = Σ_j D_ij
recv_bytes_j = Σ_i D_ij
```

完整 All-to-All workload 应尽量保留：

```text
destination_matrix = [D_ij]
```

而不是只保留全局总 bytes。

## 均匀 Baseline

如果 rank i 的总 outbound payload 为 `D`，并均匀分给 `N` 个目的 rank：

```text
D_ij ≈ D / N
```

则：

```text
send_bytes_per_rank ≈ D
recv_bytes_per_rank ≈ D
```

这个 baseline 适合量纲分析，但 MoE routing 常常不均匀。

## MoE Token Dispatch

对于 Expert Parallel：

```text
token hidden state
→ routed expert rank
→ expert compute
→ return / combine
```

如果一个 token 被 top-k 路由到多个 experts，dispatch payload 会随实际 fan-out 增长。

需要区分：

- input token count
- hidden bytes/token
- top-k
- local expert hit
- remote expert hit
- duplicate routing
- combine return bytes

不能只用 total model parameters 推通信量。

## Imbalance

如果某些 expert/rank 收到更多 token：

```text
max_recv_bytes
>> average_recv_bytes
```

critical path 往往由最忙 rank 决定，而不是平均值。

可以定义简单 imbalance factor：

```text
imbalance_factor
= max_recv_bytes / average_recv_bytes
```

该指标不等同于时间放大倍数，但能暴露 load skew。

## Bisection

All-to-All 容易让大量 traffic 跨越 topology cut。

因此需要同时检查：

- endpoint injection bandwidth
- local scale-up bandwidth
- NIC bandwidth
- fabric bisection bandwidth
- oversubscription

单链路峰值不能代表整个 All-to-All 的可扩展性。

## Incast / Hotspot

多个 sender 同时发向一个 receiver 或一组 uplink 时，会形成：

- incast
- queue buildup
- tail latency
- backpressure

所以相同 total bytes、不同 `D_ij`，性能可能完全不同。

## Locality

如果 routed expert 与 token source 在同一 scale-up domain：

```text
local dispatch
```

可能避免 scale-out path。

因此 Expert placement 与 routing policy 要联合分析。

见：

- [[system/topology/scale-up-vs-scale-out|Scale-up vs Scale-out]]
- [[system/scheduling/topology-aware-scheduling|拓扑感知调度]]

## 时间下界

最简单 lower bound 至少受：

```text
max(
  max_rank_send / injection_BW,
  max_rank_recv / receive_BW,
  cut_crossing_bytes / bisection_BW
)
```

再加 startup、同步、contention 和 algorithm overhead。

统一时间模型见 [[system/communication/communication-cost-model|Communication Cost Model]]。

## 输出

- `per_rank_send_bytes`
- `per_rank_receive_bytes`
- `destination_matrix`
- `all_to_all_time_lower_bound`
- `imbalance_factor`

## 直接来源

本页定义通用 All-to-All 数据守恒、routing matrix 与 topology cost，没有引入特定框架或网络 benchmark，因此 `evidence: {}`。
