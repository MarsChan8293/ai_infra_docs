# Broadcom AI 基础设施芯片资料

- 研究截止日：2026-09-13
- 核验日期：2026-09-13
- 厂商范围：与 AI scale-up / scale-out 强绑定的 Ethernet NIC、交换 ASIC；本目录不是 GPU/NPU 算力芯片目录
- 证据原则：NIC、交换芯片、交换机/板卡、网络拓扑和 XPU 集群规模分层记录

## 芯片页关系导航

- [[thor-ultra|Broadcom — Thor Ultra 800G AI Ethernet NIC]] · [打开 Markdown](./thor-ultra.md)
- [[tomahawk-ultra|Broadcom — Tomahawk Ultra]] · [打开 Markdown](./tomahawk-ultra.md)

## 当前结论

Broadcom 在 AI 基础设施中的关键角色之一是 Ethernet scale-up / scale-out 网络，而不是提供通用 AI 计算 GPU。当前仓库补入两条代表性路线：

1. **Thor Ultra**：800G AI Ethernet NIC，面向 UEC/AI scale-out，主机侧为 PCIe Gen6 x16；2025-10 发布时状态为 sampling。
2. **Tomahawk Ultra**：面向 AI scale-up/HPC 的 51.2Tb/s Ethernet switch ASIC，Broadcom 在 2025-07 宣布已经 shipping。

这两类芯片都不能与 GPU/NPU 的 FP8、HBM 容量做“同表算力比较”。它们解决的是主机/XPU 接入、交换、拥塞、可靠传输和 collective 网络路径问题。

## 生命周期与边界

| 产品 | 对象层级 | 公开状态 | 关键边界 |
| --- | --- | --- | --- |
| Thor Ultra | 800G NIC / adapter silicon | 2025-10 sampling | “连接数十万 XPU”是网络规模主张，不是单卡数量 |
| Tomahawk Ultra | Ethernet switch ASIC | 2025-07 Broadcom 宣布 shipping | 51.2Tb/s 是交换容量，不是 AI 算力 |

## 网络能力脉络

Thor Ultra 的公开能力包括 packet-level multipathing、out-of-order delivery 到 XPU memory、selective retransmission、可编程拥塞控制、PCIe Gen6 x16，以及线速加解密/PSP offload。Tomahawk Ultra 则强调低时延、lossless fabric 与 in-network collectives，用于 scale-up Ethernet。

这些机制可以影响分布式训练/推理的通信效率，但不能直接推导端到端 tokens/s 或模型性能。

## 直接来源

- [Broadcom：Thor Ultra 800G AI Ethernet NIC，2025-10-14](https://investors.broadcom.com/news-releases/news-release-details/broadcom-introduces-industrys-first-800g-ai-ethernet-nic)
- [Broadcom：Tomahawk Ultra shipping，2025-07-15](https://www.broadcom.com/company/news/product-releases/63341)
- [Broadcom：Tomahawk Ultra BCM78920 Series](https://www.broadcom.com/products/ethernet-connectivity/switching/strataxgs/bcm78920-series)
- [Hot Chips 2026 Program](https://hc2026.hotchips.org/program/)

## 待补证据

- Thor Ultra 从 sampling 到量产/大规模出货的后续官方状态。
- Thor Ultra 单卡功耗、板型差异与完整 UEC profile。
- Tomahawk Ultra SKU、buffer、SerDes 配置与实际系统拓扑的逐项拆分。
- 与 Tomahawk 6、Jericho4、SUE 的 scale-out/scale-up 分工可以在网络专题中进一步整理。
