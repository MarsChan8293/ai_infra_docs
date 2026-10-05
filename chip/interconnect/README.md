---
title: AI Interconnect / Fabric / Optical I/O
tags: [moc, chip, interconnect, fabric, optical]
updated: 2026-10-05
---
# AI Interconnect / Fabric / Optical I/O

本页是 AI accelerator 互联硬件的跨厂商入口。目标不是把所有“网络”对象放在一起，而是明确区分协议/链路代际、交换层、物理/光 I/O 形态、系统 topology，避免不同 scope 的带宽数字直接横比。

## 对象分层

```text
Accelerator / XPU
        │
        ├─ protocol / link generation
        │  NVLink · Infinity Fabric · ICI · UALink · UnifiedBus
        │
        ▼
Switch / fabric silicon or switch generation
        │
        ├─ electrical SerDes / copper
        ├─ pluggable optics
        ├─ LPO / NPO
        └─ CPO
        │
        ▼
Physical fabric / fiber
        │
        ▼
System topology / collective behavior
```

Hardware 页只记录对象本体的可验证事实；fabric bisection、oversubscription、collective efficiency、placement 与 failure domain 由 [[system/topology/accelerator-fabric|Accelerator Fabric]] 等 System 页面建模。

## Scale-up interconnect

| 对象 | 类型 | 当前重点 |
|---|---|---|
| [[chip/NVIDIA/nvlink-5|NVIDIA NVLink 5]] | accelerator interconnect | 1,800 GB/s per GPU；18 links |
| [[chip/NVIDIA/nvlink-5-switch|NVIDIA NVLink 5 Switch]] | switch generation | 8/72 GPU domain；NVL72 130 TB/s aggregate |
| [[chip/UALink/ualink-1-0|UALink 200G 1.0]] | open interconnect standard | 200G/lane；最多 1,024 accelerators |
| [[chip/AMD/infinity-fabric-instinct|AMD Infinity Fabric for Instinct]] | accelerator interconnect | MI300X 1,024 GB/s peak aggregate P2P |
| [[chip/Google/tpu-ici|Google TPU ICI]] | accelerator interconnect | v5p/v6e/TPU7x per-chip ICI + torus topology |
| [[chip/Huawei/unifiedbus-2|Huawei UnifiedBus 2.0 / 灵衢 2.0]] | SuperPoD interconnect standard | memory semantics；TB-class；约 2.1 μs RTT |
| [[chip/Broadcom/tomahawk-ultra|Broadcom Tomahawk Ultra]] | scale-up Ethernet switch ASIC | 51.2 Tb/s |

## Optical I/O

| 对象 | 形态 | 当前重点 |
|---|---|---|
| [[chip/Broadcom/th6-davisson-cpo|Broadcom TH6 Davisson CPO]] | CPO switch | 102.4 Tb/s；16 × 6.4T optical engines；200G/link |
| [[chip/Huawei/hi-one-npo|Huawei Hi-ONE NPO]] | NPO optical engine | 7.2 Tb/s / engine；内置光源 |

### CPO / NPO 不是协议

- CPO (Co-Packaged Optics)：optical engines 与 switch / XPU silicon 进入同一 package 或极紧密的共封装体系，核心目标是缩短高速电路径、提高 bandwidth density、降低 I/O power。
- NPO (Near-Packaged Optics)：optical engine 位于主 silicon package 附近但保持更强的模块化/可维护性；具体机械、电气与光学边界依产品实现而异。
- LPO / pluggable optics：属于不同的 optical I/O implementation，不应与 NVLink / UALink / Ethernet 等 protocol/fabric 名称放在同一比较列。

## Scale-out / NIC / Switch

现有代表对象：

- [[chip/NVIDIA/connectx-7|NVIDIA ConnectX-7]]
- [[chip/NVIDIA/bluefield-3|NVIDIA BlueField-3]]
- [[chip/NVIDIA/spectrum-4|NVIDIA Spectrum-4]]
- [[chip/Broadcom/thor-ultra|Broadcom Thor Ultra]]

## 后续缺口

优先继续补：

1. NVIDIA NVLink 6 / NVLink 6 Switch，按链路代际与 switch generation 分页。
2. Huawei UnifiedBus 互联设备：LinkBlade、LinkDevice、UBG / SF9300，并与协议页分层。
3. Huawei CloudEngine XH9300 NPO switch，区分 NPO optical engine 与完整 switch system。
4. Broadcom TH5-Bailly、更多 CPO generation，以及 CPO / NPO / LPO 横向字段。
5. UEC / Scale-Up Ethernet (SUE) 等开放 Ethernet fabric 标准与对应 silicon implementation。
6. 其他厂商自研 accelerator fabric；只在有直接公开 Evidence 时建独立对象。

## 横向比较字段

互联对象优先比较：

- protocol / generation
- per-lane / per-link signaling rate
- per-device injection / P2P bandwidth
- switch aggregate capacity
- radix / port count
- scale-up domain size
- latency / RTT scope
- topology
- electrical / optical medium
- pluggable / LPO / NPO / CPO packaging
- optical engine bandwidth
- laser source placement
- lifecycle / shipping status

任何数字必须保留 lane / link / engine / device / switch / domain / rack / cluster scope。
