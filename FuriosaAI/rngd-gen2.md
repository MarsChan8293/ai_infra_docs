# FuriosaAI — RNGD Gen 2

- 产品层级：AI 推理加速器
- 研究截止日：2026-09-05
- 核验日期：2026-09-05
- 页面性质：基于直接来源整理的自包含证据页；芯片、加速卡、软件和云服务分层记录

## 产品定位与对象边界

| 字段 | 内容 | 边界 |
| --- | --- | --- |
| 执行架构 | Tensor Contraction Processor、Tensor DMA、Fetch network、Virtual ISA | TCP 不是 Search/Top-k 加速器 |
| 内存 | 旧版资料记录 48 GB HBM3、1.5 TB/s；256 MB SRAM | 带宽峰值不等于离散 Gather 已解决 |
| 软件 | 编译器负责 sharding、broadcast、reuse 与 pipeline；HbmTensor 提供 indexed-gather API | SDK/API 不能升级为硬件 page translator |
| 功耗 | 旧资料同时出现 150 W 与 180 W | 两个口径必须并列，不能选择一个覆盖所有版本 |
| 状态 | 旧版资料记录 2026-01 进入量产并交付首批；下一代仍在开发 | 需重新核验当前 GA、出货量和客户部署 |

## 生命周期状态

| 阶段 | RNGD Gen 2 的公开状态 | 证据边界 |
| --- | --- | --- |
| 宣布/规格披露 | 直接来源公开了 RNGD 规格、架构和产品定位 | 以来源页面原文为准 |
| 流片/工程样片 | 公开资料未确认 | 不能从规格页或论文倒推流片批次 |
| 量产/首批交付 | 历史资料记录 2026-01 进入量产并交付首批 | 属历史资料记录；当前官方 GA、批量出货量和客户名单未重新确认 |
| 客户部署 | 公开资料未确认 | 不能用“交付首批”替代可核验客户部署证据 |
| 云/实例可用 | 公开资料未确认 | NPUaaS/SDK 路线不等于 RNGD Gen 2 云实例 |
| 路线图 | 下一代仍在开发 | 不回填为 RNGD Gen 2 的新增规格 |

## 直接来源

- [RNGD 当前规格页](https://furiosa.ai/renegade-spec)
- [RNGD 开发者文档](https://developer.furiosa.ai/latest/en/overview/rngd.html)
- [Tensor Contraction Processor 论文](https://furiosa.ai/download/FuriosaAI-tensor-contraction-processor-isca24)
- [RNGD 进入量产公告](https://furiosa.ai/blog/rngd-enters-mass-production-the-high-performance-ai-accelerator-for-any-data-center)

## 证据边界

下一代 HBM4/2 nm 平台和 NPUaaS/SDK 不能写成 RNGD Gen 2 的新芯片规格。公开材料未确认硬件 Retrieval Core、硬件 Top-k、KV page translator 或 candidate-aware merge collective。
