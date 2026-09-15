---
title: "Cerebras Wafer-Scale Engines"
vendor: Cerebras
object_type: vendor-overview
updated: 2026-09-15
---
# Cerebras Wafer-Scale Engines

Cerebras 的处理器对象是整片晶圆。WSE、CS 系统、MemoryX 与云服务必须分层。

| 对象 | 层级 | 状态 | 关键事实 |
|---|---|---|---|
| [[chip/Cerebras/wse-3|WSE-3]] | wafer-scale processor | production | 5nm；4T transistors；44GB SRAM |
| [[chip/Cerebras/wse-3-turbo|WSE-3 Turbo]] | wafer-scale processor | announced | 250 PFLOPS sparse FP16；43.2PB/s |

## 边界
- CS-3 15U / ~23kW 是系统，不是 WSE-3 TDP。
- CS-4 = 3 × WSE-3T + power/cooling/network，系统聚合值不回填单 WSE。

## 来源
- https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine
- https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions
