---
schema_version: system-v0.1
name: 加速器资源模型
object_type: concept
category: resource-management
inputs:
  - hardware.accelerator.capability
  - hardware.memory
  - hardware.interconnect
  - hardware.health
  - workload.role
constraints:
  - resource-capacity
  - topology
  - runtime-compatibility
  - sharing-isolation
  - health-state
outputs:
  - allocatable_resource_model
  - placement_attributes
  - role_suitability
assumptions:
  - 静态硬件能力、动态健康状态与 workload suitability 分开表达
related_layers:
  - workload
  - memory
  - topology
  - scheduling
  - accelerator
  - network
evidence: {}
updated: 2026-09-25
tags:
  - system
  - accelerator
  - resource-management
---
# 加速器资源模型

> 加速器资源模型描述控制面如何表达、申请、分配、共享和隔离 GPU、NPU、NIC 与相关内存/互联资源。核心不是把硬件差异抹平，而是把差异变成可查询、可调度的数据。

## 为什么简单计数不够

类似 `vendor.com/gpu: 1` 的逻辑资源只能表达数量，无法完整表达：

- 厂商、型号和代际
- HBM / device memory 容量与带宽
- PCIe / CXL / NVLink / 专有互联拓扑
- NUMA 与 CPU / NIC 亲和性
- 驱动、固件和 runtime 约束
- 健康状态、故障域与热插拔能力
- MIG / vGPU / time-slicing 等共享与隔离能力
- workload role suitability，例如 Prefill、Decode、训练或通信密集型角色

## 控制面示例

- [Kubernetes DRA](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/cloud-native/Kubernetes-DRA/Kubernetes-DRA.md)：复杂设备的声明与结构化分配。
- [HAMi](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/Project-HAMi/HAMi/HAMi.md)：设备共享、隔离与多厂商资源管理。
- [NVIDIA k8s-device-plugin](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/NVIDIA/k8s-device-plugin/NVIDIA-k8s-device-plugin.md)：传统 Device Plugin 路线。
- [NVIDIA GPU Operator](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/NVIDIA/GPU-Operator/NVIDIA-GPU-Operator.md)：GPU 节点驱动、runtime、device plugin 与监控组件生命周期。
- [KAI-Scheduler](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/kai-scheduler/KAI-Scheduler/KAI-Scheduler.md)：消费设备事实进行 AI workload placement。

这些链接用于举例，项目事实本身不在本仓库重复维护。

## 建模原则

资源模型应该把“硬件是什么”“当前能否使用”“适合承担什么角色”分开表达。型号和显存属于静态能力，健康状态属于动态事实，Prefill/Decode suitability 则属于 workload 与系统策略共同决定的派生属性。

## 相关概念

- [[system/scheduling/topology-aware-scheduling|拓扑感知调度]]
- [[system/heterogeneous-compute/heterogeneous-inference|异构推理]]
- [[chip/00-project-index|芯片与基础设施资料库]]
