---
schema_version: system-v0.1
name: 拓扑感知调度
object_type: concept
category: scheduling
updated: 2026-09-25
tags:
  - system
  - topology
  - scheduling
---
# 拓扑感知调度

> AI workload 的可用算力不仅由“有多少张卡”决定，还取决于卡、CPU、NUMA、NIC、交换网络和内存层级之间的物理关系。

## 需要建模的拓扑

```text
Workload role / parallelism
        ↓
Node / NUMA placement
        ↓
Accelerator ↔ Accelerator
        ↓
Accelerator ↔ NIC
        ↓
NIC ↔ Fabric
        ↓
Remote accelerator / memory / storage
```

关键事实包括 GPU/NPU 间互联带宽、PCIe switch 层级、NUMA 归属、NIC 亲和性、Rail、机架/故障域和跨节点 fabric。

## 调度路径

Workload placement 可以由 [KAI-Scheduler](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/kai-scheduler/KAI-Scheduler/KAI-Scheduler.md)、[Volcano](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/volcano-sh/Volcano/Volcano.md)、[Kueue](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/kubernetes-sigs/Kueue/Kueue.md) 等控制面参与；设备描述与分配可以结合 [Kubernetes DRA](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/cloud-native/Kubernetes-DRA/Kubernetes-DRA.md) 或 [HAMi](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/Project-HAMi/HAMi/HAMi.md)。

项目只是实现示例。系统层真正需要维护的是拓扑事实与 workload 约束之间的映射。

## 判断要点

- TP / EP / PP 等并行策略需要与真实互联层级匹配。
- Prefill、Decode、KV transfer、MoE all-to-all 对网络形态的敏感度不同。
- GPU 与 NIC 不同 NUMA 或跨 PCIe switch 时，标称设备性能无法代表端到端性能。
- 故障域与可维护性也属于拓扑，不应只优化最短路径。
- 调度策略必须消费真实硬件拓扑，而不是只看逻辑资源数量。

## 相关概念

- [[system/resource/accelerator-resource-model|加速器资源模型]]
- [[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层级]]
- [[system/heterogeneous-compute/heterogeneous-inference|异构推理]]
- [[chip/00-project-index|芯片与基础设施资料库]]
