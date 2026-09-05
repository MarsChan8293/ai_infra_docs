# Cerebras Systems — WSE-3

- 研究截止日：2026-09-05
- 资料核验日：2026-09-05
- 产品层级：晶圆级处理器（Wafer-Scale Engine，单片晶圆作为一个处理器对象）
- 综合报告（仅作导航）：[04-cerebras-wse.md](04-cerebras-wse.md)。该报告的截止日早于本页，不替代本页的直接来源核验。
- 证据标记：`官方事实`、`厂商主张`、`独立验证`、`分析推断`、`公开资料未确认`。

## 一句话结论

WSE-3 于 2024-03-13 被 Cerebras 正式公布，公开资料支持它作为 CS-3 的晶圆级处理器进入商业交付和当前服务，且有 Sandia、G42/Condor Galaxy 及云服务层面的采用证据；但这些证据主要证明 CS-3 系统或服务的交付，不能替代 WSE-3 裸片的流片批次、工程样片、独立量产数量、裸片单独出货或芯片级功耗证明。2026 年公布的 WSE-3 Turbo/CS-4 是后续代际，相关系统数字不回填到 WSE-3。[W1][W2][W7][W9]

## 产品层级与对象边界

| 对象 | 本页可以归属的证据 | 不应从中推导的结论 |
|---|---|---|
| **WSE-3** | 一片晶圆级处理器。官方发布材料给出 TSMC 5nm、46,225 mm²、4T 晶体管、900,000 AI 优化核心、44 GB 片上 SRAM 和 125 PFLOPS 峰值/稀疏 FP16 计算口径。[W1][W5] | 这些是处理器/晶圆级指标；不能把 CS-3 机箱功耗、外部 MemoryX 容量或集群吞吐量写成 WSE-3 芯片规格。 |
| **CS-3** | 以一片 WSE-3 为核心的系统，另含供电、液冷、网络、管理和外部 MemoryX 等系统组件。官方对比页给出 15U、最高约 23 kW 等系统口径。[W2][W6] | 23 kW 是 CS-3 系统级峰值，不是 WSE-3 裸片 TDP；15U 也不是芯片封装尺寸。 |
| **MemoryX/集群** | CS-3 可以通过外部 MemoryX 扩展到 TB 级内存，并组成最高 2,048 台 CS-3 的集群。[W1][W2] | 1.5 TB、12 TB、1.2 PB 和 2,048 系统等数字不是片上 SRAM、芯片 I/O 或单片 WSE-3 规模。 |
| **客户部署/机房** | Sandia 的 Kingfisher 是 CS-3 节点部署；G42 的 Condor Galaxy 是由多台 CS-3 组成的集群/数据中心。[W7][W8] | 客户验收的是系统或集群，不能据此宣称客户单独采购或部署了 WSE-3 裸片。 |
| **云服务/实例** | Cerebras Inference 公开提供 WSE-3 支撑的云 API；OpenAI 的公开材料明确写明 GPT-5.6 Sol Ultrafast 运行在 WSE-3。AWS Marketplace listing 也以 WSE/CS-3 SaaS 形式提供入口，但 listing 标注“Deployed on AWS: No”。[W3][W9][W12] | 云 API 或 Marketplace 销售渠道不等于裸片实例 SKU；AWS 与 Cerebras 的 Bedrock 公告是 CS-3 方案的未来部署计划，不能据此确认某个 AWS 区域已经提供 WSE-3 实例。[W11][W12] |
| **WSE-3 Turbo / CS-4** | 2026 年公布的后续 WSE/系统代际。[W15] | WSE-3T/CS-4 的核心、带宽、系统吞吐和路线图数字不回填到 WSE-3。 |

## 生命周期与商业状态

| 生命周期项目 | WSE-3 状态（截至 2026-09-05） | 证据与边界 |
|---|---|---|
| 宣布 | **已确认：2024-03-13** | WSE-3 正式发布；发布材料同时宣布 CS-3 系统，并称将把 WSE-3/CS-3 推向市场。[W1] |
| 流片/工程样片 | **公开资料未确认** | 没有找到 tape-out 日期、工程样片批次、样片编号或晶圆厂验收报告。正式发布和后来出货产品叙述不等于样片时间线。 |
| 送样 | **公开资料未确认** | 没有找到 WSE-3 裸片单独送样或客户评估样片公告；CS-3 试用/部署属于系统层。 |
| 量产 | **厂商材料支持“在产/商业化”，独立批量证据公开资料未确认** | Cerebras 的比较材料称 WSE-3 是在产的大型芯片；制造文章称当前 shipping product 使用 900,000 个 active cores，并将容错设计描述为商业化基础。[W6][W4] 这些是厂商材料，不是独立晶圆产量、良率或批次审计。 |
| 出货 | **CS-3 系统：已由厂商确认向客户出货；WSE-3 裸片单独出货：公开资料未确认** | Cerebras CS-3 页面写明“shipping to customers today/ select customers”；对象是整机系统。不能把系统出货改写为裸片供应。[W2] |
| 客户部署 | **已确认系统级部署** | Sandia 于 2024-10 安装 Kingfisher 的首批四个 CS-3 节点；G42/Condor Galaxy 既有系统已交付，CG3 规划为 64 台 CS-3。[W7][W8] |
| 云/实例可用 | **已确认 WSE-3 支撑的服务可用；独立裸片实例 SKU 公开资料未确认** | Cerebras Inference 于 2024-08-27 公开提供云 API；2026-08-13/27 的 OpenAI 合作材料明确指向 WSE-3，但属于服务层/限量预览。AWS Bedrock 的 CS-3 方案在公告中仍是 coming soon/计划口径。[W3][W9][W10][W11] |
| 路线图 | **后续代际已公布，WSE-3 EOL 未确认** | WSE-3T/CS-4 已在 2026 年公布；Hot Chips 资料把 CS-5 目标放在 2027 年，并继续描述 CS-6 设计目标。没有找到 WSE-3 停产、维护期或最后订货日公告。[W15] |

“CS-3 shipping to customers today”足以支持系统级商业交付，不足以证明 WSE-3 裸片已经作为独立商品出货。类似地，云 API 可用证明服务入口存在，不自动证明每个租户得到固定的 WSE-3 芯片实例。

## 芯片级规格

| 指标 | WSE-3 单片晶圆 | 证据层级与说明 |
|---|---:|---|
| 制程 | TSMC 5nm | WSE-3 发布材料事实。[W1] |
| 晶圆面积 | 46,225 mm² | WSE-3 发布材料和制造文章事实。[W1][W4] |
| 晶体管 | 4T | WSE-3 发布材料事实。[W1] |
| 物理/有效核心 | 970,000 physical；900,000 active AI-optimized | 制造文章明确区分 physical 与当前 shipping product 的 active cores；970,000 是厂商材料口径，未提供独立验证。[W4] |
| 片上 SRAM | 44 GB | WSE-3 发布材料事实。[W1][W5] |
| AI 计算 | 125 PFLOPS | 原始发布材料写作 peak；当前数据手册对 CS-3/WSE-3 对照的 AI compute 使用稀疏 FP16 脚注。不能当作未加限定的稠密 FP16 峰值。[W1][W5] |
| 片上内存带宽 | 21.6 PB/s（官方数据手册）；约 21 PB/s（官方服务/产品文章的四舍五入口径） | 数据手册的精确值用于主规格；旧/服务文章的 21 PB/s 保留为四舍五入，不人为制造两个不同芯片版本。[W3][W5] |
| 片上互连带宽 | 26.7 PB/s（官方数据手册）；约 27 PB/s（官方产品文章的四舍五入口径） | 与上行带宽一样，精确值与四舍五入值分开记录。[W5][W6] |
| 对外 I/O | 1.2 Tbit/s | CS-3 一片 WSE-3 的系统对照指标；公开资料没有把它拆成独立裸片封装接口的电气规格。[W5] |
| I/O 延迟 | 芯片级：**公开资料未确认**；CS-3 对照表为 5 µs | 5 µs 是 CS-3/一片 WSE-3 系统 I/O 路径口径，不当作裸片固有延迟。[W5] |
| 绝对功耗/TDP | **公开资料未确认** | CS-3 最高约 23 kW 是系统级峰值；不能回填到 WSE-3。[W6] |
| 数值格式 | WSE-3 核心为 8-wide FP16 SIMD 的官方架构描述；完整 FP8、INT8、稠密/稀疏各精度吞吐表 **公开资料未确认** | 不用软件栈兼容性替代芯片级格式规格。[W3][W1] |

