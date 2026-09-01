# Google TPU 与附件新推理 GPU 方案对照

> 研究厂商｜Google TPU  
> 目标时间｜2025-07-01 至 2026-08-22  
> 资料访问日｜2026-08-22  
> 研究对象｜TPU7x/Ironwood，以及窗口内后续公开的 TPU 8t、TPU 8i

## 一句话结论

Ironwood最值得研究的地方，是把高密度 TensorCore、面向不规则访问的 SparseCore、HBM 和大规模 ICI 放进同一个推理与训练系统。它对附件的 Move、Route、部分 Address 和跨卡 collective 有真实对应，对 Search、精确 Top-k、score materialization 消除和 page-aware KV Gather 没有公开的专用证据。2026-04-22 宣布的 TPU 8i 更接近附件的问题定义，它增加 CAE、384 MB 片上 SRAM 和 Boardfly 低跳数互联，但截至 2026-08-22 仍标为 Coming soon，不能把宣传方向写成可用芯片的端到端结果。[Google TPU 产品页](https://cloud.google.com/tpu?hl=en)（访问日期｜2026-08-22）

## 时间口径与产品状态

严格按窗口，Ironwood 的首次宣布发生在 2025-04-09，早于窗口。它在 2025-11-06 被 Google 宣布进入 General Availability，2025-11-25 的官方文章称已面向 Cloud customers available；当前 TPU 产品页把 Ironwood 标为 Generally available，所以本文把它作为窗口内“可用”对象，而不把 2025-04 的宣布日期伪装成窗口内发布。Google没有给出独立的量产或出货日期，量产状态写作“公开资料未确认”。[首次宣布](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/)（访问日期｜2026-08-22） [GA公告](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads)（访问日期｜2026-08-22） [可用公告](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-google-tpu-things-to-know/)（访问日期｜2026-08-22）

TPU 8t 与 TPU 8i 在 2026-04-22 于 Cloud Next 26 宣布，属于窗口内的新款。Google的第八代产品文章写的是两者将在今年稍后 GA，当前产品页仍标为 Coming soon。它们是“宣布”，不是“量产/可用”证据。本文纳入二者，是为了满足严格时间窗，并把 Ironwood 放在后续 Google TPU 的真实演进线上。截至 2026-08-22，官方 TPU 产品页未列出比 8t/8i 更新的 Google TPU。[第八代宣布](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)（访问日期｜2026-08-22） [当前状态页](https://cloud.google.com/tpu?hl=en)（访问日期｜2026-08-22）

## 核心规格表

| 项目 | TPU7x/Ironwood | TPU 8t | TPU 8i |
|---|---|---|---|
| 制程 | 公开资料未确认 | 公开资料未确认 | 公开资料未确认 |
| 单芯片密集计算 | 2 个 TensorCore；BF16 峰值 2,307 TFLOPs，FP8 峰值 4,614 TFLOPs | 原生 FP4；官方技术表列峰值 FP4 12.6 PFLOPs | 2 个 TensorCore；官方技术表列峰值 FP4 10.1 PFLOPs |
| SparseCore 或专用单元 | Cloud TPU 架构页写 4 个 SparseCore | 有 SparseCore，数量公开资料未确认 | 1 个 CAE，官方称替代 Ironwood 的 4 个 SparseCore |
| HBM | 每芯片 192 GiB；7,380 GB/s，文档正文约写 7.37 TB/s | 216 GB；6,528 GB/s | 288 GB；8,601 GB/s |
| 片上 SRAM 或 VMEM | VMEM 是高带宽片上 scratchpad，容量未给出 | 128 MB VMEM | 384 MB SRAM/VMEM，约为上一代 3 倍 |
| 芯片内互联 | 双向 ICI 1,200 GB/s；3D torus 每轴 200 GB/s | ICI scale-up 带宽为 Ironwood 的 2 倍，绝对单芯片值未公开 | 宣传口径为 19.2 Tb/s；Boardfly，最大跳数公开为 7 |
| Pod 规模 | 9,216 芯片；官方另称约 1.77 PB HBM、近 10 MW 系统规模 | 9,600 芯片；2 PB 共享 HBM；121 ExaFlops 系统宣传值 | 官方宣布页写 1,152 芯片；技术深潜的详细拓扑写最多 1,024 active chips |
| 功耗 | 单芯片 TDP 未公开；近 10 MW 是大 Pod 级口径 | 单芯片 TDP 未公开；官方称较 Ironwood 最多 2 倍性能/瓦 | 单芯片 TDP 未公开；官方称较 Ironwood 最多 2 倍性能/瓦 |
| 主要状态 | GA，当前产品页标为 Generally available | 宣布，Coming soon | 宣布，Coming soon |

Ironwood 数字来自 [TPU7x 官方架构文档](https://docs.cloud.google.com/tpu/docs/tpu7x)（访问日期｜2026-08-22）、[Ironwood 系统公告](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads)（访问日期｜2026-08-22）和[首次架构宣布](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/)（访问日期｜2026-08-22）。8t/8i 数字来自 [Google 第八代架构深潜](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)（访问日期｜2026-08-22）与[第八代宣布页](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)（访问日期｜2026-08-22）。这里的 PFLOPs、ExaFlops、性能/瓦都是官方峰值或宣传口径，不是本文测得的推理吞吐。

### 官方资料冲突

Ironwood 的 SparseCore 数量有单位差异。Cloud TPU 架构页和 TPU7x 规格表按物理芯片写 4 个，双 chiplet 结构是每个 chiplet 1 个 TensorCore、2 个 SparseCore。JAX Pallas 开发文档则把 TPU7x 写成 2 个逻辑 SparseCore、4 个 physical cores，并且运行时示例返回 `num_cores=2`。本文采用硬件盘点口径 4 个物理单元，同时注明编程模型可见的逻辑口径 2 个，不把它们相加。[Cloud TPU 架构](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm)（访问日期｜2026-08-22） [JAX SparseCore 文档](https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)（访问日期｜2026-08-22）

8i 的 Pod 规模也有冲突。Google 的高层宣布页写 1,152，技术深潜的 Boardfly 分解写 36 组、最多 1,024 active chips。本文在讨论具体拓扑、跳数和资源规划时采用更细的 1,024，保留 1,152 作为官方未解决的高层口径。[宣布页](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/)（访问日期｜2026-08-22） [技术深潜](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)（访问日期｜2026-08-22）

## 先看附件提出的四类问题

附件把新推理 GPU 拆成 Tensor Plane 和 Retrieval Plane，原文见[《推导推理GPU新路径-ELI5.html》](/Users/chenmingmin/Documents/GitHub/ai_infra_chip/推导推理GPU新路径-ELI5.html)。它提出的四类问题如下。

1. **密集计算**。GEMM、FFN、Attention 等规则计算适合 TensorCore。附件的判断是，增加 FLOPS 不能自动覆盖检索、地址 bookkeeping 和数据移动造成的等待，因此 Tensor Plane 应继续负责规则计算。
2. **动态检索与 Indexer**。Query 运行时才知道候选位置，Indexer要做打分、找位置和地址转换，形态更接近搜索引擎和地址簿。精确扫描在没有额外索引时仍可能是 O(L)，附件把“必须完整物化 score”列为待验证假设。
3. **Top-k 与 Reduce**。候选分数需要比较、规约和保留索引。附件建议流式 score、每个分区 Local Top-k、再做 Global Merge，目标是少写回完整 score，减少跨卡数据对象；它没有声称这样会自动减少精确扫描量。
4. **离散 KV Gather 与跨卡通信**。Top-k 结果要翻译成 page、物理地址和 Gather descriptor，再读取不相邻 KV。多卡场景还要处理 all-gather、reduce 或候选合并。附件提出 Gather DMA、Route、Address 和以 candidate/block 为轴的切分。

## ELI5 看 Ironwood 与后续款

把 TensorCore 想成一座能高速生产规则砖块的工厂，把 SparseCore 想成负责从大仓库按编号取货、整理和通信的分拣线。Ironwood 让两条线并存，并用 192 GiB HBM 做远端仓库、VMEM 做近端工作台、ICI 做芯片间道路。它还允许 SparseCore Collective Offloading，让 All-Gather 或 Reduce-Scatter 在 TensorCore 计算时并行推进，这直接说明 Google把不规则数据流和通信控制从主矩阵路径旁路出去。[Ironwood 性能文档](https://docs.cloud.google.com/tpu/docs/ironwood-performance)（访问日期｜2026-08-22）

这个类比的边界很重要。SparseCore公开的主要对象是 embedding lookup 与稀疏操作；JAX文档还公开了 dynamic indexing、DMA、排序、indexed gather/scatter。它可以作为附件 Retrieval Plane 的结构先例，但没有证据表明 Ironwood 有面向 Indexer 的 Q×K Search、流式精确 Top-k、KV page translator 或一个把 Top-k 结果直接交给 KV DMA 的硬件队列。TPU v4 原始论文报告 SparseCore 主要加速 embedding，并把它作为旧一代架构参考，不能把论文中的 5–7 倍 embedding 加速移植成 Indexer 加速。[SparseCore 开发文档](https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)（访问日期｜2026-08-22） [TPU v4 原始论文](https://arxiv.org/abs/2304.01433)（访问日期｜2026-08-22）

TPU 8t 把这条思路继续用于训练和 embedding-heavy workload，并加入原生 FP4、SparseCore data-dependent all-gather、TPUDirect RDMA 和 TPUDirect Storage。它更直接解决大规模数据输入与通信，仍然没有公开附件所需的 Indexer Top-k 证据。TPU 8i 则把问题移向采样和服务，384 MB 片上 SRAM 用于更大的 KV cache，CAE负责 Reduce 与同步，Boardfly用较少跳数服务 all-to-all。对附件来说，8i是最值得继续追踪的 Google 芯片，但公开资料仍没有 Indexed KV Gather、Local/Global Top-k 或 score materialization 消除的确认。[8t/8i 技术深潜](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)（访问日期｜2026-08-22）

## 对附件系统动作的映射

| 附件动作或指标 | 公开能力映射 | 判断 | 证据 |
|---|---|---|---|
| Dense compute | Ironwood 2 个 TensorCore，BF16/FP8 峰值明确；8t原生 FP4 | 直接解决密集算力，不能替代 Retrieval Plane | [TPU7x文档](https://docs.cloud.google.com/tpu/docs/tpu7x)（访问日期｜2026-08-22） |
| Search | SparseCore 面向 embedding lookup，8i CAE面向 reduce/sync | 没有解决或证据不足，未公开 Indexer Search | [SparseCore文档](https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)（访问日期｜2026-08-22） |
| Select、Top-k | 公开了排序、计数、规约相关能力，但没有专用 Top-k 或 Merge Top-k 说明 | 间接帮助，Local/Global Top-k 没有证据 | [SparseCore文档](https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)（访问日期｜2026-08-22） |
| score materialization | HBM、VMEM、8i SRAM有利于保存中间数据；资料未承诺流式 score | 间接帮助，是否消除物化未确认 | [Ironwood性能文档](https://docs.cloud.google.com/tpu/docs/ironwood-performance)（访问日期｜2026-08-22） |
| Move、Address | SparseCore支持 indexed gather/scatter、dynamic indexing、DMA；Ironwood有 VMEM/HBM层次 | 直接覆盖通用离散搬运，KV page/address descriptor 未公开 | [SparseCore文档](https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)（访问日期｜2026-08-22） |
| Route、跨卡通信 | Ironwood ICI、3D torus、collective offload；8i Boardfly、CAE和 OCS | 直接解决 collective 与网络路径，未解决候选级 KV 路由 | [Ironwood性能文档](https://docs.cloud.google.com/tpu/docs/ironwood-performance)（访问日期｜2026-08-22） [8i深潜](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)（访问日期｜2026-08-22） |
| Gather | JAX层面有 HBM indexed gather | 对通用 Gather 是直接帮助，对 page-aware KV Gather DMA 仍属证据不足 | [Gather/scatter文档](https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)（访问日期｜2026-08-22） |
| TPOT、TTFT、Tokens/J | Google给出峰值、性能/瓦、性能/美元和低延迟定位 | 没有公开附件同口径的 Indexer TPOT、TTFT、Tokens/J 或 J/token | [Google TPU产品页](https://cloud.google.com/tpu?hl=en)（访问日期｜2026-08-22） |

## 创新性判断

以下是沿用附件权重的架构研究价值判断，满分 100，不是 benchmark。六项分数都是分析判断，针对 GA 的 Ironwood，并把 SparseCore 的公开边界纳入扣分。[TPU7x 官方架构文档](https://docs.cloud.google.com/tpu/docs/tpu7x)（访问日期｜2026-08-22）

| 维度 | 权重 | 得分 | 理由 |
|---|---:|---:|---|
| 数据搬运与存储 | 30% | 24 | 192 GiB HBM、7.38 TB/s、VMEM、双 chiplet 与通用 indexed gather；没有公开 KV page 数据流 |
| 执行架构 | 20% | 15 | TensorCore 与 SparseCore 分工，SparseCore可独立承载通信控制；没有公开 Top-k 专用执行单元 |
| 稀疏与动态计算 | 15% | 9 | embedding、随机访问、DMA和 gather/scatter有基础；Indexer Search 语义未确认 |
| Scale-up 与互联 | 15% | 14 | 3D torus、1,200 GB/s 双向 ICI、9,216 芯片和 OCS 具备系统价值；通信模式仍需按检索 workload 测量 |
| 数值格式与计算密度 | 10% | 8 | 原生 FP8 和 4,614 TFLOPs 峰值有价值；对稀疏地址与 Top-k收益有限 |
| 可编程性 | 10% | 7 | JAX、PyTorch、Pallas和双 chiplet 可见性较好；TensorFlow不支持，硬件描述符接口未公开 |
| **合计** | **100%** | **77** | **对附件 Retrieval GPU 的研究价值较高，不能解读为性能排名** |

TPU 8i若按附件问题打分，CAE、片上 KV 容量和 Boardfly会让它的研究信号高于 Ironwood；由于它仍是 announced/Coming soon，且没有公开真实 TPOT、TTFT 和 Gather 结果，本文不把这个判断升级成已验证分数。

## 局限与常见误解

- 官方峰值 FLOPs、Pod 总 ExaFlops、性能/瓦和性能/美元都依赖精度、并行度、软件栈和系统边界。它们不能推出 Indexer 的端到端 TPOT，也不能推出 Tokens/J。[8t/8i技术深潜](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)（访问日期｜2026-08-22）
- SparseCore 的 embedding lookup 与附件 Indexer 有共同的随机访问特征，工作集、分数计算、Top-k语义和 KV layout 仍不同。embedding 加速不能直接等同 Indexer 加速。[TPU v4原始论文](https://arxiv.org/abs/2304.01433)（访问日期｜2026-08-22）
- “1.77 PB 共享 HBM”描述的是 Pod 级可访问总量。Ironwood 两个 chiplet 各有独立 96 GB 内存空间，公开资料没有把它描述成单一平坦 cache。[TPU7x 双 chiplet 文档](https://docs.cloud.google.com/tpu/docs/tpu7x)（访问日期｜2026-08-22）
- ICI带宽能降低通信成本，却不自动产生 Local Top-k、Global Merge 或 Gather descriptor。拓扑只解决路，数据对象和算法仍要由软件与硬件共同定义。[TPU7x拓扑文档](https://docs.cloud.google.com/tpu/docs/tpu7x)（访问日期｜2026-08-22）
- Ironwood GA 不等于任何项目都能无预约使用，Google训练文档仍要求先获得 TPU7x access 并联系 account team。8t/8i则明确仍是 Coming soon。[TPU7x训练文档](https://docs.cloud.google.com/tpu/docs/tpu7x-training)（访问日期｜2026-08-22） [状态页](https://cloud.google.com/tpu?hl=en)（访问日期｜2026-08-22）

## 对下一代 Retrieval GPU 的借鉴

下面五点均为基于官方资料和附件的推论，不代表 Google 已经实现了完整 Retrieval Plane。

1. **可直接借鉴**。沿用 TensorCore 与不规则数据平面并置的组织方式，让 Search、Reduce、Gather和通信控制有独立执行资源，并允许与密集计算重叠。
2. **可直接借鉴**。把 indexed gather/scatter、DMA、近端 scratchpad 和持久化 descriptor 队列做成可编程基础设施，再增加 page、物理地址和 KV layout 语义。
3. **可直接借鉴**。把 collective offload 与 Local/Global Top-k 一起设计，先在每个 HBM 分区保留小候选，再让互联只传候选和地址描述。
4. **只能类比**。3D torus适合邻近、规则的并行通信，Boardfly适合降低 all-to-all 跳数。二者都不能直接当成 candidate-aware KV Route；拓扑要由 TPOT、跨卡 bytes/token 和尾延迟实验选择。
5. **不宜照搬**。不要把 embedding SparseCore、CAE或 FP4 直接命名为 Retrieval Core，也不要把某个模型的 Indexer 公式焊死。附件提出的 Exact Mode、Approximate Mode、Top-k 和 Gather 必须分别验证 recall、精确一致性、HBM bytes/token、跨卡 bytes/token 与 J/token。

## 参考来源

1. [Google Cloud TPU 产品页，含 Ironwood GA 与 TPU 8t/8i Coming soon 状态，访问日期 2026-08-22](https://cloud.google.com/tpu?hl=en)
2. [TPU7x/Ironwood 官方架构与规格文档，访问日期 2026-08-22](https://docs.cloud.google.com/tpu/docs/tpu7x)
3. [Ironwood GA 公告，2025-11-06，访问日期 2026-08-22](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads)
4. [Ironwood 面向 Cloud customers available 的官方文章，2025-11-25，访问日期 2026-08-22](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-google-tpu-things-to-know/)
5. [Google 第八代 TPU 宣布，2026-04-22，访问日期 2026-08-22](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)
6. [TPU 8t/8i architecture deep dive，含 SparseCore、CAE、Boardfly 与芯片表，2026-04-22，访问日期 2026-08-22](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)
7. [JAX Pallas SparseCore 开发文档，含 dynamic indexing、DMA、gather/scatter，访问日期 2026-08-22](https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)
8. [TPU v4 原始论文，作为 SparseCore 的上一代架构基线，访问日期 2026-08-22](https://arxiv.org/abs/2304.01433)
