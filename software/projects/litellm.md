---
schema_version: software-v0.1
name: LiteLLM
object_type: project
category: distributed-serving
organization: BerriAI
status: active
repo: https://github.com/BerriAI/litellm
docs: https://docs.litellm.ai/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - llm-gateway
  - provider-routing
  - rate-limiting
  - cost-tracking
  - openai-compatible-proxy
integrations: []
backends:
  - api
updated: 2026-09-15
---
# LiteLLM

> 面向多模型、多提供商的 OpenAI-compatible LLM Gateway 与统一客户端层。

## 核心能力

| 能力 | 说明 |
|---|---|
| 统一 API | 用统一 OpenAI 风格接口调用多类模型提供方 |
| Proxy / Gateway | 自托管模型网关与路由 |
| 治理能力 | 支持认证、限流、成本跟踪和日志钩子 |
| Fallback / Routing | 在多个 deployment/provider 间路由和回退 |

## 边界

LiteLLM 主要管理 API 与模型提供方流量，不负责 GPU kernel、KV Cache 或 Kubernetes 设备资源。

## 集成与后端

V0.1 暂不把通用 OpenAI-compatible endpoint 兼容自动视作“项目级强集成”。

## 关联项目

- Kubernetes inference routing：[[software/projects/gateway-api-inference-extension|Gateway API Inference Extension]]。
- 通用模型服务：[[software/projects/bentoml|BentoML]]。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前官方文档为快照。

## 直接来源

- https://docs.litellm.ai/
- https://github.com/BerriAI/litellm
