# AWS Trainium2（v3）芯片证据页

- 研究截止日：2026-09-05
- 实际核验日：2026-09-05
- 厂商：Amazon Web Services（AWS）
- 产品层级：AI 训练与推理加速芯片；对应产品为 EC2 Trn2 实例和 Trn2 UltraServer
- 导航：[AWS Trainium / Inferentia 综合报告](06-aws-trainium.md)

## 一句话结论

Trainium2 是 AWS 第三代 NeuronDevice、Trainium 家族的第二代芯片，单颗芯片含 8 个 NeuronCore-v3；当前 AWS Neuron 架构页给出 1,299 FP8 TFLOPS、667 BF16/FP16/TF32 TFLOPS、96 GiB HBM、2.9 TB/s 带宽、3.5 TB/s DMA 和 1.28 TB/s/chip NeuronLink-v3。[S1] Trn2 实例已于 2024-12-03 GA，而同一发布中 Trn2 UltraServer 是预览；截至本次核验，后续 UltraServer GA 公告、芯片 tape-out、送样、量产和单独出货记录仍未确认。[S2][S3]

## 产品层级与对象边界

| 对象 | 本页如何使用 | 边界说明 |
|---|---|---|
| Trainium2 | 芯片级事实 | 算力、HBM、DMA、NeuronCore 和芯片级互联数字默认指单颗芯片。 |
| NeuronCore-v3 | 芯片内部计算单元 | 8 个 NeuronCore-v3 构成一颗 Trainium2；“v3”是 NeuronCore 代际，不是 Trainium3 芯片。[S1] |
| EC2 Trn2 | 实例级事实 | `trn2.3xlarge`、`trn2.48xlarge` 等实例的芯片数和聚合资源独立记录。 |
| Trn2 UltraServer | 服务器级组合 | 由 4 个 `trn2u.48xlarge` 组成、共 64 颗 Trainium2；服务器总内存、总算力和网络不能回写为单芯片规格。[S4][S5] |
| UltraCluster / EFAv3 | 集群与系统级事实 | 用于多 UltraServer 扩展；不是 Trainium2 的片上内存或出货量证据。 |
| Neuron SDK / NKI | 软件与编程接口 | 编译器、NKI、运行时和框架支持不能单独证明芯片硬件规格。 |

## 生命周期与可用性

| 阶段 | 截至研究截止日的证据判断 | 证据与边界 |
|---|---|---|
| 宣布 | 已确认事实：AWS 于 2023-11-28 正式公布 Trainium2，称其面向大模型训练，并给出相对前代的性能、内存和能效目标。[S2] | 这是产品宣布和厂商目标，不是量产证明。发布页中的原型图片也不足以确认工程样片阶段。 |
| 流片 / 工程样片 | 公开资料未确认 | AWS 发布页展示了标注为 prototype 的图片，但没有披露 tape-out、工程样片测试或封装验证时间。[S2] |
| 送样 | 公开资料未确认 | 本次核验未找到 AWS 对外送样对象、数量或送样批次的直接披露。 |
| 量产 | 公开资料未确认 | Trn2 实例 GA 和后续 Project Rainier 采用叙述不能替代晶圆、封装测试或累计量产披露。 |
| 出货 | 公开资料未确认 | 未找到按 Trainium2 芯片单独披露的首批出货日期、累计出货量或库存数字。 |
| 客户部署 | 厂商/客户采用主张：AWS 在 2025-11-03 的回顾中称 Project Rainier 已有近 500,000 颗定制 Trainium2 芯片投入使用，Anthropic 已用其训练和运行 Claude。[S6] | 这是 AWS 对平台和客户部署的公开主张，不是第三方审计；“投入使用”也不等同于公开的芯片出货统计。 |
| 云 / 实例可用 | 已确认事实：Trn2 实例于 2024-12-03 GA；同一发布将 Trn2 UltraServer 标为 preview。[S3] 当前 EC2 产品页列出 `trn2u.48xlarge`，但本次核验未找到后续明确宣布 UltraServer GA 的公告。[S5] | 因此 Trn2 实例为 GA；UltraServer 的后续 GA 状态写为公开资料未确认。当前产品页同时出现“available now”的营销引文与“available in preview”的产品细节，属于状态表述冲突，不能单凭前者升级为 GA。 |
| 路线图 | 公开资料未确认 | Trainium3 已有后续产品公告，但不构成 Trainium2 的停产、EOL 或剩余库存时间表。 |

## 芯片级规格

