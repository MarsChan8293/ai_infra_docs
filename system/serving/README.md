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
- [[system/serving/continuous-batching|Continuous Batching]]
- [[system/serving/prefix-caching|Prefix Caching]]
- [[system/serving/disaggregated-prefill-decode|Disaggregated Prefill / Decode]]
- [[system/serving/kv-transfer|KV Transfer]]

## 基础依赖

- [[system/compute/prefill-vs-decode|Prefill vs Decode]]
- [[system/memory/kv-cache-model|KV Cache Model]]
- [[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层级]]
- [[system/topology/README|Topology Model]]

Serving 的请求调度、Prefix Cache、P/D 分离与 KV Transfer 基础模型均已建立。
