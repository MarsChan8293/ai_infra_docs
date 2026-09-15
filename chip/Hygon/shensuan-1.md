---
title: 海光 深算一号
vendor: Hygon
object_type: dcu-generation
status: legacy
architecture: GPGPU
process: null
memory: {}
compute: {}
interconnect:
  scale_up: HSL
power:
  value_w: null
  scope: chip
lifecycle:
  commercial_generation_confirmed: true
updated: 2026-09-15
schema_version: chip-v0.2
layer: unknown
relations: {}
evidence:
  S1:
    url: https://www.hygon.cn/
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
  architecture:
  - S1
  interconnect.scale_up:
  - S1
  lifecycle.commercial_generation_confirmed:
  - S1
  power.scope:
  - S1
---
# 海光 深算一号

> 海光第一代 DCU/GPGPU 代际。

## 边界
- 当前直接材料不足以安全写入裸片制程、显存、功耗与完整峰值表。
- 板卡或服务器参数不回填 DCU 裸片。

## 直接来源
- https://www.hygon.cn/
