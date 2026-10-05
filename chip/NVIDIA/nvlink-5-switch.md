---
schema_version: chip-v0.2
title: NVIDIA NVLink 5 Switch
vendor: NVIDIA
object_type: network-switch-generation
layer: network
status: current-catalog
architecture: Fifth-generation NVLink Switch
process: null
memory: {}
compute: {}
interconnect:
  type: NVLink 5 Switch
  gpu_to_gpu_bandwidth_gb_s: 1800
  supported_domain_gpus: [8, 72]
  nvl72_aggregate_tb_s: 130
power: {}
lifecycle: {}
relations:
  compatible-with:
    - chip/NVIDIA/nvlink-5
  used-in:
    - chip/NVIDIA/gb200-nvl72
evidence:
  S1:
    url: https://www.nvidia.com/en-us/data-center/nvlink/
    source_type: official
    accessed: '2026-10-05'
evidence_map:
  __page__: [S1]
  architecture: [S1]
  interconnect.type: [S1]
  interconnect.gpu_to_gpu_bandwidth_gb_s: [S1]
  interconnect.supported_domain_gpus: [S1]
  interconnect.nvl72_aggregate_tb_s: [S1]
updated: 2026-10-05
---
# NVIDIA NVLink 5 Switch

> Blackwell 平台第五代 NVLink 的交换层代际对象，用于把 NVLink GPU domain 从单机扩展到 NVL72。

## 核心规格

- NVIDIA 当前规格表给出 NVLink 5 Switch 的 GPU-to-GPU bandwidth 为 1,800 GB/s。
- 支持 8 GPU 与 72 GPU NVLink domain。
- NVL72 的总聚合带宽为 130 TB/s。

## 边界

- 本页记录 NVLink Switch 代际/平台能力，不把 130 TB/s 解释为单颗 switch ASIC 的交换容量。
- 1,800 GB/s 是 NVIDIA 在 NVLink Switch 表中给出的 GPU-to-GPU 带宽口径，不等于单条 SerDes / 单条 NVLink 的速率。
- NVL72 的拓扑、collective 路径与有效带宽由 [[system/topology/accelerator-fabric|Accelerator Fabric]] 与 [[system/communication/collective-communication|Collective Communication]] 建模。
- 链路代际本身见 [[chip/NVIDIA/nvlink-5|NVIDIA NVLink 5]]。

## 直接来源

- https://www.nvidia.com/en-us/data-center/nvlink/
