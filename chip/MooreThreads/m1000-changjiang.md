---
title: Moore Threads M1000 / 长江
vendor: Moore Threads
object_type: soc
status: unknown
architecture: 长江
process: null
components:
- CPU
- GPU
- NPU
- VPU
- DPU
- ISP
- Audio_DSP
memory: {}
compute: {}
interconnect: {}
power:
  value_w: null
  scope: soc
updated: 2026-09-15
schema_version: chip-v0.2
layer: soc
legacy_status: current-platform
lifecycle: {}
relations: {}
evidence:
  S1:
    url: https://www.mthreads.com/
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
---
# Moore Threads M1000 / 长江

> 面向端边的异构 SoC，集成 CPU、全功能 GPU、NPU、VPU、DPU、ISP 与 Audio DSP。

## 边界
- E300 是 MXM 模组，AIBOOK/AICUBE 是整机。
- 整机的统一内存/存储和 50TOPS 等组合口径不能拆给单独 NPU 或 GPU 单元。

## 直接来源
- https://www.mthreads.com/
