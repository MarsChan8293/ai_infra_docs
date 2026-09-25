---
schema_version: system-v0.1
name: Transformer Compute Model
object_type: concept
category: compute-model
inputs:
  - model.parameters
  - model.architecture
  - model.attention
  - model.experts
  - workload.prompt_tokens
  - workload.output_tokens
  - workload.batch_size
  - workload.sequence_length
  - workload.parallelism
  - execution.precision
constraints:
  - compute-throughput
  - memory-bandwidth
  - kernel-efficiency
  - shape-efficiency
  - synchronization
outputs:
  - linear_flops
  - attention_flops
  - moe_active_flops
  - prefill_flops
  - decode_flops_per_token
  - compute_time_lower_bound
assumptions:
  - 仓库 FLOP 口径默认一次乘法和一次加法合计为 2 FLOPs
  - 任何 2P/token 近似都必须注明它只近似参数化线性层计算，不等于完整 Transformer FLOPs
  - 并行切分改变 per-device work 与通信，不自动改变全局数学 FLOPs
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
tags:
  - system
  - compute
  - transformer
---
# Transformer Compute Model

> Transformer 的“算力需求”不能只用参数量乘一个常数概括。参数化线性层、attention 的序列长度项、MoE active experts、batch / shape，以及 Prefill 与 Decode 的执行形态都必须分开。

## FLOP 计数约定

本仓库 System 推导默认采用：

```text
1 multiply = 1 FLOP
1 add      = 1 FLOP
1 FMA      = 2 FLOPs
```

因此标准矩阵乘：

```text
[M × K] @ [K × N]
```

其主要乘加计算量近似：

```text
F_gemm ≈ 2 × M × K × N
```

这是仓库内部统一计数 convention。引用厂商 TFLOPS、论文或 benchmark 时必须确认对方口径，不能把不同 FLOP 定义直接比较。

## 输入

Compute Model 消费：

- 模型参数与架构事实；
- [[system/workload/ai-workload-model|Workload]] 的实际 token、batch 与 sequence；
- 执行精度；
- 并行切分信息。

如果 layer count、hidden size、head 数、expert 结构等模型事实未知，精确 FLOP 也应保持未知，不能用相邻模型结构补齐。

## 参数化线性层

对于一个权重矩阵 `W[K,N]`，一次处理 `M` 个 token row：

```text
F_linear ≈ 2 × M × K × N
```

若把某一前向阶段所有实际参与计算的参数化线性层权重元素数记为 `P_linear_active`，并且每个 token 对这些权重各执行一次标准乘加，则可以写成近似：

```text
F_linear_per_token
≈ 2 × P_linear_active
```

这就是常见 `2P/token` 直觉的来源，但它有明确边界。

### 2P/token 不包括什么

它不是完整 Transformer FLOP 公式，至少不能自动覆盖：

- attention 中 QKᵀ 与 AV 的序列长度相关计算；
- softmax / normalization；
- rotary / positional operations；
- routing / top-k；
- activation function；
- embedding lookup；
- sampling；
- layout conversion；
- communication；
- runtime / allocator 开销。

因此本仓库禁止把 `2 × total_parameters × tokens` 无条件标成“完整推理 FLOPs”。

## Dense Transformer

对于 Dense 模型：

```text
P_linear_active
≈ 当前前向实际使用的参数化线性层权重元素
```

如果所有 decoder layer 的主要线性权重都参与每 token 前向，`P_linear_active` 会接近模型的大部分参数量，但 embedding、norm、未参与 matmul 的参数以及权重共享都会让二者不完全相等。

所以只有在明确注明“参数化线性层近似”时，才可以从 total parameter count 建立 lower-fidelity 估算。

## Attention Compute

Self-Attention 至少拆成：

1. Q / K / V projection；
2. QKᵀ；
3. softmax / masking；
4. attention probability × V；
5. output projection。

Projection 属于参数化线性层，可进入前面的 linear FLOPs。

对 full dense attention，若：

- batch = `B`
- query heads = `H`
- head dimension = `D`
- query length = `S_q`
- key/value length = `S_k`

则 QKᵀ 的主要乘加：

```text
F_QK
≈ 2 × B × H × S_q × S_k × D
```

AV 的主要乘加同阶：

```text
F_AV
≈ 2 × B × H × S_q × S_k × D
```

因此两项合计：

```text
F_attention_matmul
≈ 4 × B × H × S_q × S_k × D
```

这个公式是 dense pairwise attention 的矩阵乘 baseline。Causal triangular 计算、FlashAttention、local/sliding-window、sparse attention、MLA、linear attention 等都会改变实际 work 或数据移动，必须单独注明。

## Prefill

对于长度为 `S` 的 prompt，在最简单 full self-attention baseline 下：

```text
S_q = S
S_k = S
```

因此 attention pairwise work 随：

```text
O(S²)
```

增长。

与此同时，线性层通常按 token 数近似线性增长：

```text
F_linear_prefill
≈ S × F_linear_per_token
```

