---
schema_version: system-v0.1
name: CXL / Memory Pooling
object_type: concept
category: memory-architecture
inputs:
  - workload.working_set_bytes
  - workload.access_pattern
  - memory.local_capacity
  - memory.remote_capacity
  - memory.remote_bandwidth
  - memory.remote_latency
  - topology.path
constraints:
  - capacity
  - bandwidth
  - latency
  - locality
  - failure-domain
outputs:
  - tier_placement
  - pooled_memory_capacity
  - remote_memory_traffic
  - remote_memory_time_lower_bound
  - placement_tradeoff
assumptions:
  - CXL/pooled memory 在本页作为较远 memory tier 建模，不把它视为 HBM 等价替代
  - 协议细节、交换器能力和实际带宽必须由具体硬件事实页提供
related_layers:
  - workload
  - memory
  - communication
  - topology
  - storage
  - accelerator
  - reliability
evidence: {}
updated: 2026-09-25
tags:
  - system
  - memory
  - cxl
  - pooling
---
# CXL / Memory Pooling

> CXL / Memory Pooling 在本仓库中首先是“把容量放到更远 memory tier”的系统问题，而不是“增加了多少 GB 就等于增加了多少 HBM”。

## 分层位置

概念链：

```text
accelerator local memory
→ host / attached memory
→ pooled / fabric-attached memory
→ storage
```

具体系统不一定包含所有层。

本页不规定某一代 CXL 协议细节，只定义容量、带宽、时延、拓扑和故障域的系统交换。

## Capacity

若本地可用容量：

```text
C_local
```

workload working set：

```text
W
```

当：

```text
W > C_local
```

可以把部分状态放到更远 tier。

但：

```text
local_capacity + remote_capacity
```

只说明逻辑容量池，不代表所有数据都具有相同访问成本。

## Placement

一个对象应记录：

- logical bytes
- local resident bytes
- remote resident bytes
- migration / fetch bytes
- replication
- dirty/writeback behavior
- locality / owner

因此：

```text
object_size
!= device_resident_size
!= transfer_bytes_per_step
```

## Bandwidth / Latency

若每 step 需要访问远端 `D_remote` bytes，远端有效 bandwidth 为 `B_remote`：

```text
T_remote_bandwidth
>= D_remote / B_remote
```

若访问粒度小或 dependency 串行，还需加入 latency。

所以远端 memory 是否有价值取决于 workload：

- sequential bulk transfer
- random small access
- prefetchable state
- latency-critical state

不能只比较 capacity。

## Hot / Warm / Cold

典型分层思路可以抽象为：

```text
hot state   → local high-bandwidth tier
warm state  → pooled / remote memory
cold state  → storage
```

“冷热”是 workload 属性，不是介质固定标签。

## KV Cache

长上下文或高并发 KV 可能推动容量向更远层扩展。

但判断是否适合放到 pooled memory，需要联合：

- [[system/memory/kv-cache-model|KV Cache Model]]
- [[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层级]]
- [[system/memory/memory-bandwidth-model|Memory Bandwidth Model]]

如果 retrieve 时间超过 recompute 或 SLA 预算，额外容量并不产生系统收益。

## Weight Offload

Weight 也可以分层：

```text
full model weights
→ local working set
+ remote/offloaded remainder
```

但如果每个 token 都频繁 fetch 远端 weight，remote bandwidth 可能成为新的 ceiling。

所以 Weight Offload 必须和 [[system/memory/weight-memory|Weight Memory Model]] 联合。

## Topology

Remote memory 的路径可能涉及：

- CPU / root complex
- switch
- fabric
- memory device / pool

因此物理 locality 会改变：

- latency
- bandwidth
- contention
- failure scope

具体 path 由 [[system/topology/numa-and-pcie-topology|NUMA / PCIe Topology]] 记录。

## Pooling vs Sharing

Pooling 至少应区分：

- capacity is pooled
- allocation can move
- multiple hosts can access
- data is replicated or single-owned

这些语义不同，不能因为“共享一个 pool”就假定任意 accelerator 可等价访问所有 bytes。

## Failure Domain

把更多状态放到共享 pool 可能改变故障半径。

需要记录：

- pool device failure
- switch/path failure
- host attachment failure
- recovery / replica

所以 memory tiering 也属于 reliability 问题。

## 输出

- `tier_placement`
- `pooled_memory_capacity`
- `remote_memory_traffic`
- `remote_memory_time_lower_bound`
- `placement_tradeoff`

## 直接来源

本页只定义 pooled / remote memory 的系统建模边界，不写具体 CXL 版本、协议带宽或产品能力，因此 `evidence: {}`。
