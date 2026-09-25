---
schema_version: system-v0.1
name: 拓扑感知调度
object_type: concept
category: topology-scheduling
updated: 2026-09-25
---

# 拓扑感知调度

> AI workload 的“有几张卡”只是第一层问题，更重要的是这些卡、CPU、NIC 和内存之间如何连接。

## 拓扑层级

```text
Workload
  ↓
GPU / NPU group
  ↓
on-board / NVLink / XGMI / PCIe topology
  ↓
CPU socket / NUMA / PCIe root complex
  ↓
NIC / fabric
  ↓
rack / cluster
```

同样数量的加速器，如果跨 NUMA、跨 PCIe root complex 或跨节点，实际通信路径和可用带宽可能完全不同。调度策略因此需要消费真实硬件拓扑，而不是只统计逻辑设备数量。

## 调度关注点

- Tensor / Pipeline / Expert Parallel 的通信边应尽量贴合高带宽互联。
- NIC 与 accelerator 的 PCIe / NUMA 亲和性会影响 RDMA 和跨节点通信。
- P/D 分离、KV 迁移和远端内存访问需要把数据路径纳入 placement。
- 故障域、热设计与共享资源会影响“拓扑最优”是否等于“系统最优”。

## 软件实现参照

- [KAI-Scheduler](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/kai-scheduler/KAI-Scheduler/KAI-Scheduler.md)
- [Volcano](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/volcano-sh/Volcano/Volcano.md)
- [Kueue](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/kubernetes-sigs/Kueue/Kueue.md)
- [Kubernetes DRA](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/cloud-native/Kubernetes-DRA/Kubernetes-DRA.md)
- [HAMi](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/Project-HAMi/HAMi/HAMi.md)

## 相关节点

- [[system/resource/accelerator-resource-model|加速器资源模型]]
- [[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层次]]
- [[system/heterogeneous-compute/heterogeneous-inference|异构推理]]
- [[chip/00-project-index|芯片与基础设施资料库]]
