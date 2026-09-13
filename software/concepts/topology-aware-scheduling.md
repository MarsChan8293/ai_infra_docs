---
title: 拓扑感知调度
aliases:
  - Topology-aware Scheduling
  - AI 拓扑调度
tags:
  - concept
  - scheduling
  - topology
---

# 拓扑感知调度

AI workload 的“8 张空闲卡”并不等价于“8 张适合一起工作的卡”。拓扑感知调度要把 CPU NUMA、PCIe Root/Switch、NVLink/NVSwitch、RDMA NIC、跨节点网络等距离纳入 placement。

## 典型关系

```text
[[software/scheduling/kai-scheduler|KAI-Scheduler]]：决定 Pod / Job 放置
        ↓
[[software/device-resource/dra|Kubernetes DRA]] / [[software/device-resource/hami|HAMi]]：表达、分配和隔离设备
        ↓
NUMA / PCIe / NVLink / NIC / GPU / NPU
        ↑
[[software/inference-engine/vllm|vLLM]] 的 TP / EP / KV offload 性能
```

## 推理场景

TP 多卡通常希望落在同一高速互联域；MoE EP 要减少 All-to-All 慢链路；CPU/KV offload 要关注 GPU 与本地 NUMA memory；[[software/concepts/pd-disaggregation|P/D 分离]] 还要求 Prefill 与 Decode 池之间有足够的网络带宽和较低尾延迟。

拓扑策略应和具体硬件事实一起评估，可从 [[chip/00-project-index|芯片与基础设施资料库]] 进入厂商和产品页面，而不是只根据抽象 GPU 数量做判断。

## 相关概念

- [[software/concepts/accelerator-resource-model|加速器资源模型]]
- [[software/concepts/heterogeneous-inference|异构推理]]
- [[software/concepts/llm-serving-stack|LLM Serving 软件栈]]

返回 [[software/README|AI Infra 软件栈地图]]。
