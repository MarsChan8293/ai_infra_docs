---
schema_version: software-v0.1
name: 异构推理
object_type: concept
category: inference-architecture
updated: 2026-09-15
---
# 异构推理

> 不把不同 GPU/NPU 伪装成同一种设备，而是保留硬件、软件和 SLA 差异后再做选择。

## 问题

不同加速器在显存/HBM、互联、量化、算子覆盖、推理引擎兼容性和成本上差异明显。只用理论 FLOPS 选择硬件容易得到错误结论。

## 核心机制

```text
模型 / 请求画像
  + Benchmark
  + SLA / 成本目标
        ↓
控制面
  ├── 选择推理引擎
  ├── 请求级路由
  ├── Pod 级 placement
  └── 设备资源分配
        ↓
不同 GPU / NPU 资源池
```

## 判断要点

- 硬件选择应基于真实 workload benchmark，而不是单一峰值指标。
- P/D 分离可以让不同阶段选择不同资源，但 KV 格式和传输兼容性会成为新约束。
- 跨厂商透明 KV 复用通常比同硬件池内复用更困难。
- 调度还必须结合 [[software/concepts/topology-aware-scheduling|拓扑感知调度]]。

## 相关项目与概念

- [[software/projects/vllm|vLLM]]
- [[software/projects/llm-d|llm-d]]
- [[software/concepts/accelerator-resource-model|加速器资源模型]]
- [[chip/00-project-index|芯片与硬件资料库]]
