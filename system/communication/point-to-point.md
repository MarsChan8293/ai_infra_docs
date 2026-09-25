---
schema_version: system-v0.1
name: Point-to-Point Communication
object_type: concept
category: communication-model
inputs:
  - communication.payload_bytes
  - communication.source
  - communication.destination
  - topology.path
  - topology.effective_bandwidth
  - topology.path_latency
constraints:
  - path-bandwidth
  - path-latency
  - staging
  - synchronization
  - buffer-capacity
outputs:
  - p2p_payload_bytes
  - p2p_path
  - p2p_time_lower_bound
  - staging_bytes
assumptions:
  - P2P 必须明确 source/destination 和数据所在 memory tier
  - 经过 host staging 或多级 memory 时每一段都单独计入
related_layers:
  - workload
  - parallelism
  - communication
  - topology
  - memory
  - accelerator
  - network
evidence: {}
updated: 2026-09-25
tags:
  - system
  - communication
  - p2p
---
# Point-to-Point Communication

> Point-to-Point 是一个 source 到一个 destination 的依赖路径。PP activation、KV transfer、remote state fetch 都可以归一成 P2P，但路径可能完全不同。

## 最小模型

设 payload 为 `D` bytes，端到端有效带宽为 `B_path`，固定 path latency 为 `L_path`：

```text
T_p2p
>= L_path + D / B_path
```

这是理想 lower bound。

真实时间还可能包含：

- software dispatch
- layout conversion
- source synchronization
- destination synchronization
- staging
- queueing

## Path 必须显式

不要只记录：

```text
source GPU → destination GPU
```

而应尽可能解析成：

```text
source HBM
→ local fabric / PCIe
→ NIC
→ network
→ remote NIC
→ remote fabric / PCIe
→ destination HBM
```

实际 bottleneck 是 path 上的最弱环节。

## Multi-stage

若必须串行经过多个 stage：

```text
T
>= Σ latency_i
 + Σ D_i / B_i
```

如果可以 pipeline：

```text
steady_state_throughput
<= min(B_i)
```

但仍需计 fill / drain。

## Host Staging

若 device-to-device transfer 需要先落到 host memory：

```text
device
→ host buffer
→ network / peer
→ host buffer
→ device
```

则必须记录：

- staging capacity
- extra memory copies
- host bandwidth
- NUMA affinity

不能仍按单一 device link bandwidth 计算。

## Pipeline Parallel

PP 的主要 P2P payload 通常是 stage boundary activation。

每个 microbatch：

```text
stage_i
→ activation payload
→ stage_i+1
```

因此性能受：

- activation size
- microbatch cadence
- pipeline schedule
- neighbor placement

影响。

详见 [[system/parallelism/pipeline-parallelism|Pipeline Parallelism]]。

## KV Transfer

P/D 分离或 KV offload 也可以视为 P2P / staged P2P。

需要比较：

```text
T_transfer
vs
T_recompute
```

而不仅是介质容量。

KV 大小来自 [[system/memory/kv-cache-model|KV Cache Model]]，驻留层级来自 [[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层级]]。

## Buffering

异步 P2P 通常需要 send/recv buffer。

因此：

```text
communication payload
≠ peak buffer capacity automatically
```

双 buffer、pipeline depth 或 retransmit 可能增加 peak resident bytes。

这些 buffer 最终进入 [[system/memory/model-memory-accounting|Memory Accounting]]。

## Topology

同样大小的 payload：

- 同 scale-up domain
- 同 node 跨 PCIe switch
- 跨 NIC
- 跨 rack

会有不同 `B_path` 和 `L_path`。

所以 P2P 必须与 [[system/topology/scale-up-vs-scale-out|Topology]] 联合建模。

## 输出

- `p2p_payload_bytes`
- `p2p_path`
- `p2p_time_lower_bound`
- `staging_bytes`

统一时间分解见 [[system/communication/communication-cost-model|Communication Cost Model]]。

## 直接来源

本页定义通用 P2P critical-path 模型，没有引入具体互联协议或 benchmark，因此 `evidence: {}`。
