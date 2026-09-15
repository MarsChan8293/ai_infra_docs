---
schema_version: software-v0.1
name: 拓扑感知调度
object_type: concept
category: scheduling-architecture
updated: 2026-09-15
---
# 拓扑感知调度

> AI workload 的“有几张空闲卡”不等于“这些卡适合一起工作”。

## 问题

TP、EP、KV offload、P/D 分离等场景对 NUMA、PCIe、NVLink/xGMI、NIC 和跨节点网络距离高度敏感。

## 核心机制

```text
Workload placement
  [[software/projects/kai-scheduler|KAI-Scheduler]] / [[software/projects/volcano|Volcano]] / [[software/projects/kueue|Kueue]]
        ↓
Device description / allocation
  [[software/projects/kubernetes-dra|Kubernetes DRA]] / [[software/projects/hami|HAMi]]
        ↓
Device software
  [[software/projects/nvidia-gpu-operator|NVIDIA GPU Operator]] / [[software/projects/nvidia-k8s-device-plugin|NVIDIA Device Plugin]]
        ↓
NUMA / PCIe / NVLink / xGMI / NIC
        ↑
Communication
  [[software/projects/nccl|NCCL]] / [[software/projects/rccl|RCCL]] / [[software/projects/ucx|UCX]] / [[software/projects/nixl|NIXL]]
```

## 判断要点

- TP/EP worker 应优先落在高带宽互联域。
- CPU/KV offload 要关注 GPU 与本地 NUMA memory。
- P/D 分离要同时考虑 GPU 与 NIC 距离。
- 调度策略必须基于真实硬件拓扑，而非只看逻辑资源数量。

## 相关项目与概念

- [[software/concepts/accelerator-resource-model|加速器资源模型]]
- [[software/concepts/pd-disaggregation|Prefill / Decode 分离]]
- [[software/concepts/heterogeneous-inference|异构推理]]
