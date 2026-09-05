# Google / 谷歌 — TPU v5p

- 拆分日期：2026-09-02
- 产品层级：TPU ASIC/Cloud TPU
- 综合报告：[03-google-ironwood.md](./03-google-ironwood.md)
- 文件性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容逐行摘录综合报告，保留原报告中的状态、数字、证据等级和未知项。

> 第 128 行：|---|---|---|---|---|---|---|
> 第 129 行：| TPU v5p | ASIC/芯片、Pod、Cloud TPU 服务 | 2023-12-06 发布 | **[未确认]** Google 未公开独立流片或量产日期 | **[官方事实]** 2023 年已向 Cloud customers 提供；曾用于 Salesforce 等客户训练 | **[官方事实]** Cloud TPU v5p 已 GA；当前不是最新主力 | 上一代性能基线 |
> 第 130 行：| TPU v6e / Trillium | ASIC/芯片、Pod、Cloud TPU 服务 | 2024-05-14 宣布；2024-12-11 GA | **[未确认]** | **[官方事实]** GA，Google 称用于训练 Gemini 2.0；独立出货数量未公开 | **[官方事实]** GA | Ironwood 的上一代可用产品 |
> 第 213 行：12. [Trillium GA 公告](https://cloud.google.com/blog/products/compute/trillium-tpu-is-ga)
> 第 214 行：13. [TPU v5p 架构文档](https://docs.cloud.google.com/tpu/docs/v5p)

## 直接来源链接

1. <https://cloud.google.com/blog/products/compute/trillium-tpu-is-ga)>
2. <https://docs.cloud.google.com/tpu/docs/v5p)>

## 证据边界

- 这是资料重排页，不是重新发布或重新核验的产品公告。
- “发布、流片、送样、量产、出货、客户部署、云端可用、路线图、停产”等状态只在综合报告明确写出时保留；缺失项仍为“公开资料未确认”。
- 若摘录同时出现芯片、板卡、服务器、机架或云服务，均按原报告层级保留，并以“产品层级”字段提醒，不做跨层级推导。

## 关联表格原文（完整表格）

以下表格块来自综合报告中与本拆分项命中的表格，完整保留表头、状态列和规格列。

> 来源综合报告第 127-134 行：
> 第 127 行：| 产品 | 产品层级 | 首次披露/发布 | 流片/量产 | 出货/客户部署 | 云端状态 | 窗口内定位 |
> 第 128 行：|---|---|---|---|---|---|---|
> 第 129 行：| TPU v5p | ASIC/芯片、Pod、Cloud TPU 服务 | 2023-12-06 发布 | **[未确认]** Google 未公开独立流片或量产日期 | **[官方事实]** 2023 年已向 Cloud customers 提供；曾用于 Salesforce 等客户训练 | **[官方事实]** Cloud TPU v5p 已 GA；当前不是最新主力 | 上一代性能基线 |
> 第 130 行：| TPU v6e / Trillium | ASIC/芯片、Pod、Cloud TPU 服务 | 2024-05-14 宣布；2024-12-11 GA | **[未确认]** | **[官方事实]** GA，Google 称用于训练 Gemini 2.0；独立出货数量未公开 | **[官方事实]** GA | Ironwood 的上一代可用产品 |
> 第 131 行：| TPU7x / Ironwood | 双 chiplet ASIC、三芯片板、4 芯片/VM、Pod、Cloud TPU 服务 | 2025-04-09 首次披露（早于窗口） | **[未确认]** 没有 Google 独立量产/流片日期 | **[官方事实]** 2025-11-24 Preview；2026-03-31 GA；Cloud 文档/GKE 已有可用配置 | **[官方事实]** 产品页为 Generally available；仍可能需要 quota/reservation/access | 窗口内主力可用产品 |
> 第 132 行：| TPU 8t | ASIC/专用训练系统、9,600 芯片 Superpod、Virgo scale-out、Cloud TPU 目标服务 | 2026-04-22 宣布 | **[未确认]** | **[未确认]** 没有公开出货或客户生产部署证据 | **[官方事实]** 产品页仍为 Coming soon；Google 仅称稍后/即将提供 | 窗口内最新训练路线 |
> 第 133 行：| TPU 8i | ASIC/专用推理/RL 系统、Boardfly Pod、Cloud TPU 目标服务 | 2026-04-22 宣布 | **[未确认]** | **[未确认]** 没有公开出货或客户生产部署证据 | **[官方事实]** 产品页仍为 Coming soon | 窗口内最新推理路线 |
> 第 134 行：| 更后续 TPU | 未见当前产品页列出 | **[未确认]** | **[未确认]** | **[未确认]** | **[未确认]** | 不以传闻或供应链消息补齐 |
