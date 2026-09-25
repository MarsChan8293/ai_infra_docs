---
schema_version: system-v0.1
name: KV Cache 内存层级
object_type: concept
category: memory-architecture
inputs:
  - model.context_length
  - model.architecture.attention
  - workload.batch_size
  - workload.concurrency
  - workload.prefix_reuse
  - hardware.memory.capacity
  - hardware.memory.bandwidth
constraints:
  - memory-capacity
  - memory-bandwidth
  - transfer-bandwidth
  - transfer-latency
  - storage-endurance
  - isolation
outputs:
  - kv_placement_policy
  - kv_transfer_cost
  - recompute_vs_retrieve_break_even
  - tier_capacity_requirements
assumptions:
  - KV 状态可以在生命周期边界内被识别、迁移和失效
  - 派生判断必须显式计入传输、排队和布局转换成本
related_layers:
  - model
  - workload
  - memory
  - communication
  - topology
  - accelerator
  - storage
evidence: {}
updated: 2026-09-25
tags:
  - system
  - memory
  - kv-cache
---
# KV Cache 内存层级

> KV Cache 不只是推理引擎内部对象，而是贯穿生成、驻留、复用、迁移、卸载和淘汰的一类系统状态。硬件视角的关键问题是：状态应该放在哪一层、通过什么路径搬运，以及搬运成本是否低于重新 Prefill。

## 系统层级

```text
GPU / NPU on-chip state
        ↓
HBM / device memory
        ↓  PCIe / CXL / NVLink / vendor fabric
Host DRAM
        ↓
CXL Memory / pooled memory / remote memory
        ↓  RDMA / fabric
Remote DRAM
        ↓
NVMe SSD / flash tier
```

实际系统不一定包含全部层级。每增加一层都在容量、带宽、时延、成本、功耗和故障域之间做交换。

## 生命周期

1. Prefill 生成 KV 或其他上下文状态。
2. 状态优先驻留在设备侧高带宽内存。
3. 热状态在本地复用，降低重复 Prefill。
4. 容量不足时迁移到 Host DRAM、远端内存或持久化介质。
5. Decode 或后续请求命中时取回。
6. 根据热度、租户、会话和失效语义淘汰。

项目实现示例可直接参考 [vLLM](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/vllm-project/vLLM/vLLM.md)、[SGLang](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/sgl-project/SGLang/SGLang.md)、[LMCache](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/LMCache/LMCache/LMCache.md)、[Mooncake](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/kvcache-ai/Mooncake/Mooncake.md) 与 [NIXL](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/ai-dynamo/NIXL/NIXL.md)。

## 硬件判断维度

| 维度 | 关注点 |
|---|---|
| 容量 | 每 token / 每会话状态大小，长上下文和并发放大倍数 |
| 带宽 | Retrieve / Transfer 是否会吞掉 Decode 或 Prefill 的时间预算 |
| 时延 | 首字节、随机访问、尾延迟与跨 NUMA / 跨节点代价 |
| 传输路径 | PCIe、CXL、NVLink、RDMA、NIC 与交换网络的真实瓶颈 |
| 耐久度 | SSD / flash 的写入寿命、DWPD/TBW、写放大与冷热分层策略 |
| 功耗与成本 | $/GB、W/GB 与单位 token 的数据搬运能耗 |
| 一致性与隔离 | 多租户生命周期、失效、回收和故障恢复语义 |

## 第一性原理判断

只有当“取回状态的总成本”小于“重新计算状态的总成本”时，卸载与复用才有系统收益。这个比较必须包含介质访问、网络传输、序列化布局转换、排队和尾延迟，而不只是比较介质标称带宽。

SSD 等持久化介质还需要单独评估写放大和耐久度。它们的容量优势并不自动意味着适合作为高频写入的 KV 热层。

## 相关概念

- [[system/scheduling/topology-aware-scheduling|拓扑感知调度]]
- [[system/heterogeneous-compute/heterogeneous-inference|异构推理]]
- [[chip/00-project-index|芯片与基础设施资料库]]
- [[models/00-model-index|AI Model Index]]
