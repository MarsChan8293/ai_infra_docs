---
title: Intel Crescent Island
vendor: Intel
object_type: accelerator-card
status: announced
architecture: Xe3P
process: null
compute_units:
  xe_cores: 32
  xmx_engines: 256
memory:
  type: LPDDR5X
  capacity_gb_max: 480
  bandwidth_tb_s: null
compute: {}
interconnect:
  host: PCIe
power:
  value_w: 350
  scope: board
  cooling: air
lifecycle:
  public_architecture: 2026-08-24
  sampling: null
  mass_production: null
updated: 2026-09-15
schema_version: chip-v0.2
layer: accelerator
relations: {}
evidence:
  S1:
    url: https://www.intel.com/content/www/us/en/newsroom/news/client-computing/intel-outlines-architectures-for-agentic-ai-at-hot-chips-2026.html
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
---
# Intel Crescent Island

> 面向数据中心实时 AI 推理的高容量、风冷 PCIe GPU 加速卡。

## 核心规格
- Xe3P；32 Xe Core；256 XMX engine。
- 最高 480GB LPDDR5X。
- 350W 风冷 PCIe 卡。

## 生命周期与边界
- Hot Chips 2026 官方 Intel 材料公开架构与卡级规格。
- 同页的 Intel 18A/Foveros/UCIe 信息属于其他产品，不能回填 Crescent Island。
- 制程、峰值算力、sampling、量产与客户部署未确认。

## 直接来源
- https://www.intel.com/content/www/us/en/newsroom/news/client-computing/intel-outlines-architectures-for-agentic-ai-at-hot-chips-2026.html
