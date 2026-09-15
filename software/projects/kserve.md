---
schema_version: software-v0.1
name: KServe
object_type: project
category: distributed-serving
organization: KServe
status: active
repo: https://github.com/kserve/kserve
docs: https://kserve.github.io/website/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - kubernetes-model-serving
  - llm-inference-service
  - autoscaling
  - inference-routing
integrations:
  - vllm
  - gateway-api-inference-extension
backends:
  - kubernetes
updated: 2026-09-15
---
# KServe

> Kubernetes 原生模型服务控制面，覆盖传统 InferenceService 与 LLMInferenceService。

## 核心能力

| 能力 | 说明 |
|---|---|
| InferenceService | 标准化模型部署与服务入口 |
| LLMInferenceService | 面向生成式 AI 的 LLM serving API |
| 多节点 / 分离式工作负载 | 可表达多节点并行与 Prefill/Decode 分离 |
| Gateway 集成 | 通过 Kubernetes Gateway 体系暴露和路由服务 |

## 边界

KServe 主要负责 Kubernetes 模型服务生命周期和 API 编排，不负责底层 LLM kernel 与单 worker 执行优化。

## 集成与后端

- [[software/projects/vllm|vLLM]]：KServe 生成式推理 runtime 的主要高性能后端之一。
- [[software/projects/gateway-api-inference-extension|Gateway API Inference Extension]]：LLMInferenceService 路由基础设施之一。

## 关联项目

- 分布式推理编排：[[software/projects/llm-d|llm-d]]。
- 另一条分布式服务路线：[[software/projects/ray-serve|Ray Serve]]。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前官方文档为快照。

## 直接来源

- https://kserve.github.io/website/
- https://github.com/kserve/kserve
