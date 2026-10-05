---
schema_version: chip-v0.2
title: Ultra Ethernet Specification 1.0.3
vendor: Ultra Ethernet Consortium
object_type: interconnect-standard
layer: network
status: current-catalog
architecture: Ethernet-based AI/HPC communications stack
process: null
memory: {}
compute: {}
interconnect:
  type: Ultra Ethernet 1.0.3
  primary_scope: backend scale-out
  transport: UET
  ethernet_based: true
power: {}
lifecycle:
  public_specification: 2026-07-16
relations:
  related:
    - chip/UEC/scale-up-transport-roadmap
evidence:
  S1:
    url: https://ultraethernet.org/specification-history/
    source_type: official
    accessed: '2026-10-05'
  S2:
    url: https://ultraethernet.org/ultra-ethernet-consortium-uec-launches-specification-1-0-transforming-ethernet-for-ai-and-hpc-at-scale/
    source_type: official
    accessed: '2026-10-05'
  S3:
    url: https://ultraethernet.org/uec-1-0-spec
    source_type: official
    accessed: '2026-10-05'
evidence_map:
  __page__: [S1, S2, S3]
  architecture: [S2, S3]
  interconnect.type: [S1]
  interconnect.primary_scope: [S3]
  interconnect.transport: [S2, S3]
  interconnect.ethernet_based: [S2, S3]
  lifecycle.public_specification: [S1]
updated: 2026-10-05
---
# Ultra Ethernet Specification 1.0.3

> Ultra Ethernet Consortium 当前公开的推荐实现版本；用于 AI / HPC 的开放 Ethernet communication stack。

## 当前版本

UEC specification history 将 1.0.3（2026-07-16）列为 current published version。

Ultra Ethernet 不是一个单独的 switch ASIC，而是横跨软件 API、transport、link/PHY、管理和 interoperability 的通信规范体系；核心 transport 为 UET。

## Scale-out / Scale-up 边界

当前 1.0.x 规范的主要目标仍是 backend scale-out。UEC 的公开材料明确说明会考虑 scale-up，并正在推进专门优化的 scale-up transport，但不应把正在开发的 scale-up work 反写成 1.0.3 已 ratified 的能力集合。

专用 scale-up 工作见 [[chip/UEC/scale-up-transport-roadmap|UEC Scale-Up Transport / SUE Roadmap]]。

## 边界

- 本页记录 standard/specification，不对应某个 NIC、switch 或 optical product。
- UET 是 transport，不等价于 Ethernet PHY 速率。
- 某个厂商宣称“UEC-ready/compatible”不自动建立 compatibility relation，必须有具体硬件官方资料。

## 直接来源

- https://ultraethernet.org/specification-history/
- https://ultraethernet.org/ultra-ethernet-consortium-uec-launches-specification-1-0-transforming-ethernet-for-ai-and-hpc-at-scale/
- https://ultraethernet.org/uec-1-0-spec
