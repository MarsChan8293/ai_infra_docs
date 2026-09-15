---
schema_version: software-v0.1
name: SGLang
object_type: project
category: inference-engine
organization: sgl-project
status: active
repo: https://github.com/sgl-project/sglang
docs: https://docs.sglang.ai/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - continuous-batching
  - radix-attention
  - prefix-caching
  - tensor-parallel
  - expert-parallel
  - speculative-decoding
integrations:
  - nvidia-dynamo
  - ray-serve
  - llm-d
  - mooncake
  - flashinfer
relations:
  alternative-to:
    - vllm
    - tensorrt-llm
    - llama-cpp
backends:
  - nvidia
  - amd
  - intel
  - ascend
  - tpu
updated: 2026-09-16
---
# SGLang

> 面向大模型与多模态模型的高性能推理与 serving 框架。

## 核心能力

| 能力 | 说明 | 证据 |
|---|---|---|
| RadixAttention / Prefix Cache | 围绕共享前缀和 KV 复用优化请求执行 | [S1] |
| Serving Runtime | 提供在线服务、调度与模型执行 | [S1] |
| 分布式执行 | 支持多 GPU、多节点及多种并行方式 | [S1] |
| 多硬件后端 | 覆盖 NVIDIA、AMD、Ascend、TPU 等路径 | [S1] |

## 边界

SGLang 的主战场是模型推理执行与 serving runtime；集群级 Pod placement、设备资源治理和通用 AI Gateway 不属于其核心职责。

## 集成与后端

- [[software/projects/nvidia-dynamo|NVIDIA Dynamo]]、[[software/projects/ray-serve|Ray Serve]]、[[software/projects/llm-d|llm-d]]：分布式 serving 与路由层。
- [[software/projects/mooncake|Mooncake]]：高性能数据 / KV 传输集成。
- [[software/projects/flashinfer|FlashInfer]]：serving kernel 后端之一。

## 关联项目

- 同层引擎：[[software/projects/vllm|vLLM]]、[[software/projects/tensorrt-llm|TensorRT-LLM]]、[[software/projects/llama-cpp|llama.cpp]]。
- Kernel / 编译：[[software/projects/triton|Triton]]、[[software/projects/flashattention|FlashAttention]]、[[software/projects/deepep|DeepEP]]。
- AMD 通信路径：[[software/projects/rccl|RCCL]]。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前官方资料为快照。

## 直接来源

- [S1] https://docs.sglang.ai/
- [S2] https://github.com/sgl-project/sglang
