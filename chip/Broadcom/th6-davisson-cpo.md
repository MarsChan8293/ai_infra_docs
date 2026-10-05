---
schema_version: chip-v0.2
title: Broadcom Tomahawk 6 Davisson CPO
vendor: Broadcom
object_type: cpo-switch
layer: network
status: sampling
architecture: Third-generation co-packaged optics Ethernet switch
process: null
memory: {}
compute: {}
interconnect:
  type: CPO Ethernet
  part_number: BCM78919
  switch_capacity_tb_s: 102.4
  optical_engines: 16
  optical_engine_tb_s: 6.4
  per_link_gbps: 200
  scale_up_xpus: 512
  two_tier_scale_xpus: 100000
power: {}
lifecycle:
  announced: 2025-10-08
  sampling: 2025-10-08
relations: {}
evidence:
  S1:
    url: https://investors.broadcom.com/news-releases/news-release-details/broadcom-announces-tomahawkr-6-davisson-industrys-first-1024
    source_type: official
    accessed: '2026-10-05'
  S2:
    url: https://www.broadcom.com/products/fiber-optic-modules-components/co-packaged-optics/switches
    source_type: official
    accessed: '2026-10-05'
evidence_map:
  __page__: [S1, S2]
  architecture: [S1, S2]
  interconnect.type: [S1, S2]
  interconnect.part_number: [S1, S2]
  interconnect.switch_capacity_tb_s: [S1, S2]
  interconnect.optical_engines: [S1]
  interconnect.optical_engine_tb_s: [S1]
  interconnect.per_link_gbps: [S1]
  interconnect.scale_up_xpus: [S1]
  interconnect.two_tier_scale_xpus: [S1]
  lifecycle.announced: [S1]
  lifecycle.sampling: [S1]
updated: 2026-10-05
---
# Broadcom Tomahawk 6 Davisson CPO

> Broadcom 第三代 Co-Packaged Optics（CPO）Ethernet switch，器件型号 BCM78919。

## 核心规格

- 102.4 Tb/s switching capacity。
- 16 × 6.4 Tb/s Davisson DR optical engines。
- 200 Gb/s per link。
- Broadcom 给出的目标规模为单级 scale-up 512 XPUs；两层网络可扩展到 100,000+ XPUs。
- 光引擎与 Ethernet switch 采用共封装方式，外部激光源模块可现场更换。

## 生命周期口径

Broadcom 2025-10-08 的发布稿标题/正文使用 “shipping” 描述 TH6-Davisson 平台，但 Availability 段明确写明 BCM78919 当时正在向 early-access customers / partners sampling。本库采用更保守的器件级 status= sampling，避免把平台发布口径直接升级为器件全面 GA。

## 边界

- CPO 是 optical engine 与 switch silicon 的封装/物理 I/O 形态，不是 Ethernet 之外的新网络协议。
- 102.4 Tb/s 是 switch aggregate capacity；6.4 Tb/s 是单 optical engine 容量；200 Gb/s 是 per-link 口径，三者不能互换。
- CPO 的系统级功耗收益依赖 pluggable optics 对照基线和完整 switch configuration，本页不把百分比节能换算成器件绝对功耗。

## 直接来源

- https://investors.broadcom.com/news-releases/news-release-details/broadcom-announces-tomahawkr-6-davisson-industrys-first-1024
- https://www.broadcom.com/products/fiber-optic-modules-components/co-packaged-optics/switches
