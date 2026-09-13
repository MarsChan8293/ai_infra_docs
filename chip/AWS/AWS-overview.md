# AWS Trainium3 / Trn3 UltraServer：面向推理数据流的架构研究

## 芯片页关系导航

本页是本目录唯一的厂家总览。下面的页面均按单一芯片、芯片家族或芯片关联产品对象拆分；芯片页中的“厂商总览”链接回到本页。`[[...]]` 用于 Obsidian 图谱，Markdown 链接用于普通阅读。

- [[inferentia-v1|AWS Inferentia（v1）芯片证据页]] · [打开 Markdown](./inferentia-v1.md)
- [[inferentia2|AWS Inferentia2（v2）芯片证据页]] · [打开 Markdown](./inferentia2.md)
- [[trainium-v1|AWS Trainium（v1）芯片证据页]] · [打开 Markdown](./trainium-v1.md)
- [[trainium2|AWS Trainium2（v3）芯片证据页]] · [打开 Markdown](./trainium2.md)
- [[trainium3|AWS Trainium3（v4）芯片证据页]] · [打开 Markdown](./trainium3.md)
- [[trainium4-roadmap|AWS Trainium4 路线图证据页]] · [打开 Markdown](./trainium4-roadmap.md)

> 资料访问日：2026-09-01。范围只研究 AWS；文中“首次公开、宣布、GA/上市、量产/出货/部署”分开记录。新增内容按“官方事实 / 厂商主张 / 独立测试 / 分析判断 / 未确认”标注。

## 1. 一句话结论

