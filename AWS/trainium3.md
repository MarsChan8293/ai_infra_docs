# AWS Trainium3（v4）芯片证据页

- 研究截止日：2026-09-05
- 实际核验日：2026-09-05
- 厂商：Amazon Web Services（AWS）
- 产品层级：AI 训练与推理加速芯片；公开云承载形态是 EC2 Trn3 UltraServer
- 导航：[AWS Trainium / Inferentia 综合报告](06-aws-trainium.md)

## 一句话结论

Trainium3 是 AWS 第四代 NeuronDevice，单颗芯片包含 8 个 NeuronCore-v4；AWS Neuron 芯片页给出 2,517 MXFP8/MXFP4 TFLOPS、671 BF16/FP16/TF32 TFLOPS、183 FP32 TFLOPS、144 GiB 设备内存、4.9 TB/s 带宽和 2.56 TB/s/device NeuronLink-v4。[S1] AWS 已于 2025-12-02 宣布 Trn3 UltraServer GA，但芯片 tape-out、样片、送样、晶圆量产和独立出货记录没有在本次核验的公开资料中确认。[S3][S4]

## 产品层级与对象边界

| 对象 | 本页如何使用 | 边界说明 |
|---|---|---|
| Trainium3 | 芯片级事实 | 本页的核心数、算力、HBM、DMA 和芯片互联数字默认指单颗芯片。 |
| NeuronCore-v4 | 芯片内部计算单元 | 8 个 NeuronCore-v4 构成一颗 Trainium3；NeuronCore 不是 UltraServer 或 EC2 实例。[S1][S2] |
| Trn3 UltraServer | 服务器级组合 | 当前 Neuron 架构页列出 64 芯片 Gen1 和 144 芯片 Gen2 两种聚合配置。[S5] |
| EC2 UltraCluster 3.0 | 集群级平台 | 连接多个 UltraServer；集群芯片数和 exaflops 是平台能力/容量口径，不能回写为单芯片规格。 |
| Neuron SDK / NKI | 软件与编程接口 | NKI 指南说明编程模型和硬件路径，但软件 API 不能单独证明额外的应用级硬件。 |

## 生命周期与可用性

| 阶段 | 截至研究截止日的证据判断 | 证据与边界 |
|---|---|---|
| 宣布 | 已确认事实：2025-12-02 AWS 宣布 Trn3 UltraServer GA，并明确其由 Trainium3 芯片驱动；本页将该公告作为 Trainium3 首个已核验的产品级公开节点。[S3][S4] | 本次没有找到更早、单独针对 Trainium3 芯片的公告，因此不另造早于该日的宣布日期。 |
| 流片 / 工程样片 | 公开资料未确认 | “首个 3 nm AWS AI 芯片”是官方产品/制程表述，不等于公开披露 tape-out 或工程样片日期。[S3] |
| 送样 | 公开资料未确认 | Trn3 UltraServer GA 和客户案例没有披露对外送样对象、批次或数量。 |
| 量产 | 公开资料未确认 | UltraServer GA 说明云平台已交付产品，不提供晶圆、封装测试或 Trainium3 累计量产数字。 |
| 出货 | 公开资料未确认 | 本次核验未找到按 Trainium3 单独披露的首批出货、累计出货或库存数据。 |
| 客户部署 | 厂商/客户采用主张：AWS 发布材料称 Amazon Bedrock 已有 Trainium3 生产工作负载，并列出 Anthropic、Karakuri、Metagenomi、NetoAI、Ricoh、Splash Music 等客户/合作方。[S4][S7] | 这是 AWS 和客户引述；不等同于第三方部署审计或芯片出货量。 |
| 云 / 实例可用 | 已确认事实：Trn3 UltraServer 于 2025-12-02 GA；AWS Neuron 架构页列出 Gen1 64 芯片和 Gen2 144 芯片 UltraServer 配置。[S3][S5] | 本页确认 UltraServer 云产品路径；具体区域、配额、价格和每个 SKU 的即时库存不在本次证据页中展开。 |
| 路线图 | 公开资料未确认 | Trainium4 另有路线图公告，但不能反推 Trainium3 的停产、EOL 或库存时间。 |

