---
schema_version: system-v0.1
name: 加速器资源模型
object_type: concept
category: resource-management
updated: 2026-09-25
---

# 加速器资源模型

> 描述 AI 控制面如何把 GPU、NPU、NIC 与其真实硬件属性表达成可查询、可分配、可隔离的资源。

## 为什么不能只有“1 张卡”

简单的 `vendor.com/gpu: 1` 无法完整表达型号、HBM 容量、互联、NUMA、共享能力、健康状态、驱动 / runtime 约束，也无法表达 GPU + NIC 或多卡拓扑组合。

## 应显式建模的硬件事实

- 厂商、架构与具体型号。
- HBM / 显存容量与可用容量。
- PCIe、NVLink / NVSwitch、XGMI、片间互联与 NIC 邻接关系。
- NUMA / CPU socket / root complex。
- 支持的数据类型、共享 / 分片能力与隔离边界。
- 驱动、固件、runtime 与健康状态。
- workload role suitability，例如 Prefill、Decode、训练或通信密集任务。

统一资源入口不等于抹平硬件差异，而是把差异变成可查询、可调度的数据。

## 软件实现参照

- [Kubernetes DRA](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/cloud-native/Kubernetes-DRA/Kubernetes-DRA.md)
- [HAMi](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/Project-HAMi/HAMi/HAMi.md)
- [NVIDIA k8s-device-plugin](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/NVIDIA/k8s-device-plugin/NVIDIA-k8s-device-plugin.md)
- [NVIDIA GPU Operator](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/NVIDIA/GPU-Operator/NVIDIA-GPU-Operator.md)

## 相关节点

- [[system/topology/topology-aware-scheduling|拓扑感知调度]]
- [[system/heterogeneous-compute/heterogeneous-inference|异构推理]]
- [[chip/00-project-index|芯片与基础设施资料库]]
