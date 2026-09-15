---
title: Meta MTIA 400
vendor: Meta
object_type: chip
status: pre-deployment
architecture: MTIA
process: null
chiplets:
  compute: 2
memory:
  type: HBM
  capacity_gb: null
  bandwidth_tb_s: null
compute: {}
interconnect:
  scale_up_domain_accelerators: 72
  scope_note: system
power:
  value_w: null
  scope: chip
lifecycle:
  lab_testing_complete: true
  data_center_deployment: planned
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
---
# Meta MTIA 400

> 从推荐扩展到 GenAI 的 MTIA 代际，实验室测试已完成并走向数据中心部署。

## 边界
- 2 个 compute chiplet 是芯片级。
- 72 加速器 scale-up 域是机架/系统层，不是芯片内部资源。

## 直接来源
- https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/
