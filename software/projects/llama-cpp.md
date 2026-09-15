---
schema_version: software-v0.1
name: llama.cpp
object_type: project
category: inference-engine
organization: ggml-org
status: active
repo: https://github.com/ggml-org/llama.cpp
docs: https://github.com/ggml-org/llama.cpp
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - gguf
  - quantization
  - local-inference
  - openai-compatible-server
integrations: []
backends:
  - cpu
  - nvidia
  - amd
  - apple
updated: 2026-09-15
---
# llama.cpp

> 以 C/C++ 为核心、强调本地与广泛硬件适配的 LLM/VLM 推理项目。

## 核心能力

| 能力 | 说明 |
|---|---|
| GGUF 生态 | 围绕 GGUF 模型格式进行加载、量化和执行 |
| 本地推理 | 强调低依赖、本地设备和边缘环境 |
| llama-server | 提供 OpenAI-compatible 服务入口 |
| 多硬件路径 | 覆盖 CPU 与多类 GPU/加速后端 |

## 边界

llama.cpp 更强调便携、本地和边缘推理，不以大规模 Kubernetes 分布式 serving 为主要设计中心。

## 集成与后端

当前 V0.1 不记录特定上层系统为强集成；硬件支持范围广，但不同 backend 的性能与功能不应视为等价。

## 关联项目

- 数据中心推理引擎对照：[[software/projects/vllm|vLLM]]、[[software/projects/sglang|SGLang]]。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前官方仓库为快照。

## 直接来源

- https://github.com/ggml-org/llama.cpp
