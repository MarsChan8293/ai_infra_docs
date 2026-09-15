---
schema_version: software-v0.1
name: KAI-Scheduler
object_type: project
category: scheduler
organization: kai-scheduler
status: active
repo: https://github.com/kai-scheduler/KAI-Scheduler
docs: https://github.com/kai-scheduler/KAI-Scheduler/tree/main/docs
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - queue-quota
  - fair-share
  - gang-scheduling
  - preemption
  - gpu-sharing
  - topology-aware-scheduling
integrations:
  - hami
  - kubernetes-dra
backends: []
updated: 2026-09-15
---
# KAI-Scheduler

> 面向 AI / GPU 工作负载的 Kubernetes 集群调度器。

## 核心能力

| 能力 | 说明 |
|---|---|
| Queue / Quota | 多团队资源治理与配额 |
| Fair-share | 在共享集群中分配空闲资源并维持公平性 |
| Gang Scheduling | 一组 Pod 满足条件后共同调度 |
| Priority / Preemption | 优先级与资源回收 |
| GPU Sharing | 支持部分 GPU 资源的调度语义 |
| Topology-aware Placement | 把设备拓扑纳入 placement |

## 边界

KAI-Scheduler 做 Pod / Job 级 placement，不做 LLM request 级路由，也不负责模型执行。GPU sharing 的运行时隔离能力需要 HAMi、MIG、MPS 或其他设备层机制配合。

拓扑问题见 [[software/concepts/topology-aware-scheduling|拓扑感知调度]]。

## 集成与后端

- HAMi：设备共享、隔离和异构资源管理。
- Kubernetes DRA：结构化设备声明和动态资源分配。
- KAI 是调度策略层，因此 V0.1 不把具体 GPU/NPU 厂商直接写进 `backends`。

## 版本快照

当前页未固定 release 或 commit；能力以 2026-09-15 的仓库资料为快照。

## 直接来源

- https://github.com/kai-scheduler/KAI-Scheduler
- https://github.com/kai-scheduler/KAI-Scheduler/tree/main/docs/queues
- https://github.com/Project-HAMi/HAMi
- https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/
