---
schema_version: software-v0.1
name: 拓扑感知调度
object_type: concept
category: scheduling
updated: 2026-09-15
---
# 拓扑感知调度

> AI workload 的“若干张空闲卡”不等价于“若干张适合一起工作的卡”。

## 问题

TP、EP、KV offload 和 P/D 分离都会受 CPU NUMA、PCIe Root/Switch、NVLink/NVSwitch、RDMA NIC 和跨节点网络距离影响。

## 核心机制

```text
[[software/projects/kai-scheduler|KAI-Scheduler]] 负责 placement
        ↓
[[software/projects/kubernetes-dra|DRA]] / [[software/projects/hami|HAMi]] 表达与分配设备
        ↓
NUMA / PCIe / NVLink / NIC / GPU / NPU
```

## 判断要点

- TP/EP 优先关注设备间高速互联。
- CPU/KV offload 关注 GPU 与本地 NUMA memory。
- P/D 分离还要关注 Prefill / Decode 池之间的网络带宽和尾延迟。
- 具体硬件拓扑事实应回到 [[chip/00-project-index|芯片与硬件资料库]] 核对。

## 相关项目与概念

- [[software/projects/kai-scheduler|KAI-Scheduler]]
- [[software/projects/kubernetes-dra|Kubernetes DRA]]
- [[software/projects/hami|HAMi]]
- [[software/concepts/accelerator-resource-model|加速器资源模型]]
