---
schema_version: system-v0.1
name: Rack / Failure Domain
object_type: concept
category: topology
inputs:
  - topology.node
  - topology.rack
  - topology.switch
  - topology.rail
  - topology.power
  - topology.cooling
  - workload.replica
  - workload.parallel_group
constraints:
  - failure-domain
  - correlated-failure
  - placement
  - power-domain
  - network-domain
outputs:
  - failure_domain_hierarchy
  - correlated_failure_sets
  - placement_anti_affinity
  - recovery_scope
  - topology_risk
assumptions:
  - 性能最优 placement 与可靠性最优 placement 可能冲突
  - failure domain 必须来自真实基础设施边界，不按设备数量猜测
related_layers:
  - workload
  - parallelism
  - communication
  - topology
  - scheduling
  - network
  - power
  - reliability
  - accelerator
evidence: {}
updated: 2026-09-25
tags:
  - system
  - topology
  - rack
  - failure-domain
---
# Rack / Failure Domain

> Topology 不只有带宽和时延，还包含“哪些资源会一起坏”。Rack / Failure Domain 把 device、node、switch、rail、power、cooling 等相关故障边界纳入 placement。

## Failure Domain Hierarchy

概念上可以分层：

```text
device
→ node
→ local switch / fabric domain
→ rack
→ rail / network plane
→ power / cooling domain
→ larger cluster zone
```

实际设施边界必须由真实部署事实定义。

## Correlated Failure

多个 device 共享：

- PCIe switch
- NIC
- top-of-rack switch
- power feed
- cooling loop

时，它们的 failure 并非独立。

所以可靠性模型不能把：

```text
N devices
```

当作 N 个完全独立 failure units。

## Parallel Group

TP/EP/CP 等 tight-coupled group 可能为了性能集中在一个局部 domain。

优点：

- lower latency
- higher bandwidth

代价：

- shared failure exposure

因此 placement 需要同时记录：

```text
performance affinity
reliability anti-affinity
```

## Replica

Serving replica 或训练冗余副本如果全部放在同一 rack/power domain，逻辑 replica 数量并不等于独立可用性。

需要记录：

```text
replica
→ failure domain
```

并检查是否真正分散。

## Network Rail

多 rail 可以提供：

- bandwidth
- path diversity
- failure isolation

但前提是 workload/rank 确实跨不同 rail placement。

如果所有关键 rank 仍绑定同一 rail，理论上的多 rail 不等于容错。

## Power / Cooling

高密度 accelerator rack 的 power/cooling 也是共享 domain。

本页不记录具体 kW 或冷却产品，只要求系统模型能表达：

- shared power dependency
- shared cooling dependency
- rack-level correlated outage

后续任务 `PWR-001` 建立 Power / Cooling 专题后可进一步细化；当前不提前创建不存在的 Wiki Link。

## Recovery Scope

故障发生后需要知道重启粒度：

- one process
- one accelerator
- one node
- one parallel group
- entire job / replica

恢复范围与 parallel state、checkpoint 和 distributed runtime 共同决定。

## Checkpoint

训练 checkpoint 的价值取决于 failure domain 与 lost work。

后续 `REL-001` 会把：

```text
failure rate
× checkpoint interval
× recovery time
```

连接起来。

## Scheduling

[[system/scheduling/topology-aware-scheduling|拓扑感知调度]] 不应只优化 shortest path。

还需要考虑：

- anti-affinity
- rack spread
- rail spread
- maintenance domain
- degraded topology

## Output

- `failure_domain_hierarchy`
- `correlated_failure_sets`
- `placement_anti_affinity`
- `recovery_scope`
- `topology_risk`

## 直接来源

本页定义通用 failure-domain 与 placement 语义，不引入具体数据中心设施参数，因此 `evidence: {}`。
