---
title: Distributed Training
aliases:
  - Training MOC
tags:
  - moc
  - system
  - training
updated: 2026-09-25
---
# Distributed Training

Training 层把训练 workload、forward/backward、并行、内存、gradient communication 与 checkpoint/recovery 连接起来。

## 核心概念

- [[system/training/distributed-training-model|Distributed Training Model]]
- [[system/training/training-memory-model|Training Memory Model]]
- [[system/training/gradient-synchronization|Gradient Synchronization]]
- [[system/workload/training-workload|Training Workload]]

## 基础依赖

- [[system/parallelism/parallelism-overview|Parallelism Overview]]
- [[system/memory/model-memory-accounting|Model Memory Accounting]]
- [[system/communication/README|Communication Model]]

Training Memory 与 Gradient Synchronization 已建立；Checkpoint / Recovery 由 Reliability 域维护。
