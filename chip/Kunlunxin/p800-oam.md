---
title: 昆仑芯 P800 OAM
vendor: Kunlunxin
object_type: module
status: product
architecture: P800 / XPU-P based
process: null
memory:
  capacity_gb: 96
  source_level: integration_partner
  type: null
compute:
  formats:
  - FP16
  - FP32
  - INT8
interconnect:
  host: PCIe Gen5 x16
  cluster: IB or RoCE
power:
  value_w: 400
  scope: module
  source_level: integration_partner
updated: 2026-09-15
schema_version: chip-v0.2
layer: module
lifecycle: {}
relations: {}
evidence:
  S1:
    url: https://www.kunlunxin.com/
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
---
# 昆仑芯 P800 OAM

> 基于 P800 的 OCP-OAM 模组。

## 核心规格与证据层级
- 昆仑芯官方确认 OAM 形态、P800 基础、IB/RoCE 万卡集群方向。
- TencentOS Server 部署文档给出 96GB、400W、PCIe5 x16、FP16/FP32/INT8，属于集成方资料，不升级为昆仑芯官方 datasheet。

## 直接来源
- https://www.kunlunxin.com/
