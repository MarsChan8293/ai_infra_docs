---
title: Prefill / Decode 分离
aliases:
  - P/D Disaggregation
  - PD 分离
  - Prefill Decode Disaggregation
tags:
  - concept
  - inference
  - pd-disaggregation
---

# Prefill / Decode 分离

P/D 分离把 LLM 推理中的 Prefill 与 Decode 拆到不同 worker 或不同资源池运行。它的核心动机是：Prefill 更偏计算密集，Decode 更偏 HBM 带宽和低延迟，两阶段的最优硬件与调度策略往往不同。

## 关键链路

```text
请求
  → [[software/distributed-serving/llm-d|llm-d]] 选择 Prefill / Decode worker
  → [[software/inference-engine/vllm|vLLM]] Prefill 生成 KV
  → [[software/kv-cache/lmcache|LMCache]] / 高速传输搬运 KV
  → [[software/inference-engine/vllm|vLLM]] Decode 持续生成 token
```

底层 placement 由 [[software/scheduling/kai-scheduler|KAI-Scheduler]] 等调度器完成，设备声明与共享可由 [[software/device-resource/dra|Kubernetes DRA]]、[[software/device-resource/hami|HAMi]] 等组件参与。

## 是否值得拆分

P/D 分离成立的关键，不是“架构更漂亮”，而是 KV 搬运成本必须低于重新计算或阶段混跑造成的代价。要同时观察 TTFT、TPOT、KV 大小、网络带宽、worker 排队、故障恢复和拓扑距离。

## 相关概念

- [[software/concepts/kv-cache-lifecycle|KV Cache 生命周期]]
- [[software/concepts/topology-aware-scheduling|拓扑感知调度]]
- [[software/concepts/heterogeneous-inference|异构推理]]
- [[software/concepts/llm-serving-stack|LLM Serving 软件栈]]

返回 [[software/README|AI Infra 软件栈地图]]。
