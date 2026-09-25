---
schema_version: system-v0.1
name: Training Memory Model
object_type: concept
category: training
inputs:
  - memory.weights
  - training.trainable_parameters
  - training.gradient_precision
  - training.optimizer_state
  - memory.activations
  - parallelism
constraints:
  - device-memory
  - optimizer-state
  - gradient-memory
  - activation-memory
  - communication-buffer
outputs:
  - gradient_bytes
  - optimizer_state_bytes
  - master_weight_bytes
  - saved_activation_bytes
  - training_peak_device_bytes
assumptions:
  - optimizer state bytes 必须由具体 optimizer/state precision 定义，不使用全仓固定倍数
  - global state 与 per-device resident state 分开
related_layers:
  - model
  - workload
  - compute
  - memory
  - parallelism
  - communication
  - accelerator
evidence: {}
updated: 2026-09-25
tags: [system, training, memory]
---
# Training Memory Model

> 训练显存不是简单的“模型权重乘一个经验倍数”。每项状态都应从元素数量、精度、复制/分片和生命周期分别记账。

## 统一骨架

单设备峰值：

```text
training_peak_device_bytes
=
resident_weights
+ resident_gradients
+ resident_optimizer_states
+ resident_master_weights
+ saved_activations
+ workspace
+ communication_buffers
+ allocator/runtime reserve
```

所有项必须是同一 device 和同一 peak window。

## Gradients

若有 P_trainable 个本 rank resident trainable parameters，gradient 每元素 b_grad bytes：

```text
gradient_bytes
≈ P_trainable_local × b_grad
```

若 gradient sharded/replicated，按真实规则调整。

## Optimizer State

不要写统一“optimizer = 8 bytes/param”之类全仓规则。

应显式列：

```text
state_1 elements × bytes
+ state_2 elements × bytes
+ ...
```

具体 optimizer 是否有 momentum、variance、master state 由 scenario 或 Evidence 决定。

## Master Weights

混合精度训练可能存在额外 master weights，也可能不存在。

所以：

```text
master_weight_bytes = unknown
```

优于无证据时强行套倍数。

## Activations

Saved activation 来自 [[system/memory/activation-memory|Activation Memory Model]]。

Recomputation 会交换：

```text
saved activation memory ↓
compute ↑
```

必须把策略显式写入 workload。

## Parallelism

不同维度影响不同状态：

- TP/PP：切模型与 activation
- DP：可能复制或分片 optimizer/gradients
- EP：分布 expert weights
- CP：分布 sequence-dependent state

因此 per-device memory 必须经过实际 parallel layout，而不是总状态除 world size。

## Communication Buffers

Gradient bucket、Reduce-Scatter/All-Gather staging 也可能贡献峰值。

通信 payload 与 resident buffer lifecycle 不是同一概念，需要分别记录。

## 输出

- `gradient_bytes`
- `optimizer_state_bytes`
- `master_weight_bytes`
- `saved_activation_bytes`
- `training_peak_device_bytes`

## 直接来源

本页定义训练状态逐项记账方法，不绑定具体 optimizer 或 framework，因此 `evidence: {}`。
