---
schema_version: software-v0.1
name: AIBrix
object_type: project
category: distributed-serving
organization: vllm-project
status: active
repo: https://github.com/vllm-project/aibrix
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - llm-infrastructure
  - model-serving
  - autoscaling
  - request-routing
integrations:
  - vllm
backends:
  - kubernetes
updated: 2026-09-15
---
# AIBrix

> 面向大模型推理基础设施的 Kubernetes 原生控制与运维项目。

## 核心能力

AIBrix 关注模型服务实例的部署、扩缩容、路由与运行管理，适合作为推理引擎之上的基础设施控制层观察对象。

## 边界

AIBrix 不是模型执行 kernel，也不替代 [[software/projects/vllm|vLLM]] 这类推理引擎；它更靠近 serving control plane 与 Kubernetes 运行管理。

## 集成与后端

- 与 [[software/projects/vllm|vLLM]] 形成明确的上下层关系。
- 与 [[software/projects/kserve|KServe]]、[[software/projects/gateway-api-inference-extension|Gateway API Inference Extension]] 同处 Kubernetes LLM serving 控制层。

## 关联项目

- 执行层：[[software/projects/vllm|vLLM]]。
- 服务控制：[[software/projects/kserve|KServe]]、[[software/projects/nvidia-dynamo|NVIDIA Dynamo]]、[[software/projects/llm-d|llm-d]]。

## 版本快照

本页不绑定单一 release 或 commit；以 2026-09-15 前公开资料为快照。

## 直接来源

- https://github.com/vllm-project/aibrix
