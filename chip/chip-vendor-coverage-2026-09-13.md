# AI 芯片与基础设施厂家覆盖汇总（2026-09-13）

[项目总入口](./00-project-index.md) · [上一轮覆盖记录](./chip-vendor-coverage-2026-09-02.md) · [Hot Chips 2026 对照](./hot-chips-2026.md)

- 本轮研究截止日：2026-09-13
- 本轮重点：补齐上一轮 Hot Chips 2026 明确指出的 Intel、Meta、Microsoft、SambaNova、Broadcom、Samsung PIM、XCENA/CXL computational memory 空档。
- 证据规则：芯片、板卡/模组、服务器、机架、集群、网络和云服务分层；announcement、sample、production、shipment、deployment、cloud GA 分开；未核验项保持“公开资料未确认”。
- 旧有厂商：除本轮新增/补档对象外，规格状态沿用 2026-09-05 已有厂商页证据，本轮不假装重新逐项验证。

## 厂商目录

| 厂商目录 | 唯一总描述文档 | 本轮状态 |
| --- | --- | --- |
| AMD | [AMD-overview](./AMD/AMD-overview.md) | 沿用既有证据，待继续补 MI400/MI500 会议增量 |
| AWS | [AWS-overview](./AWS/AWS-overview.md) | 沿用既有证据 |
| Biren | [壁仞科技-概览](./Biren/壁仞科技-概览.md) | 沿用既有证据 |
| Broadcom | [Broadcom-overview](./Broadcom/Broadcom-overview.md) | **本轮新增**：Thor Ultra / Tomahawk Ultra |
| Cambricon | [寒武纪-概览](./Cambricon/寒武纪-概览.md) | 沿用既有证据 |
| Cerebras | [Cerebras-overview](./Cerebras/Cerebras-overview.md) | 沿用既有证据，待 HC2026 rack-scale 材料公开 |
| d-Matrix | [d-Matrix-overview](./d-Matrix/d-Matrix-overview.md) | 沿用既有证据，Pavehawk 保持实验室硅边界 |
| Enflame | [燧原科技-概览](./Enflame/燧原科技-概览.md) | 沿用既有证据 |
| FuriosaAI | [FuriosaAI-overview](./FuriosaAI/FuriosaAI-overview.md) | 沿用既有证据 |
| Google | [Google-overview](./Google/Google-overview.md) | 沿用既有证据，TPU8 保持 Coming soon/未 GA 边界 |
| Groq | [Groq-overview](./Groq/Groq-overview.md) | 沿用既有证据 |
| Huawei | [华为-概览](./Huawei/华为-概览.md) | 沿用既有证据 |
| Hygon | [海光信息-概览](./Hygon/海光信息-概览.md) | 沿用既有证据 |
| Iluvatar | [天数智芯-概览](./Iluvatar/天数智芯-概览.md) | 沿用既有证据 |
| Intel | [Intel-overview](./Intel/Intel-overview.md) | **本轮新增**：Crescent Island |
| Kunlunxin | [昆仑芯-概览](./Kunlunxin/昆仑芯-概览.md) | 沿用既有证据 |
| Meta | [Meta-overview](./Meta/Meta-overview.md) | **本轮新增**：MTIA 300/400/450/500 |
| MetaX | [沐曦-概览](./MetaX/沐曦-概览.md) | 沿用既有证据 |
| Microsoft | [Microsoft-overview](./Microsoft/Microsoft-overview.md) | **本轮新增**：Maia 200 |
| MooreThreads | [摩尔线程-概览](./MooreThreads/摩尔线程-概览.md) | 沿用既有证据 |
| NVIDIA | [NVIDIA-overview](./NVIDIA/NVIDIA-overview.md) | 沿用既有证据，待 HC2026 Rubin/LPU 材料公开 |
| Samsung | [Samsung-overview](./Samsung/Samsung-overview.md) | **本轮新增**：LPDDR5X-PIM |
| SambaNova | [SambaNova-overview](./SambaNova/SambaNova-overview.md) | **本轮新增**：SN50 RDU |
| Sunrise | [曦望-概览](./Sunrise/曦望-概览.md) | 沿用既有证据 |
| Tenstorrent | [Tenstorrent-overview](./Tenstorrent/Tenstorrent-overview.md) | 沿用既有证据 |
| XCENA | [XCENA-overview](./XCENA/XCENA-overview.md) | **本轮新增**：MX1 CXL Computational Memory |
| Xiaomi | [小米-概览](./Xiaomi/小米-概览.md) | 沿用既有证据 |
| openai | [openai-overview](./openai/openai-overview.md) | 沿用既有证据，Jalapeño 生命周期继续分层 |

