# AWS Trainium4 路线图证据页

- 研究截止日：2026-09-05
- 实际核验日：2026-09-05
- 厂商：Amazon Web Services（AWS）
- 产品层级：尚在公开路线图中的 AI 加速芯片；没有已核验的 EC2 实例或 UltraServer SKU
- 厂商总览：[AWS / 亚马逊云科技](./AWS-overview.md) · [[AWS-overview|图谱总览]]

## 一句话结论

截至 2026-09-05，公开一手资料只确认 Trainium4 是下一代 Trainium 芯片，并在 AWS 与 OpenAI 的战略合作公告中被描述为预计于 2027 年开始交付，方向包括更高 FP4 算力、更高内存带宽和更大 HBM 容量。[S1] 目前没有足够公开证据确认 Trainium4 已流片、送样、量产、出货、部署或以 EC2/UltraServer 形态 GA；所有具体芯片规格均应保留为公开资料未确认。

## 产品层级与对象边界

| 对象 | 本页如何使用 | 边界说明 |
|---|---|---|
| Trainium4 | 芯片路线图对象 | 只记录 AWS 已公开的方向性描述和预期时间，不把 Trainium3 的规格迁移过来。 |
| NeuronCore / NeuronDevice | 内部架构对象 | 截至核验日没有找到 Trainium4 专属 NeuronCore 数量、版本或微架构资料。 |
| EC2 Trn4 / 其他实例 | 云实例对象 | 没有找到公开的 Trn4 实例名称、规格、区域、价格或 GA 公告。 |
| UltraServer / UltraCluster | 服务器/集群对象 | OpenAI 公告谈的是通过 AWS 基础设施消费 Trainium 容量，并非已公布的 Trainium4 服务器拓扑。[S1] |
| Neuron SDK / NKI | 软件对象 | 当前 Trainium 家族软件页和 Trainium3 文档不能证明 Trainium4 已有专属软件支持。 |

## 生命周期与可用性

| 阶段 | 截至研究截止日的证据判断 | 证据与边界 |
|---|---|---|
| 宣布 | 已确认事实：2026-02-27 AWS 与 OpenAI 公告称双方承诺覆盖 Trainium3 和下一代 Trainium4。[S1] AWS 2026-01-02 行业回顾也提到 AWS CEO 分享了对 Trainium4 的展望。[S2] | 这是路线图/合作公告，不是芯片产品 GA。 |
| 流片 / 工程样片 | 公开资料未确认 | 公告没有披露 tape-out、工程样片、晶圆厂或验证平台。 |
| 送样 | 公开资料未确认 | 没有披露送样客户、数量、时间或样片状态。 |
| 量产 | 公开资料未确认 | “预计开始交付”是前瞻性商业时间表，不能证明晶圆或封装已量产。 |
| 出货 | 公开资料未确认 | 2027 年预计开始交付尚未构成截至研究截止日的已出货记录；公告也没有给出芯片数量。 |
| 客户部署 | 公开资料未确认 | OpenAI 承诺消费 Trainium 容量是未来容量安排，且覆盖 Trainium3 与 Trainium4，不能证明 Trainium4 已部署在客户生产环境。 |
| 云 / 实例可用 | 公开资料未确认 | 本次核验未找到 `Trn4`、Trainium4 UltraServer、区域、价格、Capacity Block 或托管服务 GA 的官方页面。AWS 当前 Trainium 产品页提供家族导航，但未给出 Trainium4 SKU。[S3] |
| 路线图 | 已确认方向性主张：Trainium4 预计于 2027 年开始交付，并针对 FP4 算力、内存带宽和 HBM 容量提升。[S1] | AWS 同一公告明确这些计算能力和交付时间属于存在不确定性的前瞻性陈述。[S1] GA 日期、区域和实际性能公开资料未确认。 |

## 芯片级规格

| 项目 | 截至 2026-09-05 的公开口径 | 证据状态 |
|---|---|---|
| 产品代际 | 下一代 Trainium；公告将其与 Trainium3 并列。[S1] | 已确认路线图身份 |
| FP4 算力 | “significantly higher FP4 compute performance”，没有数值。[S1] | 厂商方向性主张；数值公开资料未确认。 |
| HBM 容量 | “increased high-bandwidth memory capacity”，没有容量、代际或颗粒数。[S1] | 厂商方向性主张；具体规格公开资料未确认。 |
| 内存带宽 | “expanded memory bandwidth”，没有带宽数值或接口定义。[S1] | 厂商方向性主张；具体规格公开资料未确认。 |
| NeuronCore 数量与版本 | 公开资料未确认 | 不把 Trainium3 的 8 个 NeuronCore-v4 或其他代际数字代入。 |
| Tensor / Vector / Scalar / GPSIMD 结构 | 公开资料未确认 | 当前 Trainium3 架构文档只证明 Trainium3 的结构，不证明 Trainium4 复用或新增的硬件。 |
| HBM 类型、封装、制程、芯片面积、TDP | 公开资料未确认 | 2 GW 容量承诺和 2027 时间表都不能推出这些芯片参数。 |
| DMA、NeuronLink、集合通信、主机接口 | 公开资料未确认 | 没有 Trainium4 专属架构或数据手册。 |
| 物理芯片数量 | 公开资料未确认 | OpenAI 的 2 GW 是基础设施容量，不是 Trainium4 芯片数量。 |

