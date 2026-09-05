# Moore Threads / 摩尔线程 — 摩尔线程 AIBOOK、AICUBE、SGX5000、KUAE 与云原生（边界文件，非芯片）

- 拆分日期：2026-09-02
- 产品层级：终端/服务器/软件平台（非芯片）
- 综合报告：[moore-threads-chips-2026-09-01.md](./moore-threads-chips-2026-09-01.md)
- 文件性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容逐行摘录综合报告，保留原报告中的状态、数字、证据等级和未知项。

> 第 10 行：
> 第 11 行：截至 2026-09-01，摩尔线程公开产品已经形成从第四代“平湖”架构 PH100/MTT S5000、第三代“曲院”/MTT S4000、第一代 MUSA 的“春晓”/MTT S3000、S80、S70，到“苏堤”/MTT S1000、S2000，再到长江 M1000 SoC、MTT E300 边缘模组和 AIBOOK/AICUBE 端侧设备的全栈矩阵。技术路线的核心差异在于全功能 GPU、原生 FP8、张量访存引擎 TME、异步通信引擎 ACE、MTLink Scale-up 和 MUSA 软件生态；但最新产品的公开页面仍没有完整披露芯片面积、制程、晶体管数、TDP、流片/送样/量产/出货与客户部署时间线，不能用厂商性能宣传或服务器配置替代这些状态证据。
> 第 12 行：
> 第 16 行：| --- | --- | --- | --- |
> 第 17 行：| 平湖 / PH100，第四代 MUSA | MTT S5000 | 单卡智算加速卡；另见 SGX5000/KUAE 系统 | 2026-05-18 产品发布会公开；2026-05-26 公布通过国家安全可靠测评。量产、出货、客户部署、公有云可用时间未由当前公开一手资料确认。 |
> 第 18 行：| 曲院，第三代 MUSA | MTT S4000 | 单卡智算加速卡 | 2023-09 秋季发布会公开；2025-05-07 获中国信通院 AI 芯片和大模型适配验证。规模化系统部署有官方案例，但单卡量产/出货日期未单独确认。 |
> 第 21 行：| 未公开命名或未建立公开映射 | MTT X300、MTT S50、MTT S30、MTT S10 | 专业显卡、桌面显卡 | 产品页提供板卡规格和驱动支持；芯片名称、流片/量产/出货日期公开资料未确认。 |
> 第 22 行：| 长江 / M1000 | MTT E300、AIBOOK、AICUBE、AIModule | SoC、AI 模组、算力本、家庭 AI 中枢 | M1000 是芯片，E300 是模组，AIBOOK/AICUBE 是整机设备。三者不能把 50 TOPS 或统一内存数字写成单独 NPU 或 GPU 的规格。 |
> 第 23 行：
> 第 41 行：
> 第 42 行：M1000 把全大核 CPU、全功能 GPU、NPU、VPU、DPU、ISP 和 Audio DSP 集成在一个异构 SoC 中。E300 是面向嵌入式集成的 MXM 模组；AIBOOK 和 AICUBE 是基于同一 SoC 的端侧设备，不是两种新的 GPU 芯片。
> 第 43 行：
> 第 49 行：| --- | --- | --- | --- | --- | --- |
> 第 50 行：| PH100 / S5000 | 2026-05-18 产品发布会；2026-05-26 安全可靠测评公告 | 公开资料未确认 | 公开资料未确认 | 官方页面给出 SiliconFlow 测试方案、KUAE 集成方案和“联系我们”，但公开资料未确认公有云实例或普遍客户部署 | 测评通过不等同于量产 |
> 第 51 行：| 曲院 / S4000 | 2023-09 秋季发布会 | 公开资料未确认 | 公开资料未确认 | 2023-12 夸娥智算中心正式揭幕；2025-05-07 中国信通院适配验证 | 系统落地与单卡出货需分开 |
> 第 56 行：| M1000 / E300 | E300 产品页和开发者文档可见 | 公开资料未确认 | 公开资料未确认 | E300定位客户集成；AIModule 文档给出边缘视频推理路径；没有公开客户名单/出货数量 | E300是模组，M1000是内部 SoC |
> 第 57 行：| AIBOOK、AICUBE、SGX5000、KUAE | AIBOOK 产品页有“立即购买”；AICUBE 产品页有“Buy Now”；SGX5000/KUAE为系统产品 | 适用于内部芯片的流片状态：公开资料未确认 | 设备/服务器的具体生产批次公开资料未确认 | KUAE产品页称“30天建设集群”、支持万卡级目标；不是公有云可用证明 | 服务器/集群数字不得回填到单卡 |
> 第 58 行：
> 第 103 行：| MTT E300 | M1000 SoC内部的 MXM 314-pin AI模组 | 60 mm × 82 mm；最高45 W；8核全大核、2.65 GHz；50 TOPS INT8 Dense；GPU 12 TFLOPS FP16/24 TOPS INT8、3 TFLOPS FP32；双核NPU、每核1.5 GHz；统一内存16/32/64 GB；带宽102.4/120/136.5 GB/s；PCIe 5.0 x14；双千兆网口 | 45 W是模组平台上限；不能当作 M1000单独芯片 TDP |
> 第 104 行：| MTT AIBOOK | 长江 M1000 SoC；算力本/端侧工作站 | 50 TOPS异构 AI；32 GB LPDDR5X 7500 MT/s统一内存；1 TB SSD；CPU+Universal GPU；Linux/Windows/Android | 整机产品；50 TOPS不是单独NPU或GPU规格 |
> 第 105 行：| MTT AICUBE | 长江 M1000 SoC；家庭AI中枢 | 50 TOPS；16/32 GB LPDDR5X；统一内存带宽120 GB/s；1×1 TB NVMe、2个扩展槽；2.65 GHz全大核CPU；125 mm × 125 mm × 135 mm；约1.16 kg（标准配置） | 整机产品；无公开整机 TDP |
> 第 106 行：| MTT SGX5000 | 服务器，不是芯片 | 双路、8 GPU服务器；官方产品组合将其与 S5000 和 KUAE 绑定 | 服务器规格不能回填 S5000单卡；完整 CPU/网络/电源配置未公开确认 |
> 第 107 行：| MTT KUAE | 智算中心软硬一体方案 | 基于 S5000 与 SGX5000；KUAE Platform 集群管理；ModelStudio模型开发/训练；官网称30天集群建设、支持万亿参数分布式训练目标 | 解决方案/软件平台，不是芯片、板卡或公有云实例 |
> 第 108 行：
> 第 115 行：        ↓
> 第 116 行：SGX5000（双路八卡服务器）、AIBOOK/AICUBE（端侧设备）
> 第 117 行：        ↓
> 第 118 行：KUAE（集群基础设施 + Platform + ModelStudio）
> 第 119 行：        ↓
> 第 125 行：- S2000 是一张板卡内含两颗苏堤芯片的历史特殊形态；不能把 S2000 的板卡显存、功耗或 PCIe Switch 规格写成单颗芯片规格。
> 第 126 行：- E300 是 MXM 模组，M1000 是其内部 SoC；AIBOOK/AICUBE 是整机，统一内存容量和整机存储不能写成显存容量。
> 第 127 行：- SGX5000 是双路八卡服务器；“8 GPU”是服务器组成，不是 S5000 单卡或 PH100 单芯片规格。
> 第 128 行：- KUAE 的“千卡/万卡”“30天建设”是系统方案目标/能力声明，不是已经交付的固定机架型号，也不是云服务 SKU。
> 第 129 行：
> 第 145 行：
> 第 146 行：S5000公开了 80 GB、1.6 TB/s 单卡显存和 60 MB LLC；S4000公开了 48 GB、768 GB/s；S3000公开了 32 GB GDDR6、448 GB/s。S80/S70/S50等为 GDDR6 路线，E300/AIBOOK/AICUBE为 LPDDR统一内存路线。对于 PH100，当前公开页面没有明确标注显存介质类型，不能自行写成 HBM。
> 第 147 行：
> 第 156 行：- 分析工具：Moore Perf Compute、Moore Perf System、mthreads-gmi；当前服务器文档可见 Driver/MUSA SDK 5.2.0 安装路径。
> 第 157 行：- 云原生：KUAE Platform、MT GPU Operator、sGPU/vGPU、SR-IOV、Kubernetes；官方云原生文档列出 Kubernetes 1.19–1.32 的支持范围，但版本随文档更新可能变化。
> 第 158 行：- M1000 端侧：MTNN、MTStream、vLLM-MUSA-M1000、SGLang-MUSA-M1000；E300文档给出NPU优先、GPU辅助或纯GPU推理路径。
> 第 203 行：- S5000与 PH100、平湖、第四代 MUSA 的关联，以及 S4000与曲院、S3000/S80/S70与春晓、S1000/S2000与苏堤的关联，有官方页面/文档支撑。
> 第 204 行：- MTT E300 是模组，M1000 是内部 SoC；AIBOOK/AICUBE是长江 SoC设备；SGX5000是双路八卡服务器；KUAE是软硬一体系统方案。
> 第 205 行：- TCE、TME、ATB、ACE、MTLink、LLC和 MUSA 软件栈的功能描述来自官方架构/产品/开发文档。
> 第 210 行：- 平湖 FP8 GEMM、Flash Attention、ACE收益和 MTLink带宽效率数字。
> 第 211 行：- X300 相对 S50 的图形倍率，以及 S4000/KUAE 的规模化集群能力。
> 第 212 行：
> 第 216 行：- MUSA全功能路线更强调通用性和软件迁移，可能以更复杂的生态适配换取功能覆盖；综合性能仍需要按模型、版本、拓扑和精度实测。
> 第 217 行：- 统一内存的 E300/AIBOOK/AICUBE 对端侧部署便利，但 50 TOPS异构总和不能直接与数据中心单卡 Tensor峰值比较。
> 第 218 行：
> 第 228 行：8. M1000：E300文档公开了 SoC异构组成，但没有公开 M1000芯片面积、制程、晶体管数和独立芯片级峰值表。
> 第 229 行：9. 公共云：官网的试用、购买、联系我们、GPU Cloud PC入口、KUAE集群方案和合作方测试不能替代“用户可在某云按 SKU 开通实例”的证据；截至截止日公开资料未确认统一公有云可用状态。
> 第 230 行：10. 停产/停售：未找到官方停产公告；当前目录未突出 S1000 不能作为停产证据。
> 第 256 行：| 产品概述（MTT E300 与 M1000 SoC） | 页面日期未标注 | https://docs.mthreads.com/e300/version-1.5.0/e300-doc-online/product_overview/ | M1000与E300层级、GPU/NPU/统一内存 |
> 第 257 行：| MTT AIBOOK | 页面日期未标注 | https://www.mthreads.com/product/aibook | 长江 SoC设备规格 |
> 第 258 行：| MTT AICUBE | 页面日期未标注 | https://en.mthreads.com/product/aicube | 长江 SoC家庭设备规格 |
> 第 259 行：| MTT SGX5000 | 页面日期未标注 | https://www.mthreads.com/product/SGX5000 | 双路八卡服务器层级 |
> 第 260 行：| MTT KUAE | 页面日期未标注 | https://www.mthreads.com/product/KUAE | 集群方案、Platform、ModelStudio |
> 第 261 行：| 关于我们 | 页面日期未标注 | https://www.mthreads.com/about | 2023-09 S4000/夸娥发布、2023-12智算中心、2024-07万卡方案 |
> 第 262 行：| MTT S4000 训推一体计算卡通过中国信通院 AI 芯片和大模型适配验证 | 2025-05-07 | https://www.mthreads.com/news/244 | 第三方适配/验证状态 |
> 第 263 行：| MT GPU Operator 发布版本信息 | 页面日期未标注 | https://docs.mthreads.com/en/cloud-native/cloud-native-doc-online/releasenote/ | GPU型号、Kubernetes和云原生支持 |
> 第 264 行：| sGPU 使用指南 | 页面日期未标注 | https://docs.mthreads.com/cloud-native/cloud-native-doc-online/user_guide/sgpu_guide/ | sGPU显存切分与容器使用边界 |
> 第 265 行：| AIModule - MTStream | 页面日期未标注 | https://docs.mthreads.com/mtstream/mtstream-doc-online/ | M1000 NPU/GPU边缘推理与零拷贝路径 |