| 项目 | 公开口径 | 证据状态 |
|---|---|---|
| 计算单元 | 8 个 NeuronCore-v3 / 芯片。[S1] | 已确认事实 |
| FP8 算力 | 1,299 TFLOPS / 芯片。[S1] | 已确认事实；采用 AWS Neuron 页的 FP8 口径。 |
| BF16 / FP16 / TF32 算力 | 667 TFLOPS / 芯片。[S1] | 已确认事实 |
| 稀疏算力 | 2,563 TFLOPS，覆盖 sparse FP8/FP16/BF16/TF32 口径。[S1] | 已确认事实；稀疏口径不与 dense 算力相加。 |
| FP32 算力 | 181 TFLOPS / 芯片。[S1] | 已确认事实 |
| 设备内存 | 96 GiB HBM / 芯片。[S1] | 已确认事实；实例资料常写 96 GB/1.5 TB 等聚合值，单位和层级分开保留。 |
| 设备内存带宽 | 2.9 TB/s / 芯片。[S1] | 已确认事实；与 UltraServer 聚合带宽分开。 |
| DMA | 3.5 TB/s，支持内联压缩/解压缩。[S1] | 已确认事实；这是芯片内数据搬运能力。 |
| 芯片间互联 | NeuronLink-v3，1.28 TB/s per chip，支持 scale-out 和内存池化。[S1] | 已确认事实；Trn2 架构页的实例内互联表使用另一层级/单位，见冲突说明。 |
| 集合通信 | 16 个 CC-Cores。[S1] | 已确认事实；不等同于 NeuronCore 数量。 |
| 编程能力 | 支持 logical NeuronCore（LNC）、动态形状、控制流、可编程舍入和 GPSIMD 自定义算子。[S1] | 硬件/编程能力已确认；不能推出任意模型都无需改写。 |
| 制程、封装、功耗、片上 SRAM 容量 | 公开资料未确认 | 不使用服务器级电源或后代芯片资料代填。 |

## EC2 Trn2、UltraServer 与集群边界

| 对象 | Trainium2 芯片数 | 设备侧聚合口径 | 服务器/网络侧信息 |
|---|---:|---|---|
| `trn2.3xlarge` | 1 | 96 GB 级加速器内存 | 12 vCPU、128 GB 主机内存；非 UltraServer。 |
| `trn2.48xlarge` | 16 | 1.5 TB 加速器内存；最高 20.8 FP8 PFLOPS | 192 vCPU、2 TB 主机内存；3.2 Tbps EFAv3。 |
| `trn2u.48xlarge` | 16 | 1.5 TB 加速器内存；作为 UltraServer 构件 | 192 vCPU、2 TB 主机内存；产品页标记为 EC2 UltraServer 构件。 |
| Trn2 UltraServer | 64 | 6 TB 加速器内存；最高 83.2 FP8 PFLOPS；约 185 TB/s 聚合带宽 | 4 个 `trn2u.48xlarge`；最高 12.8 Tbps EFAv3。[S4][S5] |
| Trn2 UltraCluster | 多个 Trn2 / UltraServer | 平台聚合资源 | 2023 公布的目标为最多 100,000 颗芯片；发布时 Trn2 文章使用“tens of thousands”等表述。[S2][S3] |

表中 TB、GB 和 PFLOPS 均保留 AWS 实例产品页的聚合口径。[S4][S5] UltraServer/UltraCluster 的数字只用于说明云平台拓扑，不应被写成单颗 Trainium2 的 HBM、算力或出货数量。

## 架构与软件证据

- **NeuronCore-v3，已确认事实。** AWS Neuron 将 Trainium2 定义为包含 8 个 NeuronCore-v3 的 NeuronDevice，并提供 LNC，把多个物理核心组合为逻辑计算单元。[S1]
- **互联与扩展，已确认事实。** Trn2 实例使用 4×4 的 2D Torus 和 NeuronLink；UltraServer 由四个 16 芯片实例组成，具体拓扑、EFAv3 和地址路由属于服务器/系统层。[S4]
- **软件栈，已确认事实。** AWS Trn2 产品页列出 Neuron SDK、NKI、主流框架和模型支持路径；这些是可编程/软件交付能力，不能直接等同于芯片上存在某种应用级算子或检索单元。[S5]
- **边界判断，分析推断。** LNC 与内存池化有利于将大模型训练/推理映射到多芯片拓扑，但实际性能仍取决于并行策略、编译版本、模型算子和通信模式。

## 性能与采用证据

