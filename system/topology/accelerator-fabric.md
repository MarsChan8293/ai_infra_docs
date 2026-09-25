---
schema_version: system-v0.1
name: Accelerator Fabric
object_type: concept
category: topology
inputs:
  - topology.accelerator_count
  - topology.link_graph
  - topology.switch_graph
  - hardware.link_bandwidth
  - hardware.device_injection_bandwidth
  - workload.communication_pattern
constraints:
  - link-bandwidth
  - latency
  - radix
  - hop-count
  - bisection-bandwidth
  - non-uniformity
outputs:
  - accelerator_domain
  - fabric_path
  - aggregate_injection_limit
  - bisection_limit
  - collective_topology_constraints
assumptions:
  - 单 link bandwidth、device aggregate bandwidth 与 fabric bisection 分开记录
  - 厂商协议名不等于固定 topology 形态
related_layers:
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
  - topology
  - accelerator-fabric
---
# Accelerator Fabric

> Accelerator Fabric 描述 accelerator 之间的高带宽互联图。系统层关心的是 graph、path、injection、bisection 和 collective mapping，而不是只记录一个“互联带宽”数字。

## Graph

把 accelerator fabric 表示成：

```text
G = (devices, links, switches)
```

每条 link 至少应有：

- direction
- bandwidth
- latency if known
- endpoint
- failure state

switch 节点还需要：

- port/radix
- forwarding path
- uplink/downlink structure

## 三种 Bandwidth

必须区分：

### Link bandwidth

单条 link 的能力。

### Device aggregate / injection bandwidth

一个 accelerator 同时通过多条 link 注入 fabric 的上限。

### Fabric bisection bandwidth

整个 domain 跨某 cut 的可用吞吐。

三者不是同一个指标。

## Path

两个 accelerator 的 path 可能：

- direct link
- one switch hop
- multi-switch hop
- non-uniform path

因此：

```text
peer bandwidth
```

不能只由设备的 aggregate link 总和推出。

## Collective Mapping

Collective algorithm 会把 rank 顺序映射到 fabric graph。

一个 ring 如果穿过弱 link：

```text
collective effective bandwidth
<= bottleneck path
```

所以 topology-aware collective 与调度是同一问题的两面。

通信模型见：

[[system/communication/collective-communication|Collective Communication]]

## Scale-up Domain

Accelerator Fabric 常构成 [[system/topology/scale-up-vs-scale-out|Scale-up]] 的核心，但本页不把“scale-up”绑定到任何厂商协议。

一个 scale-up domain 至少应记录：

- member accelerators
- internal path
- switch hierarchy
- domain boundary

## Non-uniform Topology

并非所有 device pair 都有相同 path。

因此调度器应避免假设：

```text
all accelerators are equivalent
```

需要记录 rank-to-device mapping。

## TP / CP / EP

不同并行模式对 fabric 压力不同：

- TP：高频 collective、latency 敏感
- CP：多轮 context exchange
- EP：destination-driven All-to-All
- PP：邻接 P2P

所以同一 fabric 对不同 workload 的 suitability 需要由 pattern 决定。

## Failure Domain

Fabric switch/link 本身也是 failure domain。

一个 switch failure 可能影响一组 accelerator 的互联，即使 accelerator 本身健康。

所以资源模型应分别记录：

- device health
- link health
- switch/fabric health

## 输出

- `accelerator_domain`
- `fabric_path`
- `aggregate_injection_limit`
- `bisection_limit`
- `collective_topology_constraints`

## 直接来源

本页定义通用 accelerator-fabric graph 与系统指标，不引入具体厂商协议数值，因此 `evidence: {}`。
