---
title: Google TPU7x / Ironwood
vendor: Google
object_type: chip
status: ga
architecture: TPU7x
process: null
compute_units:
  tensor_core: 2
  sparse_core_physical: 4
memory:
  type: HBM
  capacity_gib: 192
  bandwidth_tb_s: 7.38
compute:
  bf16_tflops: 2307
  fp8_tflops: 4614
interconnect:
  ici_gb_s_bidirectional: 1200
power:
  value_w: null
  scope: chip
lifecycle:
  announced: 2025-04-09
  cloud_ga: 2026-03-31
updated: 2026-09-15
schema_version: chip-v0.2
layer: chip
relations: {}
evidence:
  S1:
    url: https://docs.cloud.google.com/tpu/docs/tpu7x
    source_type: other
    accessed: '2026-09-16'
  S2:
    url: https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
  - S2
---
# Google TPU7x / Ironwood

> Google 当前 GA 的高端 TPU。SparseCore 的物理单元和编程模型逻辑 core 口径不同。

## 核心规格
- 2 TensorCore；4 physical SparseCore。
- BF16 2,307 TFLOPs；FP8 4,614 TFLOPs。
- 192 GiB HBM；7.38 TB/s。
- ICI 1,200 GB/s 双向。

## 生命周期与边界
- 2025-04-09 首次披露；2026-03-31 GA。
- 9,216 芯片 Pod、约 1.77PB HBM、近 10MW 是 Pod 系统级。
- JAX 可见 2 logical SparseCore / 4 physical cores，不相加。

## 直接来源
- https://docs.cloud.google.com/tpu/docs/tpu7x
- https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm
