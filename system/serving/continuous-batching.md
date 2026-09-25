---
schema_version: system-v0.1
name: Continuous Batching
object_type: concept
category: serving
inputs:
  - workload.request_rate
  - workload.active_sequences
  - workload.context_length_distribution
  - workload.output_length_distribution
  - workload.sla
  - memory.kv_capacity
constraints:
  - ttft
  - tpot
  - queueing
  - kv-capacity
  - scheduler-overhead
outputs:
  - dynamic_batch_size
  - admission_policy
  - iteration_token_count
  - capacity_envelope
  - latency_throughput_tradeoff
assumptions:
  - scheduler batch 是随迭代变化的状态，不等于系统并发数
  - 提高 batch 只有在 SLA 与 memory envelope 内才构成收益
related_layers:
  - workload
  - compute
  - memory
  - scheduling
  - accelerator
evidence: {}
updated: 2026-09-25
tags: [system, serving, batching]
---
# Continuous Batching

> Continuous Batching 在每个调度轮次重新组合仍然活跃的请求，让新请求、长短不同的 Decode 序列和完成请求动态进入或退出执行批次。

## 三个不同的数量

必须区分：

```text
concurrency
scheduler_batch_size(t)
kernel_effective_rows(t)
```

并发是系统里活跃请求数；scheduler batch 是某轮被选中的请求；kernel shape 还会受 phase、padding 和算子结构影响。

## 调度循环

典型抽象：

```text
admit requests
→ choose runnable sequences
→ reserve/check KV capacity
→ execute one scheduling quantum
→ append tokens / finish requests
→ repeat
```

因此 batch 是时间函数：

```text
B = B(t)
```

不能用一个固定 batch 代表整个服务周期。

## Throughput 与 Latency

更大的 batch 可能提高：

- weight reuse
- GEMM utilization
- tokens/step

但也可能增加：

- queue wait
- per-step latency
- KV resident bytes
- tail latency

所以 admission policy 的目标不是“batch 越大越好”，而是在 [[system/workload/inference-workload|Inference Workload]] 的 TTFT/TPOT/SLA 下最大化可持续服务能力。

## KV Capacity

每个 active sequence 都占用状态。粗粒度约束是：

```text
sum(per-sequence allocated KV/state)
+ other device memory
<= usable device memory
```

KV 大小由 [[system/memory/kv-cache-model|KV Cache Model]] 给出；allocator 与其他 resident bytes 进入 [[system/memory/model-memory-accounting|Memory Accounting]]。

## Length Heterogeneity

不同请求拥有不同：

- prompt length
- current context
- remaining output
- cache reuse

因此同一个 batch 中每条序列的 compute/memory cost 不相同。仅报告 batch size 无法完整解释性能。

## Admission

新请求是否进入当前调度窗口至少受：

- KV headroom
- latency budget
- priority
- phase
- current batch shape

限制。

如果持续 arrival rate 超过稳定服务率，continuous batching 只能改变效率，不能消除无限排队。

## 输出

- `dynamic_batch_size`
- `admission_policy`
- `iteration_token_count`
- `capacity_envelope`
- `latency_throughput_tradeoff`

## 直接来源

本页定义通用 continuous-batching 系统语义，不绑定具体 runtime 实现，因此 `evidence: {}`。
