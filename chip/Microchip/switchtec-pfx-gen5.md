---
schema_version: chip-v0.2
title: Microchip Switchtec PFX Gen 5
vendor: Microchip
object_type: pcie-switch-family
layer: chip
status: current-catalog
architecture: PCIe Gen5 fanout switch family
process: null
memory: {}
compute: {}
interconnect:
  pcie_generation: PCIe Gen5
  max_lanes: 100
  max_ports: 52
  virtual_switch_partitions: 26
  non_transparent_bridges: 48
power: {}
lifecycle: {}
relations: {}
evidence:
  S1:
    url: https://www.microchip.com/en-us/products/interface-networking-connectivity/pcie/pcie-switches
    source_type: official
    accessed: '2026-09-25'
evidence_map:
  __page__: [S1]
  architecture: [S1]
  interconnect.pcie_generation: [S1]
  interconnect.max_lanes: [S1]
  interconnect.max_ports: [S1]
  interconnect.virtual_switch_partitions: [S1]
  interconnect.non_transparent_bridges: [S1]
updated: 2026-09-25
---
# Microchip Switchtec PFX Gen 5

> PCIe Gen5 fanout switch family，用于扩展 CPU/root complex 到 accelerator、NIC、storage 等 PCIe endpoint 的拓扑。

## 核心规格

- PCIe Gen5。
- 最高 100 lanes、52 ports。
- 最高 26 virtual switch partitions、48 Non-Transparent Bridges。

## 边界

- 这是 PCIe switch family，不是 Ethernet / InfiniBand switch。
- Lane/port 数描述 topology fanout 能力，不等于某一 endpoint 的有效传输带宽。
- Shared uplink / fanout contention 由 [[system/topology/numa-and-pcie-topology|NUMA / PCIe Topology]] 建模。

## 直接来源

- https://www.microchip.com/en-us/products/interface-networking-connectivity/pcie/pcie-switches
