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
- [[system/moe/expert-routing-and-load-balance|Expert Routing / Load Balance]]
- [[system/parallelism/expert-parallelism|Expert Parallelism]]
- [[system/communication/all-to-all|All-to-All]]

MoE 的参数、Expert Parallel、All-to-All、Routing 与 Load Balance 基础模型均已建立。
