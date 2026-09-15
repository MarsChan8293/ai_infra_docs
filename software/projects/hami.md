---
schema_version: software-v0.1
name: HAMi
object_type: project
category: device-resource
organization: Project-HAMi
status: active
repo: https://github.com/Project-HAMi/HAMi
docs: https://project-hami.io/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - gpu-sharing
  - memory-isolation
  - device-plugin
  - heterogeneous-accelerators
  - topology-aware-allocation
integrations:
  - kai-scheduler
  - kubernetes-dra
backends:
  - nvidia
  - ascend
  - cambricon
  - hygon
  - iluvatar
  - metax
  - moore-threads
updated: 2026-09-15
---
# HAMi

> Kubernetes 上的异构 AI 加速器共享、隔离和设备资源管理中间件。

## 核心能力

| 能力 | 说明 |
|---|---|
| GPU/NPU Sharing | 支持比整卡更细粒度的资源分配 |
| Isolation | 对部分后端提供显存/算力约束 |
| Device Resource | 参与设备发现、分配和容器注入 |
| 异构设备 | 覆盖多厂商 GPU/NPU 路径 |

## 边界

HAMi 解决设备资源与共享，不理解 token、KV Cache 或 LLM request routing。

## 集成与后端

- [[software/projects/kai-scheduler|KAI-Scheduler]]：上层 AI workload 调度组合路径。
- [[software/projects/kubernetes-dra|Kubernetes DRA]]：通过 DRA 路线表达和分配复杂设备资源。

## 关联项目

- NVIDIA Device Plugin 路线：[[software/projects/nvidia-k8s-device-plugin|NVIDIA k8s-device-plugin]]。
- NVIDIA 节点软件生命周期：[[software/projects/nvidia-gpu-operator|NVIDIA GPU Operator]]。

## 版本快照

本页不绑定单一 release；能力判断以 2026-09-15 前官方资料为快照。

## 直接来源

- https://project-hami.io/
- https://github.com/Project-HAMi/HAMi
