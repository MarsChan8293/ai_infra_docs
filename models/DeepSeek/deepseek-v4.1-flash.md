---
schema_version: model-v0.2
name: DeepSeek V4.1 Flash
object_type: model
organization: DeepSeek
family: DeepSeek V4.1
status: released
release_date: 2026-09-10
architecture:
  backbone: causal-encoder-decoder
  sparsity: moe
  attention: compressed-sparse-attention
parameters:
  total: 552000000000
  active: null
structure:
  num_layers: null
  hidden_size: null
  intermediate_size: null
  attention:
    num_attention_heads: null
    num_key_value_heads: null
    head_dim: null
    growing_layers: 4
    kv_lora_rank: null
    qk_rope_head_dim: null
    sliding_window: 128
  moe:
    num_experts: 384
    experts_per_token: 6
    shared_experts: 1
  recurrent:
    type: null
    layers: null
    state_size: null
context_length: 1048576
kv_cache_64k_fp8_bytes: 83886080
modalities:
  - text
  - image
weights: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
snapshot:
  revision: null
  as_of: 2026-09-16
updated: 2026-09-16
---

# DeepSeek V4.1 Flash

> DeepSeek 2026-09-10 发布的 552B MoE 原生多模态模型，采用非对称 Causal Encoder-Decoder 与压缩稀疏上下文状态。

## 核心规格

| 项目 | 值 | Evidence |
|---|---:|---|
| 总参数 | 552B | [S1] |
| 激活参数 | 输入约 8B；输出约 16B，非单一标量 | [S1] |
| 原生最大上下文 | 1,048,576 tokens | [S2] |
| 模态 | Text + Image | [S1] |
| 64K FP8 KV footprint | 83,886,080 bytes（80 MiB） | [S3][S4] |

## 架构特征

| 特征 | 说明 | Evidence |
|---|---|---|
| Backbone | Causal Encoder-Decoder，输入/输出计算非对称 | [S1] |
| MoE | 384 routed experts，每 token 选择 6 个，另有 shared expert | [S2] |
| Context | 全层 128-token sliding window，并由少数 source layer 产生压缩 global KV | [S3] |
| Global KV source | layer 2/8/14/20；前三个 2:1 压缩，layer 20 为 1:1 | [S3] |
| Global KV latent width | `head_dim=512` | [S3][S4] |

## AI Infra 关注点

- 该模型的长序列 global KV 不是传统“每层 K+V”结构，而是由 4 个 source layer 共享压缩 latent。[S3][S4]
- `kv_cache_64k_fp8_bytes` 只计算随序列增长的 global compressed KV：`65536 × 512 × (1/2 + 1/2 + 1/2 + 1) = 83,886,080 bytes`。[S3][S4]
- 该指标不包含 128-token fixed sliding-window local cache、sparse index key、candidate index 和量化 metadata。
- **分析判断：**这种 cache 结构会显著改变 P/D 分离、KV 迁移与外部 KV Store 的网络/存储压力模型，不应拿传统 GQA 的逐层 KV 公式直接估算。

## 版本与边界

- 页面绑定 2026-09-10 发布的 DeepSeek V4.1 Flash。
- DeepSeek 官方已将 V4-Flash 与 V4-Flash-Vision-Exp 下线并临时路由到 V4.1 Flash，因此不在本轮建立重复的旧 alias 节点。[S1]
- `parameters.active` 保持 `null`，因为官方明确给出输入 8B、输出 16B 两种激活规模，单一标量会丢失语义。

## 关联软件与系统

- 推理引擎：[vLLM](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/vllm-project/vLLM/vLLM.md)、[SGLang](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/sgl-project/SGLang/SGLang.md)
- KV / Memory：[LMCache](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/LMCache/LMCache/LMCache.md)、[Mooncake](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/kvcache-ai/Mooncake/Mooncake.md)
- 机制：Prefill / Decode 分离、[[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层级]]

## 直接来源

- [S1] https://www.deepseek.com/en/news/deepseek-v4-1-flash/
- [S2] https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/config.json
- [S3] https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/inference/config.json
- [S4] https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/inference/model.py
