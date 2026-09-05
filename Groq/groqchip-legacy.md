# GroqChip 上一代基线证据页

- 研究截止日：2026-09-05
- 核验日期：2026-09-05
- 研究对象：GroqChip Processor，Groq 早期/上一代 LPU 芯片基线
- 产品层级：芯片；另单列 GroqCard、GroqRack/服务器、GroqCloud API 与 Tokens/s 服务边界
- 导航报告：[07-groq-lpu.md](./07-groq-lpu.md)

## 一句话结论

本地综合报告引用的 Groq 产品简报把 GroqChip 作为早期 LPU 芯片基线，并列出 14 nm、230 MB 片上 SRAM、80 TB/s 片上带宽，以及 300 W max、215 W TDP、185 W average 等口径；这些数字只适用于旧 GroqChip，不能迁移到 Groq 3/LP30。除产品简报外，当前已读取材料不足以确认 GroqChip 的完整流片、送样、量产、出货和客户部署链路；GroqCloud 的 Tokens/s 也不能归因给这颗芯片。[S1][S2][S3]

## 产品层级与对象边界

| 层级 | 本页范围 | 不能跨层级推断 |
|---|---|---|
| GroqChip Processor | 只记录本地报告引用的产品简报直接归属于芯片的规格与 LPU 架构基线 | 不把 GroqCard、GroqRack 或云服务指标写成芯片能力 |
| GroqCard/板卡 | 承载芯片的板卡层；当前页不重建板卡配置 | 板卡内存、主机接口和散热不等于单颗 GroqChip 规格 |
| GroqRack/服务器 | 多卡、多芯片、主机和网络组成的系统层；当前材料不足以确认其完整配置 | 机架吞吐、容量、功耗和部署数量不能回填到 GroqChip |
| GroqCloud/API | Groq 提供的云 API 和托管服务 | API 的 Tokens/s、延迟和模型可用性不证明旧芯片仍是当前后端，也不证明每颗芯片的峰值 |
| Tokens/s | 服务端输出速度指标，依赖模型、输入输出、并发、队列、网络、软件和后端设备 | 不能写成 GroqChip 的 tokens/s 或 Tokens/J |
| Groq 3/LP30 | 新一代芯片对象，另见 [groq3-lp30.md](./groq3-lp30.md) | 不能用 GroqChip 的规格推导 LP30 |

## 生命周期状态

| 生命周期字段 | 截至 2026-09-05 的判断 | 证据状态与边界 |
|---|---|---|
| 宣布/命名 | GroqChip 名称和产品简报已出现在现有直接来源中；首次宣布日期公开资料未确认 | 已确认产品对象存在；首发日期不补猜。[S1] |
| 流片或工程样片 | 公开资料未确认 | 当前已读取来源没有流片批次、工程样片或 bring-up 日期 |
| 送样/客户取样 | 公开资料未确认 | 产品简报不是送样证明，云服务可用也不是客户取样证明 |
| 量产 | 芯片级量产日期和数量公开资料未确认 | 产品简报与服务材料不能单独证明晶圆量产规模 |
| 出货 | 公开资料未确认 | 未读取到按 GroqChip 标注的出货数量、客户订单或供应链确认 |
| 客户部署 | 芯片级客户部署公开资料未确认 | 云服务/基础设施存在不等于能识别具体芯片、客户、数量或部署时间 |
| 云或实例可用 | GroqCloud API 的服务存在；GroqChip 是否对应当前每个实例公开资料未确认 | 服务可用性和芯片代际映射必须分开写。[S3] |
| 路线图 | Groq 官方 LPU 材料提及第一代与未来节点演进；对应 GroqChip 的确切后续 SKU、时间表和当前状态公开资料未确认 | 通用路线表述不等于 GroqChip 仍在量产，也不等于 LP30 已上线。[S2] |

## 芯片级规格

下表只列本地报告已经引用的 GroqChip 产品简报口径；未在该材料中直接确认的字段不补数字。

| 项目 | GroqChip 公开口径 | 证据状态与边界 |
|---|---|---|
| 产品名称 | GroqChip Processor | 已确认产品简报口径。[S1] |
| 制程 | 14 nm | 本地报告将其作为第一代/旧芯片口径引用；不适用于 LP30。[S1][S2] |
| 片上 SRAM | 230 MB | 产品简报口径；不是系统总容量，也不是外部内存。[S1] |
| 片上存储带宽 | 80 TB/s | 产品简报口径；不是某模型的有效带宽。[S1] |
| 最大功耗 | 300 W max | 产品简报口径；不能与 TDP、平均功耗混写。[S1] |
| TDP | 215 W | 产品简报口径；不能等同于任意模型的实际功耗。[S1] |
| 平均功耗 | 185 W average | 产品简报口径；完整 workload、利用率、软件版本和测量边界公开资料未确认。[S1] |
| 计算单元数量、频率、面积、封装 | 公开资料未确认 | 当前已读取直接来源没有足够字段支持数字 |
| 片外内存、主机接口、板卡级网络 | 公开资料未确认或属于板卡/系统层 | 不把 GroqCard、GroqRack 或主机配置回填为芯片规格 |

