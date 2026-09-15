---
schema_version: software-v0.1
name: RCCL
object_type: project
category: communication
organization: AMD ROCm
status: active
repo: https://github.com/ROCm/rocm-systems
docs: https://rocm.docs.amd.com/projects/rccl/en/latest/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - all-reduce
  - all-gather
  - reduce-scatter
  - all-to-all
  - point-to-point
integrations: []
backends:
  - amd
updated: 2026-09-15
---
# RCCL

> AMD ROCm 面向多 GPU、多节点的集合通信库。

## 核心能力

| 能力 | 说明 |
|---|---|
| Collectives | 覆盖 AllReduce、AllGather、AllToAll 等原语 |
| xGMI / PCIe | 优化 AMD GPU 节点内高速互联 |
| RDMA / Network | 支持跨节点 InfiniBand、RoCE 等通信路径 |
| P2P | 支持 GPU 到 GPU 点到点通信 |

## 边界

RCCL 位于通信层，不负责模型执行、Serving 或调度策略。

## 集成与后端

V0.1 将框架使用 RCCL 的关系记录在关联区，不自动把所有 ROCm 使用者标为强集成。

## 关联项目

- NVIDIA 对应通信栈：[[software/projects/nccl|NCCL]]。
- AMD 推理引擎路径：[[software/projects/vllm|vLLM]]、[[software/projects/sglang|SGLang]]。

## 版本快照

本页不绑定单一 release；能力判断以 2026-09-15 前 ROCm RCCL 官方文档为快照。

## 直接来源

- https://rocm.docs.amd.com/projects/rccl/en/latest/
- https://github.com/ROCm/rocm-systems
