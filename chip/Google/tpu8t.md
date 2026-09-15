---
title: "Google TPU 8t"
vendor: Google
object_type: chip
status: announced
architecture: TPU Gen8 training
process: null
memory: {type: HBM, capacity_gb: 216, bandwidth_tb_s: 6.528, vmem_mb: 128}
compute: {fp4_pflops: 12.6}
interconnect: {ici: "2x Ironwood bandwidth; absolute chip value not public"}
power: {value_w: null, scope: chip}
lifecycle: {announced: 2026-04-22, cloud_ga: null}
updated: 2026-09-15
---
# Google TPU 8t

> 第八代训练 TPU，当前官方产品页仍为 Coming soon。

## 核心规格
- 原生 FP4，峰值 12.6 PFLOPs。
- 216GB HBM；6.528TB/s。
- 128MB VMEM。
- ICI scale-up 带宽为 Ironwood 的 2×，单芯片绝对值未公开。

## 边界
- 9,600 芯片、2PB HBM、121 ExaFlops 是 Superpod 系统级。

## 直接来源
- https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive
- https://cloud.google.com/tpu
