# AWS Inferentia2（v2）芯片证据页

- 研究截止日：2026-09-05
- 实际核验日：2026-09-05
- 厂商：Amazon Web Services（AWS）
- 产品层级：AI 推理芯片；对应的云产品是 Amazon EC2 Inf2
- 厂商总览：[AWS / 亚马逊云科技](./AWS-overview.md) · [[AWS-overview|图谱总览]]

## 一句话结论

Inferentia2 是 AWS 第二代推理专用芯片，每颗芯片包含 2 个 NeuronCore-v2；AWS Neuron 架构页给出的单芯片口径为 380 INT8 TOPS、190 FP16/BF16/cFP8/TF32 TFLOPS、47.5 FP32 TFLOPS、32 GiB HBM 和 820 GiB/s 带宽。[S1] 芯片流片、送样、晶圆量产及单独出货记录未在本次核验中确认，而 EC2 Inf2 已于 2023-04-13 GA。[S3][S4]

## 产品层级与对象边界

| 对象 | 本页如何使用 | 边界说明 |
|---|---|---|
| Inferentia2 | 芯片级事实 | 本页的算力、HBM、DMA 和 NeuronCore 数字默认指单颗芯片。 |
| NeuronCore-v2 | 芯片内部计算单元 | 2 个 NeuronCore-v2 构成一颗 Inferentia2；NeuronCore 不是独立 EC2 实例。[S1][S2] |
| EC2 Inf2 | 实例级事实 | 实例包含 1、6 或 12 颗芯片；实例总算力、总 HBM 和 EFA 不能回写为单芯片规格。[S4][S6] |
| Neuron SDK / NKI | 软件与编程接口 | 编译器、运行时、NKI 和框架支持不等于额外的芯片硬件或独立加速器。 |
| Inf2 UltraCluster、EFA、托管服务 | 系统/云事实 | 只说明部署和扩展方式；不作为芯片封装、片上内存或芯片数量的证据。 |

## 生命周期与可用性

| 阶段 | 截至研究截止日的证据判断 | 证据与边界 |
|---|---|---|
| 宣布 | 已确认事实：AWS 的 Inf2 GA 文章回顾其在 2022 年 re:Invent 作为预览发布。[S4] | 预览是产品公开节点，不能替代 tape-out 或芯片送样披露。 |
| 流片 / 工程样片 | 公开资料未确认 | 本次核验未找到 AWS 对 Inferentia2 tape-out、工程样片或封装验证日期的直接披露。 |
| 送样 | 公开资料未确认 | Inf2 预览/GA 只证明云端产品路径，未披露对外样片范围。 |
| 量产 | 公开资料未确认 | EC2 实例 GA 不是晶圆量产声明；AWS 未在核验资料中给出 Inferentia2 的晶圆、封装或累计量产数字。 |
| 出货 | 公开资料未确认 | 未找到按 Inferentia2 芯片单独披露的出货量或出货日期。 |
| 客户部署 | 厂商/客户采用主张：AWS 当前 Inferentia 产品页列出 Leonardo.ai、Deutsche Telekom、Qualtrics 等 Inf2 采用案例。[S5] | 这是 AWS 产品页和客户引述，不是独立部署审计，也没有统一的芯片数量口径。 |
| 云 / 实例可用 | 已确认事实：EC2 Inf2 于 2023-04-13 GA，提供 `inf2.xlarge`、`inf2.8xlarge`、`inf2.24xlarge` 和 `inf2.48xlarge`，GA 公告初始覆盖美国东部（弗吉尼亚北部、俄亥俄）。[S3][S4] | 这是实例层可用性；不能推导芯片级量产或区域库存。 |
| 路线图 | 公开资料未确认 | AWS 已公布后续 Trainium/Inferentia 家族信息，但本次资料没有给出 Inferentia2 的停产、EOL 或替代时间表。 |

## 芯片级规格

| 项目 | 公开口径 | 证据状态 |
|---|---|---|
| 计算单元 | 2 个 NeuronCore-v2 / 芯片。[S1] | 已确认事实 |
| INT8 算力 | 380 TOPS / 芯片。[S1] | 已确认事实 |
| FP16 / BF16 / cFP8 / TF32 算力 | 190 TFLOPS / 芯片。[S1] | 已确认事实；保留 AWS 的合并数据类型口径。 |
| FP32 算力 | 47.5 TFLOPS / 芯片。[S1] | 已确认事实 |
| 设备内存 | 32 GiB HBM / 芯片。[S1] | 已确认事实；GA 产品资料有时使用 GB，本页不擅自换算。 |
| 设备内存带宽 | 820 GiB/s / 芯片。[S1] | 已确认事实；与实例聚合带宽分开。 |
| DMA | 1 TB/s，支持内联压缩/解压缩。[S1] | 已确认事实；这是芯片数据搬运能力，不等同 EC2 网络带宽。 |
| 芯片间互联 | NeuronLink-v2 支持芯片间 collective compute 和扩展推理。[S1] | 能力已确认；本页不把实例页面的链路/网络聚合数回写成芯片额定值。 |
| 可编程能力 | NeuronCore-v2 ISA 支持动态形状和控制流，GPSIMD 路径支持 C++ 自定义算子。[S1][S2] | 硬件/编程能力已确认；不是对所有模型的性能保证。 |
| 制程、封装、功耗、片上 SRAM 容量 | 公开资料未确认 | 不以 EC2 服务器参数或软件 API 猜测。 |

## EC2 Inf2、实例互联与云边界

