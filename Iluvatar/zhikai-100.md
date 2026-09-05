# Iluvatar CoreX / 天数智芯 — 智铠 100

- 拆分日期：2026-09-02
- 产品层级：GPGPU 芯片/推理产品
- 综合报告：[iluvatar-chips-2026-09-01.md](./iluvatar-chips-2026-09-01.md)
- 文件性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容逐行摘录综合报告，保留原报告中的状态、数字、证据等级和未知项。

> 第 14 行：| 天垓（TG） | 云端/数据中心训练通用 GPU | 天垓 300、天垓 150、天垓 100 | 芯片 + PCIe 加速卡；官网当前页对 300/150 的详细参数不完整 |
> 第 15 行：| 智铠（ZK） | 云端推理通用 GPU | 智铠 100 | 芯片 + MR-V50/MR-V100 PCIe 加速卡 |
> 第 16 行：| 彤央（TY） | 边端/终端 GPGPU | TY1000、TY1100、TY1100-NX、TY1100-NX-PRO、TY1200 | 模组或算力终端/整机形态，不应与数据中心 GPU 卡混为一谈 |
> 第 24 行：- 天垓 300 于 2026-07-19 由官方开发者门户列为正式发布的新一代旗舰；官方披露“具备规模化应用条件”，但本次已核验材料未确认流片、量产、批量出货、客户部署或云端可用的独立日期。
> 第 25 行：- 智铠 100 是面向推理的通用 GPU 产品，MR-V50/MR-V100 是其公开的加速卡型号；官方披露其在 2024-12 已上线无问芯穹 Infini-AI 异构云平台，可支持 7B–72B 参数模型推理。
> 第 26 行：- 彤央四款产品在官方 2026-01-26 发布活动中整体公布；官网当前还列出 TY1100-NX-PRO。它们是边端模组/终端，官网给出了不同的封装、内存、CPU 和尺寸，但本次材料没有逐型号给出流片、量产、出货日期。
> 第 48 行：
> 第 49 行：官网将智铠 100 描述为基于天垓 100 芯片设计的通用 GPU 推理产品，并在详细页同时列出“智铠 100 芯片”、智铠 50 加速卡和智铠 100 加速卡。[智铠 100 产品页](https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-tlxltt-zk100)
> 第 50 行：
> 第 52 行：|---|---|---|---|
> 第 53 行：| 智铠 100 芯片 | 芯片 | 官网未给出裸芯片面积、制程、晶体管数或完整算力表 | 官网产品体系可确认；流片/量产日期未在本次页面中单独确认 |
> 第 54 行：| 智铠 50（MR-V50） | PCIe 推理加速卡 | 通用 GPU；16 GB HBM2e；板级功耗 75 W；半长半高单槽 PCIe；被动散热；PCIe Gen4 x16；支持 H.264/H.265/VP9/AVS2 | 官网在访问日公开列出；单独发布、量产和出货日期未确认 |
> 第 55 行：| 智铠 100（MR-V100） | PCIe 推理加速卡 | 通用 GPU；32 GB HBM2e；板级功耗 150 W；全长全高单槽 PCIe；被动散热；PCIe Gen4 x16；最大 128 路 H.264 1080p@30fps 视频解码；JPEG HD 解码/编码 2000/500 帧 | 官网在访问日公开列出；已形成百卡推理集群并于 2024-12 上线 Infini-AI 平台 |
> 第 56 行：
> 第 57 行：官网还声称智铠系列支持 FP32、FP16、INT8 混合推理、800+ 通用指令以及主流深度学习框架；“实际使用性能为市场主流产品 2–3 倍”“迁移时间下降 50% 以上”属于厂商主张，缺少本次已核验的独立复现实验。[智铠 100 产品页](https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-tlxltt-zk100)
> 第 58 行：
> 第 76 行：|---|---|---|
> 第 77 行：| 芯片 | 天垓 100、天垓 150、天垓 300、智铠 100，以及彤央内部的自研 GPGPU 模块 | “产品名”不等于已经公开了裸芯片完整规格；彤央页面没有给出独立芯片料号 |
> 第 78 行：| 板卡 | BI-V100（天垓 100）；MR-V50、MR-V100（智铠） | 板卡容量/功耗不能直接当作裸芯片 TDP |
> 第 79 行：| 模组 | TY1000、TY1100 | 699 pin、LPDDR/HBM 等是模组产品页规格，不能与 PCIe 卡规格横向直接比较 |
> 第 82 行：| 集群/机架 | 官方上市文件称提供通用 GPU 服务器和可扩展通用 GPU 集群；官方新闻提到智铠百卡推理集群、千卡异构混合训练平台 | 本次材料没有确认天数自有标准机架 SKU、机架级功耗、交换机型号或完整拓扑 |
> 第 83 行：| 云服务 | 智铠 100 于 2024-12 已在无问芯穹 Infini-AI 平台上线，支持 7B–72B 参数模型推理；这是合作方异构云/MaaS 平台上的可用性 | 不能表述为天数自营公有云，也不能把合作平台上线等同于所有型号均可云端租用 |
> 第 84 行：
> 第 86 行：
> 第 87 行：云端/集群证据：[智铠 GPU 百卡推理集群与 Infini-AI 上线](https://www.iluvatar.com/newsDetails?code=tszxlhwwxqwczkGPUbktljqcsykpzcdc&topicId=495)。官方文章称 2024-07 已合作构建单任务千卡规模异构混合训练平台，2024-12 完成智铠 100 接入并对外提供 MaaS；文章属于厂商与合作方联合发布，平台性能数字应按厂商/合作方口径理解。
> 第 88 行：
> 第 95 行：| 天垓 300 | 2026-07-19 官方开发者门户/公众号 | 2026-07-19 | 未确认 | 未确认 | 官方称具备规模化应用条件，未等同于已量产 | 未确认 | 未确认 | 2026 新架构产品 | 未发现官方 EOL |
> 第 96 行：| 智铠 100 / MR-V50/MR-V100 | 官方 2022–2023 新闻已展示/应用 | 精确正式发布日未在本次一手材料中确认 | 未确认 | 未确认 | 上市文件称 ZK Gen 1 为首个面向推理的国产 GPGPU 产品并已量产；未按 MR-V50/MR-V100 拆分 | 2024-12 前已形成百卡推理集群；客户部署总量未按卡型拆分 | 2024-12 Infini-AI 上线，支持 7B–72B 推理 | 属已发布代际 | 未发现官方 EOL |
> 第 97 行：| 彤央系列 | 2026-01-26 官方合作伙伴大会 | 2026-01-26 整体发布四款；官网另列 NX-PRO | 未确认 | 未确认 | 未确认 | 官方称已落地格蓝若、瑞幸门店、车路云试点等案例，属于厂商发布的落地陈述 | 未确认 | 边端产品线 | 未发现官方 EOL |
> 第 107 行：- 天垓 100 产品页将其归为通用 GPU，支持标量、矢量、张量运算；板卡为 32 GB HBM2、250 W、PCIe Gen4 x16，并公布 64 GB/s 主控双向带宽和 64 GB/s 片间互联带宽。
> 第 108 行：- 智铠 100 产品页将其归为通用 GPU 推理系列，MR-V50/MR-V100 采用 16 GB/32 GB HBM2e、75 W/150 W 板级功耗，支持 FP32、FP16、INT8 混合推理。
> 第 109 行：- 天垓 300 官方发布材料将其描述为 SIMT 通用计算架构，支持标量、矢量、张量，并针对 Attention、MoE、AF 分离、PD 分离和大规模系统扩展优化。Attention 超过 90%、相对 Hopper 的 64K Attention/MoE/Decode/通信改善等数值属于天数官方测试/宣传口径；本次没有取得可审计的测试脚本、完整硬件配置和独立复现实验。
> 第 133 行：- 天垓系列定位为训练产品线。官网将天垓 100 描述为支持 AI 训练、科学计算、新算法研究和通用计算。
> 第 134 行：- 官方 2023 新闻称基于天垓 100 与智铠 100 的方案已支持国内研究机构 650 亿参数大模型训练以及千亿级参数大模型推理；这是厂商应用案例表述，未给出独立测试报告。[2023 世界计算大会官方新闻](https://www.iluvatar.com/newsDetails?code=tszxzztyGPUsljjfasldc2023sjjsdh&topicId=495)
> 第 135 行：- 官方 2024-12 新闻称 2024-07 已与无问芯穹合作构建单任务千卡规模异构芯片混合训练平台，最高算力利用率 97.6%；该数值是合作双方发布的厂商/平台口径。
> 第 138 行：
> 第 139 行：- 智铠系列定位为推理产品，MR-V50/MR-V100 公开支持 FP32、FP16、INT8 和视频编解码。
> 第 140 行：- 官方 2024-12 新闻称智铠 100 已在 Infini-AI 上线，可支持 7B–72B 参数模型推理；已收录 Stable Diffusion、Qwen2.5、CogVideoX、Llama 3.1 等模型。该事实是平台上线范围，不是所有模型在所有批量/上下文下的性能保证。[官方合作新闻](https://www.iluvatar.com/newsDetails?code=tszxlhwwxqwczkGPUbktljqcsykpzcdc&topicId=495)
> 第 141 行：- 彤央 TY1200 官网称最高支持 35B 模型、完全离线运行；这是终端产品页的厂商能力描述，未公开具体量化格式、上下文长度和 tokens/s。
> 第 168 行：3. 天垓 150 的正式发布日期、量产批次和具体客户/云平台。
> 第 169 行：4. 智铠 100 芯片的制程、面积、完整算力、显存带宽和芯片级功耗；MR-V50/MR-V100 的流片/量产时间。
> 第 170 行：5. 彤央各型号内部 GPGPU 的芯片料号、制程、频率、算力精度、带宽、功耗和封装来源。
> 第 180 行：| 天垓 100 产品页 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-xlxl-tg100 | BI-V100 规格与能力 |
> 第 181 行：| 智铠 100 产品页 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-tlxltt-zk100 | MR-V50/MR-V100 规格 |
> 第 182 行：| 彤央 TY1000 产品页 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-tyty1000 | 模组规格 |
> 第 190 行：| 天数智芯联合无问芯穹完成智铠 GPU 百卡推理集群测试与适配…… | 2024-12-08 | 2026-09-01 | https://www.iluvatar.com/newsDetails?code=tszxlhwwxqwczkGPUbktljqcsykpzcdc&topicId=495 | 百卡推理、千卡混训、Infini-AI 上线 |
> 第 191 行：| 天数智芯自主通用 GPU 算力解决方案闪亮登场 2023 世界计算大会 | 2023-09-16 | 2026-09-01 | https://www.iluvatar.com/newsDetails?code=tszxzztyGPUsljjfasldc2023sjjsdh&topicId=495 | 天垓 100/智铠 100 应用与量产表述 |
> 第 192 行：| 天垓 300 正式发布——让 AI 触手可及 | 2026-07-19 | 2026-09-01 | https://developer.iluvatar.com/news/300-ai | 新旗舰正式发布记录 |

## 直接来源链接

1. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-tlxltt-zk100)>
2. <https://www.iluvatar.com/newsDetails?code=tszxlhwwxqwczkGPUbktljqcsykpzcdc&topicId=495)。官方文章称>
3. <https://www.iluvatar.com/newsDetails?code=tszxzztyGPUsljjfasldc2023sjjsdh&topicId=495)>
4. <https://www.iluvatar.com/newsDetails?code=tszxlhwwxqwczkGPUbktljqcsykpzcdc&topicId=495)>
5. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-xlxl-tg100>
6. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-tlxltt-zk100>
7. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-tyty1000>
8. <https://www.iluvatar.com/newsDetails?code=tszxlhwwxqwczkGPUbktljqcsykpzcdc&topicId=495>
9. <https://www.iluvatar.com/newsDetails?code=tszxzztyGPUsljjfasldc2023sjjsdh&topicId=495>
10. <https://developer.iluvatar.com/news/300-ai>

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
2. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100>
3. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100_NX>
4. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100NXPRO>
5. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1200>
6. <https://www.iluvatar.com/software?fullCode=cpjs-rj-rjz>
7. <https://www.iluvatar.com/cooperation/direct>
8. <https://www.iluvatar.com/newsDetails?code=tszxzpgbxpsdjglxttybdxlxncygjzls&topicId=495>
9. <https://mp.weixin.qq.com/s/TMxa68E2WCjfh_prfhOszg>
10. <https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1230/2025123000020_c.pdf>
11. <https://www.hkexnews.hk/listedco/listconews/sehk/2026/0427/2026042701285_c.pdf>
