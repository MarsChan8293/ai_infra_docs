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

## 跨层入口

- Workload：[[system/workload/README|Workload Model]]
- Communication：[[system/communication/README|Communication Model]]
- Topology：[[system/topology/README|Topology Model]]
- System Schema：[[system/SCHEMA|System Schema V0.1]]
- 实施任务：[[TASKS|Implementation Tasks]]

后续按 `PAR-001` 至 `PAR-006` 建立总览和各并行策略概念页。
