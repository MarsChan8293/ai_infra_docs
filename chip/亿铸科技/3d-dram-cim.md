---
title: 亿铸科技 3D DRAM 全数字存算一体技术
vendor: 亿铸科技
object_type: experimental-silicon
status: unknown
architecture: 3D DRAM / Digital CIM
process: null
memory:
  type: 3D stacked DRAM
  capacity_gb: null
  bandwidth_tb_s: null
compute: {}
interconnect: {}
power:
  value_w: null
  scope: silicon
lifecycle:
  tapeout: null
  lab_validation: null
  mass_production: null
updated: 2026-10-17
schema_version: chip-v0.2
layer: unknown
relations: {}
evidence: {}
evidence_map: {}
---
# 亿铸科技 3D DRAM 全数字存算一体

> 公开技术路线跟踪页，**尚非已核实规格的量产芯片型号**。流片、硬件验证、量产及商业部署需要分别举证。

## 需要澄清的微架构
- 计算位置：DRAM 阵列内、Sense Amplifier/Bank Peripheral、独立 Logic Die 还是 Near-Memory。
- 数据流：权重驻留、激活广播、部分和归约、片上网络及跨芯片通信。
- 带宽口径：阵列内部聚合/等效计算带宽、外部 I/O 带宽、LLM 实测有效带宽不可混用。
- 精度与算子：BF16、FP8、INT8、FP4、GEMM、Attention、Softmax、RoPE、Norm。

## LLM 适配核验
- Dense/MoE Decode 的 Batch 1/8/32/128 吞吐与功耗。
- MLA/GQA、KV Cache、长上下文、Expert Routing/All-to-All。
- PyTorch、vLLM、SGLang、编译器、Runtime、Profiling 的实际兼容级别。
- 相同模型/精度/SLA 下对比 GPU 的 TTFT、TPOT、Tokens/s/W。

## 已收录对照
- [[chip/d-Matrix/pavehawk|d-Matrix Pavehawk 3DIMC]]
- [[chip/Samsung/lpddr5x-pim|Samsung LPDDR5X-PIM]]

## 资料核验
- 公开公司网站： https://www.yizhu-tech.com/ （需进一步核对产品技术公告与规格书）
- 技术细节、芯片指标和量产状态以正式规格书、实测及 CTO 交流资料为准。
