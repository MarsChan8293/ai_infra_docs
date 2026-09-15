---
schema_version: software-v0.1
name: Kubernetes DRA
object_type: project
category: device-resource
organization: Kubernetes
status: active
repo: https://github.com/kubernetes/kubernetes
docs: https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - resource-claim
  - device-class
  - resource-slice
  - structured-device-allocation
integrations:
  - hami
  - kai-scheduler
  - nvidia-gpu-operator
backends:
  - kubernetes
updated: 2026-09-15
---
# Kubernetes DRA

> Kubernetes Dynamic Resource Allocation，面向复杂设备的标准资源声明和分配框架。

## 核心能力

| 能力 | 说明 |
|---|---|
| ResourceClaim | 由 workload 声明设备需求 |
| DeviceClass | 定义可申请设备类别与选择逻辑 |
| ResourceSlice | 由 driver 发布设备及属性 |
| Structured Allocation | 把复杂设备属性纳入调度与分配 |

## 边界

DRA 是 Kubernetes 资源 API 与分配框架，不执行 GPU kernel、设备虚拟化或 LLM serving。

## 集成与后端

- [[software/projects/hami|HAMi]]：异构设备与共享能力可进入 DRA 路线。
- [[software/projects/kai-scheduler|KAI-Scheduler]]：调度器可利用结构化设备资源信息。
- [[software/projects/nvidia-gpu-operator|NVIDIA GPU Operator]]：其 GPUCluster 路线使用 DRA 进行 GPU 分配。

## 关联项目

- 传统 Device Plugin 路线：[[software/projects/nvidia-k8s-device-plugin|NVIDIA k8s-device-plugin]]。

## 版本快照

本页不绑定单一 Kubernetes release；能力判断以 2026-09-15 前官方文档为快照。

## 直接来源

- https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/
- https://github.com/kubernetes/kubernetes
