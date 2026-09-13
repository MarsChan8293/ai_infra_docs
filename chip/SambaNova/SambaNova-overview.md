# SambaNova 芯片资料

- 研究截止日：2026-09-13
- 核验日期：2026-09-13
- 厂商范围：SambaNova Reconfigurable Dataflow Unit（RDU）及其强绑定系统边界
- 证据原则：单 RDU、8 芯片 node、16 芯片 SambaRack 与 256 RDU scale-up 分开记录

## 芯片页关系导航

- [[sn50|SambaNova — SN50 RDU]] · [打开 Markdown](./sn50.md)

## 当前结论

SN50 是 SambaNova 第五代 RDU，定位于大规模、agentic AI 推理。官方产品页给出的单芯片关键规格为 **TSMC 5nm、Reconfigurable Dataflow Architecture、432MB 片上 SRAM、64GB HBM2E，以及最高 512GB DDR5 容量层**；计算口径为 **1600 TFLOPS BF16、3200 TFLOPS FP8**。

SN50 采用三级内存层次，把片上 SRAM、HBM 与大容量 DDR5 分层使用。这个设计方向与传统 GPU 的统一显存叙事不同，因此不能把“最高 512GB DDR5”误写成片上或 HBM 容量，也不能把多芯片系统的内存容量回填给单 RDU。

## 系统边界

| 层级 | 公开信息 | 边界 |
| --- | --- | --- |
| 单 SN50 RDU | 432MB SRAM、64GB HBM2E、最高 512GB DDR5；5nm | 芯片/加速器级 |
| Node | 官方产品表列出 8 chips per node | 节点级，不是芯片核心数 |
| SambaRack SN50 | 16 颗 SN50 | 机架级系统 |
| 多机架 scale-up | 最高 256 RDUs，多 TB/s 互联 | 系统/网络级 |

## 生命周期

SambaNova 在 2026-02-24 正式发布 SN50 与 SambaRack SN50，并表示“将在 2026 年下半年开始向客户出货”。截至本次核验，官方产品页已经将 SN50 作为当前产品展示，也有单机架实测/演示材料；但没有找到足够清晰的官方公告证明“面向广泛客户的大规模出货”已经完成。因此资料库保留为：**已发布、已公开产品化资料；客户出货计划为 2026H2，实际广泛出货状态公开资料未充分确认。**

## 软件与架构边界

RDU 通过 dataflow 映射减少不必要的数据搬运，SambaNova 的系统软件负责图编译和运行时调度。厂商给出的与 GPU 的倍数性能、tokens/s、TCO 等结果必须带模型、批大小、上下文和系统配置，不能作为 SN50 的无条件峰值指标。

## 直接来源

- [SambaNova：RDU / SN50 产品页](https://sambanova.ai/products/rdu-ai-chips)
- [SambaNova：Introducing the SN50 RDU，2026-02-24](https://sambanova.ai/blog/introducing-the-sn50-rdu-purpose-built-for-agentic-inference)
- [SambaNova：SambaRack](https://sambanova.ai/products/sambarack)
- [Hot Chips 2026 Program](https://hc2026.hotchips.org/program/)

## 待补证据

- SN50 单芯片 TDP、封装与 die/chiplet 组织。
- HBM2E 与 DDR5 的实际带宽以及三级内存的寻址/一致性细节。
- 256 RDU 互联拓扑、链路宽度和协议的完整技术文档。
- 2026H2 实际客户出货、部署数量和可复现第三方 benchmark。
