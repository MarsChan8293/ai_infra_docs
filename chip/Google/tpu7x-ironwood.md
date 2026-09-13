# Google / 谷歌 — TPU7x / Ironwood

- 研究截止日：2026-09-05
- 核验日期：2026-09-05
- 产品层级：TPU ASIC/Cloud TPU
- 厂商总览：[Google TPU](./Google-overview.md) · [[Google-overview|图谱总览]]
- 页面性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容按对象边界重排自现有综合报告，并以本页直接来源清单核验；不能由相邻产品层级推导的项目保留为“公开资料未确认”。

资料访问日｜2026-09-01（本次复核）；原有 2026-08-22 访问标记保留在历史段落中
研究对象｜TPU7x/Ironwood，以及窗口内后续公开的 TPU 8t、TPU 8i

Ironwood最值得研究的地方，是把高密度 TensorCore、面向不规则访问的 SparseCore、HBM 和大规模 ICI 放进同一个推理与训练系统。它对附件的 Move、Route、部分 Address 和跨卡 collective 有真实对应，对 Search、精确 Top-k、score materialization 消除和 page-aware KV Gather 没有公开的专用证据。2026-04-22 宣布的 TPU 8i 更接近附件的问题定义，它增加 CAE、384 MB 片上 SRAM 和 Boardfly 低跳数互联，但截至 2026-09-01 仍标为 Coming soon，不能把宣传方向写成可用芯片的端到端结果。[Google TPU 产品页](https://cloud.google.com/tpu?hl=en)（本次复核日期｜2026-09-01；原有 2026-08-22 访问标记保留）

严格按窗口，Ironwood 的首次宣布发生在 2025-04-09，早于窗口。它在 2025-11-06 被 Google 宣布进入 General Availability，2025-11-25 的官方文章称已面向 Cloud customers available；当前 TPU 产品页把 Ironwood 标为 Generally available，所以本文把它作为窗口内“可用”对象，而不把 2025-04 的宣布日期伪装成窗口内发布。Google没有给出独立的量产或出货日期，量产状态写作“公开资料未确认”。[首次宣布](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/)（访问日期｜2026-08-22） [GA公告](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads)（访问日期｜2026-08-22） [可用公告](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-google-tpu-things-to-know/)（访问日期｜2026-08-22）

TPU 8t 与 TPU 8i 在 2026-04-22 于 Cloud Next 26 宣布，属于窗口内的新款。Google的第八代产品文章写的是两者将在今年稍后 GA，当前产品页仍标为 Coming soon。它们是“宣布”，不是“量产/可用”证据。本文纳入二者，是为了满足严格时间窗，并把 Ironwood 放在后续 Google TPU 的真实演进线上。截至 2026-08-22，官方 TPU 产品页未列出比 8t/8i 更新的 Google TPU。[第八代宣布](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)（访问日期｜2026-08-22） [当前状态页](https://cloud.google.com/tpu?hl=en)（访问日期｜2026-08-22）

Ironwood 数字来自 [TPU7x 官方架构文档](https://docs.cloud.google.com/tpu/docs/tpu7x)（访问日期｜2026-08-22）、[Ironwood 架构页](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/)、[系统公告](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads)（访问日期｜2026-08-22）和[首次架构宣布](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/)（访问日期｜2026-08-22）。8t/8i 数字来自 [Google 第八代架构深潜](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)（访问日期｜2026-08-22）与[第八代宣布页](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)（访问日期｜2026-08-22）。这里的 PFLOPs、ExaFlops、性能/瓦都是官方峰值或宣传口径，不是本文测得的推理吞吐。

Ironwood 的 SparseCore 数量有单位差异。Cloud TPU 架构页和 TPU7x 规格表按物理芯片写 4 个，双 chiplet 结构是每个 chiplet 1 个 TensorCore、2 个 SparseCore。JAX Pallas 开发文档则把 TPU7x 写成 2 个逻辑 SparseCore、4 个 physical cores，并且运行时示例返回 `num_cores=2`。本文采用硬件盘点口径 4 个物理单元，同时注明编程模型可见的逻辑口径 2 个，不把它们相加。[Cloud TPU 架构](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm)（访问日期｜2026-08-22） [JAX SparseCore 文档](https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)（访问日期｜2026-08-22）

## ELI5 看 Ironwood 与后续款

把 TensorCore 想成一座能高速生产规则砖块的工厂，把 SparseCore 想成负责从大仓库按编号取货、整理和通信的分拣线。Ironwood 让两条线并存，并用 192 GiB HBM 做远端仓库、VMEM 做近端工作台、ICI 做芯片间道路。它还允许 SparseCore Collective Offloading，让 All-Gather 或 Reduce-Scatter 在 TensorCore 计算时并行推进，这直接说明 Google把不规则数据流和通信控制从主矩阵路径旁路出去。[Ironwood 性能文档](https://docs.cloud.google.com/tpu/docs/ironwood-performance)（访问日期｜2026-08-22）

这个类比的边界很重要。SparseCore公开的主要对象是 embedding lookup 与稀疏操作；JAX文档还公开了 dynamic indexing、DMA、排序、indexed gather/scatter。它可以作为附件 Retrieval Plane 的结构先例，但没有证据表明 Ironwood 有面向 Indexer 的 Q×K Search、流式精确 Top-k、KV page translator 或一个把 Top-k 结果直接交给 KV DMA 的硬件队列。TPU v4 原始论文报告 SparseCore 主要加速 embedding，并把它作为旧一代架构参考，不能把论文中的 5–7 倍 embedding 加速移植成 Indexer 加速。[SparseCore 开发文档](https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)（访问日期｜2026-08-22） [TPU v4 原始论文](https://arxiv.org/abs/2304.01433)（访问日期｜2026-08-22）

以下是沿用附件权重的架构研究价值判断，满分 100，不是 benchmark。六项分数都是分析判断，针对 GA 的 Ironwood，并把 SparseCore 的公开边界纳入扣分。[TPU7x 官方架构文档](https://docs.cloud.google.com/tpu/docs/tpu7x)（访问日期｜2026-08-22）

TPU 8i若按附件问题打分，CAE、片上 KV 容量和 Boardfly会让它的研究信号高于 Ironwood；由于它仍是 announced/Coming soon，且没有公开真实 TPOT、TTFT 和 Gather 结果，本文不把这个判断升级成已验证分数。

- SparseCore 的 embedding lookup 与附件 Indexer 有共同的随机访问特征，工作集、分数计算、Top-k语义和 KV layout 仍不同。embedding 加速不能直接等同 Indexer 加速。[TPU v4原始论文](https://arxiv.org/abs/2304.01433)（访问日期｜2026-08-22）
- “1.77 PB 共享 HBM”描述的是 Pod 级可访问总量。Ironwood 两个 chiplet 各有独立 96 GB 内存空间，公开资料没有把它描述成单一平坦 cache。[TPU7x 双 chiplet 文档](https://docs.cloud.google.com/tpu/docs/tpu7x)（访问日期｜2026-08-22）
- ICI带宽能降低通信成本，却不自动产生 Local Top-k、Global Merge 或 Gather descriptor。拓扑只解决路，数据对象和算法仍要由软件与硬件共同定义。[TPU7x拓扑文档](https://docs.cloud.google.com/tpu/docs/tpu7x)（访问日期｜2026-08-22）
- Ironwood GA 不等于任何项目都能无预约使用，Google训练文档仍要求先获得 TPU7x access 并联系 account team。8t/8i则明确仍是 Coming soon。[TPU7x训练文档](https://docs.cloud.google.com/tpu/docs/tpu7x-training)（访问日期｜2026-08-22） [状态页](https://cloud.google.com/tpu?hl=en)（访问日期｜2026-08-22）

- **[厂商主张]**：Google 的峰值、相对性能、价格性能、性能/瓦或自家实测；不等于独立复现。
- **[独立基准]**：MLCommons/MLPerf 的公开基准框架或结果。若公开页面没有把具体 run 映射到 Ironwood，不能借此推出 Ironwood 分数。
- **[分析判断]**：基于已列事实对附件 Retrieval Plane 的映射；不是 Google 的产品承诺。

状态依据：Google Cloud 当前 TPU 产品页明确把 Ironwood 标为 “Generally available”，把 TPU 8t/8i 标为 “Coming soon”；release notes 记录 TPU7x 于 2025-11-24 Preview、2026-03-31 GA；Cloud TPU 文档当前列出的产品入口包括 Compute Engine、GKE 和 Vertex AI。[TPU 产品页](https://cloud.google.com/tpu?hl=en)（2026-09-01 访问）[Release notes](https://docs.cloud.google.com/tpu/docs/release-notes)（2026-09-01 访问）[Cloud TPU 文档](https://docs.cloud.google.com/tpu/docs)（2026-09-01 访问）

对上文旧时间段的口径补充：2025-11-06 的 GA 标题是产品宣布/即将可用，release notes 将 2025-11-24 记为 Preview、2026-03-31 记为 TPU7x GA。因此状态矩阵采用 release notes 的正式 GA 日期，同时保留 2025-11-06 的宣布和 2025-11-25 的 Cloud customers available 作为历史事件，不把它们混成同一个状态。

这里严格区分“产品可在云上申请/使用”与“芯片由 Google 对外出货”。Google 公开资料支持前者，不支持后者的独立日期、数量或客户交付清单。Anthropic 的“计划访问最多 100 万 TPU”属于客户/合作公告中的计划性容量表述，不能改写为已交付 100 万颗 Ironwood。[Ironwood GA 公告](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads)（2025-11-06）

Ironwood 芯片/拓扑依据：[TPU7x 架构文档](https://docs.cloud.google.com/tpu/docs/tpu7x)（2026-09-01 访问）；板级图片与 GA 说明依据：[Ironwood GA 公告](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads)（2026-09-01 访问）；GKE 云端可用依据：[About Ironwood in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpu-ironwood)（2026-09-01 访问）。

SparseCore 数量需保留两种口径：Cloud TPU7x 架构页按每 chiplet 2 个、整芯片 4 个物理单元说明；JAX Pallas 运行时表按 TPU 7x 暴露 `num_cores=2`，并标注 “2 logical / 4 physical cores”。本报告采用“4 physical cores、2 logical cores”并列写法，不把两者相加。[TPU7x 架构](https://docs.cloud.google.com/tpu/docs/tpu7x)（2026-09-01 访问）[JAX SparseCore 文档](https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)（2026-09-01 访问）

Google 当前产品页列出 JAX、TorchTPU/PyTorch、OpenXLA、MaxText、Tunix、vLLM；TPU7x 性能文档强调 FP8、sharding、通信优化、activation rematerialization、VMEM 调优和自定义 kernel。8t/8i 技术深潜另列 Pallas、Mosaic、XLA、Pathways、TPUDirect RDMA 和 TPU Direct Storage。[TPU 产品页](https://cloud.google.com/tpu?hl=en)（2026-09-01 访问）[Ironwood performance](https://docs.cloud.google.com/tpu/docs/ironwood-performance)（2026-09-01 访问）[8t/8i technical deep dive](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)（2026-09-01 访问）

Google Developers Blog 的 Qwen 3.5-397B Ironwood playbook 给出一个可复核但属于**厂商实测/厂商优化栈**的结果：在指定 8K/1K prefill-heavy、1K/8K decode-heavy、Concurrency 64 场景，报告 3,707 tokens/s/chip 和 677 tokens/s/chip，并说明 decode 受 HBM 带宽、VPU indexing stalls 与状态更新往返影响；其 RPA 示例把 KV page 从 16 调到 256，在 Concurrency-512 的 kernel step latency 中报告 428 µs 降至 283 µs。该材料非常适合说明 KV Gather/indexing 的真实软件瓶颈，但不能当作独立 benchmark 或泛化到所有模型。[Qwen 3.5-397B Ironwood playbook](https://developers.googleblog.com/systems-engineering-playbook-optimizing-qwen-35-397b-moe-on-ironwood-tpu7x/)（2026-09-01 访问）

截至本次打开的公开 MLCommons 新闻页，能够确认“Google 参与 MLPerf Training v6.0”和“该轮新增稀疏基准”，但页面本身没有把某个结果 run 明确标成 TPU7x/Ironwood。因此本报告不把 MLPerf v6.0 结果数字归因给 Ironwood。Trillium 的 MLPerf 4.1 引用仍是上一代产品的历史基准，不能替代 Ironwood 的独立结果。结论是：**Ironwood 有 Google 自家实测和开发者 playbook，有独立基准框架参与证据，但本次资料集没有完成 Ironwood-specific 的 MLCommons run 级归因。**

1. **最强已证实方向**：Ironwood 把 dense TensorCore 与面向不规则访问/通信的 SparseCore 放在同一系统；TPU7x 文档、JAX Pallas 和 Google 的 Ironwood playbook 共同证明，数据移动、索引、KV page 粒度和通信重叠是实际调优对象。
2. **最新路线的分化**：TPU 8t 继续强化训练、embedding、FP4、Virgo 和存储直达；TPU 8i 转向采样/服务、384 MB 片上 SRAM、CAE 和 Boardfly。两者仍是 Coming soon，不能把路线图写成已量产或可租用性能。
3. **独立性边界**：Google 自测数字可以用于“在明确 workload、软件栈、并行度下的厂商结果”；MLPerf 可用于独立方法与结果核验，但本次未将任何 v6.0 run 归因到 Ironwood。
4. **对附件的实际启发**：优先验证 `HBM bytes/token`、跨卡 `bytes/token`、索引/地址开销、Local/Global Top-k 的召回与精确性、KV page 粒度和尾延迟；不要用峰值 FLOPs、Pod 总带宽或 SparseCore embedding 数字替代这些指标。

## 关联证据与规格

本节保留与本对象相关的关联规格和生命周期证据；其中的卡、模块、服务器、机架、集群或云数据保持原产品层级，不能回填为芯片规格。

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

| 产品 | 产品层级 | 首次披露/发布 | 流片/量产 | 出货/客户部署 | 云端状态 | 窗口内定位 |
|---|---|---|---|---|---|---|
| TPU v5p | ASIC/芯片、Pod、Cloud TPU 服务 | 2023-12-06 发布 | **[未确认]** Google 未公开独立流片或量产日期 | **[官方事实]** 2023 年已向 Cloud customers 提供；曾用于 Salesforce 等客户训练 | **[官方事实]** Cloud TPU v5p 已 GA；当前不是最新主力 | 上一代性能基线 |
| TPU v6e / Trillium | ASIC/芯片、Pod、Cloud TPU 服务 | 2024-05-14 宣布；2024-12-11 GA | **[未确认]** | **[官方事实]** GA，Google 称用于训练 Gemini 2.0；独立出货数量未公开 | **[官方事实]** GA | Ironwood 的上一代可用产品 |
| TPU7x / Ironwood | 双 chiplet ASIC、三芯片板、4 芯片/VM、Pod、Cloud TPU 服务 | 2025-04-09 首次披露（早于窗口） | **[未确认]** 没有 Google 独立量产/流片日期 | **[官方事实]** 2025-11-24 Preview；2026-03-31 GA；Cloud 文档/GKE 已有可用配置 | **[官方事实]** 产品页为 Generally available；仍可能需要 quota/reservation/access | 窗口内主力可用产品 |
| TPU 8t | ASIC/专用训练系统、9,600 芯片 Superpod、Virgo scale-out、Cloud TPU 目标服务 | 2026-04-22 宣布 | **[未确认]** | **[未确认]** 没有公开出货或客户生产部署证据 | **[官方事实]** 产品页仍为 Coming soon；Google 仅称稍后/即将提供 | 窗口内最新训练路线 |
| TPU 8i | ASIC/专用推理/RL 系统、Boardfly Pod、Cloud TPU 目标服务 | 2026-04-22 宣布 | **[未确认]** | **[未确认]** 没有公开出货或客户生产部署证据 | **[官方事实]** 产品页仍为 Coming soon | 窗口内最新推理路线 |
| 更后续 TPU | 未见当前产品页列出 | **[未确认]** | **[未确认]** | **[未确认]** | **[未确认]** | 不以传闻或供应链消息补齐 |

| 层级 | Ironwood 已公开内容 | 不能推出的内容 |
|---|---|---|
| 芯片/ASIC | 1 个 TPU 芯片由 2 个 chiplet 组成；每 chiplet 有 1 TensorCore、2 SparseCore、96 GB HBM；因此物理盘点为 2 TensorCore、4 个物理 SparseCore、192 GB HBM | 不能把 Pod 的共享 HBM 当作单芯片平坦缓存；每 chiplet 有独立内存空间 |
| 板卡/液冷组件 | 官方图片说明 Ironwood board 上连接 3 个 TPU，并配液冷；这是板级封装/冷却证据 | 没有公开完整 BOM、板级供电、板卡内所有控制器或量产数量 |
| 主机/VM | 每台 TPU7x VM 包含 4 个芯片、224 vCPU、960 GB RAM、2 个 NUMA 节点；PCIe 连接 CPU host | 不能把 host RAM 当成 HBM；它是较慢的可选 offload 层 |
| Pod/系统 | 3D torus，最大 9,216 芯片；每轴双向 200 GB/s；产品页称 42.5 ExaFlops、液冷 | 42.5 ExaFlops 是 Pod 级 FP8 峰值口径，不是单芯片、板卡或云实例实测吞吐 |
| Cloud service | 通过 Cloud TPU、Compute Engine、GKE 等形态申请/管理；GKE 文档已列 Ironwood GA 区域/版本 | GA 不保证任意区域即时有容量，也不等于 8t/8i 已可租用 |

| 项目 | TPU7x / Ironwood | TPU 8t | TPU 8i | 证据边界 |
|---|---:|---:|---:|---|
| 单芯片峰值 | BF16 2,307 TFLOPs；FP8 4,614 TFLOPs | FP4 12.6 PFLOPs | FP4 10.1 PFLOPs | [官方事实] 文档/技术深潜表；峰值不是应用吞吐 |
| HBM | 192 GB；约 7.37–7.38 TB/s | 216 GB；6,528 GB/s | 288 GB；8,601 GB/s | [官方事实] 单芯片口径；GB 与 GiB 需按原表理解 |
| 片上存储 | VMEM；容量未在 TPU7x 主规格中给出 | 128 MB VMEM | 384 MB SRAM/VMEM | [官方事实] 8i 是 8t 的 3 倍片上 SRAM宣传口径 |
| 互联 | 3D torus；每轴双向 200 GB/s；双向总 ICI 约 1,200 GB/s | ICI 为 Ironwood 的 2 倍；Virgo 最高 4 倍 DCN 带宽 | 19.2 Tb/s 以及 Boardfly；宣传为通信密集场景最高 50% 延迟改善 | [官方事实]+[厂商主张] 绝对值、方向和系统边界不可混用 |
| Pod | 9,216 芯片；约 1.77 PB HBM 为系统总量 | 9,600 芯片；2 PB shared HBM；121 ExaFlops | 高层资料称最多 1,152 芯片；深潜拓扑又写 36 组、最多 1,024 active chips | 8i 的 1,152/1,024 是保留的官方口径冲突，不擅自消解 |
| 功耗 | 单芯片 TDP 未公开；“近 10 MW”是旧有 Pod 级口径 | 单芯片 TDP 未公开 | 单芯片 TDP 未公开 | [未确认] 不能由性能/瓦倒算真实 TDP |

| 动作 | 公开证据 | 截至本次能下的结论 |
|---|---|---|
| Search | SparseCore 面向稀疏、随机访问、低至中计算量；公开操作包括 gather/scatter、sorting、unique、counts、histograms、ragged operations | [分析判断] 可承载搜索前处理或索引相关 kernel；没有 Google 公开的 Q×K 全扫描/ANN Indexer 专用单元证据 |
| Reduce | TPU collective、SparseCore collectives；8i CAE明确面向 reduction/synchronization | [官方事实] 8i把 Reduce/同步作为专用方向；不等于 Global Top-k 已硬件化 |
| Top-k | JAX/硬件编程资料公开排序、规约和 indexed 操作 | [未确认] 没有公开“Local Top-k + Global Merge Top-k”专用指令/单元或端到端结果 |
| Address | Pallas SparseCore scalar subcore 可做 dynamic indexing、发起 DMA/stream；Ironwood 有多层 HBM/VMEM/host memory | [分析判断] 通用地址计算与 DMA 有编程基础；KV page translator、descriptor queue、物理地址安全检查未公开 |
| Route | TPU7x 3D torus、collective offload；8t Virgo；8i Boardfly、OCS、CAE | [官方事实]+[分析判断] 拓扑和 collective 路径是强项；没有 candidate-aware KV Route 证据 |
| Gather | SparseCore 明确支持 indexed fetch/send 和 gather/scatter；Qwen playbook 实际采用 Ragged Page Attention | [官方事实] 通用 indexed gather 和软件层 KV page gather 已有证据；硬件级 page-aware KV Gather DMA 未确认 |
| KV | TPU7x 有 192 GB HBM；Google 性能文档讨论 KV cache 适配；Qwen playbook 对非连续 KV page 做了调优；8i宣传 384 MB SRAM 可容纳更大 KV 工作集 | [官方事实]+[厂商主张] “更适合 KV”成立；不能写成 KV 全部片上、无需 HBM 或已达到某个 TTFT/TPOT |

## 直接来源

1. [Google TPU 产品页](https://cloud.google.com/tpu?hl=en)；核验日期：2026-09-05。
2. [首次宣布](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/)；核验日期：2026-09-05。
3. [GA公告](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads)；核验日期：2026-09-05。
4. [可用公告](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-google-tpu-things-to-know/)；核验日期：2026-09-05。
5. [第八代宣布](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)；核验日期：2026-09-05。
6. [TPU7x 官方架构文档](https://docs.cloud.google.com/tpu/docs/tpu7x)；核验日期：2026-09-05。
7. [Google 第八代架构深潜](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)；核验日期：2026-09-05。
8. [Cloud TPU 架构](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm)；核验日期：2026-09-05。
9. [JAX SparseCore 文档](https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)；核验日期：2026-09-05。
10. [Ironwood 性能文档](https://docs.cloud.google.com/tpu/docs/ironwood-performance)；核验日期：2026-09-05。
11. [TPU v4 原始论文](https://arxiv.org/abs/2304.01433)；核验日期：2026-09-05。
12. [TPU7x训练文档](https://docs.cloud.google.com/tpu/docs/tpu7x-training)；核验日期：2026-09-05。
13. [Release notes](https://docs.cloud.google.com/tpu/docs/release-notes)；核验日期：2026-09-05。
14. [Cloud TPU 文档](https://docs.cloud.google.com/tpu/docs)；核验日期：2026-09-05。
15. [About Ironwood in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpu-ironwood)；核验日期：2026-09-05。
16. [Qwen 3.5-397B Ironwood playbook](https://developers.googleblog.com/systems-engineering-playbook-optimizing-qwen-35-397b-moe-on-ironwood-tpu7x/)；核验日期：2026-09-05。
17. [MLCommons：MLPerf Training v6.0 Results](https://mlcommons.org/2026/06/mlperf-training-v6-0-results/)；核验日期：2026-09-05。

## 证据边界

- 芯片、封装、卡/模组、服务器/机架、集群、软件和云服务按来源原层级记录；系统、卡、模块或集群数据不自动回填为芯片规格。
- “宣布、流片/工程样片、送样、量产、出货、客户部署、云/实例可用、路线图、停产”分别判断；没有直接证据的阶段写为“公开资料未确认”。
- 官方发布、产品页或软件支持不能单独证明量产、出货或独立性能；厂商主张、独立验证和分析推断不混写。
- 本页是基于现有综合报告和直接来源的证据重排页；引用以文末直接 URL 为准，不再使用综合报告行号作为外部引用。
