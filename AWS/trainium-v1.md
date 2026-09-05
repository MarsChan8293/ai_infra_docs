# Amazon Web Services / 亚马逊云科技 — Trainium（v1）

- 拆分日期：2026-09-02
- 产品层级：芯片/EC2 实例边界
- 综合报告：[06-aws-trainium.md](./06-aws-trainium.md)
- 文件性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容逐行摘录综合报告，保留原报告中的状态、数字、证据等级和未知项。

> 第 27 行：|Inferentia（v1）|4 个 NeuronCore-v1；8 GB DDR4、50 GB/s；128 INT8 TOPS、64 FP16/BF16 TFLOPS。[架构文档](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/inferentia.html)|2018-11-28 首次公开；Inf1 于 2019-12 GA（AWS 后续回顾）。|AWS 列出 Finch AI、Sprinklr、Money Forward、Amazon Alexa；Amazon Search 和 ByteDance 也有 AWS 案例入口。[产品页](https://aws.amazon.com/ai/machine-learning/inferentia/)|公开资料未确认具体 tape-out、送样、晶圆量产、出货量；未查到停产公告。|
> 第 28 行：|Trainium（v1，NeuronCore-v2）|2 个 NeuronCore-v2；32 GiB HBM、0.8 TB/s；191 FP8、191 BF16/FP16/TF32、48 FP32 TFLOPS；NeuronLink-v2 384 GB/s/chip。[架构文档](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium.html)|2020-11 re:Invent 公开路线；Trn1 预览 2021-11-30，GA 2022-10-10；Trn1n GA 2023-04-13。[Trn1 GA](https://aws.amazon.com/blogs/aws/amazon-ec2-trn1-instances-for-high-performance-model-training-are-now-available/)、[Trn1n GA](https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-ec2-trn1n-instances-network-ai-models/)|Ricoh、Helixon、Money Forward、Magic、Cactus、Watashiha 等案例在 Trn1 产品页；Trn1/Trn1n 已面向生产使用。[客户案例](https://aws.amazon.com/ec2/instance-types/trn1/)|公开资料未确认 tape-out、送样、量产和累计出货；未查到停产公告。|
> 第 29 行：|Inferentia2（v2，NeuronCore-v2）|2 个 NeuronCore-v2；32 GB HBM；190 FP16/BF16/cFP8/TF32 TFLOPS、47.5 FP32 TFLOPS；NeuronLink 384 GB/s/chip。[架构文档](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/inferentia2.html)|2022 re:Invent 预览；Inf2 GA 2023-04-13，4 种实例规格、最多 12 颗芯片，初始公开区域为 us-east-1/us-east-2。[GA 公告](https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-ec2-inf2-instances-generative-ai-generally-available/)|AWS 列出 Leonardo.ai、Deutsche Telekom、Qualtrics；Inf2 支持 175B 级模型的单实例分片。[产品页](https://aws.amazon.com/ai/machine-learning/inferentia/)|公开资料未确认 tape-out、送样、量产和累计出货；未查到停产公告。|
> 第 30 行：|Trainium2（v3，NeuronCore-v3）|8 个 NeuronCore-v3；96 GiB HBM、2.9 TB/s；1,299 FP8、667 BF16/FP16/TF32、181 FP32 TFLOPS；3.5 TB/s DMA、1.28 TB/s/chip NeuronLink、16 CC-Cores。[架构文档](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium2.html)|AWS 于 2023-11 公开下一代；Trn2 实例 GA 2024-12-03，Trn2 UltraServer 当时为 preview；Neuron 2.21 于 2024-12-23 增加 Trn2 支持。[Trn2 公告](https://aws.amazon.com/blogs/aws/amazon-ec2-trn2-instances-and-trn2-ultraservers-for-aiml-training-and-inference-is-now-available/)|AWS 称数万 Trainium 已支撑服务，Trn2 已用于 Amazon Bedrock 的 Llama 3.1 405B、Claude 3.5 Haiku；Project Rainier 由 Anthropic 使用 Trainium2，属于客户/平台部署叙述。[Project Rainier](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-project-rainier-amazon-cloudwatch-investigations-aws-mcp-servers-and-more-june-30-2025/)|公开资料未确认 Trainium2 tape-out、送样、晶圆量产和累计出货；未查到停产公告。|
> 第 31 行：|Trainium3（v4，NeuronCore-v4）|8 个 NeuronCore-v4；144 GiB/GB HBM3e、产品页 4.9 TB/s（NKI 指南 4.7 TB/s）；2.52 PFLOPS MXFP8/MXFP4；128 DMA、20 CC-Cores、4 个 NeuronLink-v4。[NKI 架构](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html)|Trn3 UltraServer GA 2025-12-02；最多 144 颗芯片，进入 EC2 UltraClusters 3.0。具体 Trn3 EC2 instance type、区域和公开价格在本次已打开资料中未完整确认。[产品页](https://aws.amazon.com/ec2/instance-types/trn3/)|AWS 宣称 Bedrock 上 Trainium3 是最快加速器；客户页的 Anthropic、Decart、Hugging Face 等内容需要按“公司/AWS 客户页主张”读取，不能等同第三方复测。[客户页](https://aws.amazon.com/ai/machine-learning/trainium/customers/)|公开资料未确认 tape-out、送样、晶圆量产、2026 出货量、真实库存或停产；GA/云端产品可用不等于已公开量产数字。|
> 第 33 行：
> 第 34 行：**代际命名提醒。** AWS Neuron 文档把 Trainium / Inferentia2 归入 NeuronCore-v2，把 Trainium2 归入 v3，把 Trainium3 归入 v4；“Trainium1/2/3”是产品代际，“NeuronCore-v1/v2/v3/v4”是核心架构代际，不能混成同一列。Inf1/Trn1/Inf2/Trn2/Trn3 是 EC2 实例或平台名称，也不能反推单颗芯片数量。
> 第 35 行：
> 第 41 行：|2019-12|Inf1/Inferentia GA。|AWS 后续官方博客回顾；未找到当日 GA 原始公告。|
> 第 42 行：|2020-11|re:Invent 公开 Trainium，目标为 2021 年下半年。|官方 re:Invent 直播记录；目标日期不等于出货。|
> 第 43 行：|2021-11-30|Trn1 预览。|官方 What's New。|
> 第 44 行：|2022-10-10|Trn1 GA。|官方 AWS News Blog。|
> 第 45 行：|2022 re:Invent|Inferentia2/Inf2 预览。|官方 Inf2 GA 博客回顾。|
> 第 58 行：- **芯片：** AWS 自研加速器，不向客户单独购买裸片；本报告不把芯片型号当成可直接采购的 PCIe 卡。
> 第 59 行：- **实例/服务器：** Inf1、Inf2、Trn1/Trn1n、Trn2 是 EC2 实例产品；Trn2/Trn3 UltraServer 是更大 scale-up 平台，不能把平台 HBM、带宽和 PFLOPS 回填为单芯片规格。
> 第 60 行：- **集群/云服务：** UltraCluster 是跨服务器的网络与调度边界；Amazon Bedrock 是托管模型 API。Bedrock 上的模型可用只证明云服务路径存在，不证明用户能租到对应的裸芯片或固定 Trn3 拓扑。
> 第 61 行：- **客户部署：** AWS 的 Trn1 客户案例和 Inferentia 客户名单是采用证据；Project Rainier、Anthropic 的近百万 Trainium2 口径是 AWS 客户页/博客中的公司叙述；对 Trainium3 只能写“产品 GA/客户页提及”，不把“预计继续扩展”写成已完成装机。
> 第 62 行：- **Inferentia 与 Trainium 的角色：** Inferentia 优先面向推理，Trainium 优先面向训练，但 Trainium 实例也可用于推理。架构、软件和实例边界比营销标签更重要。
> 第 63 行：
> 第 67 行：|---|---|---|
> 第 68 行：|制程/执行单元|3nm；8 个 NeuronCore-v4，每核含 Tensor、Vector、Scalar、GpSimd。[AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/)|144 颗芯片，36 台服务器、每台 4 颗。[架构表](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html)|
> 第 69 行：|格式/计算|FP32、BF16、MXFP8、MXFP4；GA 口径每芯片 [2.52 PFLOP FP8](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)。| [362,448 MXFP8/MXFP4 TFLOPS](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html)；FP16/BF16/TF32 为 96,624 TFLOPS。|
> 第 114 行：
> 第 115 行：截至 2026-09-01，本次没有找到把 Trainium3 与 H200/B200 在同一模型、同一 batch、同一精度、同一服务栈和同一价格口径下复测的第三方结果。一个公开的独立测试页面报告了 Trn1 的 32-core 独立分片吞吐、Trn2 的 70B LoRA / Mixtral 端到端验证，但明确说这些实验不是统一的 price-performance benchmark。[BrazenLab Trainium Validation Evidence](https://brazenlab.ai/research.html)
> 第 116 行：
> 第 122 行：|AWS Neuron NKI/库函数|API/编程能力已公开；包括 segmented attention、KV-parallel prefill、Gather、Top-k Reduce 等|不能写成硬件已有独立 Search Core，或证明每 token 的跨卡通信量已降到某个复杂度|
> 第 123 行：|BrazenLab Trn1/Trn2|独立作者公开了可复核的实验范围与部分结果|不能把 Trn1/Trn2 结果外推成 Trainium3；不能把独立分片吞吐当单作业延迟|
> 第 124 行：|MLCommons Training v6.0 公共参考/结果索引|本次查验未定位到 AWS Trainium/Inferentia 的 MLPerf 正式提交|不能据此证明全球绝对没有任何其他第三方基准，也不能把 reference implementation 当提交结果。[MLCommons training](https://github.com/mlcommons/training)、[MLCommons results](https://github.com/mlcommons/training_results_v6.0)|
> 第 125 行：
> 第 166 行：7. [NKI Library kernels](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/nki/library/api/index.html)
> 第 167 行：8. [AWS Trainium customers](https://aws.amazon.com/ai/machine-learning/trainium/customers/)
> 第 168 行：9. [AWS Inferentia customers/product page](https://aws.amazon.com/ai/machine-learning/inferentia/)
> 第 169 行：10. [AWS OpenAI strategic partnership：Trainium4 2027 roadmap](https://press.aboutamazon.com/2026/2/openai-and-amazon-announce-strategic-partnership)
> 第 170 行：11. [BrazenLab independent Trainium validation](https://brazenlab.ai/research.html)
> 第 171 行：12. [Spheron public Trainium3 comparison and limitations](https://www.spheron.network/blog/aws-trainium-3-vs-nvidia-h200-b200-llm-training-inference-2026/)

## 直接来源链接

1. <https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/inferentia.html>
2. <https://aws.amazon.com/ai/machine-learning/inferentia/>
3. <https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium.html>
4. <https://aws.amazon.com/blogs/aws/amazon-ec2-trn1-instances-for-high-performance-model-training-are-now-available/>
5. <https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-ec2-trn1n-instances-network-ai-models/>
6. <https://aws.amazon.com/ec2/instance-types/trn1/>
7. <https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/inferentia2.html>
8. <https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-ec2-inf2-instances-generative-ai-generally-available/>
9. <https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium2.html>
10. <https://aws.amazon.com/blogs/aws/amazon-ec2-trn2-instances-and-trn2-ultraservers-for-aiml-training-and-inference-is-now-available/>
11. <https://aws.amazon.com/blogs/aws/aws-weekly-roundup-project-rainier-amazon-cloudwatch-investigations-aws-mcp-servers-and-more-june-30-2025/>
12. <https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html>
13. <https://aws.amazon.com/ec2/instance-types/trn3/>
14. <https://aws.amazon.com/ai/machine-learning/trainium/customers/>
15. <https://aws.amazon.com/ai/machine-learning/trainium/>
16. <https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html>
17. <https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/>
18. <https://brazenlab.ai/research.html>
19. <https://github.com/mlcommons/training>
20. <https://github.com/mlcommons/training_results_v6.0>
21. <https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/nki/library/api/index.html>
22. <https://press.aboutamazon.com/2026/2/openai-and-amazon-announce-strategic-partnership>
23. <https://www.spheron.network/blog/aws-trainium-3-vs-nvidia-h200-b200-llm-training-inference-2026/>

## 证据边界

- 这是资料重排页，不是重新发布或重新核验的产品公告。
- “发布、流片、送样、量产、出货、客户部署、云端可用、路线图、停产”等状态只在综合报告明确写出时保留；缺失项仍为“公开资料未确认”。
- 若摘录同时出现芯片、板卡、服务器、机架或云服务，均按原报告层级保留，并以“产品层级”字段提醒，不做跨层级推导。

## 关联表格原文（完整表格）

以下表格块来自综合报告中与本拆分项命中的表格，完整保留表头、状态列和规格列。

> 来源综合报告第 25-32 行：
> 第 25 行：|家族/对象|芯片级公开口径|产品与云端节点|客户/部署证据|流片、送样、量产、出货、停产|
> 第 26 行：|---|---|---|---|---|
> 第 27 行：|Inferentia（v1）|4 个 NeuronCore-v1；8 GB DDR4、50 GB/s；128 INT8 TOPS、64 FP16/BF16 TFLOPS。[架构文档](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/inferentia.html)|2018-11-28 首次公开；Inf1 于 2019-12 GA（AWS 后续回顾）。|AWS 列出 Finch AI、Sprinklr、Money Forward、Amazon Alexa；Amazon Search 和 ByteDance 也有 AWS 案例入口。[产品页](https://aws.amazon.com/ai/machine-learning/inferentia/)|公开资料未确认具体 tape-out、送样、晶圆量产、出货量；未查到停产公告。|
> 第 28 行：|Trainium（v1，NeuronCore-v2）|2 个 NeuronCore-v2；32 GiB HBM、0.8 TB/s；191 FP8、191 BF16/FP16/TF32、48 FP32 TFLOPS；NeuronLink-v2 384 GB/s/chip。[架构文档](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium.html)|2020-11 re:Invent 公开路线；Trn1 预览 2021-11-30，GA 2022-10-10；Trn1n GA 2023-04-13。[Trn1 GA](https://aws.amazon.com/blogs/aws/amazon-ec2-trn1-instances-for-high-performance-model-training-are-now-available/)、[Trn1n GA](https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-ec2-trn1n-instances-network-ai-models/)|Ricoh、Helixon、Money Forward、Magic、Cactus、Watashiha 等案例在 Trn1 产品页；Trn1/Trn1n 已面向生产使用。[客户案例](https://aws.amazon.com/ec2/instance-types/trn1/)|公开资料未确认 tape-out、送样、量产和累计出货；未查到停产公告。|
> 第 29 行：|Inferentia2（v2，NeuronCore-v2）|2 个 NeuronCore-v2；32 GB HBM；190 FP16/BF16/cFP8/TF32 TFLOPS、47.5 FP32 TFLOPS；NeuronLink 384 GB/s/chip。[架构文档](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/inferentia2.html)|2022 re:Invent 预览；Inf2 GA 2023-04-13，4 种实例规格、最多 12 颗芯片，初始公开区域为 us-east-1/us-east-2。[GA 公告](https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-ec2-inf2-instances-generative-ai-generally-available/)|AWS 列出 Leonardo.ai、Deutsche Telekom、Qualtrics；Inf2 支持 175B 级模型的单实例分片。[产品页](https://aws.amazon.com/ai/machine-learning/inferentia/)|公开资料未确认 tape-out、送样、量产和累计出货；未查到停产公告。|
> 第 30 行：|Trainium2（v3，NeuronCore-v3）|8 个 NeuronCore-v3；96 GiB HBM、2.9 TB/s；1,299 FP8、667 BF16/FP16/TF32、181 FP32 TFLOPS；3.5 TB/s DMA、1.28 TB/s/chip NeuronLink、16 CC-Cores。[架构文档](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium2.html)|AWS 于 2023-11 公开下一代；Trn2 实例 GA 2024-12-03，Trn2 UltraServer 当时为 preview；Neuron 2.21 于 2024-12-23 增加 Trn2 支持。[Trn2 公告](https://aws.amazon.com/blogs/aws/amazon-ec2-trn2-instances-and-trn2-ultraservers-for-aiml-training-and-inference-is-now-available/)|AWS 称数万 Trainium 已支撑服务，Trn2 已用于 Amazon Bedrock 的 Llama 3.1 405B、Claude 3.5 Haiku；Project Rainier 由 Anthropic 使用 Trainium2，属于客户/平台部署叙述。[Project Rainier](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-project-rainier-amazon-cloudwatch-investigations-aws-mcp-servers-and-more-june-30-2025/)|公开资料未确认 Trainium2 tape-out、送样、晶圆量产和累计出货；未查到停产公告。|
> 第 31 行：|Trainium3（v4，NeuronCore-v4）|8 个 NeuronCore-v4；144 GiB/GB HBM3e、产品页 4.9 TB/s（NKI 指南 4.7 TB/s）；2.52 PFLOPS MXFP8/MXFP4；128 DMA、20 CC-Cores、4 个 NeuronLink-v4。[NKI 架构](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html)|Trn3 UltraServer GA 2025-12-02；最多 144 颗芯片，进入 EC2 UltraClusters 3.0。具体 Trn3 EC2 instance type、区域和公开价格在本次已打开资料中未完整确认。[产品页](https://aws.amazon.com/ec2/instance-types/trn3/)|AWS 宣称 Bedrock 上 Trainium3 是最快加速器；客户页的 Anthropic、Decart、Hugging Face 等内容需要按“公司/AWS 客户页主张”读取，不能等同第三方复测。[客户页](https://aws.amazon.com/ai/machine-learning/trainium/customers/)|公开资料未确认 tape-out、送样、晶圆量产、2026 出货量、真实库存或停产；GA/云端产品可用不等于已公开量产数字。|
> 第 32 行：|Trainium4（路线图）|本次已打开的一手资料只确认“更高 FP4 算力、更高内存带宽和更大 HBM 容量”，没有颗粒数、制程、HBM 类型、互联或功耗规格。|AWS 与 OpenAI 2026-02 战略合作公告称预计 **2027 年开始交付**；这是路线图/承诺节点，不是 GA 或云端可用日期。[官方公告](https://press.aboutamazon.com/2026/2/openai-and-amazon-announce-strategic-partnership)|OpenAI 的容量承诺覆盖 Trainium3 与 Trainium4；不能据此推导芯片已流片、量产或客户已部署。|tape-out、送样、量产、出货、GA、区域、停产：**未确认**。|

> 来源综合报告第 38-52 行：
> 第 38 行：|日期|事件|证据等级|
> 第 39 行：|---|---|---|
> 第 40 行：|2018-11-28|AWS 首次公开 Inferentia，目标是 2019 可用。|官方新闻稿；“预计可用”不等于 GA。|
> 第 41 行：|2019-12|Inf1/Inferentia GA。|AWS 后续官方博客回顾；未找到当日 GA 原始公告。|
> 第 42 行：|2020-11|re:Invent 公开 Trainium，目标为 2021 年下半年。|官方 re:Invent 直播记录；目标日期不等于出货。|
> 第 43 行：|2021-11-30|Trn1 预览。|官方 What's New。|
> 第 44 行：|2022-10-10|Trn1 GA。|官方 AWS News Blog。|
> 第 45 行：|2022 re:Invent|Inferentia2/Inf2 预览。|官方 Inf2 GA 博客回顾。|
> 第 46 行：|2023-04-13|Inf2 与 Trn1n GA。|官方 What's New。|
> 第 47 行：|2023-11|AWS 公开 Trainium2。|本次已打开的一手材料确认“下一代已宣布”，未在报告中补写未核实的具体日。|
> 第 48 行：|2024-12-03|Trn2 实例 GA；Trn2 UltraServer 为 preview。|官方 AWS News Blog。|
> 第 49 行：|2024-12-23|Neuron 2.21 加入 Trainium2、Trn2、NxD Inference。|官方 What's New。|
> 第 50 行：|2025-12-02|Trn3 UltraServer GA；Trainium3 产品公开。|官方 What's New。|
> 第 51 行：|2026-02|OpenAI/AWS 公告 Trainium4，预计 2027 开始交付。|官方新闻稿；路线图，不是 GA。|
> 第 52 行：|2026-05-26 至 2026-08-17|Neuron 2.30、2.31、2.32 逐步加入 Trainium3/NKI 新能力。|官方 release/What's New。|

> 来源综合报告第 66-73 行：
> 第 66 行：|项目|Trainium3 单芯片|Trn3 UltraServer Gen2（平台级）|
> 第 67 行：|---|---|---|
> 第 68 行：|制程/执行单元|3nm；8 个 NeuronCore-v4，每核含 Tensor、Vector、Scalar、GpSimd。[AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/)|144 颗芯片，36 台服务器、每台 4 颗。[架构表](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html)|
> 第 69 行：|格式/计算|FP32、BF16、MXFP8、MXFP4；GA 口径每芯片 [2.52 PFLOP FP8](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)。| [362,448 MXFP8/MXFP4 TFLOPS](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html)；FP16/BF16/TF32 为 96,624 TFLOPS。|
> 第 70 行：|存储|4 个 HBM stack、[144 GB HBM3e](https://aws.amazon.com/ec2/instance-types/trn3/)；每核 SBUF 32 MiB、PSUM 2 MiB。[NKI 架构指南](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html)|[20,736 GiB HBM](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html)，产品页约写 20.7 TB。|
> 第 71 行：|带宽|产品页 [4.9 TB/s](https://aws.amazon.com/ec2/instance-types/trn3/)；NKI 指南写 4.7 TB/s。[另一口径](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html)|[705.6 TB/s](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html)，产品页四舍五入为 706 TB/s。|
> 第 72 行：|互联/搬运|4 个 NeuronLink-v4、128 DMA engine、20 CC-Core。[NKI 指南](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html)|NeuronSwitch-v1 all-to-all；NeuronLink-v4 [2,048 GiB/s/device](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html)，EFA 28,800 Gbps。|
> 第 73 行：|功耗|绝对 TDP/芯片瓦数：**公开资料未确认**；只有相对 Trn2 UltraServer 超过 4 倍性能/瓦的比较。[产品页](https://aws.amazon.com/ec2/instance-types/trn3/)|不能把 Tokens/MW 或性能/瓦反推为机架功耗。|

> 来源综合报告第 119-124 行：
> 第 119 行：|证据|可写成什么|不能写成什么|
> 第 120 行：|---|---|---|
> 第 121 行：|AWS Trn3 产品页：2.52 PFLOPS/chip、4.9 TB/s、4.4x/4x、Bedrock 3x|官方规格或 AWS 自测/主张，取决于字段|不能写成独立实验、全模型平均或跨供应商普适优势|
> 第 122 行：|AWS Neuron NKI/库函数|API/编程能力已公开；包括 segmented attention、KV-parallel prefill、Gather、Top-k Reduce 等|不能写成硬件已有独立 Search Core，或证明每 token 的跨卡通信量已降到某个复杂度|
> 第 123 行：|BrazenLab Trn1/Trn2|独立作者公开了可复核的实验范围与部分结果|不能把 Trn1/Trn2 结果外推成 Trainium3；不能把独立分片吞吐当单作业延迟|
> 第 124 行：|MLCommons Training v6.0 公共参考/结果索引|本次查验未定位到 AWS Trainium/Inferentia 的 MLPerf 正式提交|不能据此证明全球绝对没有任何其他第三方基准，也不能把 reference implementation 当提交结果。[MLCommons training](https://github.com/mlcommons/training)、[MLCommons results](https://github.com/mlcommons/training_results_v6.0)|

## 补充直接来源链接

1. <https://press.aboutamazon.com/2026/2/openai-and-amazon-announce-strategic-partnership>（OpenAI）
2. <https://aws.amazon.com/ec2/instance-types/trn3/>；每核
3. <https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html>（20,736）
4. <https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html>，产品页约写
5. <https://aws.amazon.com/ec2/instance-types/trn3/>；NKI
6. <https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html>（705.6）
7. <https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html>，产品页四舍五入为
8. <https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html>（NeuronSwitch-v1）
9. <https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html>，EFA
10. <https://aws.amazon.com/ec2/instance-types/trn3/>（不能把）
