---
schema_version: software-v0.1
name: Triton
object_type: project
category: compiler
organization: triton-lang
status: active
repo: https://github.com/triton-lang/triton
docs: https://triton-lang.org/main/index.html
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - gpu-kernel-dsl
  - compiler
  - jit
  - mlir
integrations: []
backends:
  - nvidia
  - amd
updated: 2026-09-15
---
# Triton

> 用于编写高性能并行计算与深度学习 kernel 的语言和编译器。

## 核心能力

| 能力 | 说明 |
|---|---|
| Python DSL | 用 Python 风格语言描述 GPU kernel |
| Compiler | 把 Triton 程序编译到底层 GPU 代码 |
| JIT | 支持运行时特化与编译 |
| MLIR | 使用 Triton MLIR dialect 表达和优化程序 |

## 边界

Triton 是 kernel 开发与编译层，不负责模型 serving 或集群编排。

## 集成与后端

V0.1 暂不把“项目内部存在 Triton kernel”自动升级为强集成关系。

## 关联项目

- 上层推理：[[software/projects/vllm|vLLM]]、[[software/projects/sglang|SGLang]]。
- Kernel 库：[[software/projects/flashinfer|FlashInfer]]、[[software/projects/flashattention|FlashAttention]]、[[software/projects/cutlass|CUTLASS]]、[[software/projects/deepgemm|DeepGEMM]]。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前官方资料为快照。

## 直接来源

- https://triton-lang.org/main/index.html
- https://github.com/triton-lang/triton
