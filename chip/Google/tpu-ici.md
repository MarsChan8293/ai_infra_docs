---
schema_version: chip-v0.2
title: Google TPU Inter-Chip Interconnect (ICI)
vendor: Google
object_type: accelerator-interconnect
layer: network
status: current-catalog
architecture: TPU Inter-Chip Interconnect
process: null
memory: {}
compute: {}
interconnect:
  type: ICI
  scope: TPU slice
  v5p_bidirectional_per_chip_gb_s: 1200
  v6e_bidirectional_per_chip_gb_s: 800
  tpu7x_bidirectional_per_chip_gb_s: 1200
  v5p_topology: 3D torus
  v6e_topology: 2D torus
  tpu7x_topology: 3D torus
  intra_cube_medium: copper
  inter_cube_medium: optical links via optical circuit switches
power: {}
lifecycle: {}
relations:
  used-in:
    - chip/Google/tpu-v5p
    - chip/Google/tpu-v6e-trillium
    - chip/Google/tpu7x-ironwood
evidence:
  S1:
    url: https://docs.cloud.google.com/compute/docs/tpus/tpu-machines
    source_type: cloud
    accessed: '2026-10-05'
  S2:
    url: https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm
    source_type: cloud
    accessed: '2026-10-05'
evidence_map:
  __page__: [S1, S2]
  architecture: [S1, S2]
  interconnect.type: [S1, S2]
  interconnect.v5p_bidirectional_per_chip_gb_s: [S1]
  interconnect.v6e_bidirectional_per_chip_gb_s: [S1]
  interconnect.tpu7x_bidirectional_per_chip_gb_s: [S1]
  interconnect.v5p_topology: [S1, S2]
  interconnect.v6e_topology: [S1, S2]
  interconnect.tpu7x_topology: [S1, S2]
  interconnect.intra_cube_medium: [S2]
  interconnect.inter_cube_medium: [S2]
updated: 2026-10-05
---
# Google TPU Inter-Chip Interconnect (ICI)

> Cloud TPU slice 内连接 TPU chips 的高带宽、低时延专用互联。

## 代际规格

| TPU | 双向 ICI / chip | 典型 topology |
|---|---:|---|
| TPU v5p | 1,200 GB/s | 3D torus |
| TPU v6e / Trillium | 800 GB/s | 2D torus |
| TPU7x / Ironwood | 1,200 GB/s | 3D torus |

Google 的 TPU architecture 文档进一步说明：从 TPU v4 开始，cube 内的 ICI 使用铜连接；cube 之间可通过 optical links 与 optical circuit switches（OCS）连接，并提供 ICI resiliency。

## 边界

- ICI 是 TPU slice 内互联；不同 slice 之间的 Multislice 通信使用 data center network（DCN），不能把两者带宽混为同一 fabric。
- 表中带宽是 bidirectional per chip，不是 Pod aggregate、bisection bandwidth 或 all-reduce 实测带宽。
- 具体 TPU 的芯片规格仍以 [[chip/Google/Google-overview|Google TPU]] 各代页面为准。

## 直接来源

- https://docs.cloud.google.com/compute/docs/tpus/tpu-machines
- https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm
