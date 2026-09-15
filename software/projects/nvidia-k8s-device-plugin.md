---
schema_version: software-v0.1
name: NVIDIA k8s-device-plugin
object_type: project
category: device-resource
organization: NVIDIA
status: active
repo: https://github.com/NVIDIA/k8s-device-plugin
docs: https://github.com/NVIDIA/k8s-device-plugin
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - kubernetes-device-plugin
  - gpu-discovery
  - gpu-health
  - time-slicing
  - mps
integrations:
  - nvidia-gpu-operator
backends:
  - nvidia
  - kubernetes
updated: 2026-09-15
---
# NVIDIA k8s-device-plugin

> NVIDIA 官方 Kubernetes Device Plugin，用于向 kubelet 暴露并分配 GPU 资源。

## 核心能力

| 能力 | 说明 |
|---|---|
| GPU Discovery | 向 Kubernetes 报告节点 GPU |
| Allocate | 把选定设备注入容器 |
| Health | 跟踪 GPU 可用状态 |
| Sharing | 支持 time-slicing、MPS 等共享配置 |

## 边界

该项目负责 Kubernetes device plugin 语义，不承担完整驱动生命周期、Job 调度或 LLM serving。

## 集成与后端

- [[software/projects/nvidia-gpu-operator|NVIDIA GPU Operator]]：常由 Operator 管理和部署。

## 关联项目

- 结构化设备分配：[[software/projects/kubernetes-dra|Kubernetes DRA]]。
- 异构共享设备层：[[software/projects/hami|HAMi]]。

## 版本快照

本页不绑定单一 release；能力判断以 2026-09-15 前官方仓库为快照。

## 直接来源

- https://github.com/NVIDIA/k8s-device-plugin
