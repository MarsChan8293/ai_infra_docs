# Iluvatar CoreX / 天数智芯 — 天数智芯板卡、服务器、集群与云（边界文件，非芯片）

- 拆分日期：2026-09-02
- 产品层级：板卡/模组/服务器/集群/云（非芯片）
- 综合报告：[iluvatar-chips-2026-09-01.md](./iluvatar-chips-2026-09-01.md)
- 文件性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容逐行摘录综合报告，保留原报告中的状态、数字、证据等级和未知项。

> 第 1 行：# 天数智芯（Iluvatar CoreX）公开 AI 芯片与算力产品研究
> 第 2 行：
> 第 4 行：> 访问日：2026-09-01  
> 第 5 行：> 范围：天数智芯公开的通用 GPU、AI 加速卡、边端 GPGPU 模组/终端、服务器/集群方案、云端可用性与软件栈。  
> 第 6 行：> 证据口径：优先采用天数智芯官网、天数智芯开发者门户、天数智芯官方公众号原文链接、香港联交所上市文件。官网产品页的动态字段可能随时间变化，本文记录访问日可见内容。
> 第 15 行：| 智铠（ZK） | 云端推理通用 GPU | 智铠 100 | 芯片 + MR-V50/MR-V100 PCIe 加速卡 |
> 第 16 行：| 彤央（TY） | 边端/终端 GPGPU | TY1000、TY1100、TY1100-NX、TY1100-NX-PRO、TY1200 | 模组或算力终端/整机形态，不应与数据中心 GPU 卡混为一谈 |
> 第 17 行：
> 第 18 行：官方上市文件将公司的产品和解决方案进一步拆为“通用 GPU 芯片及加速卡”与“定制 AI 算力解决方案”，后者包括通用 GPU 服务器和通用 GPU 集群。服务器/集群是系统交付层，不是新的芯片型号。[香港联交所招股章程（2025-12-30）](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1230/2025123000020_c.pdf)
> 第 19 行：
> 第 24 行：- 天垓 300 于 2026-07-19 由官方开发者门户列为正式发布的新一代旗舰；官方披露“具备规模化应用条件”，但本次已核验材料未确认流片、量产、批量出货、客户部署或云端可用的独立日期。
> 第 25 行：- 智铠 100 是面向推理的通用 GPU 产品，MR-V50/MR-V100 是其公开的加速卡型号；官方披露其在 2024-12 已上线无问芯穹 Infini-AI 异构云平台，可支持 7B–72B 参数模型推理。
> 第 26 行：- 彤央四款产品在官方 2026-01-26 发布活动中整体公布；官网当前还列出 TY1100-NX-PRO。它们是边端模组/终端，官网给出了不同的封装、内存、CPU 和尺寸，但本次材料没有逐型号给出流片、量产、出货日期。
> 第 52 行：|---|---|---|---|
> 第 53 行：| 智铠 100 芯片 | 芯片 | 官网未给出裸芯片面积、制程、晶体管数或完整算力表 | 官网产品体系可确认；流片/量产日期未在本次页面中单独确认 |
> 第 54 行：| 智铠 50（MR-V50） | PCIe 推理加速卡 | 通用 GPU；16 GB HBM2e；板级功耗 75 W；半长半高单槽 PCIe；被动散热；PCIe Gen4 x16；支持 H.264/H.265/VP9/AVS2 | 官网在访问日公开列出；单独发布、量产和出货日期未确认 |
> 第 55 行：| 智铠 100（MR-V100） | PCIe 推理加速卡 | 通用 GPU；32 GB HBM2e；板级功耗 150 W；全长全高单槽 PCIe；被动散热；PCIe Gen4 x16；最大 128 路 H.264 1080p@30fps 视频解码；JPEG HD 解码/编码 2000/500 帧 | 官网在访问日公开列出；已形成百卡推理集群并于 2024-12 上线 Infini-AI 平台 |
> 第 56 行：
> 第 60 行：
> 第 61 行：彤央不是一组数据中心 PCIe 卡，而是边端算力模组或终端。官方 2026-01-26 发布活动称发布四款彤央产品，并将全系列标称算力描述为实测稠密算力、覆盖 100T–300T；该“优于 AGX Orin”等比较属于官方测试/厂商主张，未见独立测试数据。[天数智芯官方发布：四代架构路线图与彤央系列](https://www.iluvatar.com/newsDetails?code=tszxzpgbxpsdjglxttybdxlxncygjzls&topicId=495)
> 第 62 行：
> 第 64 行：|---|---|---|---|
> 第 65 行：| 彤央 TY1000 | 算力模组 | 699 pin；100 × 87 × 15.29 mm；32 GB HBM2e；16 GB LPDDR4；天数自研 GPGPU；8-Core ARM | 官方 2026-01-26 发布活动列为四款彤央产品之一；正式流片、量产、出货日期未确认 |
> 第 66 行：| 彤央 TY1100 | 算力模组 | 699 pin；100 × 87 × 45 mm；16/32 GB HBM2e；16 GB LPDDR5x；天数自研 GPGPU；12-Core ARM | 面向具身智能、工业能源、物流仓储、智慧超市/门店、车路协同；生命周期日期未确认 |
> 第 67 行：| 彤央 TY1100-NX | 算力终端 | 130 × 130 × 63 mm；32/64 GB LPDDR5x；16 GB LPDDR5x；天数自研 GPGPU；12-Core ARM | 官网列为当前产品；面向教学、工业、物流、门店、具身智能、视频分析、AI Agent、天气预警；生命周期日期未确认 |
> 第 68 行：| 彤央 TY1100-NX-PRO | 算力终端 | 130 × 130 × 63 mm；32 GB HBM2e；16 GB LPDDR5x；天数自研 GPGPU；12-Core ARM | 官网列为当前产品；官方 2026-01-26 新闻正文摘要重点描述四款产品，未单独给出 PRO 的发布/量产日期 |
> 第 69 行：| 彤央 TY1200 | 算力终端 | 150 × 150 × 56 mm；32 GB HBM2e；16 GB LPDDR5x；天数自研 GPGPU；16-Core x86；512 GB SSD，最高支持 2 TB NVMe | 官网称支持最高 35B 模型、可完全离线运行；官方发布活动称 300 TOPS；正式流片、量产、出货日期未确认 |
> 第 70 行：
> 第 72 行：
> 第 73 行：## 2. 芯片、板卡、模组、服务器、机架与云服务的区分
> 第 74 行：
> 第 80 行：| 终端 | TY1100-NX、TY1100-NX-PRO、TY1200 | 这是边端整机/终端形态，附带 CPU、存储和离线运行能力 |
> 第 81 行：| 服务器 | 官方认证服务器目录中的第三方服务器，如 H3C R4900 G6/R5300G5、安擎 EG520-G30/EG820G-G20、宝德 PR210KI 等，目录展示 BI-V100 的 2U/4U、2/4/8/10 卡配置 | 认证服务器不是天数自有芯片型号，也不等同于统一机架产品 |
> 第 82 行：| 集群/机架 | 官方上市文件称提供通用 GPU 服务器和可扩展通用 GPU 集群；官方新闻提到智铠百卡推理集群、千卡异构混合训练平台 | 本次材料没有确认天数自有标准机架 SKU、机架级功耗、交换机型号或完整拓扑 |
> 第 83 行：| 云服务 | 智铠 100 于 2024-12 已在无问芯穹 Infini-AI 平台上线，支持 7B–72B 参数模型推理；这是合作方异构云/MaaS 平台上的可用性 | 不能表述为天数自营公有云，也不能把合作平台上线等同于所有型号均可云端租用 |
> 第 84 行：
> 第 85 行：服务器认证目录：[天数智芯认证服务器目录](https://www.iluvatar.com/cooperation/direct)。该目录在访问日明确给出第三方服务器型号、服务器形态、每节点最大 GPU 数和天数产品型号，属于硬件兼容认证信息。
> 第 86 行：
> 第 87 行：云端/集群证据：[智铠 GPU 百卡推理集群与 Infini-AI 上线](https://www.iluvatar.com/newsDetails?code=tszxlhwwxqwczkGPUbktljqcsykpzcdc&topicId=495)。官方文章称 2024-07 已合作构建单任务千卡规模异构混合训练平台，2024-12 完成智铠 100 接入并对外提供 MaaS；文章属于厂商与合作方联合发布，平台性能数字应按厂商/合作方口径理解。
> 第 88 行：
> 第 95 行：| 天垓 300 | 2026-07-19 官方开发者门户/公众号 | 2026-07-19 | 未确认 | 未确认 | 官方称具备规模化应用条件，未等同于已量产 | 未确认 | 未确认 | 2026 新架构产品 | 未发现官方 EOL |
> 第 96 行：| 智铠 100 / MR-V50/MR-V100 | 官方 2022–2023 新闻已展示/应用 | 精确正式发布日未在本次一手材料中确认 | 未确认 | 未确认 | 上市文件称 ZK Gen 1 为首个面向推理的国产 GPGPU 产品并已量产；未按 MR-V50/MR-V100 拆分 | 2024-12 前已形成百卡推理集群；客户部署总量未按卡型拆分 | 2024-12 Infini-AI 上线，支持 7B–72B 推理 | 属已发布代际 | 未发现官方 EOL |
> 第 97 行：| 彤央系列 | 2026-01-26 官方合作伙伴大会 | 2026-01-26 整体发布四款；官网另列 NX-PRO | 未确认 | 未确认 | 未确认 | 官方称已落地格蓝若、瑞幸门店、车路云试点等案例，属于厂商发布的落地陈述 | 未确认 | 边端产品线 | 未发现官方 EOL |
> 第 124 行：| KV | 未公开 KV Cache 容量管理、分页策略、压缩/量化格式、KV 带宽或 KV/Attention 片上路径 | 公开资料未确认 |
> 第 125 行：| 跨卡通信 | 天垓 100 页面公布 64 GB/s 片间互联带宽；官网未公开完整链路协议、交换结构、collective 实现和集群拓扑 | 只有带宽数字已确认，完整通信架构未确认 |
> 第 126 行：
> 第 134 行：- 官方 2023 新闻称基于天垓 100 与智铠 100 的方案已支持国内研究机构 650 亿参数大模型训练以及千亿级参数大模型推理；这是厂商应用案例表述，未给出独立测试报告。[2023 世界计算大会官方新闻](https://www.iluvatar.com/newsDetails?code=tszxzztyGPUsljjfasldc2023sjjsdh&topicId=495)
> 第 135 行：- 官方 2024-12 新闻称 2024-07 已与无问芯穹合作构建单任务千卡规模异构芯片混合训练平台，最高算力利用率 97.6%；该数值是合作双方发布的厂商/平台口径。
> 第 136 行：
> 第 139 行：- 智铠系列定位为推理产品，MR-V50/MR-V100 公开支持 FP32、FP16、INT8 和视频编解码。
> 第 140 行：- 官方 2024-12 新闻称智铠 100 已在 Infini-AI 上线，可支持 7B–72B 参数模型推理；已收录 Stable Diffusion、Qwen2.5、CogVideoX、Llama 3.1 等模型。该事实是平台上线范围，不是所有模型在所有批量/上下文下的性能保证。[官方合作新闻](https://www.iluvatar.com/newsDetails?code=tszxlhwwxqwczkGPUbktljqcsykpzcdc&topicId=495)
> 第 141 行：- 彤央 TY1200 官网称最高支持 35B 模型、完全离线运行；这是终端产品页的厂商能力描述，未公开具体量化格式、上下文长度和 tokens/s。
> 第 144 行：
> 第 145 行：官方 2026-01-26 发布活动披露的路线图为：2025 年天枢、2026 年天璇、2026 年天玑、2027 年天权，2027 年之后转向突破性计算芯片架构设计；官方目标口径包括 2025 年超越 Hopper、2026 年对标/超越 Blackwell、2027 年超越 Rubin。[天数智芯官方路线图新闻](https://www.iluvatar.com/newsDetails?code=tszxzpgbxpsdjglxttybdxlxncygjzls&topicId=495)
> 第 146 行：
> 第 148 行：|---|---|---|
> 第 149 行：| 天枢、天璇、天玑、天权名称及年份 | 官方路线图 | 已公开路线图，不等于每一代芯片已经发布或量产 |
> 第 150 行：| “超越 Hopper/Blackwell/Rubin” | 厂商目标/比较主张 | 不能写成独立验证的性能事实 |
> 第 165 行：
> 第 166 行：1. 天垓 150、天垓 300 的裸芯片料号、制程、晶体管数、die 面积、完整算力、显存带宽、板卡功耗和板卡型号。
> 第 167 行：2. 天垓 300 的流片、送样、量产、批量出货、首个客户部署和云端租用日期。
> 第 168 行：3. 天垓 150 的正式发布日期、量产批次和具体客户/云平台。
> 第 169 行：4. 智铠 100 芯片的制程、面积、完整算力、显存带宽和芯片级功耗；MR-V50/MR-V100 的流片/量产时间。
> 第 170 行：5. 彤央各型号内部 GPGPU 的芯片料号、制程、频率、算力精度、带宽、功耗和封装来源。
> 第 171 行：6. Search、Reduce、Top-k、Address、Route、Gather、KV Cache 的专用硬件/指令/软件实现。
> 第 172 行：7. 跨卡协议、拓扑、交换芯片、collective 通信实现以及按型号的集群规模和 MFU。
> 第 173 行：8. 任一型号的停产、EOL、最后订货日或软件支持终止日期。
> 第 187 行：| 天数智算软件栈 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/software?fullCode=cpjs-rj-rjz | 编译器、驱动、库、框架与 Linux 生态 |
> 第 188 行：| 认证服务器目录 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/cooperation/direct | 服务器层与 BI-V100 兼容配置 |
> 第 189 行：| 天数智芯重磅公布芯片四代架构路线图…… | 2026-01-25 | 2026-09-01 | https://www.iluvatar.com/newsDetails?code=tszxzpgbxpsdjglxttybdxlxncygjzls&topicId=495 | 路线图、彤央发布、架构主张与落地案例 |
> 第 190 行：| 天数智芯联合无问芯穹完成智铠 GPU 百卡推理集群测试与适配…… | 2024-12-08 | 2026-09-01 | https://www.iluvatar.com/newsDetails?code=tszxlhwwxqwczkGPUbktljqcsykpzcdc&topicId=495 | 百卡推理、千卡混训、Infini-AI 上线 |
> 第 191 行：| 天数智芯自主通用 GPU 算力解决方案闪亮登场 2023 世界计算大会 | 2023-09-16 | 2026-09-01 | https://www.iluvatar.com/newsDetails?code=tszxzztyGPUsljjfasldc2023sjjsdh&topicId=495 | 天垓 100/智铠 100 应用与量产表述 |
> 第 192 行：| 天垓 300 正式发布——让 AI 触手可及 | 2026-07-19 | 2026-09-01 | https://developer.iluvatar.com/news/300-ai | 新旗舰正式发布记录 |
> 第 193 行：| 天垓 300 官方公众号原文 | 2026-07-19 | 2026-09-01 | https://mp.weixin.qq.com/s/TMxa68E2WCjfh_prfhOszg | 官方发布原文入口 |
> 第 194 行：| Shanghai Iluvatar CoreX Semiconductor Co., Ltd. 招股章程 | 2025-12-30 | 2026-09-01 | https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1230/2025123000020_c.pdf | 三代产品、量产、交付、客户与服务器/集群层定义 |
> 第 195 行：| 2025 Annual Report | 2026-04-27 | 2026-09-01 | https://www.hkexnews.hk/listedco/listconews/sehk/2026/0427/2026042701285_c.pdf | 上市后公司披露入口；本报告未用其补齐未确认的逐型号规格 |

## 直接来源链接

1. <https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1230/2025123000020_c.pdf)>
2. <https://www.iluvatar.com/newsDetails?code=tszxzpgbxpsdjglxttybdxlxncygjzls&topicId=495)>
3. <https://www.iluvatar.com/cooperation/direct)。该目录在访问日明确给出第三方服务器型号、服务器形态、每节点最大>
4. <https://www.iluvatar.com/newsDetails?code=tszxlhwwxqwczkGPUbktljqcsykpzcdc&topicId=495)。官方文章称>
5. <https://www.iluvatar.com/newsDetails?code=tszxzztyGPUsljjfasldc2023sjjsdh&topicId=495)>
6. <https://www.iluvatar.com/newsDetails?code=tszxlhwwxqwczkGPUbktljqcsykpzcdc&topicId=495)>
7. <https://www.iluvatar.com/software?fullCode=cpjs-rj-rjz>
8. <https://www.iluvatar.com/cooperation/direct>
9. <https://www.iluvatar.com/newsDetails?code=tszxzpgbxpsdjglxttybdxlxncygjzls&topicId=495>
10. <https://www.iluvatar.com/newsDetails?code=tszxlhwwxqwczkGPUbktljqcsykpzcdc&topicId=495>
11. <https://www.iluvatar.com/newsDetails?code=tszxzztyGPUsljjfasldc2023sjjsdh&topicId=495>
12. <https://developer.iluvatar.com/news/300-ai>
13. <https://mp.weixin.qq.com/s/TMxa68E2WCjfh_prfhOszg>
14. <https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1230/2025123000020_c.pdf>
15. <https://www.hkexnews.hk/listedco/listconews/sehk/2026/0427/2026042701285_c.pdf>

## 证据边界

- 这是资料重排页，不是重新发布或重新核验的产品公告。
- “发布、流片、送样、量产、出货、客户部署、云端可用、路线图、停产”等状态只在综合报告明确写出时保留；缺失项仍为“公开资料未确认”。
- 若摘录同时出现芯片、板卡、服务器、机架或云服务，均按原报告层级保留，并以“产品层级”字段提醒，不做跨层级推导。

## 关联表格原文（完整表格）

以下表格块来自综合报告中与本拆分项命中的表格，完整保留表头、状态列和规格列。

> 来源综合报告第 12-16 行：
> 第 12 行：| 产品线 | 主要定位 | 访问日官网列出的产品 | 产品层级判断 |
> 第 13 行：|---|---|---|---|
> 第 14 行：| 天垓（TG） | 云端/数据中心训练通用 GPU | 天垓 300、天垓 150、天垓 100 | 芯片 + PCIe 加速卡；官网当前页对 300/150 的详细参数不完整 |
> 第 15 行：| 智铠（ZK） | 云端推理通用 GPU | 智铠 100 | 芯片 + MR-V50/MR-V100 PCIe 加速卡 |
> 第 16 行：| 彤央（TY） | 边端/终端 GPGPU | TY1000、TY1100、TY1100-NX、TY1100-NX-PRO、TY1200 | 模组或算力终端/整机形态，不应与数据中心 GPU 卡混为一谈 |

> 来源综合报告第 51-55 行：
> 第 51 行：| 产品 | 层级 | 已核验规格 | 状态与边界 |
> 第 52 行：|---|---|---|---|
> 第 53 行：| 智铠 100 芯片 | 芯片 | 官网未给出裸芯片面积、制程、晶体管数或完整算力表 | 官网产品体系可确认；流片/量产日期未在本次页面中单独确认 |
> 第 54 行：| 智铠 50（MR-V50） | PCIe 推理加速卡 | 通用 GPU；16 GB HBM2e；板级功耗 75 W；半长半高单槽 PCIe；被动散热；PCIe Gen4 x16；支持 H.264/H.265/VP9/AVS2 | 官网在访问日公开列出；单独发布、量产和出货日期未确认 |
> 第 55 行：| 智铠 100（MR-V100） | PCIe 推理加速卡 | 通用 GPU；32 GB HBM2e；板级功耗 150 W；全长全高单槽 PCIe；被动散热；PCIe Gen4 x16；最大 128 路 H.264 1080p@30fps 视频解码；JPEG HD 解码/编码 2000/500 帧 | 官网在访问日公开列出；已形成百卡推理集群并于 2024-12 上线 Infini-AI 平台 |

> 来源综合报告第 63-69 行：
> 第 63 行：| 型号 | 官方产品层级 | 官网规格（访问日） | 公开场景/状态 |
> 第 64 行：|---|---|---|---|
> 第 65 行：| 彤央 TY1000 | 算力模组 | 699 pin；100 × 87 × 15.29 mm；32 GB HBM2e；16 GB LPDDR4；天数自研 GPGPU；8-Core ARM | 官方 2026-01-26 发布活动列为四款彤央产品之一；正式流片、量产、出货日期未确认 |
> 第 66 行：| 彤央 TY1100 | 算力模组 | 699 pin；100 × 87 × 45 mm；16/32 GB HBM2e；16 GB LPDDR5x；天数自研 GPGPU；12-Core ARM | 面向具身智能、工业能源、物流仓储、智慧超市/门店、车路协同；生命周期日期未确认 |
> 第 67 行：| 彤央 TY1100-NX | 算力终端 | 130 × 130 × 63 mm；32/64 GB LPDDR5x；16 GB LPDDR5x；天数自研 GPGPU；12-Core ARM | 官网列为当前产品；面向教学、工业、物流、门店、具身智能、视频分析、AI Agent、天气预警；生命周期日期未确认 |
> 第 68 行：| 彤央 TY1100-NX-PRO | 算力终端 | 130 × 130 × 63 mm；32 GB HBM2e；16 GB LPDDR5x；天数自研 GPGPU；12-Core ARM | 官网列为当前产品；官方 2026-01-26 新闻正文摘要重点描述四款产品，未单独给出 PRO 的发布/量产日期 |
> 第 69 行：| 彤央 TY1200 | 算力终端 | 150 × 150 × 56 mm；32 GB HBM2e；16 GB LPDDR5x；天数自研 GPGPU；16-Core x86；512 GB SSD，最高支持 2 TB NVMe | 官网称支持最高 35B 模型、可完全离线运行；官方发布活动称 300 TOPS；正式流片、量产、出货日期未确认 |

> 来源综合报告第 75-83 行：
> 第 75 行：| 层级 | 已确认的天数产品/方案 | 不应作出的推断 |
> 第 76 行：|---|---|---|
> 第 77 行：| 芯片 | 天垓 100、天垓 150、天垓 300、智铠 100，以及彤央内部的自研 GPGPU 模块 | “产品名”不等于已经公开了裸芯片完整规格；彤央页面没有给出独立芯片料号 |
> 第 78 行：| 板卡 | BI-V100（天垓 100）；MR-V50、MR-V100（智铠） | 板卡容量/功耗不能直接当作裸芯片 TDP |
> 第 79 行：| 模组 | TY1000、TY1100 | 699 pin、LPDDR/HBM 等是模组产品页规格，不能与 PCIe 卡规格横向直接比较 |
> 第 80 行：| 终端 | TY1100-NX、TY1100-NX-PRO、TY1200 | 这是边端整机/终端形态，附带 CPU、存储和离线运行能力 |
> 第 81 行：| 服务器 | 官方认证服务器目录中的第三方服务器，如 H3C R4900 G6/R5300G5、安擎 EG520-G30/EG820G-G20、宝德 PR210KI 等，目录展示 BI-V100 的 2U/4U、2/4/8/10 卡配置 | 认证服务器不是天数自有芯片型号，也不等同于统一机架产品 |
> 第 82 行：| 集群/机架 | 官方上市文件称提供通用 GPU 服务器和可扩展通用 GPU 集群；官方新闻提到智铠百卡推理集群、千卡异构混合训练平台 | 本次材料没有确认天数自有标准机架 SKU、机架级功耗、交换机型号或完整拓扑 |
> 第 83 行：| 云服务 | 智铠 100 于 2024-12 已在无问芯穹 Infini-AI 平台上线，支持 7B–72B 参数模型推理；这是合作方异构云/MaaS 平台上的可用性 | 不能表述为天数自营公有云，也不能把合作平台上线等同于所有型号均可云端租用 |

> 来源综合报告第 91-97 行：
> 第 91 行：| 产品/家族 | 首次披露/研发线索 | 正式发布 | 流片/点亮 | 送样 | 量产 | 出货/部署 | 云端可用 | 路线图 | 停产 |
> 第 92 行：|---|---|---|---|---|---|---|---|---|---|
> 第 93 行：| 天垓 100 | 官网历史介绍称 2021-03 正式发布训练产品 | 2021-03 | 本次已核验材料未取得可引用的官方流片日期 | 未确认 | 上市文件称 TG Gen 1 为首个量产国产 GPGPU；官方 2023 新闻亦称率先量产 | 上市文件披露公司整体 2022–2025H1 出货增长；截至 2025-06-30 超过 52,000 片交付，未按型号拆分 | 具体云租用日未确认 | 属已发布代际 | 未发现官方 EOL |
> 第 94 行：| 天垓 150 | 至少在上市前/当前官网列出 | 未确认精确日期 | 未确认 | 未确认 | 未确认 | 未确认具体型号出货 | 未确认 | 属当前天垓训练线 | 未发现官方 EOL |
> 第 95 行：| 天垓 300 | 2026-07-19 官方开发者门户/公众号 | 2026-07-19 | 未确认 | 未确认 | 官方称具备规模化应用条件，未等同于已量产 | 未确认 | 未确认 | 2026 新架构产品 | 未发现官方 EOL |
> 第 96 行：| 智铠 100 / MR-V50/MR-V100 | 官方 2022–2023 新闻已展示/应用 | 精确正式发布日未在本次一手材料中确认 | 未确认 | 未确认 | 上市文件称 ZK Gen 1 为首个面向推理的国产 GPGPU 产品并已量产；未按 MR-V50/MR-V100 拆分 | 2024-12 前已形成百卡推理集群；客户部署总量未按卡型拆分 | 2024-12 Infini-AI 上线，支持 7B–72B 推理 | 属已发布代际 | 未发现官方 EOL |
> 第 97 行：| 彤央系列 | 2026-01-26 官方合作伙伴大会 | 2026-01-26 整体发布四款；官网另列 NX-PRO | 未确认 | 未确认 | 未确认 | 官方称已落地格蓝若、瑞幸门店、车路云试点等案例，属于厂商发布的落地陈述 | 未确认 | 边端产品线 | 未发现官方 EOL |

> 来源综合报告第 116-125 行：
> 第 116 行：| 字段 | 已确认内容 | 结论 |
> 第 117 行：|---|---|---|
> 第 118 行：| Search | 未发现官方产品页或上市文件对 Search 内核/硬件单元的明确描述 | 公开资料未确认 |
> 第 119 行：| Reduce | “标量/矢量/张量”“并行计算”不能证明有独立 Reduce 单元或特定归约树 | 公开资料未确认 |
> 第 120 行：| Top-k | 天垓 300 的 MoE/Attention 优化叙述没有披露 Top-k 路由实现 | 公开资料未确认 |
> 第 121 行：| Address | 未公开地址生成、寻址模式、页表/虚拟内存或地址宽度的产品级细节 | 公开资料未确认 |
> 第 122 行：| Route | MoE、AF/PD 分离和动态调度是工作负载/系统优化方向，不能直接推导专家路由硬件 | 公开资料未确认 |
> 第 123 行：| Gather | 未公开 Gather/Scatter 指令、访存合并规则或对应带宽测试 | 公开资料未确认 |
> 第 124 行：| KV | 未公开 KV Cache 容量管理、分页策略、压缩/量化格式、KV 带宽或 KV/Attention 片上路径 | 公开资料未确认 |
> 第 125 行：| 跨卡通信 | 天垓 100 页面公布 64 GB/s 片间互联带宽；官网未公开完整链路协议、交换结构、collective 实现和集群拓扑 | 只有带宽数字已确认，完整通信架构未确认 |

> 来源综合报告第 147-152 行：
> 第 147 行：| 信息 | 证据等级 | 正确表述 |
> 第 148 行：|---|---|---|
> 第 149 行：| 天枢、天璇、天玑、天权名称及年份 | 官方路线图 | 已公开路线图，不等于每一代芯片已经发布或量产 |
> 第 150 行：| “超越 Hopper/Blackwell/Rubin” | 厂商目标/比较主张 | 不能写成独立验证的性能事实 |
> 第 151 行：| 天垓 300 采用新一代架构并于 2026-07-19 发布 | 官方发布信息 | 正式发布已确认；量产和出货未确认 |
> 第 152 行：| 2027 年之后突破性架构 | 路线图 | 未来计划，不能当作现售产品 |

> 来源综合报告第 177-195 行：
> 第 177 行：| 来源标题 | 发布/文件日期 | 访问日 | 直接 URL | 用途 |
> 第 178 行：|---|---:|---:|---|---|
> 第 179 行：| 天数智芯产品技术总览 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/serias | 产品家族导航 |
> 第 180 行：| 天垓 100 产品页 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-xlxl-tg100 | BI-V100 规格与能力 |
> 第 181 行：| 智铠 100 产品页 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-tlxltt-zk100 | MR-V50/MR-V100 规格 |
> 第 182 行：| 彤央 TY1000 产品页 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-tyty1000 | 模组规格 |
> 第 183 行：| 彤央 TY1100 产品页 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100 | 模组规格 |
> 第 184 行：| 彤央 TY1100-NX 产品页 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100_NX | 终端规格 |
> 第 185 行：| 彤央 TY1100-NX-PRO 产品页 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100NXPRO | 终端规格 |
> 第 186 行：| 彤央 TY1200 产品页 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1200 | 终端规格与 35B/离线描述 |
> 第 187 行：| 天数智算软件栈 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/software?fullCode=cpjs-rj-rjz | 编译器、驱动、库、框架与 Linux 生态 |
> 第 188 行：| 认证服务器目录 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/cooperation/direct | 服务器层与 BI-V100 兼容配置 |
> 第 189 行：| 天数智芯重磅公布芯片四代架构路线图…… | 2026-01-25 | 2026-09-01 | https://www.iluvatar.com/newsDetails?code=tszxzpgbxpsdjglxttybdxlxncygjzls&topicId=495 | 路线图、彤央发布、架构主张与落地案例 |
> 第 190 行：| 天数智芯联合无问芯穹完成智铠 GPU 百卡推理集群测试与适配…… | 2024-12-08 | 2026-09-01 | https://www.iluvatar.com/newsDetails?code=tszxlhwwxqwczkGPUbktljqcsykpzcdc&topicId=495 | 百卡推理、千卡混训、Infini-AI 上线 |
> 第 191 行：| 天数智芯自主通用 GPU 算力解决方案闪亮登场 2023 世界计算大会 | 2023-09-16 | 2026-09-01 | https://www.iluvatar.com/newsDetails?code=tszxzztyGPUsljjfasldc2023sjjsdh&topicId=495 | 天垓 100/智铠 100 应用与量产表述 |
> 第 192 行：| 天垓 300 正式发布——让 AI 触手可及 | 2026-07-19 | 2026-09-01 | https://developer.iluvatar.com/news/300-ai | 新旗舰正式发布记录 |
> 第 193 行：| 天垓 300 官方公众号原文 | 2026-07-19 | 2026-09-01 | https://mp.weixin.qq.com/s/TMxa68E2WCjfh_prfhOszg | 官方发布原文入口 |
> 第 194 行：| Shanghai Iluvatar CoreX Semiconductor Co., Ltd. 招股章程 | 2025-12-30 | 2026-09-01 | https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1230/2025123000020_c.pdf | 三代产品、量产、交付、客户与服务器/集群层定义 |
> 第 195 行：| 2025 Annual Report | 2026-04-27 | 2026-09-01 | https://www.hkexnews.hk/listedco/listconews/sehk/2026/0427/2026042701285_c.pdf | 上市后公司披露入口；本报告未用其补齐未确认的逐型号规格 |

## 补充直接来源链接

1. <https://www.iluvatar.com/serias>
2. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-xlxl-tg100>
3. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-tlxltt-zk100>
4. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-tyty1000>
5. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100>
6. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100_NX>
7. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100NXPRO>
8. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1200>
