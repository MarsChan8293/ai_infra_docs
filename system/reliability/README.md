---
title: Reliability Model
aliases:
  - Reliability MOC
tags:
  - moc
  - system
  - reliability
updated: 2026-09-25
---
# Reliability Model

Reliability 层描述 device、network、rack 等 failure domain，以及它们如何影响 replica、parallel group、checkpoint 与 recovery。

## 核心概念

- [[system/reliability/accelerator-and-network-failure-domain|Accelerator / Network Failure Domain]]
- [[system/reliability/checkpoint-recovery-model|Checkpoint / Recovery Model]]
- [[system/topology/rack-and-failure-domain|Rack / Failure Domain]]

Failure Domain 与 Checkpoint / Recovery 的基础可靠性模型均已建立。
