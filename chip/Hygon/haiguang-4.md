# Hygon / 海光信息 — 海光四号

- 研究截止日：2026-09-05
- 核验日期：2026-09-05
- 产品层级：CPU 代际
- 厂商总览：[海光信息](./海光信息-概览.md) · [[海光信息-概览|图谱总览]]
- 页面性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容按对象边界重排自现有综合报告，并以本页直接来源清单核验；不能由相邻产品层级推导的项目保留为“公开资料未确认”。

公开网络中可见“海光四号=7400 系列”“深算四号 2026 年量产”“深算四号支持 FP4”“某代 DCU 达到某海外 GPU 百分比”等研报、媒体转述或自媒体预测。本报告未找到足以支撑这些说法的海光官方产品数据表、正式发布公告或可复核独立测试，因此均不作为确认事实。

## 关联证据与规格

本节保留与本对象相关的关联规格和生命周期证据；其中的卡、模块、服务器、机架、集群或云数据保持原产品层级，不能回填为芯片规格。

| 代际 | 已确认首次/量产/收入节点 | 发布与应用证据 | 截至 2026-09-01 的边界 |
|---|---|---|---|
| 海光一号 | 量产：2018-04；首次客户验证：2018-04；首次收入：2018-05 | 公司上市审核问询回复表格记为“结项、完成产品验证，实现商业化应用”。系列包括 7100、5100、3100。 | 公司 2022 年问询回复称该代“接近停产换代”；未找到更晚的正式停产公告，故“已停产”不作确认。 |
| 海光二号 | 量产：2020-01；首次客户验证：2020-02；首次收入：2020-04 | 公司问询回复记为“结项、完成产品验证，实现商业化应用”。系列包括 7200、5200、3200。 | 2022 年材料称其为当时主流销售产品；截至研究日的具体销量、在售 SKU、停产日期未确认。 |
| 海光三号 | 上市审核表格：量产 2022-03；公司官网新闻：2022-06-13 发布新闻，称 2022-06-07 举行新品发布会 | 最高规格：32 核 64 线程、128 条 PCIe 4.0、内存频率至 3200 MHz；公司称相对上一代整体实测性能提升约 45%。这些性能数字属于公司发布口径。 | 2023 年半年报称“新产品海光三号投放市场，得到客户认可”。可确认已进入市场；具体 2026 年主力 SKU、出货量和停产状态未确认。生态整机页面常见 7300/5300/3300，但海光官网产品中心未在同页给出该映射，作为生态侧型号记录。 |
| 海光四号 | 2023 年 10 月发布这一说法出现在 2025 年上交所披露的其他公司招股说明书引用资料中；不是海光自身产品数据表 | 海光 2022 年上市审核材料当时仍记为“暂无量产、硅后验证”；2023 年半年报将其列为下一代 CPU 研发项目。 | 公开资料未确认具体核心数、频率、内存、PCIe、制程、正式 SKU、量产日期、出货日期、客户部署规模。部分研报/二手文章称 7400 或已商用，未作为本报告官方事实。 |
| 海光五号 | 2023 年半年报列为“下一代 CPU 产品”；2026-04-21 投资者问答中，针对“是否发布、是否交付”的问题，公司仅回复 CPU、DCU 按规划推进研发与客户验证 | 无官方公开规格表、白皮书或正式发布页可核验 | **公开资料未确认：流片、送样、量产、出货、客户部署、云端可用、具体系列编号均未确认。** |

| 编号 | 来源标题 | 日期/状态 | 直接 URL | 支持内容 |
|---|---|---|---|---|
| S1 | 海光官网：CPU 产品中心 | 页面当前公开 | [hygon.cn/product/cpu](https://www.hygon.cn/product/cpu) | 7000/5000/3000 系列定位与系列级参数。 |
| S2 | 海光官网：海光三号 CPU 正式发布 | 2022-06-13 | [hygon.cn/news?newsid=102](https://www.hygon.cn/news?newsid=102) | 海光三号发布会、32 核 64 线程、128 条 PCIe 4.0、3200 MHz、异构平台与公司性能/生态表述。 |
| S3 | 海光信息 2022 年问询函回复 | 2022-01-24 | [上交所 PDF](https://static.sse.com.cn/stock/disclosure/announcement/c/202201/001043_20220124_HGDK.pdf) | 海光一号/二号/三号/四号、深算一号/二号的量产、客户验证、首次收入和研发阶段表格；CPU 三档系列；生命周期边界。 |
| S4 | 海光信息发行注册环节反馈意见落实函回复 | 2022-06-22 | [上交所 PDF](https://static.sse.com.cn/stock/disclosure/announcement/c/202206/001043_20220622_E5LP.pdf) | 深算一号已量产、深算二号当时研发；自主 GPGPU 能力与代际状态。 |
| S5 | 海光信息上市委落实函回复 | 2022-03-31 | [上交所 PDF](https://static.sse.com.cn/stock/disclosure/announcement/c/202203/001043_20220331_G6N6.pdf) | 深算二号相对一号的计算单元、SoC、GDDR6/HBM、片上网络与访存子系统设计说明。 |
| S6 | 海光信息首次公开发行招股说明书（上会稿） | 2022-03-07 | [上交所 PDF](https://static.sse.com.cn/stock/disclosure/announcement/c/202203/001043_20220307_T2KW.pdf) | 深算一号历史规格、PCIe/xGMI、HBM、TDP及中国计量科学研究院测试报告引用。 |
| S7 | 海光信息 2023 年半年度报告 | 2023-08-25 | [巨潮 PDF](https://static.cninfo.com.cn/finalpage/2023-08-25/1217637267.PDF) | 海光三号投放市场并获客户认可；海光四号、五号及深算二号、三号研发进展。 |
| S8 | 海光信息 2025 年年度报告摘要 | 2026-04-08 | [巨潮 PDF](https://static.cninfo.com.cn/finalpage/2026-04-08/1225083108.PDF) | CPU+GPU/DCU 商业化、6000+生态伙伴、365 款模型适配主张、HSL 于 2025-09 发布。 |
| S9 | 海光信息 2026 年半年度报告（公开公告镜像） | 2026-08-14 | [新浪财经公告页](https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=12492765) | 释义中的 DCU/DTK/HSL；研发项目“新一代 CPU”“海光协处理器”等处于开发阶段；报告期业务背景。该链接是公开公告镜像，原报告应以上交所/公司披露为准。 |
| S10 | 海光信息投资者互动问答汇总：深算三号/四号 | 2025-12-10 | [巨潮投资者问答 PDF](https://dataclouds.cninfo.com.cn/shgonggao/investor/2025/20251210/0d17c6e844b64a66ab07bf268afaa827.PDF) | 深算三号投入市场并获认可；深算四号研发进展顺利；HAIC/光合组织活动范围。 |
| S11 | 光合开发者社区首页 | 页面当前公开 | [developer.sourcefind.cn](https://developer.sourcefind.cn/) | BW1000、K100-AI 产品矩阵，DCU 软件/生态层级。 |
| S12 | DTK-26.04 更新：适配 BW1100 系列 DCU 卡 | 2026-03-31 | [光合开发者社区详情页](https://developer.sourcefind.cn/category/dynamics/detail?post_id=7d3e64c0-2cd2-11f1-854e-0242ac150003) | 深算三号 BW1100 适配、HIP/驱动、FP8、TensorCore、P2P/集合通信等软件更新。 |
| S13 | DAS1.8 更新：适配深算三号 BW1100 | 2026-03-31 | [光合开发者社区详情页](https://developer.sourcefind.cn/category/dynamics/detail?post_id=8f764df5-2cb6-11f1-854e-0242ac150003) | FP8、KV Cache FP8、KV Store、PD 分离、大 EP、MoE A2A overlap 等软件栈主张。 |
| S14 | 光合开发者社区 DTK 页面 | 页面当前公开 | [developer.sourcefind.cn/dtk](https://developer.sourcefind.cn/dtk) | HIP/CUDA/通信库/高速互联等软件层组成。 |
| S15 | 2026-04-21 海光信息互动问答公开转述 | 2026-04-21 | [同花顺转述页](https://yuanchuang.10jqka.com.cn/20260421/c676157793.shtml) | 针对海光五号发布/交付、深算四号量产/交付，公司回复 CPU、DCU 按规划推进研发与客户验证。因未直接取得互动平台原始页面，按“公开转述”使用。 |

## 直接来源

1. [上交所 PDF](https://static.sse.com.cn/stock/disclosure/announcement/c/202203/001043_20220307_T2KW.pdf)；核验日期：2026-09-05。
2. [巨潮 PDF](https://static.cninfo.com.cn/finalpage/2023-08-25/1217637267.PDF)；核验日期：2026-09-05。
3. [巨潮 PDF](https://static.cninfo.com.cn/finalpage/2026-04-08/1225083108.PDF)；核验日期：2026-09-05。
4. [hygon.cn/product/cpu](https://www.hygon.cn/product/cpu)；核验日期：2026-09-05。
5. [hygon.cn/news?newsid=102](https://www.hygon.cn/news?newsid=102)；核验日期：2026-09-05。
6. [上交所 PDF](https://static.sse.com.cn/stock/disclosure/announcement/c/202201/001043_20220124_HGDK.pdf)；核验日期：2026-09-05。
7. [上交所 PDF](https://static.sse.com.cn/stock/disclosure/announcement/c/202206/001043_20220622_E5LP.pdf)；核验日期：2026-09-05。
8. [上交所 PDF](https://static.sse.com.cn/stock/disclosure/announcement/c/202203/001043_20220331_G6N6.pdf)；核验日期：2026-09-05。
9. [新浪财经公告页](https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=12492765)；核验日期：2026-09-05。
10. [巨潮投资者问答 PDF](https://dataclouds.cninfo.com.cn/shgonggao/investor/2025/20251210/0d17c6e844b64a66ab07bf268afaa827.PDF)；核验日期：2026-09-05。
11. [developer.sourcefind.cn](https://developer.sourcefind.cn/)；核验日期：2026-09-05。
12. [光合开发者社区详情页](https://developer.sourcefind.cn/category/dynamics/detail?post_id=7d3e64c0-2cd2-11f1-854e-0242ac150003)；核验日期：2026-09-05。
13. [光合开发者社区详情页](https://developer.sourcefind.cn/category/dynamics/detail?post_id=8f764df5-2cb6-11f1-854e-0242ac150003)；核验日期：2026-09-05。
14. [developer.sourcefind.cn/dtk](https://developer.sourcefind.cn/dtk)；核验日期：2026-09-05。
15. [同花顺转述页](https://yuanchuang.10jqka.com.cn/20260421/c676157793.shtml)；核验日期：2026-09-05。

## 证据边界

- 芯片、封装、卡/模组、服务器/机架、集群、软件和云服务按来源原层级记录；系统、卡、模块或集群数据不自动回填为芯片规格。
- “宣布、流片/工程样片、送样、量产、出货、客户部署、云/实例可用、路线图、停产”分别判断；没有直接证据的阶段写为“公开资料未确认”。
- 官方发布、产品页或软件支持不能单独证明量产、出货或独立性能；厂商主张、独立验证和分析推断不混写。
- 本页是基于现有综合报告和直接来源的证据重排页；引用以文末直接 URL 为准，不再使用综合报告行号作为外部引用。
