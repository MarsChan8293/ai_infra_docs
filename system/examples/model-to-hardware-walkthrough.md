---
title: Qwen3.8-27B → MI300X 单卡 Decode Walkthrough
aliases:
  - Model to Hardware Walkthrough
tags:
  - system
  - example
  - integration
  - qwen
  - mi300x
updated: 2026-09-25
---

# Qwen3.8-27B → MI300X 单卡 Decode Walkthrough

> 这是方法演示，不是硬件推荐或性能预测。目标是把仓库事实、显式 workload 假设和 System 公式串成可审计链，并在证据不足时停止推导。

## 场景

- Model：[[models/Qwen/qwen3.8-27b|Qwen3.8-27B]]
- Hardware：[[chip/AMD/mi300x|AMD Instinct MI300X]]
- Workload：单 accelerator、batch=1、已有 65,536 token 上下文、生成 1 个 Decode token。
- 场景假设：weight payload 按 2 bytes/parameter 计算。
- Traffic 假设：每个 Decode step 从 HBM 读取一次完整 weight payload 和一次完整 64K growing KV payload。
- Activation、workspace、allocator overhead、runtime reserve 保持 unknown，不按 0 处理。

2 bytes/parameter 和完整读取假设都不是官方权重格式或具体 runtime 行为的事实。

## 可验证事实输入

来自 [[models/Qwen/qwen3.8-27b|Qwen3.8-27B]]：

| 字段 | 值 | 来源 |
|---|---:|---|
| total parameters | 27,000,000,000 | Model page `[S1][S2]` |
| active parameters | 27,000,000,000 | Model page `[S2]` |
| native context limit | 262,144 tokens | Model page `[S2]` |
| 64K FP8 growing KV | 2,147,483,648 bytes | Model page `[S2]` |
| growing attention layers | 16 | Model page `[S2]` |

来自 [[chip/AMD/mi300x|AMD Instinct MI300X]]：

| 字段 | 值 | 来源 |
|---|---:|---|
| HBM capacity | 192 GB | `memory.capacity_gb` → `S1` |
| HBM peak bandwidth | 5.3 TB/s | `memory.bandwidth_tb_s` → `S1` |
| compute throughput | unknown | 当前 canonical page 为 `compute: {}` |

本例不从外部知识补 MI300X FLOP/s。

## Workload 规范化

按 [[system/workload/ai-workload-model|AI Workload Model]]：

```text
kind             = inference
phase            = decode
batch_size       = 1
active_sequences = 1
context_tokens   = 65,536
new_tokens_step  = 1
parallel_degree  = 1
```

64K 在模型原生 262,144 token context limit 内。Request rate、concurrency 和 SLA 未给出，所以不推导 queueing、TTFT 或 TPOT SLA。

## Weight Memory

参数事实：

```text
P = 27,000,000,000
```

场景假设：

```text
bytes_per_parameter = 2
```

因此：

```text
weight_payload_bytes
= 27,000,000,000 × 2
= 54,000,000,000 bytes
= 54.000 GB
```

这是分析输入，不代表官方 checkpoint 一定以 2 bytes/parameter 形式驻留。

## KV Memory

模型页已给出：

```text
kv_bytes_64k_fp8
= 2,147,483,648 bytes
≈ 2.147 GB
= 2 GiB
```

该字段只覆盖 16 个 growing Gated Attention layers 的增长型 KV，不包含固定 DeltaNet state 等其他状态。

## 已知 Device Memory Lower Bound

按 [[system/memory/model-memory-accounting|Model Memory Accounting]]：

```text
known_resident_lower_bound
= weight_payload_bytes + kv_bytes
= 54,000,000,000 + 2,147,483,648
= 56,147,483,648 bytes
≈ 56.147 GB
```

与 192 GB HBM 对比：

```text
known_headroom_before_unknowns
≈ 192.000 - 56.147
≈ 135.853 GB
```

严格结论只能是：已知驻留下界约 56.147 GB，低于 192 GB HBM。完整单卡容量可行性仍未知，因为 activation、workspace、allocator、runtime reserve、固定 recurrent state 和可能的额外 weight layout 均未计入。

这遵循 `unknown != 0`。

## Compute Work

按 [[system/compute/transformer-compute-model|Transformer Compute Model]]，使用低保真 `2P/token` 参数化线性层近似：

```text
linear_FLOPs_per_token
≈ 2 × P
= 54,000,000,000 FLOPs
= 54 GFLOPs/token
```

这不是完整 Decode FLOPs。它没有完整包含 attention、DeltaNet state update、normalization、sampling 等工作，因此只标记为 linear compute approximation。

## HBM Traffic 假设

按 [[system/memory/memory-bandwidth-model|Memory Bandwidth Model]]，在本例显式 traffic 假设下：

