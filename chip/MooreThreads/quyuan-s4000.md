# Moore Threads / 摩尔线程 — 曲院 / MTT S4000

- 研究截止日：2026-09-05
- 核验日期：2026-09-05
- 产品层级：GPU 芯片/智算加速卡
- 厂商总览：[摩尔线程](./摩尔线程-概览.md) · [[摩尔线程-概览|图谱总览]]
- 页面性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容按对象边界重排自现有综合报告，并以本页直接来源清单核验；不能由相邻产品层级推导的项目保留为“公开资料未确认”。

截至 2026-09-01，摩尔线程公开产品已经形成从第四代“平湖”架构 PH100/MTT S5000、第三代“曲院”/MTT S4000、第一代 MUSA 的“春晓”/MTT S3000、S80、S70，到“苏堤”/MTT S1000、S2000，再到长江 M1000 SoC、MTT E300 边缘模组和 AIBOOK/AICUBE 端侧设备的全栈矩阵。技术路线的核心差异在于全功能 GPU、原生 FP8、张量访存引擎 TME、异步通信引擎 ACE、MTLink Scale-up 和 MUSA 软件生态；但最新产品的公开页面仍没有完整披露芯片面积、制程、晶体管数、TDP、流片/送样/量产/出货与客户部署时间线，不能用厂商性能宣传或服务器配置替代这些状态证据。

### 主力数据中心产品：MTT S4000 / 曲院

2023-09 发布的曲院和 MTT S4000 是摩尔线程此前面向大模型训练、微调和推理的主力数据中心路线。它同时保留图形、编解码、8K HDR 显示、科学计算和虚拟化能力；2023-12 夸娥智算中心揭幕说明了系统级落地，但不能反推每一批 S4000 的出货时间。

### MTT S4000：单卡层级

        ↓
MTT S5000/S4000/S3000/S2000/S1000/S80/S70/S50/S30/S10/X300/E300（板卡或模组）
        ↓

S5000公开了 80 GB、1.6 TB/s 单卡显存和 60 MB LLC；S4000公开了 48 GB、768 GB/s；S3000公开了 32 GB GDDR6、448 GB/s。S80/S70/S50等为 GDDR6 路线，E300/AIBOOK/AICUBE为 LPDDR统一内存路线。对于 PH100，当前公开页面没有明确标注显存介质类型，不能自行写成 HBM。

- MUSA SDK：指令集架构、编程模型、驱动、运行时、算子库、通信库、数学库和工具链。
- 迁移与框架：MUSIFY 用于 CUDA 程序迁移；服务器文档明确列出 PyTorch、Megatron-LM、vLLM、SGLang，S4000文档还列出 DeepSpeed、Colossal-AI；较早 S3000 文档列出 PyTorch、TensorFlow、PaddlePaddle。
- 分析工具：Moore Perf Compute、Moore Perf System、mthreads-gmi；当前服务器文档可见 Driver/MUSA SDK 5.2.0 安装路径。
- S5000：官方定位大模型预训练、微调、推理、AI4S和高性能计算；页面给出 Llama3-70B、DeepSeek-236B、Wan2.1、长上下文 Prefill、PD 分离推理等示例。
- S4000：面向千亿参数规模训练、微调、推理，同时适合图形、视频、科学计算和虚拟化。
- S3000/S2000/S1000：数据中心云桌面、云渲染、云视频、云手机、数字孪生和通用 AI；S2000/S1000的历史资料强调容器化资源调用。

本轮实际打开的官方资料中，未找到可独立复核的 MLPerf 公开成绩或完整第三方端到端性能报告。2025-05-07 中国信通院对 S4000 的“AI芯片和大模型适配验证”属于适配/验证证据，不应改写为独立性能领先证明。S5000页面提到“第三方实测”通信带宽，但当前公开页面未给出独立机构报告的完整出处，因此仍标为厂商页面转述。

- 产品页明确列出型号、产品定位和公开规格。
- S5000与 PH100、平湖、第四代 MUSA 的关联，以及 S4000与曲院、S3000/S80/S70与春晓、S1000/S2000与苏堤的关联，有官方页面/文档支撑。
- MTT E300 是模组，M1000 是内部 SoC；AIBOOK/AICUBE是长江 SoC设备；SGX5000是双路八卡服务器；KUAE是软硬一体系统方案。
- 平湖 FP8 GEMM、Flash Attention、ACE收益和 MTLink带宽效率数字。
- X300 相对 S50 的图形倍率，以及 S4000/KUAE 的规模化集群能力。

4. S5000：当前公开资料没有完整 TDP、芯片制程、晶体管数、芯片面积、显存介质/颗粒、FP8至FP64逐项峰值表、量产日期、出货量、客户名单、公有云 SKU和停产信息。
5. S4000：没有在本轮官方资料中找到流片、量产和出货的单独日期；夸娥智算中心揭幕只能证明系统级落地。
6. S3000：历史白皮书“即将进入量产阶段”没有可用的当前量产日期；不要把旧计划写成已完成量产。

## 关联证据与规格

本节保留与本对象相关的关联规格和生命周期证据；其中的卡、模块、服务器、机架、集群或云数据保持原产品层级，不能回填为芯片规格。

| 芯片/架构家族 | 公开关联产品 | 产品层级 | 公开定位与状态边界 |
| --- | --- | --- | --- |
| 平湖 / PH100，第四代 MUSA | MTT S5000 | 单卡智算加速卡；另见 SGX5000/KUAE 系统 | 2026-05-18 产品发布会公开；2026-05-26 公布通过国家安全可靠测评。量产、出货、客户部署、公有云可用时间未由当前公开一手资料确认。 |
| 曲院，第三代 MUSA | MTT S4000 | 单卡智算加速卡 | 2023-09 秋季发布会公开；2025-05-07 获中国信通院 AI 芯片和大模型适配验证。规模化系统部署有官方案例，但单卡量产/出货日期未单独确认。 |
| 春晓，第一代 MUSA | MTT S3000、MTT S80、MTT S70 | 服务器卡、游戏显卡 | 2022-11 公开春晓芯片；S3000 官方称为基于春晓的第一款服务器 GPU。三款产品有公开规格；不同页面的 S3000/S70 FP32 数字存在口径差异。 |
| 苏堤 | MTT S1000、MTT S2000 | 服务器卡 | 官方历史白皮书称 S1000、S2000 已量产出货；S2000 是两颗苏堤芯片通过板载 PCIe Switch 组成，S1000 是单芯片。当前产品中心不再突出 S1000，停售日期未确认。 |
| 未公开命名或未建立公开映射 | MTT X300、MTT S50、MTT S30、MTT S10 | 专业显卡、桌面显卡 | 产品页提供板卡规格和驱动支持；芯片名称、流片/量产/出货日期公开资料未确认。 |
| 长江 / M1000 | MTT E300、AIBOOK、AICUBE、AIModule | SoC、AI 模组、算力本、家庭 AI 中枢 | M1000 是芯片，E300 是模组，AIBOOK/AICUBE 是整机设备。三者不能把 50 TOPS 或统一内存数字写成单独 NPU 或 GPU 的规格。 |

| 产品/家族 | 首次披露或正式发布 | 流片/送样 | 量产/出货 | 客户部署/云端可用 | 备注 |
| --- | --- | --- | --- | --- | --- |
| PH100 / S5000 | 2026-05-18 产品发布会；2026-05-26 安全可靠测评公告 | 公开资料未确认 | 公开资料未确认 | 官方页面给出 SiliconFlow 测试方案、KUAE 集成方案和“联系我们”，但公开资料未确认公有云实例或普遍客户部署 | 测评通过不等同于量产 |
| 曲院 / S4000 | 2023-09 秋季发布会 | 公开资料未确认 | 公开资料未确认 | 2023-12 夸娥智算中心正式揭幕；2025-05-07 中国信通院适配验证 | 系统落地与单卡出货需分开 |
| 春晓 / S3000 | 2022-11 芯片公开；S3000 产品页当前可见 | 公开资料未确认 | 历史白皮书曾称“即将进入量产阶段”，当前量产日期未确认 | 服务器/OEM 适配有官方说明；公有云可用未确认 | 页面称 S3000 为首款春晓服务器 GPU |
| 苏堤 / S1000、S2000 | 历史产品白皮书披露 | 公开资料未确认 | 历史白皮书明确称“量产出货状态” | 容器化、Docker、Kubernetes 生态有文档；公有云可用未确认 | 白皮书页面日期未标注，具体量产日期未确认 |
| S80、S70 | 当前官网产品页可购买/下载驱动；具体首次发布日未在当前页标注 | 公开资料未确认 | 公开资料未确认 | “智娱摩方”整机方案使用 S80/S70；公有云可用未确认 | 不以购买入口推断生产批次 |
| X300、S50、S30、S10 | 当前官网产品页和驱动文档可见；具体首次发布日未在当前页标注 | 公开资料未确认 | 公开资料未确认 | 驱动、操作系统镜像和桌面场景有公开支持；云端可用未确认 | 产品页未建立芯片型号映射 |
| M1000 / E300 | E300 产品页和开发者文档可见 | 公开资料未确认 | 公开资料未确认 | E300定位客户集成；AIModule 文档给出边缘视频推理路径；没有公开客户名单/出货数量 | E300是模组，M1000是内部 SoC |
| AIBOOK、AICUBE、SGX5000、KUAE | AIBOOK 产品页有“立即购买”；AICUBE 产品页有“Buy Now”；SGX5000/KUAE为系统产品 | 适用于内部芯片的流片状态：公开资料未确认 | 设备/服务器的具体生产批次公开资料未确认 | KUAE产品页称“30天建设集群”、支持万卡级目标；不是公有云可用证明 | 服务器/集群数字不得回填到单卡 |