## 架构、软件与云产品证据

- **专属芯片架构，公开资料未确认。** 本次核验没有找到 Trainium4 的 AWS Neuron architecture、NKI architecture、数据手册、封装图或 NeuronCore 版本页面。
- **家族软件边界，已确认但不外推。** AWS 当前 Trainium 产品页介绍 Trainium 家族和已发布代际的 NeuronCore、Neuron SDK/NKI 入口。[S3] 这些页面不能证明 Trainium4 已经可编译、可运行或拥有特定硬件指令。
- **云产品边界，公开资料未确认。** Trainium3 UltraServer GA 公告只能说明前一代产品已存在，[S4] 不能推断 Trainium4 已有 Trn4 实例、UltraServer 互联、UltraCluster 规模或 Bedrock 可用性。
- **分析推断。** “更高 FP4 算力、更高内存带宽、更大 HBM”说明公开路线图针对计算密度和内存系统，但没有足够证据判断它采用何种 NeuronCore、互联、制程或封装路线。

## 性能与采用证据

| 证据 | 可以写成什么 | 不能写成什么 |
|---|---|---|
| AWS/OpenAI 战略合作公告 | OpenAI 承诺通过 AWS 基础设施消费约 2 GW Trainium 容量，承诺范围覆盖 Trainium3 和 Trainium4。[S1] | 不能把 2 GW 换算成 Trainium4 颗数、已部署数量或单芯片功耗。 |
| 公告中的 Trainium4 描述 | AWS 预计 Trainium4 在 2027 年开始交付，并将提供更高 FP4 算力、更高内存带宽和更大 HBM 容量。[S1] | 不能写成已量产、已出货、已部署、EC2 GA 或已完成性能测试。 |
| AWS 2026 行业回顾 | AWS CEO 在 re:Invent 2025 展望了下一代 Trainium4。[S2] | 该回顾没有芯片规格、基准结果或可用性承诺。 |
| 独立验证 | 本次核验未定位到 Trainium4 的独立芯片样片测试或公开 benchmark。 | 不填写 FP4 吞吐、能效、延迟、成本或集群扩展数字。 |

## 未确认项与冲突

1. **“交付”不等于 GA。** 公告的 “expected to begin delivery in 2027” 是前瞻性路线图措辞，未定义是芯片交付、服务器容量交付还是云实例可用，也没有给出 GA 日期。[S1]
2. **2 GW 不等于芯片数量。** 公告把容量承诺放在 AWS 基础设施层，且同时覆盖 Trainium3 与 Trainium4；Trainium4 的分配、功耗、部署地点和芯片数都公开资料未确认。[S1]
3. **前代证据不能跨代升级。** Trainium3 的 NeuronCore-v4、HBM、NeuronLink、Trn3 UltraServer 和 Bedrock 生产工作负载均属于前代或平台证据，不能直接作为 Trainium4 规格。[S3][S4]
4. **官方公告含前瞻性陈述免责说明。** AWS/Amazon 明确提示 Trainium 芯片的计算能力、性能特征和交付时间存在不确定性，实际结果可能发生重大变化。[S1]
5. **公开资料未确认** tape-out、工程样片、送样、量产、出货、客户部署、EC2/UltraServer/UltraCluster SKU、区域、价格、HBM 类型与容量、NeuronCore 版本、制程、封装、TDP、互联和独立性能。

## 直接来源

核验日期均为 2026-09-05；当前家族页未显示独立发布日期时，明确标注为“页面日期未标明”。S3、S4 是边界参照，不把它们当作 Trainium4 芯片规格证据。

1. **OpenAI and Amazon Announce Strategic Partnership**，发布主体 Amazon Web Services / OpenAI，发布日期：2026-02-27，核验日期：2026-09-05。[直接新闻稿](https://press.aboutamazon.com/2026/2/openai-and-amazon-announce-strategic-partnership)
2. **AWS re:Invent 2025 Recap for Automotive and Manufacturing**，发布主体 AWS for Industries，发布日期：2026-01-02，核验日期：2026-09-05。[直接文章](https://aws.amazon.com/blogs/industries/aws-reinvent-2025-recap-for-automotive-and-manufacturing/)
3. **AWS Trainium — AI accelerator**，发布主体 AWS，发布日期：页面日期未标明（当前家族产品页），核验日期：2026-09-05。[直接产品页](https://aws.amazon.com/ai/machine-learning/trainium/)
4. **Announcing Amazon EC2 Trn3 UltraServers for faster, lower-cost generative AI training**，发布主体 AWS，发布日期：2025-12-02，核验日期：2026-09-05。[直接公告](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)
