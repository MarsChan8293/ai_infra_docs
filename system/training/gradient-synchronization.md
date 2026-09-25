---
schema_version: system-v0.1
name: Gradient Synchronization
object_type: concept
category: training
inputs:
  - training.trainable_parameters
  - training.gradient_precision
  - parallelism.dp_degree
  - communication.bucket_size
  - topology
constraints:
  - all-reduce
  - reduce-scatter
  - bandwidth
  - latency
  - overlap
outputs:
  - gradient_payload_bytes
  - bucket_schedule
  - communication_time
  - exposed_tail_time
  - synchronization_efficiency
assumptions:
  - 总 gradient bytes 与暴露在 step critical path 上的通信时间分开
  - overlap 只有在 gradient ready 和 independent compute 存在时才成立
related_layers:
  - workload
  - compute
  - memory
  - parallelism
  - communication
  - topology
  - accelerator
  - network
evidence: {}
updated: 2026-09-25
tags: [system, training, gradient, communication]
---
# Gradient Synchronization

> Gradient Synchronization 把 backward 产生的 gradient 从本地状态变成跨 replica 一致或分片后的状态。系统瓶颈通常由 payload、bucket、collective、topology 和 exposed tail 共同决定。

## Payload

基线：

```text
gradient_payload_bytes
≈ trainable_parameter_elements
× bytes_per_gradient_element
```

Frozen / unused parameters、sharding 和压缩会改变实际 payload。

## Collective

Replicated DP 常使用 All-Reduce；状态分片方案可能使用 Reduce-Scatter / All-Gather。

基础通信量见：

[[system/communication/all-reduce-all-gather-reduce-scatter|All-Reduce / All-Gather / Reduce-Scatter]]

## Bucketing

把 gradient 分成 buckets 可以在部分层 backward 完成后提前发起通信：

```text
backward layer
→ gradient ready
→ bucket ready
→ collective
```

Bucket 太大可能推迟启动；太小则增加 startup 次数。

## Overlap

理想情况下 communication 与剩余 backward overlap。

需要关注：

```text
total communication time
exposed communication tail
```

训练 step 更直接受 exposed tail 影响。

## Topology

随着 DP group 扩展到更多 node/rack：

- participant count 增加
- scale-out path 增加
- bisection / NIC injection 更重要

因此不能只用单机 collective benchmark 推大规模结果。

## Gradient Accumulation

如果多个 microbatch 先本地 accumulation，再同步：

```text
sync frequency ↓
compute between sync ↑
```

但 global batch / optimization cadence 也会变化，应由 [[system/workload/training-workload|Training Workload]] 记录。

## 输出

- `gradient_payload_bytes`
- `bucket_schedule`
- `communication_time`
- `exposed_tail_time`
- `synchronization_efficiency`

## 直接来源

本页定义通用 gradient synchronization 数据流，不绑定具体 framework，因此 `evidence: {}`。
