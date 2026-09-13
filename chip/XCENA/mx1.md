# XCENA — MX1 CXL Computational Memory

- 厂商总览：[XCENA](./XCENA-overview.md) · [[XCENA-overview|图谱总览]]
- 产品层级：CXL Type-3 computational memory / near-data processing AIC
- 研究截止日：2026-09-13
- 核验日期：2026-09-13

## 一句话结论

MX1 把 **CXL 3.2 memory expansion、数千颗自研 RISC-V 数据处理核、FP32/FP16 vector engine 与 SSD-backed memory tier** 放在同一 computational-memory 产品中。当前官网规格仍明确标为 **MX1 PoC Product Brief**，因此它更适合记录为正在产品化/伙伴验证的 CXL computational-memory 平台，而不是已经完全定型的大规模量产器件。

## 当前官网 PoC 规格

| 字段 | 公开信息 | 边界 |
| --- | --- | --- |
| CXL | CXL 3.2 Type-3 HDM-DB | 主机内存扩展/一致性路径 |
| 主机接口 | PCIe 6.0 dual x8 | AIC/控制器侧 |
| 设备/SSD 接口 | PCIe 6.0 dual x4，NVMe | secondary storage path |
| DRAM | DDR5 RDIMM ×4，8400MT/s，2DPC | 板卡内存通道配置 |
| 总容量 | up to 2TB（256GB DIMM, 2DPC） | AIC/内存配置，不是片上 SRAM |
| NDP 处理器 | 数千颗自研 1.4GHz RISC-V cores | near-data processing |
| Vector | FP32 / FP16 vector engines | 公开能力；峰值未公开 |
| 管理处理器 | dual Cortex-A53 | 管理平面 |
| 压缩 | LZ4 hardware-assisted decompression；RISC-V software compression | 数据路径 |
| AIC | FHHL DW，4 DIMM | 板卡形态 |

## InfiniteMemory 边界

XCENA 还提供 SSD-backed 的 InfiniteMemory 路径，用独立 PCIe 6.0/NVMe 接口把更大的 SSD 容量纳入 memory hierarchy。厂商使用“petabyte-scale”描述其可扩展目标；这是**系统可访问容量层次**，绝不是 MX1 芯片本身拥有 PB 级 DRAM。

## 生命周期

| 阶段 | 状态 |
| --- | --- |
| FMS 2025 展示 | 已公开 MX1 |
| working samples | 2025 年公告称从 10 月起向 select partners 提供 |
| 2026 production-ready | 2025 公告中的计划 |
| 当前官网 | 仍提供“MX1 PoC Product Brief”，部分功能注明 production 才支持 |
| 伙伴/系统验证 | 2026 有 KISTI 等合作验证信息 |
| 大规模量产/广泛 GA | 本次公开资料未充分确认 |

“production-ready 计划 2026”不能自动改写成“2026 已大规模量产”。尤其官网仍区分 PoC 与 production-supported feature，说明版本边界需要继续追踪。

## 软件栈

XCENA SDK 提供多层 API、仿真/模拟、OS drivers 与 low-level device API。官网列举：

- KV Cache Offloading
- RAG / Vector DB Acceleration
- Data Analytics Acceleration

这些是**应用示例/软件方向**。没有统一硬件、数据集、模型、batch 与基线时，不把“可 offload”直接升级为固定性能倍数。

## 直接来源

- [XCENA：MX1 Computational Memory](https://xcena.com/computational_memory)
- [XCENA：MX1 working samples / production-ready plan](https://www.xcena.com/newsroom/?bmode=view&idx=170962702&t=board)
- [XCENA：SDK Overview](https://xcena.com/sdk_overview)
- [XCENA：KISTI 验证合作](https://www.xcena.com/newsroom/?bmode=view&idx=170962754&t=board)

## 未确认项

- production 版本最终 CXL feature matrix 与 PoC 差异。
- 制造节点、TDP、die/chiplet 组织。
- FP32/FP16 vector engine 数量和峰值吞吐。
- 实际商业客户、量产出货规模与端到端 benchmark。
