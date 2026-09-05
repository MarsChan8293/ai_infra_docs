# d-Matrix — Corsair

- 产品层级：AI 推理加速器平台；页面中的双卡、服务器和机架不是单芯片对象
- 资料状态：历史研究条目恢复页；数字与状态需在 HC2026 材料公开后重新核验

## 当前可确认摘要

| 字段 | 内容 | 边界 |
| --- | --- | --- |
| 计算路线 | DIMC，把部分计算放在 SRAM 附近 | 不能据此推导动态 Search、Top-k 或 KV page Gather |
| 性能内存 | 2 GB SRAM Performance Memory，厂商给出 150 TB/s 口径 | 只适用于该小容量性能内存，不代表所有容量内存 |
| 容量内存 | LPDDR5，厂商资料给出最高 256 GB、400 GB/s 口径 | 平台/双卡配置数字不能回填单芯片 |
| 执行与互联 | DIMC、SIMD、RISC-V、Dispatch/Data Reshape、chiplet、DMX Bridge | JetStream 是独立 I/O 设备，需单独记录 |
| 生命周期 | 2026-06 公告称 full production，仍写 select/qualified customers | full production 不等于所有客户 GA 或普遍可购 |

## 证据链接

- [Corsair full production 公告](https://www.d-matrix.ai/announcements/d-matrix-corsair-ai-inference-platform-enters-full-production-to-meet-customer-demand/)
- [Corsair 产品页](https://www.d-matrix.ai/product/)
- [Corsair 技术白皮书](https://d-matrix.ai/pdf/d-Matrix-WhitePaper-Technical-FINAL.pdf)

## 研究边界

公开资料支持“memory-centric / DIMC / 分层内存”的架构判断；尚未支持硬件原生索引器、流式 Top-k、KV 页地址转换或候选感知 collective。60,000 tokens/s、10×/3× 等相对数字必须保留模型、上下文、批大小和基线，不能作为通用端到端性能。
