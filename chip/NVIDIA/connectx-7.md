---
schema_version: chip-v0.2
title: NVIDIA ConnectX-7
vendor: NVIDIA
object_type: network-adapter
layer: network
status: current-catalog
architecture: RDMA network adapter / HCA
process: null
memory: {}
compute: {}
interconnect:
  protocols:
    - InfiniBand
    - Ethernet
  total_bandwidth_gbps: 400
  infiniband_ndr_gbps: 400
  ethernet_max_gbps: 400
  host_interface: PCIe Gen5
  host_lanes: 32
  network_ports:
    - 1
    - 2
    - 4
power: {}
lifecycle: {}
relations: {}
evidence:
  S1:
    url: https://www.nvidia.com/en-us/networking/infiniband-adapters/
    source_type: official
    accessed: '2026-09-25'
  S2:
    url: https://www.nvidia.com/content/dam/en-zz/Solutions/networking/infiniband/connectx-7-datasheet.pdf
    source_type: datasheet
    accessed: '2026-09-25'
evidence_map:
  __page__: [S1, S2]
  architecture: [S1, S2]
  interconnect.total_bandwidth_gbps: [S1, S2]
  interconnect.infiniband_ndr_gbps: [S2]
  interconnect.ethernet_max_gbps: [S2]
  interconnect.host_interface: [S2]
  interconnect.host_lanes: [S2]
updated: 2026-09-25
---
# NVIDIA ConnectX-7

> 面向 InfiniBand / Ethernet 的 400 Gb/s RDMA network adapter / HCA。

## 核心规格

- 总网络带宽最高 400 Gb/s。
- InfiniBand 支持 NDR 400 Gb/s；Ethernet 最高 400GbE。
- Host interface 为 PCIe Gen5，产品家族配置最高可使用 32 lanes。
- 产品家族存在 1 / 2 / 4 network-port 配置。

## AI Infra 边界

- Adapter peak throughput 不等于 workload 的有效 scale-out bandwidth。
- Accelerator ↔ NIC path 仍需结合 [[system/topology/gpu-nic-affinity|GPU/NPU ↔ NIC Affinity]]。
- Collective / RDMA 实际成本进入 [[system/communication/communication-cost-model|Communication Cost Model]]。

## 直接来源

- https://www.nvidia.com/en-us/networking/infiniband-adapters/
- https://www.nvidia.com/content/dam/en-zz/Solutions/networking/infiniband/connectx-7-datasheet.pdf
