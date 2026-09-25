---
schema_version: system-v0.1
name: NUMA / PCIe Topology
object_type: concept
category: topology
inputs:
  - topology.cpu_sockets
  - topology.numa_nodes
  - topology.pcie_roots
  - topology.pcie_switches
  - topology.accelerators
  - topology.nics
constraints:
  - pcie-bandwidth
  - pcie-hop-count
  - numa-locality
  - shared-uplink
  - peer-path
outputs:
  - device_topology_graph
  - numa_assignment
  - pcie_path
  - shared_bottlenecks
  - placement_constraints
assumptions:
  - PCIe generation/width 等具体规格由硬件事实页提供
  - NUMA 距离必须按真实 node topology 判断，不使用统一惩罚系数
related_layers:
  - workload
  - memory
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
  - numa
  - pcie
---
# NUMA / PCIe Topology

> NUMA / PCIe Topology 把 CPU socket、root complex、PCIe switch、accelerator 和 NIC 组织成一张物理 graph。它解释为什么“同一个节点里的两张卡”也可能有完全不同的数据路径。

## Topology Graph

建议把节点内结构表示为：

```text
CPU / NUMA
  ├─ PCIe root / switch
  │    ├─ accelerator
  │    └─ NIC
  └─ inter-socket path
       └─ other root / switch / devices
```

真实机器可能更复杂，但分析原则相同。

## Root Complex

两个 device 若挂在同一 root / switch 下，P2P path 与跨 root/NUMA 的 path 可能不同。

因此需要记录：

```text
device_a
→ switches / root
→ device_b
```

而不是只记录“都支持 PCIe”。

## Shared Uplink

多个 endpoint 的峰值可能共享上游。

若：

```text
accelerator_1
accelerator_2
NIC
   ↓
shared switch uplink
```

则共同流量会竞争该 uplink。

所以 endpoint link peak 不能简单求和。

## NUMA Locality

Host memory、CPU thread、NIC 和 accelerator 应尽量描述其 NUMA 归属。

典型问题包括：

- host staging buffer 分配在哪个 NUMA node
- CPU preprocessing 在哪个 socket
- NIC 属于哪个 locality
- accelerator 访问 host memory 是否跨 socket

这些都会改变 latency / bandwidth。

## Accelerator ↔ NIC

具体 affinity 由：

[[system/topology/gpu-nic-affinity|GPU/NPU ↔ NIC Affinity]]

进一步建模。

本页提供其底层 PCIe / NUMA graph。

## Peer Path

Accelerator peer transfer 可能：

- 走 dedicated accelerator fabric
- 走 PCIe switch
- 经过 host/root path

因此 path selection 需要联合 [[system/topology/accelerator-fabric|Accelerator Fabric]]。

## Memory Tier

Host / pooled memory 的访问路径也挂在拓扑上。

[[system/memory/cxl-and-memory-pooling|CXL / Memory Pooling]] 的 remote memory latency/bandwidth 不能脱离 NUMA/PCIe path 单独评估。

## Placement

调度器应把：

```text
CPU locality
+ accelerator locality
+ NIC locality
+ memory locality
```

作为一个组合约束。

只满足 accelerator count 可能仍产生非常差的数据路径。

## Output

- `device_topology_graph`
- `numa_assignment`
- `pcie_path`
- `shared_bottlenecks`
- `placement_constraints`

## 直接来源

本页定义通用 NUMA / PCIe graph 建模，不引入具体 PCIe 代际、lane bandwidth 或服务器产品拓扑，因此 `evidence: {}`。
