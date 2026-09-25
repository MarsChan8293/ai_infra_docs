---
title: AI Infra System Architecture
aliases:
  - System MOC
  - AI Infra 系统架构
tags:
  - moc
  - system
  - ai-infra
---
# AI Infra 系统架构

`system/` 是模型需求与芯片能力之间的桥梁层。这里不维护软件项目数据库，而是解释 AI workload 如何映射到内存层级、设备资源、拓扑和异构计算等系统约束。

软件项目、社区、能力和集成关系的 canonical 记录维护在 [ai_infra_relationship](https://github.com/MarsChan8293/ai_infra_relationship)。本仓库只在系统概念需要举例时直接链接对应 canonical 页面，不再维护 `software/` redirect 层。

## 核心概念

- [[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层级]]
- [[system/resource/accelerator-resource-model|加速器资源模型]]
- [[system/scheduling/topology-aware-scheduling|拓扑感知调度]]
- [[system/heterogeneous-compute/heterogeneous-inference|异构推理]]

## 跨层入口

- 上游 workload：[[models/00-model-index|AI Model Index]]
- 下游硬件：[[chip/00-project-index|AI 芯片与基础设施资料库]]
- 全仓入口：[[00-ai-infra-map|AI Infra 知识图谱入口]]

## 建模边界

系统概念回答“为什么这些模型特征会形成这样的硬件与系统约束”。项目级软件事实、版本兼容矩阵、维护者、组织关系和项目间集成不在本目录重复维护。

推荐关系主线：

```text
Model / Workload
      ↓
System Constraint
  ├─ Memory hierarchy
  ├─ Resource model
  ├─ Topology / placement
  └─ Heterogeneous execution
      ↓
Chip / Memory / Interconnect
```
