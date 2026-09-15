---
title: "AWS Trainium"
vendor: AWS
object_type: chip
status: ga
architecture: NeuronCore-v2
process: null
memory: {type: HBM, capacity_gb: 32, bandwidth_tb_s: 0.8}
compute: {fp8_tflops: 191, fp16_tflops: 191, bf16_tflops: 191, fp32_tflops: 48}
interconnect: {scale_up: NeuronLink-v2, bandwidth_tb_s_per_chip: 0.384}
power: {value_w: null, scope: chip}
lifecycle: {announced: 2020-11, cloud_available: 2022-10-10}
updated: 2026-09-15
---
# AWS Trainium

> AWS 第一代 Trainium 芯片；Trn1 / Trn1n 是 EC2 产品层。

## 核心规格
| 字段 | 值 |
|---|---|
| 核心 | 2 × NeuronCore-v2 |
| HBM | 32 GiB；0.8 TB/s |
| FP8 / FP16 / BF16 | 191 TFLOPS |
| FP32 | 48 TFLOPS |
| NeuronLink-v2 | 384 GB/s/chip |

## 生命周期与边界
- 2020-11 公开；Trn1 GA 2022-10-10，Trn1n GA 2023-04-13。
- 量产和累计出货公开资料未确认。

## 直接来源
- https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium.html
- https://aws.amazon.com/ec2/instance-types/trn1/
