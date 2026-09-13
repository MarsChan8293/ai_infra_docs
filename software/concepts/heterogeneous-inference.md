---
title: 异构推理
aliases:
  - Heterogeneous Inference
  - 异构 GPU NPU 推理
tags:
  - concept
  - heterogeneous
  - inference
  - ai-infra
---

# 异构推理

异构推理不是把 NVIDIA GPU、Ascend NPU、AMD GPU 或其他加速器“伪装成同一种卡”，而是显式保留模型、硬件、推理引擎、拓扑和 SLA 差异，再由控制面做选择。

## 核心决策链

```text
模型 / 请求画像
  + Benchmark
  + SLA / 成本目标
        │
        ▼
AI Infra Control Plane
  ├── 选择推理引擎：[[software/inference-engine/vllm|vLLM]] / 其他引擎
  ├── 请求级路由：[[software/distributed-serving/llm-d|llm-d]] / Router
  ├── Pod 级放置：[[software/scheduling/kai-scheduler|KAI-Scheduler]]
  └── 设备表达与分配：[[software/device-resource/dra|Kubernetes DRA]] / [[software/device-resource/hami|HAMi]]
        │
        ▼
NVIDIA / Ascend / AMD / 其他 GPU、NPU
```

## 不应该被抹平的差异

至少应记录：显存或 HBM 容量、HBM 带宽、算力类型、互联带宽、NUMA/PCIe/NVLink/HCCS/RoCE 拓扑、模型和算子支持、量化能力、推理引擎兼容性、TP/EP/DP 扩展效率、KV Cache 形态、稳定性、功耗与单位 token 成本。

这些硬件事实可以从 [[chip/00-project-index|芯片与基础设施资料库]] 进入，再由 [[software/concepts/accelerator-resource-model|加速器资源模型]] 把差异转换成可调度属性。

## 对 P/D 分离的意义

[[software/concepts/pd-disaggregation|Prefill / Decode 分离]] 天然适合异构化探索。Prefill 更看重计算吞吐和长上下文能力，Decode 更看重 HBM 带宽、低延迟和稳定 TPOT，因此不同阶段不一定要使用相同硬件。但跨硬件池 KV 格式、传输链路、网络和运行时兼容性可能成为新的约束。

## 对 KV Cache 的意义

[[software/concepts/kv-cache-lifecycle|KV Cache 生命周期]] 在异构环境中更复杂。不同引擎和硬件的 KV layout、dtype、block size、对齐与传输后端可能不同，所以“跨厂商透明共享 KV”通常比“同硬件池内共享 KV”更难。

## 调度原则

硬件选择应建立在实际 Benchmark 与 SLA 上，而不是单一理论 FLOPS。[[software/concepts/topology-aware-scheduling|拓扑感知调度]] 还要保证被选中的卡之间、卡与 NIC 之间、卡与 CPU memory 之间具有合适的物理距离。

## 相关节点

- [[software/concepts/llm-serving-stack|LLM Serving 软件栈]]
- [[software/concepts/accelerator-resource-model|加速器资源模型]]
- [[software/concepts/topology-aware-scheduling|拓扑感知调度]]
- [[software/concepts/pd-disaggregation|Prefill / Decode 分离]]
- [[software/concepts/kv-cache-lifecycle|KV Cache 生命周期]]

返回 [[software/README|AI Infra 软件栈地图]] 或 [[README|仓库知识图谱入口]]。
