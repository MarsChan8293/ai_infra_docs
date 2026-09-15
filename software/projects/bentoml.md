---
schema_version: software-v0.1
name: BentoML
object_type: project
category: distributed-serving
organization: BentoML
status: active
repo: https://github.com/bentoml/BentoML
docs: https://docs.bentoml.com/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - model-serving
  - api-service
  - autoscaling
  - packaging
integrations:
  - vllm
backends:
  - cpu
  - nvidia
updated: 2026-09-15
---
# BentoML

> 面向 AI 应用和模型的通用 serving 与部署框架。

## 核心能力

| 能力 | 说明 |
|---|---|
| Service API | 用 Python 定义模型与业务服务 API |
| 模型打包 | 把代码、模型和依赖组织成可部署单元 |
| 在线 Serving | 提供 HTTP 服务和生产部署能力 |
| LLM Backend | 可采用专用 LLM 推理引擎作为后端 |

## 边界

BentoML 覆盖范围比专用 LLM engine 更上层、更通用，不会替代 vLLM/SGLang 的底层 token 执行优化。

## 集成与后端

- [[software/projects/vllm|vLLM]]：官方文档提供以 vLLM 为推理后端的 LLM 部署路径。

## 关联项目

- API / Gateway 层：[[software/projects/litellm|LiteLLM]]。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前官方文档为快照。

## 直接来源

- https://docs.bentoml.com/
- https://github.com/bentoml/BentoML
