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

Compute 层负责把模型结构与 workload 转换为计算量、Arithmetic Intensity 和 compute-bound / memory-bound 等系统判断。

## 边界

- 上游：[[system/workload/README|Workload Model]]
- 内存约束：[[system/memory/README|Memory Model]]
- System Schema：[[system/SCHEMA|System Schema V0.1]]
- 实施任务：[[TASKS|Implementation Tasks]]

本目录将按 `CMP-001` 至 `CMP-003` 建立 Transformer Compute、Roofline / Arithmetic Intensity 与 Prefill vs Decode 模型。
