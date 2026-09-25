---
schema_version: system-v0.1
name: 异构推理
object_type: concept
category: heterogeneous-compute
updated: 2026-09-25
---

# 异构推理

> 异构推理不是把不同厂商设备放进同一个资源池就结束，而是把模型结构、精度、内存状态、kernel 与通信需求映射到真正合适的硬件。

## 映射链路

```text
Model / Workload / SLA
        ↓
state size + precision + parallelism
        ↓
runtime / kernel / communication capability
        ↓
device memory + compute + interconnect
        ↓
GPU / NPU placement
```

## 关键约束

- **算力类型**：BF16 / FP16 / FP8 / INT8 / INT4 等路径是否由硬件和软件栈共同支持。
- **内存容量与带宽**：权重、KV / recurrent state、activation 与 workspace 是否能驻留。
- **通信能力**：TP / EP / PP 对片内、卡间和节点间互联的要求不同。
- **Kernel 可用性**：相同模型结构在不同设备上的算子覆盖和优化程度可能不同。
- **拓扑**：设备“可用”不等于设备组合适合某种并行策略。
- **可移植性边界**：统一 API 不能消除硬件行为差异，只能把差异显式化并纳入调度。

## 软件实现参照

推理引擎和 kernel 项目可参考 [vLLM](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/vllm-project/vLLM/vLLM.md)、[SGLang](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/sgl-project/SGLang/SGLang.md)、[FlashInfer](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/flashinfer-ai/FlashInfer/FlashInfer.md) 与 [Triton](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/triton-lang/Triton/Triton.md) 的 canonical 页面。

## 相关节点

- [[system/resource/accelerator-resource-model|加速器资源模型]]
- [[system/topology/topology-aware-scheduling|拓扑感知调度]]
- [[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层次]]
- [[models/00-model-index|AI Model Index]]
- [[chip/00-project-index|芯片与基础设施资料库]]
