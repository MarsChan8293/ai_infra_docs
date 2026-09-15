---
schema_version: software-v0.1
name: LLM Serving 软件栈
object_type: concept
category: serving-architecture
updated: 2026-09-15
---
# LLM Serving 软件栈

> 把 API/Gateway、请求编排、模型执行、KV、通信、调度和设备资源分层观察。

## 问题

LLM serving 同时存在 API 路由、request 级路由、模型 worker 执行、KV 数据路径、Pod/Job placement 和设备分配。如果都叫“调度”，项目边界会迅速混乱。

## 核心机制

```text
API / Gateway
  [[software/projects/litellm|LiteLLM]] / [[software/projects/gateway-api-inference-extension|Gateway API Inference Extension]]
        ↓
Distributed Serving
  [[software/projects/llm-d|llm-d]] / [[software/projects/nvidia-dynamo|Dynamo]] / [[software/projects/kserve|KServe]] / [[software/projects/ray-serve|Ray Serve]]
        ↓
Inference Engine
  [[software/projects/vllm|vLLM]] / [[software/projects/sglang|SGLang]] / [[software/projects/tensorrt-llm|TensorRT-LLM]] / [[software/projects/llama-cpp|llama.cpp]]
        ↕
KV / Data
  [[software/projects/lmcache|LMCache]] / [[software/projects/mooncake|Mooncake]] / [[software/projects/nixl|NIXL]]
        ↓
Kernel / Communication
  [[software/projects/flashinfer|FlashInfer]] / [[software/projects/triton|Triton]] / [[software/projects/nccl|NCCL]] / [[software/projects/deepep|DeepEP]]
        ↓
Scheduler / Device
  [[software/projects/kai-scheduler|KAI]] / [[software/projects/volcano|Volcano]] / [[software/projects/kueue|Kueue]]
  [[software/projects/kubernetes-dra|DRA]] / [[software/projects/hami|HAMi]] / [[software/projects/nvidia-gpu-operator|GPU Operator]]
```

## 判断要点

- API routing、request routing 与 Pod placement 是不同层级。
- KV 状态横跨执行、缓存、传输和路由。
- Kernel、集合通信和设备资源层会直接影响上层 serving 性能，但职责不能混写。

## 相关项目与概念

- [[software/concepts/pd-disaggregation|Prefill / Decode 分离]]
- [[software/concepts/kv-cache-lifecycle|KV Cache 生命周期]]
- [[software/concepts/topology-aware-scheduling|拓扑感知调度]]
- [[software/concepts/accelerator-resource-model|加速器资源模型]]
