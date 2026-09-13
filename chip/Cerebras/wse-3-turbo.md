# Cerebras Systems — WSE-3 Turbo / WSE-3T

- 研究截止日：2026-09-05
- 资料核验日：2026-09-05
- 产品层级：晶圆级处理器（Wafer-Scale Engine，单片晶圆作为一个处理器对象）
- 厂商总览：[Cerebras Systems](./Cerebras-overview.md) · [[Cerebras-overview|图谱总览]]
- 证据标记：`官方事实`、`厂商主张`、`独立验证`、`分析推断`、`公开资料未确认`。

## 一句话结论

截至研究截止日，Cerebras 的官方资料已确认 WSE-3 Turbo（WSE-3T）于 2026-08-18 随 CS-4 发布，并披露了单片晶圆的制程、面积、晶体管、核心、片上 SRAM、计算、带宽和 I/O 指标；CS-4 是由三片 WSE-3T 组成的机架级系统。公开资料只把 CS-4 的首批出货写成“本季度开始”，尚未分别确认 WSE-3T 的流片/工程样片、送样、量产批次、裸片出货、客户部署或专属云实例；性能数字主要是 CS-4 系统级厂商主张，不能回填为 WSE-3T 裸片测试结果。[T1][T2]

## 产品层级与对象边界

| 对象 | 本页可以归属的证据 | 不应从中推导的结论 |
|---|---|---|
| **WSE-3T** | 一片晶圆级处理器。官方芯片页和 CS-4 数据手册给出每片 WSE-3T 的 5nm、46,225 mm²、4T 晶体管、900,000 AI 优化核心、44 GB SRAM、250 PFLOPS 稀疏 FP16、43.2 PB/s 片上内存带宽、53.5 PB/s 片上互连和 2.4 Tbit/s I/O。[T2][T3] | 不能把整机功耗、机架 I/O 延迟、冷却、机架吞吐量或云服务吞吐量当作裸片 TDP、裸片延迟或裸片实测性能。 |
| **CS-4** | 机架级 Cerebras 系统，明确由三片 WSE-3T 组成；系统页和新闻稿披露 750 PFLOPS、129.6 PB/s 内存带宽、160.5 PB/s 片上互连、7.2 Tbit/s I/O 等系统数字。[T1][T4] | 三片相加的系统数字不能写入 WSE-3T 的芯片规格表。 |
| **Wafer-Scale Backpack / Nexus / 机架** | 背包包含晶圆、供电转换、直接液冷、高速 I/O 和控制组件；Nexus 负责跨晶圆/跨机架连接。这些是系统、机架和互连层证据。[T1][T5][T6] | 0.5 mm 供电距离、两倍供给到 WSE-3T 的功率、2 µs I/O 延迟和跨机架组网能力不是单独的 WSE-3T 芯片物理规格。 |
| **云服务/实例** | Cerebras 公共云和 OpenAI 的公开材料明确提到 WSE-3；AWS 与 Cerebras 公告讨论的是 CS-3/Trainium/Bedrock 方案。当前核验没有找到明确标注“WSE-3T 实例”或“CS-4 云实例”的一手页面。[T8][T9] | 不能因 Cerebras 有云 API、OpenAI 使用 WSE-3 或 AWS 有 CS-3 方案，就声称 WSE-3T 已经云上可用。 |
| **客户部署** | 截至核验日没有找到点名 WSE-3T 或 CS-4 的客户部署公告。WSE-3/CS-3 的客户、数据中心和云服务证据属于上一代产品页，留在 [WSE-3 页面](wse-3.md)。 | WSE-3/CS-3 的部署不能迁移为 WSE-3T/CS-4 的部署。 |

## 生命周期与商业状态

