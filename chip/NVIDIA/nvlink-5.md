---
schema_version: chip-v0.2
title: NVIDIA NVLink 5
vendor: NVIDIA
object_type: accelerator-interconnect
layer: network
status: current-catalog
architecture: Fifth-generation NVLink
process: null
memory: {}
compute: {}
interconnect:
  type: NVLink 5
  bandwidth_per_gpu_gb_s: 1800
  links_per_gpu: 18
  max_domain_gpus: 72
  aggregate_nvl72_tb_s: 130
power: {}
lifecycle: {}
relations:
  used-in:
    - chip/NVIDIA/gb200-nvl72
evidence:
  S1:
    url: https://www.nvidia.com/en-us/data-center/nvlink/
    source_type: official
    accessed: '2026-09-25'
evidence_map:
  __page__: [S1]
  architecture: [S1]
  interconnect.type: [S1]
  interconnect.bandwidth_per_gpu_gb_s: [S1]
  interconnect.links_per_gpu: [S1]
  interconnect.max_domain_gpus: [S1]
  interconnect.aggregate_nvl72_tb_s: [S1]
updated: 2026-09-25
---
# NVIDIA NVLink 5

> Blackwell 平台的第五代 NVIDIA GPU scale-up interconnect。

## 核心规格

- 每 GPU NVLink 带宽：1,800 GB/s。
- 每 GPU 最多 18 条 NVLink。
- NVLink 5 Switch 支持 8 / 72 GPU domain；NVL72 聚合带宽为 130 TB/s。

## 边界

- 1,800 GB/s 是 **per GPU NVLink bandwidth**，不是单条 link 带宽。
- 130 TB/s 是 **NVL72 domain aggregate**，不能回填成单个 NVSwitch 芯片带宽。
- Collective 实际有效带宽由 [[system/topology/accelerator-fabric|Accelerator Fabric]] 与 [[system/communication/collective-communication|Collective Communication]] 建模。

## 直接来源

- https://www.nvidia.com/en-us/data-center/nvlink/
