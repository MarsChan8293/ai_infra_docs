---
title: OpenAI Jalapeño
vendor: OpenAI
object_type: chip
status: unknown
architecture: custom LLM inference accelerator
process: null
memory:
  type: null
  capacity_gb: null
  bandwidth_tb_s: null
compute: {}
interconnect: {}
power:
  value_w: null
  scope: chip
lifecycle:
  officially_disclosed: 2026-06-24
  tapeout: completed
  engineering_sample: confirmed
  initial_measurements: 2026-08-25
  initial_deployment_plan: 2026-end
  mass_production: null
updated: 2026-09-15
schema_version: chip-v0.2
layer: chip
legacy_status: engineering-sample
relations: {}
evidence:
  S1:
    url: https://openai.com/
    source_type: other
    accessed: '2026-09-16'
evidence_map:
  __page__:
  - S1
---
# OpenAI Jalapeño

> OpenAI 第一款公开确认的自定义 LLM 推理芯片，已完成 tape-out、工程样片运行和初步测量，但尚不能写成大规模量产/广泛部署。

## 已确认
- OpenAI 主导设计；Broadcom 参与芯片实现、网络与连接；Celestica 参与板卡/机架/系统工业化。
- 从零面向现代 LLM inference，强调降低 data movement、平衡 compute/memory/network，并兼顾吞吐与低延迟。
- 九个月完成至制造 tape-out；工程样片在实验室按生产目标频率/功耗运行；2026-08-25 公布初步测量。

## 公开资料未确认
- 制程、晶体管、封装、SRAM/cache、HBM、峰值算力、互联拓扑、TDP、ISA。
- 大规模量产、累计出货、客户部署与公开云实例。

## 边界
- 10GW OpenAI-designed accelerators 是多代平台/数据中心部署规模，不能等同于 Jalapeño 单一型号数量。
- OpenAI 模型在 Azure/AWS/OCI 可用不代表使用 Jalapeño。

## 直接来源
- https://openai.com/
