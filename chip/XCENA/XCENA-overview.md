# XCENA 芯片资料

- 研究截止日：2026-09-13
- 核验日期：2026-09-13
- 厂商范围：CXL computational memory / memory-centric computing；本轮重点为 MX1
- 证据原则：CXL 内存扩展、near-data processing、SSD-backed capacity、软件应用示例和商业生命周期分开记录

## 芯片页关系导航

- [[mx1|XCENA — MX1 CXL Computational Memory]] · [打开 Markdown](./mx1.md)

## 当前结论

MX1 是 XCENA 面向 AI 与数据密集型工作负载的 CXL computational memory 产品。官方产品页当前列出的 PoC 规格包括 **CXL 3.2 Type-3、主机侧 PCIe 6.0 dual x8、4 条 DDR5 RDIMM 通道、8400MT/s、2DPC、数千颗 1.4GHz 自研 RISC-V 数据加速核，以及 FP32/FP16 vector engine**；产品定位把内存扩展与 near-data processing 结合起来。

MX1 的“最高 2TB”来自 **256GB DIMM、2DPC 的 AIC/内存配置口径**，不是单颗控制器 die 内置 2TB DRAM。其 InfiniteMemory 还可通过独立 PCIe 6.0/NVMe 路径连接 SSD，进一步扩展可访问容量，这属于系统内存层次而不是芯片片上容量。

## 生命周期

| 阶段 | 状态 | 证据边界 |
| --- | --- | --- |
| FMS 2025 公开 | 已展示 MX1 | 官方 Newsroom |
| 工作样片 | 2025 年计划从 10 月向 select partners 提供 working samples | 厂商公告 |
| 2026 product brief | 当前官网提供 MX1 PoC Product Brief | “PoC”表明规格仍有产品化边界 |
| production-ready | 2025 公告计划 2026 推出 production-ready 版本 | 计划不等于已确认大规模量产 |
| 伙伴验证 | 2026 已公开与 KISTI 等验证/部署推进信息 | 验证环境不等于广泛商业 GA |

官网规格表还明确注明部分高亮功能“to be supported in production”，因此不能把 PoC 页面上的全部功能都写成当前量产固件已经可用。

## 软件栈

XCENA 提供 full-stack SDK，包括多层 API、仿真/模拟、OS 驱动和低层 device API。官网展示 KV Cache Offloading、RAG/Vector DB、Data Analytics 等应用示例；这些是软件/应用方向，不能直接当作每类 workload 已获得固定倍数加速的 benchmark 结论。

## 直接来源

- [XCENA：MX1 Computational Memory 产品页](https://xcena.com/computational_memory)
- [XCENA：MX1 FMS 2025 / working samples / 2026 production-ready plan](https://www.xcena.com/newsroom/?bmode=view&idx=170962702&t=board)
- [XCENA：SDK Overview](https://xcena.com/sdk_overview)
- [XCENA：2026 Series B / deployment expansion](https://www.xcena.com/newsroom/?bmode=view&idx=171571166&t=board)
- [Hot Chips 2026 Program](https://hc2026.hotchips.org/program/)

## 待补证据

- production-ready MX1 与当前 PoC brief 的最终规格差异。
- 芯片制造节点、功耗、die/chiplet 组织、向量引擎数量与峰值算力。
- CXL 3.2 特性在量产固件中的逐项可用状态。
- 伙伴验证结果、商业出货规模和可复现端到端 benchmark。
