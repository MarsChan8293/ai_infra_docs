---
title: Tenstorrent Blackhole p150
vendor: Tenstorrent
object_type: accelerator-card
status: ga
architecture: Blackhole
process: null
compute_units:
  tensix: 120
  big_riscv: 16
  baby_riscv_per_tensix: 5
memory:
  sram_mb: 180
  gddr6_gb: 32
  gddr6_bandwidth_tb_s: 0.512
compute: {}
interconnect:
  ethernet: 4x800G
  host: PCIe 5.0 x16
power:
  value_w: null
  scope: board
lifecycle:
  developer_products_available: true
updated: 2026-09-15
schema_version: chip-v0.2
layer: accelerator
relations: {}
evidence:
  S1:
    url: https://tenstorrent.com/en/hardware/cards
    source_type: other
    accessed: '2026-09-16'
  S2:
    url: https://tenstorrent.com/en/newsroom/tenstorrent-launches-blackhole-developer-products-at-tenstorrent-dev-day
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
  - S2
---
# Tenstorrent Blackhole p150

> 软件可见 SRAM/NoC 与 reader-compute-writer 数据流是其核心研究价值。

## 核心规格
- 120 Tensix；16 Big RISC-V；每 Tensix 5 个 Baby RISC-V。
- 约 180MB 分布式 SRAM。
- 32GB GDDR6；512GB/s。
- 4×800G；PCIe5 x16。

## 边界
- 早期 140 core/210MB 口径不与当前 p150 表混写。

## 直接来源
- https://tenstorrent.com/en/hardware/cards
- https://tenstorrent.com/en/newsroom/tenstorrent-launches-blackhole-developer-products-at-tenstorrent-dev-day