## 本轮新增对象速览

| 厂商/产品 | 对象层级 | 核心公开信息 | 生命周期（截至 2026-09-13） | 资料页 |
| --- | --- | --- | --- | --- |
| Intel Crescent Island | 数据中心推理 GPU / PCIe 卡 | Xe3P；32 Xe Core；256 XMX；最高 480GB LPDDR5X；350W | 规格已公开；量产/出货未确认 | [Crescent Island](./Intel/crescent-island.md) |
| Microsoft Maia 200 | 推理加速器 SoC | TSMC 3nm；>140B transistor；216GB HBM3e / 7TB/s；272MB SRAM；>10 PF4 / >5 PF8；750W | 已在 Iowa/Arizona production 数据中心 live | [Maia 200](./Microsoft/maia-200.md) |
| Meta MTIA 300 | 自研加速器 | 1 compute chiplet + 2 network chiplets；RISC-V PE；HBM | R&R training 已在 production | [MTIA 300](./Meta/mtia-300.md) |
| Meta MTIA 400 | 自研加速器 | 2 compute chiplets；FP8 +400%、HBM BW +51% vs 300；72-device scale-up 系统 | lab testing 完成，走向数据中心部署 | [MTIA 400](./Meta/mtia-400.md) |
| Meta MTIA 450 | GenAI inference 加速器 | HBM BW 2× vs 400；MX4 +75%；attention/FFN 加速 | 计划 2027 年初 mass deployment | [MTIA 450](./Meta/mtia-450.md) |
| Meta MTIA 500 | GenAI inference 加速器 | HBM BW +50%、capacity up to +80%、MX4 +43% vs 450；2×2 compute chiplets | 计划 2027 年 mass deployment | [MTIA 500](./Meta/mtia-500.md) |
| SambaNova SN50 | 第五代 RDU | TSMC 5nm；1600 TFLOPS BF16；3200 TFLOPS FP8；432MB SRAM；64GB HBM2E；≤512GB DDR5 | 已发布；2026H2 出货为厂商计划，广泛出货待确认 | [SN50](./SambaNova/sn50.md) |
| Broadcom Thor Ultra | 800G AI Ethernet NIC | PCIe Gen6 x16；UEC/RDMA multipath/OOO/selective retransmission | 2025-10 sampling；量产未确认 | [Thor Ultra](./Broadcom/thor-ultra.md) |
| Broadcom Tomahawk Ultra | AI scale-up switch ASIC | 51.2Tb/s；250ns 厂商口径；in-network collectives | 2025-07 官方确认 shipping | [Tomahawk Ultra](./Broadcom/tomahawk-ultra.md) |
| Samsung LPDDR5X-PIM | PIM memory | LPDDR5X + processing-in-memory；减少数据搬运/改善能效 | FMS 2026 已展示；sampling/量产未确认 | [LPDDR5X-PIM](./Samsung/lpddr5x-pim.md) |
| XCENA MX1 | CXL computational memory | CXL 3.2 Type-3；PCIe 6.0；DDR5 RDIMM；数千 1.4GHz RISC-V；FP32/FP16 vector | working samples/PoC；production-ready 计划与实际量产分开 | [MX1](./XCENA/mx1.md) |

