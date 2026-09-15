---
title: FuriosaAI RNGD Gen 2
vendor: FuriosaAI
object_type: accelerator
status: production
architecture: Tensor Contraction Processor
process: null
memory:
  hbm:
    type: HBM3
    capacity_gb: 48
    bandwidth_tb_s: 1.5
  sram_mb: 256
compute: {}
interconnect: {}
power:
  reported_w:
  - 150
  - 180
  scope: accelerator
  conflict: true
lifecycle:
  mass_production: 2026-01
  first_delivery: 2026-01
  broad_ga: null
updated: 2026-09-15
schema_version: chip-v0.2
layer: accelerator
relations: {}
evidence:
  S1:
    url: https://furiosa.ai/renegade-spec
    source_type: other
    accessed: '2026-09-16'
  S2:
    url: https://developer.furiosa.ai/latest/en/overview/rngd.html
    source_type: other
    accessed: '2026-09-16'
  S3:
    url: https://furiosa.ai/blog/rngd-enters-mass-production-the-high-performance-ai-accelerator-for-any-data-center
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
  - S2
  - S3
---
# FuriosaAI RNGD Gen 2

> 面向数据中心推理的加速器，采用 Tensor Contraction Processor、Tensor DMA 与片上 SRAM 数据流路线。

## 核心规格
- 48GB HBM3；1.5TB/s。
- 256MB SRAM。
- 功耗公开资料同时出现 150W 与 180W，保留冲突。

## 生命周期与边界
- 历史资料记录 2026-01 进入量产并交付首批；广泛 GA、出货量和客户部署仍需单独证据。
- SDK indexed-gather API 不等于硬件原生 page translator。

## 直接来源
- https://furiosa.ai/renegade-spec
- https://developer.furiosa.ai/latest/en/overview/rngd.html
- https://furiosa.ai/blog/rngd-enters-mass-production-the-high-performance-ai-accelerator-for-any-data-center