| 标题 | 发布/更新时间 | 直接 URL | 用途 |
| --- | --- | --- | --- |
| 词元时代，万物智能｜摩尔线程 2026 产品发布会：打造全场景 AI 算力基石 | 2026-05-18 | https://www.mthreads.com/news/310 | S5000产品发布事件 |
| 喜报｜摩尔线程 MTT S5000（PH100 芯片）通过国家《安全可靠测评》 | 2026-05-26 | https://mthreads.com/news/312 | PH100安全测评状态 |
| MTT S5000｜训推一体全功能 GPU 智算卡 | 页面日期未标注 | https://www.mthreads.com/product/S5000 | S5000定位、性能主张、模型/推理条件 |
| MTT S4000｜大模型智算加速卡 | 页面日期未标注 | https://www.mthreads.com/product/S4000 | S4000定位和产品层级 |
| MTT S4000/S5000 产品介绍 | 页面日期未标注 | https://docs.mthreads.com/driver-linux-server/driver-linux-server-doc-online/MTT_S5000/introduction/ | S4000/S5000单卡规格、MTLink、软件 |
| 平湖第四代 GPU 架构 | 页面日期未标注 | https://www.mthreads.com/architecture/pinghu | TCE/TME/ATB/ACE/MTLink/LLC与架构主张 |
| MTT S3000 产品介绍 | 页面日期未标注 | https://docs.mthreads.com/s3000/s3000-doc-online/introduction/ | S3000详细规格、软件、虚拟化 |
| MTT S3000 产品规格书 | 页面日期未标注 | https://docs.mthreads.com/s3000/s3000-doc-online/product_specifications/ | S3000电气规格及15.2 TFLOPS口径 |
| 产品白皮书 | 页面日期未标注（历史版本） | https://docs.mthreads.com/cloud-native/cloud-native-doc-online/history_version/v1.9.0/white_paper/ | 苏堤、S1000/S2000/S3000状态和板卡组成 |
| MTT S80 | 页面日期未标注 | https://www.mthreads.com/product/S80 | S80规格 |
| MTT S70 | 页面日期未标注 | https://www.mthreads.com/product/S70 | S70当前规格 |
| MTT S80 产品规格书 | 页面日期未标注 | https://www.mthreads.com/uploaded/product/specification/S80.pdf | S80历史规格口径 |
| MTT S70 产品规格书 | 页面日期未标注 | https://www.mthreads.com/uploaded/product/specification/S70.pdf | S70旧规格口径 |
| MTT S2000 | 页面日期未标注 | https://www.mthreads.com/product/S2000 | S2000产品页和规格 |
| 产品介绍（MTT S50） | 页面日期未标注 | https://docs.mthreads.com/s50/s50-doc-online/introduction/ | S50详细规格 |
| MTT S30 / S10 | 页面日期未标注 | https://www.mthreads.com/product/S10 | S30/S10规格和驱动 |
| MTT X300 | 页面日期未标注 | https://www.mthreads.com/product/X300 | X300规格与相对性能主张 |
| MTT E300 | 页面日期未标注 | https://www.mthreads.com/product/E300 | E300模组规格 |
| 产品概述（MTT E300 与 M1000 SoC） | 页面日期未标注 | https://docs.mthreads.com/e300/version-1.5.0/e300-doc-online/product_overview/ | M1000与E300层级、GPU/NPU/统一内存 |
| MTT AIBOOK | 页面日期未标注 | https://www.mthreads.com/product/aibook | 长江 SoC设备规格 |
| MTT AICUBE | 页面日期未标注 | https://en.mthreads.com/product/aicube | 长江 SoC家庭设备规格 |
| MTT SGX5000 | 页面日期未标注 | https://www.mthreads.com/product/SGX5000 | 双路八卡服务器层级 |
| MTT KUAE | 页面日期未标注 | https://www.mthreads.com/product/KUAE | 集群方案、Platform、ModelStudio |
| 关于我们 | 页面日期未标注 | https://www.mthreads.com/about | 2023-09 S4000/夸娥发布、2023-12智算中心、2024-07万卡方案 |
| MTT S4000 训推一体计算卡通过中国信通院 AI 芯片和大模型适配验证 | 2025-05-07 | https://www.mthreads.com/news/244 | 第三方适配/验证状态 |
| MT GPU Operator 发布版本信息 | 页面日期未标注 | https://docs.mthreads.com/en/cloud-native/cloud-native-doc-online/releasenote/ | GPU型号、Kubernetes和云原生支持 |
| sGPU 使用指南 | 页面日期未标注 | https://docs.mthreads.com/cloud-native/cloud-native-doc-online/user_guide/sgpu_guide/ | sGPU显存切分与容器使用边界 |
| AIModule - MTStream | 页面日期未标注 | https://docs.mthreads.com/mtstream/mtstream-doc-online/ | M1000 NPU/GPU边缘推理与零拷贝路径 |

