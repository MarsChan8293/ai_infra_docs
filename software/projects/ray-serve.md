---
schema_version: software-v0.1
name: Ray Serve
object_type: project
category: distributed-serving
organization: Ray / Anyscale
status: active
repo: https://github.com/ray-project/ray
docs: https://docs.ray.io/en/latest/serve/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - distributed-serving
  - autoscaling
  - multi-model
  - pd-disaggregation
  - prefix-aware-routing
integrations:
  - vllm
  - sglang
backends:
  - nvidia
  - amd
  - intel
  - tpu
  - ascend
updated: 2026-09-15
---
# Ray Serve

> 构建在 Ray 上的分布式模型 serving 框架，并提供专门的 LLM serving 能力。

## 核心能力

| 能力 | 说明 |
|---|---|
| 多节点 Serving | 利用 Ray runtime 构建分布式模型服务 |
| LLM Serve | 提供 OpenAI-compatible LLM 服务入口 |
| P/D 分离 | 支持 Prefill 与 Decode 独立扩展 |
| 路由与扩缩容 | 支持 prefix-aware routing、autoscaling 和多模型 |

## 边界

Ray Serve 偏分布式应用与模型 serving；底层 token 执行通常由专用推理引擎承担。

## 集成与后端

- [[software/projects/vllm|vLLM]]：主要 LLM engine 路径。
- [[software/projects/sglang|SGLang]]：可作为 Ray Serve LLM 的 engine 后端。

## 关联项目

- Kubernetes 原生 serving 控制面可对照 [[software/projects/kserve|KServe]]。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前 Ray Serve LLM 官方文档为快照。

## 直接来源

- https://docs.ray.io/en/latest/serve/llm/
- https://github.com/ray-project/ray
