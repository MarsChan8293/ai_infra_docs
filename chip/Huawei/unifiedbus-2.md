---
schema_version: chip-v0.2
title: Huawei UnifiedBus 2.0 (灵衢 2.0)
vendor: Huawei
object_type: interconnect-standard
layer: network
status: current-catalog
architecture: Bus-grade interconnect protocol for SuperPoD
process: null
memory: {}
compute: {}
interconnect:
  type: UnifiedBus 2.0
  chinese_name: 灵衢 2.0
  bandwidth_class: TB/s
  rtt_us: 2.1
  memory_semantics: true
  unified_memory_addressing: true
  optical_interconnect: true
  target_scale: 10,000+ NPU-class SuperPoD
power: {}
lifecycle:
  announced: 2025-09-18
  public_specification: 2025-09-18
relations:
  used-in:
    - chip/Huawei/unifiedbus-linkblade
    - chip/Huawei/unifiedbus-linkdevice
    - chip/Huawei/unifiedbus-ubg-switch
    - chip/Huawei/cloudengine-sf9300
evidence:
  S1:
    url: https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech
    source_type: official
    accessed: '2026-10-05'
  S2:
    url: https://www.huawei.com/cn/corporate-information/research-development
    source_type: official
    accessed: '2026-10-05'
evidence_map:
  __page__: [S1, S2]
  architecture: [S1, S2]
  interconnect.type: [S1]
  interconnect.chinese_name: [S1]
  interconnect.bandwidth_class: [S1, S2]
  interconnect.rtt_us: [S1]
  interconnect.memory_semantics: [S2]
  interconnect.unified_memory_addressing: [S2]
  interconnect.optical_interconnect: [S1]
  interconnect.target_scale: [S1]
  lifecycle.announced: [S1]
  lifecycle.public_specification: [S1]
updated: 2026-10-05
---
# Huawei UnifiedBus 2.0（灵衢 2.0）

> 华为面向 SuperPoD / 超节点提出的总线级互联协议，英文名 UnifiedBus（UB），中文名“灵衢”。

## 核心事实

- 华为于 2025-09-18 正式发布 UnifiedBus / 灵衢，并宣布开放 UnifiedBus 2.0 技术规范。
- 官方描述灵衢 2.0 面向万卡级 SuperPoD，强调总线级互联、平等协同、全量池化、协议归一、大规模组网和高可用。
- 公开口径为 TB 级带宽、约 2.1 μs RTT，并采用内存语义和统一内存编址。
- Atlas 950 SuperPoD 使用 UnifiedBus 2.0；Atlas 900 A3 SuperPoD 采用 UnifiedBus 1.0，并于 2025 年 3 月开始交付。

## 边界

- 本页记录协议/互联架构代际，不是某颗交换芯片、光引擎或完整 SuperPoD。
- “TB 级”是华为公开的量级描述，不在缺少端口/设备 scope 时强行转换成精确 GB/s 数值。
- SuperPoD 的卡数、总互联带宽和系统算力属于 system / cluster 聚合指标，不回填本页。
- 柜内/跨柜/跨集群实现分别见 [[chip/Huawei/unifiedbus-linkblade|LinkBlade]]、[[chip/Huawei/unifiedbus-linkdevice|LinkDevice]]、[[chip/Huawei/unifiedbus-ubg-switch|UBG Switch]] 与 [[chip/Huawei/cloudengine-sf9300|CloudEngine SF9300]]。
- 具体 NPO 光引擎见 [[chip/Huawei/hi-one-npo|Huawei Hi-ONE NPO]]；NPO 交换机 [[chip/Huawei/cloudengine-xh9300-npo|CloudEngine XH9300]] 当前不因同属华为 AI 网络而推断为 UnifiedBus 实现。

## 直接来源

- https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech
- https://www.huawei.com/cn/corporate-information/research-development
