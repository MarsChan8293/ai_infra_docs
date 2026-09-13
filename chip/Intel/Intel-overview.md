# Intel 芯片资料

- 研究截止日：2026-09-13
- 核验日期：2026-09-13
- 厂商范围：Intel 数据中心 AI 加速器；当前优先补齐 Hot Chips 2026 明确出现的 Crescent Island
- 证据原则：芯片、PCIe 卡、服务器与集群分层；官方未披露字段保持“公开资料未确认”

## 芯片页关系导航

本页是本目录唯一的厂家总览。芯片页中的“厂商总览”链接回到本页；`[[...]]` 用于 Obsidian 图谱。

- [[crescent-island|Intel — Crescent Island]] · [打开 Markdown](./crescent-island.md)

## 当前结论

Intel 在 Hot Chips 2026 公开了 Crescent Island 的核心配置，将其定位为面向数据中心实时 AI 推理、强调较高内存容量与现有风冷机房适配的 GPU。公开规格包括 **Xe3P、32 个 Xe Core、256 个 XMX 引擎、最高 480GB LPDDR5X，以及 350W 风冷 PCIe 卡**。

需要特别防止一个常见误写：同一篇 Intel Hot Chips 文章还介绍了采用 Intel 18A 的 Wildcat Lake 等产品，但该页面**没有把 18A 制程明确写给 Crescent Island**。因此本资料库不把 18A、Foveros Direct 3D 或 UCIe 自动回填为 Crescent Island 的芯片规格。

## 生命周期与边界

| 对象 | 当前状态 | 证据边界 |
| --- | --- | --- |
| Crescent Island | 已公开架构与卡级关键规格 | Hot Chips 2026 官方 Intel 材料可核验 |
| 裸芯片制程节点 | 公开资料未确认 | 不从同页其他 Intel 产品推导 |
| 工程样片/送样 | 公开资料未确认 | Hot Chips 演讲不等于 sampling |
| 量产/出货 | 公开资料未确认 | 产品规格公开不等于商业出货 |
| 云实例/客户部署 | 公开资料未确认 | 未找到 Intel 官方 GA/部署清单 |

## 软件与生态

Crescent Island 基于 Intel Xe/XMX 路线，但截至本次核验，公开材料更集中于硬件定位与卡级规格。本资料库暂不把 oneAPI、驱动或通用 Intel GPU 软件能力直接写成 Crescent Island 独占或已经完成验证的硬件能力；待 Intel 发布对应产品软件支持矩阵后再补。

## 直接来源

- [Intel：Intel Outlines Architectures for Agentic AI at Hot Chips 2026，2026-08-24](https://www.intel.com/content/www/us/en/newsroom/news/client-computing/intel-outlines-architectures-for-agentic-ai-at-hot-chips-2026.html)
- [Hot Chips 2026 Program](https://hc2026.hotchips.org/program/)

## 待补证据

1. Crescent Island 的制造节点、晶体管规模、die/chiplet 组织与封装信息。
2. FP8/BF16/INT8 等峰值算力及其是否为稀疏口径。
3. LPDDR5X 总带宽、PCIe 代际与卡级互联细节。
4. sampling、量产、实际出货和客户部署状态。
5. 对应驱动、编译器和框架版本的官方支持矩阵。
