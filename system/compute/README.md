---
title: Compute Model
aliases:
  - Compute MOC
tags:
  - moc
  - system
  - compute
updated: 2026-09-25
---
# Compute Model

Compute 层负责把模型结构与 workload 转换为数学计算量、Arithmetic Intensity 和 compute-bound / memory-bound 等系统判断。

## 核心概念

- [[system/compute/transformer-compute-model|Transformer Compute Model]]

## 边界

- 上游：[[system/workload/README|Workload Model]]
- 内存约束：[[system/memory/README|Memory Model]]
- 并行：[[system/parallelism/README|Parallelism Model]]
- 通信：[[system/communication/README|Communication Model]]
- System Schema：[[system/SCHEMA|System Schema V0.1]]
- 实施任务：[[TASKS|Implementation Tasks]]

下一步按 `CMP-002`、`CMP-003` 建立 Roofline / Arithmetic Intensity 与 Prefill vs Decode。
