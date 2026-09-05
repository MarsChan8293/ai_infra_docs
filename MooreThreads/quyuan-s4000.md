# Moore Threads / 摩尔线程 — 曲院 / MTT S4000

- 拆分日期：2026-09-02
- 产品层级：GPU 芯片/智算加速卡
- 综合报告：[moore-threads-chips-2026-09-01.md](./moore-threads-chips-2026-09-01.md)
- 文件性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容逐行摘录综合报告，保留原报告中的状态、数字、证据等级和未知项。

> 第 10 行：
> 第 11 行：截至 2026-09-01，摩尔线程公开产品已经形成从第四代“平湖”架构 PH100/MTT S5000、第三代“曲院”/MTT S4000、第一代 MUSA 的“春晓”/MTT S3000、S80、S70，到“苏堤”/MTT S1000、S2000，再到长江 M1000 SoC、MTT E300 边缘模组和 AIBOOK/AICUBE 端侧设备的全栈矩阵。技术路线的核心差异在于全功能 GPU、原生 FP8、张量访存引擎 TME、异步通信引擎 ACE、MTLink Scale-up 和 MUSA 软件生态；但最新产品的公开页面仍没有完整披露芯片面积、制程、晶体管数、TDP、流片/送样/量产/出货与客户部署时间线，不能用厂商性能宣传或服务器配置替代这些状态证据。
> 第 12 行：
> 第 17 行：| 平湖 / PH100，第四代 MUSA | MTT S5000 | 单卡智算加速卡；另见 SGX5000/KUAE 系统 | 2026-05-18 产品发布会公开；2026-05-26 公布通过国家安全可靠测评。量产、出货、客户部署、公有云可用时间未由当前公开一手资料确认。 |
> 第 18 行：| 曲院，第三代 MUSA | MTT S4000 | 单卡智算加速卡 | 2023-09 秋季发布会公开；2025-05-07 获中国信通院 AI 芯片和大模型适配验证。规模化系统部署有官方案例，但单卡量产/出货日期未单独确认。 |
> 第 19 行：| 春晓，第一代 MUSA | MTT S3000、MTT S80、MTT S70 | 服务器卡、游戏显卡 | 2022-11 公开春晓芯片；S3000 官方称为基于春晓的第一款服务器 GPU。三款产品有公开规格；不同页面的 S3000/S70 FP32 数字存在口径差异。 |
> 第 31 行：
> 第 32 行：### 主力数据中心产品：MTT S4000 / 曲院
> 第 33 行：
> 第 34 行：2023-09 发布的曲院和 MTT S4000 是摩尔线程此前面向大模型训练、微调和推理的主力数据中心路线。它同时保留图形、编解码、8K HDR 显示、科学计算和虚拟化能力；2023-12 夸娥智算中心揭幕说明了系统级落地，但不能反推每一批 S4000 的出货时间。
> 第 35 行：
> 第 50 行：| PH100 / S5000 | 2026-05-18 产品发布会；2026-05-26 安全可靠测评公告 | 公开资料未确认 | 公开资料未确认 | 官方页面给出 SiliconFlow 测试方案、KUAE 集成方案和“联系我们”，但公开资料未确认公有云实例或普遍客户部署 | 测评通过不等同于量产 |
> 第 51 行：| 曲院 / S4000 | 2023-09 秋季发布会 | 公开资料未确认 | 公开资料未确认 | 2023-12 夸娥智算中心正式揭幕；2025-05-07 中国信通院适配验证 | 系统落地与单卡出货需分开 |
> 第 52 行：| 春晓 / S3000 | 2022-11 芯片公开；S3000 产品页当前可见 | 公开资料未确认 | 历史白皮书曾称“即将进入量产阶段”，当前量产日期未确认 | 服务器/OEM 适配有官方说明；公有云可用未确认 | 页面称 S3000 为首款春晓服务器 GPU |
> 第 77 行：
> 第 78 行：### MTT S4000：单卡层级
> 第 79 行：
> 第 113 行：        ↓
> 第 114 行：MTT S5000/S4000/S3000/S2000/S1000/S80/S70/S50/S30/S10/X300/E300（板卡或模组）
> 第 115 行：        ↓
> 第 145 行：
> 第 146 行：S5000公开了 80 GB、1.6 TB/s 单卡显存和 60 MB LLC；S4000公开了 48 GB、768 GB/s；S3000公开了 32 GB GDDR6、448 GB/s。S80/S70/S50等为 GDDR6 路线，E300/AIBOOK/AICUBE为 LPDDR统一内存路线。对于 PH100，当前公开页面没有明确标注显存介质类型，不能自行写成 HBM。
> 第 147 行：
> 第 154 行：- MUSA SDK：指令集架构、编程模型、驱动、运行时、算子库、通信库、数学库和工具链。
> 第 155 行：- 迁移与框架：MUSIFY 用于 CUDA 程序迁移；服务器文档明确列出 PyTorch、Megatron-LM、vLLM、SGLang，S4000文档还列出 DeepSpeed、Colossal-AI；较早 S3000 文档列出 PyTorch、TensorFlow、PaddlePaddle。
> 第 156 行：- 分析工具：Moore Perf Compute、Moore Perf System、mthreads-gmi；当前服务器文档可见 Driver/MUSA SDK 5.2.0 安装路径。
> 第 164 行：- S5000：官方定位大模型预训练、微调、推理、AI4S和高性能计算；页面给出 Llama3-70B、DeepSeek-236B、Wan2.1、长上下文 Prefill、PD 分离推理等示例。
> 第 165 行：- S4000：面向千亿参数规模训练、微调、推理，同时适合图形、视频、科学计算和虚拟化。
> 第 166 行：- S3000/S2000/S1000：数据中心云桌面、云渲染、云视频、云手机、数字孪生和通用 AI；S2000/S1000的历史资料强调容器化资源调用。
> 第 180 行：
> 第 181 行：本轮实际打开的官方资料中，未找到可独立复核的 MLPerf 公开成绩或完整第三方端到端性能报告。2025-05-07 中国信通院对 S4000 的“AI芯片和大模型适配验证”属于适配/验证证据，不应改写为独立性能领先证明。S5000页面提到“第三方实测”通信带宽，但当前公开页面未给出独立机构报告的完整出处，因此仍标为厂商页面转述。
> 第 182 行：
> 第 202 行：- 产品页明确列出型号、产品定位和公开规格。
> 第 203 行：- S5000与 PH100、平湖、第四代 MUSA 的关联，以及 S4000与曲院、S3000/S80/S70与春晓、S1000/S2000与苏堤的关联，有官方页面/文档支撑。
> 第 204 行：- MTT E300 是模组，M1000 是内部 SoC；AIBOOK/AICUBE是长江 SoC设备；SGX5000是双路八卡服务器；KUAE是软硬一体系统方案。
> 第 210 行：- 平湖 FP8 GEMM、Flash Attention、ACE收益和 MTLink带宽效率数字。
> 第 211 行：- X300 相对 S50 的图形倍率，以及 S4000/KUAE 的规模化集群能力。
> 第 212 行：
> 第 224 行：4. S5000：当前公开资料没有完整 TDP、芯片制程、晶体管数、芯片面积、显存介质/颗粒、FP8至FP64逐项峰值表、量产日期、出货量、客户名单、公有云 SKU和停产信息。
> 第 225 行：5. S4000：没有在本轮官方资料中找到流片、量产和出货的单独日期；夸娥智算中心揭幕只能证明系统级落地。
> 第 226 行：6. S3000：历史白皮书“即将进入量产阶段”没有可用的当前量产日期；不要把旧计划写成已完成量产。
> 第 240 行：| MTT S5000｜训推一体全功能 GPU 智算卡 | 页面日期未标注 | https://www.mthreads.com/product/S5000 | S5000定位、性能主张、模型/推理条件 |
> 第 241 行：| MTT S4000｜大模型智算加速卡 | 页面日期未标注 | https://www.mthreads.com/product/S4000 | S4000定位和产品层级 |
> 第 242 行：| MTT S4000/S5000 产品介绍 | 页面日期未标注 | https://docs.mthreads.com/driver-linux-server/driver-linux-server-doc-online/MTT_S5000/introduction/ | S4000/S5000单卡规格、MTLink、软件 |
> 第 243 行：| 平湖第四代 GPU 架构 | 页面日期未标注 | https://www.mthreads.com/architecture/pinghu | TCE/TME/ATB/ACE/MTLink/LLC与架构主张 |
> 第 260 行：| MTT KUAE | 页面日期未标注 | https://www.mthreads.com/product/KUAE | 集群方案、Platform、ModelStudio |
> 第 261 行：| 关于我们 | 页面日期未标注 | https://www.mthreads.com/about | 2023-09 S4000/夸娥发布、2023-12智算中心、2024-07万卡方案 |
> 第 262 行：| MTT S4000 训推一体计算卡通过中国信通院 AI 芯片和大模型适配验证 | 2025-05-07 | https://www.mthreads.com/news/244 | 第三方适配/验证状态 |
> 第 263 行：| MT GPU Operator 发布版本信息 | 页面日期未标注 | https://docs.mthreads.com/en/cloud-native/cloud-native-doc-online/releasenote/ | GPU型号、Kubernetes和云原生支持 |

