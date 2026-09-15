---
schema_version: software-v0.1
name: Prefill / Decode Disaggregation
object_type: concept
category: serving-architecture
updated: 2026-09-15
---
# Prefill / Decode 分离

> 把 Prefill 与 Decode 放到不同 worker 或资源池，使两个阶段可以独立调度和扩缩容。

## 问题

Prefill 更偏计算密集，Decode 更偏 KV/HBM 带宽与逐 token 延迟。两阶段混跑时容易互相干扰，但拆分后又引入 KV 搬运与网络成本。

## 核心机制

```text
Router / Orchestrator
  [[software/projects/llm-d|llm-d]] / [[software/projects/nvidia-dynamo|Dynamo]]
        ↓
Prefill Engine
  [[software/projects/vllm|vLLM]] / [[software/projects/sglang|SGLang]] / [[software/projects/tensorrt-llm|TensorRT-LLM]]
        ↓
KV State / Transfer
  [[software/projects/lmcache|LMCache]] / [[software/projects/mooncake|Mooncake]] / [[software/projects/nixl|NIXL]]
        ↓
Decode Engine
```

Kubernetes 部署侧还可能由 [[software/projects/kserve|KServe]] 表达分离式 workload，底层 placement 由 [[software/projects/kai-scheduler|KAI-Scheduler]] 等系统完成。

## 判断要点

- KV 传输时间必须小于拆分带来的计算/排队收益。
- TTFT 与 TPOT 要分别观察。
- Prefill/Decode 池之间的 NIC、RDMA、NUMA 与 GPU 拓扑是一级变量。
- 故障恢复、rollout 与 KV 一致性会增加控制面复杂度。

## 相关项目与概念

- [[software/concepts/kv-cache-lifecycle|KV Cache 生命周期]]
- [[software/concepts/topology-aware-scheduling|拓扑感知调度]]
- [[software/concepts/llm-serving-stack|LLM Serving 软件栈]]
