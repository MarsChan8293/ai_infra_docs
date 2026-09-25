---
schema_version: system-v0.1
name: 异构推理
object_type: concept
category: heterogeneous-compute
updated: 2026-09-25
tags:
  - system
  - heterogeneous-compute
  - inference
---
# 异构推理

> 异构推理不是简单地让同一软件“支持更多卡”，而是把模型、算子、状态、通信与 SLA 映射到能力不同的加速器和内存/网络路径上。

## 系统视角

```text
Model / Workload / SLA
        ↓
Execution partitioning
        ↓
Accelerator capability
  ├─ compute / precision
  ├─ HBM capacity / bandwidth
  ├─ kernel availability
  ├─ collective communication
  └─ interconnect / topology
        ↓
Placement + memory hierarchy
```

推理引擎实现可参考 [vLLM](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/vllm-project/vLLM/vLLM.md) 与 [SGLang](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/sgl-project/SGLang/SGLang.md) 等 canonical 项目记录，但本页只维护跨项目稳定的系统约束。

## 兼容性不是一个布尔值

“支持某芯片”至少应拆成以下层次：

- 模型权重能否装入，是否需要量化或分片。
- 关键 dtype、attention、MoE 和 kernel 是否可执行。
- 单卡性能是否可接受。
- 多卡 collective / P2P / RDMA 是否完整。
- 驱动、runtime、编译器与容器栈是否稳定。
- 长上下文状态和 KV 内存层级是否可承载。
- 在真实拓扑下能否达到目标 TTFT、TPOT、吞吐和可用性。

## 调度策略

异构系统应按 workload role 与瓶颈分配设备，而不是只按“卡的数量”平均分配。例如 Prefill 更偏计算与权重吞吐，Decode 更容易受状态容量、访存和通信影响；不同模型架构还会改变两者的比例。

## 相关概念

- [[system/resource/accelerator-resource-model|加速器资源模型]]
- [[system/scheduling/topology-aware-scheduling|拓扑感知调度]]
- [[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层级]]
- [[models/00-model-index|AI Model Index]]
- [[chip/00-project-index|芯片与基础设施资料库]]
