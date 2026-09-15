---
title: NVIDIA DGX B200
vendor: NVIDIA
object_type: server
status: production
architecture: 8x Blackwell GPU
gpus: 8
memory:
  aggregate_gpu_memory_gb: 1440
  aggregate_hbm_bandwidth_tb_s: 64
interconnect:
  aggregate_nvlink_tb_s: 14.4
power:
  max_system_kw: 14.3
  scope: server
updated: 2026-09-15
schema_version: chip-v0.2
layer: system
process: null
compute: {}
lifecycle: {}
relations: {}
evidence:
  S1:
    url: https://www.nvidia.com/en-us/data-center/dgx-b200/
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
  architecture:
  - S1
  interconnect.aggregate_nvlink_tb_s:
  - S1
  memory.aggregate_gpu_memory_gb:
  - S1
  memory.aggregate_hbm_bandwidth_tb_s:
  - S1
  power.max_system_kw:
  - S1
  power.scope:
  - S1
---
# NVIDIA DGX B200

> 八 GPU AI 服务器。14.3kW 是整机最大功耗，不是 B200 TDP。

## 系统规格
- 1,440GB GPU memory；64TB/s HBM3e。
- 14.4TB/s aggregate NVLink。
- 约 14.3kW 最大系统功耗。

## 直接来源
- https://www.nvidia.com/en-us/data-center/dgx-b200/
