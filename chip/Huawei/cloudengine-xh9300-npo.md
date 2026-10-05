---
schema_version: chip-v0.2
title: Huawei CloudEngine XH9300 NPO Series
vendor: Huawei
object_type: switch-system
layer: network
status: announced
architecture: Near-Packaged Optics AI data center switch system
process: null
memory: {}
compute: {}
interconnect:
  type: NPO switch
  optical_packaging: NPO
  switch_capacity_max_tb_s: 100
  switch_capacity_variant_tb_s: 51.2
  optical_engine_tb_s: 3.2
  centralized_laser: true
  odsp_bypass: true
  optical_engine_field_replaceable: true
power: {}
lifecycle:
  announced: 2026-09-17
relations: {}
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
  interconnect.optical_packaging: [S1, S2]
  interconnect.switch_capacity_max_tb_s: [S1]
  interconnect.switch_capacity_variant_tb_s: [S1]
  interconnect.optical_engine_tb_s: [S1]
  interconnect.centralized_laser: [S1, S2]
  interconnect.odsp_bypass: [S1]
  interconnect.optical_engine_field_replaceable: [S1, S2]
  lifecycle.announced: [S1, S2]
updated: 2026-10-05
---
# Huawei CloudEngine XH9300 NPO Series

> 华为 2026 年发布的全自研 Near-Packaged Optics（NPO）AI 数据中心交换机系列；部分官方材料使用 XH9300-EN 命名。

## 核心规格

- 系列公开容量档位：100T 与 51.2T。
- 采用华为自研 3.2T OE（optical engine）光引擎。
- 光源集约化设计。
- 近封装光学路径省去 oDSP 信号处理环节。
- OE 光引擎采用可插拔卡扣结构，可现场维护。

## 方案级效果

华为公开材料称，XH9300 NPO 方案可将互联功耗降低约 40%；另一份同日发布材料给出互联功耗从 1,000 W 降至 600 W、光电转换时延降低 180 ns、单节点时延优化 26% 的方案口径。

这些数据高度依赖对照方案和节点配置，因此本页不把 600 W 写成单台交换机 power.value_w，也不把 180 ns / 26% 写成设备固有 forwarding latency。

## 边界

- NPO 是 optical I/O / packaging 形态，不是 UnifiedBus 或 Ethernet 等协议名称。
- 本页与 [[chip/Huawei/hi-one-npo|Hi-ONE NPO]] 是不同对象：前者是完整交换机系列，后者是 7.2 Tb/s NPO 光引擎产品；公开来源没有证明 XH9300 使用 Hi-ONE，因此不建立 packaged-in 关系。
- 100T/51.2T 是系列级 switch capacity 档位；3.2T 是单 OE optical engine 口径，不能直接比较。

## 直接来源

- https://e.huawei.com/cn/news/2026/solutions/enterprise-network/xinghe-intelligent-data-center-network
- https://www.huawei.com/cn/news/2026/9/hc-ai-infra-aiwan-campus
