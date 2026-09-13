# Broadcom — Thor Ultra 800G AI Ethernet NIC

- 厂商总览：[Broadcom](./Broadcom-overview.md) · [[Broadcom-overview|图谱总览]]
- 产品层级：AI Ethernet NIC / scale-out networking；不是 AI compute accelerator
- 研究截止日：2026-09-13
- 核验日期：2026-09-13

## 产品定位

Thor Ultra 是 Broadcom 面向 AI scale-out 的 800G Ethernet NIC。发布材料将其定位为 Ultra Ethernet Consortium（UEC）特性兼容的开放 Ethernet 接入方案，用于大型 XPU 集群。

## 已公开能力

| 字段 | 官方公开信息 | 边界 |
| --- | --- | --- |
| 网络速率 | 800G Ethernet | NIC 线速口径 |
| 主机接口 | PCIe Gen6 x16 | 主机侧 |
| SerDes | 200G / 100G PAM4 | 物理层能力 |
| form factor | PCIe CEM、OCP 3.0 | 板卡形态 |
| multipathing | packet-level multipathing | UEC/RDMA 数据路径 |
| out-of-order delivery | 支持乱序数据交付 | 网络能力，不等于 XPU 内存规格 |
| retransmission | selective retransmission | 可靠传输 |
| congestion control | receiver/sender programmable | 网络拥塞控制 |

Broadcom 宣称 Thor Ultra 可用于连接数十万颗 XPU。该数字是 fabric/集群规模目标，不能写成单 NIC 的端口数或同时直连 XPU 数量。

## 生命周期

| 阶段 | 状态 |
| --- | --- |
| 发布 | 2025-10-14 |
| sampling | 发布时明确为“now sampling” |
| 量产/广泛出货 | 本次公开资料未确认 |
| 大规模客户部署 | 公开资料未确认 |

因此，Thor Ultra 与已经 shipping 的 Tomahawk Ultra 生命周期不同，不能笼统写成“Broadcom Ultra Ethernet 产品均已量产”。

## AI 基础设施意义

Thor Ultra 解决的核心问题是分布式 AI 的 scale-out 网络：流量分散、拥塞、乱序与重传。它可能影响 collective、参数同步、KV/activation 交换等通信效率，但不执行 GPU/NPU 的 Tensor Core 模型计算，所以本页不记录 FP8/BF16 AI FLOPS。

## 直接来源

- [Broadcom：Broadcom Introduces Industry’s First 800G AI Ethernet NIC，2025-10-14](https://investors.broadcom.com/news-releases/news-release-details/broadcom-introduces-industrys-first-800g-ai-ethernet-nic)
- [Hot Chips 2026 Program](https://hc2026.hotchips.org/program/)

## 未确认项

- 单卡/芯片功耗。
- 片上 buffer、packet processing pipeline 细节。
- sampling 之后的正式量产和客户部署状态。
- 与不同 UEC 交换机组合下的可复现 collective benchmark。
