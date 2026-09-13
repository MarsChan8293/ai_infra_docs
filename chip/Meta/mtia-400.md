# Meta — MTIA 400

- 厂商总览：[Meta](./Meta-overview.md) · [[Meta-overview|图谱总览]]
- 产品层级：Meta 自研 AI 加速器；72-device scale-up 单列为机架/系统层
- 研究截止日：2026-09-13
- 核验日期：2026-09-13

## 产品定位

MTIA 400 是 Meta 从 R&R 优先转向更广泛 GenAI 工作负载的重要一代。官方称其在 MTIA 300 基础上实现 **FP8 FLOPS 提升 400%**、**HBM 带宽提升 51%**，并由两个 compute chiplet 提升计算密度，同时增强 MX8/MX4 低精度支持。

这些都是相对 MTIA 300 的厂商口径，不能直接转换成跨厂商绝对性能排名。

## 系统边界

Meta 公开的代表性系统是 **72 颗 MTIA 400 组成一个 scale-up domain**，通过 switched backplane 连接，并与网络设备和 air-assisted liquid cooling（AALC）机架共同组成 rack-scale 系统。

72 是系统级加速器数量，不是 MTIA 400 的核心数、chiplet 数或片上互联端口数。

## 生命周期

| 阶段 | 状态 |
| --- | --- |
| 设计/硅验证 | 已完成实验室测试 |
| 数据中心部署 | 官方表述为“on the path to deploying it in our data centers” |
| 大规模生产部署 | 截至 2026-03 官方未写成已大规模部署 |
| 外部可采购性 | 不适用/未公开；MTIA 是 Meta 内部基础设施芯片 |

## 架构增量

- 2 个 compute chiplet
- 相对 MTIA 300：FP8 FLOPS +400%
- 相对 MTIA 300：HBM bandwidth +51%
- 增强 MX8 / MX4 低精度格式
- 72-device scale-up rack/domain

## 直接来源

- [Meta AI：Four MTIA Chips in Two Years，2026-03-11](https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/)

## 未确认项

- 绝对 HBM 容量、带宽与各精度 FLOPS 的可文本核验表。
- 工艺、封装、TDP。
- 数据中心正式部署时间、数量与生产状态。
- 72-device switched backplane 的链路规格和拓扑细节。
