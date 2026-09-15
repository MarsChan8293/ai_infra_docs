---
title: "XCENA MX1"
vendor: XCENA
object_type: computational-memory
status: poc
architecture: "CXL Type-3 + near-data RISC-V processing"
process: null
compute_units: {riscv_cores: "thousands", frequency_ghz: 1.4, vector_formats: [FP32, FP16]}
memory: {ddr5_channels: 4, speed_mt_s: 8400, dpc: 2, max_aic_capacity_tb: 2}
interconnect: {cxl: "3.2 Type-3", host: "PCIe 6.0 dual x8", storage_path: "PCIe 6.0 / NVMe"}
power: {value_w: null, scope: card_or_controller}
lifecycle: {fms_public: 2025, working_samples_plan: 2025-10, production_ready_plan: 2026}
updated: 2026-09-15
---
# XCENA MX1

> 把 CXL 内存扩展和 near-data processing 合并的 computational memory 产品。

## 核心规格
- CXL 3.2 Type-3；PCIe6 dual x8。
- 4 条 DDR5 RDIMM 通道，8400MT/s，2DPC。
- 数千颗 1.4GHz 自研 RISC-V 数据加速核，FP32/FP16 vector engine。
- 最高 2TB 是 DIMM/AIC 配置容量，不是控制器 die 内置 DRAM。

## 生命周期与边界
- 当前产品 brief 明确为 PoC，部分功能标注 production 才支持。
- 2026 production-ready 是计划，不等于已经大规模量产。

## 直接来源
- https://xcena.com/computational_memory
- https://www.xcena.com/newsroom/?bmode=view&idx=170962702&t=board
