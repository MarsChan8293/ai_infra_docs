---
title: Meta MTIA 500
vendor: Meta
object_type: chip
status: roadmap
architecture: MTIA
process: null
memory:
  type: HBM
  bandwidth_vs_mtia450: +50%
  capacity_vs_mtia450_max: +80%
compute:
  mx4_vs_mtia450: +43%
interconnect: {}
power:
  value_w: null
  scope: chip
lifecycle:
  planned_large_scale_deployment: 2027
updated: 2026-09-15
schema_version: chip-v0.2
layer: chip
relations: {}
evidence:
  S1:
    url: https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
  architecture:
  - S1
  compute.mx4_vs_mtia450:
  - S1
  lifecycle.planned_large_scale_deployment:
  - S1
  memory.bandwidth_vs_mtia450:
  - S1
  memory.capacity_vs_mtia450_max:
  - S1
  memory.type:
  - S1
  power.scope:
  - S1
---
# Meta MTIA 500

> Meta 2027 GenAI 推理路线图产品。

## 路线图口径
- 相对 450：HBM 带宽 +50%，容量最高 +80%，MX4 FLOPS +43%。
- 绝对 HBM/算力/功耗与制程未公开确认。

## 直接来源
- https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/
