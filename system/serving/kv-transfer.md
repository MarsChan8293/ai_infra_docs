---
schema_version: system-v0.1
name: KV Transfer
object_type: concept
category: serving
inputs:
  - memory.kv_payload_bytes
  - memory.kv_metadata_bytes
  - topology.transfer_path
  - topology.effective_bandwidth
  - topology.path_latency
  - compute.recompute_time
constraints:
  - transfer-bandwidth
  - transfer-latency
  - staging
  - serialization
  - sla
  - failure-domain
outputs:
  - transfer_payload_bytes
  - transfer_time_lower_bound
  - transfer_buffer_bytes
  - transfer_vs_recompute_break_even
  - handoff_completion_time
assumptions:
  - KV payload、metadata、allocator layout 与 wire payload 分开记录
  - 只有在 transfer 总成本小于 recompute 且满足 SLA 时，状态迁移才形成系统收益
related_layers:
  - workload
  - compute
  - memory
  - communication
  - topology
  - scheduling
  - accelerator
  - network
evidence: {}
updated: 2026-09-25
tags: [system, serving, kv-cache, transfer]
---
# KV Transfer

> KV Transfer 把已经生成的上下文状态从一个执行位置交给另一个位置。P/D 分离、KV offload、remote cache hit 都可以落到同一个问题：搬运这份状态是否比重新计算更便宜。

## Payload

首先区分：

```text
logical_kv_payload
allocator_resident_bytes
serialized_transfer_bytes
wire_bytes
```

它们不一定相等。

逻辑 KV 大小来自 [[system/memory/kv-cache-model|KV Cache Model]]。实际 transfer 还可能包含：

- quantization scale / metadata
- block/page descriptor
- alignment/padding
- header
- checksum
- layout conversion

因此：

```text
transfer_payload_bytes
=
logical_state_payload
+ transfer_metadata
+ serialization_overhead
```

## Path

典型路径可能是：

```text
source HBM
→ local fabric / PCIe
→ NIC
→ network
→ remote NIC / fabric
→ destination HBM
```

也可能只在同一个 node / scale-up domain 内。

路径由 [[system/topology/scale-up-vs-scale-out|Scale-up vs Scale-out]] 与 [[system/topology/numa-and-pcie-topology|NUMA / PCIe Topology]] 决定。

## 时间下界

若端到端有效带宽为 `B_path`，payload 为 `D`，固定 path latency 为 `L`：

```text
T_transfer_lower_bound
>= L + D / B_path
```

若存在多段串行 staging，则需要按 [[system/communication/point-to-point|Point-to-Point Communication]] 和 [[system/communication/communication-cost-model|Communication Cost Model]] 分段建模。

## Streaming

状态不一定要等全部传完才开始消费。

如果 source 能按 block/chunk 产生，destination 也能流式恢复，则可能形成：

```text
produce
→ send chunk
→ receive
→ consume
```

此时 steady-state 受最慢 stage 限制，但仍有 fill/drain 和 dependency。

因此：

```text
full_payload / bandwidth
```

不一定等于 handoff completion time，也不一定等于 visible stall。

## Transfer Buffer

异步 / pipeline transfer 可能需要：

- send buffer
- receive buffer
- double buffer
- staging buffer

所以 peak memory 还要把 transfer buffer 放入 [[system/memory/model-memory-accounting|Memory Accounting]]。

## P/D Handoff

[[system/serving/disaggregated-prefill-decode|Disaggregated Prefill / Decode]] 中：

```text
Prefill worker
→ produce KV/state
→ transfer
→ Decode worker
```

Decode admission 可能等待：

- full state
- required first blocks
- ownership transition

具体 handoff 语义必须显式说明。

## Remote Cache

远端 prefix/KV cache 命中也属于 transfer。

总收益条件：

```text
T_lookup
+ T_transfer
+ T_restore
<
T_recompute_saved
```

如果状态很大、路径较慢或命中位置太远，cache hit 仍可能不划算。

## Recompute Break-even

定义：

```text
delta
= T_recompute
- (
    T_lookup
  + T_serialize
  + T_transfer
  + T_restore
  + T_coordination
  )
```

只有：

```text
delta > 0
```

且不违反 TTFT/TPOT/SLA，才可认为迁移有时间收益。

容量收益与时间收益必须分开讨论。

## Failure / Retry

状态迁移期间需要明确：

- source ownership
- destination ownership
- transfer completion
- timeout
- retry
- duplicate state
- cleanup

否则失败时可能出现状态泄漏、重复占用或不可恢复请求。

## 输出

- `transfer_payload_bytes`
- `transfer_time_lower_bound`
- `transfer_buffer_bytes`
- `transfer_vs_recompute_break_even`
- `handoff_completion_time`

## 直接来源

本页定义通用 KV/state transfer 成本与 break-even，不绑定具体传输库或互联产品，因此 `evidence: {}`。
