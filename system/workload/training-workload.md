---
schema_version: system-v0.1
name: Training Workload
object_type: concept
category: workload-model
inputs:
  - model.intrinsic_facts
  - training.global_batch_size
  - training.micro_batch_size
  - training.gradient_accumulation_steps
  - training.sequence_length
  - training.sequence_packing
  - training.token_budget
  - training.checkpoint_interval
constraints:
  - step-time
  - memory-capacity
  - throughput
  - checkpoint-overhead
  - failure-recovery
outputs:
  - tokens_per_step
  - samples_per_step
  - microbatches_per_step
  - checkpoint_frequency
  - training_throughput_target
assumptions:
  - global batch、micro batch 和 gradient accumulation 必须分开记录
  - sequence packing 未知时不假设所有样本都达到最大长度
  - checkpoint interval 必须带 steps、tokens 或 wall-clock 单位
related_layers:
  - model
  - workload
  - compute
  - memory
  - parallelism
  - communication
  - topology
  - storage
  - reliability
  - accelerator
evidence: {}
updated: 2026-09-25
tags:
  - system
  - workload
  - training
---
# Training Workload

> Training Workload 定义一次训练 job 如何消费模型、样本和集群资源。它把 global batch、micro batch、gradient accumulation、sequence packing、token budget 与 checkpoint cadence 显式化。

## 为什么只写 Batch 不够

训练里至少有：

- global batch
- data-parallel replica batch
- micro batch
- gradient accumulation steps
- packed token count

它们影响：

- activation memory
- optimizer / gradient sync cadence
- step time
- communication
- throughput

所以一个 `batch_size=1024` 如果没有 scope，几乎无法用于系统建模。

## Global / Micro Batch

在均匀 Data Parallel、每 replica 每 accumulation step 使用相同 micro batch 的简单条件下：

```text
global_batch
=
micro_batch_per_replica
× gradient_accumulation_steps
× data_parallel_replicas
```

这只是常见规则。

若存在：

- uneven batch
- expert/data hybrid placement
- pipeline schedule
- sequence packing by tokens
- dropped samples

必须按真实 schedule 重新计算。

## Tokens per Step

若每 sample 有固定 `S` token：

```text
tokens_per_step
= global_batch × S
```

但真实 LLM training 常有 variable-length 和 packing，因此更可靠的是直接记录：

```text
non_padding_tokens_per_step
```

以及：

```text
allocated_tokens_per_step
```

两者差异反映 padding / packing efficiency。

## Sequence Packing

Packing 会影响：

- useful tokens / allocated tokens
- attention masks
- activation memory
- FLOPs
- throughput

因此 throughput 报告应说明是：

- useful tokens/s
- padded/allocated tokens/s

否则不同 packing efficiency 的 run 不能直接比较。

## Gradient Accumulation

Gradient accumulation 让多个 microbatch 在一次 optimizer update 前依次执行。

```text
microbatches_per_optimizer_step
= gradient_accumulation_steps
```

它可以用较小 micro batch 控制 activation peak，但会改变：

- optimizer update cadence
- communication schedule
- step latency
- overlap opportunities

## Training Token Budget

训练规模最好记录：

```text
target_training_tokens
```

而不是只记录 epochs，因为大规模混合数据集的“epoch”可能没有稳定物理意义。

若每 optimizer step 的 useful token 数已知：

```text
optimizer_steps
≈ target_training_tokens / useful_tokens_per_step
```

这只是规划关系，数据重采样和动态长度会产生偏差。

## Throughput

训练 throughput 至少区分：

- useful tokens/s
- samples/s
- optimizer steps/s

只写“tokens/s”时必须说明是否包含 padding token。

## Step Time

一个训练 step 可能包含：

```text
forward
+ backward
+ gradient communication
+ optimizer
+ checkpoint / logging amortization
```

部分阶段可以 overlap，因此不能简单用各峰值时间机械相加。

## Checkpoint Interval

Checkpoint interval 必须带单位：

- every N optimizer steps
- every N tokens
- every N minutes

它影响：

- storage bandwidth
- pause time
- failure recovery point
- expected lost work

后续 `REL-001` 建立 checkpoint/recovery 模型。

## Memory 输入

Training Workload 为 [[system/memory/activation-memory|Activation Memory Model]] 提供：

- micro batch
- sequence
- packing
- accumulation/schedule

而完整 training memory 还需要 weights、gradients、optimizer states。

## Parallelism

Training Workload 与 [[system/parallelism/parallelism-overview|Parallelism Overview]] 联合决定：

- DP replica count
- TP / PP / EP / CP groups
- per-rank batch
- communication cadence
- placement

不能从 global batch 单独推出 GPU 数。

## Failure / Recovery

大规模训练需要把 job duration 与 failure exposure 联合考虑。

需要记录：

- checkpoint cadence
- restart scope
- reproducibility / replay requirement
- maximum acceptable lost work

这些不是模型固有事实。

## 输出

- `tokens_per_step`
- `samples_per_step`
- `microbatches_per_step`
- `checkpoint_frequency`
- `training_throughput_target`

所有输出应明确 useful vs allocated tokens、batch scope 和 step definition。

## 边界

1. 本页不记录某个 training framework 的项目能力。
2. 不使用“典型 batch”补未知 workload。
3. Global batch 不是单设备 memory 输入，micro batch 才更直接影响 activation。
4. Training throughput 必须绑定 model + precision + sequence + parallelism + hardware。

## 直接来源

本页定义仓库内部 training workload 语义与量纲关系，没有引入特定训练 run 或 benchmark 数值，因此 `evidence: {}`。
