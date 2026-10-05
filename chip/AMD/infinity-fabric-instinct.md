---
schema_version: chip-v0.2
title: AMD Infinity Fabric for Instinct
vendor: AMD
object_type: accelerator-interconnect
layer: network
status: current-catalog
architecture: AMD Infinity Fabric interconnect for Instinct OAM platforms
process: null
memory: {}
compute: {}
interconnect:
  type: AMD Infinity Fabric
  mi300x_peak_p2p_gb_s: 1024
  mi300x_max_links_per_oam: 8
  mi300x_peer_links_in_8gpu_node: 7
  mi300x_node_gpus: 8
  mi325x_generation: 4
power: {}
lifecycle: {}
relations:
  used-in:
    - chip/AMD/mi300x
    - chip/AMD/mi325x
evidence:
  S1:
    url: https://www.amd.com/en/products/accelerators/instinct/mi300.html
    source_type: official
    accessed: '2026-10-05'
  S2:
    url: https://instinct.docs.amd.com/develop/gpu-arch/mi300.html
    source_type: official
    accessed: '2026-10-05'
evidence_map:
  __page__: [S1, S2]
  architecture: [S1, S2]
  interconnect.type: [S1, S2]
  interconnect.mi300x_peak_p2p_gb_s: [S1]
  interconnect.mi300x_max_links_per_oam: [S1]
  interconnect.mi300x_peer_links_in_8gpu_node: [S2]
  interconnect.mi300x_node_gpus: [S2]
  interconnect.mi325x_generation: [S1]
updated: 2026-10-05
---
# AMD Infinity Fabric for Instinct

> AMD Instinct OAM 平台用于 GPU↔GPU scale-up 的 Infinity Fabric 互联。

## 核心规格

- AMD 对 MI300X 给出的峰值 aggregate GPU P2P transport rate 为最高 1,024 GB/s / GPU OAM。
- MI300X OAM 最多包含 8 条 Infinity Fabric links；在典型 8-GPU 全互联节点中，每颗 GPU 使用 7 条 peer links 与其余 7 颗 GPU 直接连接。
- AMD 明确将 MI325X 8-GPU 平台描述为通过 4th-Gen AMD Infinity Fabric links 全互联。

## 边界

- Infinity Fabric 同时承担 die/package 内与 device/node 级互联；本页只聚焦 Instinct accelerator 的 device-to-device scale-up 事实。
- 1,024 GB/s 是 MI300X OAM 的 peak aggregate P2P transport rate，不应推广成所有 Infinity Fabric 代际的统一速率。
- 8 条 link 与 8-GPU 节点中 7 条 peer link 的口径不同：前者是 OAM 可用 link 数，后者是全互联拓扑中的 GPU peer 连接数。
- 节点级 collective efficiency、contention 与 topology mapping 留给 [[system/topology/accelerator-fabric|Accelerator Fabric]]。

## 直接来源

- https://www.amd.com/en/products/accelerators/instinct/mi300.html
- https://instinct.docs.amd.com/develop/gpu-arch/mi300.html
