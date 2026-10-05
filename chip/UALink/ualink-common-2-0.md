---
schema_version: chip-v0.2
title: UALink Common 2.0
vendor: UALink Consortium
object_type: interconnect-standard
layer: network
status: current-catalog
architecture: Open accelerator scale-up common protocol with in-network compute
process: null
memory: {}
compute: {}
interconnect:
  type: UALink Common 2.0
  in_network_compute: true
  dl_pl_decoupled: true
power: {}
lifecycle:
  public_specification: 2026-04-07
relations:
  successor-of:
    - chip/UALink/ualink-1-0
  related:
    - chip/UALink/ualink-200g-dlpl-2-0
evidence:
  S1:
    url: https://ualinkconsortium.org/specification/
    source_type: official
    accessed: '2026-10-05'
  S2:
    url: https://ualinkconsortium.org/news/
    source_type: official
    accessed: '2026-10-05'
  S3:
    url: https://ualinkconsortium.org/blog/exploring-in-network-compute-how-ualink-is-redefining-ai-scale-up-architecture-1509/
    source_type: official
    accessed: '2026-10-05'
evidence_map:
  __page__: [S1, S2, S3]
  architecture: [S1, S2, S3]
  interconnect.type: [S1, S2]
  interconnect.in_network_compute: [S1, S2, S3]
  interconnect.dl_pl_decoupled: [S1, S2]
  lifecycle.public_specification: [S2]
updated: 2026-10-05
---
# UALink Common 2.0

> UALink 2026 年 ratified 的 Common Specification 2.0，重点引入 In-Network Compute，并把 Common 与 Data Link / Physical Layer 代际解耦。

## 核心变化

- 引入 In-Network Compute，让计算与 accelerator fabric 通信协同执行。
- Data Link / Physical Layer 从 Common specification 中拆分，使 PHY / speed 可以独立演进。
- 同批规范还包括 Manageability 1.0 与 Chiplet specification；这些属于独立规范，不在本页伪装成 Common 2.0 的 bandwidth 字段。

## 边界

- Common 2.0 是协议/公共语义规范，不是某颗 switch silicon。
- Common 2.0 本身不等同于“400G UALink”；当前公开套件中的高速 DL/PL 对象仍有独立的 [[chip/UALink/ualink-200g-dlpl-2-0|UALink 200G DL/PL 2.0]]。
- 具体 silicon implementation 只有厂商正式发布后再建立硬件页。

## 直接来源

- https://ualinkconsortium.org/specification/
- https://ualinkconsortium.org/news/
- https://ualinkconsortium.org/blog/exploring-in-network-compute-how-ualink-is-redefining-ai-scale-up-architecture-1509/
