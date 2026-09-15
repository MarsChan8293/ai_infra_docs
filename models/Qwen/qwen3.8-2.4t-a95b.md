---
schema_version: model-v0.1
name: Qwen3.8-2.4T-A95B
object_type: model
organization: Qwen
family: Qwen3.8
status: released
release_date: 2026-08-12
architecture:
  backbone: decoder-only
  sparsity: moe
  attention: hybrid-linear-gated-attention
parameters:
  total: 2400000000000
  active: 95000000000
context_length: 262144
kv_cache_64k_fp8_bytes: 3087007744
modalities:
  - text
weights: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
snapshot:
  revision: null
  as_of: 2026-09-16
updated: 2026-09-16
---

# Qwen3.8-2.4T-A95B

> Qwen3.8 的超大规模 MoE 文本模型，2.4T 总参数、95B 激活参数，并以 Gated DeltaNet + Gated Attention 混合结构降低长上下文 KV 增长。

## 核心规格

| 项目 | 值 | Evidence |
|---|---:|---|
| 总参数 | 2.4T | [S1][S2] |
| 激活参数 | 95B | [S1][S2] |
| 原生最大上下文 | 262,144 tokens | [S2] |
| 模态 | Text | [S2] |
| 64K FP8 KV footprint | 3,087,007,744 bytes（2.875 GiB） | [S2] |

## 架构特征

| 特征 | 说明 | Evidence |
|---|---|---|
| Layers | 92 层，23 组，每组 3 个 Gated DeltaNet + 1 个 Gated Attention | [S2] |
| Growing attention layers | 23 个 Gated Attention 层 | [S2] |
| Gated Attention | 64 Q heads、4 KV heads、head_dim=256 | [S2] |
| MoE | 512 experts，10 routed experts/token + 1 shared expert | [S2] |
| Context extension | 原生 262K，可通过官方长上下文方案扩展到约 1M | [S2] |

## AI Infra 关注点

- 只有 23 个 Gated Attention 层产生随序列线性增长的标准 KV；Gated DeltaNet 的固定状态不计入该派生指标。[S2]
- 64K FP8 KV 计算为 `65536 × 23 × 2 × 4 × 256 = 3,087,007,744 bytes`。[S2]
- **分析判断：**虽然 KV 增长被混合注意力压缩，但 2.4T 总权重与 95B 激活规模会把系统瓶颈更多推向专家并行、权重驻留和跨卡通信。

## 版本与边界

- 该模型于 2026-08-12 作为 Qwen3.8 首批主要模型发布。[S1]
- `context_length` 记录原生 262,144，而不是扩展后的约 1M，避免把运行时扩展方案当成模型原生配置。[S2]

## 关联项目

- 推理引擎：[[software/projects/vllm|vLLM]]、[[software/projects/sglang|SGLang]]
- 通信：[[software/projects/deepep|DeepEP]]、[[software/projects/nccl|NCCL]]
- 异构推理：[[software/concepts/heterogeneous-inference|异构推理]]

## 直接来源

- [S1] https://github.com/QwenLM/Qwen3.8/blob/main/README.md
- [S2] https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
