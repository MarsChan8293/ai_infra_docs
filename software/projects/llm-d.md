---
schema_version: software-v0.1
name: llm-d
object_type: project
category: distributed-serving
organization: llm-d
status: active
repo: https://github.com/llm-d/llm-d
docs: https://llm-d.ai/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - request-routing
  - kv-aware-routing
  - pd-disaggregation
  - worker-pool-orchestration
integrations:
  - vllm
  - sglang
  - lmcache
  - gateway-api-inference-extension
relations:
  alternative-to:
    - nvidia-dynamo
backends:
  - kubernetes
updated: 2026-09-16
---
# llm-d

> Kubernetes 原生的分布式 LLM 推理编排与请求路由框架。

## 核心能力

| 能力 | 说明 | 证据 |
|---|---|---|
| 请求级路由 | 在模型 worker 之间选择运行端点 | [S1] |
| KV-aware Routing | 把 prefix/KV 状态纳入路由决策 | [S1] |
| P/D 分离 | 编排 Prefill 与 Decode worker | [S1] |
| Kubernetes 集成 | 面向集群化 LLM serving | [S1] |

## 边界

llm-d 负责运行时请求与 worker 编排，不负责 GPU kernel，也不替代 Pod/Job 级集群调度器。

## 集成与后端

- [[software/projects/vllm|vLLM]]、[[software/projects/sglang|SGLang]]：模型执行 worker。
- [[software/projects/lmcache|LMCache]]：外部 KV 生命周期与传输。
- [[software/projects/gateway-api-inference-extension|Gateway API Inference Extension]]：Kubernetes inference-aware routing 基础设施。

## 关联项目

- 同层分布式推理框架：[[software/projects/nvidia-dynamo|NVIDIA Dynamo]]。
- Kubernetes 模型服务控制面：[[software/projects/kserve|KServe]]。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前官方资料为快照。

## 直接来源

- [S1] https://llm-d.ai/
- [S2] https://github.com/llm-d/llm-d