## 架构与软件证据

- Groq 的 LPU 说明将该路线描述为以片上 SRAM、显式数据移动和编译器静态安排为核心的空间数据流架构。编译器在运行前安排计算、内存和通信，目标是让执行时间和数据路径更可预测。[S2]
- Groq 的早期产品简报直接把 230 MB SRAM、80 TB/s 带宽和功耗字段放在 GroqChip Processor 这一芯片对象上，因此这些数字可用于旧芯片基线，但不可用于 LP30。[S1]
- “确定性”描述的是已编译图和执行路径的架构目标，不代表外部 API 排队、网络、动态请求、模型加载或云服务尾延迟恒定。

### 证据状态

| 主张 | 状态 | 限定 |
|---|---|---|
| SRAM-first、编译器静态调度、显式数据流是 Groq LPU 路线特征 | 厂商主张/官方架构描述 | 可以描述设计方向，不能由此推出任意模型的实际性能 |
| GroqChip 的 14 nm、230 MB、80 TB/s、功耗数值 | 厂商主张 | 来自产品简报，不是独立验证；测量条件应以原简报为准 |
| GroqChip 在 GroqCloud 服务中对应的具体实例/后端 | 公开资料未确认 | 云服务公开存在不等于芯片代际、数量和拓扑透明 |
| GroqChip 有专用动态 Search、Top-k、page-aware Gather 硬件 | 公开资料未确认 | 当前已读取架构材料没有给出这些专用单元或可复现结果 |

## 性能、采用与服务层边界

- 当前直接来源提供的是芯片产品规格和架构说明，不提供带模型、精度、batch、延迟、软件版本、功耗边界的独立 benchmark。因此本页不生成 GroqChip 的 TPOT、TTFT 或 Tokens/J 数字。
- GroqCloud 平台和 Groq 的云业务材料说明 API/生产推理服务存在，并会持续扩展基础设施；这些材料属于服务或基础设施层，不公开当前每个模型使用的芯片代际和数量。[S3][S4]
- 即使 GroqCloud 页面展示 Tokens/s 或 tokens/s/user，也只能作为服务侧观察值。它受模型、上下文、并发、排队、网络、编译产物和后端系统影响，不能反推 GroqChip 的峰值吞吐、功耗效率或当前仍在生产。
- 没有足够公开证据把某一客户、某一 GroqRack/服务器或某一 API 实例唯一映射到 GroqChip。因此客户部署、出货数量和当前云后端均保留为“公开资料未确认”。

## 未确认项与冲突

1. GroqChip 的流片、工程样片、送样、量产日期、出货数量、客户名单和物理部署数量未由当前直接来源完整确认。
2. 产品简报中的 300 W max、215 W TDP、185 W average 是三个不同功耗口径，不能择一写成“芯片功耗”；也没有足够测试条件支持跨产品比较。[S1]
3. GroqCloud API 已公开存在，与“GroqChip 仍是当前云实例后端”是两个命题；后者公开资料未确认。[S3]
4. Groq LPU 文章中的 14 nm/未来节点叙述属于第一代与通用路线背景，不能用来确定 GroqChip 的量产时点，也不能用来确认 LP30 制程。[S2]
5. 本页不把旧 GroqRack/服务器的系统规格、云服务 Tokens/s 或 Groq 3 LPX 的新规格混入 GroqChip 基线。

## 直接来源清单

| 编号 | 标题 | 主体 | 发布日期 | 核验日期 | 直接 URL |
|---|---|---|---|---|---|
| S1 | GroqChip Processor Product Brief | Groq | 未标注 | 2026-09-05 | <https://www.groq.com/GroqDocs/Product%20Spec%20Sheet%20-%20GroqChip%E2%84%A2%20Processor.pdf> |
| S2 | What Is a Language Processing Unit? | Groq | 2025-03-07 | 2026-09-05 | <https://groq.com/blog/the-groq-lpu-explained> |
| S3 | Groq Platform | Groq | 未标注 | 2026-09-05 | <https://groq.com/platform> |
| S4 | Groq Raises $650M to Scale Its AI Inference Cloud Business | Groq | 2026-06-22 | 2026-09-05 | <https://groq.com/newsroom/groq-raises-usd650m-to-scale-its-ai-inference-cloud-business> |
| S5 | Inside the LPU: Deconstructing Groq's Speed | Groq | 2025-08-01 | 2026-09-05 | <https://home.cloud.groq.io/blog/inside-the-lpu-deconstructing-groq-speed> |

> 证据边界：GroqChip 的芯片级规格主要来自 Groq 产品简报，架构解释来自 Groq 官方文章；服务页只能证明 GroqCloud/API 层存在，不能证明旧芯片仍对应每个实例。LP30 请参阅 [groq3-lp30.md](./groq3-lp30.md)，不要跨代回填规格。
