# Chip Schema V0.1

每个对象 Markdown 的 YAML frontmatter 至少包含：`title`、`vendor`、`object_type`、`status`、`architecture`、`process`、`memory`、`compute`、`interconnect`、`power`、`lifecycle`、`updated`。

`object_type` 用于区分 `chip`、`accelerator`、`board`、`module`、`system`、`soc`、`ip`、`network_asic`、`memory` 等层级。`status` 建议使用 `roadmap`、`announced`、`sampling`、`production`、`shipping`、`ga`、`legacy`、`eol`、`unknown`。

正文固定为：一句话结论 → 核心规格 → 生命周期与边界 → 直接来源。未知字段不得由相邻 SKU、板卡或系统数据推导。
