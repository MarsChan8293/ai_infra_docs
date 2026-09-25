---
title: AI Model Index
aliases:
  - Model Index
  - 模型索引
tags:
  - moc
  - models
updated: 2026-09-16
---

# AI Model Index

本目录按 **Model Schema V0.1** 记录与 AI Infra 强相关的模型事实。首批覆盖窗口为 **2026-06-16 至 2026-09-16** 的 DeepSeek、Kimi、GLM、Qwen 主要公开模型。

## Architecture Anchors

这里的 Anchor 不是“模型排名”，而是为 System 层选择有公开架构证据的代表节点。同一个模型可以同时承担多个架构锚点。

| 架构锚点 | 代表模型 | 可机器化特征 | 主要 System 入口 |
|---|---|---|---|
| Dense | [[models/Qwen/qwen3.8-27b|Qwen3.8-27B]] | 64 layers、Dense、16 growing attention layers | [[system/compute/transformer-compute-model|Compute]] / [[system/memory/weight-memory|Weight]] |
| GQA / grouped KV | [[models/Qwen/qwen3.8-27b|Qwen3.8-27B]] | 24 Q heads、4 KV heads、head_dim=256 | [[system/memory/kv-cache-model|KV Cache]] |
| MLA / compressed KV | [[models/MoonshotAI/kimi-k3|Kimi K3]]、[[models/ZAI/glm-5.3|GLM-5.3]] | kv_lora_rank / rope cache dimensions | [[system/memory/kv-cache-model|KV Cache]] |
| MoE | [[models/Qwen/qwen3.8-2.4t-a95b|Qwen3.8-2.4T-A95B]] | total/active params、512 experts、top-10 + shared expert | [[system/moe/moe-system-model|MoE System]] |
| Linear / recurrent attention | [[models/Qwen/qwen3.8-27b|Qwen3.8-27B]]、[[models/MoonshotAI/kimi-k3|Kimi K3]] | Gated DeltaNet / KDA recurrent layers | [[system/compute/prefill-vs-decode|Prefill vs Decode]] |
| Sparse / hybrid attention | [[models/Qwen/qwen3.8-flash-next|Qwen3.8-Flash-Next]]、[[models/ZAI/glm-5.3-flash|GLM-5.3-Flash]] | 少量 growing attention + sparse/linear layers | [[system/memory/kv-cache-model|KV Cache]] |
| Multimodal | [[models/Qwen/qwen3.8-27b|Qwen3.8-27B]]、[[models/MoonshotAI/kimi-k3|Kimi K3]] | Text + Image / Video modalities | [[system/workload/ai-workload-model|Workload]] |

Anchor 的字段仍以各模型页的 direct Evidence 为准。表格只做导航，不从相似模型补齐未知结构。

## DeepSeek

- [[models/DeepSeek/deepseek-v4.1-flash|DeepSeek V4.1 Flash]]

## Kimi / Moonshot AI

- [[models/MoonshotAI/kimi-k3|Kimi K3]]

## GLM / Z.ai

- [[models/ZAI/glm-5.3|GLM-5.3]]
- [[models/ZAI/glm-5.3-flash|GLM-5.3-Flash]]

> GLM-5.2 首发于 2026-06-13，早于本轮三个月窗口起点，因此不作为本轮新节点；它作为 GLM-5.3 的前代在相关页面中说明。

## Qwen

- [[models/Qwen/qwen3.8-2.4t-a95b|Qwen3.8-2.4T-A95B]]
- [[models/Qwen/qwen3.8-27b|Qwen3.8-27B]]
- [[models/Qwen/qwen3.8-flash-next|Qwen3.8-Flash-Next]]

## 规则

- Schema：[[models/SCHEMA|Model Schema V0.1]]
- 模型事实必须绑定 Evidence。
- `kv_cache_64k_fp8_bytes` 使用统一的 64K / FP8 / batch=1 派生口径。
- 模型页只记录模型事实和直接架构影响；部署性能与具体系统方案不写入 Model Schema。
