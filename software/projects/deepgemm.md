---
schema_version: software-v0.1
name: DeepGEMM
object_type: project
category: runtime
organization: deepseek-ai
status: active
repo: https://github.com/deepseek-ai/DeepGEMM
docs: https://github.com/deepseek-ai/DeepGEMM
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - gemm
  - fp8
  - fp4
  - moe-kernels
  - jit
integrations:
  - cutlass
backends:
  - nvidia
updated: 2026-09-15
---
# DeepGEMM

> DeepSeek 开源的高性能 Tensor Core kernel 库，覆盖现代 LLM 的 GEMM 与 MoE 核心计算。

## 核心能力

| 能力 | 说明 |
|---|---|
| 低精度 GEMM | 覆盖 FP8、FP4、BF16 等矩阵乘 |
| MoE Kernels | 面向专家模型的融合计算路径 |
| JIT | 运行时编译与特化 kernel |
| 轻量实现 | 强调较小而清晰的高性能 CUDA 代码 |

## 边界

DeepGEMM 专注 NVIDIA GPU 计算 kernel；通信、请求路由、KV Cache 和集群管理由其他层处理。

## 集成与后端

- [[software/projects/cutlass|CUTLASS]]：当前构建要求与 kernel 基础设施关系明确。

## 关联项目

- Kernel DSL：[[software/projects/triton|Triton]]。
- MoE 通信：[[software/projects/deepep|DeepEP]]。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前官方仓库为快照。

## 直接来源

- https://github.com/deepseek-ai/DeepGEMM
