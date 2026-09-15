---
title: Xiaomi XRING O3 / 玄戒 O3
vendor: Xiaomi
object_type: mobile-soc
status: unknown
architecture: XRING
process: 3nm
transistors_billion: 24
npu:
  llm_optimized: true
  absolute_tops: null
compute:
  vendor_claim_inference_speed_vs_previous: +45%
  vendor_claim_power_reduction: 26%
lifecycle:
  announced_event: 2026-08-24
  mass_production_claim: true
  planned_first_device: 2026-09
updated: 2026-09-15
schema_version: chip-v0.2
layer: soc
legacy_status: production-claim
memory: {}
interconnect: {}
power: {}
relations: {}
evidence:
  S1:
    url: https://ir.mi.com/
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
  architecture:
  - S1
  compute.vendor_claim_inference_speed_vs_previous:
  - S1
  compute.vendor_claim_power_reduction:
  - S1
  lifecycle.announced_event:
  - S1
  lifecycle.mass_production_claim:
  - S1
  lifecycle.planned_first_device:
  - S1
  process:
  - S1
---
# Xiaomi XRING O3 / 玄戒 O3

> 2026 年公开的 AI 旗舰手机 SoC，报道口径称已开启规模量产。

## 核心公开信息
- 3nm；240 亿晶体管。
- NPU 针对大语言模型优化；绝对 NPU TOPS 未有小米原始规格表确认。
- “推理速度 +45%、功耗 -26%”缺少完整基准条件，保留为发布会口径。

## 证据边界
- 当前仓库未取得对应小米官网原始技术稿，因此 2026-08-24 的规格/量产状态仍标为公开活动报道证据，后续应补一手来源。

## 直接来源
- https://ir.mi.com/
