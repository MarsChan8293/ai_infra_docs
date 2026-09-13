---
title: LLM Serving 软件栈
aliases:
  - LLM Serving Stack
  - LLM 推理软件栈
tags:
  - concept
  - serving
  - ai-infra
---

# LLM Serving 软件栈

这是软件目录的核心概念节点，用来把“请求级编排、推理执行、KV Cache、集群调度、设备资源”串成一张关系图。

## 分层关系

```text
请求 / API
  ↓
[[software/distributed-serving/llm-d|llm-d]]
  ↓
[[software/inference-engine/vllm|vLLM]]
  ↕
[[software/kv-cache/lmcache|LMCache]]
  ↓
[[software/scheduling/kai-scheduler|KAI-Scheduler]]
  ↓
[[software/device-resource/dra|Kubernetes DRA]] / [[software/device-resource/hami|HAMi]]
  ↓
GPU / NPU / NIC / Memory
```

这里最重要的是区分两类“调度”：[[software/distributed-serving/llm-d|llm-d]] 面向请求级路由，理解 prefix、KV 与 P/D 阶段；[[software/scheduling/kai-scheduler|KAI-Scheduler]] 面向 Pod/Job placement，理解队列、配额、Gang、拓扑和设备资源。二者是上下两级控制面，不是替代关系。

## 关键横向机制

- [[software/concepts/pd-disaggregation|Prefill / Decode 分离]]：跨越 serving、推理引擎、KV 传输和底层网络。
- [[software/concepts/kv-cache-lifecycle|KV Cache 生命周期]]：跨越 vLLM、LMCache、路由和存储。
- [[software/concepts/topology-aware-scheduling|拓扑感知调度]]：把 NUMA、PCIe、NVLink、NIC 距离映射到 placement。
- [[software/concepts/accelerator-resource-model|加速器资源模型]]：把 GPU/NPU 属性、共享和 claim 纳入 Kubernetes。
- [[software/concepts/heterogeneous-inference|异构推理]]：把模型画像、Benchmark、SLA 与硬件差异连接起来。

## 入口

返回 [[software/README|AI Infra 软件栈地图]]，或回到 [[00-ai-infra-map|AI Infra 知识图谱入口]]。
