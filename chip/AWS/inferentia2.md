---
title: AWS Inferentia2
vendor: AWS
object_type: chip
status: ga
architecture: NeuronCore-v2
process: null
memory:
  type: HBM
  capacity_gb: 32
  bandwidth_tb_s: null
compute:
  fp16_tflops: 190
  bf16_tflops: 190
  fp32_tflops: 47.5
interconnect:
  scale_up: NeuronLink
  bandwidth_tb_s_per_chip: 0.384
power:
  value_w: null
  scope: chip
lifecycle:
  announced: 2022 re:Invent
  cloud_available: 2023-04-13
updated: 2026-09-15
schema_version: chip-v0.2
layer: chip
relations: {}
evidence:
  S1:
    url: https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/inferentia2.html
    source_type: other
    accessed: '2026-09-16'
  S2:
    url: https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-ec2-inf2-instances-generative-ai-generally-available/
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
  - S2
---
# AWS Inferentia2

> 第二代 Inferentia，面向生成式 AI 推理；Inf2 已 GA。

## 核心规格
| 字段 | 值 |
|---|---|
| 核心 | 2 × NeuronCore-v2 |
| HBM | 32 GB |
| FP16/BF16/cFP8/TF32 | 190 TFLOPS |
| FP32 | 47.5 TFLOPS |
| NeuronLink | 384 GB/s/chip |

## 生命周期与边界
- 2022 re:Invent 预览；Inf2 GA 2023-04-13。
- EC2 实例最多 12 颗芯片等数字属于实例层。

## 直接来源
- https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/inferentia2.html
- https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-ec2-inf2-instances-generative-ai-generally-available/
