---
title: NVIDIA HGX B200
vendor: NVIDIA
object_type: baseboard-system
status: production
architecture: 8x B200
gpus: 8
memory:
  aggregate_hbm3e_tb: 1.44
compute:
  board_ai_pflops: 144
  qualifier: vendor_spec
interconnect:
  aggregate_nvlink_tb_s: 14.4
  per_gpu_nvlink_tb_s: 1.8
power:
  value_w: null
  scope: baseboard
updated: 2026-09-15
schema_version: chip-v0.2
layer: board
process: null
lifecycle: {}
relations: {}
evidence:
  S1:
    url: https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory-h100-h200-b200/latest/components.html
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
---
# NVIDIA HGX B200

> 8×B200 的基板/服务器组件层。

## 系统规格
- 1.44TB GPU HBM3e。
- 14.4TB/s 聚合 NVLink；官方表列板级 AI 性能 144PFLOPS。

## 边界
- 14.4TB/s 与 144PFLOPS 都是八卡聚合口径。

## 直接来源
- https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory-h100-h200-b200/latest/components.html
