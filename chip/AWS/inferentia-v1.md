---
title: AWS Inferentia
vendor: AWS
object_type: chip
status: ga
architecture: NeuronCore-v1
process: null
memory:
  type: DDR4
  capacity_gb: 8
  bandwidth_tb_s: 0.05
compute:
  int8_tops: 128
  fp16_tflops: 64
  bf16_tflops: 64
interconnect: {}
power:
  value_w: null
  scope: chip
lifecycle:
  announced: 2018-11-28
  cloud_available: 2019-12
updated: 2026-09-15
schema_version: chip-v0.2
layer: chip
relations: {}
evidence:
  S1:
    url: https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/inferentia.html
    source_type: other
    accessed: '2026-09-16'
  S2:
    url: https://aws.amazon.com/ai/machine-learning/inferentia/
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
  - S2
---
# AWS Inferentia

> AWS 第一代推理 ASIC，只通过 EC2/托管服务提供，不是可独立采购的 PCIe 商品。

## 核心规格
| 字段 | 值 |
|---|---|
| 核心 | 4 × NeuronCore-v1 |
| 内存 | 8 GB DDR4；50 GB/s |
| INT8 | 128 TOPS |
| FP16/BF16 | 64 TFLOPS |

## 生命周期与边界
- 2018-11-28 首次公开；Inf1 于 2019-12 GA。
- Tape-out、送样、晶圆量产和累计出货公开资料未确认。

## 直接来源
- https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/inferentia.html
- https://aws.amazon.com/ai/machine-learning/inferentia/
