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
  - accelerator-sharing
  - device-isolation
  - device-plugin
  - topology-aware-allocation
  - heterogeneous-device-management
integrations:
  - kubernetes-dra
  - kai-scheduler
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
| Accelerator Sharing | 允许多个 workload 更细粒度共享设备 |
| Device Isolation | 在具体后端能力允许的范围内限制显存 / 算力使用 |
| Device Plugin | 向 Kubernetes 暴露和分配设备 |
| Topology-aware Allocation | 在分配时考虑设备与节点拓扑 |
| Heterogeneous Devices | 面向多个 GPU / NPU 厂商提供管理路径 |

## 边界

HAMi 解决“设备如何暴露、共享、隔离、分配给容器”，不理解 token、KV Cache 或 P/D 请求流。共享调度与运行时硬隔离也不是同一件事，隔离强度必须按具体后端验证。

资源模型见 [[software/concepts/accelerator-resource-model|加速器资源模型]]。

## 集成与后端

- Kubernetes DRA：动态资源声明与分配模型。
- KAI-Scheduler：上层队列、Gang、抢占与 placement。
- 当前资料记录 NVIDIA、Ascend、Cambricon、Hygon、Iluvatar、MetaX、Moore Threads 等支持路径；不同后端能力粒度不应默认相同。

## 版本快照

当前页未绑定 release 或 commit。后端列表和能力以 2026-09-15 的现有项目资料为快照，后续应随官方支持矩阵更新。

## 直接来源

- https://github.com/Project-HAMi/HAMi
- https://project-hami.io/
- https://github.com/Project-HAMi/HAMi-dra
- https://github.com/Project-HAMi/KAI-resource-isolator
