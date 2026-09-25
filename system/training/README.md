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
- [[system/workload/training-workload|Training Workload]]

## 基础依赖

- [[system/parallelism/parallelism-overview|Parallelism Overview]]
- [[system/memory/model-memory-accounting|Model Memory Accounting]]
- [[system/communication/README|Communication Model]]

后续任务继续补 Training Memory、Gradient Synchronization 与 Checkpoint / Recovery。
