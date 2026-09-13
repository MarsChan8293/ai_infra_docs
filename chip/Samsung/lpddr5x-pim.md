# Samsung — LPDDR5X-PIM

- 厂商总览：[Samsung](./Samsung-overview.md) · [[Samsung-overview|图谱总览]]
- 产品层级：LPDDR memory with processing-in-memory；不是独立 GPU/NPU
- 研究截止日：2026-09-13
- 核验日期：2026-09-13

## 一句话结论

Samsung 在 FMS 2026 展示 LPDDR5X-PIM，并称其为业界首款集成 Processing-in-Memory 的 LPDDR 产品。当前一手公开材料主要确认“**在内存内部执行部分数据处理，以降低数据搬运、改善能效**”这一产品方向，尚没有足够公开数据支持完整容量、带宽、PIM 算力或量产状态表。

## 已确认信息

| 字段 | 公开信息 | 边界 |
| --- | --- | --- |
| 基础内存类型 | LPDDR5X | 内存器件 |
| PIM | Processing-in-Memory | 在内存侧进行部分处理 |
| 首次重点展示 | FMS 2026 | 产品/路线公开 |
| 目标 | 改善 data movement efficiency 与 power efficiency | 厂商定位 |
| 容量 | 公开资料未确认 | 不从普通 LPDDR5X 产品推导 |
| 带宽 | 公开资料未确认 | 不从其他 Samsung HBM/PIM 产品迁移 |
| PIM 峰值算力 | 公开资料未确认 | 缺少数据类型/阵列/频率 |
| 功耗 | 公开资料未确认 | 缺少器件级数据 |

## 生命周期

Samsung 2026-08 的官方材料将 LPDDR5X-PIM 与 HBM4E、HBM5、PM1763 一起放在 AI memory roadmap 中，并表示现场展示该产品。材料同时明确 HBM4 已量产、HBM4E 已向客户送样，但**没有把同样的量产/送样状态写给 LPDDR5X-PIM**。

因此生命周期必须分开：

- 已公开/展示：确认
- sampling：公开资料未确认
- mass production：公开资料未确认
- customer shipment/deployment：公开资料未确认

## 架构边界

PIM 的意义是将部分计算推近数据，减少 memory ↔ processor 往返。但目前没有足够公开资料说明 LPDDR5X-PIM 支持哪些运算、数据类型、编程模型或 host coherency 机制，因此不能把 Samsung 既往 HBM-PIM 的 benchmark、算子和功耗数字直接复用到本产品。

## 直接来源

- [Samsung Global Newsroom：FMS 2026 AI memory roadmap，2026-08-05](https://news.samsung.com/global/samsung-unveils-next-gen-3d-memory-vision-at-fms-2026-charting-the-future-of-ai-infrastructure)
- [Samsung Semiconductor：FMS 2026 next-generation AI infrastructure](https://semiconductor.samsung.com/news-events/tech-blog/samsung-presents-its-vision-for-next-generation-ai-infrastructure-with-3d-memory-architecture-at-fms-2026/)
- [Hot Chips 2026 Program](https://hc2026.hotchips.org/program/)

## 未确认项

- LPDDR5X-PIM 容量、速率、带宽与封装。
- PIM 核心数量、数据类型、峰值算力和支持算子。
- host/accelerator 接口、一致性与软件 API。
- sampling、量产、客户部署时间表。
