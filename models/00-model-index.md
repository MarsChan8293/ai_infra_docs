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