## 芯片级规格

| 项目 | AWS Neuron 芯片页口径 | 证据状态 |
|---|---|---|
| 计算单元 | 8 个 NeuronCore-v4 / 芯片。[S1] | 已确认事实 |
| MXFP8 / MXFP4 算力 | 2,517 TFLOPS / 芯片。[S1] | 已确认事实；GA 新闻稿将其四舍五入写作约 2.52 PFLOPS。[S3] |
| BF16 / FP16 / TF32 算力 | 671 TFLOPS / 芯片。[S1] | 已确认事实 |
| 稀疏算力 | 2,517 TFLOPS，AWS 页将其标为 sparse FP16/BF16/TF32 口径。[S1] | 已确认事实；稀疏值不与 dense 值相加。 |
| FP32 算力 | 183 TFLOPS / 芯片。[S1] | 已确认事实 |
| 设备内存 | 144 GiB；GA 新闻稿称 144 GB HBM3e。[S1][S3] | 已确认事实；GB/GiB 为不同页面单位，未擅自换算。 |
| 设备内存带宽 | 4.9 TB/s / 芯片。[S1][S3] | 已确认事实，但 NKI 指南给出 4.7 TB/s，冲突见后文。 |
| DMA | 芯片页给出 4.9 TB/s DMA，并支持内联计算。[S1] | 已确认页面口径；NKI 指南报告 128 个 DMA engines，指标定义不同或页面版本不同，不能拼接。 |
| 芯片间互联 | NeuronLink-v4，2.56 TB/s/device。[S1] | 已确认芯片页口径；Trn3 平台页使用 2,048 GiB/s/device 的表格口径，见冲突说明。 |
| 集合通信 | 芯片页给出 16 个 CC-Cores。[S1] | 已确认页面口径；NKI 指南给出 20 个 CC-Cores，保留冲突。 |
| 编程能力 | 支持逻辑 NeuronCore、可编程 RNE/随机舍入和 GPSIMD 自定义算子。[S1][S2] | 硬件/编程能力已确认；不是对任意模型的性能保证。 |
| 制程、封装、功耗 | AWS 宣传 Trainium3 为首个 3 nm AWS AI 芯片；封装与 TDP 公开资料未确认。[S3] | 3 nm 是 AWS 官方宣传事实，但不能据此推出 tape-out 日期或功耗。 |

## NeuronCore-v4 与软件证据

- **核心结构，已确认事实。** NKI 架构指南把 Trainium3 描述为 8 个 NeuronCore-v4、4 个 HBM stack、128 个 DMA engines、20 个 CC-Cores 和 4 个 NeuronLink-v4 的 NeuronDevice；每个核心的 SBUF 为 32 MiB，PSUM 为 2 MiB。[S2] 这些是 NKI 指南口径，不与芯片总览页的冲突数字自动合并。
- **新硬件路径，已确认事实。** NKI 指南列出 BF16 PSUM、后台转置、快速 exp、XORWOW PRNG、间接 SBUF/PSUM gather/scatter、片上近存储 read-add-write 和 DMA traffic shaping 等能力。[S2]
- **软件交付，已确认事实。** AWS Trainium 产品页把 Trainium3 接入 NeuronCore Compute Engine、Neuron SDK/NKI 和 Trn3 UltraServer 产品路径。[S6] 软件支持说明可编程入口，不等于独立的搜索、向量数据库或检索硬件。
- **边界判断，分析推断。** NeuronCore-v4 的片上数据路径和编程能力有助于表达复杂训练/推理算子，但不能把 NKI 的 gather、scatter 或 reduction API 解释为芯片存在未公开命名的应用级专用单元。

## 性能与采用证据

