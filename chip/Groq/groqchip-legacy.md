---
title: "GroqChip Processor"
vendor: Groq
object_type: chip
status: legacy
architecture: LPU
process: 14nm
memory: {type: SRAM, capacity_mb: 230, bandwidth_tb_s: 80}
compute: {}
interconnect: {}
power: {max_w: 300, tdp_w: 215, average_w: 185, scope: chip}
lifecycle: {product_object_confirmed: true, mass_production_date: null}
updated: 2026-09-15
---
# GroqChip Processor

> Groq 第一代/上一代 LPU 基线。

## 核心规格
- 14nm；230MB 片上 SRAM；80TB/s。
- 300W max / 215W TDP / 185W average，三个功耗口径不得混成一个。

## 边界
- GroqCloud tokens/s 是服务指标，不是 GroqChip 峰值。
- 当前云后端是否仍由该代芯片承载公开资料未确认。

## 直接来源
- https://www.groq.com/GroqDocs/Product%20Spec%20Sheet%20-%20GroqChip%E2%84%A2%20Processor.pdf
- https://groq.com/blog/the-groq-lpu-explained
