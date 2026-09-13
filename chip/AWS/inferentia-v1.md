# AWS Inferentia（v1）芯片证据页

- 研究截止日：2026-09-05
- 实际核验日：2026-09-05
- 厂商：Amazon Web Services（AWS）
- 产品层级：AI 推理芯片；对应的云产品是 Amazon EC2 Inf1
- 厂商总览：[AWS / 亚马逊云科技](./AWS-overview.md) · [[AWS-overview|图谱总览]]

## 一句话结论

Inferentia v1 是 AWS 第一代推理专用芯片，每颗芯片包含 4 个 NeuronCore-v1，公开 Neuron 架构资料给出 128 INT8 TOPS、64 FP16/BF16 TFLOPS、8 GiB 设备 DRAM 和 50 GiB/s 带宽；芯片级流片、送样、晶圆量产和出货记录没有在本次核验的公开资料中确认，但搭载它的 EC2 Inf1 已于 2019-12-03 正式可用。[S1][S3][S4]

## 产品层级与对象边界

| 对象 | 本页如何使用 | 边界说明 |
|---|---|---|
| Inferentia v1 | 芯片级事实 | AWS 的第一代推理加速器；本页的规格默认指单颗芯片。 |
| NeuronCore-v1 | 芯片内部计算单元 | 不是另一颗芯片；4 个 NeuronCore-v1 组成一颗 Inferentia v1。 |
| EC2 Inf1 | 实例级事实 | 一台实例可包含 1、4 或 16 颗 Inferentia；实例总吞吐和设备内存不能回写为单芯片规格。[S1] |
| Neuron SDK / Neuron Runtime | 软件事实 | 编译器、运行时和框架支持不等于芯片新增硬件单元。 |
| Inf1 上的服务器、EFA、云区域 | 系统/云事实 | 只用于说明实例可用性和扩展边界，不代表芯片封装或芯片互联的独立规格。 |

## 生命周期与可用性

| 阶段 | 截至研究截止日的证据判断 | 证据与边界 |
|---|---|---|
| 宣布 | 已确认事实：2018-11-28 AWS 宣布 Inferentia，公告使用“将可用于”表述，并列出 SageMaker、EC2 和 Elastic Inference 作为计划承载产品。[S3] | 这是产品宣布和计划，不是芯片送样或实例 GA。 |
| 流片 / 工程样片 | 公开资料未确认 | 本次核验未找到 AWS 对 Inferentia v1 tape-out、工程样片或封装验证日期的直接披露。 |
| 送样 | 公开资料未确认 | EC2 产品发布不能反推芯片曾以何种形式对外送样。 |
| 量产 | 公开资料未确认 | Inf1 GA 证明云实例可销售，不提供晶圆代工、封装测试或芯片累计量产数字。 |
| 出货 | 公开资料未确认 | 本次核验未找到按 Inferentia v1 单独披露的出货量或出货日期。 |
| 客户部署 | 厂商/客户采用主张：AWS 2020 年回顾称已有客户和 Amazon 服务将 Inf1 用于生产工作负载，并举例 Alexa TTS 迁移。[S5] | 这是 AWS 的客户采用叙述，不是独立部署审计，也没有给出芯片数量。 |
| 云 / 实例可用 | 已确认事实：EC2 Inf1 于 2019-12-03 GA，提供四种实例规格，初始公告覆盖美国东部（弗吉尼亚北部）和美国西部（俄勒冈）。[S4] | 这是 EC2 实例层可用性；不等于 AWS 公布了芯片量产状态。2020 年 AWS 又宣布扩展到五个区域。[S5] |
| 路线图 | 公开资料未确认 | Inferentia2 的出现只能证明后续代际存在，不能据此推断 v1 的停产、EOL 或剩余库存。 |

## 芯片级规格

下表只记录单颗 Inferentia v1 或其内部 NeuronCore-v1 的资料；Inf1 的聚合数字另列在后文。

