# Hot Chips 2026 议程对照与本地资料补强

- 会议日期：2026-08-23 至 2026-08-25（美国太平洋时间）
- 本次核对日期：2026-09-05
- 官方议程：[HC2026 Program](https://hc2026.hotchips.org/program/)
- 资料边界：[官方 FAQ](https://hc2026.hotchips.org/faq/) 说明，演讲 PDF 在演讲当天向参会者提供，录像和幻灯片计划于 2026 年 12 月初向公众开放。

## 使用口径

本页只把官方公开议程当作“会议确实安排了这个主题”的证据。议题名称、演讲者和会议日期不等于芯片已经量产，也不等于演讲中的每个数字已经公开核验。

| 标签 | 含义 |
| --- | --- |
| `[官方议程]` | Hot Chips 2026 官方节目页直接列出的演讲、教程或海报 |
| `[本地已有]` | 当前仓库已有相关厂商或产品资料，可继续回填会议增量 |
| `[待补档]` | 议程对象与当前资料范围存在明确空缺，应新增一页或一个专题 |
| `[待公开材料]` | 议程已确认，但完整幻灯片/录像尚未对公众开放，不能把演讲内容写成已核验事实 |

## 与现有资料的对照

| 会议主题 | 议程对象 | 当前本地对应 | 覆盖判断 | 下一步 |
| --- | --- | --- | --- | --- |
| GPU | NVIDIA Rubin GPU | [NVIDIA/rubin-gpu.md](./NVIDIA/rubin-gpu.md)、[NVIDIA/rubin-cpx.md](./NVIDIA/rubin-cpx.md) | `[官方议程][本地已有]` | 对照 HC2026 幻灯片公开后，单独记录 Rubin 架构新增内容；不要把 Vera Rubin 系统值回填到单 GPU |
| GPU | AMD Instinct MI400 Series GPU Architecture；MI400 System Architecture | [AMD/mi455x.md](./AMD/mi455x.md)、[AMD/mi430x.md](./AMD/mi430x.md)、[AMD/mi500.md](./AMD/mi500.md) | `[官方议程][本地已有]` | 把 MI400 芯片、EAM、Helios 托盘和机架拆成四个层级，对照会议架构细节 |
| GPU | Intel Crescent Island | 当前无 Intel 目录 | `[官方议程][待补档]` | 新增独立厂商档案；先记录议程和公开状态，待材料开放后再写规格 |
| AI 系统 | Meta Custom AI Silicon | 当前无 Meta 目录 | `[官方议程][待补档]` | 新增 Meta 自研 AI Silicon 边界页，区分推荐系统 ASIC、GenAI 芯片和系统部署 |
| AI 系统 | Microsoft MAIA 200 Accelerator | 当前无 Microsoft 目录 | `[官方议程][待补档]` | 新增 Maia 200 芯片/系统边界页，不能把数据中心系统规格当成芯片规格 |
| AI 系统 | Cerebras Rack-Scale Architecture for Wafer Scale Engine | [Cerebras/wse-3.md](./Cerebras/wse-3.md)、[Cerebras/wse-3-turbo.md](./Cerebras/wse-3-turbo.md) | `[官方议程][本地已有]` | 新增或补充 rack-scale 专题；保持 WSE-3、WSE-3 Turbo、CS-4 三个层级分开 |
| AI 系统 | NVIDIA Think Fast: LPU Accelerator for Heterogeneous Compute | [NVIDIA/NVIDIA-overview.md](./NVIDIA/NVIDIA-overview.md) | `[官方议程][待公开材料]` | 先挂会议来源，待 PDF 公开后判断是否属于新芯片、系统加速器或架构概念 |
| AI 系统 | SambaNova SN50 RDU | 当前无 SambaNova 目录 | `[官方议程][待补档]` | 新增 RDU 独立档案，重点记录 dataflow、片上内存和系统级边界 |
| AI 系统 | Google Eighth Generation TPU Family | [Google/tpu8t.md](./Google/tpu8t.md)、[Google/tpu8i.md](./Google/tpu8i.md) | `[官方议程][本地已有]` | 保留 TPU 8t/8i 的 Coming soon 状态；会议演讲不能自动升级为 GA、量产或客户部署 |
| AI 系统 | OpenAI “You Can Just Build … Chips” | [openai/jalapeno.md](./openai/jalapeno.md)、[openai/openai-overview.md](./openai/openai-overview.md) | `[官方议程][本地已有]` | 新增会议证据入口；继续把 Jalapeño 的 tape-out、工程样片、量产和云可用分开 |
| 内存 | Samsung LPDDR5X-PIM；XCENA MX1 CXL Computational Memory | 当前无独立内存/计算内存目录 | `[官方议程][待补档]` | 新增“计算内存与 PIM”专题，区分内存器件、CXL 设备和 AI 加速芯片 |
| 内存教程 | D-Matrix/Meta：3D DRAM based Accelerator for Generative Inference | [d-Matrix/pavehawk.md](./d-Matrix/pavehawk.md) | `[官方议程][本地已有][待公开材料]` | 把 Pavehawk 标作实验室硅；完整演讲材料公开后再补页码和规格 |
| 互联 | Broadcom Thor Ultra；NVIDIA BlueField-4；Spectrum-X Multiplane | NVIDIA 资料有部分系统互联内容，Broadcom 无目录 | `[官方议程][待补档]` | 新增网络/互联边界专题，不能将 NIC、DPU、交换网络算作 GPU 芯片 |
| 教程 | HBM、HBM base die、3D DRAM、先进封装、RISC-V | 当前资料仅零散涉及 HBM/封装和 CPU | `[官方议程][待补档]` | 作为架构背景专题引用，不把教程观点写成厂商产品事实 |

## 会议资料接入规则

1. 先保存官方议程、演讲标题、演讲者和公开日期；这一步不添加规格推断。
2. 演讲 PDF 或录像公开后，按“芯片、封装/模组、板卡、服务器、机架、云服务、软件”拆分证据，并在每条数字旁保留演讲页码或视频时间点。
3. 每条会议事实增加 `来源类型=Hot Chips 2026 演讲`、`公开状态=公开/参会权限/待公开` 和 `最后核验日`。
4. 会议演讲中的厂商峰值、相对性能和路线图，仍分别标为厂商主张、演讲展示或路线图；只有可复现的独立测试才进入独立基准字段。
5. HC2026 的演讲标题不能替代产品状态。`announced`、`tape-out`、`sampling`、`mass production`、`shipment`、`customer deployment`、`cloud GA` 继续分开记录。

## 当前缺口

截至 2026-09-05，HC2026 已建立本页对照，但完整演讲材料仍待官方公开；HC2025 尚未建立同样的逐议程对照。当前优先补齐 Intel、Meta、Microsoft、SambaNova、Broadcom、Samsung/CXL 计算内存六类对象，再回填 NVIDIA、AMD、Cerebras、Google、OpenAI 和 d-Matrix 的会议增量。
