# Amazon Web Services / 亚马逊云科技 — Trn3 UltraServer（平台边界，非芯片）

- 拆分日期：2026-09-02
- 产品层级：服务器/集群/云平台（非芯片）
- 综合报告：[06-aws-trainium.md](./06-aws-trainium.md)
- 文件性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容逐行摘录综合报告，保留原报告中的状态、数字、证据等级和未知项。

> 第 1 行：# AWS Trainium3 / Trn3 UltraServer：面向推理数据流的架构研究
> 第 2 行：
> 第 6 行：
> 第 7 行：Trainium3 的最新目标是用 [3nm、HBM3e、MXFP8/MXFP4](https://aws.amazon.com/ec2/instance-types/trn3/)、NeuronSwitch-v1 和 NKI 支撑长上下文与 MoE 推理；最值得研究的不是峰值 FLOPS，而是把存储、DMA、Top-k/Reduce、集合通信和 [144 芯片 scale-up](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html) 放进同一条数据路径。
> 第 8 行：
> 第 10 行：
> 第 11 行：边界必须分开：Trainium3 是单芯片；Trn3 UltraServer 是多芯片服务器级 scale-up 域；UltraCluster 3.0 是继续扩展的集群/云服务形态。选择它，是因为 AWS 已公开与附件相邻的 segmented attention、KV-parallel prefill、Gather、Top-k 和 Sparse Attention Indexer kernel。
> 第 12 行：
> 第 14 行：|---|---|
> 第 15 行：|Trainium3 芯片|首次公开/宣布日期：**本次已打开的一手资料未确认**；不能把 2024-12-03 的 Trainium2 公告当成 Trainium3 首发。Trainium3 的 Trn3 UltraServer GA 为 2025-12-02。[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)|
> 第 16 行：|Trn3 UltraServer|**GA/上市：2025-12-02，窗口内**；GA 新闻稿公开单芯片和平台口径。[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)|
> 第 17 行：|UltraCluster 3.0|是 UltraServer 的集群部署边界；AWS 宣称可扩展到数十万芯片，但这是平台能力，不是已审计的实际部署量。[EC2 Trn3](https://aws.amazon.com/ec2/instance-types/trn3/)|
> 第 18 行：|软件可用性|Neuron 2.30 GA 于 2026-05-26，2.31 于 2026-07-08，2.32 于 2026-08-17；NKI 0.4/0.5/0.6 和相关 kernels 在窗口内逐步可用。[2.30](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-announce-neuron-2-30-0/)、[2.31](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-announce-neuron-2-31-0/)、[2.32](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/whats-new.html)|
> 第 22 行：
> 第 23 行：下面把芯片、EC2 实例、UltraServer、UltraCluster 和软件分层。日期是“公开资料可证实的节点”，不是推测的流片或供应链日期。
> 第 24 行：
> 第 29 行：|Inferentia2（v2，NeuronCore-v2）|2 个 NeuronCore-v2；32 GB HBM；190 FP16/BF16/cFP8/TF32 TFLOPS、47.5 FP32 TFLOPS；NeuronLink 384 GB/s/chip。[架构文档](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/inferentia2.html)|2022 re:Invent 预览；Inf2 GA 2023-04-13，4 种实例规格、最多 12 颗芯片，初始公开区域为 us-east-1/us-east-2。[GA 公告](https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-ec2-inf2-instances-generative-ai-generally-available/)|AWS 列出 Leonardo.ai、Deutsche Telekom、Qualtrics；Inf2 支持 175B 级模型的单实例分片。[产品页](https://aws.amazon.com/ai/machine-learning/inferentia/)|公开资料未确认 tape-out、送样、量产和累计出货；未查到停产公告。|
> 第 30 行：|Trainium2（v3，NeuronCore-v3）|8 个 NeuronCore-v3；96 GiB HBM、2.9 TB/s；1,299 FP8、667 BF16/FP16/TF32、181 FP32 TFLOPS；3.5 TB/s DMA、1.28 TB/s/chip NeuronLink、16 CC-Cores。[架构文档](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium2.html)|AWS 于 2023-11 公开下一代；Trn2 实例 GA 2024-12-03，Trn2 UltraServer 当时为 preview；Neuron 2.21 于 2024-12-23 增加 Trn2 支持。[Trn2 公告](https://aws.amazon.com/blogs/aws/amazon-ec2-trn2-instances-and-trn2-ultraservers-for-aiml-training-and-inference-is-now-available/)|AWS 称数万 Trainium 已支撑服务，Trn2 已用于 Amazon Bedrock 的 Llama 3.1 405B、Claude 3.5 Haiku；Project Rainier 由 Anthropic 使用 Trainium2，属于客户/平台部署叙述。[Project Rainier](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-project-rainier-amazon-cloudwatch-investigations-aws-mcp-servers-and-more-june-30-2025/)|公开资料未确认 Trainium2 tape-out、送样、晶圆量产和累计出货；未查到停产公告。|
> 第 31 行：|Trainium3（v4，NeuronCore-v4）|8 个 NeuronCore-v4；144 GiB/GB HBM3e、产品页 4.9 TB/s（NKI 指南 4.7 TB/s）；2.52 PFLOPS MXFP8/MXFP4；128 DMA、20 CC-Cores、4 个 NeuronLink-v4。[NKI 架构](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html)|Trn3 UltraServer GA 2025-12-02；最多 144 颗芯片，进入 EC2 UltraClusters 3.0。具体 Trn3 EC2 instance type、区域和公开价格在本次已打开资料中未完整确认。[产品页](https://aws.amazon.com/ec2/instance-types/trn3/)|AWS 宣称 Bedrock 上 Trainium3 是最快加速器；客户页的 Anthropic、Decart、Hugging Face 等内容需要按“公司/AWS 客户页主张”读取，不能等同第三方复测。[客户页](https://aws.amazon.com/ai/machine-learning/trainium/customers/)|公开资料未确认 tape-out、送样、晶圆量产、2026 出货量、真实库存或停产；GA/云端产品可用不等于已公开量产数字。|
> 第 32 行：|Trainium4（路线图）|本次已打开的一手资料只确认“更高 FP4 算力、更高内存带宽和更大 HBM 容量”，没有颗粒数、制程、HBM 类型、互联或功耗规格。|AWS 与 OpenAI 2026-02 战略合作公告称预计 **2027 年开始交付**；这是路线图/承诺节点，不是 GA 或云端可用日期。[官方公告](https://press.aboutamazon.com/2026/2/openai-and-amazon-announce-strategic-partnership)|OpenAI 的容量承诺覆盖 Trainium3 与 Trainium4；不能据此推导芯片已流片、量产或客户已部署。|tape-out、送样、量产、出货、GA、区域、停产：**未确认**。|
> 第 47 行：|2023-11|AWS 公开 Trainium2。|本次已打开的一手材料确认“下一代已宣布”，未在报告中补写未核实的具体日。|
> 第 48 行：|2024-12-03|Trn2 实例 GA；Trn2 UltraServer 为 preview。|官方 AWS News Blog。|
> 第 49 行：|2024-12-23|Neuron 2.21 加入 Trainium2、Trn2、NxD Inference。|官方 What's New。|
> 第 50 行：|2025-12-02|Trn3 UltraServer GA；Trainium3 产品公开。|官方 What's New。|
> 第 51 行：|2026-02|OpenAI/AWS 公告 Trainium4，预计 2027 开始交付。|官方新闻稿；路线图，不是 GA。|
> 第 58 行：- **芯片：** AWS 自研加速器，不向客户单独购买裸片；本报告不把芯片型号当成可直接采购的 PCIe 卡。
> 第 59 行：- **实例/服务器：** Inf1、Inf2、Trn1/Trn1n、Trn2 是 EC2 实例产品；Trn2/Trn3 UltraServer 是更大 scale-up 平台，不能把平台 HBM、带宽和 PFLOPS 回填为单芯片规格。
> 第 60 行：- **集群/云服务：** UltraCluster 是跨服务器的网络与调度边界；Amazon Bedrock 是托管模型 API。Bedrock 上的模型可用只证明云服务路径存在，不证明用户能租到对应的裸芯片或固定 Trn3 拓扑。
> 第 65 行：
> 第 66 行：|项目|Trainium3 单芯片|Trn3 UltraServer Gen2（平台级）|
> 第 67 行：|---|---|---|
> 第 71 行：|带宽|产品页 [4.9 TB/s](https://aws.amazon.com/ec2/instance-types/trn3/)；NKI 指南写 4.7 TB/s。[另一口径](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html)|[705.6 TB/s](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html)，产品页四舍五入为 706 TB/s。|
> 第 72 行：|互联/搬运|4 个 NeuronLink-v4、128 DMA engine、20 CC-Core。[NKI 指南](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html)|NeuronSwitch-v1 all-to-all；NeuronLink-v4 [2,048 GiB/s/device](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html)，EFA 28,800 Gbps。|
> 第 73 行：|功耗|绝对 TDP/芯片瓦数：**公开资料未确认**；只有相对 Trn2 UltraServer 超过 4 倍性能/瓦的比较。[产品页](https://aws.amazon.com/ec2/instance-types/trn3/)|不能把 Tokens/MW 或性能/瓦反推为机架功耗。|
> 第 74 行：
> 第 92 行：|离散 KV Gather|[indirect DMA Gather](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/nki/library/api/gather.html) 与 block-based KV 直接相关。|片上 tensor indirection 放宽布局限制。|2D 行 Gather 不等于跨 HBM 的任意 page-aware Gather DMA。|
> 第 93 行：|Address / Route|Trn3 switched fabric 用地址编码路由芯片。[架构表](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html)|NeuronSwitch-v1 有利于 collective。|不是附件所说的语义索引、Page Translator 或动态地址簿。|
> 第 94 行：|跨卡通信|NeuronSwitch-v1、EFA、KV-parallel 的分片与 online merge 直接覆盖平台通信。|可扩展的 scale-up 域提供工程底座。|没有证据把通信量降到附件的 `P×k` 候选。|
> 第 95 行：|TPOT / TTFT / Tokens/J|公开了 prefix-cache 的测试方法和相对能效。|分段 KV、融合 kernel 可能改善这些指标。|Trainium3 的端到端 TPOT、TTFT、Tokens/J、HBM bytes/token、跨卡 bytes/token：**公开资料未确认**。|
> 第 139 行：|KV|segmented attention、KV-parallel prefill、block KV、prefix cache、decode/context parallel 文档。|直接对应 KV/Attention 数据流；没有证明任意 KV 检索都变成 `O(k)`。|
> 第 140 行：|跨卡|NeuronLink-v2/v3/v4、NeuronSwitch-v1、EFA、TP/PP/EP/CP 与 online merge。|通信底座和并行编程事实；没有公开 Trn3 的端到端 bytes/token 或 p99。|
> 第 141 行：
> 第 154 行：- **可直接借鉴：** software-managed scratchpad、indirect DMA/片上 tensor indirection、分段 KV、Gather/Top-k/Reduce 原语、局部计算加在线合并、可编程通信路由。
> 第 155 行：- **只能类比：** NeuronSwitch-v1 是 scale-up 底座参考，不等于 Local Top-k 候选合并；Sparse Indexer 是 kernel 组织参考，不是通用 Search ISA；MXFP4/8 需单独验证精确 score 误差。
> 第 156 行：- **不宜照搬：** DeepSeek 专用公式、固定 k/block size、把 page table 硬焊进芯片、把 144 芯片带宽线性折算到单卡、用 PFLOPS 替代 TPOT/TTFT/Tokens/J 验收。

## 直接来源链接

1. <https://aws.amazon.com/ec2/instance-types/trn3/>
2. <https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html>
3. <https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/>
4. <https://aws.amazon.com/about-aws/whats-new/2026/05/aws-announce-neuron-2-30-0/>
5. <https://aws.amazon.com/about-aws/whats-new/2026/07/aws-announce-neuron-2-31-0/>
6. <https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/whats-new.html>
7. <https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/inferentia2.html>
8. <https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-ec2-inf2-instances-generative-ai-generally-available/>
9. <https://aws.amazon.com/ai/machine-learning/inferentia/>
10. <https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium2.html>
11. <https://aws.amazon.com/blogs/aws/amazon-ec2-trn2-instances-and-trn2-ultraservers-for-aiml-training-and-inference-is-now-available/>
12. <https://aws.amazon.com/blogs/aws/aws-weekly-roundup-project-rainier-amazon-cloudwatch-investigations-aws-mcp-servers-and-more-june-30-2025/>
13. <https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html>
14. <https://aws.amazon.com/ai/machine-learning/trainium/customers/>
15. <https://press.aboutamazon.com/2026/2/openai-and-amazon-announce-strategic-partnership>
16. <https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/nki/library/api/gather.html>

## 证据边界

- 这是资料重排页，不是重新发布或重新核验的产品公告。
- “发布、流片、送样、量产、出货、客户部署、云端可用、路线图、停产”等状态只在综合报告明确写出时保留；缺失项仍为“公开资料未确认”。
- 若摘录同时出现芯片、板卡、服务器、机架或云服务，均按原报告层级保留，并以“产品层级”字段提醒，不做跨层级推导。

## 关联表格原文（完整表格）

以下表格块来自综合报告中与本拆分项命中的表格，完整保留表头、状态列和规格列。

> 来源综合报告第 13-19 行：
> 第 13 行：|对象|截至 2026-09-01 的状态|
> 第 14 行：|---|---|
> 第 15 行：|Trainium3 芯片|首次公开/宣布日期：**本次已打开的一手资料未确认**；不能把 2024-12-03 的 Trainium2 公告当成 Trainium3 首发。Trainium3 的 Trn3 UltraServer GA 为 2025-12-02。[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)|
> 第 16 行：|Trn3 UltraServer|**GA/上市：2025-12-02，窗口内**；GA 新闻稿公开单芯片和平台口径。[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)|
> 第 17 行：|UltraCluster 3.0|是 UltraServer 的集群部署边界；AWS 宣称可扩展到数十万芯片，但这是平台能力，不是已审计的实际部署量。[EC2 Trn3](https://aws.amazon.com/ec2/instance-types/trn3/)|
> 第 18 行：|软件可用性|Neuron 2.30 GA 于 2026-05-26，2.31 于 2026-07-08，2.32 于 2026-08-17；NKI 0.4/0.5/0.6 和相关 kernels 在窗口内逐步可用。[2.30](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-announce-neuron-2-30-0/)、[2.31](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-announce-neuron-2-31-0/)、[2.32](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/whats-new.html)|
> 第 19 行：|量产/实际装机|晶圆量产、良率、出货量和真实库存：**公开资料未确认**。|

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

> 来源综合报告第 87-95 行：
> 第 87 行：|附件路径|直接解决|间接帮助|没有解决/证据不足|
> 第 88 行：|---|---|---|---|
> 第 89 行：|密集计算|多类 NeuronCore engine、MXFP8/MXFP4 直接覆盖规则 GEMM/Attention。|HBM、SBUF/PSUM 减少等待。|没有证明峰值 FLOPS 解决 Indexer 搬运。|
> 第 90 行：|Search / Indexer|有实验性的 [Sparse Attention Indexer](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/nki/library/api/sparse-attention-indexer-mx-bf16score.html)，含 MX projection、BF16 score。|NKI 允许模型相关 kernel。|不是通用 Retrieval Plane，也没有通用 exact Search ISA。|
> 第 91 行：|Top-k / Reduce|有 [GpSimd Top-k 与 Top-k Reduce](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/nki/library/api/topk-reduce.html)。|可变长度 collective 适合不等长候选。|未证明已实现“各 HBM 分区 Local Top-k + Global Merge”。|
> 第 92 行：|离散 KV Gather|[indirect DMA Gather](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/nki/library/api/gather.html) 与 block-based KV 直接相关。|片上 tensor indirection 放宽布局限制。|2D 行 Gather 不等于跨 HBM 的任意 page-aware Gather DMA。|
> 第 93 行：|Address / Route|Trn3 switched fabric 用地址编码路由芯片。[架构表](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html)|NeuronSwitch-v1 有利于 collective。|不是附件所说的语义索引、Page Translator 或动态地址簿。|
> 第 94 行：|跨卡通信|NeuronSwitch-v1、EFA、KV-parallel 的分片与 online merge 直接覆盖平台通信。|可扩展的 scale-up 域提供工程底座。|没有证据把通信量降到附件的 `P×k` 候选。|
> 第 95 行：|TPOT / TTFT / Tokens/J|公开了 prefix-cache 的测试方法和相对能效。|分段 KV、融合 kernel 可能改善这些指标。|Trainium3 的端到端 TPOT、TTFT、Tokens/J、HBM bytes/token、跨卡 bytes/token：**公开资料未确认**。|

> 来源综合报告第 130-140 行：
> 第 130 行：|层级|已公开能力|证据性质与限制|
> 第 131 行：|---|---|---|
> 第 132 行：|框架/编译|PyTorch、JAX、Hugging Face Optimum Neuron、OpenXLA、NxD Training/Inference、vLLM Neuron；支持动态 shape、控制流、custom operator、profiling。|官方软件能力；具体模型仍受算子覆盖、编译时间、布局和版本限制。|
> 第 133 行：|低层编程|NKI 直接暴露 tile、SBUF/PSUM、DMA、同步和调度；Neuron 2.30–2.32 持续增加 Trn3 能力。|官方文档/API；可编程不等于已有通用硬件检索指令。|
> 第 134 行：|Search / Indexer|Sparse Attention Indexer kernel 含 MX projection 与 BF16 score。|实验性/模型相关 kernel；不等于通用 exact retrieval。|
> 第 135 行：|Reduce|CC-Cores、collective、online softmax merge、variable-length collective。|能支持分片结果合并；未公开任意 Top-k 的端到端成本。|
> 第 136 行：|Top-k|GpSimd `topk`、Top-k Reduce。|API/库函数事实；未证明 HBM 分区 local Top-k 后 global merge 的完整硬件路径。|
> 第 137 行：|Address / Route|NeuronLink/NeuronSwitch 负责芯片互联与 collective 路由；软件有 block/page 语义。|网络地址/拓扑路由；不是语义索引、Page Translator 或动态地址簿。|
> 第 138 行：|Gather|indirect DMA Gather、tensor indirection、block-based KV 相关用法。|片上/设备内数据搬运 API；2D Gather 不等于跨 HBM 任意 page-aware Gather。|
> 第 139 行：|KV|segmented attention、KV-parallel prefill、block KV、prefix cache、decode/context parallel 文档。|直接对应 KV/Attention 数据流；没有证明任意 KV 检索都变成 `O(k)`。|
> 第 140 行：|跨卡|NeuronLink-v2/v3/v4、NeuronSwitch-v1、EFA、TP/PP/EP/CP 与 online merge。|通信底座和并行编程事实；没有公开 Trn3 的端到端 bytes/token 或 p99。|

## 补充直接来源链接

1. <https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/inferentia.html)|2018-11-28>
2. <https://aws.amazon.com/ai/machine-learning/inferentia/)|公开资料未确认具体>
3. <https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium.html)|2020-11>
4. <https://aws.amazon.com/blogs/aws/amazon-ec2-trn1-instances-for-high-performance-model-training-are-now-available/)、[Trn1n>
5. <https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-ec2-trn1n-instances-network-ai-models/)|Ricoh、Helixon、Money>
6. <https://aws.amazon.com/ec2/instance-types/trn1/)|公开资料未确认>
7. <https://aws.amazon.com/ai/machine-learning/trainium/)|144>
8. <https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)。|>
9. <https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html)；FP16/BF16/TF32>
10. <https://aws.amazon.com/ec2/instance-types/trn3/)；每核>
11. <https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html)|[20,736>
12. <https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html)，产品页约写>
13. <https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/nki/library/api/sparse-attention-indexer-mx-bf16score.html)，含>
14. <https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/nki/library/api/topk-reduce.html)。|可变长度>
