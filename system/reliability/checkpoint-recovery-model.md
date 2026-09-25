---
schema_version: system-v0.1
name: Checkpoint / Recovery Model
object_type: concept
category: reliability
inputs:
  - training.checkpoint_payload_bytes
  - training.checkpoint_interval
  - storage.effective_write_bandwidth
  - storage.effective_read_bandwidth
  - reliability.failure_domain
  - reliability.restart_scope
constraints:
  - checkpoint-bandwidth
  - checkpoint-latency
  - lost-work
  - recovery-time
  - storage-capacity
outputs:
  - checkpoint_time
  - restore_time
  - maximum_lost_work
  - recovery_time
  - checkpoint_tradeoff
assumptions:
  - checkpoint interval 必须带 step/token/time 单位
  - 异步 checkpoint 只有被真实 overlap 的部分才能从 critical path 中隐藏
related_layers:
  - workload
  - memory
  - communication
  - topology
  - storage
  - reliability
  - accelerator
evidence: {}
updated: 2026-09-25
tags: [system, reliability, checkpoint, recovery]
---
# Checkpoint / Recovery Model

> Checkpoint 用写入和存储成本换取更小的故障丢失窗口。正确问题不是“多久存一次”，而是 payload、带宽、阻塞时间、故障域和 restart scope 的联合优化。

## Checkpoint Payload

需要明确 checkpoint 包含：

- model weights
- optimizer states
- scheduler/RNG state
- dataloader progress
- other restart-critical state

不能用模型 weight size 自动替代 checkpoint size。

## Checkpoint Time

若 payload D bytes、有效写带宽 B_write：

```text
T_checkpoint_lower_bound
>= D / B_write
```

真实时间还可能包含：

- serialization
- staging
- metadata
- distributed coordination
- storage contention

## Restore

同理：

```text
T_restore_lower_bound
>= D_restore / B_read
```

之后还可能有 process restart、graph/runtime initialization 和 topology reformation。

## Interval

Checkpoint interval 必须声明单位，例如：

- every N optimizer steps
- every N useful tokens
- every N minutes

最大理论 lost-work window 与 interval 同阶，但实际 recovery point 还取决于 checkpoint completion semantics。

## Async Checkpoint

异步写入可以把部分 storage traffic 移出 compute critical path，但会增加：

- staging memory
- background bandwidth
- overlap contention

因此：

```text
async != free
```

## Failure Domain

一个 checkpoint 如果和计算资源处在同一 correlated failure domain，故障时可能一起不可用。

需要联合 [[system/topology/rack-and-failure-domain|Rack / Failure Domain]] 与 [[system/reliability/accelerator-and-network-failure-domain|Accelerator / Network Failure Domain]]。

## Recovery Scope

故障可能要求重启：

- one rank
- parallel group
- node
- whole job

恢复 scope 越大，读取 payload 与重新建立分布式状态的成本通常越高。

## Tradeoff

Checkpoint 越频繁：

```text
lost work ↓
checkpoint overhead ↑
```

越稀疏则相反。

没有 failure-rate 数据时，不计算“最优 interval”，只保留 tradeoff。

## 输出

- `checkpoint_time`
- `restore_time`
- `maximum_lost_work`
- `recovery_time`
- `checkpoint_tradeoff`

## 直接来源

本页定义通用 checkpoint/recovery 成本边界，不引入具体存储设备或故障率，因此 `evidence: {}`。