## 直接来源链接

1. <https://docs.mthreads.com/e300/version-1.5.0/e300-doc-online/product_overview/>
2. <https://www.mthreads.com/product/aibook>
3. <https://en.mthreads.com/product/aicube>
4. <https://www.mthreads.com/product/SGX5000>
5. <https://www.mthreads.com/product/KUAE>
6. <https://www.mthreads.com/about>
7. <https://www.mthreads.com/news/244>
8. <https://docs.mthreads.com/en/cloud-native/cloud-native-doc-online/releasenote/>
9. <https://docs.mthreads.com/cloud-native/cloud-native-doc-online/user_guide/sgpu_guide/>
10. <https://docs.mthreads.com/mtstream/mtstream-doc-online/>

## 证据边界

- 这是资料重排页，不是重新发布或重新核验的产品公告。
- “发布、流片、送样、量产、出货、客户部署、云端可用、路线图、停产”等状态只在综合报告明确写出时保留；缺失项仍为“公开资料未确认”。
- 若摘录同时出现芯片、板卡、服务器、机架或云服务，均按原报告层级保留，并以“产品层级”字段提醒，不做跨层级推导。

## 关联表格原文（完整表格）

以下表格块来自综合报告中与本拆分项命中的表格，完整保留表头、状态列和规格列。

> 来源综合报告第 15-22 行：
> 第 15 行：| 芯片/架构家族 | 公开关联产品 | 产品层级 | 公开定位与状态边界 |
> 第 16 行：| --- | --- | --- | --- |
> 第 17 行：| 平湖 / PH100，第四代 MUSA | MTT S5000 | 单卡智算加速卡；另见 SGX5000/KUAE 系统 | 2026-05-18 产品发布会公开；2026-05-26 公布通过国家安全可靠测评。量产、出货、客户部署、公有云可用时间未由当前公开一手资料确认。 |
> 第 18 行：| 曲院，第三代 MUSA | MTT S4000 | 单卡智算加速卡 | 2023-09 秋季发布会公开；2025-05-07 获中国信通院 AI 芯片和大模型适配验证。规模化系统部署有官方案例，但单卡量产/出货日期未单独确认。 |
> 第 19 行：| 春晓，第一代 MUSA | MTT S3000、MTT S80、MTT S70 | 服务器卡、游戏显卡 | 2022-11 公开春晓芯片；S3000 官方称为基于春晓的第一款服务器 GPU。三款产品有公开规格；不同页面的 S3000/S70 FP32 数字存在口径差异。 |
> 第 20 行：| 苏堤 | MTT S1000、MTT S2000 | 服务器卡 | 官方历史白皮书称 S1000、S2000 已量产出货；S2000 是两颗苏堤芯片通过板载 PCIe Switch 组成，S1000 是单芯片。当前产品中心不再突出 S1000，停售日期未确认。 |
> 第 21 行：| 未公开命名或未建立公开映射 | MTT X300、MTT S50、MTT S30、MTT S10 | 专业显卡、桌面显卡 | 产品页提供板卡规格和驱动支持；芯片名称、流片/量产/出货日期公开资料未确认。 |
> 第 22 行：| 长江 / M1000 | MTT E300、AIBOOK、AICUBE、AIModule | SoC、AI 模组、算力本、家庭 AI 中枢 | M1000 是芯片，E300 是模组，AIBOOK/AICUBE 是整机设备。三者不能把 50 TOPS 或统一内存数字写成单独 NPU 或 GPU 的规格。 |

> 来源综合报告第 48-57 行：
> 第 48 行：| 产品/家族 | 首次披露或正式发布 | 流片/送样 | 量产/出货 | 客户部署/云端可用 | 备注 |
> 第 49 行：| --- | --- | --- | --- | --- | --- |
> 第 50 行：| PH100 / S5000 | 2026-05-18 产品发布会；2026-05-26 安全可靠测评公告 | 公开资料未确认 | 公开资料未确认 | 官方页面给出 SiliconFlow 测试方案、KUAE 集成方案和“联系我们”，但公开资料未确认公有云实例或普遍客户部署 | 测评通过不等同于量产 |
> 第 51 行：| 曲院 / S4000 | 2023-09 秋季发布会 | 公开资料未确认 | 公开资料未确认 | 2023-12 夸娥智算中心正式揭幕；2025-05-07 中国信通院适配验证 | 系统落地与单卡出货需分开 |
> 第 52 行：| 春晓 / S3000 | 2022-11 芯片公开；S3000 产品页当前可见 | 公开资料未确认 | 历史白皮书曾称“即将进入量产阶段”，当前量产日期未确认 | 服务器/OEM 适配有官方说明；公有云可用未确认 | 页面称 S3000 为首款春晓服务器 GPU |
> 第 53 行：| 苏堤 / S1000、S2000 | 历史产品白皮书披露 | 公开资料未确认 | 历史白皮书明确称“量产出货状态” | 容器化、Docker、Kubernetes 生态有文档；公有云可用未确认 | 白皮书页面日期未标注，具体量产日期未确认 |
> 第 54 行：| S80、S70 | 当前官网产品页可购买/下载驱动；具体首次发布日未在当前页标注 | 公开资料未确认 | 公开资料未确认 | “智娱摩方”整机方案使用 S80/S70；公有云可用未确认 | 不以购买入口推断生产批次 |
> 第 55 行：| X300、S50、S30、S10 | 当前官网产品页和驱动文档可见；具体首次发布日未在当前页标注 | 公开资料未确认 | 公开资料未确认 | 驱动、操作系统镜像和桌面场景有公开支持；云端可用未确认 | 产品页未建立芯片型号映射 |
> 第 56 行：| M1000 / E300 | E300 产品页和开发者文档可见 | 公开资料未确认 | 公开资料未确认 | E300定位客户集成；AIModule 文档给出边缘视频推理路径；没有公开客户名单/出货数量 | E300是模组，M1000是内部 SoC |
> 第 57 行：| AIBOOK、AICUBE、SGX5000、KUAE | AIBOOK 产品页有“立即购买”；AICUBE 产品页有“Buy Now”；SGX5000/KUAE为系统产品 | 适用于内部芯片的流片状态：公开资料未确认 | 设备/服务器的具体生产批次公开资料未确认 | KUAE产品页称“30天建设集群”、支持万卡级目标；不是公有云可用证明 | 服务器/集群数字不得回填到单卡 |

> 来源综合报告第 94-107 行：
> 第 94 行：| 产品 | 芯片/产品层级 | 公开规格摘要 | 状态与限制 |
> 第 95 行：| --- | --- | --- | --- |
> 第 96 行：| MTT S80 | 春晓；游戏显卡 | 4096核心；1.8 GHz；FP32 14.7 TFLOPS；16 GB GDDR6；256 bit；448 GB/s；PCIe Gen5 x16；最大功耗255 W；最高4路8K显示 | 当前官网有购买入口；芯片晶体管/制程和量产日期未确认 |
> 第 97 行：| MTT S70 | 春晓；游戏显卡 | 1.6 GHz；7 GB GDDR6；224 bit；392 GB/s；PCIe Gen4 x16；页面 FP32 11.5 TFLOPS；旧 PDF 为3584核心、11.2 TFLOPS | 两个官方页面存在 FP32/核心数口径差异；TDP未确认 |
> 第 98 行：| MTT S2000 | 苏堤；服务器卡 | 4096核心；FP32 10.4 TFLOPS；32 GB显存；256 bit；150 W；PCIe Gen3；两颗苏堤芯片+板载 PCIe Switch | 历史白皮书称量产出货；显存带宽未确认 |
> 第 99 行：| MTT S1000 | 苏堤；服务器卡 | 单颗苏堤芯片；半高半长、单槽；75 W；无需外接供电 | 历史白皮书称量产出货；详细算力/显存带宽未确认 |
> 第 100 行：| MTT S50 | 芯片命名未公开；桌面/工作站显卡 | 2048核心；FP32 5.2 TFLOPS；INT8 20.8 TOPS；8 GB；256 bit；1×编码器+1×解码器；TGP 85 W（全长）或70 W（半长）；PCIe单槽 | 官方支持 x86/Arm/LoongArch 与多种 Linux/Windows；芯片映射和日期未确认 |
> 第 101 行：| MTT S30 / S10 | 芯片命名未公开；数字办公显卡 | S10（4 GB）：1.0 GHz、FP32 2.0 TFLOPS、40 W；S30（2 GB）：1.3 GHz、2.6 TFLOPS、35 W；S30（4 GB）：1.3 GHz、2.6 TFLOPS、40 W；均1024核心 | 当前驱动文档支持；停售/量产日期未确认 |
> 第 102 行：| MTT X300 | 专业显卡；芯片映射未公开 | 16 GB显存；最高4路8K；36路1080P30编码、36路1080P30解码；官网称 GLMark2 为 S50 的2倍、Glx-Gears 2.9倍、Unigine Heaven 2.8倍 | 相对性能是厂商声明，页面未给完整测试平台；芯片/显存带宽/TDP未确认 |
> 第 103 行：| MTT E300 | M1000 SoC内部的 MXM 314-pin AI模组 | 60 mm × 82 mm；最高45 W；8核全大核、2.65 GHz；50 TOPS INT8 Dense；GPU 12 TFLOPS FP16/24 TOPS INT8、3 TFLOPS FP32；双核NPU、每核1.5 GHz；统一内存16/32/64 GB；带宽102.4/120/136.5 GB/s；PCIe 5.0 x14；双千兆网口 | 45 W是模组平台上限；不能当作 M1000单独芯片 TDP |
> 第 104 行：| MTT AIBOOK | 长江 M1000 SoC；算力本/端侧工作站 | 50 TOPS异构 AI；32 GB LPDDR5X 7500 MT/s统一内存；1 TB SSD；CPU+Universal GPU；Linux/Windows/Android | 整机产品；50 TOPS不是单独NPU或GPU规格 |
> 第 105 行：| MTT AICUBE | 长江 M1000 SoC；家庭AI中枢 | 50 TOPS；16/32 GB LPDDR5X；统一内存带宽120 GB/s；1×1 TB NVMe、2个扩展槽；2.65 GHz全大核CPU；125 mm × 125 mm × 135 mm；约1.16 kg（标准配置） | 整机产品；无公开整机 TDP |
> 第 106 行：| MTT SGX5000 | 服务器，不是芯片 | 双路、8 GPU服务器；官方产品组合将其与 S5000 和 KUAE 绑定 | 服务器规格不能回填 S5000单卡；完整 CPU/网络/电源配置未公开确认 |
> 第 107 行：| MTT KUAE | 智算中心软硬一体方案 | 基于 S5000 与 SGX5000；KUAE Platform 集群管理；ModelStudio模型开发/训练；官网称30天集群建设、支持万亿参数分布式训练目标 | 解决方案/软件平台，不是芯片、板卡或公有云实例 |

