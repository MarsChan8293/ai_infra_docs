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

## 核心概念

- [[system/memory/model-memory-accounting|Model Memory Accounting]]
- [[system/memory/weight-memory|Weight Memory Model]]
- [[system/memory/activation-memory|Activation Memory Model]]
- [[system/memory/memory-bandwidth-model|Memory Bandwidth Model]]
- [[system/memory/kv-cache-model|KV Cache Model]]
- [[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层级]]
- [[system/memory/cxl-and-memory-pooling|CXL / Memory Pooling]]

## 跨层入口

- 上游：[[system/workload/README|Workload Model]]
- 计算：[[system/compute/README|Compute Model]]
- 通信：[[system/communication/README|Communication Model]]
- 并行：[[system/parallelism/README|Parallelism Model]]
- 拓扑：[[system/topology/README|Topology Model]]
- System Schema：[[system/SCHEMA|System Schema V0.1]]
- 实施任务：[[TASKS|Implementation Tasks]]

Memory Foundation 的容量、带宽、Weight、Activation、KV 与 pooled-memory 基础口径均已建立。
