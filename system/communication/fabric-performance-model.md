---
schema_version: system-v0.1
name: Fabric Performance Model
object_type: concept
category: communication-model
inputs:
  - communication.critical_path_bytes
  - topology.path_stages
  - hardware.nominal_bandwidth
  - hardware.explicit_effective_bandwidth
  - execution.protocol_efficiency
  - execution.utilization
  - execution.contention_efficiency
  - topology.fixed_latency
constraints:
  - nominal-vs-effective-bandwidth
  - directionality
  - protocol-overhead
  - utilization
  - contention
  - bottleneck-stage
  - hop-latency
outputs:
  - nominal_path_bottleneck
  - effective_path_bandwidth
  - nominal_serialization_lower_bound
  - effective_serialization_lower_bound
  - path_fixed_latency
  - p2p_transfer_lower_bound
  - bottleneck_stage
assumptions:
  - 每个 path stage 的 bandwidth 必须使用本次传输方向对应的速率口径
  - effective bandwidth 只有在显式给出或所有效率因子都已知时才派生
  - 缺失效率、时延或方向信息保持 unknown，不用经验默认值填充
related_layers:
  - communication
  - topology
  - accelerator
  - network
evidence: {}
updated: 2026-10-05
tags:
  - system
  - communication
  - fabric
  - performance
---
# Fabric Performance Model

> Fabric Performance Model 把硬件页面上的 nominal bandwidth 转换成一个可执行、可追溯的 path-level 性能下界。它解决的是“这条通信路径理论上和在给定假设下能多快”，而不是把厂商峰值直接当成 collective 实测性能。

## 为什么需要独立模型

现有 [[system/communication/communication-cost-model|Communication Cost Model]] 已经定义：

```text
T_comm
=
startup
+ serialization
+ transfer
+ synchronization
+ contention
```

但其中的 `B_effective` 如果没有统一语义，很容易退化成：

```text
message_bytes / vendor_peak_bandwidth
```

本页把 bandwidth path 明确拆成：

```text
nominal bandwidth
→ protocol efficiency
→ utilization
→ contention efficiency
→ stage effective bandwidth
→ path bottleneck
```

## Path Stage

一条通信路径由一个或多个 stage 组成，例如：

```text
accelerator injection
→ local scale-up fabric
→ NIC / fabric endpoint
→ switch path
→ remote endpoint
```

每个 stage 可以记录：

- `nominal_bandwidth_gbps`
- `effective_bandwidth_gbps`，如果有直接 benchmark / measurement
- `protocol_efficiency`
- `utilization`
- `contention_efficiency`
- `fixed_latency_ns`

### Nominal bandwidth

`nominal_bandwidth_gbps` 必须已经是**当前传输方向所需的带宽口径**。

如果来源只有：

- bidirectional aggregate
- TX + RX aggregate
- domain aggregate
- switch aggregate

则不能未经转换直接放进单向 P2P path stage。

## Effective bandwidth

若 stage 有直接测得的：

```text
effective_bandwidth_gbps
```

则优先使用该值。

否则只有当下列因子全部明确给出时才派生：

```text
B_stage_effective
=
B_nominal
× protocol_efficiency
× utilization
× contention_efficiency
```

其中每个效率因子范围为：

```text
0 < efficiency <= 1
```

没有某个因子时，不默认补 1.0，也不使用“常见 80% / 90%”经验值。

## Path bottleneck

对于可 pipeline 的 steady-state path：

```text
B_path_nominal
=
min(B_stage_nominal)
```

当所有 stage 的 effective bandwidth 都已知时：

```text
B_path_effective
=
min(B_stage_effective)
```

同时必须输出 bottleneck stage，而不是只输出一个最终数字。

## Serialization

设 critical path 上需要发送：

```text
D = critical_path_bytes
```

则 nominal serialization lower bound：

```text
T_serialization_nominal
=
8D / B_path_nominal
```

若 effective bandwidth 已知：

```text
T_serialization_effective
=
8D / B_path_effective
```

这里 bandwidth 使用 bit/s，因此 bytes 需要乘 8。

## Fixed path latency

如果每个 stage 都有明确的 `fixed_latency_ns`：

```text
T_path_fixed
=
Σ latency_stage
```

如果任何 stage latency 未知，则完整 path latency 保持 unknown。

不能把部分已知 hop latency 的和冒充端到端 latency。

## P2P lower bound

当 effective bandwidth 与完整 fixed latency 均已知：

```text
T_p2p_lower_bound
=
T_path_fixed
+
T_serialization_effective
```

这仍然只是 lower bound，不含：

- runtime dispatch
- synchronization
- queueing
- retry
- congestion beyond the explicit contention factor
- layout conversion
- memory subsystem contention

## Collective 不是 P2P × N

本模型先解决 path primitive。Collective 还需要：

- participant count
- collective algorithm
- algorithm steps
- bytes on critical path
- in-network reduction / multicast
- topology mapping
- synchronization
- straggler / retry

后续 [[system/communication/collective-communication|Collective Communication]] 的 executable extension 会消费本页输出。

## Nominal / Effective / Observed 三层

统一使用：

```text
Nominal
= hardware/interface upper bound

Effective
= 在明确协议/利用率/竞争假设下的 path throughput

Observed
= benchmark/application 实测值
```

禁止用 observed benchmark 回填硬件 nominal 字段；也禁止把 nominal 值写成 observed performance。

## Failure / degraded path

发生 link/switch failure 后：

- topology 可能改变；
- bottleneck stage 可能改变；
- hop count / latency 可能增加；
- effective bandwidth 可能下降。

因此 degraded topology 必须作为新的 path profile 计算，而不是在原始 bandwidth 上简单乘一个固定“故障系数”。

## 可执行实现

脚本：

```bash
python3 scripts/build-fabric-performance.py \
  --input examples/fabric/two-stage-reference.yaml \
  --output generated/executable/fabric-reference.json \
  --markdown-output system/derived/fabric-reference.md
```

该脚本只计算输入能支持的指标。未知值保持 `null`，并进入 `unknowns`。

## 与其他层的关系

- 总通信成本：[[system/communication/communication-cost-model|Communication Cost Model]]
- Collective：[[system/communication/collective-communication|Collective Communication]]
- Fabric graph：[[system/topology/accelerator-fabric|Accelerator Fabric]]
- Scale-up / Scale-out：[[system/topology/scale-up-vs-scale-out|Scale-up vs Scale-out]]
- Hardware facts：[[chip/interconnect/README|Interconnect / Fabric / Optical I/O]]

## 直接来源

本页定义仓库内部的可执行建模语义和量纲边界，没有引入具体厂商性能事实，因此 `evidence: {}`。
