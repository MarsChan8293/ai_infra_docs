---
schema_version: software-v0.1
name: Triton Inference Server
object_type: project
category: distributed-serving
organization: triton-inference-server
status: active
repo: https://github.com/triton-inference-server/server
docs: https://docs.nvidia.com/deeplearning/triton-inference-server/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - model-serving
  - dynamic-batching
  - multi-framework-serving
integrations:
  - tensorrt-llm
backends:
  - nvidia
  - cpu
updated: 2026-09-15
---
# Triton Inference Server

> NVIDIA 主导的通用模型推理服务服务器，覆盖多框架 backend、调度与服务接口。

## 核心能力

提供模型仓库、backend、动态批处理、并发执行和标准化推理服务接口，可承载传统模型与 LLM backend。

## 边界

它是通用 serving server，不等同于 [[software/projects/triton|Triton]] GPU kernel DSL，也不替代 Kubernetes 集群调度器。

## 集成与后端

- [[software/projects/tensorrt-llm|TensorRT-LLM]] 可作为 LLM 优化路径之一。
- 可位于 [[software/projects/kserve|KServe]] 等 Kubernetes serving 层之下。

## 关联项目

- [[software/projects/tensorrt-llm|TensorRT-LLM]]
- [[software/projects/kserve|KServe]]
- [[software/projects/nvidia-gpu-operator|NVIDIA GPU Operator]]
- [[software/projects/triton|Triton]]（名称相近但职责不同）

## 版本快照

本页以 2026-09-15 前官方资料为快照。

## 直接来源

- https://github.com/triton-inference-server/server
- https://docs.nvidia.com/deeplearning/triton-inference-server/
