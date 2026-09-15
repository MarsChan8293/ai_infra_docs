---
title: Software Project Index
aliases:
  - AI Infra Software Index
  - 软件项目索引
tags:
  - moc
  - software
  - ai-infra
---
# Software Project Index

当前 Software V0.1 收录 30 个项目。项目事实统一位于 `software/projects/`；跨项目稳定机制位于 `software/concepts/`。

## Inference Engine

- [[software/projects/vllm|vLLM]]
- [[software/projects/sglang|SGLang]]
- [[software/projects/tensorrt-llm|TensorRT-LLM]]
- [[software/projects/llama-cpp|llama.cpp]]

## Distributed Serving / Gateway

- [[software/projects/llm-d|llm-d]]
- [[software/projects/nvidia-dynamo|NVIDIA Dynamo]]
- [[software/projects/kserve|KServe]]
- [[software/projects/ray-serve|Ray Serve]]
- [[software/projects/gateway-api-inference-extension|Gateway API Inference Extension]]
- [[software/projects/bentoml|BentoML]]
- [[software/projects/litellm|LiteLLM]]

## KV Cache

- [[software/projects/lmcache|LMCache]]
- [[software/projects/mooncake|Mooncake]]

## Communication

- [[software/projects/nixl|NIXL]]
- [[software/projects/nccl|NCCL]]
- [[software/projects/rccl|RCCL]]
- [[software/projects/deepep|DeepEP]]
- [[software/projects/ucx|UCX]]

## Runtime / Kernel

- [[software/projects/flashinfer|FlashInfer]]
- [[software/projects/flashattention|FlashAttention]]
- [[software/projects/cutlass|CUTLASS]]
- [[software/projects/deepgemm|DeepGEMM]]

## Compiler

- [[software/projects/triton|Triton]]

## Scheduler

- [[software/projects/kai-scheduler|KAI-Scheduler]]
- [[software/projects/volcano|Volcano]]
- [[software/projects/kueue|Kueue]]

## Device Resource

- [[software/projects/hami|HAMi]]
- [[software/projects/kubernetes-dra|Kubernetes DRA]]
- [[software/projects/nvidia-gpu-operator|NVIDIA GPU Operator]]
- [[software/projects/nvidia-k8s-device-plugin|NVIDIA k8s-device-plugin]]

## Concepts

- [[software/concepts/llm-serving-stack|LLM Serving 软件栈]]
- [[software/concepts/pd-disaggregation|Prefill / Decode 分离]]
- [[software/concepts/kv-cache-lifecycle|KV Cache 生命周期]]
- [[software/concepts/topology-aware-scheduling|拓扑感知调度]]
- [[software/concepts/accelerator-resource-model|加速器资源模型]]
- [[software/concepts/heterogeneous-inference|异构推理]]

维护约束见 [[software/SCHEMA|Software Schema V0.1]]。
