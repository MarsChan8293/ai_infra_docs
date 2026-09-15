---
title: "Groq 3 LPU / LP30"
vendor: Groq
object_type: chip
status: production-ramp
architecture: "LPU / spatial dataflow"
process: null
memory: {type: SRAM, capacity_mb: 500, bandwidth_tb_s: 150}
compute: {fp8_pflops_inferred: 1.2, inferred_from: "8-chip tray 9.6 PFLOPS"}
interconnect: {c2c_links: 96, gbps_per_link: 112, bidirectional_tb_s: 2.5}
power: {value_w: null, scope: chip}
lifecycle: {announced: 2026-03-16, platform_full_production_claim: 2026-03-16, broad_ga: null}
updated: 2026-09-15
---
# Groq 3 LPU / LP30

> Groq 第三代 LPU 芯片，公开产品形态主要是 NVIDIA Vera Rubin 体系中的 Groq 3 LPX。

## 核心规格
- 500MB SRAM；150TB/s。
- 96 条 C2C link，112Gbps/link，双向聚合约 2.5TB/s。
- 8 芯片托盘 9.6PFLOPS FP8 推得约 1.2PFLOPS/芯片，属于推导值，不是单芯片直接规格。

## 生命周期与边界
- 2026-03-16 公开命名；平台公告称进入生产，但 LPX GA/规模部署仍需单独证据。
- LPX 256 LPU、12TB DDR5、40PB/s 等属于机架级。

## 直接来源
- https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/
- https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale
