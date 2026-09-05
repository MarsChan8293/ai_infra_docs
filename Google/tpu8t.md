# Google / 谷歌 — TPU 8t

- 拆分日期：2026-09-02
- 产品层级：路线图 TPU ASIC/训练系统
- 综合报告：[03-google-ironwood.md](./03-google-ironwood.md)
- 文件性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容逐行摘录综合报告，保留原报告中的状态、数字、证据等级和未知项。

> 第 5 行：> 资料访问日｜2026-09-01（本次复核）；原有 2026-08-22 访问标记保留在历史段落中
> 第 6 行：> 研究对象｜TPU7x/Ironwood，以及窗口内后续公开的 TPU 8t、TPU 8i
> 第 7 行：
> 第 15 行：
> 第 16 行：TPU 8t 与 TPU 8i 在 2026-04-22 于 Cloud Next 26 宣布，属于窗口内的新款。Google的第八代产品文章写的是两者将在今年稍后 GA，当前产品页仍标为 Coming soon。它们是“宣布”，不是“量产/可用”证据。本文纳入二者，是为了满足严格时间窗，并把 Ironwood 放在后续 Google TPU 的真实演进线上。截至 2026-08-22，官方 TPU 产品页未列出比 8t/8i 更新的 Google TPU。[第八代宣布](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)（访问日期｜2026-08-22） [当前状态页](https://cloud.google.com/tpu?hl=en)（访问日期｜2026-08-22）
> 第 17 行：
> 第 19 行：
> 第 20 行：| 项目 | TPU7x/Ironwood | TPU 8t | TPU 8i |
> 第 21 行：|---|---|---|---|
> 第 31 行：
> 第 32 行：Ironwood 数字来自 [TPU7x 官方架构文档](https://docs.cloud.google.com/tpu/docs/tpu7x)（访问日期｜2026-08-22）、[Ironwood 系统公告](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads)（访问日期｜2026-08-22）和[首次架构宣布](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/)（访问日期｜2026-08-22）。8t/8i 数字来自 [Google 第八代架构深潜](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)（访问日期｜2026-08-22）与[第八代宣布页](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)（访问日期｜2026-08-22）。这里的 PFLOPs、ExaFlops、性能/瓦都是官方峰值或宣传口径，不是本文测得的推理吞吐。
> 第 33 行：
> 第 37 行：
> 第 38 行：8i 的 Pod 规模也有冲突。Google 的高层宣布页写 1,152，技术深潜的 Boardfly 分解写 36 组、最多 1,024 active chips。本文在讨论具体拓扑、跳数和资源规划时采用更细的 1,024，保留 1,152 作为官方未解决的高层口径。[宣布页](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/)（访问日期｜2026-08-22） [技术深潜](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)（访问日期｜2026-08-22）
> 第 39 行：
> 第 54 行：
> 第 55 行：TPU 8t 把这条思路继续用于训练和 embedding-heavy workload，并加入原生 FP4、SparseCore data-dependent all-gather、TPUDirect RDMA 和 TPUDirect Storage。它更直接解决大规模数据输入与通信，仍然没有公开附件所需的 Indexer Top-k 证据。TPU 8i 则把问题移向采样和服务，384 MB 片上 SRAM 用于更大的 KV cache，CAE负责 Reduce 与同步，Boardfly用较少跳数服务 all-to-all。对附件来说，8i是最值得继续追踪的 Google 芯片，但公开资料仍没有 Indexed KV Gather、Local/Global Top-k 或 score materialization 消除的确认。[8t/8i 技术深潜](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)（访问日期｜2026-08-22）
> 第 56 行：
> 第 60 行：|---|---|---|---|
> 第 61 行：| Dense compute | Ironwood 2 个 TensorCore，BF16/FP8 峰值明确；8t原生 FP4 | 直接解决密集算力，不能替代 Retrieval Plane | [TPU7x文档](https://docs.cloud.google.com/tpu/docs/tpu7x)（访问日期｜2026-08-22） |
> 第 62 行：| Search | SparseCore 面向 embedding lookup，8i CAE面向 reduce/sync | 没有解决或证据不足，未公开 Indexer Search | [SparseCore文档](https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)（访问日期｜2026-08-22） |
> 第 65 行：| Move、Address | SparseCore支持 indexed gather/scatter、dynamic indexing、DMA；Ironwood有 VMEM/HBM层次 | 直接覆盖通用离散搬运，KV page/address descriptor 未公开 | [SparseCore文档](https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)（访问日期｜2026-08-22） |
> 第 66 行：| Route、跨卡通信 | Ironwood ICI、3D torus、collective offload；8i Boardfly、CAE和 OCS | 直接解决 collective 与网络路径，未解决候选级 KV 路由 | [Ironwood性能文档](https://docs.cloud.google.com/tpu/docs/ironwood-performance)（访问日期｜2026-08-22） [8i深潜](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)（访问日期｜2026-08-22） |
> 第 67 行：| Gather | JAX层面有 HBM indexed gather | 对通用 Gather 是直接帮助，对 page-aware KV Gather DMA 仍属证据不足 | [Gather/scatter文档](https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)（访问日期｜2026-08-22） |
> 第 87 行：
> 第 88 行：- 官方峰值 FLOPs、Pod 总 ExaFlops、性能/瓦和性能/美元都依赖精度、并行度、软件栈和系统边界。它们不能推出 Indexer 的端到端 TPOT，也不能推出 Tokens/J。[8t/8i技术深潜](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)（访问日期｜2026-08-22）
> 第 89 行：- SparseCore 的 embedding lookup 与附件 Indexer 有共同的随机访问特征，工作集、分数计算、Top-k语义和 KV layout 仍不同。embedding 加速不能直接等同 Indexer 加速。[TPU v4原始论文](https://arxiv.org/abs/2304.01433)（访问日期｜2026-08-22）
> 第 91 行：- ICI带宽能降低通信成本，却不自动产生 Local Top-k、Global Merge 或 Gather descriptor。拓扑只解决路，数据对象和算法仍要由软件与硬件共同定义。[TPU7x拓扑文档](https://docs.cloud.google.com/tpu/docs/tpu7x)（访问日期｜2026-08-22）
> 第 92 行：- Ironwood GA 不等于任何项目都能无预约使用，Google训练文档仍要求先获得 TPU7x access 并联系 account team。8t/8i则明确仍是 Coming soon。[TPU7x训练文档](https://docs.cloud.google.com/tpu/docs/tpu7x-training)（访问日期｜2026-08-22） [状态页](https://cloud.google.com/tpu?hl=en)（访问日期｜2026-08-22）
> 第 93 行：
> 第 105 行：
> 第 106 行：1. [Google Cloud TPU 产品页，含 Ironwood GA 与 TPU 8t/8i Coming soon 状态，访问日期 2026-08-22](https://cloud.google.com/tpu?hl=en)
> 第 107 行：2. [TPU7x/Ironwood 官方架构与规格文档，访问日期 2026-08-22](https://docs.cloud.google.com/tpu/docs/tpu7x)
> 第 110 行：5. [Google 第八代 TPU 宣布，2026-04-22，访问日期 2026-08-22](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)
> 第 111 行：6. [TPU 8t/8i architecture deep dive，含 SparseCore、CAE、Boardfly 与芯片表，2026-04-22，访问日期 2026-08-22](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)
> 第 112 行：7. [JAX Pallas SparseCore 开发文档，含 dynamic indexing、DMA、gather/scatter，访问日期 2026-08-22](https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)
> 第 131 行：| TPU7x / Ironwood | 双 chiplet ASIC、三芯片板、4 芯片/VM、Pod、Cloud TPU 服务 | 2025-04-09 首次披露（早于窗口） | **[未确认]** 没有 Google 独立量产/流片日期 | **[官方事实]** 2025-11-24 Preview；2026-03-31 GA；Cloud 文档/GKE 已有可用配置 | **[官方事实]** 产品页为 Generally available；仍可能需要 quota/reservation/access | 窗口内主力可用产品 |
> 第 132 行：| TPU 8t | ASIC/专用训练系统、9,600 芯片 Superpod、Virgo scale-out、Cloud TPU 目标服务 | 2026-04-22 宣布 | **[未确认]** | **[未确认]** 没有公开出货或客户生产部署证据 | **[官方事实]** 产品页仍为 Coming soon；Google 仅称稍后/即将提供 | 窗口内最新训练路线 |
> 第 133 行：| TPU 8i | ASIC/专用推理/RL 系统、Boardfly Pod、Cloud TPU 目标服务 | 2026-04-22 宣布 | **[未确认]** | **[未确认]** 没有公开出货或客户生产部署证据 | **[官方事实]** 产品页仍为 Coming soon | 窗口内最新推理路线 |
> 第 135 行：
> 第 136 行：状态依据：Google Cloud 当前 TPU 产品页明确把 Ironwood 标为 “Generally available”，把 TPU 8t/8i 标为 “Coming soon”；release notes 记录 TPU7x 于 2025-11-24 Preview、2026-03-31 GA；Cloud TPU 文档当前列出的产品入口包括 Compute Engine、GKE 和 Vertex AI。[TPU 产品页](https://cloud.google.com/tpu?hl=en)（2026-09-01 访问）[Release notes](https://docs.cloud.google.com/tpu/docs/release-notes)（2026-09-01 访问）[Cloud TPU 文档](https://docs.cloud.google.com/tpu/docs)（2026-09-01 访问）
> 第 137 行：
> 第 149 行：| Pod/系统 | 3D torus，最大 9,216 芯片；每轴双向 200 GB/s；产品页称 42.5 ExaFlops、液冷 | 42.5 ExaFlops 是 Pod 级 FP8 峰值口径，不是单芯片、板卡或云实例实测吞吐 |
> 第 150 行：| Cloud service | 通过 Cloud TPU、Compute Engine、GKE 等形态申请/管理；GKE 文档已列 Ironwood GA 区域/版本 | GA 不保证任意区域即时有容量，也不等于 8t/8i 已可租用 |
> 第 151 行：
> 第 155 行：
> 第 156 行：| 项目 | TPU7x / Ironwood | TPU 8t | TPU 8i | 证据边界 |
> 第 157 行：|---|---:|---:|---:|---|
> 第 159 行：| HBM | 192 GB；约 7.37–7.38 TB/s | 216 GB；6,528 GB/s | 288 GB；8,601 GB/s | [官方事实] 单芯片口径；GB 与 GiB 需按原表理解 |
> 第 160 行：| 片上存储 | VMEM；容量未在 TPU7x 主规格中给出 | 128 MB VMEM | 384 MB SRAM/VMEM | [官方事实] 8i 是 8t 的 3 倍片上 SRAM宣传口径 |
> 第 161 行：| 互联 | 3D torus；每轴双向 200 GB/s；双向总 ICI 约 1,200 GB/s | ICI 为 Ironwood 的 2 倍；Virgo 最高 4 倍 DCN 带宽 | 19.2 Tb/s 以及 Boardfly；宣传为通信密集场景最高 50% 延迟改善 | [官方事实]+[厂商主张] 绝对值、方向和系统边界不可混用 |
> 第 168 行：
> 第 169 行：Google 当前产品页列出 JAX、TorchTPU/PyTorch、OpenXLA、MaxText、Tunix、vLLM；TPU7x 性能文档强调 FP8、sharding、通信优化、activation rematerialization、VMEM 调优和自定义 kernel。8t/8i 技术深潜另列 Pallas、Mosaic、XLA、Pathways、TPUDirect RDMA 和 TPU Direct Storage。[TPU 产品页](https://cloud.google.com/tpu?hl=en)（2026-09-01 访问）[Ironwood performance](https://docs.cloud.google.com/tpu/docs/ironwood-performance)（2026-09-01 访问）[8t/8i technical deep dive](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)（2026-09-01 访问）
> 第 170 行：
> 第 186 行：| Address | Pallas SparseCore scalar subcore 可做 dynamic indexing、发起 DMA/stream；Ironwood 有多层 HBM/VMEM/host memory | [分析判断] 通用地址计算与 DMA 有编程基础；KV page translator、descriptor queue、物理地址安全检查未公开 |
> 第 187 行：| Route | TPU7x 3D torus、collective offload；8t Virgo；8i Boardfly、OCS、CAE | [官方事实]+[分析判断] 拓扑和 collective 路径是强项；没有 candidate-aware KV Route 证据 |
> 第 188 行：| Gather | SparseCore 明确支持 indexed fetch/send 和 gather/scatter；Qwen playbook 实际采用 Ragged Page Attention | [官方事实] 通用 indexed gather 和软件层 KV page gather 已有证据；硬件级 page-aware KV Gather DMA 未确认 |
> 第 195 行：1. **最强已证实方向**：Ironwood 把 dense TensorCore 与面向不规则访问/通信的 SparseCore 放在同一系统；TPU7x 文档、JAX Pallas 和 Google 的 Ironwood playbook 共同证明，数据移动、索引、KV page 粒度和通信重叠是实际调优对象。
> 第 196 行：2. **最新路线的分化**：TPU 8t 继续强化训练、embedding、FP4、Virgo 和存储直达；TPU 8i 转向采样/服务、384 MB 片上 SRAM、CAE 和 Boardfly。两者仍是 Coming soon，不能把路线图写成已量产或可租用性能。
> 第 197 行：3. **独立性边界**：Google 自测数字可以用于“在明确 workload、软件栈、并行度下的厂商结果”；MLPerf 可用于独立方法与结果核验，但本次未将任何 v6.0 run 归因到 Ironwood。
> 第 206 行：5. [Ironwood GA 公告](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads)
> 第 207 行：6. [TPU 8t/8i 技术深潜](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)
> 第 208 行：7. [Google 第八代 TPU 宣布页](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)

## 直接来源链接

1. <https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)（访问日期｜2026-08-22）>
2. <https://cloud.google.com/tpu?hl=en)（访问日期｜2026-08-22）>
3. <https://docs.cloud.google.com/tpu/docs/tpu7x)（访问日期｜2026-08-22）、[Ironwood>
4. <https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads)（访问日期｜2026-08-22）和[首次架构宣布](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/)（访问日期｜2026-08-22）。8t/8i>
5. <https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)（访问日期｜2026-08-22）与[第八代宣布页](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)（访问日期｜2026-08-22）。这里的>
6. <https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/)（访问日期｜2026-08-22）>
7. <https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)（访问日期｜2026-08-22）>
8. <https://docs.cloud.google.com/tpu/docs/tpu7x)（访问日期｜2026-08-22）>
9. <https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)（访问日期｜2026-08-22）>
10. <https://docs.cloud.google.com/tpu/docs/ironwood-performance)（访问日期｜2026-08-22）>
11. <https://arxiv.org/abs/2304.01433)（访问日期｜2026-08-22）>
12. <https://docs.cloud.google.com/tpu/docs/tpu7x-training)（访问日期｜2026-08-22）>
13. <https://cloud.google.com/tpu?hl=en)>
14. <https://docs.cloud.google.com/tpu/docs/tpu7x)>
15. <https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)>
16. <https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)>
17. <https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)>
18. <https://cloud.google.com/tpu?hl=en)（2026-09-01>
19. <https://docs.cloud.google.com/tpu/docs/release-notes)（2026-09-01>
20. <https://docs.cloud.google.com/tpu/docs)（2026-09-01>
21. <https://docs.cloud.google.com/tpu/docs/ironwood-performance)（2026-09-01>
22. <https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)（2026-09-01>
23. <https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads)>

## 证据边界

- 这是资料重排页，不是重新发布或重新核验的产品公告。
- “发布、流片、送样、量产、出货、客户部署、云端可用、路线图、停产”等状态只在综合报告明确写出时保留；缺失项仍为“公开资料未确认”。
- 若摘录同时出现芯片、板卡、服务器、机架或云服务，均按原报告层级保留，并以“产品层级”字段提醒，不做跨层级推导。

## 关联表格原文（完整表格）

以下表格块来自综合报告中与本拆分项命中的表格，完整保留表头、状态列和规格列。

> 来源综合报告第 20-30 行：
> 第 20 行：| 项目 | TPU7x/Ironwood | TPU 8t | TPU 8i |
> 第 21 行：|---|---|---|---|
> 第 22 行：| 制程 | 公开资料未确认 | 公开资料未确认 | 公开资料未确认 |
> 第 23 行：| 单芯片密集计算 | 2 个 TensorCore；BF16 峰值 2,307 TFLOPs，FP8 峰值 4,614 TFLOPs | 原生 FP4；官方技术表列峰值 FP4 12.6 PFLOPs | 2 个 TensorCore；官方技术表列峰值 FP4 10.1 PFLOPs |
> 第 24 行：| SparseCore 或专用单元 | Cloud TPU 架构页写 4 个 SparseCore | 有 SparseCore，数量公开资料未确认 | 1 个 CAE，官方称替代 Ironwood 的 4 个 SparseCore |
> 第 25 行：| HBM | 每芯片 192 GiB；7,380 GB/s，文档正文约写 7.37 TB/s | 216 GB；6,528 GB/s | 288 GB；8,601 GB/s |
> 第 26 行：| 片上 SRAM 或 VMEM | VMEM 是高带宽片上 scratchpad，容量未给出 | 128 MB VMEM | 384 MB SRAM/VMEM，约为上一代 3 倍 |
> 第 27 行：| 芯片内互联 | 双向 ICI 1,200 GB/s；3D torus 每轴 200 GB/s | ICI scale-up 带宽为 Ironwood 的 2 倍，绝对单芯片值未公开 | 宣传口径为 19.2 Tb/s；Boardfly，最大跳数公开为 7 |
> 第 28 行：| Pod 规模 | 9,216 芯片；官方另称约 1.77 PB HBM、近 10 MW 系统规模 | 9,600 芯片；2 PB 共享 HBM；121 ExaFlops 系统宣传值 | 官方宣布页写 1,152 芯片；技术深潜的详细拓扑写最多 1,024 active chips |
> 第 29 行：| 功耗 | 单芯片 TDP 未公开；近 10 MW 是大 Pod 级口径 | 单芯片 TDP 未公开；官方称较 Ironwood 最多 2 倍性能/瓦 | 单芯片 TDP 未公开；官方称较 Ironwood 最多 2 倍性能/瓦 |
> 第 30 行：| 主要状态 | GA，当前产品页标为 Generally available | 宣布，Coming soon | 宣布，Coming soon |

