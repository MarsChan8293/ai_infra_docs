---
title: AI Infra System Architecture
aliases:
  - System MOC
  - AI Infra 系统架构
tags:
  - moc
  - system
  - ai-infra
---

# AI Infra System Architecture

`system/` 是模型与芯片之间的桥接层。这里不维护软件项目事实，而是解释稳定的、面向硬件的系统机制：状态放在哪里、设备如何表达、任务如何贴合拓扑、不同加速器如何组合。

## 核心主题

- [[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层次]]：HBM、主机内存、远端内存与 NVMe 之间的容量、带宽、延迟与耐久度权衡。
- [[system/resource/accelerator-resource-model|加速器资源模型]]：如何表达 GPU / NPU / NIC 的型号、显存、拓扑、共享能力与健康状态。
- [[system/topology/topology-aware-scheduling|拓扑感知调度]]：如何把 workload 放到正确的 NUMA、PCIe、NVLink / XGMI、NIC 与节点位置。
- [[system/heterogeneous-compute/heterogeneous-inference|异构推理]]：如何把模型需求映射到不同 GPU / NPU、精度、内存与通信能力。

## 边界

软件项目本身的 canonical 事实由 [ai_infra_relationship](https://github.com/MarsChan8293/ai_infra_relationship) 维护。本目录只在需要说明系统机制时引用软件项目，不复制其版本、维护者、集成关系或能力清单。

## 阅读路径

推荐从 [[models/00-model-index|模型]] 出发，先判断参数、KV / recurrent state、精度和通信模式，再通过本目录理解系统约束，最后进入 [[chip/00-project-index|芯片与基础设施资料库]] 查硬件实现。
