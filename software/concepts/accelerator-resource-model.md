---
title: 加速器资源模型
aliases:
  - Accelerator Resource Model
  - GPU NPU 资源模型
tags:
  - concept
  - resource-management
  - kubernetes
---

# 加速器资源模型

加速器资源模型回答的是：Kubernetes 和上层 AI 控制面应该如何描述、申请、分配、共享和隔离 GPU、NPU、NIC 等复杂设备。

## 核心关系

```text
Workload
  → [[software/device-resource/dra|Kubernetes DRA]] 表达设备需求
  → [[software/scheduling/kai-scheduler|KAI-Scheduler]] 做集群级 placement
  → [[software/device-resource/hami|HAMi]] 等组件完成共享、隔离或设备注入
  → 具体 GPU / NPU / NIC
```

DRA 更像标准 API 层，HAMi 更接近设备资源与虚拟化实现层，KAI-Scheduler 则负责队列、公平性、Gang、抢占和 placement。三者职责不同，但组合后才能形成完整的 AI 资源控制链路。

## 应显式建模的属性

厂商、型号、显存/HBM 容量与带宽、互联方式、NUMA、PCIe/NVLink/HCCS/RoCE 拓扑、驱动/runtime、可共享能力、健康状态，以及对 Prefill、Decode、MoE、KV Transfer 等角色的适配度。

硬件事实可继续从 [[chip/00-project-index|芯片与基础设施资料库]] 进入，调度侧关系见 [[software/concepts/topology-aware-scheduling|拓扑感知调度]]。

## 相关概念

- [[software/concepts/heterogeneous-inference|异构推理]]
- [[software/concepts/llm-serving-stack|LLM Serving 软件栈]]
- [[software/concepts/pd-disaggregation|Prefill / Decode 分离]]

返回 [[software/README|AI Infra 软件栈地图]]。
