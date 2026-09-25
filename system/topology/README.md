---
title: Topology Model
aliases:
  - Topology MOC
tags:
  - moc
  - system
  - topology
updated: 2026-09-25
---
# Topology Model

Topology 层描述 Accelerator、CPU、NUMA、PCIe、NIC、Scale-up Fabric、Scale-out Fabric、Rack 与故障域之间的物理关系。

## 已有概念

- [[system/scheduling/topology-aware-scheduling|拓扑感知调度]]
- [[system/resource/accelerator-resource-model|加速器资源模型]]

## 跨层入口

- Communication：[[system/communication/README|Communication Model]]
- Memory：[[system/memory/README|Memory Model]]
- Hardware：[[chip/00-project-index|AI 芯片与基础设施资料库]]
- System Schema：[[system/SCHEMA|System Schema V0.1]]
- 实施任务：[[TASKS|Implementation Tasks]]

后续按 `TOP-001` 至 `TOP-005` 建立 Scale-up / Scale-out、Accelerator Fabric、NIC Affinity、NUMA / PCIe 与 Rack / Failure Domain。
