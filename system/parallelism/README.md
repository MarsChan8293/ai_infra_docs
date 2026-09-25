---
title: Parallelism Model
aliases:
  - Parallelism MOC
tags:
  - moc
  - system
  - parallelism
updated: 2026-09-25
---
# Parallelism Model

Parallelism 层描述 DP、TP、PP、EP、CP 如何切分计算与状态，以及每种切分引入的通信、同步和拓扑约束。

## 核心概念

- [[system/parallelism/parallelism-overview|Parallelism Overview]]
- [[system/parallelism/tensor-parallelism|Tensor Parallelism]]
- [[system/parallelism/pipeline-parallelism|Pipeline Parallelism]]
- [[system/parallelism/expert-parallelism|Expert Parallelism]]
- [[system/parallelism/data-parallelism|Data Parallelism]]
- [[system/parallelism/context-parallelism|Context Parallelism]]

## 跨层入口

- Workload：[[system/workload/README|Workload Model]]
- Compute：[[system/compute/README|Compute Model]]
- Memory：[[system/memory/README|Memory Model]]
- Communication：[[system/communication/README|Communication Model]]
- Topology：[[system/topology/README|Topology Model]]
- System Schema：[[system/SCHEMA|System Schema V0.1]]
- 实施任务：[[TASKS|Implementation Tasks]]

TP、PP、EP、DP、CP 的基础切分、通信与拓扑口径均已建立。
