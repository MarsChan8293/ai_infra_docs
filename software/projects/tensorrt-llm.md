---
schema_version: software-v0.1
name: TensorRT-LLM
object_type: project
category: inference-engine
organization: NVIDIA
status: active
repo: https://github.com/NVIDIA/TensorRT-LLM
docs: https://docs.nvidia.com/tensorrt-llm/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - tensorrt-engine
  - quantization
  - speculative-decoding
  - tensor-parallel
  - expert-parallel
  - disaggregated-serving
integrations:
  - nvidia-dynamo
relations:
  alternative-to:
    - vllm
    - sglang
backends:
  - nvidia
updated: 2026-09-16
---
# TensorRT-LLM

> NVIDIA 面向 LLM 的高性能推理运行时与 TensorRT 优化栈。

## 核心能力

| 能力 | 说明 | 证据 |
|---|---|---|
| TensorRT Engine | 把模型构建为面向 NVIDIA GPU 优化的执行引擎 | [S1] |
| 低精度优化 | 覆盖 FP8、FP4 等推理优化路径 | [S1] |
| 并行与 MoE | 支持多 GPU 与专家并行场景 | [S1] |
| Serving Runtime | 提供 Python/C++ runtime 与服务化能力 | [S1] |

## 边界

TensorRT-LLM 深度绑定 NVIDIA GPU/TensorRT 技术栈，不追求跨厂商硬件统一抽象。

## 集成与后端

- [[software/projects/nvidia-dynamo|NVIDIA Dynamo]]：可作为 TensorRT-LLM 之上的分布式推理控制面。
- NVIDIA GPU 是其主要硬件后端。

## 关联项目

- 同层引擎：[[software/projects/vllm|vLLM]]、[[software/projects/sglang|SGLang]]。
- Kernel：[[software/projects/cutlass|CUTLASS]]。
- 通信：[[software/projects/nccl|NCCL]]。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前官方资料为快照。

## 直接来源

- [S1] https://docs.nvidia.com/tensorrt-llm/
- [S2] https://github.com/NVIDIA/TensorRT-LLM
