---
title: MoE System Architecture
aliases:
  - MoE MOC
tags:
  - moc
  - system
  - moe
updated: 2026-09-25
---
# MoE System Architecture

MoE 层把 total/active/resident parameters、routing、Expert Parallel、All-to-All 与 load balance 放进同一模型。

## 核心概念

- [[system/moe/moe-system-model|MoE System Model]]
- [[system/parallelism/expert-parallelism|Expert Parallelism]]
- [[system/communication/all-to-all|All-to-All]]

后续任务继续补 Expert Routing / Load Balance。
