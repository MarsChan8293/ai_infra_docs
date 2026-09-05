# Amazon Web Services / 亚马逊云科技 — Trainium4（路线图）

- 拆分日期：2026-09-02
- 产品层级：路线图芯片
- 综合报告：[06-aws-trainium.md](./06-aws-trainium.md)
- 文件性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容逐行摘录综合报告，保留原报告中的状态、数字、证据等级和未知项。

> 第 31 行：|Trainium3（v4，NeuronCore-v4）|8 个 NeuronCore-v4；144 GiB/GB HBM3e、产品页 4.9 TB/s（NKI 指南 4.7 TB/s）；2.52 PFLOPS MXFP8/MXFP4；128 DMA、20 CC-Cores、4 个 NeuronLink-v4。[NKI 架构](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html)|Trn3 UltraServer GA 2025-12-02；最多 144 颗芯片，进入 EC2 UltraClusters 3.0。具体 Trn3 EC2 instance type、区域和公开价格在本次已打开资料中未完整确认。[产品页](https://aws.amazon.com/ec2/instance-types/trn3/)|AWS 宣称 Bedrock 上 Trainium3 是最快加速器；客户页的 Anthropic、Decart、Hugging Face 等内容需要按“公司/AWS 客户页主张”读取，不能等同第三方复测。[客户页](https://aws.amazon.com/ai/machine-learning/trainium/customers/)|公开资料未确认 tape-out、送样、晶圆量产、2026 出货量、真实库存或停产；GA/云端产品可用不等于已公开量产数字。|
> 第 32 行：|Trainium4（路线图）|本次已打开的一手资料只确认“更高 FP4 算力、更高内存带宽和更大 HBM 容量”，没有颗粒数、制程、HBM 类型、互联或功耗规格。|AWS 与 OpenAI 2026-02 战略合作公告称预计 **2027 年开始交付**；这是路线图/承诺节点，不是 GA 或云端可用日期。[官方公告](https://press.aboutamazon.com/2026/2/openai-and-amazon-announce-strategic-partnership)|OpenAI 的容量承诺覆盖 Trainium3 与 Trainium4；不能据此推导芯片已流片、量产或客户已部署。|tape-out、送样、量产、出货、GA、区域、停产：**未确认**。|
> 第 33 行：
> 第 50 行：|2025-12-02|Trn3 UltraServer GA；Trainium3 产品公开。|官方 What's New。|
> 第 51 行：|2026-02|OpenAI/AWS 公告 Trainium4，预计 2027 开始交付。|官方新闻稿；路线图，不是 GA。|
> 第 52 行：|2026-05-26 至 2026-08-17|Neuron 2.30、2.31、2.32 逐步加入 Trainium3/NKI 新能力。|官方 release/What's New。|
> 第 168 行：9. [AWS Inferentia customers/product page](https://aws.amazon.com/ai/machine-learning/inferentia/)
> 第 169 行：10. [AWS OpenAI strategic partnership：Trainium4 2027 roadmap](https://press.aboutamazon.com/2026/2/openai-and-amazon-announce-strategic-partnership)
> 第 170 行：11. [BrazenLab independent Trainium validation](https://brazenlab.ai/research.html)

## 直接来源链接

1. <https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html>
2. <https://aws.amazon.com/ec2/instance-types/trn3/>
3. <https://aws.amazon.com/ai/machine-learning/trainium/customers/>
4. <https://press.aboutamazon.com/2026/2/openai-and-amazon-announce-strategic-partnership>
5. <https://aws.amazon.com/ai/machine-learning/inferentia/>
6. <https://brazenlab.ai/research.html>

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

## 补充直接来源链接

1. <https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/inferentia.html>（2018-11-28）
2. <https://aws.amazon.com/ai/machine-learning/inferentia/>（公开资料未确认具体）
3. <https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium.html>（2020-11）
4. <https://aws.amazon.com/blogs/aws/amazon-ec2-trn1-instances-for-high-performance-model-training-are-now-available/>、Trn1n
5. <https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-ec2-trn1n-instances-network-ai-models/>（Ricoh、Helixon、Money）
6. <https://aws.amazon.com/ec2/instance-types/trn1/>（公开资料未确认）
7. <https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/inferentia2.html>（2022）
8. <https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-ec2-inf2-instances-generative-ai-generally-available/>（AWS）
9. <https://aws.amazon.com/ai/machine-learning/inferentia/>（公开资料未确认）
10. <https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium2.html>（AWS）
11. <https://aws.amazon.com/blogs/aws/amazon-ec2-trn2-instances-and-trn2-ultraservers-for-aiml-training-and-inference-is-now-available/>（AWS）
12. <https://aws.amazon.com/blogs/aws/aws-weekly-roundup-project-rainier-amazon-cloudwatch-investigations-aws-mcp-servers-and-more-june-30-2025/>（公开资料未确认）
