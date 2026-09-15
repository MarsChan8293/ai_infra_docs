---
title: AWS Trainium3
vendor: AWS
object_type: chip
status: ga
architecture: NeuronCore-v4
process: 3nm
memory:
  type: HBM3e
  capacity_gb: 144
  bandwidth_tb_s: 4.9
compute:
  mxfp8_pflops: 2.52
  mxfp4_pflops: 2.52
interconnect:
  scale_up: NeuronLink-v4 / NeuronSwitch-v1
power:
  value_w: null
  scope: chip
lifecycle:
  ultraserver_ga: 2025-12-02
  chip_first_public: null
  mass_production: null
updated: 2026-09-15
schema_version: chip-v0.2
layer: chip
relations: {}
evidence:
  S1:
    url: https://aws.amazon.com/ec2/instance-types/trn3/
    source_type: other
    accessed: '2026-09-16'
  S2:
    url: https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html
    source_type: other
    accessed: '2026-09-16'
  S3:
    url: https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
  - S2
  - S3
---
# AWS Trainium3

> AWS 当前公开最完整的新一代 Trainium。144 芯片 Trn3 UltraServer 是平台级 scale-up 域。

## 核心规格
| 字段 | 值 |
|---|---|
| 制程 | 3 nm |
| 核心 | 8 × NeuronCore-v4 |
| HBM | 144 GB HBM3e |
| 带宽 | 4.9 TB/s；NKI 指南另有 4.7 TB/s |
| MXFP8 / MXFP4 | 2.52 PFLOPS |
| DMA / CC-Core | 128 / 20 |

## 生命周期与边界
- Trn3 UltraServer GA 2025-12-02；单芯片首次公开日、量产/出货数量未确认。
- 20.7TB HBM、705.6TB/s、144 芯片属于 UltraServer Gen2 聚合值。
- 4.9 与 4.7TB/s 是两个官方口径，保留冲突。

## 直接来源
- https://aws.amazon.com/ec2/instance-types/trn3/
- https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html
- https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html
