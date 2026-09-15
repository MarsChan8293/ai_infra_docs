---
title: "Google TPU v5p"
vendor: Google
object_type: chip
status: ga
architecture: TPU
process: null
memory: {type: HBM, capacity_gb: null, bandwidth_tb_s: null}
compute: {}
interconnect: {scale_up: ICI}
power: {value_w: null, scope: chip}
lifecycle: {announced: 2023-12-06, cloud_available: confirmed}
updated: 2026-09-15
---
# Google TPU v5p

> Cloud TPU v5p 的芯片对象；Pod 和 VM 配置不回填芯片。

## 生命周期与边界
- 2023-12-06 发布并向 Cloud customers 提供；当前是上一代 GA 产品。
- Google 未公开独立流片或量产日期。
- 本次重构不从 Pod 文档推导单芯片功耗/内存，详细数值继续以官方 v5p 架构文档为准。

## 直接来源
- https://docs.cloud.google.com/tpu/docs/v5p
