---
title: NVIDIA Rubin CPX
vendor: NVIDIA
object_type: gpu
status: roadmap
architecture: Rubin-family
process: null
memory:
  type: GDDR7
  capacity_gb: 128
  bandwidth_tb_s: null
compute:
  nvfp4_pflops_max: 30
interconnect: {}
power:
  value_w: null
  scope: gpu
lifecycle:
  announced: 2025-09-09
  planned_available: 2026-end
updated: 2026-09-15
schema_version: chip-v0.2
layer: chip
relations: {}
evidence:
  S1:
    url: https://nvidianews.nvidia.com/news/nvidia-unveils-rubin-cpx-a-new-class-of-gpu-designed-for-massive-context-inference
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
  architecture:
  - S1
  compute.nvfp4_pflops_max:
  - S1
  lifecycle.announced:
  - S1
  lifecycle.planned_available:
  - S1
  memory.capacity_gb:
  - S1
  memory.type:
  - S1
  power.scope:
  - S1
---
# NVIDIA Rubin CPX

> 面向百万 token 长上下文推理的独立 Rubin 家族 GPU。

## 核心规格
- 128GB GDDR7。
- 最高 30PFLOPS NVFP4。

## 生命周期与边界
- 2025-09-09 宣布；官方口径为预计 2026 年底可用。
- 不能把 CPX 的 GDDR7 与 Rubin GPU 的 HBM4 混写。

## 直接来源
- https://nvidianews.nvidia.com/news/nvidia-unveils-rubin-cpx-a-new-class-of-gpu-designed-for-massive-context-inference
