---
title: Cambricon-1H
vendor: Cambricon
object_type: ip
status: unknown
architecture: second-generation terminal AI processor IP
process: null
memory: {}
compute:
  1H16:
    fp16_tops: 0.5
    int8_tops: 1.0
  1H8:
    int8_tops: 1.0
  1H8mini:
    int8_tops: 0.5
interconnect: {}
power:
  value_w: null
  scope: ip
lifecycle:
  published: confirmed
updated: 2026-09-15
schema_version: chip-v0.2
layer: ip
legacy_status: published
relations: {}
evidence:
  S1:
    url: https://www.cambricon.com/
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
  architecture:
  - S1
  compute.1H16.fp16_tops:
  - S1
  compute.1H16.int8_tops:
  - S1
  compute.1H8.int8_tops:
  - S1
  compute.1H8mini.int8_tops:
  - S1
  lifecycle.published:
  - S1
  power.scope:
  - S1
---
# Cambricon-1H

> 第二代终端 AI 处理器 IP，公开规格按授权 IP 配置表达。

## 核心规格
| 配置 | 峰值 |
|---|---|
| 1H16 @1GHz | 0.5 TOPS FP16；1 TOPS INT8 |
| 1H8 | 1 TOPS INT8 |
| 1H8mini | 0.5 TOPS INT8 |

## 生命周期与边界
- IP 授权、客户 SoC 量产和当前供货状态公开资料未确认。

## 直接来源
- https://www.cambricon.com/
