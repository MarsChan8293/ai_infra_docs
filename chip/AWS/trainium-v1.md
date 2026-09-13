# AWS Trainium（v1）芯片证据页

- 研究截止日：2026-09-05
- 实际核验日：2026-09-05
- 厂商：Amazon Web Services（AWS）
- 产品层级：AI 训练加速芯片；对应的云产品是 Amazon EC2 Trn1 / Trn1n
- 厂商总览：[AWS / 亚马逊云科技](./AWS-overview.md) · [[AWS-overview|图谱总览]]

## 一句话结论

仓库所称 Trainium v1 对应 AWS 第一代 Trainium 芯片，AWS Neuron 当前架构页将它称作第二代 AWS 专用 ML 加速器，并确认每颗芯片含 2 个 NeuronCore-v2、32 GiB 设备内存和 820 GiB/s 带宽。[S1] 公开资料能确认 Trn1 于 2022-10-10 GA、Trn1n 于 2023-04-13 GA，但没有在本次核验中确认芯片本身的 tape-out、送样、晶圆量产或累计出货。[S4][S5]

## 产品层级与对象边界

| 对象 | 本页如何使用 | 边界说明 |
|---|---|---|
| Trainium v1 | 芯片级事实 | 本页的算力、设备内存、DMA 和 NeuronLink 数字默认指单颗芯片。 |
| NeuronCore-v2 | 芯片内部计算单元 | 2 个 NeuronCore-v2 构成一颗 Trainium v1；“v2”是 NeuronCore 代际，不是 Trainium2 芯片。[S1] |
| EC2 Trn1 / Trn1n | 实例级事实 | 一台实例最多 16 颗 Trainium；实例总算力、总 HBM 和 EFA 带宽不能回写为芯片规格。[S7] |
| UltraCluster / EFA | 集群与系统级事实 | 说明多实例训练网络和扩展边界，不等于芯片内部互联或芯片出货量。 |
| Neuron SDK / NKI | 软件与编程接口 | 软件能力和框架支持不能单独证明未被硬件页写出的执行单元。 |

## 生命周期与可用性

| 阶段 | 截至研究截止日的证据判断 | 证据与边界 |
|---|---|---|
| 宣布 | 已确认事实：AWS 在 2020-11-27 发布的 re:Invent 2020 直播记录中宣布 AWS Trainium，并写明目标为 2021 年下半年可用。[S2] | “Coming soon”和目标日期是路线/产品计划，不是芯片流片或量产证明。 |
| 流片 / 工程样片 | 公开资料未确认 | 本次核验未找到 AWS 对 Trainium v1 tape-out、工程样片或封装验证日期的直接披露。 |
| 送样 | 公开资料未确认 | Trn1 预览和云实例发布未披露对外送样对象、数量或样片阶段。 |
| 量产 | 公开资料未确认 | Trn1 GA 证明 EC2 资源可售，不提供晶圆、封装测试或累计量产数字。 |
| 出货 | 公开资料未确认 | 未找到按 Trainium v1 单独披露的出货量、批次或首次芯片交付日期。 |
| 客户部署 | 厂商/客户采用主张：Trn1 GA 材料列出 PyTorch、Helixon、Money Forward 等客户或合作方使用场景。[S4] AWS 当前产品页也列出 Trn1 客户案例。[S6] | 这些是 AWS 发布材料和客户引述，不是独立部署审计或芯片数量统计。 |
| 云 / 实例可用 | 已确认事实：Trn1 于 2022-10-10 GA；Trn1n 于 2023-04-13 GA，面向网络密集型生成式 AI 训练。[S4][S5] | 这是 EC2 实例层状态。Trn1n 的 1,600 Gbps 是实例网络口径，不是单芯片内存带宽。 |
| 路线图 | 公开资料未确认 | Trainium2 的公布不等于 Trainium v1 的停产或 EOL；本次核验未找到 v1-specific 生命周期公告。 |

## 芯片级规格

| 项目 | 公开口径 | 证据状态 |
|---|---|---|
| 计算单元 | 2 个 NeuronCore-v2 / 芯片。[S1] | 已确认事实 |
| INT8 算力 | 380 TOPS / 芯片。[S1] | 已确认事实 |
| FP16 / BF16 / cFP8 / TF32 算力 | 190 TFLOPS / 芯片。[S1] | 已确认事实；不使用旧报告中的未核实替代数字。 |
| FP32 算力 | 47.5 TFLOPS / 芯片。[S1] | 已确认事实 |
| 设备内存 | 32 GiB / 芯片。[S1] | 已确认事实；Neuron 架构页将其描述为 device memory，Trn1 产品资料对实例聚合值常使用 GB。 |
| 设备内存带宽 | 820 GiB/s / 芯片。[S1] | 已确认事实；与 EFA 网络带宽分开。 |
| DMA | 1 TB/s，支持内联压缩/解压缩。[S1] | 已确认事实；这是芯片内数据搬运能力。 |
| 芯片间互联 | NeuronLink-v2，用于训练扩展和内存池化。[S1][S7] | 能力已确认；实例/UltraCluster 的网络不回写为芯片链路速率。 |
| 可编程能力 | 支持动态形状、控制流、可编程舍入，以及通过 GPSIMD 编写自定义算子。[S1] | 硬件/编程能力已确认；不是对任意模型的性能保证。 |
| 制程、封装、功耗、片上 SRAM 容量 | 公开资料未确认 | 不以实例功耗、主机参数或后续代际资料代填。 |

## EC2 Trn1 / Trn1n、UltraCluster 与云边界

| 对象 | Trainium 芯片数 | 设备侧聚合口径 | 实例/集群侧信息 |
|---|---:|---|---|
| `trn1.2xlarge` | 1 | 32 GB 级设备内存 | 8 vCPU；Trn1 实例表的最小配置。 |
| `trn1.32xlarge` | 16 | 512 GB 级加速器内存；最高约 3.4 PFLOPS（实例口径） | 128 vCPU；最高 800 Gbps EFAv2。 |
| `trn1n.32xlarge` | 16 | 512 GB 级加速器内存；同一代 Trainium 聚合资源 | 128 vCPU；最高 1,600 Gbps EFAv2。 |
| Trn1 UltraCluster | 多个 Trn1/Trn1n 实例 | 聚合资源，不能写成单芯片规格 | 用 EFA 扩展训练作业；容量数字取决于页面版本和具体集群。 |

Trn1 实例表和 UltraCluster 描述来自 AWS 的 Trn1 架构文档、GA 文章及当前产品页。[S3][S4][S6][S7] 当前产品页宣传可扩展至约 30,000 颗 Trainium、约 6 exaflops；架构文档又写有超过 100,000 颗 Trainium 和 petabit 级 EFA 的更大规模口径。[S6][S7] 这些都是平台能力/容量描述，不是已部署数量，也不能反推 Trainium v1 的出货量。

## 架构与软件证据

- **NeuronCore-v2，已确认事实。** Trainium v1 与 Inferentia2 都使用 NeuronCore-v2；AWS 架构页列出 Tensor、Vector、Scalar 和 GPSIMD 路径，并说明动态形状、控制流、可编程舍入和自定义算子能力。[S1]
- **芯片间扩展，已确认事实。** NeuronLink-v2 用于 Trainium 芯片之间的 collective compute、训练扩展和内存池化；Trn1.32xlarge 的 2D Torus 及 EFAv2 属于实例/集群拓扑。[S1][S7]
- **软件栈，已确认事实。** AWS 的 Trn1 GA 资料说明 Neuron SDK 与主流深度学习框架配合，提供编译、运行和分析路径。[S4] 这说明云端使用路径，不等于每一项框架能力都是芯片硬件单元。
- **边界判断，分析推断。** NeuronCore-v2 的统一设计解释了 Trainium v1 与 Inferentia2 共享部分编程模型，但不能因此把 Inferentia2 的推理定位或后续 Trainium2 的规格迁移到本页。

## 性能与采用证据

