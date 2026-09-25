---
title: Workload Model
aliases:
  - Workload MOC
  - AI Workload
tags:
  - moc
  - system
  - workload
updated: 2026-09-25
---
# Workload Model

Workload 层描述“模型在什么运行条件下被执行”，把模型固有事实与 batch、并发、序列长度、SLA、训练批次等运行条件分开。

## 核心概念

- [[system/workload/ai-workload-model|AI Workload Model]]
- [[system/workload/inference-workload|Inference Workload]]
- [[system/workload/training-workload|Training Workload]]
- [[system/workload/workload-profile-v0.1|Workload Profile V0.1]]

## 边界

- Model facts：[[models/00-model-index|AI Model Index]]
- System Schema：[[system/SCHEMA|System Schema V0.1]]
- 实施任务：[[TASKS|Implementation Tasks]]

Inference 与 Training 的基础 workload 口径均已建立。只有真实概念页落库后才加入 Wiki Link。