| 生命周期项目 | WSE-3T 状态（截至 2026-09-05） | 证据与边界 |
|---|---|---|
| 宣布 | **已确认：2026-08-18** | Cerebras 正式宣布 CS-4，并明确写为由三片新一代 WSE-3 Turbo 组成。[T1][T4] |
| 流片/工程样片 | **公开资料未确认** | 官方资料披露成品规格和系统设计，没有披露 tape-out 日期、工程样片批次、良率或样片照片/编号。 |
| 送样 | **公开资料未确认** | 没有找到 WSE-3T 单独送样、客户试用样片或评估板公告。CS-4 的发布与性能材料不能代替送样证据。 |
| 量产 | **公开资料未确认** | 2026-08-12 的公司材料提到 2026 年制造能力扩张，但没有把产能或晶圆数量明确归属于 WSE-3T；CS-4 页面同时使用“首批出货本季度开始”的前瞻性表述。[T7] |
| 出货 | **WSE-3T 裸片：公开资料未确认** | 官方把“First CS-4 shipments begin this quarter”写成 CS-4 系统计划，并未确认截至核验日已完成实际出货；该说法也不能证明裸片独立出货。[T1][T4] |
| 客户部署 | **公开资料未确认** | 未找到点名 WSE-3T/CS-4 客户、部署地点、验收或生产上线的官方公告。 |
| 云/实例可用 | **公开资料未确认** | 当前公开的 WSE-3 云服务与 OpenAI WSE-3 材料不能作为 WSE-3T 云实例证据；AWS 公告的目标组合是 CS-3 方案，且使用了未来时态。[T8][T9] |
| 路线图 | **已披露路线图，非当前交付状态** | Hot Chips 资料称 CS-5 目标为 2027 年、使用下一代 WSE；CS-6 是带堆叠 DRAM 的 3D wafer-scale 设计目标。资料没有给出 WSE-3T 的停产、维护期限或替代时间表。[T6] |

这里的“已宣布”只表示产品和系统被正式公开，“首批出货本季度开始”也只表示公告时点的计划。两者都不能单独证明 WSE-3T 已完成量产、实际出货或客户部署。

## 芯片级规格

| 指标 | WSE-3T 单片晶圆 | 证据层级与说明 |
|---|---:|---|
| 制程 | TSMC 5nm | 官方 CS-4 数据手册事实。[T2] |
| 有效 AI 优化核心 | 900,000 | 官方芯片页/数据手册事实；WSE-3T 的物理核心总数、禁用核心数和良率未披露。[T2][T3] |
| 晶圆面积 | 46,225 mm² | 官方数据手册与芯片页事实。[T2][T3] |
| 晶体管 | 4T | 官方数据手册与芯片页事实。[T2][T3] |
| 片上 SRAM | 44 GB | 官方数据手册事实，属于 WSE-3T 片上存储；不能与 CS-4 外部/系统内存混写。[T2] |
| AI 计算 | 250 PFLOPS | 官方指标；数据手册脚注说明 AI compute 口径为稀疏 FP16，不能直接解释为稠密 FP16 峰值。[T2] |
| 片上内存带宽 | 43.2 PB/s | 官方 WSE-3T 每片指标。[T2][T3] |
| 片上互连带宽 | 53.5 PB/s | 官方 WSE-3T 每片指标；Hot Chips 资料也把该数字用于描述单片 WSE-3T 的片上通信。[T2][T6] |
| 对外 I/O | 2.4 Tbit/s | CS-4 数据手册按每片 WSE-3T 列示的 I/O 指标；“对外”不等于某一种独立板卡接口速率。[T2] |
| I/O 延迟 | **芯片级：公开资料未确认**；CS-4 系统资料为 2 µs | 2 µs 是 CS-4 系统 I/O 路径口径，不能当作 WSE-3T 裸片固有延迟。[T1][T2] |
| 绝对功耗/TDP | **公开资料未确认** | 官方材料只说 CS-4 的供电转换更靠近 WSE-3T、可提供约两倍上一代的功率；没有披露 WSE-3T 的瓦数或独立 TDP。[T1][T5] |
| 精度/数据类型 | 稀疏 FP16 计算口径已确认；完整 FP8、INT8、稠密 FP16 等逐项吞吐表 **公开资料未确认** | 不用 CS-4 软件栈或系统宣传补齐未公开的 WSE-3T 格式能力。[T2] |

