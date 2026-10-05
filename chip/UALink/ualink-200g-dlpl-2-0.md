---
schema_version: chip-v0.2
title: UALink 200G Data Link and Physical Layers 2.0
vendor: UALink Consortium
object_type: interconnect-standard
layer: network
status: current-catalog
architecture: UALink 200G Data Link and Physical Layers
process: null
memory: {}
compute: {}
interconnect:
  type: UALink 200G DL/PL 2.0
  lane_gbps: 200
  common_spec_decoupled: true
power: {}
lifecycle:
  public_specification: 2026-04-07
relations:
  related:
    - chip/UALink/ualink-common-2-0
  successor-of:
    - chip/UALink/ualink-1-0
evidence:
  S1:
    url: https://ualinkconsortium.org/specification/
    source_type: official
    accessed: '2026-10-05'
  S2:
    url: https://ualinkconsortium.org/news/
    source_type: official
    accessed: '2026-10-05'
evidence_map:
  __page__: [S1, S2]
  architecture: [S1, S2]
  interconnect.type: [S1, S2]
  interconnect.lane_gbps: [S1, S2]
  interconnect.common_spec_decoupled: [S1, S2]
  lifecycle.public_specification: [S2]
updated: 2026-10-05
---
# UALink 200G Data Link and Physical Layers 2.0

> UALink 2.0 套件中的 200G Data Link / Physical Layer 规范。

## 核心事实

- 200G per lane。
- DL/PL 与 Common specification 分拆，以便 physical layer 和速率独立迭代。
- 与 [[chip/UALink/ualink-common-2-0|UALink Common 2.0]] 同批在 2026-04-07 对外发布。

## 边界

- 200G 是 per-lane 速率，不是 station/device/switch aggregate。
- 本页是 DL/PL 标准，不是 PHY IP、retimer、switch ASIC 或 accelerator implementation。
- 不从 UALink roadmap 推断 400G/更高速率的 GA 时间或规格。

## 直接来源

- https://ualinkconsortium.org/specification/
- https://ualinkconsortium.org/news/
