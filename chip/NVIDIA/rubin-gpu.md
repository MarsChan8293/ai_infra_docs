---
title: NVIDIA Rubin GPU
vendor: NVIDIA
object_type: gpu
status: unknown
architecture: Rubin
process: null
transistors_billion: 336
compute_units:
  sm: 224
  tensor_cores: 896
memory:
  type: HBM4
  capacity_gb: 288
  bandwidth_tb_s: 22
compute:
  nvfp4_inference_pflops_sparse: 50
  nvfp4_training_pflops_dense: 35
interconnect:
  nvlink_generation: 6
  nvlink_tb_s_bidirectional: 3.6
  host: PCIe Gen6 x16, 256GB/s
power:
  value_w: null
  scope: gpu
lifecycle:
  announced: 2026-01-05
  full_production_platform_claim: 2026-03-16
  ramp: 2026-05-31
updated: 2026-09-15
schema_version: chip-v0.2
layer: unknown
legacy_status: production-ramp
relations: {}
evidence:
  S1:
    url: https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/
    source_type: other
    accessed: '2026-09-16'
  S2:
    url: https://www.nvidia.com/en-gb/data-center/nvlink/
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
  - S2
---
# NVIDIA Rubin GPU

> Rubin 平台主 GPU，当前处于量产爬坡/伙伴部署阶段。

## 核心规格
- 3360 亿晶体管；224 SM；896 Tensor Core。
- 288GB HBM4；22TB/s。
- NVFP4 inference 50PFLOPS（sparse）；training 35PFLOPS（dense）。
- NVLink6 3.6TB/s 双向；PCIe6 x16 256GB/s。

## 边界
- 制程与单 GPU TDP 未公开确认。
- NVL72 260TB/s 等是系统级。

## 直接来源
- https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/
- https://www.nvidia.com/en-gb/data-center/nvlink/
