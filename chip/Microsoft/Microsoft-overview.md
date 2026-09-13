# Microsoft 芯片资料

- 研究截止日：2026-09-13
- 核验日期：2026-09-13
- 厂商范围：Microsoft 自研数据中心 AI 加速器；本轮重点为 Maia 200
- 证据原则：把 SoC 指标、卡/节点、scale-up 网络、数据中心部署和 Azure 客户可用性分开记录

## 芯片页关系导航

- [[maia-200|Microsoft — Maia 200]] · [打开 Markdown](./maia-200.md)

## 当前结论

Maia 200 是 Microsoft 第二代自研 AI 加速器，明确面向大规模推理。Microsoft 已公开较完整的芯片级规格：**TSMC 3nm、超过 1400 亿晶体管、原生 FP4/FP8 Tensor Core、216GB HBM3e、7TB/s HBM 带宽、272MB 片上 SRAM、超过 10 petaFLOPS FP4、超过 5 petaFLOPS FP8，以及 750W SoC TDP**。

互联上，Maia 200 集成 on-die NIC。架构文章给出的单向 I/O 带宽为 1.4TB/s、双向为 2.8TB/s，并通过基于标准 Ethernet 的 ATL scale-up 网络扩展至两级、最多 6,144 个加速器。**6,144 是集群/scale-up 域规模，不是单芯片规格。**

## 生命周期与部署

| 阶段 | Maia 200 状态 | 证据边界 |
| --- | --- | --- |
| 发布 | 2026-01-26 正式发布 | Microsoft 官方博客 |
| 数据中心部署 | 已投入生产；2026 年 Q3 前已在 Iowa、Arizona 数据中心 live | Microsoft 财报电话会与 Build 2026 |
| 后续区域 | Microsoft 在 Build 2026 表示 Italy、Australia、South Korea 后续部署 | 路线/部署计划，不等于当前全部 GA |
| 客户可用性 | Microsoft 表述已有 inference capacity 可供客户使用 | 不等同于公开的独立 Maia VM/SKU 全区域 GA |
| Maia SDK | Preview/试用阶段公开 | SDK 状态与硬件部署状态分开 |

## 软件栈

Microsoft 公布的 Maia SDK 包括 PyTorch 集成、Triton compiler、优化 kernel library、Maia 低层语言与模拟/开发工具。软件栈用于降低模型迁移和 kernel 优化门槛，但软件支持本身不能反推未公开硬件特性。

## 直接来源

- [Microsoft Blog：Maia 200: The AI accelerator built for inference，2026-01-26](https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/)
- [Microsoft Azure Infrastructure Blog：Deep dive into the Maia 200 architecture](https://techcommunity.microsoft.com/blog/azureinfrastructureblog/deep-dive-into-the-maia-200-architecture/4489312)
- [Microsoft FY2026 Q3 Earnings Call](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3)
- [Microsoft Build 2026 Live Blog](https://news.microsoft.com/build-2026-live-blog)
- [Hot Chips 2026 Program](https://hc2026.hotchips.org/program/)

## 待补证据

- HBM3e stack 数量、总线组织、封装与 die/chiplet 结构的完整公开图。
- 卡/节点级功耗、主机连接与冗余设计。
- 可独立购买或 Azure SKU/区域级 GA 的产品化边界。
- 独立第三方端到端模型基准与可复现 benchmark 配置。