> 注：上表中的相对代际百分比、厂商峰值 FLOPS/OPS、网络规模和 TDP 分别保留原始口径；不进行跨精度、跨对象层级的直接排名。

## 本轮修正的关键边界

1. **Intel 制程不能串台**：Crescent Island 的 Hot Chips 2026 同篇材料包含 Intel 18A 的 Wildcat Lake，但官方没有把 18A 明确写给 Crescent Island，因此 Crescent Island 制程仍为“公开资料未确认”。
2. **Maia 200 的 6,144 是系统规模**：2.8TB/s 双向 on-die NIC 是芯片 I/O；最多 6,144 accelerators 是两级 Ethernet scale-up 域，不是单芯片资源。
3. **Meta 相对提升不能变成绝对榜单**：MTIA 300→500 的 25× compute 比较跨 MX8/MX4 精度；450/500 仍是 2027 部署计划。
4. **SambaNova 三层内存不能合并**：432MB SRAM、64GB HBM2E、最高 512GB DDR5 属于不同层级；SambaRack/256-RDU 是系统层。
5. **Broadcom 是网络芯片边界**：Thor Ultra/Tomahawk Ultra 应进入互联维度，不与 GPU/NPU 的 FP8/HBM 做同类算力比较。
6. **PIM/CXL memory 不是 GPU**：Samsung LPDDR5X-PIM 与 XCENA MX1 是数据搬运/近数据计算路线，其生命周期和编程模型必须独立追踪。

## 仍需优先补强

- **已存在但“部分完成”的厂商**：AMD、AWS、Cambricon、Cerebras、Groq、Huawei、NVIDIA、Sunrise、OpenAI，继续优先补单芯片功耗、内存/互联、量产/出货/部署与软件版本证据。
- **Hot Chips 2026 完整演讲材料**：官方 FAQ 计划 2026 年 12 月初公开录像/幻灯片；届时回填页码、架构图和新增规格，不提前用议程标题代替演讲事实。
- **Intel 历史 AI 路线**：本轮只补 Crescent Island，Gaudi 2/3、Falcon Shores 等历史/转向背景尚未系统回填。
- **Microsoft 历史路线**：Maia 100 与 Maia 200 的代际对照可继续补。
- **Meta 早期代际**：MTIA 100/200 有生产部署与论文材料，但本轮未独立拆页。
- **AI 网络专题**：Broadcom、NVIDIA Spectrum-X/BlueField、UALink、UEC、Ethernet scale-up/scale-out 可再建立跨厂商对照，但不要改变厂家目录的唯一总览规则。

## 本轮新增一手来源

- Intel Hot Chips 2026 Newsroom：<https://www.intel.com/content/www/us/en/newsroom/news/client-computing/intel-outlines-architectures-for-agentic-ai-at-hot-chips-2026.html>
- Microsoft Maia 200：<https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/>
- Microsoft Maia 200 architecture：<https://techcommunity.microsoft.com/blog/azureinfrastructureblog/deep-dive-into-the-maia-200-architecture/4489312>
- Meta MTIA 300/400/450/500：<https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/>
- SambaNova SN50：<https://sambanova.ai/products/rdu-ai-chips>
- Broadcom Thor Ultra：<https://investors.broadcom.com/news-releases/news-release-details/broadcom-introduces-industrys-first-800g-ai-ethernet-nic>
- Broadcom Tomahawk Ultra：<https://www.broadcom.com/company/news/product-releases/63341>
- Samsung FMS 2026 LPDDR5X-PIM：<https://news.samsung.com/global/samsung-unveils-next-gen-3d-memory-vision-at-fms-2026-charting-the-future-of-ai-infrastructure>
- XCENA MX1：<https://xcena.com/computational_memory>
