---
schema_version: software-v0.1
name: LightLLM
object_type: project
category: inference-engine
organization: ModelTC
status: active
repo: https://github.com/ModelTC/lightllm
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - llm-serving
  - distributed-inference
  - token-generation
integrations: []
backends:
  - nvidia
updated: 2026-09-15
---
# LightLLM

> 面向大模型在线推理的轻量高性能 serving engine。

## 核心能力

关注请求调度、模型执行、显存管理与多卡推理，是推理引擎横向比较中值得保留的一条社区路线。

## 边界

LightLLM 主要位于执行与 serving runtime 层，不负责集群级资源编排。

## 集成与后端

与 [[software/projects/vllm|vLLM]]、[[software/projects/sglang|SGLang]]、[[software/projects/tensorrt-llm|TensorRT-LLM]] 同属推理引擎比较集合。

## 关联项目

- [[software/projects/vllm|vLLM]]
- [[software/projects/sglang|SGLang]]
- [[software/projects/tensorrt-llm|TensorRT-LLM]]

## 版本快照

本页以 2026-09-15 前公开资料为快照。

## 直接来源

- https://github.com/ModelTC/lightllm
