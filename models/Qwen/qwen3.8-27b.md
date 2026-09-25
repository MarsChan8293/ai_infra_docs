---
schema_version: model-v0.2
name: Qwen3.8-27B
object_type: model
organization: Qwen
family: Qwen3.8
status: released
release_date: 2026-08-14
architecture:
  backbone: decoder-only
  sparsity: dense
  attention: hybrid-linear-gated-attention
parameters:
  total: 27000000000
  active: 27000000000
structure:
  num_layers: 64
  hidden_size: null
  intermediate_size: null
  attention:
    num_attention_heads: 24
    num_key_value_heads: 4
    head_dim: 256
    growing_layers: 16
    kv_lora_rank: null
    qk_rope_head_dim: null
    sliding_window: null
  moe: null
  recurrent:
    type: gated-deltanet
    layers: 48
    state_size: null
context_length: 262144
kv_cache_64k_fp8_bytes: 2147483648
modalities:
  - text
  - image
  - video
weights: https://huggingface.co/Qwen/Qwen3.8-27B
snapshot:
  revision: null
  as_of: 2026-09-16
updated: 2026-09-16
---

# Qwen3.8-27B

> Qwen3.8 的 27B dense 原生多模态模型，以 Gated DeltaNet + Gated Attention 混合结构在中等模型规模下支持长上下文。

## 核心规格

| 项目 | 值 | Evidence |
|---|---:|---|
| 总参数 | 27B | [S1][S2] |
| 激活参数 | 27B | [S2] |
| 原生最大上下文 | 262,144 tokens | [S2] |
| 模态 | Text + Image + Video | [S2] |
| 64K FP8 KV footprint | 2,147,483,648 bytes（2 GiB） | [S2] |

## 架构特征

| 特征 | 说明 | Evidence |
|---|---|---|
| Layers | 64 层，16 组，每组 3 个 Gated DeltaNet + 1 个 Gated Attention | [S2] |
| Growing attention layers | 16 个 Gated Attention 层 | [S2] |
| Gated Attention | 24 Q heads、4 KV heads、head_dim=256 | [S2] |
| Sparsity | Dense | [S2] |
| Multimodal | 原生支持图像与视频输入 | [S2] |

## AI Infra 关注点

- 16 个 Gated Attention 层产生增长型 KV，Gated DeltaNet 的固定状态不计入本字段。[S2]
- 64K FP8 KV 计算为 `65536 × 16 × 2 × 4 × 256 = 2,147,483,648 bytes`。[S2]
- **分析判断：**与 2.4T MoE 版本相比，27B dense 更适合用来观察混合注意力本身对长上下文状态的影响，而不会被超大规模 EP 通信完全淹没。

## 版本与边界

- 该模型于 2026-08-14 发布。[S1]
- `context_length` 记录官方权重原生 262K，而不是扩展后的约 1M。[S2]

## 关联软件与系统

- 推理引擎：[vLLM](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/vllm-project/vLLM/vLLM.md)、[SGLang](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/sgl-project/SGLang/SGLang.md)
- Kernel：[FlashInfer](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/flashinfer-ai/FlashInfer/FlashInfer.md)
- KV：[LMCache](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/LMCache/LMCache/LMCache.md)

## 直接来源

- [S1] https://github.com/QwenLM/Qwen3.8/blob/main/README.md
- [S2] https://huggingface.co/Qwen/Qwen3.8-27B
