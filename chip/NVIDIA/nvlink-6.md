---
schema_version: chip-v0.2
title: NVIDIA NVLink 6
vendor: NVIDIA
object_type: accelerator-interconnect
layer: network
status: announced
architecture: Sixth-generation NVLink
process: null
memory: {}
compute: {}
interconnect:
  type: NVLink 6
  bandwidth_per_gpu_gb_s: 3000
  links_per_gpu: 36
  max_domain_gpus: 72
  aggregate_nvl72_tb_s: 216
  spec_status: preliminary
  natively_lossless: true
  credit_based_flow_control: true
power: {}
lifecycle:
  announced: 2026-01-05
relations:
  successor-of:
    - chip/NVIDIA/nvlink-5
  used-in:
    - chip/NVIDIA/rubin-gpu
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
  S4:
    url: https://developer.nvidia.com/blog/nvidia-nvlink-the-scale-up-network-for-ai-factories/
    source_type: official
    accessed: '2026-10-05'
evidence_map:
  __page__: [S1, S2, S3, S4]
  architecture: [S1, S2]
  interconnect.type: [S1, S2, S3]
  interconnect.bandwidth_per_gpu_gb_s: [S1]
  interconnect.links_per_gpu: [S1]
  interconnect.max_domain_gpus: [S1, S3]
  interconnect.aggregate_nvl72_tb_s: [S1]
  interconnect.spec_status: [S1]
  interconnect.natively_lossless: [S3]
  interconnect.credit_based_flow_control: [S3]
  lifecycle.announced: [S2]
updated: 2026-10-05
---
# NVIDIA NVLink 6

> NVIDIA Rubin / Vera Rubin 平台的第六代 GPU scale-up interconnect。

## 当前规格口径

截至 2026-10-05，NVIDIA 英文 NVLink 产品页给出的 preliminary specification 为：

- NVLink bandwidth：3,000 GB/s per GPU。
- 最大 36 条 NVLink / GPU。
- NVLink domain：最高 72 GPUs。
- Vera Rubin NVL72 aggregate：216 TB/s。

## 官方规格修订记录

NVIDIA 在 2026-01 Rubin 发布稿和 2026-07 技术博客中曾公开过 3.6 TB/s per GPU / 260 TB/s per NVL72 的数字；当前英文产品页和 Vera Rubin 产品页已改为 3.0 TB/s / 216 TB/s。

因此本库：

1. 结构化字段采用当前英文产品页口径。
2. 保留早期官方数字作为规格演进记录，不把两组数字合并或平均。
3. spec_status 保留 preliminary，后续 NVIDIA 若再次更新，以当前官方产品页为准。

## Resiliency

NVIDIA 2026-09 的技术资料明确描述 NVLink 6 为 natively lossless fabric，并使用 credit-based flow control（CBFC）、FEC、Physical Layer Retry 与 UPHY recovery 等机制。

## 边界

- 3,000 GB/s 是 per-GPU aggregate NVLink bandwidth，不是单条 NVLink 速率。
- 216 TB/s 是 72-GPU NVL72 domain aggregate，不是单颗 switch ASIC capacity。
- 36 是每 GPU 最大 NVLink 数，不等价于 switch port count。
- NVLink Switch 交换层见 [[chip/NVIDIA/nvlink-6-switch|NVIDIA NVLink 6 Switch]]。

## 直接来源

- https://www.nvidia.com/en-us/data-center/nvlink/
- https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Kicks-Off-the-Next-Generation-of-AI-With-Rubin--Six-New-Chips-One-Incredible-AI-Supercomputer/default.aspx
- https://developer.nvidia.com/blog/how-nvidia-nvlink-6-delivers-multi-layer-resiliency-for-ai-factories/
- https://developer.nvidia.com/blog/nvidia-nvlink-the-scale-up-network-for-ai-factories/
