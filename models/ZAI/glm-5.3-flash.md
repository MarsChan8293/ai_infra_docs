---
schema_version: model-v0.2
name: GLM-5.3-Flash
object_type: model
organization: Z.ai
family: GLM-5
status: released
release_date: 2026-08-26
architecture:
  backbone: decoder-only
  sparsity: moe
  attention: hybrid-linear-sparse-mla
parameters:
  total: 320000000000
  active: 18000000000
structure:
  num_layers: 45
  hidden_size: null
  intermediate_size: null
  attention:
    num_attention_heads: null
    num_key_value_heads: null
    head_dim: null
    growing_layers: 11
    kv_lora_rank: 512
    qk_rope_head_dim: 0
    sliding_window: null
  moe:
    num_experts: null
    experts_per_token: null
    shared_experts: null
  recurrent:
    type: linear-attention
    layers: 34
    state_size: null
context_length: 1048576
kv_cache_64k_fp8_bytes: 369098752
modalities:
  - text
  - image
  - video
weights: https://huggingface.co/zai-org/GLM-5.3-Flash
snapshot:
  revision: null
  as_of: 2026-09-16
updated: 2026-09-16
---

# GLM-5.3-Flash

> Z.ai 的 320B-A18B 原生多模态 Flash 模型，以 34 层线性注意力 + 11 层 sparse MLA 把 1M 长上下文的增长型 KV 压到较低水平。

## 核心规格

| 项目 | 值 | Evidence |
|---|---:|---|
| 发布日期 | 2026-08-26 | [S4] |
| 总参数 | 320B | [S1] |
| 激活参数 | 18B | [S1] |
| 原生最大上下文 | 1,048,576 tokens | [S2] |
| 模态 | Text + Image + Video | [S2][S3] |
| 64K FP8 KV footprint | 369,098,752 bytes（352 MiB） | [S2] |

## 架构特征

| 特征 | 说明 | Evidence |
|---|---|---|
| Hybrid attention | 45 层中 34 层 linear attention、11 层 deepseek sparse attention | [S2] |
| Full/sparse attention layers | 3/7/11/.../43，共 11 层 | [S2] |
| MLA | `kv_lora_rank=512`，`qk_rope_head_dim=0` | [S2] |
| MoE | 320B total / 18B active | [S1] |
| Native multimodal | GLM-5 系首个原生多模态模型 | [S3] |

## AI Infra 关注点

- 只有 11 个 sparse-MLA 层产生随序列增长的 latent KV；34 个 linear-attention 层的固定 recurrent/conv state 不计入该指标。[S2]
- 计算为 `65536 × 11 × 512 = 369,098,752 bytes`。[S2]
- **分析判断：**与 GLM-5.3 相比，Flash 的关键系统差异不是只有参数变小，而是 attention state 从“绝大多数层增长”转为“少数层增长 + 多数层固定状态”。

## 版本与边界

- ZCode 官方 changelog 在 2026-08-26 加入 GLM-5.3 Flash 多模态模型。[S4]
- 页面记录的是 canonical open weights；不同 FP8/BF16/NVFP4 checkpoint 不拆成独立模型实体。

## 关联软件与系统

- 推理引擎：[vLLM](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/vllm-project/vLLM/vLLM.md)、[SGLang](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/sgl-project/SGLang/SGLang.md)、[TokenSpeed](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/lightseekorg/TokenSpeed/TokenSpeed.md)
- Kernel：[FlashInfer](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/flashinfer-ai/FlashInfer/FlashInfer.md)
- KV：[LMCache](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/LMCache/LMCache/LMCache.md)、[Mooncake](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/kvcache-ai/Mooncake/Mooncake.md)

## 直接来源

- [S1] https://github.com/zai-org/GLM-5
- [S2] https://huggingface.co/zai-org/GLM-5.3-Flash/blob/main/config.json
- [S3] https://autoclaw.z.ai/blog/model/glm-5.3-flash/
- [S4] https://zcode.z.ai/en/changelog
