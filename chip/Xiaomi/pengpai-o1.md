---
title: Xiaomi XRING O1 / 玄戒 O1
vendor: Xiaomi
object_type: mobile-soc
status: shipping
architecture: XRING
process: 2nd-generation 3nm
transistors_billion: 19
cpu:
  cores: 10
gpu:
  cores: 16
  type: Immortalis-G925
npu:
  cores: 6
  tops: 44
isp: 4th-generation
power:
  value_w: null
  scope: soc
lifecycle:
  announced: 2025-05-22
  shipping_devices:
  - Xiaomi 15S Pro
  - Xiaomi Pad 7 Ultra
updated: 2026-09-15
schema_version: chip-v0.2
layer: soc
memory: {}
compute: {}
interconnect: {}
relations: {}
evidence:
  S1:
    url: https://www.mi.com/global/event/2025/xiaomi-15s-pro-pad-7-ultra/
    source_type: other
    accessed: '2026-09-16'
  S2:
    url: https://ir.mi.com/
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
  - S2
---
# Xiaomi XRING O1 / 玄戒 O1

> 小米旗舰手机/平板 SoC，集成 CPU、GPU、ISP 与 6 核 NPU。

## 核心规格
- 第二代 3nm；190 亿晶体管。
- 10 核 CPU；16 核 Immortalis-G925 GPU。
- 6 核 NPU，官方 44TOPS；第四代 ISP。

## 生命周期与边界
- 2025-05-22 发布并随 15S Pro / Pad 7 Ultra 出货。
- 44TOPS 只属于 NPU，不能把整颗 SoC 的其他计算单元混入。

## 直接来源
- https://www.mi.com/global/event/2025/xiaomi-15s-pro-pad-7-ultra/
- https://ir.mi.com/
