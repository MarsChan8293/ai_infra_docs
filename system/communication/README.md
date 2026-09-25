---
title: Communication Model
aliases:
  - Communication MOC
tags:
  - moc
  - system
  - communication
updated: 2026-09-25
---
# Communication Model

Communication 层把 message size、participant、collective algorithm、链路带宽、时延与同步转换为通信成本。

## 跨层入口

- Parallelism：[[system/parallelism/README|Parallelism Model]]
- Topology：[[system/topology/README|Topology Model]]
- 现有调度概念：[[system/scheduling/topology-aware-scheduling|拓扑感知调度]]
- System Schema：[[system/SCHEMA|System Schema V0.1]]
- 实施任务：[[TASKS|Implementation Tasks]]

后续按 `COM-001` 至 `COM-005` 建立 Collective、All-Reduce/All-Gather/Reduce-Scatter、All-to-All、P2P 和统一 Cost Model。