> 来源综合报告第 59-68 行：
> 第 59 行：| 附件动作或指标 | 公开能力映射 | 判断 | 证据 |
> 第 60 行：|---|---|---|---|
> 第 61 行：| Dense compute | Ironwood 2 个 TensorCore，BF16/FP8 峰值明确；8t原生 FP4 | 直接解决密集算力，不能替代 Retrieval Plane | [TPU7x文档](https://docs.cloud.google.com/tpu/docs/tpu7x)（访问日期｜2026-08-22） |
> 第 62 行：| Search | SparseCore 面向 embedding lookup，8i CAE面向 reduce/sync | 没有解决或证据不足，未公开 Indexer Search | [SparseCore文档](https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)（访问日期｜2026-08-22） |
> 第 63 行：| Select、Top-k | 公开了排序、计数、规约相关能力，但没有专用 Top-k 或 Merge Top-k 说明 | 间接帮助，Local/Global Top-k 没有证据 | [SparseCore文档](https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)（访问日期｜2026-08-22） |
> 第 64 行：| score materialization | HBM、VMEM、8i SRAM有利于保存中间数据；资料未承诺流式 score | 间接帮助，是否消除物化未确认 | [Ironwood性能文档](https://docs.cloud.google.com/tpu/docs/ironwood-performance)（访问日期｜2026-08-22） |
> 第 65 行：| Move、Address | SparseCore支持 indexed gather/scatter、dynamic indexing、DMA；Ironwood有 VMEM/HBM层次 | 直接覆盖通用离散搬运，KV page/address descriptor 未公开 | [SparseCore文档](https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)（访问日期｜2026-08-22） |
> 第 66 行：| Route、跨卡通信 | Ironwood ICI、3D torus、collective offload；8i Boardfly、CAE和 OCS | 直接解决 collective 与网络路径，未解决候选级 KV 路由 | [Ironwood性能文档](https://docs.cloud.google.com/tpu/docs/ironwood-performance)（访问日期｜2026-08-22） [8i深潜](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive)（访问日期｜2026-08-22） |
> 第 67 行：| Gather | JAX层面有 HBM indexed gather | 对通用 Gather 是直接帮助，对 page-aware KV Gather DMA 仍属证据不足 | [Gather/scatter文档](https://docs.jax.dev/en/latest/pallas/tpu/sparsecore.html)（访问日期｜2026-08-22） |
> 第 68 行：| TPOT、TTFT、Tokens/J | Google给出峰值、性能/瓦、性能/美元和低延迟定位 | 没有公开附件同口径的 Indexer TPOT、TTFT、Tokens/J 或 J/token | [Google TPU产品页](https://cloud.google.com/tpu?hl=en)（访问日期｜2026-08-22） |

> 来源综合报告第 127-134 行：
> 第 127 行：| 产品 | 产品层级 | 首次披露/发布 | 流片/量产 | 出货/客户部署 | 云端状态 | 窗口内定位 |
> 第 128 行：|---|---|---|---|---|---|---|
> 第 129 行：| TPU v5p | ASIC/芯片、Pod、Cloud TPU 服务 | 2023-12-06 发布 | **[未确认]** Google 未公开独立流片或量产日期 | **[官方事实]** 2023 年已向 Cloud customers 提供；曾用于 Salesforce 等客户训练 | **[官方事实]** Cloud TPU v5p 已 GA；当前不是最新主力 | 上一代性能基线 |
> 第 130 行：| TPU v6e / Trillium | ASIC/芯片、Pod、Cloud TPU 服务 | 2024-05-14 宣布；2024-12-11 GA | **[未确认]** | **[官方事实]** GA，Google 称用于训练 Gemini 2.0；独立出货数量未公开 | **[官方事实]** GA | Ironwood 的上一代可用产品 |
> 第 131 行：| TPU7x / Ironwood | 双 chiplet ASIC、三芯片板、4 芯片/VM、Pod、Cloud TPU 服务 | 2025-04-09 首次披露（早于窗口） | **[未确认]** 没有 Google 独立量产/流片日期 | **[官方事实]** 2025-11-24 Preview；2026-03-31 GA；Cloud 文档/GKE 已有可用配置 | **[官方事实]** 产品页为 Generally available；仍可能需要 quota/reservation/access | 窗口内主力可用产品 |
> 第 132 行：| TPU 8t | ASIC/专用训练系统、9,600 芯片 Superpod、Virgo scale-out、Cloud TPU 目标服务 | 2026-04-22 宣布 | **[未确认]** | **[未确认]** 没有公开出货或客户生产部署证据 | **[官方事实]** 产品页仍为 Coming soon；Google 仅称稍后/即将提供 | 窗口内最新训练路线 |
> 第 133 行：| TPU 8i | ASIC/专用推理/RL 系统、Boardfly Pod、Cloud TPU 目标服务 | 2026-04-22 宣布 | **[未确认]** | **[未确认]** 没有公开出货或客户生产部署证据 | **[官方事实]** 产品页仍为 Coming soon | 窗口内最新推理路线 |
> 第 134 行：| 更后续 TPU | 未见当前产品页列出 | **[未确认]** | **[未确认]** | **[未确认]** | **[未确认]** | 不以传闻或供应链消息补齐 |

> 来源综合报告第 144-150 行：
> 第 144 行：| 层级 | Ironwood 已公开内容 | 不能推出的内容 |
> 第 145 行：|---|---|---|
> 第 146 行：| 芯片/ASIC | 1 个 TPU 芯片由 2 个 chiplet 组成；每 chiplet 有 1 TensorCore、2 SparseCore、96 GB HBM；因此物理盘点为 2 TensorCore、4 个物理 SparseCore、192 GB HBM | 不能把 Pod 的共享 HBM 当作单芯片平坦缓存；每 chiplet 有独立内存空间 |
> 第 147 行：| 板卡/液冷组件 | 官方图片说明 Ironwood board 上连接 3 个 TPU，并配液冷；这是板级封装/冷却证据 | 没有公开完整 BOM、板级供电、板卡内所有控制器或量产数量 |
> 第 148 行：| 主机/VM | 每台 TPU7x VM 包含 4 个芯片、224 vCPU、960 GB RAM、2 个 NUMA 节点；PCIe 连接 CPU host | 不能把 host RAM 当成 HBM；它是较慢的可选 offload 层 |
> 第 149 行：| Pod/系统 | 3D torus，最大 9,216 芯片；每轴双向 200 GB/s；产品页称 42.5 ExaFlops、液冷 | 42.5 ExaFlops 是 Pod 级 FP8 峰值口径，不是单芯片、板卡或云实例实测吞吐 |
> 第 150 行：| Cloud service | 通过 Cloud TPU、Compute Engine、GKE 等形态申请/管理；GKE 文档已列 Ironwood GA 区域/版本 | GA 不保证任意区域即时有容量，也不等于 8t/8i 已可租用 |

> 来源综合报告第 156-163 行：
> 第 156 行：| 项目 | TPU7x / Ironwood | TPU 8t | TPU 8i | 证据边界 |
> 第 157 行：|---|---:|---:|---:|---|
> 第 158 行：| 单芯片峰值 | BF16 2,307 TFLOPs；FP8 4,614 TFLOPs | FP4 12.6 PFLOPs | FP4 10.1 PFLOPs | [官方事实] 文档/技术深潜表；峰值不是应用吞吐 |
> 第 159 行：| HBM | 192 GB；约 7.37–7.38 TB/s | 216 GB；6,528 GB/s | 288 GB；8,601 GB/s | [官方事实] 单芯片口径；GB 与 GiB 需按原表理解 |
> 第 160 行：| 片上存储 | VMEM；容量未在 TPU7x 主规格中给出 | 128 MB VMEM | 384 MB SRAM/VMEM | [官方事实] 8i 是 8t 的 3 倍片上 SRAM宣传口径 |
> 第 161 行：| 互联 | 3D torus；每轴双向 200 GB/s；双向总 ICI 约 1,200 GB/s | ICI 为 Ironwood 的 2 倍；Virgo 最高 4 倍 DCN 带宽 | 19.2 Tb/s 以及 Boardfly；宣传为通信密集场景最高 50% 延迟改善 | [官方事实]+[厂商主张] 绝对值、方向和系统边界不可混用 |
> 第 162 行：| Pod | 9,216 芯片；约 1.77 PB HBM 为系统总量 | 9,600 芯片；2 PB shared HBM；121 ExaFlops | 高层资料称最多 1,152 芯片；深潜拓扑又写 36 组、最多 1,024 active chips | 8i 的 1,152/1,024 是保留的官方口径冲突，不擅自消解 |
> 第 163 行：| 功耗 | 单芯片 TDP 未公开；“近 10 MW”是旧有 Pod 级口径 | 单芯片 TDP 未公开 | 单芯片 TDP 未公开 | [未确认] 不能由性能/瓦倒算真实 TDP |

> 来源综合报告第 181-189 行：
> 第 181 行：| 动作 | 公开证据 | 截至本次能下的结论 |
> 第 182 行：|---|---|---|
> 第 183 行：| Search | SparseCore 面向稀疏、随机访问、低至中计算量；公开操作包括 gather/scatter、sorting、unique、counts、histograms、ragged operations | [分析判断] 可承载搜索前处理或索引相关 kernel；没有 Google 公开的 Q×K 全扫描/ANN Indexer 专用单元证据 |
> 第 184 行：| Reduce | TPU collective、SparseCore collectives；8i CAE明确面向 reduction/synchronization | [官方事实] 8i把 Reduce/同步作为专用方向；不等于 Global Top-k 已硬件化 |
> 第 185 行：| Top-k | JAX/硬件编程资料公开排序、规约和 indexed 操作 | [未确认] 没有公开“Local Top-k + Global Merge Top-k”专用指令/单元或端到端结果 |
> 第 186 行：| Address | Pallas SparseCore scalar subcore 可做 dynamic indexing、发起 DMA/stream；Ironwood 有多层 HBM/VMEM/host memory | [分析判断] 通用地址计算与 DMA 有编程基础；KV page translator、descriptor queue、物理地址安全检查未公开 |
> 第 187 行：| Route | TPU7x 3D torus、collective offload；8t Virgo；8i Boardfly、OCS、CAE | [官方事实]+[分析判断] 拓扑和 collective 路径是强项；没有 candidate-aware KV Route 证据 |
> 第 188 行：| Gather | SparseCore 明确支持 indexed fetch/send 和 gather/scatter；Qwen playbook 实际采用 Ragged Page Attention | [官方事实] 通用 indexed gather 和软件层 KV page gather 已有证据；硬件级 page-aware KV Gather DMA 未确认 |
> 第 189 行：| KV | TPU7x 有 192 GB HBM；Google 性能文档讨论 KV cache 适配；Qwen playbook 对非连续 KV page 做了调优；8i宣传 384 MB SRAM 可容纳更大 KV 工作集 | [官方事实]+[厂商主张] “更适合 KV”成立；不能写成 KV 全部片上、无需 HBM 或已达到某个 TTFT/TPOT |
