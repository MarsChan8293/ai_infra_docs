# Meta — MTIA 500

- 厂商总览：[Meta](./Meta-overview.md) · [[Meta-overview|图谱总览]]
- 产品层级：Meta 自研 GenAI inference 优先加速器 / 2027 路线
- 研究截止日：2026-09-13
- 核验日期：2026-09-13

## 产品定位

MTIA 500 延续 MTIA 450 的 GenAI inference 优先路线，在 HBM、MX4 计算与模块化 chiplet 组织上继续加强。它当前仍属于明确公开但**计划 2027 年大规模部署**的未来代际，不应提前写成量产或已部署。

## 官方公开增量

相对 MTIA 450：

- HBM bandwidth **+50%**
- HBM capacity **最高 +80%**
- MX4 FLOPS **+43%**
- 进一步增加低精度格式与硬件加速能力

这些是相对代际指标，不是已公开的绝对 TB/s、GB 或 PFLOPS 值。

## Chiplet 组织

Meta 公开 MTIA 500 采用更模块化的组织：

- 2×2 配置的较小 compute chiplets
- 多组 HBM stacks
- 2 个 network chiplets
- 1 个 SoC chiplet，用于连接 host CPU 的 PCIe 与 scale-out NICs

这种拆分把计算、网络和 host I/O 分离到不同 chiplet，有利于独立迭代。但官方公开材料不足以确认每颗 compute chiplet 的 PE 数量、工艺节点或 die 面积。

## 生命周期

| 阶段 | 状态 |
| --- | --- |
| 路线公开 | 2026-03-11 已公开 |
| 流片/工程样片 | 公开资料未确认 |
| 大规模部署 | 计划 2027 年 mass deployment |
| 当前生产部署 | 未确认，不应提前升级 |
| 外部销售 | 未公开，主要面向 Meta 内部基础设施 |

## 系统边界

MTIA 500 与 400/450 复用 chassis、rack 和 network infrastructure。该兼容性属于平台设计策略，不等于 MTIA 500 与旧代芯片的片上接口完全相同。

## 直接来源

- [Meta AI：Four MTIA Chips in Two Years，2026-03-11](https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/)

## 未确认项

- 绝对 HBM 容量/带宽与 MX4/FP8/BF16 峰值。
- 工艺、封装、TDP、chiplet die 面积。
- scale-up/scale-out 链路绝对带宽和拓扑。
- 2027 mass deployment 的实际执行状态。
