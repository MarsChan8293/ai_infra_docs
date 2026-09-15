---
title: "Google TPU 8i"
vendor: Google
object_type: chip
status: announced
architecture: TPU Gen8 inference
process: null
compute_units: {tensor_core: 2, cae: 1}
memory: {type: HBM, capacity_gb: 288, bandwidth_tb_s: 8.601, sram_mb: 384}
compute: {fp4_pflops: 10.1}
interconnect: {boardfly_tb_s: 2.4, boardfly_tbit_s: 19.2}
power: {value_w: null, scope: chip}
lifecycle: {announced: 2026-04-22, cloud_ga: null}
updated: 2026-09-15
---
# Google TPU 8i

> 第八代推理/RL TPU，引入 CAE 与更大片上 SRAM；当前仍 Coming soon。

## 核心规格
- 2 TensorCore；1 CAE。
- FP4 10.1 PFLOPs。
- 288GB HBM；8.601TB/s。
- 384MB SRAM/VMEM。
- Boardfly 19.2Tb/s（2.4TB/s）互联口径。

## 生命周期与边界
- 2026-04-22 宣布，未确认 GA/量产。
- 高层发布写 1,152 芯片，技术拓扑写最多 1,024 active chips；两者均为 Pod 层冲突，不回填芯片。

## 直接来源
- https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive
- https://cloud.google.com/tpu
