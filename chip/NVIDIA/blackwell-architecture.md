---
title: NVIDIA Blackwell Architecture
vendor: NVIDIA
object_type: gpu-architecture
status: production
architecture: Blackwell
process: TSMC 4NP
transistors_billion: 208
dies: 2
inter_die_link_tb_s: 10
features:
- 2nd-gen Transformer Engine
- FP4
- 5th-gen NVLink
- RAS
- Decompression_Engine
lifecycle:
  announced: 2024-03-18
  full_production_platform: confirmed
updated: 2026-09-15
schema_version: chip-v0.2
layer: unknown
memory: {}
compute: {}
interconnect: {}
power: {}
relations: {}
evidence:
  S1:
    url: https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
---
# NVIDIA Blackwell Architecture

> 两个 reticle-limited GPU die 通过 10TB/s 芯片内链路组成统一 GPU。

## 核心事实
- TSMC 4NP；2080 亿晶体管；双 die。
- 第二代 Transformer Engine、FP4、第五代 NVLink、RAS、硬件 Decompression Engine。

## 生命周期
- 2024-03-18 发布；NVIDIA 当前架构页称 Blackwell 已 full production。

## 直接来源
- https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/