## 直接来源链接

1. <https://www.mthreads.com/product/S5000>
2. <https://www.mthreads.com/product/S4000>
3. <https://docs.mthreads.com/driver-linux-server/driver-linux-server-doc-online/MTT_S5000/introduction/>
4. <https://www.mthreads.com/architecture/pinghu>
5. <https://www.mthreads.com/product/KUAE>
6. <https://www.mthreads.com/about>
7. <https://www.mthreads.com/news/244>
8. <https://docs.mthreads.com/en/cloud-native/cloud-native-doc-online/releasenote/>

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
3. <https://docs.mthreads.com/s3000/s3000-doc-online/introduction/>
4. <https://docs.mthreads.com/s3000/s3000-doc-online/product_specifications/>
5. <https://docs.mthreads.com/cloud-native/cloud-native-doc-online/history_version/v1.9.0/white_paper/>
6. <https://www.mthreads.com/product/S80>
7. <https://www.mthreads.com/product/S70>
8. <https://www.mthreads.com/uploaded/product/specification/S80.pdf>
9. <https://www.mthreads.com/uploaded/product/specification/S70.pdf>
10. <https://www.mthreads.com/product/S2000>
11. <https://docs.mthreads.com/s50/s50-doc-online/introduction/>
12. <https://www.mthreads.com/product/S10>
13. <https://www.mthreads.com/product/X300>
14. <https://www.mthreads.com/product/E300>
15. <https://docs.mthreads.com/e300/version-1.5.0/e300-doc-online/product_overview/>
16. <https://www.mthreads.com/product/aibook>
17. <https://en.mthreads.com/product/aicube>
18. <https://www.mthreads.com/product/SGX5000>
19. <https://docs.mthreads.com/cloud-native/cloud-native-doc-online/user_guide/sgpu_guide/>
20. <https://docs.mthreads.com/mtstream/mtstream-doc-online/>
