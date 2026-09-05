# Google TPU 研究索引

本目录记录 Google TPU 产品家族、Ironwood/TPU7x、TPU 8t、TPU 8i 的公开资料与架构证据，截止日为 2026-09-01。

## 文档

- [03-google-ironwood.md](03-google-ironwood.md)：主报告。包含产品状态矩阵、芯片/板卡/主机/Pod/云服务层级拆分、规格冲突、软件栈、厂商实测、MLPerf 独立基准边界，以及 Search / Reduce / Top-k / Address / Route / Gather / KV 对附件 Retrieval Plane 的证据映射。
- [Hot Chips 2026 对照](../hot-chips-2026.md)：第八代 TPU 议程、Coming soon 状态和待公开演讲材料边界。

## 阅读口径

- `[官方事实]` 只表示来源页面直接写明的事实。
- `[厂商主张]` 包含 Google 峰值、相对性能、价格性能、性能/瓦和自家实测。
- `[独立基准]` 仅在 MLCommons/MLPerf 页面或 run 记录能完成硬件归因时使用；不能把“Google 参与”写成“Ironwood 已有独立分数”。
- `[分析判断]` 是面向 Retrieval/Data-Movement Plane 的推导，不是 Google 产品承诺。
- `[未确认]` 表示公开资料不足，尤其是流片、量产、出货数量、TPU 8t/8i 客户生产部署和 Ironwood 的 run 级独立基准归因。

## 关键当前状态

截至 2026-09-01，Google Cloud 产品页将 Ironwood 标为 Generally available，将 TPU 8t 与 TPU 8i 标为 Coming soon。请以主报告中的状态矩阵和来源链接为准，不将路线图、峰值规格或客户计划容量写成已出货事实。

## 按芯片拆分

- [芯片拆分索引](./Google-chip-index.md)：按芯片名称、芯片家族和产品层级导航到独立 Markdown 文件。
- [综合报告](./03-google-ironwood.md)：保留完整研究、状态矩阵、规格边界和参考来源。

拆分页只重排已有综合报告内容；发布、流片、送样、量产、出货、客户部署、云端可用和路线图仍按原报告分别记录，未确认项不做推断。