| 证据 | 可保留的表述 | 证据等级与限制 |
|---|---|---|
| Trn3 UltraServer GA 公告 | AWS 宣称相对 Trn2 UltraServer 最高 4.4 倍性能、3.9 倍内存带宽和 4 倍性能/功耗；并给出最多 144 芯片、约 362 PFLOPS 的 UltraServer 口径。[S3] | 厂商比较主张和服务器级聚合值，不是独立测试，也不是单芯片普适性能。 |
| AWS Press Center | AWS 称 Bedrock 上已有 Trainium3 生产工作负载，并列出多家客户；客户案例还包含对吞吐/成本的主张。[S4][S7] | AWS/客户主张；未提供足以复现的完整模型、批量、精度、延迟、价格和功耗条件。 |
| UltraServer 结构 | Gen1 64 芯片、Gen2 144 芯片，分别有约 161 PFLOPS、362 PFLOPS 等聚合口径。[S5] | 服务器级规格；不能当作单芯片 161/362 PFLOPS。 |
| 独立验证 | 本次核验未定位到满足同一模型、精度、批量、并行、延迟和功耗边界的独立 Trainium3 芯片级对比。 | 公开资料未确认统一独立基准。 |

## 未确认项与冲突

1. **高层芯片页与 NKI 指南数字不完全一致。** 芯片页给出 4.9 TB/s HBM 带宽、4.9 TB/s DMA 和 16 CC-Cores；NKI 指南给出 4.7 TB/s HBM 带宽、128 个 DMA engines、20 个 CC-Cores，并补充 4 个 HBM stacks。两者都是 AWS 官方页面，但本次没有找到解释版本/定义差异的注释，故不擅自选边。
2. **芯片互联数字的单位/层级差异。** 芯片页的 2.56 TB/s/device 与 Trn3 平台页的 2,048 GiB/s/device 不能直接当作同一统计口径；平台表的 aggregate bandwidth 也不能回写为芯片额定带宽。[S1][S5]
3. **GB 与 GiB 的单位差异。** GA 新闻稿写 144 GB HBM3e，Neuron 芯片页写 144 GiB；本页保留原单位。
4. **2,517 TFLOPS 与 2.52 PFLOPS 是精度不同的表述。** 本页将其视为同一官方口径的精确值与四舍五入值，不把它们和 UltraServer 聚合值混用。
5. **公开资料未确认** tape-out、工程样片、送样、晶圆量产、累计出货、封装、TDP、停产时间、具体区域库存以及 Trainium3 的独立第三方基准。

## 直接来源

核验日期均为 2026-09-05；在线文档和当前产品页未显示独立发布日期时，明确标注为“页面日期未标明”。

1. **Trainium3 — AWS Neuron architecture**，发布主体 AWS Neuron，发布日期：页面日期未标明（在线文档），核验日期：2026-09-05。[直接页面](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium3.html)
2. **Trainium3 architecture — NKI architecture guide**，发布主体 AWS Neuron，发布日期：页面日期未标明（在线文档），核验日期：2026-09-05。[直接页面](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html)
3. **Announcing Amazon EC2 Trn3 UltraServers for faster, lower-cost generative AI training**，发布主体 AWS，发布日期：2025-12-02，核验日期：2026-09-05。[直接公告](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)
4. **Trainium3 UltraServers now available, enabling customers to train and deploy AI models faster at lower cost**，发布主体 Amazon / AWS Press Center，发布日期：2025-12-02，核验日期：2026-09-05。[直接新闻稿](https://press.aboutamazon.com/2025/12/trainium3-ultraservers-now-available-enabling-customers-to-train-and-deploy-ai-models-faster-at-lower-cost)
5. **Trn3 architecture**，发布主体 AWS Neuron，发布日期：页面日期未标明（在线文档），核验日期：2026-09-05。[直接页面](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trn3-arch.html)
6. **AWS Trainium — AI accelerator**，发布主体 AWS，发布日期：页面日期未标明（当前产品页），核验日期：2026-09-05。[直接产品页](https://aws.amazon.com/ai/machine-learning/trainium/)
7. **AWS Trainium customers**，发布主体 AWS，发布日期：页面日期未标明（当前客户页），核验日期：2026-09-05。[直接客户页](https://aws.amazon.com/ai/machine-learning/trainium/customers/)
