---
schema_version: software-v0.1
name: FlashInfer
object_type: project
category: runtime
organization: flashinfer-ai
status: active
repo: https://github.com/flashinfer-ai/flashinfer
docs: https://docs.flashinfer.ai/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - attention-kernels
  - paged-attention
  - lora-kernels
  - kernel-generation
integrations:
  - vllm
  - sglang
relations:
  backend-for:
    - vllm
    - sglang
backends:
  - nvidia
updated: 2026-09-16
---
# FlashInfer

> 专注 LLM serving 的高性能 GPU kernel library 与 kernel generator。

## 核心能力

| 能力 | 说明 | 证据 |
|---|---|---|
| Attention Kernels | 提供 FlashAttention、Paged Attention 等高性能实现 | [S1] |
| Serving-oriented | 围绕动态 batch、KV layout 等 serving 场景优化 | [S1] |
| Kernel Generation | 支持 JIT / 预编译 kernel 管理 | [S1] |
| LoRA 等算子 | 覆盖多类 LLM serving 核心算子 | [S1] |

## 边界

FlashInfer 负责 GPU kernel 与算子层，不承担完整请求服务、分布式路由或 Kubernetes 管理。

## 集成与后端

- [[software/projects/vllm|vLLM]]、[[software/projects/sglang|SGLang]]：上层推理引擎集成路径。

## 关联项目

- Attention：[[software/projects/flashattention|FlashAttention]]。
- Kernel / 编译：[[software/projects/triton|Triton]]、[[software/projects/cutlass|CUTLASS]]。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前官方文档为快照。

## 直接来源

- [S1] https://docs.flashinfer.ai/
- [S2] https://github.com/flashinfer-ai/flashinfer
