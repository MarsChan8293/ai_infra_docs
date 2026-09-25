---
schema_version: system-v0.1
name: KV Cache 内存层次
object_type: concept
category: memory-architecture
updated: 2026-09-25
---

# KV Cache 内存层次

> KV Cache 与其他推理状态不只是“显存里的一块缓存”，而是一类会在容量、带宽、延迟、互联和耐久度之间移动的系统资源。

## 硬件视角

```text
GPU / NPU on-package memory (HBM)
        ↓  PCIe / CXL / NVLink / XGMI
Host DRAM / CXL-attached memory
        ↓  RDMA / fabric
Remote DRAM
        ↓
NVMe / SSD
```

越靠近计算单元，通常延迟更低、带宽更高，但容量更贵且更有限；越往下层迁移，容量和成本优势更明显，同时会引入搬运、排队和介质耐久度问题。

## 关键判断量

- **容量**：单请求状态、并发请求与前缀复用后的总驻留量。
- **带宽与延迟**：Retrieve / Transfer 成本必须和重新 Prefill 的代价比较，而不能只看介质容量。
- **互联路径**：PCIe、CXL、NIC、NUMA 与交换结构决定状态能否以足够低的代价移动。
- **耐久度**：DRAM / HBM 与 NAND SSD 的写入寿命机制不同，持续 KV offload 到 SSD 时必须关注写放大、DWPD / TBW 与实际写入流量。
- **布局兼容**：KV layout、dtype、block size 与具体模型、engine 和硬件实现有关。
- **隔离与失效**：多租户、节点故障和缓存一致性决定状态能否安全复用。

## 软件实现参照

项目事实不在本仓库维护，可参考 [LMCache](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/LMCache/LMCache/LMCache.md)、[Mooncake](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/kvcache-ai/Mooncake/Mooncake.md) 与 [NIXL](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/ai-dynamo/NIXL/NIXL.md) 的 canonical 页面。

## 相关节点

- [[system/topology/topology-aware-scheduling|拓扑感知调度]]
- [[system/heterogeneous-compute/heterogeneous-inference|异构推理]]
- [[models/00-model-index|AI Model Index]]
- [[chip/00-project-index|芯片与基础设施资料库]]
