# Broadcom — Tomahawk Ultra

- 厂商总览：[Broadcom](./Broadcom-overview.md) · [[Broadcom-overview|图谱总览]]
- 产品层级：Ethernet switch ASIC / AI scale-up fabric
- 研究截止日：2026-09-13
- 核验日期：2026-09-13

## 产品定位

Tomahawk Ultra 是 Broadcom 为 AI scale-up 与 HPC 设计的 Ethernet switch ASIC。与 Thor Ultra NIC 不同，它位于交换 fabric 层，负责低时延、lossless switching、集体通信等网络功能。

## 已公开规格

| 字段 | 官方公开信息 | 边界 |
| --- | --- | --- |
| 总交换容量 | 51.2Tb/s | switch capacity，不是 AI FLOPS |
| 端口组合 | 64×800G / 128×400G / 256×200G Ethernet | SKU/配置层 |
| SerDes | 106.25G PAM4 | 物理层 |
| 交换时延 | 约 250ns 厂商口径 | 芯片/交换路径 |
| packet rate | 64B packet 下超过 76B packets/s 的产品口径 | 厂商规格 |
| AI fabric | LLR、CBFC、AI Fabric Headers、in-network collectives | 网络能力 |
| Scale-up | 官方定位 up to 256 XPUs | fabric 系统级 |

## 生命周期

Broadcom 在 2025-07-15 发布材料中明确使用 **“Now Shipping”**，表示 Tomahawk Ultra 已出货，用于 rack-scale AI training clusters 与 supercomputing 环境。这个状态比 Thor Ultra 在 2025-10 的 sampling 更成熟。

| 阶段 | 状态 |
| --- | --- |
| 发布 | 已发布 |
| shipping | 2025-07 官方明确确认 |
| 具体客户/出货量 | 公开资料有限 |
| 云服务可用性 | 不适用；这是交换 ASIC/网络产品 |

## 对 AI 的作用边界

Tomahawk Ultra 的 in-network collective、低时延和 lossless 机制可以减少 scale-up 通信开销，但这类网络优化不是 Tensor FLOPS。跨厂商比较时，应将其放在“互联/交换”维度，与 NVLink switch、UALink/UEC 等系统互联路线比较，而不是与 GPU 的算力和显存比较。

## 直接来源

- [Broadcom：Tomahawk Ultra shipping，2025-07-15](https://www.broadcom.com/company/news/product-releases/63341)
- [Broadcom：BCM78920 Tomahawk Ultra Series](https://www.broadcom.com/products/ethernet-connectivity/switching/strataxgs/bcm78920-series)
- [Hot Chips 2026 Program](https://hc2026.hotchips.org/program/)

## 未确认项

- SKU 级 buffer、功耗和封装差异。
- in-network collective 支持的具体操作和软件接口。
- 实际 256-XPU fabric 的拓扑、oversubscription 与系统基准。
