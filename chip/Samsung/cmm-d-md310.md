---
schema_version: chip-v0.2
title: Samsung CMM-D MD310
vendor: Samsung
object_type: memory-expander
layer: memory
status: current-catalog
architecture: CXL Memory Module - DRAM
process: null
memory:
  type: DDR5
  capacity_gb: 256
  bandwidth_gb_s: 72
compute: {}
interconnect:
  type: CXL
  cxl_version: '3.2'
  host_interface: PCIe 6.0
  form_factor: EDSFF E3.S 2T
power: {}
lifecycle: {}
relations: {}
evidence:
  S1:
    url: https://semiconductor.samsung.com/cxl-memory/cmm-d/
    source_type: official
    accessed: '2026-09-25'
evidence_map:
  __page__: [S1]
  architecture: [S1]
  memory.type: [S1]
  memory.capacity_gb: [S1]
  memory.bandwidth_gb_s: [S1]
  interconnect.type: [S1]
  interconnect.cxl_version: [S1]
  interconnect.host_interface: [S1]
  interconnect.form_factor: [S1]
updated: 2026-09-25
---
# Samsung CMM-D MD310

> Samsung 的 CXL-attached DDR5 memory module，用于 memory expansion / pooling。

## 核心规格

- CXL 3.2，PCIe 6.0 interface。
- 256 GB DDR5。
- Samsung 页面给出 server↔memory 带宽最高 72 GB/s。
- EDSFF E3.S 2T form factor。

## 边界

- 72 GB/s 是该 CXL memory product 的公开带宽口径，不等同 HBM bandwidth。
- 远端 memory 的 latency、tier placement 与 workload 代价由 [[system/memory/cxl-and-memory-pooling|CXL / Memory Pooling]] 建模。
- 不把 pooled system aggregate capacity 回填成单模块容量。

## 直接来源

- https://semiconductor.samsung.com/cxl-memory/cmm-d/
