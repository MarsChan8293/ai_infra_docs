---
title: Iluvatar MR-V50
vendor: Iluvatar CoreX
object_type: board
status: unknown
architecture: 智铠 inference GPU
memory:
  type: HBM2e
  capacity_gb: 16
compute:
  formats:
  - FP32
  - FP16
  - INT8
interconnect:
  host: PCIe Gen4 x16
power:
  value_w: 75
  scope: board
updated: 2026-09-15
schema_version: chip-v0.2
layer: board
legacy_status: commercialized
process: null
lifecycle: {}
relations: {}
evidence:
  S1:
    url: https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-tlxltt-zk100
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
  architecture:
  - S1
  compute.formats:
  - S1
  interconnect.host:
  - S1
  memory.capacity_gb:
  - S1
  memory.type:
  - S1
  power.scope:
  - S1
  power.value_w:
  - S1
---
# Iluvatar MR-V50

> 智铠 50 推理 PCIe 卡。

## 核心规格
- 16GB HBM2e；75W。
- HHHL 单槽 PCIe Gen4 x16；被动散热。

## 直接来源
- https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-tlxltt-zk100
