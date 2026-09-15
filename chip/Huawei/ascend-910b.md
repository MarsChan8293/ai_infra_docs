---
title: Huawei Ascend 910B
vendor: Huawei
object_type: chip
status: ga
architecture: Ascend
process: null
memory:
  type: null
  capacity_gb: null
  bandwidth_tb_s: null
compute: {}
interconnect: {}
power:
  value_w: null
  scope: chip
lifecycle:
  cloud_resource_support: confirmed
  mass_production_date: null
updated: 2026-09-15
schema_version: chip-v0.2
layer: chip
relations: {}
evidence:
  S1:
    url: https://www.hiascend.com/
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
  architecture:
  - S1
  lifecycle.cloud_resource_support:
  - S1
  power.scope:
  - S1
---
# Huawei Ascend 910B

> 950 系列之前的主流昇腾代际。公开云资源与 CANN 支持能证明可用性，但不补猜芯片裸片规格。

## 生命周期与边界
- 华为云 ModelArts / CANN 中存在 910B 资源和软件支持。
- 社区出现的 64G 环境不能自动回填为芯片 HBM 容量。
- 制程、裸片 TDP、正式量产/出货批次在当前一手资料中未完整确认。

## 直接来源
- https://www.hiascend.com/
