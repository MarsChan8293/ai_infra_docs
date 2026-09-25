---
schema_version: model-v0.1
name: Qwen3.8-Flash-Next
object_type: model
organization: Qwen
family: Qwen3.8
status: released
release_date: 2026-08-26
architecture:
  backbone: decoder-only
  sparsity: moe
  attention: hybrid-linear-sparse-attention
parameters:
  total: 180000000000
  active: 6000000000
context_length: 262144
kv_cache_64k_fp8_bytes: 805306368
modalities:
  - text
  - image
  - video
weights: https://huggingface.co/Qwen/Qwen3.8-Flash-Next
snapshot:
  revision: null
  as_of: 2026-09-16
updated: 2026-09-16
---

# Qwen3.8-Flash-Next

> Qwen3.8 的 Flash 架构预览模型，以 125B/6B-active MoE core、Gated DeltaNet 与 Qwen Sparse Attention 探索下一代长上下文高效推理路线。

## 核心规格

| 项目 | 值 | Evidence |
|---|---:|---|
| 参数总量 | 约 180B：125B core + 51B n-gram embedding + 4B MTP | [S1][S2] |
| 激活参数 | 6B（官方对 core model 的口径） | [S2] |
| 原生最大上下文 | 262,144 tokens | [S2] |
| 模态 | Text + Image + Video | [S2] |
| 64K FP8 KV footprint | 805,306,368 bytes（768 MiB） | [S2] |

## 架构特征

| 特征 | 说明 | Evidence |
|---|---|---|
| Layers | 48 层，12 组，每组 3 个 Gated DeltaNet + 1 个 Qwen Sparse Attention | [S2] |
| Growing attention layers | 12 个 sparse-attention 层 | [S2] |
| Sparse Attention | 24 Q heads、2 KV heads、head_dim=256，另有独立 indexer | [S2] |
| MoE | 512 experts，10 routed + 1 shared | [S2] |
| Architecture preview | 官方将其描述为面向下一代 Qwen 架构的 early preview | [S1] |

## AI Infra 关注点

- 只计算 12 个 sparse-attention 层的 K/V cache，不计 Gated DeltaNet 固定状态与 sparse indexer 的辅助 key/cache。[S2]
- 64K FP8 KV 为 `65536 × 12 × 2 × 2 × 256 = 805,306,368 bytes`。[S2]
- **分析判断：**Flash-Next 的意义在于同时压缩“有多少层需要增长型 KV”和“每个增长层的 KV heads”，因此长上下文状态压力明显低于同代 27B dense。

## 版本与边界

- 该模型于 2026-08-26 发布。[S1]
- `parameters.total=180B` 是对官方明确列出的 125B core、51B n-gram embedding、4B MTP 三部分求和的派生值，不应和“core 125B”混写。[S2]
- `parameters.active=6B` 采用官方 core-model 激活口径，不代表 n-gram/MTP 的逐 token 完整运行成本。

## 关联项目

- 推理引擎：[vLLM](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/vllm-project/vLLM/vLLM.md)、[SGLang](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/sgl-project/SGLang/SGLang.md)
- Kernel：[FlashInfer](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/flashinfer-ai/FlashInfer/FlashInfer.md)、[Triton](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/triton-lang/Triton/Triton.md)
- KV：[LMCache](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/LMCache/LMCache/LMCache.md)、[Mooncake](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/kvcache-ai/Mooncake/Mooncake.md)

## 直接来源

- [S1] https://github.com/QwenLM/Qwen3.8-Flash-Next/blob/main/README.md
- [S2] https://huggingface.co/Qwen/Qwen3.8-Flash-Next
