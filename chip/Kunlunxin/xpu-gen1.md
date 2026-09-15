---
title: 昆仑芯一代 XPU
vendor: Kunlunxin
object_type: chip
status: production
architecture: XPU-K
process: null
memory:
  type: GDDR6
  capacity_gb:
  - 16
  - 32
compute:
  int8_tops: 256
  int16_tops: 128
  int32_tops: 128
interconnect: {}
power:
  reported_w:
  - 150
  - 160
  scope: chip_or_product_variant
lifecycle:
  roadmap: 2019
  large_scale_deployment: 2020
updated: 2026-09-15
schema_version: chip-v0.2
layer: chip
relations: {}
evidence:
  S1:
    url: https://www.kunlunxin.com/
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
  architecture:
  - S1
  compute.int16_tops:
  - S1
  compute.int32_tops:
  - S1
  compute.int8_tops:
  - S1
  lifecycle.large_scale_deployment:
  - S1
  lifecycle.roadmap:
  - S1
  memory.capacity_gb:
  - S1
  memory.type:
  - S1
  power.reported_w:
  - S1
  power.scope:
  - S1
---
# 昆仑芯一代 XPU

> 第一代云端 AI 芯片路线，2020 年已有大规模部署。

## 核心规格
- INT8 256 TOPS；INT16/INT32 128 TOPS。
- 16GB 或 32GB GDDR6；150W 或 160W，官网未把组合拆成独立 SKU。

## 直接来源
- https://www.kunlunxin.com/
