# Samsung AI 内存资料

- 研究截止日：2026-09-13
- 核验日期：2026-09-13
- 厂商范围：与 AI 基础设施强相关的 PIM/AI memory；本轮重点为 LPDDR5X-PIM
- 证据原则：内存器件、PIM 运算能力、AI 加速器、服务器平台分层记录

## 芯片页关系导航

- [[lpddr5x-pim|Samsung — LPDDR5X-PIM]] · [打开 Markdown](./lpddr5x-pim.md)

## 当前结论

Samsung 在 FMS 2026 展示 LPDDR5X-PIM，并将其列入 HBM4E、HBM5 等下一代 AI memory roadmap。官方定义是把 processing-in-memory 能力加入 LPDDR5X，使部分数据处理在内存侧完成，以减少数据移动并改善能效。

当前公开材料**没有给出足够完整的 LPDDR5X-PIM 容量、带宽、PIM 计算阵列、支持算子、量产时间和客户出货信息**。因此本目录只记录已公开的产品定位和生命周期，不把 Samsung 既往 HBM-PIM 的性能数字迁移到 LPDDR5X-PIM。

## 生命周期与边界

| 阶段 | 状态 | 证据边界 |
| --- | --- | --- |
| 产品公开 | 2026-08 FMS 2026 展示 | Samsung 官方 Newsroom |
| 架构定位 | LPDDR + PIM，在内存内部处理数据 | 不等于独立 AI 加速器 |
| 样片/送样 | 公开资料未确认 | HBM4E sampling 不能套用到 LPDDR5X-PIM |
| 量产 | 公开资料未确认 | Samsung 的“从设计到量产能力”是公司能力描述，不是该产品状态 |
| 客户部署 | 公开资料未确认 | 展示不等于客户部署 |

## 与 AI 加速器的关系

PIM 的核心价值在于把部分计算移动到数据附近，缓解 host/accelerator 与内存间的数据搬运压力。是否能加速 LLM inference、embedding、attention 或数据库操作，取决于具体可编程模型和支持算子；在公开指令/编程文档出现前，不把这些潜在用途写成 LPDDR5X-PIM 已确认硬件能力。

## 直接来源

- [Samsung Global Newsroom：Samsung Unveils Next-Gen 3D-Memory Vision at FMS 2026，2026-08-05](https://news.samsung.com/global/samsung-unveils-next-gen-3d-memory-vision-at-fms-2026-charting-the-future-of-ai-infrastructure)
- [Samsung Semiconductor：FMS 2026 next-generation AI infrastructure / LPDDR5X-PIM](https://semiconductor.samsung.com/news-events/tech-blog/samsung-presents-its-vision-for-next-generation-ai-infrastructure-with-3d-memory-architecture-at-fms-2026/)
- [Hot Chips 2026 Program](https://hc2026.hotchips.org/program/)

## 待补证据

- 容量、速率、带宽、功耗与封装形态。
- PIM 单元数量、数据类型、指令/算子和编程模型。
- sampling、量产、客户导入时间表。
- 与 CPU/GPU/NPU 的一致性、互联和软件栈。
