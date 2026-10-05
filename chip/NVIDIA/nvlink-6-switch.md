---
schema_version: chip-v0.2
title: NVIDIA NVLink 6 Switch
vendor: NVIDIA
object_type: network-switch-generation
layer: network
status: announced
architecture: Sixth-generation NVLink Switch
process: null
memory: {}
compute: {}
interconnect:
  type: NVLink 6 Switch
  gpu_to_gpu_bandwidth_gb_s: 3000
  supported_domain_gpus: [8, 72]
  nvl72_aggregate_tb_s: 216
  spec_status: preliminary
  in_network_compute: SHARP
  control_plane_resilience: true
  partial_rack_operation: true
  hot_swappable_switch_trays: true
power: {}
lifecycle:
  announced: 2026-01-05
relations:
  successor-of:
    - chip/NVIDIA/nvlink-5-switch
  compatible-with:
    - chip/NVIDIA/nvlink-6
evidence:
  S1:
    url: https://www.nvidia.com/en-us/data-center/nvlink/
    source_type: official
    accessed: '2026-10-05'
  S2:
    url: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Kicks-Off-the-Next-Generation-of-AI-With-Rubin--Six-New-Chips-One-Incredible-AI-Supercomputer/default.aspx
    source_type: official
    accessed: '2026-10-05'
  S3:
    url: https://developer.nvidia.com/blog/how-nvidia-nvlink-6-delivers-multi-layer-resiliency-for-ai-factories/
    source_type: official
    accessed: '2026-10-05'
evidence_map:
  __page__: [S1, S2, S3]
  architecture: [S1, S2]
  interconnect.type: [S1, S2, S3]
  interconnect.gpu_to_gpu_bandwidth_gb_s: [S1]
  interconnect.supported_domain_gpus: [S1]
  interconnect.nvl72_aggregate_tb_s: [S1]
  interconnect.spec_status: [S1]
  interconnect.in_network_compute: [S1, S2]
  interconnect.control_plane_resilience: [S1, S3]
  interconnect.partial_rack_operation: [S1, S3]
  interconnect.hot_swappable_switch_trays: [S1, S3]
  lifecycle.announced: [S2]
updated: 2026-10-05
---
# NVIDIA NVLink 6 Switch

> Vera Rubin 平台的第六代 NVLink 交换层对象。

## 当前规格

- GPU-to-GPU bandwidth：3,000 GB/s。
- 支持 8-GPU 与 72-GPU NVLink domains。
- NVL72 aggregate：216 TB/s。
- 内置 SHARP in-network reduction / multicast acceleration。
- 新增 control-plane resilience、partial-rack operation 和 hot-swappable switch trays 等可维护性能力。

上述带宽仍被 NVIDIA 标记为 preliminary specification。

## 边界

- 3,000 GB/s 是 NVIDIA NVLink Switch 规格表里的 GPU-to-GPU 口径，不等于单颗 switch 芯片 aggregate capacity。
- 216 TB/s 是 NVL72 domain aggregate。
- 本页不从 NVL72 的 switch tray 数量反推出单颗 NVSwitch capacity。
- 链路代际见 [[chip/NVIDIA/nvlink-6|NVIDIA NVLink 6]]。

## 直接来源

- https://www.nvidia.com/en-us/data-center/nvlink/
- https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Kicks-Off-the-Next-Generation-of-AI-With-Rubin--Six-New-Chips-One-Incredible-AI-Supercomputer/default.aspx
- https://developer.nvidia.com/blog/how-nvidia-nvlink-6-delivers-multi-layer-resiliency-for-ai-factories/
