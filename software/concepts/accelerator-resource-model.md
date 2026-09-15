---
schema_version: software-v0.1
name: 加速器资源模型
object_type: concept
category: resource-management
updated: 2026-09-15
---
# 加速器资源模型

> 描述、申请、分配、共享和隔离 GPU、NPU、NIC 等复杂设备的统一思考框架。

## 问题

简单的 `gpu: 1` 无法表达型号、显存、拓扑、共享能力、健康状态和组合资源需求，异构 AI 集群因此需要更丰富的资源模型。

## 核心机制

```text
Workload
  → [[software/projects/kubernetes-dra|Kubernetes DRA]] 表达设备需求
  → [[software/projects/kai-scheduler|KAI-Scheduler]] 做 placement
  → [[software/projects/hami|HAMi]] 等组件负责共享 / 隔离 / 注入
  → GPU / NPU / NIC
```

## 判断要点

至少应显式保留厂商、型号、容量、互联、NUMA/PCIe/NVLink/RoCE 拓扑、驱动/runtime、共享能力和健康状态。统一资源入口不应把硬件差异抹掉，而应把差异变成可调度属性。

## 相关项目与概念

- [[software/projects/kubernetes-dra|Kubernetes DRA]]
- [[software/projects/kai-scheduler|KAI-Scheduler]]
- [[software/projects/hami|HAMi]]
- [[software/concepts/heterogeneous-inference|异构推理]]
