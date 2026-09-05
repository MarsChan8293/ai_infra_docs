# FuriosaAI — RNGD Gen 2

- 产品层级：AI 推理加速器
- 资料状态：从历史架构资料恢复的证据页；量产状态以当前官方产品页和公告复核

## 当前可确认摘要

| 字段 | 内容 | 边界 |
| --- | --- | --- |
| 执行架构 | Tensor Contraction Processor、Tensor DMA、Fetch network、Virtual ISA | TCP 不是 Search/Top-k 加速器 |
| 内存 | 旧版资料记录 48 GB HBM3、1.5 TB/s；256 MB SRAM | 带宽峰值不等于离散 Gather 已解决 |
| 软件 | 编译器负责 sharding、broadcast、reuse 与 pipeline；HbmTensor 提供 indexed-gather API | SDK/API 不能升级为硬件 page translator |
| 功耗 | 旧资料同时出现 150 W 与 180 W | 两个口径必须并列，不能选择一个覆盖所有版本 |
| 状态 | 旧版资料记录 2026-01 进入量产并交付首批；下一代仍在开发 | 需重新核验当前 GA、出货量和客户部署 |

## 来源

- [RNGD 当前规格页](https://furiosa.ai/renegade-spec)
- [RNGD 开发者文档](https://developer.furiosa.ai/latest/en/overview/rngd.html)
- [Tensor Contraction Processor 论文](https://furiosa.ai/download/FuriosaAI-tensor-contraction-processor-isca24)
- [RNGD 进入量产公告](https://furiosa.ai/blog/rngd-enters-mass-production-the-high-performance-ai-accelerator-for-any-data-center)

## 路线边界

下一代 HBM4/2 nm 平台和 NPUaaS/SDK 不能写成 RNGD Gen 2 的新芯片规格。公开材料未确认硬件 Retrieval Core、硬件 Top-k、KV page translator 或 candidate-aware merge collective。
