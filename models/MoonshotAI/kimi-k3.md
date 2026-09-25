---
schema_version: model-v0.1
name: Kimi K3
object_type: model
organization: Moonshot AI
family: Kimi K3
status: released
release_date: 2026-07-17
architecture:
  backbone: decoder-only
  sparsity: moe
  attention: hybrid-kda-mla
parameters:
  total: 2800000000000
  active: null
context_length: 1048576
kv_cache_64k_fp8_bytes: 905969664
modalities:
  - text
  - image
weights: https://huggingface.co/moonshotai/Kimi-K3
snapshot:
  revision: null
  as_of: 2026-09-16
updated: 2026-09-16
---

# Kimi K3

> Moonshot AI 的 2.8T MoE 原生视觉模型，以 Kimi Delta Attention、Attention Residuals 与超稀疏专家规模扩展到 1M 上下文。

## 核心规格

| 项目 | 值 | Evidence |
|---|---:|---|
| 总参数 | 2.8T | [S1][S2] |
| 激活参数 | 公开资料未给出统一参数量口径 | [S1] |
| 原生最大上下文 | 1,048,576 tokens | [S1][S3] |
| 模态 | Text + Image | [S1][S2] |
| 64K FP8 KV footprint | 905,969,664 bytes（864 MiB） | [S3] |

## 架构特征

| 特征 | 说明 | Evidence |
|---|---|---|
| Attention | KDA 线性注意力与 full MLA 混合 | [S1][S3] |
| Attention Residuals | 以 block 级残差改善深层信息流 | [S1] |
| MoE | 896 routed experts，每 token 激活 16 个，另有 2 shared experts | [S1][S3] |
| Layers | 93 层；24 个 full-attention layer，其余为 KDA | [S3] |
| MLA cache width | `kv_lora_rank=512` + `qk_rope_head_dim=64` | [S3] |

## AI Infra 关注点

- KDA 层维护固定规模 recurrent/conv state，不随 64K 序列线性增长，因此不计入本仓库的 KV 派生指标。[S3]
- 24 个 full-attention 层按 latent KV `512 + 64` bytes/token/layer 的 FP8 口径计算：`65536 × 24 × 576 = 905,969,664 bytes`。[S3]
- **分析判断：**K3 把大量层从增长型 KV 转成固定状态，使长上下文服务的状态容量曲线和传统 Transformer 明显不同；容量评估应同时观察“增长型 KV”和“固定 recurrent state”。

## 版本与边界

- Kimi K3 于 2026-07-17 发布，完整权重和技术资料于 2026-07-27 开放。[S1][S2]
- `parameters.active` 不根据 896/16 专家比例反推，因为 dense/shared/attention 等部分会使简单比例失真。

## 关联软件与系统

- 推理引擎：[vLLM](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/vllm-project/vLLM/vLLM.md)、[SGLang](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/sgl-project/SGLang/SGLang.md)
- Kernel / Communication：[FlashInfer](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/flashinfer-ai/FlashInfer/FlashInfer.md)、[DeepEP](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/deepseek-ai/DeepSeek-Infra/DeepEP.md)
- KV：[LMCache](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/LMCache/LMCache/LMCache.md)、[Mooncake](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/kvcache-ai/Mooncake/Mooncake.md)

## 直接来源

- [S1] https://www.kimi.com/news/kimi-k3
- [S2] https://www.kimi.com/news/kimi-k3-open-source
- [S3] https://huggingface.co/moonshotai/Kimi-K3/blob/main/config.json
