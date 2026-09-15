---
schema_version: software-v0.1
name: CUTLASS
object_type: project
category: runtime
organization: NVIDIA
status: active
repo: https://github.com/NVIDIA/cutlass
docs: https://docs.nvidia.com/cutlass/latest/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - gemm
  - cute
  - cuda-templates
  - python-dsl
integrations:
  - deepgemm
backends:
  - nvidia
updated: 2026-09-15
---
# CUTLASS

> NVIDIA CUDA 高性能线性代数 kernel 的模板、CuTe 抽象与 Python DSL 工具库。

## 核心能力

| 能力 | 说明 |
|---|---|
| GEMM | 提供高性能矩阵乘 kernel 构建模块 |
| CuTe | 用可组合布局和张量抽象描述数据移动与计算 |
| 低精度类型 | 覆盖 FP8、FP4 等现代 Tensor Core 路径 |
| Kernel Building Blocks | 为自定义 kernel 和上层库提供积木 |

## 边界

CUTLASS 聚焦 NVIDIA CUDA kernel 构建，不负责模型图执行、Serving API 或跨节点调度。

## 集成与后端

- [[software/projects/deepgemm|DeepGEMM]]：kernel 基础设施关系。

## 关联项目

- 推理 runtime：[[software/projects/tensorrt-llm|TensorRT-LLM]]。
- Kernel / DSL 生态：[[software/projects/flashinfer|FlashInfer]]、[[software/projects/triton|Triton]]、[[software/projects/tilelang|TileLang]]。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前 CUTLASS 官方资料为快照。

## 直接来源

- https://docs.nvidia.com/cutlass/latest/
- https://github.com/NVIDIA/cutlass