## 架构与软件证据

### 已确认和厂商明确描述的部分

- **晶圆级对象**：Cerebras 将 WSE-3T 作为一片晶圆级处理器销售和描述；CS-4 的基本构成为三片 WSE-3T。这里的“每片”与“每个 CS-4”是不同计量层级。[T1][T2][T3]
- **片上通信**：官方资料把 53.5 PB/s 作为单片 WSE-3T 片上互连带宽，并说明跨系统时高体量的张量/专家通信尽量留在晶圆内，晶圆之间传递较低体量的激活。这是厂商的系统架构描述，不是对某个检索算子或内存地址机制的证明。[T2][T6]
- **CS-4 软件/互连层**：CS-4 材料提到可编程 I/O、RoCE v2 RDMA 和 Direct Wafer Links。这些是 CS-4 系统的互连与软件能力，不能直接改写为 WSE-3T 裸片拥有某个专用网络协议引擎。[T1][T5]

### 仍未被 WSE-3T 专属资料证实的部分

- WSE-3T 的处理单元组织、NoC/路由细节、时钟、每核心本地存储、指令格式、稀疏执行单元和精度转换路径，公开资料未给出足够的专属技术资料。
- 没有找到可把 WSE-3T 明确对应到 Search、Top-k、Gather、倒排索引、分页表或 KV Cache 地址引擎的官方硬件证据。高片上带宽与大 SRAM 对解码或检索工作负载可能有帮助，这是**分析推断**，不等于存在检索专用硬件。
- 截至核验日没有找到 WSE-3T 专属 SDK/compiler 版本、编程模型变更或完整指令集发布。CSL、SDK 和 WSE-3 的编程证据保留在上一代页面，不能自动移植到 WSE-3T。

## 性能与采用证据

| 证据对象 | 结果 | 证据性质与限制 |
|---|---:|---|
| CS-4 运行 GPT-OSS-120B | >4,400 tokens/s/user | Cerebras 新闻稿的**厂商主张**，用于相同提示的对比；对象是 CS-4 机架系统，不是 WSE-3T 裸片。新闻稿没有提供足以复现实验的完整上下文长度、精度、批量、并发和服务配置。[T1] |
| CS-4 对 GPU 的比较 | up to 30× | **厂商主张/系统级比较**；不是独立测试，也不是 WSE-3T 的单片加速比。[T1][T4] |
| CS-4 大模型吞吐 | 产品页写“>1,000 tok/s on >50T models”，发布博客写“>1,000 tok/s on >10T models” | 两个官方页面的模型规模口径不一致。保留原文，不用一个数字覆盖另一个，也不把它改写成 WSE-3T 裸片能力。[T4][T5] |
| 独立验证 | **公开资料未确认有直接绑定 WSE-3T/CS-4 的可复现实测** | 第三方云服务榜单即使测到 Cerebras endpoint，也通常无法从公开页面确认其具体是 WSE-3T 还是其他 WSE/CS 系统；因此不能作为 WSE-3T 裸片验证。 |
| 客户/云采用 | **WSE-3T/CS-4 专属：公开资料未确认** | 截至核验日，未找到点名 WSE-3T 或 CS-4 的客户部署、云实例 SKU 或实际生产上线材料。WSE-3/CS-3 采用证据见 [WSE-3 页面](wse-3.md)。 |

## 未确认项、冲突与使用边界

