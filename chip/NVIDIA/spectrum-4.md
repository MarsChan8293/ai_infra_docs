---
schema_version: chip-v0.2
title: NVIDIA Spectrum-4
vendor: NVIDIA
object_type: network-asic
layer: network
status: current-catalog
architecture: Ethernet switch ASIC
process: null
memory: {}
compute: {}
interconnect:
  switch_capacity_tb_s: 51.2
  max_400gbe_ports: 128
  sn5600_max_800gbe_ports: 64
power: {}
lifecycle: {}
relations: {}
evidence:
  S1:
    url: https://nvidianews.nvidia.com/news/nvidia-announces-spectrum-high-performance-data-center-networking-infrastructure-platform
    source_type: official
    accessed: '2026-09-25'
  S2:
    url: https://networking-docs.nvidia.com/sn5000hw/introduction
    source_type: official
    accessed: '2026-09-25'
evidence_map:
  __page__: [S1, S2]
  architecture: [S1, S2]
  interconnect.switch_capacity_tb_s: [S1, S2]
  interconnect.max_400gbe_ports: [S1]
  interconnect.sn5600_max_800gbe_ports: [S2]
updated: 2026-09-25
---
# NVIDIA Spectrum-4

> 面向高性能数据中心 Ethernet fabric 的 51.2 Tb/s switch ASIC。

## 核心规格

- ASIC aggregate switching throughput：51.2 Tb/s。
- Spectrum-4 平台公开支持 128 × 400GbE。
- 基于 Spectrum-4 的 SN5600 系统可提供 64 × 800GbE。

## 边界

- 51.2 Tb/s 是 switch ASIC / platform switching capacity，不是单 endpoint 带宽。
- SN5600 的端口配置属于 switch system 实现，本页只作为 Spectrum-4 可实现形态的直接证据，不把系统功耗回填到 ASIC。
- Scale-out topology 的 bisection / oversubscription 由 [[system/topology/scale-up-vs-scale-out|Scale-up vs Scale-out]] 建模。

## 直接来源

- https://nvidianews.nvidia.com/news/nvidia-announces-spectrum-high-performance-data-center-networking-infrastructure-platform
- https://networking-docs.nvidia.com/sn5000hw/introduction