| 项目 | 公开口径 | 证据状态 |
|---|---|---|
| 计算单元 | 4 个 NeuronCore-v1 / 芯片。[S1] | 已确认事实 |
| NeuronCore-v1 结构 | 每个 NeuronCore-v1 是独立的异构计算单元，包含 Tensor、Vector、Scalar 引擎和软件管理的 SRAM。[S2] | 已确认事实 |
| INT8 算力 | 128 TOPS / 芯片。[S1] | 已确认事实；数据类型和计量单位按 AWS Neuron 文档保留。 |
| FP16 / BF16 算力 | 64 TFLOPS / 芯片。[S1] | 已确认事实；不能与 Inf1 实例总值混用。 |
| 设备内存 | 8 GiB device DRAM。[S1] AWS 产品页同时写作 8 GB DDR4。[S6] | 已确认事实；两个页面的单位/命名不同，本页不擅自换算。 |
| 设备内存带宽 | 50 GiB/s。[S1] | 已确认事实；产品页采用 GB/s 口径时不与 GiB/s 强行等同。 |
| 片上 SRAM 容量 | NeuronCore-v1 使用软件管理的 SRAM；本次核验的直接页面没有给出每颗芯片的容量数字。[S2] | 部分确认；容量公开资料未确认。 |
| 芯片间互联 | NeuronLink-v1 用于多芯片协同；本次芯片页面未单独给出链路额定带宽。[S1] | 能力已确认；芯片级数字公开资料未确认。 |
| 支持数据类型 | Neuron 架构页列出 FP16、BF16、FP32、INT8 等类型。[S1][S2] | 已确认事实；支持类型不等于每种类型都有同一算力。 |
| 制程、封装、功耗 | 公开资料未确认 | 本次核验不以 EC2 服务器功耗或后代工艺信息代填。 |

## EC2 Inf1、服务器与互联边界

| 实例 | Inferentia 芯片数 | 设备侧聚合口径 | 实例侧其他信息 |
|---|---:|---|---|
| Inf1.xlarge | 1 | 64 FP16/BF16 TFLOPS、128 INT8 TOPS、8 GiB 设备内存 | 4 vCPU、8 GiB 主机内存；无 NeuronLink。 |
| Inf1.2xlarge | 1 | 同上 | 8 vCPU、16 GiB 主机内存；无 NeuronLink。 |
| Inf1.6xlarge | 4 | 256 FP16/BF16 TFLOPS、512 INT8 TOPS、32 GiB 设备内存 | 24 vCPU、48 GiB 主机内存；NeuronLink-v1，文档给出 32 GiB/s/chip 的实例互联口径。 |
| Inf1.24xlarge | 16 | 1,024 FP16/BF16 TFLOPS、2,048 INT8 TOPS、128 GiB 设备内存 | 96 vCPU、192 GiB 主机内存；NeuronLink-v1，文档给出 32 GiB/s/chip 的实例互联口径。 |

以上是 `inf1-arch` 的实例表；其中的总算力、总设备内存和 NeuronLink 数字属于实例/多芯片拓扑，不应当写入芯片规格表。[S7]

## 架构与软件证据

- **芯片架构，已确认事实。** NeuronCore-v1 将 Tensor、Vector、Scalar 三类执行引擎组合在一个独立计算单元中，并让软件管理片上 SRAM；Neuron 文档还给出每个 Tensor 引擎 16 FP16/BF16 TFLOPS 的口径。[S2]
- **软件栈，已确认事实。** AWS 的 Inf1 GA 公告说明 Neuron SDK 提供编译器、运行时和性能分析工具，并与 TensorFlow、PyTorch、MXNet 预集成。[S4] 2018 年公告还列出 ONNX 支持计划。[S3]
- **边界判断，分析推断。** NeuronCore 的编程模型可以解释为什么 AWS 能在实例层提供模型编译和流水线能力，但不能从 SDK、框架或运行时页面推导出未被硬件页面明确列出的片上搜索、稀疏或额外专用单元。

## 性能与采用证据