1. 官方资料称 WSE-3T 是新一代处理器，并披露了相对 CS-3 的系统提升；但没有公开 WSE-3T 的 tape-out、工程样片、核心物理总数、时钟、裸片功耗、良率、量产数量或独立客户验收。不能据此推断它只是 WSE-3 的加频版，也不能反向推断为全新微架构。
2. “三片 WSE-3T”“750 PFLOPS”“129.6 PB/s”“160.5 PB/s”“7.2 Tbit/s”和“2 µs”均属于 CS-4 系统边界。只有明确标注为“每片 WSE-3T”的 250 PFLOPS、43.2 PB/s、53.5 PB/s 和 2.4 Tbit/s 才进入本页的芯片级表格。[T1][T2]
3. CS-4 的“首批出货本季度开始”是公告时的前瞻性时间表；公司材料还包含面向未来的风险与客户采用表述。公开资料没有把该时间表更新为 WSE-3T/CS-4 已完成实际出货的确认。[T1][T7]
4. WSE-3 云服务、OpenAI 的 WSE-3 说明、CS-3 客户部署和 AWS 的 CS-3 方案都不能证明 WSE-3T 已经具备云或客户部署状态。[T8][T9]
5. CS-5/CS-6 是路线图或设计目标，不是 WSE-3T 的生命周期状态，也不构成 WSE-3T 停产日期。[T6]

## 直接来源

1. [Cerebras Unveils CS-4: Up to 30 Times Faster than GPU-based Solutions](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions) — 主体：Cerebras Systems；发布日期：2026-08-18；核验日期：2026-09-05。CS-4 三片 WSE-3T、系统规格、性能比较和首批出货时间表。
2. [Meet CS-4 — Cerebras Systems Datasheet](https://cdn.sanity.io/files/e4qjo92p/production/bb028ae2422089dfbcc9fd2455c021f3625c7a75.pdf) — 主体：Cerebras Systems；发布日期：2026-08-18（随 CS-4 发布，PDF 正文未单列独立日期）；核验日期：2026-09-05。WSE-3T 每片规格及 CS-3/CS-4 对照表。
3. [The Future of AI is Wafer Scale / Chip](https://www.cerebras.ai/chip) — 主体：Cerebras Systems；发布日期：公开资料未确认（持续更新的产品页）；核验日期：2026-09-05。WSE-3T 芯片页的面积、晶体管、核心和计算指标。
4. [Cerebras CS-4](https://www.cerebras.ai/cs4) — 主体：Cerebras Systems；发布日期：2026-08-18（页面未单列日期，与 CS-4 发布同日）；核验日期：2026-09-05。CS-4 系统构成、三片 WSE-3T、系统级吞吐和首批出货表述。
5. [Introducing Cerebras CS-4: The Fastest AI Just Got Faster](https://www.cerebras.ai/blog/introducing-cerebras-cs-4) — 主体：Cerebras Systems；发布日期：2026-08-18；核验日期：2026-09-05。Wafer-Scale Backpack、供电/液冷/I/O、系统性能与出货表述。
6. [Ultrafast Frontier Inference: Cerebras Deep Dive at Hot Chips 2026](https://www.cerebras.ai/blog/ultrafast-frontier-inference-cerebras-deep-dive-at-hot-chips-2026) — 主体：Cerebras Systems；发布日期：2026-08-25；核验日期：2026-09-05。WSE-3T 片上通信描述及 CS-5/CS-6 路线图。
7. [Cerebras Reports Second Quarter 2026 Financial Results](https://investors.cerebras.ai/node/7286/pdf) — 主体：Cerebras Systems；发布日期：2026-08-12；核验日期：2026-09-05。制造能力、产能合同和云/客户业务背景；未将其扩张数字归属到 WSE-3T。
8. [How Cerebras Serves GPT-5.6 Sol at up to 750 Tokens per Second](https://www.cerebras.ai/blog/how-cerebras-serves-gpt-5-6-sol-at-up-to-750-tokens-per-second) — 主体：Cerebras Systems；发布日期：2026-08-27；核验日期：2026-09-05。明确指向 WSE-3 的现有服务，用于排除 WSE-3T 云实例推断。
9. [AWS and Cerebras Collaboration Aims to Set New Standard for AI Inference](https://investors.cerebras.ai/news-releases/news-release-details/aws-and-cerebras-collaboration-aims-set-new-standard-ai) — 主体：AWS、Cerebras Systems；发布日期：2026-03-13；核验日期：2026-09-05。CS-3/Trainium/Bedrock 方案公告，使用未来时态，非 CS-4/WSE-3T 可用性证明。