所以长上下文下不能只用 `2P × S` 忽略 attention 的序列平方项。

## Decode

自回归 Decode 每一步通常新增少量 query token，并读取已有上下文状态。若一次每序列生成 1 token，已有 KV 长度记为 `L`：

```text
S_q ≈ 1
S_k ≈ L
```

dense attention matmul baseline 约为：

```text
F_attention_decode_step
≈ 4 × B × H × L × D
```

因此单步 attention 计算随已有上下文长度近似线性增长。

但 Decode 的系统瓶颈不能只从 FLOPs 判断。小 batch / 小 M 的线性层可能具有较低算术强度，并受到权重与 KV 数据移动影响；这一点由后续 `CMP-002` Roofline 和 `CMP-003` Prefill vs Decode 进一步判断。

## MoE

MoE 必须区分：

- total parameters；
- 每 token active parameters；
- shared experts；
- routed experts；
- router；
- top-k；
- expert imbalance。

对于 expert MLP 的粗粒度参数化线性层近似，应使用 **实际 active expert weights**：

```text
F_moe_linear_per_token
≈ 2 × P_active_expert_linear
```

而不是：

```text
2 × total_model_parameters
```

如果有 shared experts，它们应与 routed active experts 分开计数再合并。

同时 MoE 的系统成本还包括 token dispatch / combine 和 All-to-All；这些属于 [[system/communication/README|Communication]] 与后续 Expert Parallelism，而不是 FLOPs 本身。

## GQA / MQA / MLA 等结构

不同 attention 结构会同时改变：

- K/V projection work；
- KV Cache 大小；
- attention cache layout；
- 数据读取；
- 部分实现的 kernel shape。

不能因为两个模型 total parameters 接近，就假定其 attention FLOPs 和 memory traffic 相同。

本页只提供统一骨架；精确模型计算需要 Model Schema 提供足够架构字段。

## Batch 与 Shape Efficiency

数学 FLOPs 相同不代表执行时间相同。

例如同样的总 token 数：

```text
M = 1
```

与：

```text
M = 128
```

会形成完全不同的 GEMM shape、并行度和硬件利用率。

因此必须区分：

```text
required mathematical FLOPs
≠ achieved hardware FLOP/s
```

后者受 batch、矩阵形状、dtype、kernel、memory bandwidth、同步和硬件架构影响。

## 并行切分

TP / PP / EP / DP 等并行策略主要改变：

- 每设备承担的 FLOPs；
- 每设备驻留的状态；
- collective / P2P 通信；
- bubble / synchronization；
- shape efficiency。

它们通常不改变模型前向的全局数学定义本身。

因此应该先计算：

```text
global mathematical work
```

再根据 [[system/parallelism/README|Parallelism Model]] 映射成 per-device work 和通信，而不是简单用“总 FLOPs ÷ 卡数”代表端到端执行时间。

## Compute Time Lower Bound

若某阶段需要的数学计算量为：

```text
F_required
```

设备在对应 dtype / operation / shape 下的**有效**计算吞吐为：

```text
R_effective FLOP/s
```

则纯计算时间下界：

```text
T_compute
>= F_required / R_effective
```

如果只有厂商 peak throughput `R_peak`，则：

```text
F_required / R_peak
```

最多只能视为非常乐观的理论下界，不能称为预期 latency。

实际时间还可能受：

- HBM bandwidth；
- KV traffic；
- collective；
- launch / scheduling；
- load imbalance；
- pipeline bubble；
- queueing

限制。

## Training

训练不能简单把 inference FLOPs 乘一个全仓固定倍数。

Backward 需要计算 activation gradient、weight gradient，并受到：

- activation checkpointing / recomputation；
- optimizer；
- sequence packing；
- parallel strategy；
- frozen parameters；
- MoE routing

影响。

训练 Compute Model 后续应与 `TRN-001` 单独展开。本页暂时只规定通用 forward 计算骨架。

## 输出

Compute Model 输出至少包括：

- `linear_flops`
- `attention_flops`
- `moe_active_flops`
- `prefill_flops`
- `decode_flops_per_token`
- `compute_time_lower_bound`

任何数值输出都必须附带：

```text
FLOP convention
+ model inputs
+ workload inputs
+ precision
+ scope
+ assumptions
```

## 与其他层的关系

- Workload：[[system/workload/ai-workload-model|AI Workload Model]]
- Memory Accounting：[[system/memory/model-memory-accounting|Model Memory Accounting]]
- Memory：[[system/memory/README|Memory Model]]
- Parallelism：[[system/parallelism/README|Parallelism Model]]
- Communication：[[system/communication/README|Communication Model]]
- Hardware：[[chip/00-project-index|AI 芯片与基础设施资料库]]
- Schema：[[system/SCHEMA|System Schema V0.1]]

## 直接来源

本页定义仓库内部统一的 FLOP convention、矩阵乘计数和 Transformer compute 分解，没有引入具体厂商峰值、benchmark 或模型私有规格，因此 `evidence: {}`。后续使用具体模型配置或硬件峰值时必须链接直接 Evidence。