| 证据 | 可保留的表述 | 不能扩大的结论 |
|---|---|---|
| AWS Inf1 GA 公告 | AWS 宣称相对 EC2 G4 最高 3 倍吞吐、每次推理成本降低最高 40%。[S4] | 这是 AWS 的比较主张；公告未构成独立复测，也不说明适用于所有模型、批量和延迟目标。 |
| AWS 当前 Inferentia 产品页 | AWS 当前页面给出相对可比 EC2 最高 2.3 倍吞吐、最高 70% 成本下降，并列出多家采用 Inf1 的客户。[S6] | 该页面与 2019 GA 公告的比较基线/数字不同；本页保留差异，不择一当作普适性能。 |
| AWS 2020 Inf1 回顾 | AWS 称客户和 Amazon 服务已将 Inf1 用于生产工作负载，并具体提到 Alexa TTS。[S5] | 属于 AWS/客户案例主张；未给出完整模型、批量、精度、功耗和独立测试数据。 |
| 独立验证 | 本次核验未定位到满足相同模型、精度、批量、延迟和功耗条件的独立 Inferentia v1 芯片级对比。 | 因此不填写独立吞吐、能效或成本数字。 |

## 未确认项与冲突

1. **芯片状态不能由实例状态替代。** Inf1 GA 和客户生产使用已经确认云产品成熟度，但不能证明具体晶圆批次、封装量产、累计出货或芯片库存。
2. **8 GB 与 8 GiB 的单位差异。** AWS 产品页写 8 GB DDR4，Neuron 架构页写 8 GiB device DRAM；来源页面没有在本次核验中给出统一换算说明，因此按原页面分别保留。
3. **芯片与实例算力边界。** 128 INT8 TOPS 和 64 FP16/BF16 TFLOPS 是单颗芯片口径；2,048 INT8 TOPS 等是 16 芯片 Inf1.24xlarge 的聚合值。
4. **公开资料未确认** tape-out、工程样片、对外送样、晶圆量产、累计出货、制程节点、封装、TDP、退市时间和当前每个区域的库存。

## 直接来源

核验日期均为 2026-09-05；在线文档/当前产品页未显示独立发布日期时，明确标注为“页面日期未标明”。

1. **Inferentia — AWS Neuron architecture**，发布主体 AWS Neuron，发布日期：页面日期未标明（在线文档），核验日期：2026-09-05。[直接页面](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/inferentia.html)
2. **NeuronCore-v1 — AWS Neuron architecture**，发布主体 AWS Neuron，发布日期：页面日期未标明（在线文档），核验日期：2026-09-05。[直接页面](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/neuron-core-v1.html)
3. **Announcing Amazon Inferentia machine learning inference microchip**，发布主体 AWS，发布日期：2018-11-28，核验日期：2026-09-05。[直接公告](https://aws.amazon.com/about-aws/whats-new/2018/11/announcing-amazon-inferentia-machine-learning-inference-microchip/)
4. **Introducing Amazon EC2 Inf1 instances**，发布主体 AWS，发布日期：2019-12-03，核验日期：2026-09-05。[直接公告](https://aws.amazon.com/about-aws/whats-new/2019/12/introducing-amazon-ec2-inf1-instances-high-performance-and-the-lowest-cost-machine-learning-inference-in-the-cloud/)
5. **Amazon EC2 Inf1 instances ... now available in five new regions and with improved performance**，发布主体 AWS Machine Learning Blog，发布日期：2020-08-13，核验日期：2026-09-05。[直接文章](https://aws.amazon.com/blogs/machine-learning/amazon-ec2-inf1-instances-featuring-aws-inferentia-chips-now-available-in-five-new-regions-and-with-improved-performance/)
6. **AWS Inferentia — AI inference chip**，发布主体 AWS，发布日期：页面日期未标明（当前产品页），核验日期：2026-09-05。[直接产品页](https://aws.amazon.com/ai/machine-learning/inferentia/)
7. **Inf1 architecture**，发布主体 AWS Neuron，发布日期：页面日期未标明（在线文档），核验日期：2026-09-05。[直接页面](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/inf1-arch.html)
