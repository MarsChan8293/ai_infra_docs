---
title: Cerebras WSE-3
vendor: Cerebras
object_type: wafer-scale-processor
status: production
architecture: Wafer-Scale Engine
process: TSMC 5nm
area_mm2: 46225
transistors_trillion: 4
cores:
  physical: 970000
  active: 900000
memory:
  type: SRAM
  capacity_gb: 44
  bandwidth_pb_s: 21.6
compute:
  sparse_fp16_pflops: 125
interconnect:
  on_wafer_fabric_pb_s: 26.7
  external_io_tbit_s: 1.2
power:
  value_w: null
  scope: processor
lifecycle:
  announced: 2024-03-13
  commercial_system_shipping: confirmed
updated: 2026-09-15
schema_version: chip-v0.2
layer: chip
relations: {}
evidence:
  S1:
    url: https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
  architecture:
  - S1
  compute.sparse_fp16_pflops:
  - S1
  interconnect.external_io_tbit_s:
  - S1
  interconnect.on_wafer_fabric_pb_s:
  - S1
  lifecycle.announced:
  - S1
  lifecycle.commercial_system_shipping:
  - S1
  memory.bandwidth_pb_s:
  - S1
  memory.capacity_gb:
  - S1
  memory.type:
  - S1
  power.scope:
  - S1
  process:
  - S1
---
# Cerebras WSE-3

> 一整片晶圆作为一个处理器对象。CS-3 的电力、液冷和外部 MemoryX 不属于 WSE-3 本体。

## 核心规格
- TSMC 5nm；46,225 mm²；4 万亿晶体管。
- 970,000 physical / 900,000 active AI cores。
- 44 GB 片上 SRAM；21.6 PB/s 内存带宽；26.7 PB/s fabric。
- 125 PFLOPS，当前资料脚注为 sparse FP16。
- 对外 I/O 1.2 Tbit/s。

## 生命周期与边界
- 2024-03-13 发布；CS-3 已由厂商确认商业交付。
- 裸 WSE-3 独立出货量、晶圆量产批次和处理器 TDP 未公开。
- CS-3 ~23kW 是系统级峰值，不能回填本页。

## 直接来源
- https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine
