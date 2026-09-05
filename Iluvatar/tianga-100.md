# Iluvatar CoreX / 天数智芯 — 天垓 100 / TG Gen 1

- 拆分日期：2026-09-02
- 产品层级：GPGPU 芯片/训练产品
- 综合报告：[iluvatar-chips-2026-09-01.md](./iluvatar-chips-2026-09-01.md)
- 文件性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容逐行摘录综合报告，保留原报告中的状态、数字、证据等级和未知项。

> 第 13 行：|---|---|---|---|
> 第 14 行：| 天垓（TG） | 云端/数据中心训练通用 GPU | 天垓 300、天垓 150、天垓 100 | 芯片 + PCIe 加速卡；官网当前页对 300/150 的详细参数不完整 |
> 第 15 行：| 智铠（ZK） | 云端推理通用 GPU | 智铠 100 | 芯片 + MR-V50/MR-V100 PCIe 加速卡 |
> 第 21 行：
> 第 22 行：- 天垓 100 是已量产并形成出货/部署的上一代主力产品。公司上市文件披露，截至 2025-06-30 已向超过 290 名客户交付超过 52,000 片通用 GPU 产品，但没有在该处按具体型号拆分。
> 第 23 行：- 天垓 150 已被官网列为当前训练产品；其单独产品页在本次访问中没有取得可复核的规格字段，量产、出货、客户部署和云端可用日期均未在已核验材料中确认。
> 第 32 行：
> 第 33 行：官网产品导航在访问日列出天垓 300、天垓 150、天垓 100。[天数智芯产品技术总览](https://www.iluvatar.com/serias)
> 第 34 行：
> 第 36 行：|---|---|---|---|
> 第 37 行：| 天垓 100 / TG Gen 1 | 天垓 100 芯片；BI-V100 PCIe 加速卡 | 通用 GPU；32 GB HBM2；板级功耗 250 W；全长全高双槽 PCIe 卡；PCIe Gen4 x16；官网列出主控双向带宽 64 GB/s、片间互联带宽 64 GB/s | 2021-03 正式发布；上市文件称 TG Gen 1 为首个量产的国产 GPGPU 产品；已出货并部署。芯片流片的精确官方日期、本型号累计出货量未在本次已核验的一手材料中拆出 |
> 第 38 行：| 天垓 150 / TG Gen 2 | 官网训练产品；具体卡型号未在本次页面文本中取得 | 官网当前列出；上市文件称 TG Gen 2 已用于国内外主流大语言模型训练和通用计算，TG Gen 3 支持更高精度、更大内存和 PCIe Gen5，但文件没有把代际名称逐一等同为官网中文型号 | 当前产品目录可确认；正式发布、流片、送样、量产、出货、部署、云端可用日期未确认 |
> 第 40 行：
> 第 41 行：**天垓 100 的官网规格**：官网将型号写为“天垓 100 加速卡（BI-V100）”，并列出 32 GB DRAM HBM2、PCIe Gen4 x16、主控双向 64 GB/s、片间互联 64 GB/s、板级功耗 250 W、全长全高双槽和被动散热。[天垓 100 产品页](https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-xlxl-tg100)
> 第 42 行：
> 第 43 行：**天垓 100 的公开能力表述**：官网声称其核心 IP、系统架构、指令集、核心算子和软件栈由天数团队开发；支持标量、矢量、张量运算；已支持 200 余种 AI 模型。官网“百余个算法模型平均性能可媲美主流产品”等属于厂商主张，不是独立测试结论。[天垓 100 产品页](https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-xlxl-tg100)
> 第 44 行：
> 第 48 行：
> 第 49 行：官网将智铠 100 描述为基于天垓 100 芯片设计的通用 GPU 推理产品，并在详细页同时列出“智铠 100 芯片”、智铠 50 加速卡和智铠 100 加速卡。[智铠 100 产品页](https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-tlxltt-zk100)
> 第 50 行：
> 第 76 行：|---|---|---|
> 第 77 行：| 芯片 | 天垓 100、天垓 150、天垓 300、智铠 100，以及彤央内部的自研 GPGPU 模块 | “产品名”不等于已经公开了裸芯片完整规格；彤央页面没有给出独立芯片料号 |
> 第 78 行：| 板卡 | BI-V100（天垓 100）；MR-V50、MR-V100（智铠） | 板卡容量/功耗不能直接当作裸芯片 TDP |
> 第 79 行：| 模组 | TY1000、TY1100 | 699 pin、LPDDR/HBM 等是模组产品页规格，不能与 PCIe 卡规格横向直接比较 |
> 第 80 行：| 终端 | TY1100-NX、TY1100-NX-PRO、TY1200 | 这是边端整机/终端形态，附带 CPU、存储和离线运行能力 |
> 第 81 行：| 服务器 | 官方认证服务器目录中的第三方服务器，如 H3C R4900 G6/R5300G5、安擎 EG520-G30/EG820G-G20、宝德 PR210KI 等，目录展示 BI-V100 的 2U/4U、2/4/8/10 卡配置 | 认证服务器不是天数自有芯片型号，也不等同于统一机架产品 |
> 第 82 行：| 集群/机架 | 官方上市文件称提供通用 GPU 服务器和可扩展通用 GPU 集群；官方新闻提到智铠百卡推理集群、千卡异构混合训练平台 | 本次材料没有确认天数自有标准机架 SKU、机架级功耗、交换机型号或完整拓扑 |
> 第 92 行：|---|---|---|---|---|---|---|---|---|---|
> 第 93 行：| 天垓 100 | 官网历史介绍称 2021-03 正式发布训练产品 | 2021-03 | 本次已核验材料未取得可引用的官方流片日期 | 未确认 | 上市文件称 TG Gen 1 为首个量产国产 GPGPU；官方 2023 新闻亦称率先量产 | 上市文件披露公司整体 2022–2025H1 出货增长；截至 2025-06-30 超过 52,000 片交付，未按型号拆分 | 具体云租用日未确认 | 属已发布代际 | 未发现官方 EOL |
> 第 94 行：| 天垓 150 | 至少在上市前/当前官网列出 | 未确认精确日期 | 未确认 | 未确认 | 未确认 | 未确认具体型号出货 | 未确认 | 属当前天垓训练线 | 未发现官方 EOL |
> 第 106 行：
> 第 107 行：- 天垓 100 产品页将其归为通用 GPU，支持标量、矢量、张量运算；板卡为 32 GB HBM2、250 W、PCIe Gen4 x16，并公布 64 GB/s 主控双向带宽和 64 GB/s 片间互联带宽。
> 第 108 行：- 智铠 100 产品页将其归为通用 GPU 推理系列，MR-V50/MR-V100 采用 16 GB/32 GB HBM2e、75 W/150 W 板级功耗，支持 FP32、FP16、INT8 混合推理。
> 第 124 行：| KV | 未公开 KV Cache 容量管理、分页策略、压缩/量化格式、KV 带宽或 KV/Attention 片上路径 | 公开资料未确认 |
> 第 125 行：| 跨卡通信 | 天垓 100 页面公布 64 GB/s 片间互联带宽；官网未公开完整链路协议、交换结构、collective 实现和集群拓扑 | 只有带宽数字已确认，完整通信架构未确认 |
> 第 126 行：
> 第 132 行：
> 第 133 行：- 天垓系列定位为训练产品线。官网将天垓 100 描述为支持 AI 训练、科学计算、新算法研究和通用计算。
> 第 134 行：- 官方 2023 新闻称基于天垓 100 与智铠 100 的方案已支持国内研究机构 650 亿参数大模型训练以及千亿级参数大模型推理；这是厂商应用案例表述，未给出独立测试报告。[2023 世界计算大会官方新闻](https://www.iluvatar.com/newsDetails?code=tszxzztyGPUsljjfasldc2023sjjsdh&topicId=495)
> 第 135 行：- 官方 2024-12 新闻称 2024-07 已与无问芯穹合作构建单任务千卡规模异构芯片混合训练平台，最高算力利用率 97.6%；该数值是合作双方发布的厂商/平台口径。
> 第 179 行：| 天数智芯产品技术总览 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/serias | 产品家族导航 |
> 第 180 行：| 天垓 100 产品页 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-xlxl-tg100 | BI-V100 规格与能力 |
> 第 181 行：| 智铠 100 产品页 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-tlxltt-zk100 | MR-V50/MR-V100 规格 |
> 第 187 行：| 天数智算软件栈 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/software?fullCode=cpjs-rj-rjz | 编译器、驱动、库、框架与 Linux 生态 |
> 第 188 行：| 认证服务器目录 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/cooperation/direct | 服务器层与 BI-V100 兼容配置 |
> 第 189 行：| 天数智芯重磅公布芯片四代架构路线图…… | 2026-01-25 | 2026-09-01 | https://www.iluvatar.com/newsDetails?code=tszxzpgbxpsdjglxttybdxlxncygjzls&topicId=495 | 路线图、彤央发布、架构主张与落地案例 |
> 第 190 行：| 天数智芯联合无问芯穹完成智铠 GPU 百卡推理集群测试与适配…… | 2024-12-08 | 2026-09-01 | https://www.iluvatar.com/newsDetails?code=tszxlhwwxqwczkGPUbktljqcsykpzcdc&topicId=495 | 百卡推理、千卡混训、Infini-AI 上线 |
> 第 191 行：| 天数智芯自主通用 GPU 算力解决方案闪亮登场 2023 世界计算大会 | 2023-09-16 | 2026-09-01 | https://www.iluvatar.com/newsDetails?code=tszxzztyGPUsljjfasldc2023sjjsdh&topicId=495 | 天垓 100/智铠 100 应用与量产表述 |
> 第 192 行：| 天垓 300 正式发布——让 AI 触手可及 | 2026-07-19 | 2026-09-01 | https://developer.iluvatar.com/news/300-ai | 新旗舰正式发布记录 |

## 直接来源链接

1. <https://www.iluvatar.com/serias>
2. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-xlxl-tg100>
3. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-tlxltt-zk100>
4. <https://www.iluvatar.com/newsDetails?code=tszxzztyGPUsljjfasldc2023sjjsdh&topicId=495>
5. <https://www.iluvatar.com/serias>
6. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-xlxl-tg100>
7. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-tlxltt-zk100>
8. <https://www.iluvatar.com/software?fullCode=cpjs-rj-rjz>
9. <https://www.iluvatar.com/cooperation/direct>
10. <https://www.iluvatar.com/newsDetails?code=tszxzpgbxpsdjglxttybdxlxncygjzls&topicId=495>
11. <https://www.iluvatar.com/newsDetails?code=tszxlhwwxqwczkGPUbktljqcsykpzcdc&topicId=495>
12. <https://www.iluvatar.com/newsDetails?code=tszxzztyGPUsljjfasldc2023sjjsdh&topicId=495>
13. <https://developer.iluvatar.com/news/300-ai>

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

> 来源综合报告第 35-39 行：
> 第 35 行：| 型号 | 芯片/卡/系统层级 | 已核验规格或描述 | 生命周期状态（截至 2026-09-01） |
> 第 36 行：|---|---|---|---|
> 第 37 行：| 天垓 100 / TG Gen 1 | 天垓 100 芯片；BI-V100 PCIe 加速卡 | 通用 GPU；32 GB HBM2；板级功耗 250 W；全长全高双槽 PCIe 卡；PCIe Gen4 x16；官网列出主控双向带宽 64 GB/s、片间互联带宽 64 GB/s | 2021-03 正式发布；上市文件称 TG Gen 1 为首个量产的国产 GPGPU 产品；已出货并部署。芯片流片的精确官方日期、本型号累计出货量未在本次已核验的一手材料中拆出 |
> 第 38 行：| 天垓 150 / TG Gen 2 | 官网训练产品；具体卡型号未在本次页面文本中取得 | 官网当前列出；上市文件称 TG Gen 2 已用于国内外主流大语言模型训练和通用计算，TG Gen 3 支持更高精度、更大内存和 PCIe Gen5，但文件没有把代际名称逐一等同为官网中文型号 | 当前产品目录可确认；正式发布、流片、送样、量产、出货、部署、云端可用日期未确认 |
> 第 39 行：| 天垓 300 | 新一代旗舰通用 GPU；具体芯片/卡料号、显存规格未在当前可复核页面文本中公开 | 官方发布材料描述为 SIMT 通用计算架构，支持标量、矢量、张量计算；面向 Attention、MoE、AF 分离、PD 分离和大规模系统扩展优化 | 2026-07-19 正式发布；官方称具备规模化应用条件。流片、量产、批量出货、客户部署、云端可用日期未确认 |

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

1. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-tyty1000>
2. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100>
3. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100_NX>
4. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100NXPRO>
5. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1200>
6. <https://mp.weixin.qq.com/s/TMxa68E2WCjfh_prfhOszg>
7. <https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1230/2025123000020_c.pdf>
8. <https://www.hkexnews.hk/listedco/listconews/sehk/2026/0427/2026042701285_c.pdf>
