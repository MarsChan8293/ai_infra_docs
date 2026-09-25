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

## 核心概念

- [[system/communication/collective-communication|Collective Communication]]
- [[system/communication/communication-cost-model|Communication Cost Model]]
- [[system/communication/all-reduce-all-gather-reduce-scatter|All-Reduce / All-Gather / Reduce-Scatter]]
- [[system/communication/all-to-all|All-to-All]]
- [[system/communication/point-to-point|Point-to-Point]]

## 跨层入口

- Parallelism：[[system/parallelism/README|Parallelism Model]]
- Topology：[[system/topology/README|Topology Model]]
- 调度：[[system/scheduling/topology-aware-scheduling|拓扑感知调度]]
- System Schema：[[system/SCHEMA|System Schema V0.1]]
- 实施任务：[[TASKS|Implementation Tasks]]

Collective、All-to-All、P2P 与统一 Cost Model 的基础口径已经建立。
