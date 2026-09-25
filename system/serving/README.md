---
title: Serving Architecture
aliases:
  - Serving MOC
tags:
  - moc
  - system
  - serving
updated: 2026-09-25
---
# Serving Architecture

Serving 层把 [[system/workload/inference-workload|Inference Workload]] 映射到请求生命周期、Prefill/Decode、KV、batch、queue 和 SLA。

## 核心概念

- [[system/serving/llm-serving-model|LLM Serving Model]]

## 基础依赖

- [[system/compute/prefill-vs-decode|Prefill vs Decode]]
- [[system/memory/kv-cache-model|KV Cache Model]]
- [[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层级]]
- [[system/topology/README|Topology Model]]

后续任务继续补 Continuous Batching、Prefix Caching、P/D Disaggregation 与 KV Transfer。
