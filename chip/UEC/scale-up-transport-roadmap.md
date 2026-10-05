---
schema_version: chip-v0.2
title: UEC Scale-Up Ethernet / Scale-Up Transport Roadmap
vendor: Ultra Ethernet Consortium
object_type: interconnect-standard
layer: network
status: roadmap
architecture: Scale-up-focused Ethernet transport derived from UET
process: null
memory: {}
compute: {}
interconnect:
  type: UEC scale-up transport
  scope: scale-up
  base_transport: UET
  development_status: work-in-progress
power: {}
lifecycle:
  announced: 2025-10-09
relations:
  related:
    - chip/UEC/ultra-ethernet-1-0-3
evidence:
  S1:
    url: https://ultraethernet.org/accelerating-ai-with-open-standards-uecs-expanding-vision/
    source_type: official
    accessed: '2026-10-05'
  S2:
    url: https://ultraethernet.org/uec-2025-in-review-preparing-for-what-comes-next-a-letter-from-uecs-chair/
    source_type: official
    accessed: '2026-10-05'
  S3:
    url: https://ultraethernet.org/specification-history/
    source_type: official
    accessed: '2026-10-05'
evidence_map:
  __page__: [S1, S2, S3]
  architecture: [S1, S2]
  interconnect.type: [S1, S2]
  interconnect.scope: [S1, S2]
  interconnect.base_transport: [S1]
  interconnect.development_status: [S1, S2]
  lifecycle.announced: [S1]
updated: 2026-10-05
---
# UEC Scale-Up Ethernet / Scale-Up Transport Roadmap

> Ultra Ethernet Consortium 面向本地/机架级 scale-up traffic 正在推进的优化 transport 工作。本页是 roadmap 状态，不是已 ratified 的独立 SUE specification。

## 当前公开状态

UEC 公开材料说明：

- Scale-up network 的 traffic management 与 scale-out 不同。
- Consortium 正在开发一个 scale-up-focused transport，并复用 UET 的基础能力。
- 同一后续工作流还包含 small-message 优化与 In-Network Collectives。
- 截至 2026-10-05，UEC specification history 仍将 1.0.3 列为 current published specification；公开列表没有单独列出已 ratified 的 scale-up specification。

因此仓库把这条线标为 roadmap，而不是 current-catalog。

## 命名说明

“SUE / Scale-Up Ethernet”在产业讨论中常用于指 Ethernet scale-up 路线；本页标题同时保留更接近 UEC 官方公开文本的 Scale-Up Transport，避免把产业简称误写成已正式发布的 UEC 规范名。

## 边界

- 不填写 speculative lane rate、domain size 或 latency。
- 不把 UEC 1.0.3 的 backend scale-out target 自动套到 scale-up transport。
- 后续 UEC 若发布正式版本，应新建稳定版本页，而不是直接覆盖本 roadmap 节点。

## 直接来源

- https://ultraethernet.org/accelerating-ai-with-open-standards-uecs-expanding-vision/
- https://ultraethernet.org/uec-2025-in-review-preparing-for-what-comes-next-a-letter-from-uecs-chair/
- https://ultraethernet.org/specification-history/
