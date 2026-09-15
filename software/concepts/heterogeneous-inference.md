---
schema_version: software-v0.1
name: 异构推理
object_type: concept
category: inference-architecture
updated: 2026-09-15
---
# 异构推理

> 保留不同硬件、runtime、通信和模型的真实差异，再由控制面根据 workload 与 SLA 做选择。

## 问题

NVIDIA、AMD、Ascend、CPU/边缘设备在算子支持、显存、带宽、互联、量化、通信和软件成熟度上都不同，不能只用理论 FLOPS 做选择。

## 核心机制

```text
模型 / Workload / SLA
        ↓
Inference Engine
  [[software/projects/vllm|vLLM]] / [[software/projects/sglang|SGLang]] / [[software/projects/llama-cpp|llama.cpp]]
        ↓
Runtime / Communication
  [[software/projects/flashinfer|FlashInfer]] / [[software/projects/triton|Triton]]
  [[software/projects/nccl|NCCL]] / [[software/projects/rccl|RCCL]]
        ↓
Resource / Placement
  [[software/projects/kai-scheduler|KAI-Scheduler]] / [[software/projects/kubernetes-dra|DRA]] / [[software/projects/hami|HAMi]]
        ↓
不同 GPU / NPU / CPU
```

## 判断要点

- 记录功能支持度，而不仅是“能启动”。
- Benchmark 必须绑定 engine、版本、模型、量化和硬件。
- P/D 分离允许不同阶段使用不同资源池，但 KV 格式和数据路径可能成为新约束。
- 同一个 API 并不意味着不同 backend 性能和功能等价。

## 相关项目与概念

- [[software/concepts/pd-disaggregation|Prefill / Decode 分离]]
- [[software/concepts/accelerator-resource-model|加速器资源模型]]
- [[software/concepts/topology-aware-scheduling|拓扑感知调度]]
- [[chip/00-project-index|芯片与基础设施资料库]]
