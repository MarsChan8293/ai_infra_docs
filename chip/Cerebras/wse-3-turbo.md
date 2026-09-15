---
title: "Cerebras WSE-3 Turbo / WSE-3T"
vendor: Cerebras
object_type: wafer-scale-processor
status: announced
architecture: "Wafer-Scale Engine"
process: "TSMC 5nm"
area_mm2: 46225
transistors_trillion: 4
cores: {active: 900000}
memory: {type: SRAM, capacity_gb: 44, bandwidth_pb_s: 43.2}
compute: {sparse_fp16_pflops: 250}
interconnect: {on_wafer_fabric_pb_s: 53.5, external_io_tbit_s: 2.4}
power: {value_w: null, scope: processor}
lifecycle: {announced: 2026-08-18, independent_chip_shipping: null}
updated: 2026-09-15
---
# Cerebras WSE-3 Turbo / WSE-3T

> 2026-08-18 随 CS-4 公布的晶圆级处理器，重点提高 decode 所需的片上带宽与系统互联。

## 核心规格
- 5nm；46,225 mm²；4T transistors；900k AI cores。
- 44GB SRAM；43.2PB/s memory bandwidth；53.5PB/s fabric。
- 250 PFLOPS sparse FP16。
- 2.4Tb/s 对外 I/O。

## 生命周期与边界
- CS-4 使用 3 片 WSE-3T；3× 聚合算力/内存/带宽属于系统层。
- 单处理器功耗、独立采购与规模出货公开资料未确认。

## 直接来源
- https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions
- https://www.cerebras.ai/cs4
