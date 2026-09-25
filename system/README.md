---
title: AI Infra System Architecture
aliases:
  - System MOC
  - AI Infra 系统架构
tags:
  - moc
  - system
  - ai-infra
updated: 2026-09-25
---
# AI Infra 系统架构

`system/` 是模型需求与硬件能力之间的桥梁层。这里不维护软件项目数据库，而是把 **Model facts + Workload** 映射成计算、内存、通信、并行、拓扑、调度和可靠性等系统约束。

软件项目、社区、能力和集成关系的 canonical 记录维护在 [ai_infra_relationship](https://github.com/MarsChan8293/ai_infra_relationship)。本仓库只在系统概念需要举例时直接链接对应 canonical 页面，不维护项目级版本、能力矩阵、组织或集成事实的第二份副本。

## 建模主线

```text
Model intrinsic facts
        ↓
Workload
        ↓
Compute / Memory
        ↓
Parallelism / Communication
        ↓
Topology / Scheduling
        ↓
Hardware capability
```

## System Foundation

- [[system/workload/README|Workload Model]]
- [[system/compute/README|Compute Model]]
- [[system/memory/README|Memory Model]]
- [[system/parallelism/README|Parallelism Model]]
- [[system/communication/README|Communication Model]]
- [[system/topology/README|Topology Model]]

这些 MOC 是领域入口。尚未落库的具体概念只记录在 [[TASKS|Implementation Tasks]]，不提前创建虚假 Wiki Link。

## 已有核心概念

- [[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层级]]
- [[system/resource/accelerator-resource-model|加速器资源模型]]
- [[system/scheduling/topology-aware-scheduling|拓扑感知调度]]
- [[system/heterogeneous-compute/heterogeneous-inference|异构推理]]

## 集成案例

- [[system/examples/model-to-hardware-walkthrough|Qwen3.8-27B → MI300X 单卡 Decode Walkthrough]]

这个案例用于检查 Model → Workload → Compute / Memory / Communication / Topology → Hardware 是否真正可追溯；它不是硬件推荐或 benchmark。

## Schema 与实施

- [[system/SCHEMA|System Schema V0.1]]
- [[TASKS|实施任务与进度跟踪]]
- [[ROADMAP|AI Infra Docs Roadmap]]

System Concept 必须声明 inputs、constraints、outputs、assumptions、related_layers 和 evidence。外部事实需要直接 Evidence；第一性原理推导必须把输入和假设显式写出来。

## 跨层入口

- 上游模型：[[models/00-model-index|AI Model Index]]
- 下游硬件：[[chip/00-project-index|AI 芯片与基础设施资料库]]
- 全仓入口：[[00-ai-infra-map|AI Infra 知识图谱入口]]

## 建模边界

System 页面回答“为什么这些模型和 workload 特征会形成这样的硬件与系统约束”。项目级软件事实、版本兼容矩阵、维护者、组织关系和项目间集成不在本目录重复维护。

一个系统结论应尽量保持以下可追溯链：

```text
Source facts
   ↓
Explicit assumptions
   ↓
System mechanism / formula
   ↓
Derived requirement
   ↓
Hardware capability
```
