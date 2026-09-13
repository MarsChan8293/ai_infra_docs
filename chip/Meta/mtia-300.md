# Meta — MTIA 300

- 厂商总览：[Meta](./Meta-overview.md) · [[Meta-overview|图谱总览]]
- 产品层级：Meta 自研 AI 加速器
- 研究截止日：2026-09-13
- 核验日期：2026-09-13

## 产品定位与状态

MTIA 300 最初针对 Meta 的 ranking & recommendation（R&R）工作负载设计，目前官方明确为**已在生产环境用于 R&R training**。它也是 MTIA 400/450/500 快速迭代路线的基础。

## 架构组成

官方公开 MTIA 300 由：

- 1 个 compute chiplet
- 2 个 network chiplet
- 多组 HBM stack

组成。compute chiplet 内部是 Processing Element（PE）网格，并包含冗余 PE 以改善良率。

每个 PE 已公开包含：

| 单元 | 作用 |
| --- | --- |
| 2× RISC-V vector cores | 通用/向量控制与计算 |
| Dot Product Engine | 矩阵乘/点积 |
| Special Function Unit | activation 与 elementwise 操作 |
| Reduction Engine | 累加与 PE 间通信 |
| DMA engine | local scratch memory 数据搬运 |

MTIA 300 还引入 built-in NIC chiplet、collective message engine 与 near-memory reduction，说明 Meta 从这一代开始就把 scale-up/scale-out 通信视为加速器设计的一部分。

## 公开状态与边界

| 字段 | 状态 |
| --- | --- |
| R&R training | 已在生产 |
| GenAI inference | 后续代际重点；不能把 400/450 的优化回填 300 |
| HBM 绝对容量/带宽 | 本页不从图表图片 OCR；等待可直接核验表格/论文 |
| 功耗 | 公开资料未确认 |
| 制造节点 | 本轮一手材料未确认 |
| Scale-up | 有片间通信设计；不要把后续 72-device MTIA 400 rack 写给 300 |

Meta 在文章脚注指出 MTIA 300 配置了 200GB/s 的较高 scale-out network bandwidth，以适配其相对较小的 scale-up domain 与 R&R 目标工作负载。该数字是网络配置口径，不是 HBM 带宽。

## 直接来源

- [Meta AI：Four MTIA Chips in Two Years，2026-03-11](https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/)
- [Meta AI：Next Generation MTIA，2024-04-10](https://ai.meta.com/blog/next-generation-meta-training-inference-accelerator-AI-MTIA/)

## 未确认项

- 绝对 MX8/FP8/BF16 算力、HBM 容量/带宽。
- 工艺、die 面积、封装、TDP。
- 生产部署总量和系统节点配置。
