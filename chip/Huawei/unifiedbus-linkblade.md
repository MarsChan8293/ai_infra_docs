---
schema_version: chip-v0.2
title: Huawei UnifiedBus LinkBlade
vendor: Huawei
object_type: interconnect-blade
layer: network
status: announced
architecture: Cable-free intra-cabinet UnifiedBus interconnect blade
process: null
memory: {}
compute: {}
interconnect:
  type: UnifiedBus
  scope: intra-cabinet
  cable_free: true
power: {}
lifecycle:
  announced: 2026-09-17
relations:
  compatible-with:
    - chip/Huawei/unifiedbus-2
evidence:
  S1:
    url: https://www.huawei.com/cn/news/2026/9/hc-lingqu-agent-ai
    source_type: official
    accessed: '2026-10-05'
evidence_map:
  __page__: [S1]
  architecture: [S1]
  interconnect.type: [S1]
  interconnect.scope: [S1]
  interconnect.cable_free: [S1]
  lifecycle.announced: [S1]
updated: 2026-10-05
---
# Huawei UnifiedBus LinkBlade

> 华为面向柜内场景发布的灵衢互联刀片，用于把 UnifiedBus 互联下沉到机柜内部。

## 核心事实

- 华为将 LinkBlade 定位为柜内灵衢互联刀片。
- 官方描述其采用无电缆设计，用于消除传统线缆/连接电路带来的损耗。
- 华为给出的 4096-NPU SuperPoD 示例中，LinkBlade 方案可减少约 196 km 铜缆。

## 边界

- 本页记录 LinkBlade 这个柜内互联部件，不把 196 km 作为器件自身规格；该数字是 4096-NPU SuperPoD 的系统级部署效果。
- 官方当前未公开本页可安全结构化的 per-port / per-link bandwidth、端口数或器件功耗，因此保持 unknown。
- LinkBlade 所使用的协议对象见 [[chip/Huawei/unifiedbus-2|Huawei UnifiedBus 2.0]]。
- 跨柜互联由 [[chip/Huawei/unifiedbus-linkdevice|Huawei UnifiedBus LinkDevice]] 单独记录。

## 直接来源

- https://www.huawei.com/cn/news/2026/9/hc-lingqu-agent-ai
