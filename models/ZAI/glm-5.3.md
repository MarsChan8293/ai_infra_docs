---
schema_version: model-v0.1
name: GLM-5.3
object_type: model
organization: Z.ai
family: GLM-5
status: released
release_date: 2026-08-14
architecture:
  backbone: decoder-only
  sparsity: moe
  attention: sparse-mla
parameters:
  total: 744000000000
  active: 40000000000
context_length: 1048576
kv_cache_64k_fp8_bytes: 2944401408
modalities:
  - text
weights: https://huggingface.co/zai-org/GLM-5.3
snapshot:
  revision: null
  as_of: 2026-09-16
updated: 2026-09-16
---

# GLM-5.3

> Z.ai 2026-08-14 发布的 744B-A40B GLM-5 系旗舰后训练版本，沿用 GLM-5.2 base model 并面向 coding 与长程 Agent 继续强化。

## 核心规格

| 项目 | 值 | Evidence |
|---|---:|---|
| 总参数 | 744B | [S1] |
| 激活参数 | 40B | [S1] |
| 原生最大上下文 | 1,048,576 tokens | [S2] |
| 模态 | Text | [S1] |
| 64K FP8 KV footprint | 2,944,401,408 bytes（2.7421875 GiB） | [S2] |

## 架构特征

| 特征 | 说明 | Evidence |
|---|---|---|
| Base model | 与 GLM-5.2 使用同一 base model，增益来自 post-training | [S1] |
| MoE | 744B-A40B | [S1] |
| Attention | GLM MoE DSA / sparse MLA 路线 | [S1][S2] |
| Layers | 78 层 | [S2] |
| MLA cache width | `kv_lora_rank=512` + `qk_rope_head_dim=64` | [S2] |

## AI Infra 关注点

- 按 78 层 latent KV、每层 `512 + 64` 个 FP8 缓存值计算：`65536 × 78 × 576 = 2,944,401,408 bytes`。[S2]
- 该值不包含 DSA indexer key / top-k candidate metadata。
- **分析判断：**GLM-5.3 的主要系统压力仍然是超大 MoE 权重、EP 通信与长上下文 sparse-attention 数据路径，post-training 本身并未改变 base architecture 的 KV 几何。

## 版本与边界

- GLM-5.3 于 2026-08-14 在 ZCode 官方 changelog 中发布。[S3]
- 官方项目明确说明 GLM-5.3 与 GLM-5.2 共用同一 base model；因此本页不把 post-training 能力差异写成新硬件架构。[S1]
- GLM-5.2 首发早于 2026-06-16，本轮不建立独立 recent-release 节点。

## 关联项目

- 推理引擎：[[software/projects/vllm|vLLM]]、[[software/projects/sglang|SGLang]]
- 通信：[[software/projects/nccl|NCCL]]、[[software/projects/deepep|DeepEP]]
- 异构推理：[[software/concepts/heterogeneous-inference|异构推理]]

## 直接来源

- [S1] https://github.com/zai-org/GLM-5
- [S2] https://huggingface.co/zai-org/GLM-5.3/blob/main/config.json
- [S3] https://zcode.z.ai/en/changelog
