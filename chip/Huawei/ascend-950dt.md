---
title: "Huawei Ascend 950DT"
vendor: Huawei
object_type: chip
status: announced
architecture: "Ascend 950"
process: null
compute_units: {ai_subsystems_max: 36, cube_variants: [36,32,28], vector_variants: [72,64,56]}
memory: {technology: "HiZQ 2.0", max_capacity_gb: 144, max_bandwidth_tb_s: 4.0, l2_mb: 128}
compute: {mxfp4_tflops: [2007,1784,1561], fp8_tflops: [1034,919,804], bf16_tflops: [547,486,425]}
interconnect: {unified_bus_2_0_gb_s_bidirectional: 2016, pcie: "Gen5 x16, 128GB/s bidirectional"}
power: {value_w: null, scope: chip}
lifecycle: {announced: 2025-09-18, planned_launch: 2026-Q4, mass_production: null}
updated: 2026-09-15
---
# Huawei Ascend 950DT

> Decode/训练方向的 Ascend 950 变体，官方路线图指向 2026Q4；SuperPoD 实机展示不等于芯片普遍可采购。

## 核心规格
- 最高 144GB HiZQ 2.0；4TB/s。
- 128MB L2。
- MXFP4 最高 2007 TFLOPS；FP8 1034；BF16 547。
- Unified Bus 2.0 2016GB/s 双向；PCIe5 x16 128GB/s 双向。

## 生命周期与边界
- 2025-09-18 宣布；截至当前核验，量产/普遍可采购状态未确认。
- Atlas 950 SuperPoD 的 1024 卡与 100kW 是系统级。

## 直接来源
- https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech
- https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf
