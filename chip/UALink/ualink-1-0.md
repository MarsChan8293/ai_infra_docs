---
schema_version: chip-v0.2
title: UALink 200G 1.0
vendor: UALink Consortium
object_type: interconnect-standard
layer: network
status: current-catalog
architecture: Accelerator scale-up interconnect standard
process: null
memory: {}
compute: {}
interconnect:
  type: UALink 200G 1.0
  lane_gbps: 200
  station_lanes: 4
  station_tx_gbps: 800
  station_rx_gbps: 800
  max_accelerators: 1024
power: {}
lifecycle:
  public_specification: 2025-04-01
relations: {}
evidence:
  S1:
    url: https://ualinkconsortium.org/specification/
    source_type: official
    accessed: '2026-09-25'
  S2:
    url: https://ualinkconsortium.org/about-ualink/
    source_type: official
    accessed: '2026-09-25'
evidence_map:
  __page__: [S1, S2]
  architecture: [S1, S2]
  interconnect.type: [S1]
  interconnect.lane_gbps: [S1]
  interconnect.max_accelerators: [S1, S2]
updated: 2026-09-25
---
# UALink 200G 1.0

> UALink Consortium 发布的开放 accelerator-to-accelerator scale-up interconnect 规范。

## 核心规格

- 200G per lane。
- 4 lanes 可构成一个 Station，TX 与 RX 各最高 800 Gb/s。
- UALink 1.0 面向单个 AI pod 最多 1,024 accelerators。

## 边界

- 本页记录**标准/协议代际**，不是某颗交换 ASIC 或某台 switch system。
- 200G 是 per-lane 口径；不能与 device aggregate 或 fabric bisection 直接比较。
- 实际硬件实现、拓扑与 collective 效率必须由具体产品页和 System 层提供。

## 直接来源

- https://ualinkconsortium.org/specification/
- https://ualinkconsortium.org/about-ualink/
