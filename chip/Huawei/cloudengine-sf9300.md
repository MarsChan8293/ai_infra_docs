---
schema_version: chip-v0.2
title: Huawei CloudEngine SF9300 UBG Series
vendor: Huawei
object_type: switch-system
layer: network
status: announced
architecture: Two-layer multi-plane UnifiedBus UBG switch system
process: null
memory: {}
compute: {}
interconnect:
  type: UnifiedBus UBG
  topology: two-layer multi-plane
  link_layer_retransmission: true
power: {}
lifecycle:
  announced: 2026-09-17
relations:
  compatible-with:
    - chip/Huawei/unifiedbus-2
  related:
    - chip/Huawei/unifiedbus-ubg-switch
evidence:
  S1:
    url: https://e.huawei.com/cn/news/2026/solutions/enterprise-network/xinghe-intelligent-data-center-network
    source_type: official
    accessed: '2026-10-05'
  S2:
    url: https://www.huawei.com/cn/news/2026/9/hc-ai-infra-aiwan-campus
    source_type: official
    accessed: '2026-10-05'
evidence_map:
  __page__: [S1, S2]
  architecture: [S1, S2]
  interconnect.type: [S1, S2]
  interconnect.topology: [S1, S2]
  interconnect.link_layer_retransmission: [S1, S2]
  lifecycle.announced: [S1, S2]
updated: 2026-10-05
---
# Huawei CloudEngine SF9300 UBG Series

> 华为 2026 年发布的 CloudEngine SF9300 系列 UBG 灵衢网络交换机。

## 核心事实

- 产品采用 two-layer multi-plane 架构，华为称其可省去传统核心层。
- 采用 UnifiedBus / UB 极简转发。
- 支持 LLR（Link-Layer Retransmission，链路层重传），用于链路误码或闪断场景的快速恢复。
- 华为在方案级公开口径中称，统一协议可把端到端时延从 20 μs 降至 11 μs。

## 边界

- 20 → 11 μs 是方案端到端口径，不是单台 SF9300 的 ASIC/switch latency，因此不写入结构化 latency 字段。
- 公开发布稿没有给出本页可直接绑定的 switch capacity、端口速率或精确 port count；这些字段保持 unknown。
- [[chip/Huawei/unifiedbus-ubg-switch|UnifiedBus UBG Switch]] 记录通用 UBG 交换层公开的 1,024 Radix 与百万 NPU 规模；本页不假定这些数字等同于 SF9300 的具体 SKU 规格，除非后续产品资料直接确认。

## 直接来源

- https://e.huawei.com/cn/news/2026/solutions/enterprise-network/xinghe-intelligent-data-center-network
- https://www.huawei.com/cn/news/2026/9/hc-ai-infra-aiwan-campus
