---
title: d-Matrix Corsair
vendor: d-Matrix
object_type: inference-platform
status: production
architecture: DIMC
process: null
memory:
  performance_sram_gb: 2
  performance_sram_bandwidth_tb_s: 150
  capacity_memory: LPDDR5 up to 256GB / 400GB/s platform-level
compute:
  units:
  - DIMC
  - SIMD
  - RISC-V
  - Dispatch
  - Data_Reshape
interconnect:
  chiplet_bridge: DMX_Bridge
power:
  value_w: null
  scope: platform
lifecycle:
  full_production_claim: 2026-06
  customers: select/qualified
updated: 2026-09-15
schema_version: chip-v0.2
layer: unknown
relations: {}
evidence:
  S1:
    url: https://www.d-matrix.ai/announcements/d-matrix-corsair-ai-inference-platform-enters-full-production-to-meet-customer-demand/
    source_type: other
    accessed: '2026-09-16'
  S2:
    url: https://www.d-matrix.ai/product/
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
  - S2
---
# d-Matrix Corsair

> 面向 AI 推理的 DIMC 平台，重点把计算靠近 SRAM。

## 核心公开信息
- 2GB SRAM Performance Memory，150TB/s。
- LPDDR5 最高 256GB、400GB/s 是平台/双卡容量层口径，不自动当作单芯片。
- DIMC、SIMD、RISC-V、Dispatch/Data Reshape、chiplet、DMX Bridge。

## 生命周期与边界
- 2026-06 厂商公告使用 full production，但仍是 select/qualified customers，不等于普遍 GA。

## 直接来源
- https://www.d-matrix.ai/announcements/d-matrix-corsair-ai-inference-platform-enters-full-production-to-meet-customer-demand/
- https://www.d-matrix.ai/product/
