---
schema_version: chip-v0.2
title: Huawei UnifiedBus UBG Switch
vendor: Huawei
object_type: switch-system
layer: network
status: announced
architecture: High-radix inter-cluster UnifiedBus switch
process: null
memory: {}
compute: {}
interconnect:
  type: UnifiedBus UBG
  scope: inter-cluster
  radix: 1024
  max_cluster_npus: 1000000
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
  interconnect.radix: [S1]
  interconnect.max_cluster_npus: [S1]
  lifecycle.announced: [S1]
updated: 2026-10-05
---
# Huawei UnifiedBus UBG Switch

> 华为面向跨集群场景发布的高 Radix 灵衢网络交换层对象。

## 核心规格

- Radix 扇出能力：最高 1,024。
- 华为公开称其可支撑百万 NPU 级 SuperCluster。
- 在华为分层互联模型中，UBG 位于 LinkBlade（柜内）和 LinkDevice（跨柜）之上，承担跨集群扩展。

## 边界

- 本页记录华为在计算架构发布中公开的 UBG 交换层能力，不是某个已确认具体 SKU 的完整规格页。
- 1,024 是 Radix/fan-out 口径，不是端口带宽。
- 1,000,000 NPUs 是官方公开的目标集群规模，不是单个 UBG 设备端口数，也不代表无阻塞 bisection scale。
- 具体的 CloudEngine UBG 产品系列见 [[chip/Huawei/cloudengine-sf9300|CloudEngine SF9300]]；本页不把该具体产品尚未明确披露的字段反向补到通用 UBG 对象。

## 直接来源

- https://www.huawei.com/cn/news/2026/9/hc-lingqu-agent-ai
