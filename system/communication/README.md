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

## 跨层入口

- Parallelism：[[system/parallelism/README|Parallelism Model]]
- Topology：[[system/topology/README|Topology Model]]
- 调度：[[system/scheduling/topology-aware-scheduling|拓扑感知调度]]
- System Schema：[[system/SCHEMA|System Schema V0.1]]
- 实施任务：[[TASKS|Implementation Tasks]]

后续按 `COM-002` 至 `COM-005` 建立具体 collective、P2P 和统一 Communication Cost Model。
