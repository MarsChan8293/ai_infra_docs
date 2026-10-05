---
schema_version: chip-v0.2
title: Huawei UnifiedBus LinkDevice
vendor: Huawei
object_type: interconnect-device
layer: network
status: announced
architecture: All-optical inter-cabinet UnifiedBus interconnect device
process: null
memory: {}
compute: {}
interconnect:
  type: UnifiedBus
  scope: inter-cabinet
  medium: optical
  port_count: 176
  port_bandwidth_tbit_s: 1.6
  device_aggregate_tbit_s: 280
  rtt_us: 2
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
  interconnect.medium: [S1]
  interconnect.port_count: [S1]
  interconnect.port_bandwidth_tbit_s: [S1]
  interconnect.device_aggregate_tbit_s: [S1]
  interconnect.rtt_us: [S1]
  lifecycle.announced: [S1]
updated: 2026-10-05
---
# Huawei UnifiedBus LinkDevice

> 华为面向跨柜场景发布的全光灵衢互联设备。

## 核心规格

- 176 个端口。
- 每端口带宽：1.6 Tbit/s。
- 单机全光互联带宽：280 Tbit/s。
- RTT 时延：最低约 2 μs。
- 官方将其定位为跨柜高速总线协议互联设备。

## 边界

- 1.6 Tbit/s 是 per-port 口径；280 Tbit/s 是 device aggregate 口径，两者不能直接互换。
- RTT 2 μs 是华为对该跨柜互联设备公开的最低时延口径，不等于应用 collective latency。
- 本页不把端口带宽推导成单 lane SerDes 速率，因为公开来源未披露 lane 组成。
- 柜内互联见 [[chip/Huawei/unifiedbus-linkblade|UnifiedBus LinkBlade]]；协议层见 [[chip/Huawei/unifiedbus-2|UnifiedBus 2.0]]。

## 直接来源

- https://www.huawei.com/cn/news/2026/9/hc-lingqu-agent-ai