| 证据 | 可保留的表述 | 证据等级与限制 |
|---|---|---|
| Trainium2 发布公告 | AWS 宣称最高 4 倍训练速度、3 倍内存容量和 2 倍性能/功耗，并计划 Trn2 及最多 100,000 芯片的 UltraCluster。[S2] | 厂商目标/主张；不能当作独立测量或已完成交付。 |
| Trn2 GA 文章与产品页 | AWS 给出 Trn2 16 芯片、20.8 FP8 PFLOPS 及 UltraServer 64 芯片、83.2 FP8 PFLOPS 等平台口径。[S3][S5] | 服务器/实例聚合规格；不应回写为单芯片算力。 |
| Project Rainier | AWS 称近 500,000 颗 Trainium2 已投入 Project Rainier，Anthropic 训练/运行 Claude。[S6][S7] | AWS/客户部署主张；没有公开逐芯片序列、第三方审计或独立能效测试。 |
| 独立验证 | 本次核验未定位到满足相同模型、精度、批量、并行、延迟和功耗边界的独立 Trainium2 芯片级对比。 | 公开资料未确认统一独立基准。 |

## 未确认项与冲突

1. **Trainium2、NeuronCore-v3 与 Trainium3 不同层级。** Trainium2 页面中的 “v3” 指核心代际；Trainium3 是后续芯片家族，不能按编号直接合并。
2. **NeuronLink 数值的层级差异。** 芯片页给出 1.28 TB/s per chip；Trn2 架构页展示实例内部互联表时使用 1,024 GB/s/chip 等口径。两者未在同一页面定义为可直接换算的同一指标，本页不强行统一。
3. **UltraServer 状态存在时间边界和页面内冲突。** 2024-12-03 发布明确写 Trn2 GA、UltraServer preview；当前产品页列出 `trn2u.48xlarge`，并同时出现“available now”引文与“available in preview”细节，但没有给出后续 GA 日期。因此 UltraServer GA 仍标为公开资料未确认。
4. **近 500,000 颗是平台部署主张。** Project Rainier 的“投入使用”数字不能转换成 Trainium2 单独出货量，也不能证明全部芯片均对应 EC2 Trn2 公有实例。
5. **公开资料未确认** tape-out、工程样片、对外送样、晶圆量产、累计芯片出货、制程、封装、TDP、停产时间和区域库存。

## 直接来源

核验日期均为 2026-09-05；在线文档和当前产品页未显示独立发布日期时，明确标注为“页面日期未标明”。

1. **Trainium2 — AWS Neuron architecture**，发布主体 AWS Neuron，发布日期：页面日期未标明（在线文档），核验日期：2026-09-05。[直接页面](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium2.html)
2. **AWS unveils next-generation AWS-designed chips**，发布主体 Amazon / AWS Press Center，发布日期：2023-11-28，核验日期：2026-09-05。[直接新闻稿](https://press.aboutamazon.com/2023/11/aws-unveils-next-generation-aws-designed-chips)
3. **Amazon EC2 Trn2 instances and Trn2 UltraServers for AI/ML training and inference are now available**，发布主体 AWS News Blog，发布日期：2024-12-03，核验日期：2026-09-05。[直接文章](https://aws.amazon.com/blogs/aws/amazon-ec2-trn2-instances-and-trn2-ultraservers-for-aiml-training-and-inference-is-now-available/)
4. **Trn2 architecture**，发布主体 AWS Neuron，发布日期：页面日期未标明（在线文档），核验日期：2026-09-05。[直接页面](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trn2-arch.html)
5. **Amazon EC2 Trn2 instances**，发布主体 AWS，发布日期：页面日期未标明（当前产品页），核验日期：2026-09-05。[直接产品页](https://aws.amazon.com/ec2/instance-types/trn2/)
6. **AWS Weekly Roundup: Project Rainier online, Amazon Nova, Amazon Bedrock, and more**，发布主体 AWS News Blog，发布日期：2025-11-03，核验日期：2026-09-05。[直接文章](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-project-rainier-online-amazon-nova-amazon-bedrock-and-more-november-3-2025/)
7. **AWS Project Rainier: AI compute cluster built with Trainium2**，发布主体 About Amazon，发布日期：页面日期未标明（当前专题页），核验日期：2026-09-05。[直接文章](https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster?linkId=872917983)
8. **AWS Trainium customers**，发布主体 AWS，发布日期：页面日期未标明（当前客户页），核验日期：2026-09-05。[直接客户页](https://aws.amazon.com/ai/machine-learning/trainium/customers/)
