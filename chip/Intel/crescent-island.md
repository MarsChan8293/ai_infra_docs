# Intel — Crescent Island

- 厂商总览：[Intel](./Intel-overview.md) · [[Intel-overview|图谱总览]]
- 产品层级：数据中心 AI 推理 GPU / PCIe 加速卡
- 研究截止日：2026-09-13
- 核验日期：2026-09-13
- 页面性质：官方公开规格证据页；未公开项不从同场其他 Intel 产品推导

## 一句话结论

Crescent Island 是 Intel 面向数据中心实时/agentic AI 推理的 Xe3P GPU 路线，当前最清晰的公开配置是 **32 Xe cores、256 XMX engines、最高 480GB LPDDR5X 和 350W 风冷 PCIe 卡**。公开材料尚不足以确认制造节点、各精度峰值算力、内存带宽、量产出货和云部署状态。

## 已确认规格

| 字段 | 官方公开信息 | 层级/边界 |
| --- | --- | --- |
| 架构 | Xe3P | GPU 架构 |
| Xe Core | 32 | 芯片/加速器级 |
| XMX engine | 256 | 芯片/加速器级 |
| 内存 | 最高 480GB LPDDR5X | PCIe 产品配置；具体颗粒/总线未公开 |
| 功耗 | 350W | 风冷 PCIe card 口径 |
| 主要定位 | 数据中心 AI inference、agentic AI、较长上下文/高并发 | 厂商定位，不是 benchmark |
| 部署形态 | 可适配现有 air-cooled data-center footprint | 卡/系统部署主张 |
| 制造节点 | 公开资料未确认 | 不使用同篇文章里 Wildcat Lake 的 Intel 18A 信息 |
| 峰值 AI 算力 | 公开资料未确认 | 不从 XMX 数量自行估算 |
| LPDDR5X 带宽 | 公开资料未确认 | 不能只凭容量反推 |

## 生命周期

| 阶段 | 状态 | 说明 |
| --- | --- | --- |
| 产品/代号公开 | 已公开 | Intel 已公开 Crescent Island 并在 Hot Chips 2026 讲解 |
| 架构/关键规格公开 | 已公开 | 2026-08 Intel Newsroom 给出核心、XMX、内存与卡功耗 |
| 流片/工程样片 | 公开资料未确认 | 演讲不等于样片状态 |
| sampling | 公开资料未确认 | 未发现 Intel 官方 sampling 公告 |
| 量产 | 公开资料未确认 | 不能从“产品公开”升级 |
| 出货/客户部署 | 公开资料未确认 | 尚缺客户或 SKU 可购证据 |
| 云实例 | 公开资料未确认 | 尚缺公有云实例证据 |

## 架构判断

480GB LPDDR5X 是 Crescent Island 最显著的公开差异化参数之一，明显强调推理场景的模型驻留与上下文容量。LPDDR5X 的选择也说明 Intel 在该产品上优先考虑容量、能效、风冷可部署性等约束，而不是简单复制 HBM 型训练 GPU 的产品形态。

但“更大模型、更长上下文、更多并发 agent”仍属于厂商对使用场景的描述。没有模型、batch、context、量化格式和软件版本时，不能把这些表述转换为固定 tokens/s 或成本优势。

## 直接来源

- [Intel：Intel Outlines Architectures for Agentic AI at Hot Chips 2026，2026-08-24](https://www.intel.com/content/www/us/en/newsroom/news/client-computing/intel-outlines-architectures-for-agentic-ai-at-hot-chips-2026.html)
- [Intel 中文 Newsroom：Hot Chips 2026 架构布局](https://newsroom.intel.com/zh-cn/客户端计算/三大架构同台亮相！英特尔hot-chips-2026详解智能体ai架构创新)
- [Hot Chips 2026 Program](https://hc2026.hotchips.org/program/)

## 后续核验清单

- 制造工艺、die/chiplet、封装。
- FP8/BF16/INT8/INT4 峰值与稀疏口径。
- LPDDR5X 总带宽与内存通道组织。
- PCIe 版本、卡间互联与网络适配方式。
- sampling、量产、出货、客户/云部署。
- oneAPI/框架/驱动的正式支持矩阵。