Trainium3 的最新目标是用 [3nm、HBM3e、MXFP8/MXFP4](https://aws.amazon.com/ec2/instance-types/trn3/)、NeuronSwitch-v1 和 NKI 支撑长上下文与 MoE 推理；最值得研究的不是峰值 FLOPS，而是把存储、DMA、Top-k/Reduce、集合通信和 [144 芯片 scale-up](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html) 放进同一条数据路径。

## 2. 目标芯片与时间状态

边界必须分开：Trainium3 是单芯片；Trn3 UltraServer 是多芯片服务器级 scale-up 域；UltraCluster 3.0 是继续扩展的集群/云服务形态。选择它，是因为 AWS 已公开与附件相邻的 segmented attention、KV-parallel prefill、Gather、Top-k 和 Sparse Attention Indexer kernel。

|对象|截至 2026-09-01 的状态|
|---|---|
|Trainium3 芯片|首次公开/宣布日期：**本次已打开的一手资料未确认**；不能把 2024-12-03 的 Trainium2 公告当成 Trainium3 首发。Trainium3 的 Trn3 UltraServer GA 为 2025-12-02。[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)|
|Trn3 UltraServer|**GA/上市：2025-12-02，窗口内**；GA 新闻稿公开单芯片和平台口径。[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)|
|UltraCluster 3.0|是 UltraServer 的集群部署边界；AWS 宣称可扩展到数十万芯片，但这是平台能力，不是已审计的实际部署量。[EC2 Trn3](https://aws.amazon.com/ec2/instance-types/trn3/)|
|软件可用性|Neuron 2.30 GA 于 2026-05-26，2.31 于 2026-07-08，2.32 于 2026-08-17；NKI 0.4/0.5/0.6 和相关 kernels 在窗口内逐步可用。[2.30](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-announce-neuron-2-30-0/)、[2.31](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-announce-neuron-2-31-0/)、[2.32](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/whats-new.html)|
|量产/实际装机|晶圆量产、良率、出货量和真实库存：**公开资料未确认**。|

### 2.1 全产品家族与代际状态

下面把芯片、EC2 实例、UltraServer、UltraCluster 和软件分层。日期是“公开资料可证实的节点”，不是推测的流片或供应链日期。

|家族/对象|芯片级公开口径|产品与云端节点|客户/部署证据|流片、送样、量产、出货、停产|
|---|---|---|---|---|
|Inferentia（v1）|4 个 NeuronCore-v1；8 GB DDR4、50 GB/s；128 INT8 TOPS、64 FP16/BF16 TFLOPS。[架构文档](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/inferentia.html)|2018-11-28 首次公开；Inf1 于 2019-12 GA（AWS 后续回顾）。|AWS 列出 Finch AI、Sprinklr、Money Forward、Amazon Alexa；Amazon Search 和 ByteDance 也有 AWS 案例入口。[产品页](https://aws.amazon.com/ai/machine-learning/inferentia/)|公开资料未确认具体 tape-out、送样、晶圆量产、出货量；未查到停产公告。|
|Trainium（v1，NeuronCore-v2）|2 个 NeuronCore-v2；32 GiB HBM、0.8 TB/s；191 FP8、191 BF16/FP16/TF32、48 FP32 TFLOPS；NeuronLink-v2 384 GB/s/chip。[架构文档](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium.html)|2020-11 re:Invent 公开路线；Trn1 预览 2021-11-30，GA 2022-10-10；Trn1n GA 2023-04-13。[Trn1 GA](https://aws.amazon.com/blogs/aws/amazon-ec2-trn1-instances-for-high-performance-model-training-are-now-available/)、[Trn1n GA](https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-ec2-trn1n-instances-network-ai-models/)|Ricoh、Helixon、Money Forward、Magic、Cactus、Watashiha 等案例在 Trn1 产品页；Trn1/Trn1n 已面向生产使用。[客户案例](https://aws.amazon.com/ec2/instance-types/trn1/)|公开资料未确认 tape-out、送样、量产和累计出货；未查到停产公告。|
|Inferentia2（v2，NeuronCore-v2）|2 个 NeuronCore-v2；32 GB HBM；190 FP16/BF16/cFP8/TF32 TFLOPS、47.5 FP32 TFLOPS；NeuronLink 384 GB/s/chip。[架构文档](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/inferentia2.html)|2022 re:Invent 预览；Inf2 GA 2023-04-13，4 种实例规格、最多 12 颗芯片，初始公开区域为 us-east-1/us-east-2。[GA 公告](https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-ec2-inf2-instances-generative-ai-generally-available/)|AWS 列出 Leonardo.ai、Deutsche Telekom、Qualtrics；Inf2 支持 175B 级模型的单实例分片。[产品页](https://aws.amazon.com/ai/machine-learning/inferentia/)|公开资料未确认 tape-out、送样、量产和累计出货；未查到停产公告。|
|Trainium2（v3，NeuronCore-v3）|8 个 NeuronCore-v3；96 GiB HBM、2.9 TB/s；1,299 FP8、667 BF16/FP16/TF32、181 FP32 TFLOPS；3.5 TB/s DMA、1.28 TB/s/chip NeuronLink、16 CC-Cores。[架构文档](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium2.html)|AWS 于 2023-11 公开下一代；Trn2 实例 GA 2024-12-03，Trn2 UltraServer 当时为 preview；Neuron 2.21 于 2024-12-23 增加 Trn2 支持。[Trn2 公告](https://aws.amazon.com/blogs/aws/amazon-ec2-trn2-instances-and-trn2-ultraservers-for-aiml-training-and-inference-is-now-available/)|AWS 称数万 Trainium 已支撑服务，Trn2 已用于 Amazon Bedrock 的 Llama 3.1 405B、Claude 3.5 Haiku；Project Rainier 由 Anthropic 使用 Trainium2，属于客户/平台部署叙述。[Project Rainier](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-project-rainier-amazon-cloudwatch-investigations-aws-mcp-servers-and-more-june-30-2025/)|公开资料未确认 Trainium2 tape-out、送样、晶圆量产和累计出货；未查到停产公告。|
|Trainium3（v4，NeuronCore-v4）|8 个 NeuronCore-v4；144 GiB/GB HBM3e、产品页 4.9 TB/s（NKI 指南 4.7 TB/s）；2.52 PFLOPS MXFP8/MXFP4；128 DMA、20 CC-Cores、4 个 NeuronLink-v4。[NKI 架构](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html)|Trn3 UltraServer GA 2025-12-02；最多 144 颗芯片，进入 EC2 UltraClusters 3.0。具体 Trn3 EC2 instance type、区域和公开价格在本次已打开资料中未完整确认。[产品页](https://aws.amazon.com/ec2/instance-types/trn3/)|AWS 宣称 Bedrock 上 Trainium3 是最快加速器；客户页的 Anthropic、Decart、Hugging Face 等内容需要按“公司/AWS 客户页主张”读取，不能等同第三方复测。[客户页](https://aws.amazon.com/ai/machine-learning/trainium/customers/)|公开资料未确认 tape-out、送样、晶圆量产、2026 出货量、真实库存或停产；GA/云端产品可用不等于已公开量产数字。|
|Trainium4（路线图）|本次已打开的一手资料只确认“更高 FP4 算力、更高内存带宽和更大 HBM 容量”，没有颗粒数、制程、HBM 类型、互联或功耗规格。|AWS 与 OpenAI 2026-02 战略合作公告称预计 **2027 年开始交付**；这是路线图/承诺节点，不是 GA 或云端可用日期。[官方公告](https://press.aboutamazon.com/2026/2/openai-and-amazon-announce-strategic-partnership)|OpenAI 的容量承诺覆盖 Trainium3 与 Trainium4；不能据此推导芯片已流片、量产或客户已部署。|tape-out、送样、量产、出货、GA、区域、停产：**未确认**。|

**代际命名提醒。** AWS Neuron 文档把 Trainium / Inferentia2 归入 NeuronCore-v2，把 Trainium2 归入 v3，把 Trainium3 归入 v4；“Trainium1/2/3”是产品代际，“NeuronCore-v1/v2/v3/v4”是核心架构代际，不能混成同一列。Inf1/Trn1/Inf2/Trn2/Trn3 是 EC2 实例或平台名称，也不能反推单颗芯片数量。

### 2.2 时间线与证据等级

|日期|事件|证据等级|
|---|---|---|
|2018-11-28|AWS 首次公开 Inferentia，目标是 2019 可用。|官方新闻稿；“预计可用”不等于 GA。|
|2019-12|Inf1/Inferentia GA。|AWS 后续官方博客回顾；未找到当日 GA 原始公告。|
|2020-11|re:Invent 公开 Trainium，目标为 2021 年下半年。|官方 re:Invent 直播记录；目标日期不等于出货。|
|2021-11-30|Trn1 预览。|官方 What's New。|
|2022-10-10|Trn1 GA。|官方 AWS News Blog。|
|2022 re:Invent|Inferentia2/Inf2 预览。|官方 Inf2 GA 博客回顾。|
|2023-04-13|Inf2 与 Trn1n GA。|官方 What's New。|
|2023-11|AWS 公开 Trainium2。|本次已打开的一手材料确认“下一代已宣布”，未在报告中补写未核实的具体日。|
|2024-12-03|Trn2 实例 GA；Trn2 UltraServer 为 preview。|官方 AWS News Blog。|
|2024-12-23|Neuron 2.21 加入 Trainium2、Trn2、NxD Inference。|官方 What's New。|
|2025-12-02|Trn3 UltraServer GA；Trainium3 产品公开。|官方 What's New。|
|2026-02|OpenAI/AWS 公告 Trainium4，预计 2027 开始交付。|官方新闻稿；路线图，不是 GA。|
|2026-05-26 至 2026-08-17|Neuron 2.30、2.31、2.32 逐步加入 Trainium3/NKI 新能力。|官方 release/What's New。|

当前仍没有公开、可交叉核验的 AWS 颗粒级“流片日、送样日、晶圆量产日、首批出货量、累计出货量、库存量”字段。对 AWS 自身服务已部署的芯片数量，只有公司或客户的叙述，不能冒充供应链审计。

### 2.3 客户部署、云可用与产品边界

- **芯片：** AWS 自研加速器，不向客户单独购买裸片；本报告不把芯片型号当成可直接采购的 PCIe 卡。
- **实例/服务器：** Inf1、Inf2、Trn1/Trn1n、Trn2 是 EC2 实例产品；Trn2/Trn3 UltraServer 是更大 scale-up 平台，不能把平台 HBM、带宽和 PFLOPS 回填为单芯片规格。
- **集群/云服务：** UltraCluster 是跨服务器的网络与调度边界；Amazon Bedrock 是托管模型 API。Bedrock 上的模型可用只证明云服务路径存在，不证明用户能租到对应的裸芯片或固定 Trn3 拓扑。
- **客户部署：** AWS 的 Trn1 客户案例和 Inferentia 客户名单是采用证据；Project Rainier、Anthropic 的近百万 Trainium2 口径是 AWS 客户页/博客中的公司叙述；对 Trainium3 只能写“产品 GA/客户页提及”，不把“预计继续扩展”写成已完成装机。
- **Inferentia 与 Trainium 的角色：** Inferentia 优先面向推理，Trainium 优先面向训练，但 Trainium 实例也可用于推理。架构、软件和实例边界比营销标签更重要。

## 3. 核心规格表

|项目|Trainium3 单芯片|Trn3 UltraServer Gen2（平台级）|
|---|---|---|
|制程/执行单元|3nm；8 个 NeuronCore-v4，每核含 Tensor、Vector、Scalar、GpSimd。[AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/)|144 颗芯片，36 台服务器、每台 4 颗。[架构表](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html)|
|格式/计算|FP32、BF16、MXFP8、MXFP4；GA 口径每芯片 [2.52 PFLOP FP8](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)。| [362,448 MXFP8/MXFP4 TFLOPS](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html)；FP16/BF16/TF32 为 96,624 TFLOPS。|
|存储|4 个 HBM stack、[144 GB HBM3e](https://aws.amazon.com/ec2/instance-types/trn3/)；每核 SBUF 32 MiB、PSUM 2 MiB。[NKI 架构指南](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html)|[20,736 GiB HBM](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html)，产品页约写 20.7 TB。|
|带宽|产品页 [4.9 TB/s](https://aws.amazon.com/ec2/instance-types/trn3/)；NKI 指南写 4.7 TB/s。[另一口径](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html)|[705.6 TB/s](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html)，产品页四舍五入为 706 TB/s。|
|互联/搬运|4 个 NeuronLink-v4、128 DMA engine、20 CC-Core。[NKI 指南](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html)|NeuronSwitch-v1 all-to-all；NeuronLink-v4 [2,048 GiB/s/device](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html)，EFA 28,800 Gbps。|
|功耗|绝对 TDP/芯片瓦数：**公开资料未确认**；只有相对 Trn2 UltraServer 超过 4 倍性能/瓦的比较。[产品页](https://aws.amazon.com/ec2/instance-types/trn3/)|不能把 Tokens/MW 或性能/瓦反推为机架功耗。|

**冲突口径。** `144 GB` 与 `144 GiB` 是单位/文档层级差异；4.9 与 4.7 TB/s 的原因 AWS 未解释，本文产品比较采用 4.9，同时保留 4.7。GA 新闻稿写 FP8，后续表写 MXFP8/MXFP4，不把两种命名当成可相加指标。互联旧摘要还出现 2.56 TB/s/device、16 CC-Core；本文采用最新 v2.32.0 平台表与当前 NKI 结构指南，不拼接不同版本数字。

## 4. ELI5：问题先行、机制与边界

**问题：** 长上下文解码每个 token 都要找历史 KV。真正耗时的部分可能是定位、搬运、离散 Gather 和跨芯片合并，不只是矩阵乘。

**机制：** Tensor Engine 做规则 GEMM；HBM 放大数据，SBUF/PSUM 放近计算的工作集，DMA 搬运；NKI 可写接近 ISA 的 kernel。segmented attention 按 KV 区段处理，KV-parallel prefill 让不同 rank 处理分片 KV，再做 online softmax 合并；NKI 0.6 还提供 GpSimd `topk`、可变长度 collective 和数据依赖循环。[NKI 0.6](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/release-notes/components/nki.html)

**类比：** HBM 像大仓库，SBUF 像操作台，DMA 是叉车，block table 是货架地图；分段 attention 是分区拣货，KV-parallel 是多人拣货后合单。边界是：这只解释数据流，不表示 Trainium3 自动拥有通用搜索索引；AWS 的 kernel 仍是 KV/Attention 语义，不能把它宣传成任意 exact retrieval。

## 5. 与附件《推导推理GPU新路径-ELI5.html》的映射

|附件路径|直接解决|间接帮助|没有解决/证据不足|
|---|---|---|---|
|密集计算|多类 NeuronCore engine、MXFP8/MXFP4 直接覆盖规则 GEMM/Attention。|HBM、SBUF/PSUM 减少等待。|没有证明峰值 FLOPS 解决 Indexer 搬运。|
|Search / Indexer|有实验性的 [Sparse Attention Indexer](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/nki/library/api/sparse-attention-indexer-mx-bf16score.html)，含 MX projection、BF16 score。|NKI 允许模型相关 kernel。|不是通用 Retrieval Plane，也没有通用 exact Search ISA。|
|Top-k / Reduce|有 [GpSimd Top-k 与 Top-k Reduce](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/nki/library/api/topk-reduce.html)。|可变长度 collective 适合不等长候选。|未证明已实现“各 HBM 分区 Local Top-k + Global Merge”。|
|离散 KV Gather|[indirect DMA Gather](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/nki/library/api/gather.html) 与 block-based KV 直接相关。|片上 tensor indirection 放宽布局限制。|2D 行 Gather 不等于跨 HBM 的任意 page-aware Gather DMA。|
|Address / Route|Trn3 switched fabric 用地址编码路由芯片。[架构表](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html)|NeuronSwitch-v1 有利于 collective。|不是附件所说的语义索引、Page Translator 或动态地址簿。|
|跨卡通信|NeuronSwitch-v1、EFA、KV-parallel 的分片与 online merge 直接覆盖平台通信。|可扩展的 scale-up 域提供工程底座。|没有证据把通信量降到附件的 `P×k` 候选。|
|TPOT / TTFT / Tokens/J|公开了 prefix-cache 的测试方法和相对能效。|分段 KV、融合 kernel 可能改善这些指标。|Trainium3 的端到端 TPOT、TTFT、Tokens/J、HBM bytes/token、跨卡 bytes/token：**公开资料未确认**。|

## 6. 六维创新性评分

这是架构研究价值判断，不是 benchmark，也不是 AWS 官方评分。

|维度|权重|分数|加权|
|---|---:|---:|---:|
|数据搬运/存储|30%|8.5|25.5|
|执行架构|20%|7.5|15.0|
|稀疏/动态计算|15%|8.0|12.0|
|Scale-up/互联|15%|9.0|13.5|
|数值格式/计算密度|10%|9.0|9.0|
|可编程性|10%|8.5|8.5|
|**总分**|**100%**| |**83.5/100**|

理由是：Trainium3 对数据搬运、动态 kernel 和 scale-up 的启发强，但仍没有公开独立 Retrieval Core，也没有附件所需的端到端检索指标。

## 6A. 独立基准与可比性边界

截至 2026-09-01，本次没有找到把 Trainium3 与 H200/B200 在同一模型、同一 batch、同一精度、同一服务栈和同一价格口径下复测的第三方结果。一个公开的独立测试页面报告了 Trn1 的 32-core 独立分片吞吐、Trn2 的 70B LoRA / Mixtral 端到端验证，但明确说这些实验不是统一的 price-performance benchmark。[BrazenLab Trainium Validation Evidence](https://brazenlab.ai/research.html)

另一个公开对比也指出，Trainium3 可用数字主要是 AWS 内部/厂商口径，而 H200 数字来自独立测量，不能直接拼成排名。[Spheron 2026 comparison](https://www.spheron.network/blog/aws-trainium-3-vs-nvidia-h200-b200-llm-training-inference-2026/)

|证据|可写成什么|不能写成什么|
|---|---|---|
|AWS Trn3 产品页：2.52 PFLOPS/chip、4.9 TB/s、4.4x/4x、Bedrock 3x|官方规格或 AWS 自测/主张，取决于字段|不能写成独立实验、全模型平均或跨供应商普适优势|
|AWS Neuron NKI/库函数|API/编程能力已公开；包括 segmented attention、KV-parallel prefill、Gather、Top-k Reduce 等|不能写成硬件已有独立 Search Core，或证明每 token 的跨卡通信量已降到某个复杂度|
|BrazenLab Trn1/Trn2|独立作者公开了可复核的实验范围与部分结果|不能把 Trn1/Trn2 结果外推成 Trainium3；不能把独立分片吞吐当单作业延迟|
|MLCommons Training v6.0 公共参考/结果索引|本次查验未定位到 AWS Trainium/Inferentia 的 MLPerf 正式提交|不能据此证明全球绝对没有任何其他第三方基准，也不能把 reference implementation 当提交结果。[MLCommons training](https://github.com/mlcommons/training)、[MLCommons results](https://github.com/mlcommons/training_results_v6.0)|

应优先要求未来公开 `TTFT`、`TPOT`、p50/p99、吞吐、功耗、HBM bytes/token、NeuronLink/EFA bytes/token、模型质量和编译/移植成本；仅有 PFLOPS 或“性能/瓦”无法回答长上下文推理的端到端问题。

## 6B. 软件栈与操作原语证据矩阵

|层级|已公开能力|证据性质与限制|
|---|---|---|
|框架/编译|PyTorch、JAX、Hugging Face Optimum Neuron、OpenXLA、NxD Training/Inference、vLLM Neuron；支持动态 shape、控制流、custom operator、profiling。|官方软件能力；具体模型仍受算子覆盖、编译时间、布局和版本限制。|
|低层编程|NKI 直接暴露 tile、SBUF/PSUM、DMA、同步和调度；Neuron 2.30–2.32 持续增加 Trn3 能力。|官方文档/API；可编程不等于已有通用硬件检索指令。|
|Search / Indexer|Sparse Attention Indexer kernel 含 MX projection 与 BF16 score。|实验性/模型相关 kernel；不等于通用 exact retrieval。|
|Reduce|CC-Cores、collective、online softmax merge、variable-length collective。|能支持分片结果合并；未公开任意 Top-k 的端到端成本。|
|Top-k|GpSimd `topk`、Top-k Reduce。|API/库函数事实；未证明 HBM 分区 local Top-k 后 global merge 的完整硬件路径。|
|Address / Route|NeuronLink/NeuronSwitch 负责芯片互联与 collective 路由；软件有 block/page 语义。|网络地址/拓扑路由；不是语义索引、Page Translator 或动态地址簿。|
|Gather|indirect DMA Gather、tensor indirection、block-based KV 相关用法。|片上/设备内数据搬运 API；2D Gather 不等于跨 HBM 任意 page-aware Gather。|
|KV|segmented attention、KV-parallel prefill、block KV、prefix cache、decode/context parallel 文档。|直接对应 KV/Attention 数据流；没有证明任意 KV 检索都变成 `O(k)`。|
|跨卡|NeuronLink-v2/v3/v4、NeuronSwitch-v1、EFA、TP/PP/EP/CP 与 online merge。|通信底座和并行编程事实；没有公开 Trn3 的端到端 bytes/token 或 p99。|

**分析判断。** AWS 的创新重点是“可编程的内存搬运 + 集合通信 + 模型相关 kernel”与高密度 scale-up 的组合；它对附件提出的 Retrieval Plane 是可借鉴的工程样本，但截至截止日仍不能把该组合命名为已经产品化的通用 Retrieval Plane。

## 7. 局限与常见误解

1. 3nm 不等于绝对低功耗；TDP 未公开，性能/瓦不能替代实测瓦数。
2. 144 GB HBM3e 不是片上缓存；KV layout、块大小、延迟和有效容量仍是瓶颈。
3. Sparse Attention Indexer 是实验性、模型相关 kernel，不等于通用搜索芯片。
4. Segmented attention 解决分段/分页 KV，不自动把精确扫描变成 `O(k)`。
5. All-to-all 改善互联路径，不保证跨卡 bytes/token 已经很低；量产和实际装机也未公开确认。

## 8. 下一代 Retrieval GPU 可借鉴点

- **可直接借鉴：** software-managed scratchpad、indirect DMA/片上 tensor indirection、分段 KV、Gather/Top-k/Reduce 原语、局部计算加在线合并、可编程通信路由。
- **只能类比：** NeuronSwitch-v1 是 scale-up 底座参考，不等于 Local Top-k 候选合并；Sparse Indexer 是 kernel 组织参考，不是通用 Search ISA；MXFP4/8 需单独验证精确 score 误差。
- **不宜照搬：** DeepSeek 专用公式、固定 k/block size、把 page table 硬焊进芯片、把 144 芯片带宽线性折算到单卡、用 PFLOPS 替代 TPOT/TTFT/Tokens/J 验收。

## 9. 关键参考来源

1. [AWS News Blog：Trn2 instances 与 UltraServers](https://aws.amazon.com/blogs/aws/amazon-ec2-trn2-instances-and-trn2-ultraservers-for-aiml-training-and-inference-is-now-available/)
2. [AWS What's New：Trn3 UltraServers GA](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)
3. [Amazon EC2 Trn3 产品页](https://aws.amazon.com/ec2/instance-types/trn3/)
4. [AWS Neuron Trn3 Architecture](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html)
5. [Trainium3 NKI Architecture Guide](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html)
6. [NKI 0.6.0 / Neuron 2.32 What's New](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/whats-new.html)
7. [NKI Library kernels](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/nki/library/api/index.html)
8. [AWS Trainium customers](https://aws.amazon.com/ai/machine-learning/trainium/customers/)
9. [AWS Inferentia customers/product page](https://aws.amazon.com/ai/machine-learning/inferentia/)
10. [AWS OpenAI strategic partnership：Trainium4 2027 roadmap](https://press.aboutamazon.com/2026/2/openai-and-amazon-announce-strategic-partnership)
11. [BrazenLab independent Trainium validation](https://brazenlab.ai/research.html)
12. [Spheron public Trainium3 comparison and limitations](https://www.spheron.network/blog/aws-trainium-3-vs-nvidia-h200-b200-llm-training-inference-2026/)
13. [MLCommons Training repository](https://github.com/mlcommons/training)
