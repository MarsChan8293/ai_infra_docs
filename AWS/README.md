# AWS AI 芯片研究索引


## 按芯片拆分

- [芯片拆分索引](./chip-index.md)：按芯片名称、芯片家族和产品层级导航到独立 Markdown 文件。
- [综合报告](./06-aws-trainium.md)：保留完整研究、状态矩阵、规格边界和参考来源。

拆分页只重排已有综合报告内容；发布、流片、送样、量产、出货、客户部署、云端可用和路线图仍按原报告分别记录，未确认项不做推断。
资料截止：2026-09-01。当前目录只保留 AWS Trainium / Inferentia 家族研究，主报告为 [06-aws-trainium.md](./06-aws-trainium.md)。

## 当前报告覆盖

- Inferentia v1、Trainium v1、Inferentia2、Trainium2、Trainium3，以及 Trainium4 路线图。
- 芯片、NeuronCore、HBM、片上 SRAM、DMA、NeuronLink、CC-Core、服务器、UltraServer、UltraCluster 和 Bedrock 的层级边界。
- 首次公开、预览、GA、客户部署、云端可用、路线图，以及 tape-out、送样、量产、出货、停产等公开缺口。
- Search、Reduce、Top-k、Address、Route、Gather、KV 和跨卡通信的事实与推断边界。
- AWS 官方口径、AWS/客户主张、独立公开测试和未确认字段的分层记录。

## 阅读约定

数字尽量保留来源原单位和层级；`GB` 与 `GiB` 不强行换算。平台聚合值不回填单芯片。性能/瓦、成本/Token、客户规模和“最快/最低成本”等宣传性结论，均保留其测试条件或标注为厂商/客户主张。
