---
schema_version: system-v0.1
name: Disaggregated Prefill / Decode
object_type: concept
category: serving
inputs:
  - workload.prefill
  - workload.decode
  - compute.prefill
  - compute.decode
  - memory.kv
  - topology.transfer_path
constraints:
  - ttft
  - tpot
  - kv-transfer
  - queueing
  - resource-balance
outputs:
  - prefill_pool
  - decode_pool
  - kv_handoff_bytes
  - disaggregation_break_even
  - role_capacity_balance
assumptions:
  - P/D 分离只有在专门化收益超过 KV 交接和协调成本时才有系统收益
  - Prefill/Decode 资源适配是 workload 派生属性，不是芯片固有标签
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
tags: [system, serving, prefill, decode, disaggregation]
---
# Disaggregated Prefill / Decode

> P/D 分离把 Prefill 与 Decode 放到不同资源池，通过 KV/state handoff 连接两阶段。它的目标是分别优化两类 workload，但代价是新增 transfer、排队与容量协调。

## 为什么分离

[[system/compute/prefill-vs-decode|Prefill vs Decode]] 已说明两阶段的 compute shape、memory traffic 和 latency budget 不同。

分离后可以分别选择：

- batch policy
- resource pool
- placement
- capacity headroom

但系统必须付出 state handoff。

## 数据流

```text
request
→ prefill queue
→ prefill worker
→ KV/state produced
→ state transfer
→ decode queue
→ decode worker
→ output
```

TTFT 和 TPOT 之间因此新增一个阶段边界。

## Break-even

抽象收益条件：

```text
T_saved_by_specialization
>
T_state_transfer
+ T_extra_queue
+ T_coordination
```

若 transfer 占掉全部专门化收益，分离只增加复杂度。

## Capacity Balance

Prefill pool 与 Decode pool 的服务率需要匹配。

长期稳定要求：

```text
prefill departure rate
≈ decode admission rate
```

若 Prefill 远快于 Decode，会把压力转成：

- decode queue
- pending KV state
- memory/network capacity

反之则 Decode 资源空转。

## KV Handoff

Handoff bytes 来自 [[system/memory/kv-cache-model|KV Cache Model]]，路径来自 [[system/topology/scale-up-vs-scale-out|Topology]]。

具体 transfer cost 由后续任务 SRV-005 单独建模。

## Local vs Remote

P/D pools 可以：

- 同 node
- 同 scale-up domain
- 跨 node
- 跨 rack

path 越远，transfer 带宽、时延、failure domain 和 staging 都可能变化。

## Failure

Prefill 完成但 KV 尚未被 Decode 接管时，要定义：

- ownership
- retry
- duplicate copy
- cleanup

这些影响 memory peak 和可靠性。

## 输出

- `prefill_pool`
- `decode_pool`
- `kv_handoff_bytes`
- `disaggregation_break_even`
- `role_capacity_balance`

## 直接来源

本页定义 P/D 分离的通用系统边界和 break-even 关系，不绑定具体 serving runtime，因此 `evidence: {}`。
