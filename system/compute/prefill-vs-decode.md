---
schema_version: system-v0.1
name: Prefill vs Decode
object_type: concept
category: compute-model
inputs:
  - model.architecture
  - model.parameters
  - workload.prefill_tokens
  - workload.decode_active_sequences
  - workload.context_length
  - workload.batch_size
  - memory.weight_bytes
  - memory.kv_bytes
constraints:
  - compute-throughput
  - memory-bandwidth
  - latency
  - kv-capacity
  - communication
outputs:
  - prefill_compute_shape
  - decode_compute_shape
  - prefill_time_lower_bound
  - decode_time_lower_bound
  - weight_bytes_per_token
  - kv_bytes_per_step
  - phase_bottleneck_candidates
assumptions:
  - Prefill 与 Decode 必须独立建模后再组成请求延迟
  - 不把 Prefill 恒定标记为 compute-bound，也不把 Decode 恒定标记为 memory-bound
related_layers:
  - model
  - workload
  - compute
  - memory
  - parallelism
  - communication
  - topology
  - accelerator
evidence: {}
updated: 2026-09-25
tags:
  - system
  - compute
  - inference
  - prefill
  - decode
---
# Prefill vs Decode

> Prefill 与 Decode 使用同一套模型权重，却是两种不同的系统 workload。前者一次处理大量输入 token，后者反复处理少量新 token 并访问不断增长的状态。

## 请求时间分解

一个自回归请求可以抽象为：

```text
T_request
=
T_queue
+ T_prefill
+ Σ T_decode_step
+ other_overhead
```

因此 TTFT 与后续 TPOT 不应由同一个平均 tokens/s 代替。

输入语义见 [[system/workload/inference-workload|Inference Workload]]。

## Prefill

假设一个 batch 中总共有 `M_prefill` 个有效 prompt token row。

参数化线性层通常形成较大的 GEMM：

```text
[M_prefill × K] @ [K × N]
```

其主要乘加：

```text
F_linear_prefill
≈ 2 × M_prefill × K × N
```

对 full dense attention，单序列长度 `S` 的 pairwise attention work 具有 `O(S²)` 项。

Prefill 还会：

- 写入 growing KV
- 生成 fixed recurrent state
- 受 padding / packing 影响
- 可能受 multimodal encoder 前处理影响

## Decode

典型自回归 Decode step 中，每个 active sequence 只新增少量 token。

若当前 active sequence 数为 `B_active`，线性层有效 `M` 常接近：

```text
M_decode ≈ B_active
```

而不是 context length。

但 attention / state 访问会依赖已有 context。

因此 Decode 同时具有：

- 小 M 的 weight GEMM/GEMV tendency
- growing KV read
- new KV write
- sampling / scheduler dependency

## Weight Reuse

假设某一 Decode step 需要触碰 `W` bytes 权重，并且一次读取服务 `B_active` 个 token：

```text
weight_bytes_per_token
≈ W / B_active
```

这解释了为什么增加 decode batch 可能提高 weight reuse 和 Arithmetic Intensity。

但只有在“同一 weight read 确实服务这些 token”的实现条件下才成立。

## KV Growth

每个新 token 的 growing KV payload 由 [[system/memory/kv-cache-model|KV Cache Model]] 给出。

```text
kv_write_per_step
≈ new_tokens
× growing_kv_bytes_per_token
```

历史 KV read 则取决于 attention layout 与可见 context，不能直接由 capacity 字段替代。

## Context Length 对 Decode 的影响

对于 full attention，一个 query token 面对 context `L`，attention matmul work 与可读取 KV 状态通常随 `L` 增长。

因此同一个模型：

```text
Decode at 2K context
!= Decode at 128K context
```

即使 batch 和 output token 数相同。

## Arithmetic Intensity

Prefill 和 Decode 应分别计算：

```text
AI_prefill
= FLOPs_prefill / HBM_bytes_prefill

AI_decode
= FLOPs_decode / HBM_bytes_decode
```

统一方法见 [[system/compute/roofline-and-arithmetic-intensity|Roofline]]。

不能用一个模型级 `FLOP/byte` 覆盖整个请求生命周期。

## 为什么 Prefill 常更容易形成大 GEMM

Prefill 一次拥有更多 token rows，通常能增大 GEMM 的 `M` 维度。

这可能：

- 提高矩阵单元利用率
- 摊薄 weight traffic/token
- 提高 arithmetic intensity

但长 context attention、memory capacity、kernel shape 等仍可能成为约束。

所以“Prefill compute-bound”只是常见现象，不是 schema 事实。

## 为什么 Decode 常更敏感于 Memory

Decode 每 step token rows 较少，权重和 KV 数据移动可能占更大比例。

但以下因素可以改变结论：

- large continuous batch
- quantized weights
- cache reuse
- MLA / GQA
- speculative decoding
- hardware cache hierarchy
- kernel fusion

所以“Decode memory-bound”也只能由具体 Roofline 判断。

## 时间下界

分别定义：

```text
T_prefill_compute
T_prefill_memory
T_prefill_comm

T_decode_compute
T_decode_memory
T_decode_comm
```

若阶段内资源可以高度 overlap：

```text
T_phase
>= max(
  T_compute,
  T_memory,
  T_comm
)
```

若存在串行 dependency，则按 critical path 加和。

Communication 使用 [[system/communication/communication-cost-model|Communication Cost Model]]。

## TTFT

TTFT 的建模边界至少说明：

```text
queue
+ scheduling
+ state/input transfer
+ prefill
+ first-token boundary
```

不同 benchmark 对 first-token boundary 定义可能不同，因此比较前必须统一口径。

## TPOT

TPOT 不应只给平均值。

需要绑定：

- context length
- active batch
- output position
- percentile
- parallelism
- hardware topology

因为随着 context 增长，后续 decode step 可能比前面的 step 更贵。

## P/D 分离的前置条件

将 Prefill 和 Decode 放到不同资源池之前，必须先知道两阶段的：

- compute work
- memory footprint / bandwidth
- KV transfer bytes
- SLA budget
- topology

否则无法判断拆分收益是否大于 KV transfer 和调度成本。

具体 P/D disaggregation 留给 `SRV-004`。

## 输出

- `prefill_compute_shape`
- `decode_compute_shape`
- `prefill_time_lower_bound`
- `decode_time_lower_bound`
- `weight_bytes_per_token`
- `kv_bytes_per_step`
- `phase_bottleneck_candidates`

## 与其他层的关系

- Inference workload：[[system/workload/inference-workload|Inference Workload]]
- Compute：[[system/compute/transformer-compute-model|Transformer Compute Model]]
- KV：[[system/memory/kv-cache-model|KV Cache Model]]
- Memory bandwidth：[[system/memory/memory-bandwidth-model|Memory Bandwidth Model]]
- Roofline：[[system/compute/roofline-and-arithmetic-intensity|Roofline]]
- Communication：[[system/communication/communication-cost-model|Communication Cost Model]]

## 直接来源

本页定义仓库内部 Prefill / Decode 分解和系统公式，没有引入特定 benchmark 或厂商性能数字，因此 `evidence: {}`。
