# d-Matrix — Corsair

- 产品层级：AI 推理加速器平台；页面中的双卡、服务器和机架不是单芯片对象
- 研究截止日：2026-09-05
- 核验日期：2026-09-05
- 页面性质：基于直接来源整理的自包含证据页；芯片、平台、系统和云服务分层记录

## 产品定位与对象边界

| 字段 | 内容 | 边界 |
| --- | --- | --- |
| 计算路线 | DIMC，把部分计算放在 SRAM 附近 | 不能据此推导动态 Search、Top-k 或 KV page Gather |
| 性能内存 | 2 GB SRAM Performance Memory，厂商给出 150 TB/s 口径 | 只适用于该小容量性能内存，不代表所有容量内存 |
| 容量内存 | LPDDR5，厂商资料给出最高 256 GB、400 GB/s 口径 | 平台/双卡配置数字不能回填单芯片 |
| 执行与互联 | DIMC、SIMD、RISC-V、Dispatch/Data Reshape、chiplet、DMX Bridge | JetStream 是独立 I/O 设备，需单独记录 |
| 生命周期 | 2026-06 公告称 full production，仍写 select/qualified customers | full production 不等于所有客户 GA 或普遍可购 |

## 生命周期状态

| 阶段 | Corsair 的公开状态 | 证据边界 |
| --- | --- | --- |
| 宣布/平台发布 | 官方产品页与公告公开 Corsair 平台定位 | 平台公开不等于裸芯片完整规格公开 |
| 流片/工程样片 | 公开资料未确认独立流片或样片批次 | 不能从 DIMC 白皮书推导制造节点或批次 |
| 量产 | 2026-06 官方公告使用 “full production” 表述 | 这是平台/商业交付表述，不自动等同于裸芯片大规模量产 |
| 出货/客户部署 | 公告称面向 select/qualified customers；独立出货量和部署清单未确认 | 保留厂商口径，不升级为普遍可购或广泛部署 |
| 云/实例可用 | 公开资料未确认 | 平台公告不等于公有云实例 |
| 路线图 | Pavehawk 作为下一代 3D DIMC 路线单独记录 | 不把 Pavehawk 的方向性材料回填为 Corsair 规格 |

## 直接来源

- [Corsair full production 公告](https://www.d-matrix.ai/announcements/d-matrix-corsair-ai-inference-platform-enters-full-production-to-meet-customer-demand/)
- [Corsair 产品页](https://www.d-matrix.ai/product/)
- [Corsair 技术白皮书](https://d-matrix.ai/pdf/d-Matrix-WhitePaper-Technical-FINAL.pdf)

## 证据边界

公开资料支持“memory-centric / DIMC / 分层内存”的架构判断；尚未支持硬件原生索引器、流式 Top-k、KV 页地址转换或候选感知 collective。60,000 tokens/s、10×/3× 等相对数字必须保留模型、上下文、批大小和基线，不能作为通用端到端性能。