| 实例 | Inferentia2 芯片数 | 设备侧聚合口径 | 实例侧其他信息 |
|---|---:|---|---|
| `inf2.xlarge` | 1 | 32 GB/片加速器内存 | 4 vCPU、16 GB 实例内存；单芯片，无 NeuronLink。 |
| `inf2.8xlarge` | 1 | 32 GB/片加速器内存 | 32 vCPU、128 GB 实例内存；单芯片，无 NeuronLink。 |
| `inf2.24xlarge` | 6 | 192 GB 聚合加速器内存 | 96 vCPU、384 GB 实例内存；有 NeuronLink。 |
| `inf2.48xlarge` | 12 | 384 GB 聚合加速器内存 | 192 vCPU、768 GB 实例内存；有 NeuronLink。 |

实例表来自 AWS 的 Inf2 GA 文章和 Inf2 架构页。[S4][S6] 表中的 GB、实例内存、EFA 和 NeuronLink 位置属于实例层；不能把 `inf2.48xlarge` 的 2.3 PFLOPS、384 GB 或 9.8 TB/s 写成单颗 Inferentia2 的规格。[S3][S5]

## 架构与软件证据

- **NeuronCore-v2，已确认事实。** AWS 将 NeuronCore-v2 描述为支持动态执行/输入形状、控制流和 GPSIMD 自定义算子，并通过 NeuronLink-v2 支持分布式推理。[S1][S2]
- **软件栈，已确认事实。** Inf2 GA 资料说明 Neuron SDK 提供编译器、运行时和性能分析工具，且支持主流深度学习框架；具体模型是否可编译、是否达到目标性能取决于算子覆盖和编译配置。[S3][S4]
- **边界判断，分析推断。** 动态形状、控制流和自定义算子说明编程接口更灵活，但它们不能被改写成独立的搜索、向量数据库或额外片上存储硬件。

## 性能与采用证据

| 证据 | 可保留的表述 | 证据等级与限制 |
|---|---|---|
| Inf2 GA 公告 | AWS 宣称相对 Inf1 最高 4 倍吞吐、最高 10 倍低延迟；相对可比 EC2 实例最高 3 倍吞吐、最高 8 倍低延迟、最高 40% 更好价格性能。[S3] | 厂商比较主张；公告没有把结论扩展到所有模型、批量、精度、上下文长度和服务 SLA。 |
| AWS 当前 Inferentia 产品页 | AWS 当前页面保留 Inf2 的代际提升和客户采用案例，并列出 Leonardo.ai 等客户口径。[S5] | 客户/厂商主张；不能当作独立基准或统一工作负载实验。 |
| 官方客户引述 | Leonardo.ai、Runway、Qualtrics 等案例被 AWS 产品页用于说明成本、吞吐或分布式推理效果。[S5] | 缺少可横向复现的完整模型、批量、精度、功耗和价格条件，本页不抽取为独立数值。 |
| 独立验证 | 本次核验未定位到满足相同模型、精度、批量、延迟和功耗条件的独立 Inferentia2 芯片级对比。 | 公开资料未确认独立统一基准。 |

## 未确认项与冲突

1. **芯片、实例和网络三层不能混写。** 380 INT8 TOPS、190 TFLOPS、32 GiB HBM 和 820 GiB/s 是单芯片口径；2.3 PFLOPS、384 GB、9.8 TB/s 等是 `inf2.48xlarge` 的实例聚合口径。[S1][S5]
2. **GB 与 GiB 的单位差异。** Neuron 架构页使用 GiB，EC2 发布材料常使用 GB；本页保留来源单位，不把它们宣称为一个经过换算的精确值。
3. **NeuronLink 数字未升级为芯片事实。** 实例页面可展示链路或网络聚合值，但本次核验的芯片页只确认 NeuronLink-v2 能力，未采用未明确标注层级的数值。
4. **公开资料未确认** tape-out、工程样片、送样、晶圆量产、累计出货、制程、封装、TDP、停产和每个区域的现时库存。

## 直接来源

核验日期均为 2026-09-05；在线文档和当前产品页未显示独立发布日期时，明确标注为“页面日期未标明”。

1. **Inferentia2 — AWS Neuron architecture**，发布主体 AWS Neuron，发布日期：页面日期未标明（在线文档），核验日期：2026-09-05。[直接页面](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/inferentia2.html)
2. **NeuronCore-v2 — AWS Neuron architecture**，发布主体 AWS Neuron，发布日期：页面日期未标明（在线文档），核验日期：2026-09-05。[直接页面](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/neuron-core-v2.html)
3. **Amazon EC2 Inf2 instances for generative AI are generally available**，发布主体 AWS，发布日期：2023-04-13，核验日期：2026-09-05。[直接公告](https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-ec2-inf2-instances-generative-ai-generally-available/)
4. **Amazon EC2 Inf2 instances for low-cost, high-performance generative AI inference are now generally available**，发布主体 AWS News Blog，发布日期：2023-04-13，核验日期：2026-09-05。[直接文章](https://aws.amazon.com/blogs/aws/amazon-ec2-inf2-instances-for-low-cost-high-performance-generative-ai-inference-are-now-generally-available/)
5. **AWS Inferentia — AI inference chip**，发布主体 AWS，发布日期：页面日期未标明（当前产品页），核验日期：2026-09-05。[直接产品页](https://aws.amazon.com/ai/machine-learning/inferentia/)
6. **Inf2 architecture**，发布主体 AWS Neuron，发布日期：页面日期未标明（在线文档），核验日期：2026-09-05。[直接页面](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/inf2-arch.html)