## 架构与软件证据

### WSE-3 的架构证据

- **数据流执行**：官方 WSE-3 SDK 材料描述二维矩形 PE mesh；每个 PE 有独立的 48 kB 指令/数据本地存储，以 32-bit wavelet 传递数据，数据到达可触发任务执行。这是 WSE-3/CSL 的架构和编程模型证据。[W3]
- **向量计算**：官方 CS-3 材料描述每个核心具备 8-wide FP16 SIMD，并将非线性算术能力作为相对上一代的改进点。[W2]
- **容错与可制造性**：官方制造文章称 WSE-3 设计有 fault tolerance，失效区域可以被禁用；其“970,000 physical / 900,000 active”叙述解释了规格表中两个核心数的来源。93% 的可用硅面积等数字仍属于厂商材料，应标为厂商主张。[W4]
- **软件栈**：官方材料称 SDK 初始支持 WSE-3，CSL 是类似 C 的数据流编程语言，并提供 x86 上的 fabric simulator；WSE-3 发布材料还宣称支持 PyTorch 2.0、MoE/多模态/扩散模型和动态/非结构化稀疏。软件能力不等于 WSE-3 裸片拥有专用算子硬件。[W3][W1]

### 对检索、解码和 KV Cache 的证据边界

WSE-3 的 44 GB SRAM、片上带宽、片上互连和数据流模型可以支持把权重或中间结果留在晶圆内部，这是基于已披露规格的**分析推断**。截至核验日，没有找到 Cerebras 官方资料证明 WSE-3 内置 Search、Top-k、Gather、倒排索引、分页表或 KV Cache 地址引擎。不能把 SDK、编译器、系统级 MemoryX 或云服务 API 的能力写成这类芯片硬件事实。

## 性能与采用证据

| 证据对象 | 结果 | 证据性质与限制 |
|---|---:|---|
| WSE-3 发布指标 | 125 PFLOPS | **官方发布指标**；当前数据手册脚注限定稀疏 FP16 口径。缺少完整测试配置，不能视为独立实测。[W1][W5] |
| CS-3 相对 CS-2 | 在 Llama 2、Falcon 40B、MPT 30B 等真实模型测试中最高约 2× tokens/s | Cerebras 博客的**厂商主张**，对象是 CS-3 系统，测试条件和模型服务配置不完整，不能还原为 WSE-3 裸片加速比。[W2] |
| CS-3 系统形态 | 15U、最高约 23 kW；外部 MemoryX 可扩展到 TB 级 | **系统级官方事实/产品口径**，不是芯片功耗或芯片外部存储规格。[W6][W1] |
| 独立云服务观测 | Artificial Analysis 的 GPT-OSS-120B provider 页面在 10,000 input tokens 工作负载下记录 Cerebras provider 约 1,793 output tok/s 的中位数；统计窗口、端点和模型服务配置以该页面定义为准 | **第三方服务层数据**，不是对 WSE-3 裸片的独立验证；页面不能确认底层是 WSE-3、WSE-3T 还是其他 Cerebras 系统。[W14] |
| WSE-3 明确的服务采用 | OpenAI 材料称 GPT-5.6 Sol Ultrafast 在 Cerebras WSE-3 上运行，最高约 750 output tok/s；2024 年 Cerebras Inference 公开提供 WSE-3 支撑的 API | **厂商/合作方服务层主张**，2026 年材料注明限量预览；吞吐受模型、上下文和服务配置影响，不能当作芯片裸测。[W3][W9][W10] |
| 客户系统部署 | Sandia Kingfisher 首批四个 CS-3 节点于 2024-10 安装；G42/Condor Galaxy 使用多台 CS-3 | **官方客户/部署证据，系统级**。它证明 WSE-3 通过 CS-3 进入客户系统，不证明裸片独立交付。[W7][W8] |

## 未确认项、冲突与使用边界

1. **21 vs 21.6 PB/s、27 vs 26.7 PB/s**：前者来自官方产品/服务文章的四舍五入，后者来自当前 CS-4 数据手册的 CS-3 一片对照表。本页主规格使用精确值，并保留约值来源，不把它们解释成不同 WSE-3 型号。[W3][W5][W6]
2. **125 PFLOPS 的精度口径**：WSE-3 发布稿使用 peak 表述，当前数据手册脚注使用 sparse FP16。没有完整 dense/sparse、batch、频率和功耗测试矩阵，因此正文不扩展为稠密峰值。[W1][W5]
3. **23 kW、15U、MemoryX 容量、5 µs 和集群规模**都是 CS-3 系统/集群层数字；本页没有把它们写入 WSE-3 的裸片功耗、封装面积、片上存储、芯片延迟或芯片数量。[W1][W2][W5][W6]
4. **量产状态**：官方资料足以支持“CS-3/WSE-3 已商业化并有当前出货产品”的厂商证据，但没有公开独立的 WSE-3 晶圆产量、良率、批次、代工验证或裸片采购记录。量产表格因此没有写成独立确认的“已量产”。[W2][W4][W6]
5. **日期口径**：WSE-3 发布页的页面元数据与正文 dateline 存在 2024-03-11/2024-03-13 的显示差异；本页按正式新闻稿正文 dateline 记录 2024-03-13，并在来源中保留直接页面。[W1]
6. **WSE-3T/CS-4 不回填**：后续代际的芯片、系统和路线图资料只用于说明产品代际边界，不用于补齐 WSE-3 的核心、带宽、功耗、吞吐或云实例状态。[W15]

## 直接来源