| 证据 | 可保留的表述 | 证据等级与限制 |
|---|---|---|
| Trn1 GA 文章 | AWS 宣称 Trn1 相对可比 EC2 GPU 实例最高可节省 50% 训练成本，并给出最高约 3.4 PFLOPS 的实例级口径。[S4] | 厂商主张；比较结果受模型、并行策略、训练时长、实例价格和软件版本影响。 |
| Trn1n GA 公告 | AWS 宣称 1,600 Gbps EFAv2 可带来最高 20% 更快的训练时间，并给出最高 50% 成本节省。[S5] | 实例/网络级厂商主张；不能写成单芯片算力或内存带宽提升。 |
| 客户案例 | AWS 发布材料提到 Helixon、Money Forward 等客户或合作方使用 Trn1。[S4][S6] | 是 AWS/客户采用叙述，缺少可横向复现的完整模型、精度、批量、功耗和价格条件。 |
| 独立验证 | 本次核验未定位到满足同一模型、精度、并行策略、时长和功耗边界的独立 Trainium v1 芯片级对比。 | 公开资料未确认独立统一基准；本页不补填独立数字。 |

## 未确认项与冲突

1. **Trainium v1 与 NeuronCore-v2 的命名容易混淆。** “v2”在这里是 NeuronCore 代际；Trainium2 是后续芯片家族，不应把两者视为同一产品。
2. **集群规模存在公开口径差异。** 当前 Trn1 产品页的约 30,000 颗与架构文档的超过 100,000 颗属于不同页面版本/平台描述；本页不选择一个数字作为实际部署量。
3. **实例聚合值不能降级成芯片规格。** 512 GB、3.4 PFLOPS、800/1,600 Gbps EFA 都是 Trn1/Trn1n 实例口径；单芯片的公开内存和算力以芯片架构页为准。[S1][S7]
4. **公开资料未确认** tape-out、工程样片、对外送样、晶圆量产、累计出货、制程节点、封装、TDP、停产时间和区域库存。

## 直接来源

核验日期均为 2026-09-05；在线文档和当前产品页未显示独立发布日期时，明确标注为“页面日期未标明”。

1. **Trainium — AWS Neuron architecture**，发布主体 AWS Neuron，发布日期：页面日期未标明（在线文档），核验日期：2026-09-05。[直接页面](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium.html)
2. **re:Invent 2020 Liveblog: Andy Jassy Keynote**，发布主体 AWS News Blog，发布日期：2020-11-27，核验日期：2026-09-05。[直接文章](https://aws.amazon.com/blogs/aws/reinvent-2020-liveblog-andy-jassy-keynote/)
3. **Announcing preview of Amazon EC2 Trn1 instances**，发布主体 AWS，发布日期：2021-11-30，核验日期：2026-09-05。[直接公告](https://aws.amazon.com/about-aws/whats-new/2021/11/amazon-ec2-trn1-instances/)
4. **Amazon EC2 Trn1 instances for high-performance model training are now available**，发布主体 AWS News Blog，发布日期：2022-10-10，核验日期：2026-09-05。[直接文章](https://aws.amazon.com/blogs/aws/amazon-ec2-trn1-instances-for-high-performance-model-training-are-now-available/)
5. **Amazon EC2 Trn1n instances ... are now generally available**，发布主体 AWS，发布日期：2023-04-13，核验日期：2026-09-05。[直接公告](https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-ec2-trn1n-instances-network-ai-models/)
6. **Amazon EC2 Trn1 instances**，发布主体 AWS，发布日期：页面日期未标明（当前产品页），核验日期：2026-09-05。[直接产品页](https://aws.amazon.com/ec2/instance-types/trn1/)
7. **Trn1 architecture**，发布主体 AWS Neuron，发布日期：页面日期未标明（在线文档），核验日期：2026-09-05。[直接页面](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trn1-arch.html)
8. **Scaling distributed training with AWS Trainium and Amazon EKS**，发布主体 AWS Machine Learning Blog，发布日期：2023-02-01，核验日期：2026-09-05。[直接文章](https://aws.amazon.com/blogs/machine-learning/scaling-distributed-training-with-aws-trainium-and-amazon-eks/)
