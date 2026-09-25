---
schema_version: chip-v0.2
title: NVIDIA DGX GB200 NVL72 Rack
vendor: NVIDIA
object_type: rack-system
layer: rack
status: production
architecture: DGX GB200 NVL72 rack-scale system
process: null
memory: {}
compute: {}
interconnect:
  nvlink_domain_gpus: 72
  compute_trays: 18
  nvlink_switch_trays: 9
power:
  value_w: 120000
  scope: rack-approximate
  power_shelves: 8
  psus_per_shelf: 6
  psu_w: 5500
lifecycle: {}
relations:
  related:
    - chip/NVIDIA/gb200-nvl72
  connects-via:
    - chip/NVIDIA/nvlink-5
evidence:
  S1:
    url: https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
    source_type: official
    accessed: '2026-09-25'
evidence_map:
  __page__: [S1]
  architecture: [S1]
  interconnect.nvlink_domain_gpus: [S1]
  interconnect.compute_trays: [S1]
  interconnect.nvlink_switch_trays: [S1]
  power.value_w: [S1]
  power.scope: [S1]
  power.power_shelves: [S1]
  power.psus_per_shelf: [S1]
  power.psu_w: [S1]
updated: 2026-09-25
---
# NVIDIA DGX GB200 NVL72 Rack

> 72-GPU NVLink domain 的 DGX Grace Blackwell rack-scale implementation，采用 rack-level liquid cooling 与集中供电。

## 机架构成

- 18 × 1RU compute trays，每 tray 2 Grace CPUs + 4 Blackwell GPUs。
- 9 × 1RU NVLink switch trays。
- NVL72：72-GPU NVLink domain。

## Power / Cooling

- NVIDIA DGX rack user guide 给出约 120 kW rack power consumption。
- 8 个 power shelves；每 shelf 6 × 5.5 kW PSU，并通过 bus bar 向 rack components 供电。
- Compute trays 通过 rack liquid-cooling manifolds / cold plates 冷却；network/storage 等部分组件仍可风冷。

## 边界

- 120 kW 是 DGX GB rack system 的**近似 rack power consumption**，不是单 GPU TDP。
- Power shelf 装机容量与 rack 实际 IT power 不是同一个量。
- Power/cooling 对 workload placement 的影响见 [[system/power/rack-power-and-cooling|Rack Power / Cooling Model]]。

## 直接来源

- https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
