---
title: "Meta MTIA 300"
vendor: Meta
object_type: chip
status: production
architecture: MTIA
process: null
chiplets: {compute: 1, network: 2}
memory: {type: HBM, capacity_gb: null, bandwidth_tb_s: null}
compute_units: {processing_element: "2 RISC-V vector cores + DPE + SFU + Reduction Engine + DMA"}
compute: {}
interconnect: {}
power: {value_w: null, scope: chip}
lifecycle: {production_deployment: confirmed}
updated: 2026-09-15
---
# Meta MTIA 300

> 面向 Ranking & Recommendation 训练，已在 Meta 生产环境使用。

## 核心架构
- 1 compute chiplet + 2 network chiplet + HBM。
- Processing Element 公开包含 2 个 RISC-V vector core、Dot Product Engine、Special Function Unit、Reduction Engine 与 DMA。

## 直接来源
- https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/