## 直接来源

1. <https://www.mthreads.com/product/S5000>；核验日期：2026-09-05。
2. <https://www.mthreads.com/product/S4000>；核验日期：2026-09-05。
3. <https://docs.mthreads.com/driver-linux-server/driver-linux-server-doc-online/MTT_S5000/introduction/>；核验日期：2026-09-05。
4. <https://www.mthreads.com/architecture/pinghu>；核验日期：2026-09-05。
5. <https://www.mthreads.com/product/KUAE>；核验日期：2026-09-05。
6. <https://www.mthreads.com/about>；核验日期：2026-09-05。
7. <https://www.mthreads.com/news/244>；核验日期：2026-09-05。
8. <https://docs.mthreads.com/en/cloud-native/cloud-native-doc-online/releasenote/>；核验日期：2026-09-05。
9. <https://www.mthreads.com/news/310>；核验日期：2026-09-05。
10. <https://mthreads.com/news/312>；核验日期：2026-09-05。
11. <https://docs.mthreads.com/s3000/s3000-doc-online/introduction/>；核验日期：2026-09-05。
12. <https://docs.mthreads.com/s3000/s3000-doc-online/product_specifications/>；核验日期：2026-09-05。
13. <https://docs.mthreads.com/cloud-native/cloud-native-doc-online/history_version/v1.9.0/white_paper/>；核验日期：2026-09-05。
14. <https://www.mthreads.com/product/S80>；核验日期：2026-09-05。
15. <https://www.mthreads.com/product/S70>；核验日期：2026-09-05。
16. <https://www.mthreads.com/uploaded/product/specification/S80.pdf>；核验日期：2026-09-05。
17. <https://www.mthreads.com/uploaded/product/specification/S70.pdf>；核验日期：2026-09-05。
18. <https://www.mthreads.com/product/S2000>；核验日期：2026-09-05。
19. <https://docs.mthreads.com/s50/s50-doc-online/introduction/>；核验日期：2026-09-05。
20. <https://www.mthreads.com/product/S10>；核验日期：2026-09-05。
21. <https://www.mthreads.com/product/X300>；核验日期：2026-09-05。
22. <https://www.mthreads.com/product/E300>；核验日期：2026-09-05。
23. <https://docs.mthreads.com/e300/version-1.5.0/e300-doc-online/product_overview/>；核验日期：2026-09-05。
24. <https://www.mthreads.com/product/aibook>；核验日期：2026-09-05。
25. <https://en.mthreads.com/product/aicube>；核验日期：2026-09-05。
26. <https://www.mthreads.com/product/SGX5000>；核验日期：2026-09-05。
27. <https://docs.mthreads.com/cloud-native/cloud-native-doc-online/user_guide/sgpu_guide/>；核验日期：2026-09-05。
28. <https://docs.mthreads.com/mtstream/mtstream-doc-online/>；核验日期：2026-09-05。

## 证据边界

- 芯片、封装、卡/模组、服务器/机架、集群、软件和云服务按来源原层级记录；系统、卡、模块或集群数据不自动回填为芯片规格。
- “宣布、流片/工程样片、送样、量产、出货、客户部署、云/实例可用、路线图、停产”分别判断；没有直接证据的阶段写为“公开资料未确认”。
- 官方发布、产品页或软件支持不能单独证明量产、出货或独立性能；厂商主张、独立验证和分析推断不混写。
- 本页是基于现有综合报告和直接来源的证据重排页；引用以文末直接 URL 为准，不再使用综合报告行号作为外部引用。
