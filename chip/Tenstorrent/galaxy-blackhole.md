---
title: Tenstorrent Galaxy Blackhole
vendor: Tenstorrent
object_type: system
status: ga
architecture: 32x Blackhole ASIC
accelerators: 32
memory:
  gddr6_tb: 1
  aggregate_bandwidth_tb_s: 16
  aggregate_sram_gb: 6.2
  aggregate_sram_bandwidth_pb_s: 2.9
compute:
  blockfp8_pflops: 23
power:
  value_w: null
  scope: system
lifecycle:
  ga: confirmed
updated: 2026-09-15
schema_version: chip-v0.2
layer: system
process: null
interconnect: {}
relations: {}
evidence:
  S1:
    url: https://tenstorrent.com/hardware/galaxy
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
---
# Tenstorrent Galaxy Blackhole

> 32 ASIC 系统，本页专门承接原来混在 Blackhole 页里的聚合规格。

## 系统规格
- 32 ASIC；1TB GDDR6；16TB/s。
- 约 6.2GB SRAM；约 2.9PB/s。
- 23PFLOPS BlockFP8。

## 边界
- 350+ tokens/s/user 是特定系统工作负载，不是单 ASIC 峰值。

## 直接来源
- https://tenstorrent.com/hardware/galaxy
