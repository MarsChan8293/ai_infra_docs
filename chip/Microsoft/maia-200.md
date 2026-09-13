# Microsoft — Maia 200

- 厂商总览：[Microsoft](./Microsoft-overview.md) · [[Microsoft-overview|图谱总览]]
- 产品层级：自研数据中心 AI 推理加速器 SoC；scale-up fabric 与数据中心部署单列
- 研究截止日：2026-09-13
- 核验日期：2026-09-13

## 一句话结论

Maia 200 是 Microsoft 第二代 AI accelerator，已经从“路线图/会议对象”进入实际数据中心生产部署。其公开资料在 hyperscaler 自研芯片中相对完整：**TSMC 3nm、>140B 晶体管、>10 petaFLOPS FP4、>5 petaFLOPS FP8、216GB HBM3e / 7TB/s、272MB on-die SRAM、750W SoC TDP，以及 2.8TB/s 双向 on-die NIC**。

## 芯片级规格

| 字段 | 官方公开信息 | 证据边界 |
| --- | --- | --- |
| 工艺 | TSMC 3nm / N3 | 芯片级 |
| 晶体管 | 超过 1400 亿 | 芯片级 |
| 低精度计算 | 原生 FP4 / FP8 Tensor Core | 芯片级 |
| FP4 | >10 petaFLOPS；架构文章另给 10.1 PetaOPS | 峰值厂商口径，注意 FLOPS/OPS 术语差异 |
| FP8 | >5 petaFLOPS | 峰值厂商口径 |
| HBM | 216GB HBM3e | 芯片/封装级 |
| HBM 带宽 | 7TB/s | 芯片级 |
| SRAM | 272MB on-die | 芯片级 |
| SoC TDP | 750W | SoC 口径，不等于整机功耗 |
| 数据移动 | multi-level DMA + hierarchical NoC | 芯片级 |
| NIC | on-die NIC，1.4TB/s 单向、2.8TB/s 双向 | 芯片 I/O |

## 执行层次

Microsoft 的架构说明将 Maia 200 组织为层级化 tile/cluster 结构。tile 内包含 tensor compute、SIMD/vector 处理、本地 SRAM 与 DMA；更高层通过 cluster SRAM、DMA 和层级 NoC 组织数据流。该结构强调低精度计算与数据搬运协同，而不是仅依靠峰值 tensor FLOPS。

## Scale-up 网络边界

Maia 200 的 on-die NIC 使用基于标准 Ethernet 的 ATL（AI Transport Layer）实现 scale-up。Microsoft 给出的能力包括 packet spraying、multipath routing 与拥塞控制，并宣称两级 scale-up 拓扑最多覆盖 **6,144 accelerators**。

这里的 6,144 是**集群/网络域规模**。它不能写成单芯片包含 6,144 个核心，也不能把集群总带宽直接除/乘后当作芯片固定指标。

## 生命周期与部署

| 时间/阶段 | 状态 | 证据 |
| --- | --- | --- |
| 2026-01-26 | 正式发布 | Microsoft Blog |
| 2026-01 | US Central / Iowa 先行部署，Arizona 后续 | 首发材料 |
| FY2026 Q3 | Iowa 与 Arizona 数据中心均已 live | Microsoft earnings call |
| Build 2026 | Microsoft 表示已 production，并计划扩展到 Italy、Australia、South Korea | 官方 Build live blog |
| Azure 商品化 | 可承载 Microsoft/客户推理容量，但独立 Maia VM/SKU 的全区域 GA 边界未确认 | 不把内部部署等同独立 SKU GA |

## 软件栈

首发资料公开了 Maia SDK preview：

- PyTorch integration
- Triton compiler
- optimized kernel library
- Maia low-level programming language
- simulator / development tooling

这使 Maia 200 更接近可编程 hyperscaler accelerator，而不是完全封闭的固定功能 ASIC。但 SDK preview 仍应与 Azure 硬件 production 状态分开。

## 性能口径警告

Microsoft 给出的“相对 Trainium3 / TPU7、tokens per dollar、performance per dollar”都属于厂商内部比较。没有完全一致的模型、软件、功耗与系统配置时，不应把这些倍数直接放入跨厂商绝对性能榜。

## 直接来源

- [Microsoft Blog：Maia 200，2026-01-26](https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/)
- [Microsoft Azure Infrastructure Blog：Deep dive into Maia 200](https://techcommunity.microsoft.com/blog/azureinfrastructureblog/deep-dive-into-the-maia-200-architecture/4489312)
- [Microsoft FY2026 Q3 Earnings Call](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3)
- [Microsoft Build 2026 Live Blog](https://news.microsoft.com/build-2026-live-blog)
- [Hot Chips 2026 Program](https://hc2026.hotchips.org/program/)

## 未确认项

- HBM stack 数、封装方式、die 面积与良率相关设计。
- 卡/节点级 TDP、电源和冷却形态。
- 独立 Azure Maia SKU、定价和区域 GA 清单。
- 大规模部署下的实际 scale-up oversubscription 与故障恢复细节。
- 第三方可复现的模型基准。
