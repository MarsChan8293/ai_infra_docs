---
schema_version: system-v0.1
name: GPU/NPU ↔ NIC Affinity
object_type: concept
category: topology
inputs:
  - topology.accelerator
  - topology.nic
  - topology.pcie_path
  - topology.numa_node
  - topology.rail
  - workload.network_traffic
constraints:
  - pcie-bandwidth
  - numa-locality
  - nic-injection-bandwidth
  - shared-switch-contention
  - rail-placement
outputs:
  - accelerator_nic_distance
  - preferred_nic
  - network_path
  - locality_penalty
  - rail_assignment
assumptions:
  - NIC 数量相同不代表 accelerator 到 NIC 的 path 相同
  - affinity 必须按真实 PCIe/NUMA/fabric 路径判断
related_layers:
  - workload
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
  - nic-affinity
---
# GPU/NPU ↔ NIC Affinity

> Accelerator 到 NIC 的距离会决定 scale-out 流量走哪条 PCIe/NUMA 路径。一个节点有多张 NIC，不代表任意 accelerator 都能以同样成本访问任意 NIC。

## Path

典型逻辑路径：

```text
accelerator
→ local PCIe / fabric
→ NIC
→ network
```

但实际可能经过：

- shared PCIe switch
- CPU root complex
- cross-socket / NUMA path
- different rail

所以 affinity 是 graph 属性。

## Preferred NIC

对 accelerator i 和 NIC j，可以记录：

```text
path(i, j)
```

并基于：

- hop count
- bottleneck bandwidth
- NUMA crossing
- shared switch
- rail

选择 preferred NIC。

这比“node 有 8 NIC”更有调度价值。

## Shared Switch

若多个 accelerator 和 NIC 共享同一 PCIe switch，上游带宽可能成为共同 bottleneck。

因此：

```text
sum(endpoint peak)
```

不等于 switch uplink 能同时承载的吞吐。

## NUMA

当 accelerator 和 NIC 挂在不同 CPU/socket locality 下，数据路径可能跨 NUMA。

需要区分：

- local root complex
- remote root complex
- host memory staging
- peer/direct path if available

具体结构见 [[system/topology/numa-and-pcie-topology|NUMA / PCIe Topology]]。

## Rail

多 rail 网络中，NIC 可能属于不同 fabric plane / rail。

rank placement 需要让：

```text
accelerator group
↔ NIC assignment
↔ rail assignment
```

一致，避免所有流量集中到同一 rail。

## Communication Pattern

不同 workload 需要不同 affinity：

- TP 跨节点：频繁 collective
- EP：All-to-All
- PP：邻接 P2P
- KV transfer：source/destination heavy P2P

因此 preferred NIC 不能只看静态 nearest hop，还要结合 traffic pattern。

## Scheduling

[[system/scheduling/topology-aware-scheduling|拓扑感知调度]] 应把：

- accelerator
- NIC
- NUMA
- rail

作为一个 placement bundle，而不是分别选完再拼接。

## Output

- `accelerator_nic_distance`
- `preferred_nic`
- `network_path`
- `locality_penalty`
- `rail_assignment`

## 直接来源

本页定义通用 accelerator↔NIC locality 与调度边界，没有引入具体服务器拓扑或产品数值，因此 `evidence: {}`。
