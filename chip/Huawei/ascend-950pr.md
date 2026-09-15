---
title: "Huawei Ascend 950PR"
vendor: Huawei
object_type: chip
status: commercial-product
architecture: "Ascend 950"
process: null
compute_units: {ai_subsystems_max: 36, cube_variants: [32,28], vector_variants: [64,56]}
memory: {technology: "HiBL 1.0", max_capacity_gb: 128, max_bandwidth_tb_s: 1.6, product_variant_capacity_gb: 112, product_variant_bandwidth_tb_s: 1.4, l2_mb: 128}
compute: {mxfp4_tflops: [1784,1561], fp8_tflops: [919,804], bf16_tflops: [486,425]}
interconnect: {unified_bus_2_0_gb_s_bidirectional: 2016, pcie: "Gen5 x16, 128GB/s bidirectional"}
power: {value_w: null, scope: chip, related_card_max_w: 600}
lifecycle: {announced: 2025-09-18, atlas_350_launch: 2026-03-20}
updated: 2026-09-15
---
# Huawei Ascend 950PR

> Ascend 950 Die 的 Prefill/推荐方向变体；2026-03-20 搭载它的 Atlas 350 正式上市。

## 核心规格
- 最高 128GB、1.6TB/s HiBL 1.0；产品变体 112GB/1.4TB/s。
- 128MB 统一 L2，512B line / 128B sector。
- MXFP4 1784/1561 TFLOPS；FP8 919/804；BF16 486/425，按变体。
- Unified Bus 2.0 双向 2016GB/s；PCIe5 x16 双向 128GB/s。

## 边界
- Atlas 350 ≤600W 是卡级，不是 950PR 芯片 TDP。
- 具体 nm 制程公开资料未确认。

## 直接来源
- https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech
- https://www.hiascend.com/activities/dynamic-news/20260320-3
- https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf
