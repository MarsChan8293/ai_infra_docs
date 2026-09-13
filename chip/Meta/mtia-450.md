# Meta — MTIA 450

- 厂商总览：[Meta](./Meta-overview.md) · [[Meta-overview|图谱总览]]
- 产品层级：Meta 自研 GenAI inference 优先加速器
- 研究截止日：2026-09-13
- 核验日期：2026-09-13

## 产品定位

MTIA 450 从 MTIA 400 演进而来，把优化重心进一步转向 GenAI inference，尤其是 decode、MoE FFN、attention 和低精度计算。

## 官方公开的代际增量

| 相对 MTIA 400 | MTIA 450 增量 | 边界 |
| --- | --- | --- |
| HBM bandwidth | 2× | 相对值，不等于已公开绝对 TB/s |
| MX4 FLOPS | +75% | 厂商相对峰值 |
| 低精度 | MX4 等进一步优化 | 不能与不同数据类型直接混比 |
| Attention/FFN | 加入硬件加速以缓解 Softmax、FlashAttention 等瓶颈 | 公开的是能力方向，不等于完整微架构 |

Meta 还称 MTIA 450 的 MX4 FLOPS 为同一设备 FP16/BF16 的 6×。这说明低精度是设计核心，但依然是**精度不同的峰值比值**，不是“所有模型快 6×”。

## 生命周期

| 阶段 | 状态 |
| --- | --- |
| 公开 | 2026-03-11 官方公开路线与架构增量 |
| 工程验证 | 公开资料未给出完整阶段 |
| 量产/大规模部署 | **计划 2027 年初 mass deployment** |
| 当前生产部署 | 截至公开材料不应写成已完成 |
| 外部销售 | 未公开，主要面向 Meta 内部基础设施 |

## 系统关系

Meta 表示 MTIA 400、450、500 复用 chassis、rack 与 network infrastructure。这个复用策略可以缩短部署切换时间，但属于系统平台属性，不能据此推导 MTIA 450 的单芯片接口数量或带宽。

## 直接来源

- [Meta AI：Four MTIA Chips in Two Years，2026-03-11](https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/)

## 未确认项

- 绝对 HBM 容量/带宽、MX4/FP8/BF16 峰值。
- chiplet 数量、工艺、封装、TDP。
- 2027 年初 mass deployment 是否按计划发生。
- attention/FFN 加速单元的具体数据流与指令模型。