> 来源综合报告第 236-265 行：
> 第 236 行：| 标题 | 发布/更新时间 | 直接 URL | 用途 |
> 第 237 行：| --- | --- | --- | --- |
> 第 238 行：| 词元时代，万物智能｜摩尔线程 2026 产品发布会：打造全场景 AI 算力基石 | 2026-05-18 | https://www.mthreads.com/news/310 | S5000产品发布事件 |
> 第 239 行：| 喜报｜摩尔线程 MTT S5000（PH100 芯片）通过国家《安全可靠测评》 | 2026-05-26 | https://mthreads.com/news/312 | PH100安全测评状态 |
> 第 240 行：| MTT S5000｜训推一体全功能 GPU 智算卡 | 页面日期未标注 | https://www.mthreads.com/product/S5000 | S5000定位、性能主张、模型/推理条件 |
> 第 241 行：| MTT S4000｜大模型智算加速卡 | 页面日期未标注 | https://www.mthreads.com/product/S4000 | S4000定位和产品层级 |
> 第 242 行：| MTT S4000/S5000 产品介绍 | 页面日期未标注 | https://docs.mthreads.com/driver-linux-server/driver-linux-server-doc-online/MTT_S5000/introduction/ | S4000/S5000单卡规格、MTLink、软件 |
> 第 243 行：| 平湖第四代 GPU 架构 | 页面日期未标注 | https://www.mthreads.com/architecture/pinghu | TCE/TME/ATB/ACE/MTLink/LLC与架构主张 |
> 第 244 行：| MTT S3000 产品介绍 | 页面日期未标注 | https://docs.mthreads.com/s3000/s3000-doc-online/introduction/ | S3000详细规格、软件、虚拟化 |
> 第 245 行：| MTT S3000 产品规格书 | 页面日期未标注 | https://docs.mthreads.com/s3000/s3000-doc-online/product_specifications/ | S3000电气规格及15.2 TFLOPS口径 |
> 第 246 行：| 产品白皮书 | 页面日期未标注（历史版本） | https://docs.mthreads.com/cloud-native/cloud-native-doc-online/history_version/v1.9.0/white_paper/ | 苏堤、S1000/S2000/S3000状态和板卡组成 |
> 第 247 行：| MTT S80 | 页面日期未标注 | https://www.mthreads.com/product/S80 | S80规格 |
> 第 248 行：| MTT S70 | 页面日期未标注 | https://www.mthreads.com/product/S70 | S70当前规格 |
> 第 249 行：| MTT S80 产品规格书 | 页面日期未标注 | https://www.mthreads.com/uploaded/product/specification/S80.pdf | S80历史规格口径 |
> 第 250 行：| MTT S70 产品规格书 | 页面日期未标注 | https://www.mthreads.com/uploaded/product/specification/S70.pdf | S70旧规格口径 |
> 第 251 行：| MTT S2000 | 页面日期未标注 | https://www.mthreads.com/product/S2000 | S2000产品页和规格 |
> 第 252 行：| 产品介绍（MTT S50） | 页面日期未标注 | https://docs.mthreads.com/s50/s50-doc-online/introduction/ | S50详细规格 |
> 第 253 行：| MTT S30 / S10 | 页面日期未标注 | https://www.mthreads.com/product/S10 | S30/S10规格和驱动 |
> 第 254 行：| MTT X300 | 页面日期未标注 | https://www.mthreads.com/product/X300 | X300规格与相对性能主张 |
> 第 255 行：| MTT E300 | 页面日期未标注 | https://www.mthreads.com/product/E300 | E300模组规格 |
> 第 256 行：| 产品概述（MTT E300 与 M1000 SoC） | 页面日期未标注 | https://docs.mthreads.com/e300/version-1.5.0/e300-doc-online/product_overview/ | M1000与E300层级、GPU/NPU/统一内存 |
> 第 257 行：| MTT AIBOOK | 页面日期未标注 | https://www.mthreads.com/product/aibook | 长江 SoC设备规格 |
> 第 258 行：| MTT AICUBE | 页面日期未标注 | https://en.mthreads.com/product/aicube | 长江 SoC家庭设备规格 |
> 第 259 行：| MTT SGX5000 | 页面日期未标注 | https://www.mthreads.com/product/SGX5000 | 双路八卡服务器层级 |
> 第 260 行：| MTT KUAE | 页面日期未标注 | https://www.mthreads.com/product/KUAE | 集群方案、Platform、ModelStudio |
> 第 261 行：| 关于我们 | 页面日期未标注 | https://www.mthreads.com/about | 2023-09 S4000/夸娥发布、2023-12智算中心、2024-07万卡方案 |
> 第 262 行：| MTT S4000 训推一体计算卡通过中国信通院 AI 芯片和大模型适配验证 | 2025-05-07 | https://www.mthreads.com/news/244 | 第三方适配/验证状态 |
> 第 263 行：| MT GPU Operator 发布版本信息 | 页面日期未标注 | https://docs.mthreads.com/en/cloud-native/cloud-native-doc-online/releasenote/ | GPU型号、Kubernetes和云原生支持 |
> 第 264 行：| sGPU 使用指南 | 页面日期未标注 | https://docs.mthreads.com/cloud-native/cloud-native-doc-online/user_guide/sgpu_guide/ | sGPU显存切分与容器使用边界 |
> 第 265 行：| AIModule - MTStream | 页面日期未标注 | https://docs.mthreads.com/mtstream/mtstream-doc-online/ | M1000 NPU/GPU边缘推理与零拷贝路径 |

## 补充直接来源链接

1. <https://www.mthreads.com/news/310>
2. <https://mthreads.com/news/312>
3. <https://www.mthreads.com/product/S5000>
4. <https://www.mthreads.com/product/S4000>
5. <https://docs.mthreads.com/driver-linux-server/driver-linux-server-doc-online/MTT_S5000/introduction/>
6. <https://www.mthreads.com/architecture/pinghu>
7. <https://docs.mthreads.com/s3000/s3000-doc-online/introduction/>
8. <https://docs.mthreads.com/s3000/s3000-doc-online/product_specifications/>
9. <https://docs.mthreads.com/cloud-native/cloud-native-doc-online/history_version/v1.9.0/white_paper/>
10. <https://www.mthreads.com/product/S80>
11. <https://www.mthreads.com/product/S70>
12. <https://www.mthreads.com/uploaded/product/specification/S80.pdf>
13. <https://www.mthreads.com/uploaded/product/specification/S70.pdf>
14. <https://www.mthreads.com/product/S2000>
15. <https://docs.mthreads.com/s50/s50-doc-online/introduction/>
16. <https://www.mthreads.com/product/S10>
17. <https://www.mthreads.com/product/X300>
18. <https://www.mthreads.com/product/E300>
