---
schema_version: chip-v0.2
title: NVIDIA BlueField-3 DPU
vendor: NVIDIA
object_type: dpu
layer: network
status: current-catalog
architecture: Infrastructure compute DPU
process: null
memory:
  type: DDR5
  capacity_gb: 16
compute:
  arm_cores: 16
interconnect:
  ethernet_max_gbps: 400
  infiniband_max_gbps: 400
  host_interface: PCIe Gen5
  host_lanes: 32
power: {}
lifecycle: {}
relations: {}
evidence:
  S1:
    url: https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/documents/datasheet-nvidia-bluefield-3-dpu.pdf
    source_type: datasheet
    accessed: '2026-09-25'
  S2:
    url: https://www.nvidia.com/en-us/networking/products/data-processing-unit/
    source_type: official
    accessed: '2026-09-25'
evidence_map:
  __page__: [S1, S2]
  architecture: [S1, S2]
  memory.type: [S1]
  memory.capacity_gb: [S1]
  compute.arm_cores: [S1]
  interconnect.ethernet_max_gbps: [S1, S2]
  interconnect.infiniband_max_gbps: [S1]
  interconnect.host_interface: [S1]
  interconnect.host_lanes: [S1]
updated: 2026-09-25
---
# NVIDIA BlueField-3 DPU

> 400 Gb/s infrastructure compute DPU，用于 network / storage / security data path offload。

## 核心规格

- Ethernet：最高 400 Gb/s。
- InfiniBand：单端口 NDR 400 Gb/s 或双 NDR200/HDR 配置。
- Host：32 lanes PCIe Gen5。
- 最多 16 Arm cores；板载 16 GB DDR5。

## 边界

- DPU 的 Arm compute 不属于 AI accelerator tensor compute，不能与 GPU TFLOPS 并表。
- 400 Gb/s 是 endpoint network capability，不等于应用 collective 的 effective bandwidth。
- NIC/DPU locality 进入 [[system/topology/gpu-nic-affinity|GPU/NPU ↔ NIC Affinity]]。

## 直接来源

- https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/documents/datasheet-nvidia-bluefield-3-dpu.pdf
- https://www.nvidia.com/en-us/networking/products/data-processing-unit/
