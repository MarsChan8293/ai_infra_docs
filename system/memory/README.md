---
title: Memory Model
aliases:
  - Memory MOC
tags:
  - moc
  - system
  - memory
updated: 2026-09-25
---
# Memory Model

Memory 层描述权重、KV、Activation、Workspace、通信 buffer 与内存层级如何形成容量、带宽、时延和耐久度约束。

## 已有概念

- [[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层级]]

## 跨层入口

- 上游：[[system/workload/README|Workload Model]]
- 计算：[[system/compute/README|Compute Model]]
- 拓扑：[[system/topology/README|Topology Model]]
- System Schema：[[system/SCHEMA|System Schema V0.1]]
- 实施任务：[[TASKS|Implementation Tasks]]

后续按 `MEM-001` 至 `MEM-006` 补齐 Memory Accounting、Weight、Activation、KV、Bandwidth 与 CXL / Memory Pooling。
