---
schema_version: software-v0.1
name: NCCL
object_type: project
category: communication
organization: NVIDIA
status: active
repo: https://github.com/NVIDIA/nccl
docs: https://docs.nvidia.com/deeplearning/nccl/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - all-reduce
  - all-gather
  - reduce-scatter
  - broadcast
  - point-to-point
integrations:
  - vllm
  - tensorrt-llm
  - deepep
backends:
  - nvidia
updated: 2026-09-15
---
# NCCL

> NVIDIA GPU 多卡与多节点集合通信库。

## 核心能力

| 能力 | 说明 |
|---|---|
| Collectives | 提供 AllReduce、AllGather、ReduceScatter、Broadcast 等原语 |
| Topology-aware | 根据 NVLink、PCIe、网络拓扑优化通信 |
| Multi-node | 支持跨节点 GPU 通信 |
| P2P | 提供点到点 send/recv 能力 |

## 边界

NCCL 只解决通信原语，不负责模型并行策略本身、请求调度或 Pod placement。

## 集成与后端

- [[software/projects/vllm|vLLM]]、[[software/projects/tensorrt-llm|TensorRT-LLM]]：NVIDIA 多 GPU 推理的重要通信底座。
- [[software/projects/deepep|DeepEP]]：DeepEP 的通信后端关系。

## 关联项目

- 通信对照：[[software/projects/rccl|RCCL]]、[[software/projects/vccl|VCCL]]、[[software/projects/flagcx|FlagCX]]。
- 训练框架：[[software/projects/colossal-ai|Colossal-AI]]、[[software/projects/oneflow|OneFlow]]。

## 版本快照

本页不绑定单一 release；能力判断以 2026-09-15 前 NVIDIA 官方文档为快照。

## 直接来源

- https://docs.nvidia.com/deeplearning/nccl/
- https://github.com/NVIDIA/nccl
