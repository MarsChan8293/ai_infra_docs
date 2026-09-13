# Hot Chips 2026 议程对照与本地资料补强

- 会议日期：2026-08-23 至 2026-08-25（美国太平洋时间）
- 本次核对日期：2026-09-13
- 官方议程：[HC2026 Program](https://hc2026.hotchips.org/program/)
- 资料边界：[官方 FAQ](https://hc2026.hotchips.org/faq/) 说明，演讲 PDF 在演讲当天向参会者提供，录像和幻灯片计划于 2026 年 12 月初向公众开放。

## 使用口径

官方议程只能证明“会议安排了该主题”。本轮额外使用厂商在会前、会中或会后公开的一手 Newsroom、产品页与架构文章补齐可核验事实，但**不把尚未公开的 Hot Chips 幻灯片内容自行还原**。

| 标签 | 含义 |
| --- | --- |
| `[官方议程]` | Hot Chips 2026 官方节目页直接列出的演讲、教程或海报 |
| `[本地已有]` | 当前仓库已有相关厂商或产品资料 |
| `[厂商资料已回填]` | 已用厂商公开一手页面补齐产品规格/状态，不等于 HC 幻灯片已公开 |
| `[待公开材料]` | 完整 HC2026 幻灯片/录像仍未公众开放，页码级证据待后补 |
| `[专题待补]` | 跨厂商背景专题仍可扩展，但不阻塞厂商/产品建档 |

## 与现有资料的对照

| 会议主题 | 议程对象 | 当前本地对应 | 覆盖判断 | 下一步 |
| --- | --- | --- | --- | --- |
| GPU | NVIDIA Rubin GPU | [NVIDIA/rubin-gpu.md](./NVIDIA/rubin-gpu.md)、[NVIDIA/rubin-cpx.md](./NVIDIA/rubin-cpx.md) | `[官方议程][本地已有][待公开材料]` | HC2026 幻灯片公开后补页码和架构增量；不要把 Vera Rubin 系统值回填到单 GPU |
| GPU | AMD Instinct MI400 Series GPU Architecture；MI400 System Architecture | [AMD/mi455x.md](./AMD/mi455x.md)、[AMD/mi430x.md](./AMD/mi430x.md)、[AMD/mi500.md](./AMD/mi500.md) | `[官方议程][本地已有][待公开材料]` | 保持 MI400 芯片、EAM、Helios 托盘/机架分层 |
| GPU | Intel Crescent Island | [Intel/crescent-island.md](./Intel/crescent-island.md) | `[官方议程][本地已有][厂商资料已回填][待公开材料]` | Intel 已公开 Xe3P、32 Xe Core、256 XMX、最高 480GB LPDDR5X、350W PCIe 卡；制造节点/量产仍未确认 |
| AI 系统 | Meta Custom AI Silicon | [Meta/Meta-overview.md](./Meta/Meta-overview.md)、[MTIA 300](./Meta/mtia-300.md)、[MTIA 400](./Meta/mtia-400.md)、[MTIA 450](./Meta/mtia-450.md)、[MTIA 500](./Meta/mtia-500.md) | `[官方议程][本地已有][厂商资料已回填][待公开材料]` | 300 已生产；400 测试完成待部署；450/500 保持 2027 计划状态 |
| AI 系统 | Microsoft MAIA 200 Accelerator | [Microsoft/maia-200.md](./Microsoft/maia-200.md) | `[官方议程][本地已有][厂商资料已回填][待公开材料]` | 已补 3nm、HBM3e/SRAM、算力、750W、on-die NIC 和生产部署；6,144 accelerators 保持系统级 |
| AI 系统 | Cerebras Rack-Scale Architecture for Wafer Scale Engine | [Cerebras/wse-3.md](./Cerebras/wse-3.md)、[Cerebras/wse-3-turbo.md](./Cerebras/wse-3-turbo.md) | `[官方议程][本地已有][待公开材料]` | 完整材料公开后补 rack-scale 细节；保持 WSE-3、WSE-3 Turbo、CS-4 层级分开 |
| AI 系统 | NVIDIA Think Fast: LPU Accelerator for Heterogeneous Compute | [NVIDIA/NVIDIA-overview.md](./NVIDIA/NVIDIA-overview.md) | `[官方议程][待公开材料]` | 待公开材料后判断是新芯片、系统加速器或架构概念 |
| AI 系统 | SambaNova SN50 RDU | [SambaNova/sn50.md](./SambaNova/sn50.md) | `[官方议程][本地已有][厂商资料已回填][待公开材料]` | 已补 5nm、BF16/FP8、SRAM/HBM2E/DDR5 与系统层；继续确认 2026H2 实际客户出货 |
| AI 系统 | Google Eighth Generation TPU Family | [Google/tpu8t.md](./Google/tpu8t.md)、[Google/tpu8i.md](./Google/tpu8i.md) | `[官方议程][本地已有][待公开材料]` | 保留 TPU 8t/8i Coming soon；会议演讲不能自动升级 GA/量产 |
| AI 系统 | OpenAI “You Can Just Build … Chips” | [openai/jalapeno.md](./openai/jalapeno.md)、[openai/openai-overview.md](./openai/openai-overview.md) | `[官方议程][本地已有][待公开材料]` | 继续把 tape-out、工程样片、量产和云可用分开 |
| 内存 | Samsung LPDDR5X-PIM | [Samsung/lpddr5x-pim.md](./Samsung/lpddr5x-pim.md) | `[官方议程][本地已有][厂商资料已回填][待公开材料]` | 已确认 PIM 产品定位；容量/带宽/算子/量产状态仍待官方补充 |
| 内存 | XCENA MX1 CXL Computational Memory | [XCENA/mx1.md](./XCENA/mx1.md) | `[官方议程][本地已有][厂商资料已回填][待公开材料]` | 已补 CXL 3.2、PCIe 6、DDR5/RISC-V/vector/PoC 边界；继续追踪 production 版本 |
| 内存教程 | D-Matrix/Meta：3D DRAM based Accelerator for Generative Inference | [d-Matrix/pavehawk.md](./d-Matrix/pavehawk.md) | `[官方议程][本地已有][待公开材料]` | Pavehawk 保持实验室硅；公开材料后补页码与规格 |
| 互联 | Broadcom Thor Ultra | [Broadcom/thor-ultra.md](./Broadcom/thor-ultra.md) | `[官方议程][本地已有][厂商资料已回填][待公开材料]` | 已补 800G、PCIe Gen6 x16、UEC 数据路径与 sampling 状态 |
| 互联 | NVIDIA BlueField-4；Spectrum-X Multiplane | NVIDIA 厂商资料已有部分系统互联内容 | `[官方议程][本地已有][待公开材料]` | 与 GPU 芯片规格分层；待完整会议材料补互联专题 |
| 教程 | HBM、HBM base die、3D DRAM、先进封装、RISC-V | 当前资料分散在各厂商页 | `[官方议程][专题待补][待公开材料]` | 可建立跨厂商背景专题，但不把教程观点写成某个厂商产品事实 |

## 本轮已补齐的原“待补档”对象

截至 2026-09-13，上一版列为主要空档的对象已经完成首轮厂商/产品建档：

- Intel：[[Intel-overview]] → [[crescent-island]]
- Meta：[[Meta-overview]] → [[mtia-300]] / [[mtia-400]] / [[mtia-450]] / [[mtia-500]]
- Microsoft：[[Microsoft-overview]] → [[maia-200]]
- SambaNova：[[SambaNova-overview]] → [[sn50]]
- Broadcom：[[Broadcom-overview]] → [[thor-ultra]] / [[tomahawk-ultra]]
- Samsung：[[Samsung-overview]] → [[lpddr5x-pim]]
- XCENA：[[XCENA-overview]] → [[mx1]]

其中 Samsung 与 XCENA 分目录处理，是为了避免把 LPDDR PIM 与 CXL computational memory 混成一个“计算内存芯片”对象。

## 会议资料接入规则

1. 先保存官方议程、演讲标题、演讲者和公开日期；议程本身不添加规格推断。
2. 厂商另行公开的 Newsroom、产品页和架构文章可以先回填，但标明它们不是 Hot Chips 幻灯片页码级证据。
3. 演讲 PDF 或录像公开后，按“芯片、封装/模组、板卡、服务器、机架、网络、云服务、软件”拆分证据，并在每条会议新增数字旁保留页码或视频时间点。
4. 厂商峰值、相对性能和路线图分别标为厂商主张、演讲展示或路线图；只有可复现独立测试进入独立基准字段。
5. `announced`、`tape-out`、`sampling`、`mass production`、`shipment`、`customer deployment`、`cloud GA` 继续分开记录。

## 当前缺口

截至 2026-09-13，HC2026 议程中此前最明显的厂商空目录已经补齐。下一阶段重点从“有没有页面”转为“证据有多深”：

1. 等待官方 FAQ 所述的 2026 年 12 月初公众幻灯片/录像，逐页回填 Intel、NVIDIA、AMD、Cerebras、Meta、Microsoft、SambaNova、OpenAI、d-Matrix 等会议增量。
2. 为 HBM/HBM base die、先进封装、3D DRAM、RISC-V 与 AI Ethernet 建立跨厂商背景专题，但不改变厂家目录唯一总览规则。
3. HC2025 仍未建立同样的逐议程对照，可作为后续历史补全任务。
