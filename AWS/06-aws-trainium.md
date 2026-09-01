# AWS Trainium3 / Trn3 UltraServer：面向推理数据流的架构研究

> 资料访问日：2026-08-22。范围只研究 AWS；文中“首发、宣布、GA/上市、量产/部署”分开记录。

## 1. 一句话结论

Trainium3 的最新目标是用 [3nm、HBM3e、MXFP8/MXFP4](https://aws.amazon.com/ec2/instance-types/trn3/)、NeuronSwitch-v1 和 NKI 支撑长上下文与 MoE 推理；最值得研究的不是峰值 FLOPS，而是把存储、DMA、Top-k/Reduce、集合通信和 [144 芯片 scale-up](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html) 放进同一条数据路径。

## 2. 目标芯片与时间状态

边界必须分开：Trainium3 是单芯片；Trn3 UltraServer 是多芯片服务器级 scale-up 域；UltraCluster 3.0 是继续扩展的集群/云服务形态。选择它，是因为 AWS 已公开与附件相邻的 segmented attention、KV-parallel prefill、Gather、Top-k 和 Sparse Attention Indexer kernel。

|对象|窗口内状态（2025-07-01 至 2026-08-22）|
|---|---|
|Trainium3 芯片|**首发/宣布为 2024-12-03，窗口外**；AWS 当时预计首批实例于 2025 年末可用，不能写成窗口内首发。[AWS Press Center](https://press.aboutamazon.com/2024/12/aws-trainium2-instances-now-generally-available)|
|Trn3 UltraServer|**GA/上市：2025-12-02，窗口内**；GA 新闻稿公开单芯片和平台口径。[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)|
|UltraCluster 3.0|是 UltraServer 的集群部署边界；AWS 宣称可扩展到数十万芯片，但这是平台能力，不是已审计的实际部署量。[EC2 Trn3](https://aws.amazon.com/ec2/instance-types/trn3/)|
|软件可用性|Neuron 2.30 GA 于 2026-05-26，2.31 于 2026-07-08，2.32 于 2026-08-17；NKI 0.4/0.5/0.6 和相关 kernels 在窗口内逐步可用。[2.30](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-announce-neuron-2-30-0/)、[2.31](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-announce-neuron-2-31-0/)、[2.32](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/whats-new.html)|
|量产/实际装机|晶圆量产、良率、出货量和真实库存：**公开资料未确认**。|

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

1. [AWS Press Center：Trainium3 首次公开](https://press.aboutamazon.com/2024/12/aws-trainium2-instances-now-generally-available)
2. [AWS What's New：Trn3 UltraServers GA](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)
3. [Amazon EC2 Trn3 产品页](https://aws.amazon.com/ec2/instance-types/trn3/)
4. [AWS Neuron Trn3 Architecture](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/arch/neuron-hardware/trn3-arch.html)
5. [Trainium3 NKI Architecture Guide](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/guides/architecture/trainium3_arch.html)
6. [NKI 0.6.0 / Neuron 2.32 What's New](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/about-neuron/whats-new.html)
7. [NKI Library kernels](https://awsdocs-neuron.readthedocs-hosted.com/en/v2.32.0/nki/library/api/index.html)
