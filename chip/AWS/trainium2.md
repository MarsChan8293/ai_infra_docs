---
title: AWS Trainium2
vendor: AWS
object_type: chip
status: ga
architecture: NeuronCore-v3
process: null
memory:
  type: HBM
  capacity_gb: 96
  bandwidth_tb_s: 2.9
compute:
  fp8_tflops: 1299
  fp16_tflops: 667
  bf16_tflops: 667
  fp32_tflops: 181
interconnect:
  scale_up: NeuronLink
  bandwidth_tb_s_per_chip: 1.28
power:
  value_w: null
  scope: chip
lifecycle:
  announced: 2023-11
  cloud_available: 2024-12-03
updated: 2026-09-15
schema_version: chip-v0.2
layer: chip
relations: {}
evidence:
  S1:
    url: https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium2.html
    source_type: other
    accessed: '2026-09-16'
  S2:
    url: https://aws.amazon.com/blogs/aws/amazon-ec2-trn2-instances-and-trn2-ultraservers-for-aiml-training-and-inference-is-now-available/
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
  - S2
---
# AWS Trainium2

> Trainium 第二代产品芯片（NeuronCore-v3）；Trn2 UltraServer 是系统层。

## 核心规格
| 字段 | 值 |
|---|---|
| 核心 | 8 × NeuronCore-v3 |
| HBM | 96 GiB；2.9 TB/s |
| FP8 | 1.299 PFLOPS |
| FP16/BF16/TF32 | 667 TFLOPS |
| NeuronLink | 1.28 TB/s/chip |

## 生命周期与边界
- 2023-11 公开；Trn2 GA 2024-12-03。
- Project Rainier 等是平台/客户部署证据，不是单芯片出货审计。

## 直接来源
- https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium2.html
- https://aws.amazon.com/blogs/aws/amazon-ec2-trn2-instances-and-trn2-ultraservers-for-aiml-training-and-inference-is-now-available/
