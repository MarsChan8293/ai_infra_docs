# Iluvatar CoreX / 天数智芯 — 彤央 TY1100

- 拆分日期：2026-09-02
- 产品层级：端侧算力模组
- 综合报告：[iluvatar-chips-2026-09-01.md](./iluvatar-chips-2026-09-01.md)
- 文件性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容逐行摘录综合报告，保留原报告中的状态、数字、证据等级和未知项。

> 第 15 行：| 智铠（ZK） | 云端推理通用 GPU | 智铠 100 | 芯片 + MR-V50/MR-V100 PCIe 加速卡 |
> 第 16 行：| 彤央（TY） | 边端/终端 GPGPU | TY1000、TY1100、TY1100-NX、TY1100-NX-PRO、TY1200 | 模组或算力终端/整机形态，不应与数据中心 GPU 卡混为一谈 |
> 第 17 行：
> 第 25 行：- 智铠 100 是面向推理的通用 GPU 产品，MR-V50/MR-V100 是其公开的加速卡型号；官方披露其在 2024-12 已上线无问芯穹 Infini-AI 异构云平台，可支持 7B–72B 参数模型推理。
> 第 26 行：- 彤央四款产品在官方 2026-01-26 发布活动中整体公布；官网当前还列出 TY1100-NX-PRO。它们是边端模组/终端，官网给出了不同的封装、内存、CPU 和尺寸，但本次材料没有逐型号给出流片、量产、出货日期。
> 第 27 行：- 未发现已核验官方材料公布任何型号的停产/EOL 日期；因此不能把“官网未展示”解释为停产。
> 第 65 行：| 彤央 TY1000 | 算力模组 | 699 pin；100 × 87 × 15.29 mm；32 GB HBM2e；16 GB LPDDR4；天数自研 GPGPU；8-Core ARM | 官方 2026-01-26 发布活动列为四款彤央产品之一；正式流片、量产、出货日期未确认 |
> 第 66 行：| 彤央 TY1100 | 算力模组 | 699 pin；100 × 87 × 45 mm；16/32 GB HBM2e；16 GB LPDDR5x；天数自研 GPGPU；12-Core ARM | 面向具身智能、工业能源、物流仓储、智慧超市/门店、车路协同；生命周期日期未确认 |
> 第 67 行：| 彤央 TY1100-NX | 算力终端 | 130 × 130 × 63 mm；32/64 GB LPDDR5x；16 GB LPDDR5x；天数自研 GPGPU；12-Core ARM | 官网列为当前产品；面向教学、工业、物流、门店、具身智能、视频分析、AI Agent、天气预警；生命周期日期未确认 |
> 第 68 行：| 彤央 TY1100-NX-PRO | 算力终端 | 130 × 130 × 63 mm；32 GB HBM2e；16 GB LPDDR5x；天数自研 GPGPU；12-Core ARM | 官网列为当前产品；官方 2026-01-26 新闻正文摘要重点描述四款产品，未单独给出 PRO 的发布/量产日期 |
> 第 69 行：| 彤央 TY1200 | 算力终端 | 150 × 150 × 56 mm；32 GB HBM2e；16 GB LPDDR5x；天数自研 GPGPU；16-Core x86；512 GB SSD，最高支持 2 TB NVMe | 官网称支持最高 35B 模型、可完全离线运行；官方发布活动称 300 TOPS；正式流片、量产、出货日期未确认 |
> 第 70 行：
> 第 71 行：规格来源分别为：[TY1000](https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-tyty1000)、[TY1100](https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100)、[TY1100-NX](https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100_NX)、[TY1100-NX-PRO](https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100NXPRO)、[TY1200](https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1200)。官网没有在这些页面中提供完整的 TOPS 计算精度、频率、内存带宽、功耗或互联表，因此相应字段为“公开资料未确认”。
> 第 72 行：
> 第 78 行：| 板卡 | BI-V100（天垓 100）；MR-V50、MR-V100（智铠） | 板卡容量/功耗不能直接当作裸芯片 TDP |
> 第 79 行：| 模组 | TY1000、TY1100 | 699 pin、LPDDR/HBM 等是模组产品页规格，不能与 PCIe 卡规格横向直接比较 |
> 第 80 行：| 终端 | TY1100-NX、TY1100-NX-PRO、TY1200 | 这是边端整机/终端形态，附带 CPU、存储和离线运行能力 |
> 第 81 行：| 服务器 | 官方认证服务器目录中的第三方服务器，如 H3C R4900 G6/R5300G5、安擎 EG520-G30/EG820G-G20、宝德 PR210KI 等，目录展示 BI-V100 的 2U/4U、2/4/8/10 卡配置 | 认证服务器不是天数自有芯片型号，也不等同于统一机架产品 |
> 第 182 行：| 彤央 TY1000 产品页 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-tyty1000 | 模组规格 |
> 第 183 行：| 彤央 TY1100 产品页 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100 | 模组规格 |
> 第 184 行：| 彤央 TY1100-NX 产品页 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100_NX | 终端规格 |
> 第 185 行：| 彤央 TY1100-NX-PRO 产品页 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100NXPRO | 终端规格 |
> 第 186 行：| 彤央 TY1200 产品页 | 当前页面；访问日记录 | 2026-09-01 | https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1200 | 终端规格与 35B/离线描述 |

## 直接来源链接

1. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-tyty1000)、[TY1100](https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100)、[TY1100-NX](https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100_NX)、[TY1100-NX-PRO](https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100NXPRO)、[TY1200](https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1200)。官网没有在这些页面中提供完整的>
2. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-tyty1000>
3. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100>
4. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100_NX>
5. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1100NXPRO>
6. <https://www.iluvatar.com/productDetails?fullCode=cpjs-yj-ytxl-TY1200>

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
4. <https://www.iluvatar.com/software?fullCode=cpjs-rj-rjz>
5. <https://www.iluvatar.com/cooperation/direct>
6. <https://www.iluvatar.com/newsDetails?code=tszxzpgbxpsdjglxttybdxlxncygjzls&topicId=495>
7. <https://www.iluvatar.com/newsDetails?code=tszxlhwwxqwczkGPUbktljqcsykpzcdc&topicId=495>
8. <https://www.iluvatar.com/newsDetails?code=tszxzztyGPUsljjfasldc2023sjjsdh&topicId=495>
9. <https://developer.iluvatar.com/news/300-ai>
10. <https://mp.weixin.qq.com/s/TMxa68E2WCjfh_prfhOszg>
11. <https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1230/2025123000020_c.pdf>
12. <https://www.hkexnews.hk/listedco/listconews/sehk/2026/0427/2026042701285_c.pdf>
