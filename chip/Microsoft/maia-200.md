---
title: "Microsoft Maia 200"
vendor: Microsoft
object_type: chip
status: production
architecture: Maia
process: "TSMC 3nm"
transistors_billion: ">140"
memory: {type: HBM3e, capacity_gb: 216, bandwidth_tb_s: 7, sram_mb: 272}
compute: {fp4_pflops: ">10", fp8_pflops: ">5"}
interconnect: {on_die_nic_tb_s_one_way: 1.4, bidirectional_tb_s: 2.8, scale_up: ATL_Ethernet}
power: {value_w: 750, scope: soc_tdp}
lifecycle: {announced: 2026-01-26, production_data_centers: [Iowa, Arizona], customer_inference_capacity: confirmed}
updated: 2026-09-15
---
# Microsoft Maia 200

> 第二代自研 AI 加速器，明确面向大规模推理。

## 核心规格
- TSMC 3nm；超过 1400 亿晶体管。
- 216GB HBM3e；7TB/s；272MB SRAM。
- >10 PFLOPS FP4；>5 PFLOPS FP8。
- 750W SoC TDP。
- On-die NIC 1.4TB/s 单向、2.8TB/s 双向。

## 生命周期与边界
- 2026-01-26 发布，已在 Iowa/Arizona 数据中心 live。
- ATL 最多 6,144 加速器是 scale-up 域，不是单芯片规格。
- 客户有推理容量不等于公开 Maia VM/SKU 全区域 GA。

## 直接来源
- https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/
- https://techcommunity.microsoft.com/blog/azureinfrastructureblog/deep-dive-into-the-maia-200-architecture/4489312
