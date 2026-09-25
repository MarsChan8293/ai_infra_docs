---
schema_version: system-v0.1
name: Roofline 与 Arithmetic Intensity
object_type: concept
category: compute-model
inputs:
  - compute.required_flops
  - memory.required_bytes
  - hardware.compute.peak_flops
  - hardware.memory.peak_bandwidth
  - execution.effective_compute
  - execution.effective_bandwidth
constraints:
  - compute-throughput
  - memory-bandwidth
  - arithmetic-intensity
  - kernel-efficiency
outputs:
  - arithmetic_intensity_flops_per_byte
  - ridge_point_flops_per_byte
  - compute_time_lower_bound
  - memory_time_lower_bound
  - roofline_throughput_ceiling
  - bottleneck_class
assumptions:
  - FLOPs 与 bytes 必须描述同一执行范围
  - Peak Roofline 只提供理论上界，不代表真实 kernel 或端到端性能
related_layers:
  - workload
  - compute
  - memory
  - accelerator
evidence: {}
updated: 2026-09-25
tags:
  - system
  - compute
  - roofline
---
# Roofline 与 Arithmetic Intensity

> Roofline 把“需要多少计算”和“需要搬多少数据”放进同一个量纲框架，从而判断某个执行范围更可能受 compute throughput 还是 memory bandwidth 约束。

## Arithmetic Intensity

对于同一执行范围：

```text
AI
= required_FLOPs / required_memory_bytes
```

单位：

```text
FLOP / byte
```

这里的 bytes 必须是相关 memory tier 上实际发生的数据移动，而不是 tensor 的逻辑大小总和。

因此：

```text
Arithmetic Intensity
!= FLOPs / resident capacity
```

## Peak Roofline

假设硬件对应精度的峰值计算能力是：

```text
P_peak [FLOP/s]
```

目标 memory tier 峰值带宽：

```text
B_peak [byte/s]
```

则理想 Roofline：

```text
P_roof
= min(
    P_peak,
    AI × B_peak
  )
```

这是理论吞吐上界。

## Ridge Point

Compute roof 与 bandwidth roof 相交的 Arithmetic Intensity：

```text
AI_ridge
= P_peak / B_peak
```

若：

```text
AI < AI_ridge
```

在 peak Roofline 模型中更偏 memory-bandwidth-bound。

若：

```text
AI > AI_ridge
```

则更偏 compute-bound。

注意这是模型分类，不是实测诊断。

## 时间下界形式

与其只画 roof，也可以直接比较时间：

```text
T_compute_peak
= FLOPs / P_peak

T_memory_peak
= bytes / B_peak

T_roofline_lower_bound
>= max(T_compute_peak, T_memory_peak)
```

如果使用有效 compute / bandwidth：

```text
T_compute_effective
= FLOPs / P_effective

T_memory_effective
= bytes / B_effective
```

则能得到更接近特定 kernel 的系统上界，但仍未包含通信、同步、queueing 等端到端成本。

## 四种性能层级

仓库中必须区分以下四层：

### 1. Vendor Peak

厂商规格表中的：

- peak FLOP/s；
- peak memory bandwidth。

它们是硬件能力事实，不是 workload 性能。

### 2. Peak Roofline

使用 vendor peak 和 workload AI 得到：

```text
min(P_peak, AI × B_peak)
```

这是理论上界。

### 3. Effective System Ceiling

把真实或假设的：

- effective compute；
- effective memory bandwidth；
- shape efficiency；
- implementation constraints

带入后得到更现实的上界。

它仍然不是 benchmark。

### 4. Measured Performance

在明确：

```text
model
+ workload
+ software
+ hardware
+ topology
+ version
```

条件下实测得到的性能。

这四类数字禁止在表格里混成同一“性能”列。

## Prefill 与 Decode

同一模型在 Prefill 和 Decode 的 AI 往往不同。

### Prefill

大量 token 同时参与较大的 GEMM，权重读取可能被更多 token 复用，Arithmetic Intensity 往往有机会提高。

### Decode

小 batch / 单 token step 中，权重和 KV 的 bytes/token 可能更高，使 Arithmetic Intensity 降低。

但不能把“Prefill = compute-bound，Decode = memory-bound”写成无条件定律。batch、架构、量化、KV layout、硬件和 kernel 都会改变结果。

具体分解由后续 `CMP-003` 处理。

## MoE

MoE 的 Arithmetic Intensity 必须使用实际 active work 与实际 memory traffic。

不能使用：

```text
total_model_parameters
```

直接估计单 token FLOPs，也不能假定所有 experts 的权重每 token 都读取。

同时 EP 通信可能成为 HBM Roofline 之外的第三个瓶颈，所以 MoE 不能只靠二维 compute-memory Roofline 完成系统判断。

## 多级 Memory Roofline

如果一个 workload 同时受：

- HBM；
- Host DRAM；
- CXL / remote memory；
- NVMe

约束，可以分别建立：

```text
AI_i = FLOPs / bytes_on_tier_i
P_i  = AI_i × B_i
```

然后比较不同 tier 的 ceiling。

不要把多层带宽求和成一个虚构的统一 memory bandwidth。

## Communication Roof

分布式 workload 还存在 network / fabric ceiling：

```text
T_comm_lower_bound
```

此时更完整的端到端下界接近：

```text
T_step
>= max(
  T_compute,
  T_memory,
  T_communication
)
```

前提是三者可重叠；若 dependency 要求串行，还需按 critical path 相加。

通信时间统一由 [[system/communication/communication-cost-model|Communication Cost Model]] 建模。

## Batch 如何移动 Roofline

如果一次权重读取可以服务更多 token，增加 batch 会提高：

```text
FLOPs / weight_bytes
```

即提高部分算子的 Arithmetic Intensity。

但更大的 batch 也会改变：

- KV/activation traffic；
- shape；
- latency；
- queueing；
- memory capacity。

因此 batch 对 Roofline 的影响必须重新计算 bytes 与 FLOPs，而不是直接套一个比例。

## 典型错误

禁止以下写法：

```text
hardware peak FLOPS / model FLOPs
= real tokens/s
```

也禁止：

```text
HBM TB/s / model size
= guaranteed decode tokens/s
```

它们最多可以在明确 assumptions 下形成理论 ceiling，还必须检查 attention、KV、activation、通信和 runtime overhead。

## 输出

- `arithmetic_intensity_flops_per_byte`
- `ridge_point_flops_per_byte`
- `compute_time_lower_bound`
- `memory_time_lower_bound`
- `roofline_throughput_ceiling`
- `bottleneck_class`

任何 `bottleneck_class` 都必须说明它属于 peak、effective 还是 measured 层级。

## 与其他层的关系

- Compute：[[system/compute/transformer-compute-model|Transformer Compute Model]]
- Memory Bandwidth：[[system/memory/memory-bandwidth-model|Memory Bandwidth Model]]
- Communication：[[system/communication/communication-cost-model|Communication Cost Model]]
- Workload：[[system/workload/ai-workload-model|AI Workload Model]]
- Hardware：[[chip/00-project-index|AI 芯片与基础设施资料库]]
- Schema：[[system/SCHEMA|System Schema V0.1]]

## 直接来源

本页定义仓库内部 Roofline 量纲、分类和理论下界，不引入具体硬件或 benchmark 数值，因此 `evidence: {}`。
