---
schema_version: chip-v0.2
title: Huawei Hi-ONE NPO
vendor: Huawei
object_type: npo-optical-engine
layer: network
status: production
architecture: Near-Packaged Optics optical interconnect engine
process: null
memory: {}
compute: {}
interconnect:
  type: NPO
  engine_capacity_tb_s: 7.2
  integrated_laser: true
  target: SuperPoD scale-up optical interconnect
power: {}
lifecycle:
  production_disclosed: 2026-09-17
relations:
  compatible-with:
    - chip/Huawei/unifiedbus-2
evidence:
  S1:
    url: https://www.huawei.com/cn/news/2026/9/hc-wang-keynote
    source_type: official
    accessed: '2026-10-05'
evidence_map:
  __page__: [S1]
  architecture: [S1]
  interconnect.type: [S1]
  interconnect.engine_capacity_tb_s: [S1]
  interconnect.integrated_laser: [S1]
  interconnect.target: [S1]
  lifecycle.production_disclosed: [S1]
updated: 2026-10-05
---
# Huawei Hi-ONE NPO

> 华为面向超节点互联的 Near-Packaged Optics（NPO）光互联产品。

## 核心规格

- 单个 Hi-ONE 光引擎传输容量：7.2 Tb/s。
- 华为公开称其为具备量产能力的 NPO 产品，并强调内置光源。
- Hi-ONE 与 [[chip/Huawei/unifiedbus-2|UnifiedBus / 灵衢]] 共同构建可规模扩展的 SuperPoD 互联系统。
- 华为在 OIF 提出 NPO 标准立项建议。

## 系统级部署事实

华为在 2026 年公开的 Ascend 960 SuperPoD 方案中称，4096 卡系统使用约 5,500 个 Hi-ONE，替代约 48,000 个 800G pluggable optical modules。该数字属于 SuperPoD 系统级配置，因此只在正文保留，不回填为光引擎本体字段。

## 边界

- NPO 描述的是光引擎相对 switch / interconnect silicon 的封装位置，不是新的网络协议。
- 7.2 Tb/s 是单引擎传输容量，不能直接与 switch ASIC aggregate capacity 或整机 fabric bandwidth 比较。
- 系统功耗节省、MTBF 与可用度来自 4096 卡 SuperPoD 配置，不属于单个 Hi-ONE 的器件功耗。

## 直接来源

- https://www.huawei.com/cn/news/2026/9/hc-wang-keynote