```text
assumed_HBM_bytes_per_decode_token
= 54,000,000,000 + 2,147,483,648
= 56,147,483,648 bytes/token
```

这是场景模型，不是实测 traffic。实际 kernel 可能存在 cache/reuse、额外写流量或不同 KV 访问行为。

## Peak HBM 时间下界

MI300X canonical page 记录：

```text
B_peak = 5.3 TB/s = 5.3e12 bytes/s
```

因此：

```text
T_memory_peak
>= 56,147,483,648 / 5.3e12
≈ 0.010594 s
≈ 10.59 ms/token
```

对应 peak-bandwidth-only ceiling：

```text
tokens_per_second_memory_ceiling
<= 5.3e12 / 56,147,483,648
≈ 94.39 tokens/s
```

94.39 tokens/s 不是预测性能。它同时依赖完整 weight+KV 每 step 读取一次和达到 peak HBM bandwidth 两个强假设。

## Arithmetic Intensity

在同一 scope：

```text
F_linear ≈ 54,000,000,000 FLOPs/token
D_HBM    ≈ 56,147,483,648 bytes/token

AI = F / D
   ≈ 0.962 FLOP/byte
```

按 [[system/compute/roofline-and-arithmetic-intensity|Roofline 与 Arithmetic Intensity]]，当前只能得到 AI，不能计算：

```text
AI_ridge = P_peak / B_peak
```

因为 [[chip/AMD/mi300x|MI300X]] 当前 `compute: {}`。因此本例不下结论“compute-bound”或“memory-bound”。

## Communication

按 [[system/parallelism/parallelism-overview|Parallelism Overview]]，本例 `parallel_degree = 1`，没有 TP/PP/EP/CP group。

所以对本案例定义的 critical path：

```text
inter_accelerator_payload_bytes = 0
T_inter_accelerator_comm = 0
```

这个 0 来自 workload topology 定义，不表示 MI300X 没有互联能力。若改为 TP>1，必须重新引入 collective、per-rank payload、拓扑和 [[system/communication/communication-cost-model|Communication Cost Model]]。

## Topology

本例路径只有：

```text
HBM ↔ single MI300X accelerator
```

所以 Scale-up、Scale-out、NIC affinity 和 network bisection 当前都不进入 critical path。见 [[system/topology/scale-up-vs-scale-out|Scale-up vs Scale-out]]。

## 当前结果

| 项目 | 结果 | 类型 |
|---|---:|---|
| 2-byte/param weight payload | 54.000 GB | scenario-derived |
| 64K FP8 growing KV | 2.147 GB / 2 GiB | model-derived |
| known resident lower bound | 56.147 GB | scenario-derived |
| known headroom before unknowns | 约 135.853 GB | scenario-derived |
| linear compute approximation | 54 GFLOPs/token | scenario-derived |
| assumed HBM traffic | 56.147 GB/token | scenario-derived |
| peak HBM time lower bound | 10.59 ms/token | theoretical lower bound |
| peak HBM-only ceiling | 94.39 token/s | theoretical ceiling |
| approximate AI | 0.962 FLOP/byte | scenario-derived |
| inter-accelerator communication | 0 | workload definition |

## 不能回答的问题

当前仍不能严谨回答：

- 真实 tokens/s 或 TPOT；
- 完整单卡 memory feasibility；
- 完整 Decode FLOPs；
- compute-bound 还是 memory-bound；
- 最优 batch；
- TP 扩展效率；
- 与其他 accelerator 的性能比较。

## 反向暴露的仓库缺口

1. MI300X canonical page 缺少机器可读 compute throughput。
2. Model Schema V0.1 尚未机器化 Qwen3.8-27B 的 layers、heads、hidden/FFN、linear-attention state 等字段。
3. `MEM-003` Activation Memory Model 尚未完成。
4. `MEM-004` KV Cache Model 尚未完成。
5. `CMP-003` Prefill vs Decode 尚未完成。
6. 多卡分析仍需要 `PAR-002`、`COM-002`、`TOP-002`。

## 可追溯链

```text
Qwen3.8-27B facts
  + explicit workload/storage assumptions
        ↓
[[system/memory/model-memory-accounting|Memory Accounting]]
[[system/memory/memory-bandwidth-model|Memory Bandwidth]]
[[system/compute/transformer-compute-model|Transformer Compute]]
[[system/compute/roofline-and-arithmetic-intensity|Roofline]]
[[system/parallelism/parallelism-overview|Parallelism]]
[[system/communication/communication-cost-model|Communication Cost]]
[[system/topology/scale-up-vs-scale-out|Topology]]
        ↓
MI300X capacity / bandwidth facts
        ↓
Derived bounds + explicit unknowns
```

每个派生数字都能回到仓库事实、公式或明确 assumption。
