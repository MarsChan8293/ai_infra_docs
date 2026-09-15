---
schema_version: software-v0.1
name: 加速器资源模型
object_type: concept
category: resource-management
updated: 2026-09-15
---
# 加速器资源模型

> 描述 Kubernetes 和 AI 控制面如何表达、申请、分配、共享和隔离 GPU、NPU、NIC 等设备。

## 问题

简单的 `vendor.com/gpu: 1` 无法表达型号、显存、拓扑、共享能力、健康状态或 GPU+NIC 组合需求。

## 核心机制

- [[software/projects/kubernetes-dra|Kubernetes DRA]]：标准化复杂设备的声明与结构化分配。
- [[software/projects/hami|HAMi]]：设备共享、隔离与多厂商资源管理。
- [[software/projects/nvidia-k8s-device-plugin|NVIDIA k8s-device-plugin]]：传统 Device Plugin 路线。
- [[software/projects/nvidia-gpu-operator|NVIDIA GPU Operator]]：GPU 节点驱动、runtime、device plugin、监控组件生命周期。
- [[software/projects/kai-scheduler|KAI-Scheduler]]：利用设备事实进行 AI workload placement。

## 判断要点

应显式建模厂商、型号、显存/HBM、互联、NUMA、驱动/runtime、健康状态、共享能力以及 workload role suitability。

统一资源入口不等于抹平硬件差异，而是把差异变成可查询、可调度的数据。

## 相关项目与概念

- [[software/concepts/topology-aware-scheduling|拓扑感知调度]]
- [[software/concepts/heterogeneous-inference|异构推理]]
- [[chip/00-project-index|芯片与基础设施资料库]]
