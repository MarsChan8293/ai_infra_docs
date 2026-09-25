---
schema_version: system-v0.1
name: Activation Memory Model
object_type: concept
category: memory-model
inputs:
  - model.architecture
  - workload.batch_size
  - workload.sequence_length
  - workload.micro_batch
  - execution.activation_precision
  - execution.kernel_fusion
  - execution.recomputation
  - workload.parallelism
constraints:
  - memory-capacity
  - tensor-lifetime
  - pipeline-schedule
  - recomputation
  - workspace
outputs:
  - activation_live_bytes
  - activation_peak_bytes
  - saved_activation_bytes
  - recompute_tradeoff
  - per_device_activation_bytes
assumptions:
  - Activation peak 按 live tensor 生命周期计算，不把历史生成过的 tensor 全部累加
  - 推理和训练 activation 必须分开
  - Kernel fusion 可能消除 HBM 中间态，但未知时不默认消除
related_layers:
  - model
  - workload
  - compute
  - memory
  - parallelism
  - accelerator
evidence: {}
updated: 2026-09-25
tags:
  - system
  - memory
  - activation
---
# Activation Memory Model

> Activation Memory Model 关注执行过程中同时存活的中间 tensor。关键指标是 peak live bytes，而不是“所有 layer 曾经生成过多少字节”的历史总和。

## Activation 与 KV

必须分开：

- Activation：算子/层执行过程中的临时中间状态；
- KV / recurrent state：跨 Decode step 或序列生命周期保留的模型状态。

KV 见 [[system/memory/kv-cache-model|KV Cache Model]]。

把两者混在一起会同时误判 capacity 和 lifetime。

## Live Set

在时间点 `t`：

```text
activation_live_bytes(t)
= Σ size(tensor_i)
  for all live activation tensors
```

峰值：

```text
activation_peak_bytes
= max_t activation_live_bytes(t)
```

这是 capacity accounting 应使用的量。

## 推理 Prefill

Prefill activation 受：

- total prompt token rows
- hidden size
- attention implementation
- MLP intermediate size
- fusion
- tensor parallel sharding

影响。

长 sequence 可能让某些 attention intermediate 很大，但 Flash/streaming 风格 kernel 可以改变中间 tensor 是否落到 HBM。

因此不能只靠数学 attention matrix 大小直接等同真实 activation resident bytes。

## 推理 Decode

Decode 的 active token rows 通常远少于 Prefill，但：

- active batch
- context-dependent attention workspace
- sampling buffer
- graph/runtime buffer

仍会形成 activation/workspace。

所以 Decode activation 不能简单按“1 token”视为零。

## Training Saved Activations

反向传播需要前向信息。

训练时要区分：

```text
ephemeral_forward_activation
saved_for_backward_activation
recomputed_activation
```

若不重计算，更多前向 activation 需要跨较长时间保留。

## Activation Checkpointing / Recomputation

Checkpointing 的核心交换：

```text
less saved activation memory
↔ more forward recomputation
```

概念上：

```text
saved_activation_bytes ↓
recompute_FLOPs ↑
```

不能把“节省多少显存”写成全仓固定比例，因为它取决于 checkpoint granularity 和模型结构。

## Micro Batch

训练 activation 通常强依赖 micro batch。

在其他 shape 不变的简单场景：

```text
activation bytes
∝ micro_batch
```

但 sequence packing、variable length、kernel workspace 和 pipeline schedule 会改变精确关系。

因此 Training Workload 必须明确：

- global batch
- micro batch
- gradient accumulation

而不能只给一个 batch size。

## Sequence Length

许多 activation tensor 至少随：

```text
batch × sequence × hidden
```

增长。

Full attention 某些 naive intermediate 还可能具有 sequence² 规模，但真实 kernel 是否 materialize 这些 tensor 取决于实现。

System 文档应区分：

```text
mathematical intermediate
vs
materialized HBM tensor
```

## Tensor Parallel

TP 可能切分 activation，也可能要求：

- All-Gather
- Reduce-Scatter
- temporary communication buffer

所以 per-device activation：

```text
local activation shard
+ replicated activation
+ communication staging
```

不能无条件除以 TP degree。

## Pipeline Parallel

PP 的 activation peak 还取决于：

- number of microbatches in flight
- 1F1B / other schedule
- pipeline depth
- stage boundary
- send/recv buffer

多个 microbatch 同时在 stage 内存活会增加 peak。

因此 PP memory 必须绑定具体 schedule。

## Fusion

Kernel fusion 可以让部分中间 tensor：

- 留在 register / SRAM
- 不写回 HBM
- 缩短 lifetime

但 fusion 是 implementation fact。

如果 software/kernel 未指定，不应默认“理论可 fusion”就等于实际已经消除内存。

## Workspace 边界

Activation 与 workspace 也要分开。

Workspace 是 kernel/runtime 为算法执行申请的 scratch / temporary storage，可能与 activation 同时达到峰值。

最终两者在 [[system/memory/model-memory-accounting|Memory Accounting]] 中合并。

## Training Memory

完整训练内存还包括：

- weights
- gradients
- optimizer states
- possible master weights
- activations
- communication buffers

Activation Model 只解决其中一项。

后续 `TRN-002` 负责完整 Training Memory Model。

## 输出

- `activation_live_bytes`
- `activation_peak_bytes`
- `saved_activation_bytes`
- `recompute_tradeoff`
- `per_device_activation_bytes`

输出必须绑定 phase、batch/sequence、precision、parallelism、schedule 和 kernel assumptions。

## 直接来源

本页定义通用 activation lifetime/accounting 方法，没有引入具体 framework 实现或 benchmark 数值，因此 `evidence: {}`。
