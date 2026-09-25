---
schema_version: chip-v0.2
title: Astera Labs Aries PT5161LX
vendor: Astera Labs
object_type: retimer
layer: chip
status: production
architecture: CXL / PCIe Smart DSP Retimer
process: null
memory: {}
compute: {}
interconnect:
  pcie_generation: PCIe 5.0
  cxl_version: '2.0'
  lanes: 16
power: {}
lifecycle:
  production: confirmed
relations: {}
evidence:
  S1:
    url: https://www.asteralabs.com/product-details/pt5161lx/
    source_type: official
    accessed: '2026-09-25'
  S2:
    url: https://www.asteralabs.com/products/pcie-cxl-smart-dsp-retimers/
    source_type: official
    accessed: '2026-09-25'
evidence_map:
  __page__: [S1, S2]
  architecture: [S1, S2]
  interconnect.pcie_generation: [S1, S2]
  interconnect.cxl_version: [S1, S2]
  interconnect.lanes: [S1, S2]
  lifecycle.production: [S1, S2]
updated: 2026-09-25
---
# Astera Labs Aries PT5161LX

> PCIe 5.0 / CXL 2.0 x16 low-latency Smart DSP Retimer。

## 核心规格

- PCIe 5.0 / CXL 2.0。
- x16 lanes。
- Astera Labs 当前产品页标记为 Production。
- PCIe 5.0 32 GT/s per lane 的 signaling-rate 口径来自 PCIe generation，本页不把它换算成应用 payload bandwidth。

## AI Infra 边界

Retimer 解决高速链路 reach / signal integrity，不创造新的 endpoint bandwidth。它会进入 [[system/topology/numa-and-pcie-topology|NUMA / PCIe Topology]] 的 path，但不应被当成 memory / network capacity 节点。

## 直接来源

- https://www.asteralabs.com/product-details/pt5161lx/
- https://www.asteralabs.com/products/pcie-cxl-smart-dsp-retimers/
