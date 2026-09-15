---
schema_version: software-v0.1
name: LLM Serving 软件栈
object_type: concept
category: serving-architecture
updated: 2026-09-15
---
# LLM Serving 软件栈

> 把请求路由、模型执行、KV、集群调度和设备资源管理分层观察。

## 问题

LLM serving 同时存在 request 级、worker 级、Pod/Job 级和设备级控制。如果把这些职责都叫“调度”，项目边界会迅速混乱。

## 核心机制

```text
Request / API
  ↓
[[software/projects/llm-d|llm-d]]          请求级路由与编排
  ↓
[[software/projects/vllm|vLLM]]           模型执行
  ↕
[[software/projects/lmcache|LMCache]]      KV 外部生命周期
  ↓
[[software/projects/kai-scheduler|KAI]]    Pod / Job placement
  ↓
[[software/projects/kubernetes-dra|DRA]] / [[software/projects/hami|HAMi]]
  ↓
GPU / NPU / NIC / Memory
```

## 判断要点

- request routing 与 Pod placement 是两级不同的调度。
- KV 状态跨越执行、缓存和路由层。
- 项目可以跨层实现能力，但仍应有一个主定位。

## 相关项目与概念

- [[software/concepts/pd-disaggregation|Prefill / Decode 分离]]
- [[software/concepts/kv-cache-lifecycle|KV Cache 生命周期]]
- [[software/concepts/topology-aware-scheduling|拓扑感知调度]]
- [[software/concepts/accelerator-resource-model|加速器资源模型]]