1. [Cerebras Announces Third-Generation Wafer-Scale Engine](https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine) — 主体：Cerebras Systems；发布日期：2024-03-13（页面元数据另显示 2024-03-11，正文 dateline 为 2024-03-13）；核验日期：2026-09-05。WSE-3 芯片规格、CS-3 系统、MemoryX 和集群口径。
2. [Cerebras CS3](https://www.cerebras.ai/blog/cerebras-cs3) — 主体：Cerebras Systems；发布日期：2024-03-12；核验日期：2026-09-05。CS-3 shipping、系统性能、MemoryX、客户和云服务说明。
3. [Introducing Cerebras Inference: AI at Instant Speed](https://www.cerebras.ai/blog/introducing-cerebras-inference-ai-at-instant-speed) — 主体：Cerebras Systems；发布日期：2024-08-27；核验日期：2026-09-05。WSE-3 支撑的公开云 API 与约 21 PB/s 服务口径。
4. [Supercharge Your HPC Research with the Cerebras SDK](https://www.cerebras.ai/blog/supercharge-your-hpc-research-with-the-cerebras-sdk) — 主体：Cerebras Systems；发布日期：2024-05-01；核验日期：2026-09-05。WSE-3 PE mesh、48 kB 本地存储、wavelet、FP16 SIMD 和 CSL/SDK。
5. [100x Defect Tolerance: How Cerebras Solved the Yield Problem](https://www.cerebras.ai/blog/100x-defect-tolerance-how-cerebras-solved-the-yield-problem) — 主体：Cerebras Systems；发布日期：2025-01-13；核验日期：2026-09-05。970,000 physical/900,000 active cores、容错与制造主张。
6. [Cerebras CS-3 vs NVIDIA B200: 2024 AI Accelerators Compared](https://www.cerebras.ai/blog/cerebras-cs-3-vs-nvidia-b200-2024-ai-accelerators-compared) — 主体：Cerebras Systems；发布日期：2024-04-12；核验日期：2026-09-05。CS-3/WSE-3 对比、约 27 PB/s 及系统功耗/机架口径。
7. [Sandia Deploys Cutting-Edge Cerebras CS-3 Testbed for AI Workloads](https://www.cerebras.ai/press-release/sandia-deploys-cutting-edge-cerebras-cs-3-testbed-for-ai-workloads) — 主体：Sandia National Laboratories、Cerebras Systems；发布日期：2024-11-13；核验日期：2026-09-05。Kingfisher 首批 CS-3 节点部署。
8. [Cerebras and G42 Announce Condor Galaxy 3](https://www.cerebras.ai/press-release/cerebras-g42-announce-condor-galaxy-3) — 主体：Cerebras Systems、G42；发布日期：2024-03-13；核验日期：2026-09-05。CG3 的 64 台 CS-3 规划与既有系统交付口径。
9. [Cerebras Announces Six New AI Datacenters](https://www.cerebras.ai/press-release/cerebras-announces-six-new-ai-datacenters-across-north-america-and-europe-to-deliver-industry-s) — 主体：Cerebras Systems；发布日期：2025-03-11；核验日期：2026-09-05。多数据中心、CS-3 系统和云/客户采用背景。
10. [How Cerebras Serves GPT-5.6 Sol at up to 750 Tokens per Second](https://www.cerebras.ai/blog/how-cerebras-serves-gpt-5-6-sol-at-up-to-750-tokens-per-second) — 主体：Cerebras Systems；发布日期：2026-08-27；核验日期：2026-09-05。明确把该服务绑定到 WSE-3，并说明多 CS-3 系统的服务边界。
11. [Accelerating GPT-5.6 Sol Ultrafast with OpenAI](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai) — 主体：Cerebras Systems、OpenAI；发布日期：2026-08-13；核验日期：2026-09-05。WSE 架构、44 GB SRAM、限量预览和服务吞吐。
12. [AWS and Cerebras Collaboration Aims to Set New Standard for AI Inference](https://investors.cerebras.ai/news-releases/news-release-details/aws-and-cerebras-collaboration-aims-set-new-standard-ai) — 主体：AWS、Cerebras Systems；发布日期：2026-03-13；核验日期：2026-09-05。CS-3/Trainium/Bedrock 方案及未来时态。
13. [Cerebras Fast Inference Cloud](https://aws.amazon.com/marketplace/pp/prodview-ph4bdvplhhz3o) — 主体：Cerebras Systems、AWS Marketplace；发布日期：公开资料未确认（动态 listing）；核验日期：2026-09-05。WSE/CS-3 SaaS 入口及“Deployed on AWS: No”的对象边界。
14. [GPT-OSS-120B Providers](https://artificialanalysis.ai/models/gpt-oss-120b/providers) — 主体：Artificial Analysis；发布日期：公开资料未确认（动态基准页）；核验日期：2026-09-05。第三方 provider 层吞吐数据和统计口径，不能绑定到裸片。
15. [Ultrafast Frontier Inference: Cerebras Deep Dive at Hot Chips 2026](https://www.cerebras.ai/blog/ultrafast-frontier-inference-cerebras-deep-dive-at-hot-chips-2026) — 主体：Cerebras Systems；发布日期：2026-08-25；核验日期：2026-09-05。WSE-3T/CS-4 后续代际路线图，用于边界而非 WSE-3 芯片规格。
