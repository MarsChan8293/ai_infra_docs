# 厂商与芯片：2025-06 之后最新款——NVIDIA Rubin GPU

> 研究对象：NVIDIA Rubin GPU；Vera Rubin 是系统边界，Rubin CPX 是同代长上下文变体。研究窗口：2025-07-01 至 2026-08-22。原始资料访问日期：2026-08-22；本次结构核验：2026-09-05。Hot Chips 2026 议程只作为会议证据入口，未据此新增 Rubin 规格。

## 一句话结论

Rubin 最值得研究的地方，不是把 Tensor Core 再堆大，而是把 **HBM4、TMA 数据搬运、依赖触发和 NVLink 6** 组合成一条更紧的推理执行路径。它确实改善了密集计算、规则张量搬运、跨卡通信和 kernel 间等待；但公开资料没有证明它已经提供附件设想的独立 **Search/Indexer、精确 Local/Global Top-k、page-aware Indexed Gather DMA**。因此，它是“更强的推理 GPU + 系统协同”，还不是完整的 Retrieval GPU。[架构深读](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)；[NVLink 6](https://www.nvidia.com/en-gb/data-center/nvlink/)（访问：2026-08-22）。

## 目标芯片与时间状态

| 对象 | 窗口内状态 | 芯片与系统边界 |
|---|---|---|
| **Rubin GPU** | 2026-01-05 宣布 Rubin 平台；2026-03-16 NVIDIA 称平台七颗芯片进入 full production；2026-05-31 称 Vera Rubin 正在爬产，2026-07-21 官方技术文公开架构细节。产品处于量产爬坡、合作伙伴部署/出货阶段；单卡直接购买状态公开资料未确认。来源：[宣布](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer)；[量产](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform)；[爬产](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Vera-Rubin-Ramps-Into-Full-Production-to-Power-Agentic-AI-Factories-Worldwide/default.aspx)；[合作伙伴部署](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)（均访问：2026-08-22）。 | 一颗 Rubin GPU：288 GB HBM4。Vera Rubin Superchip 是 2 颗 GPU + 1 颗 Vera CPU；NVL72 是 72 颗 GPU + 36 颗 CPU 的机架系统，不能把后两者规格写成单芯片规格。 |
| **Rubin CPX** | 2025-09-09 宣布，官方状态为“预计 2026 年底可用”，截至截止日仍不是已可获得产品。来源：[NVIDIA 新闻稿](https://nvidianews.nvidia.com/news/nvidia-unveils-rubin-cpx-a-new-class-of-gpu-designed-for-massive-context-inference)（访问：2026-08-22）。 | 这是面向百万 token 上下文的独立 NVIDIA GPU，采用 128 GB GDDR7、最高 30 PFLOPS NVFP4；不能把 CPX 的 GDDR7 规格与 Rubin GPU 的 HBM4 混写。 |

**跨边界注记。** Groq 3 LPX 在 2026-03-16 被 NVIDIA 纳入 Vera Rubin 平台，是独立的低延迟推理加速器机架；本文只用它说明平台边界，不把其 SRAM、带宽或性能写成 Rubin GPU 规格。[官方公告](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform)（访问：2026-08-22）。

**为什么选 Rubin。** 在指定时间窗内，Rubin 是 NVIDIA 正式宣布并进入量产爬坡的最新数据中心 GPU 平台；CPX 更新近、问题相关性强，但仍是预期产品。因此主对象是 Rubin GPU，CPX 只用于说明 NVIDIA 对长上下文的另一条产品边界。当前核验到 2026-08-22 的 [NVIDIA 数据中心产品页](https://www.nvidia.com/en-us/data-center/products/)、官方新闻和技术文中，未发现比 Rubin/CPX 更新且已宣布或可用的 NVIDIA 数据中心 AI GPU（这是本次核验范围内的结论）。

## 核心规格表

| 项目 | Rubin GPU 公开规格 | 边界与状态 |
|---|---|---|
| 制程 | **公开资料未确认** | NVIDIA 产品页、架构文和 datasheet 没有给出制程节点；不能用传闻补齐。来源：[产品页](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)（访问：2026-08-22）。 |
| 计算单元 | 3360 亿晶体管、224 SM、896 Tensor Core；第五代 Tensor Core、第三代 Transformer Engine。来源：[架构文](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)（访问：2026-08-22）。 | 这是 GPU 层信息；GPC、集中式 L2、GigaThread Engine、MIG Control 的容量或细节未完整公开。 |
| 数值格式 | NVFP4 推理最高 50 PFLOPS（官方脚注明确为 sparse specification）；NVFP4 训练 35 PFLOPS 为 dense；另列 FP8/FP6、FP16/BF16、TF32、FP32、FP64。支持矩阵 B 的 3-bit lookup-table 格式。来源：[官方规格](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)；[datasheet](https://dam-cdn.nvd.orangelogic.com/AssetLink/v5rf2icnf86o26e464tf6djn23r8ibhe.pdf)（访问：2026-08-22）。 | PFLOPS 是峰值/规格口径，不是 Indexer 或端到端推理速度。 |
| 内存 | GPU：288 GB HBM4，最高 22 TB/s；HBM4 是封装旁高带宽内存，不等于片上 SRAM。来源：[官方规格](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)（访问：2026-08-22）。 | 片上 L2/SRAM 容量：公开资料未确认。Superchip 的 1.5 TB LPDDR5X 和 1.8 TB/s NVLink-C2C 属于 CPU-GPU 系统边界。 |
| 互联 | NVLink 6：每 GPU 3.6 TB/s 双向 GPU-GPU 带宽；x16 PCIe Gen6 最高 256 GB/s 主机连接。NVL72 的 NVLink 域为 260 TB/s、72 GPU all-to-all。来源：[NVLink 页](https://www.nvidia.com/en-gb/data-center/nvlink/)；[架构文](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)（访问：2026-08-22）。 | 3.6 TB/s 是每 GPU 的互联带宽，260 TB/s 是 NVL72 系统值；二者不是冲突。 |
| 功耗 | **单 GPU TDP/功耗公开资料未确认** | datasheet 在 NVL4 对比中出现 1,800 W/GPU 的测试假设，但那是系统性能比较口径，不应当作 Rubin 单卡 TDP。来源：[datasheet](https://dam-cdn.nvd.orangelogic.com/AssetLink/v5rf2icnf86o26e464tf6djn23r8ibhe.pdf)（访问：2026-08-22）。 |

## ELI5 核心特性：为什么它和推理有关

原始 ELI5 附件（当前目录未提供）把推理 GPU 拆成四个难题：密集计算、动态检索/Indexer、Top-k/Reduce、离散 KV Gather 与跨卡通信。Rubin 的回答是：先把“算、搬、等、跨卡传”做得更顺，但没有公开一个专门的 Retrieval Plane。

**类比。** Tensor Core 像大工厂，HBM4 像工厂旁的大仓库；TMA 像能按运输单把规则货箱送到工位的自动传送带；TMA 的 inline descriptor update 像同一张运输单可以在运行时改货物起点和步长，不必为每个专家重新制作一张单。生产者 kernel 做完一个 tile，消费者 kernel 可在所需输入到达后更早启动，像收货线按托盘到达开工，而不是等整车到齐。NVLink 6 则是机架内高速公路，SHARP 可在网络中做部分 collective reduction。来源：[Rubin 架构深读](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)；[NVLink 6](https://www.nvidia.com/en-gb/data-center/nvlink/)（访问：2026-08-22）。

**技术层。** Rubin 公布了 TMA 的复杂布局搬运、运行时 descriptor 的 pointer/stride 更新、tile-level dependent-kernel triggering、device-initiated NVLink 的 counted writes，以及 attention 中把 dense QKᵀ 中间结果压成结构化 2:4 稀疏格式后再做 softmax/后续 GEMM。这些能力减少元数据、等待或中间结果写入的压力，属于对数据路径的硬件—软件协同优化。[官方解释](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)（访问：2026-08-22）。

**类比边界。** “运输单”仍主要描述规则张量的布局、指针和步长，不等于按任意 index/page table 读取离散 KV；2:4 activation sparsity 也不等于动态精确 Top-k。官方资料没有确认 Indexed Gather DMA、KV Page Translator、Indexer 专用 SRAM 或 ANN 搜索引擎。后一句是基于公开规格缺失的证据边界，不是断言硬件绝对没有这些内部实现。

## 它解决的系统问题

| 附件问题 | 直接解决 | 间接帮助 | 没有解决/证据不足 |
|---|---|---|---|
| **Search / Indexer** | 无公开的专用 Search/Indexer 单元。 | HBM4 带宽和 TMA 可让 Key/激活读取更快。 | 没有公开检索索引、候选生成或动态 ANN 机制；这是对[架构公开范围](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)和[规格页](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)的证据边界判断（访问：2026-08-22）。 |
| **Select、score materialization** | 2:4 压缩可减少特定 attention 中间分数的写入和后续处理。 | 更快 exponential/softmax 和 NVFP4 压缩有助于 attention。 | 官方流程仍先做 dense QKᵀ；不是附件 Exact Mode 的“扫描时 Local Top-k、不写回完整 score”。[来源](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)（访问：2026-08-22）。 |
| **Move / Address** | TMA 对规则张量搬运是直接能力；inline descriptor 可运行时更新地址相关字段。 | 这为 Gather descriptor、异步流水提供可借鉴接口。 | 没有确认 page-aware indexed gather、物理地址翻译或 KV page map；官方只公开了 TMA/descriptor 机制。[架构文](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)（访问：2026-08-22）。 |
| **Route** | MoE expert 权重/Token 的跨位置搬运和 NVLink 通信得到针对性优化。 | counted writes 可减少 GPU-GPU 完成同步开销。 | 这不是附件意义上的 candidate route 或 KV route。 |
| **Local/Global Top-k、Reduce** | NVLink 6 Switch 的 in-network collective reduction 对 Reduce 是直接帮助。 | 可把候选集合放到高速 all-to-all 上做合并。 | SHARP/reduction 不等于 Top-k；没有公开 Local Top-k、Global Merge Top-k 原语。[NVLink 6 说明](https://www.nvidia.com/en-gb/data-center/nvlink/)（访问：2026-08-22）。 |
| **离散 KV Gather / 跨卡通信** | 跨卡通信有直接硬件支持：3.6 TB/s/GPU、NVL72 260 TB/s、counted writes。 | 22 TB/s HBM4、TMA 有助于 KV 搬运吞吐。 | 没有端到端证据表明它减少了 KV page 数、跨卡 payload 或精确 Gather 延迟。 |
| **TPOT / TTFT / Tokens/J** | 依赖触发可能缩短 kernel 间空洞；NVLink/HBM4 提供降低等待的条件。 | NVIDIA 宣传 NVL72 的 tokens/MW、token cost 和 agent throughput per watt。 | 官方没有针对附件 Indexer 的 TPOT、TTFT、HBM bytes/token、inter-GPU bytes/token 或 J/token 测量。官方数字使用特定模型、上下文和系统配置，不能替代端到端 benchmark。[产品页](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)（访问：2026-08-22）。 |

## 创新性判断（分析判断，不是 benchmark）

评分依据是[Rubin 架构深读](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)、[Rubin 官方规格](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)和 [NVLink 6 说明](https://www.nvidia.com/en-gb/data-center/nvlink/)（访问：2026-08-22）；分项分数是本文的架构研究判断，不是 NVIDIA benchmark 或性能承诺。

| 维度 | 权重 | 得分 | 判断 |
|---|---:|---:|---|
| 数据搬运与存储 | 30% | 22 | HBM4、TMA、descriptor 更新、压缩和 counted writes 覆盖了规则搬运与同步，但没有公开 Indexed Gather。 |
| 执行架构 | 20% | 16 | Tensor Core/Transformer Engine 之外，tile 级依赖触发把流水颗粒度推进了一步。 |
| 稀疏/动态计算 | 15% | 8 | 2:4 activation sparsity 有价值，但约束强，不是动态 Indexer 的任意稀疏。 |
| Scale-up/互联 | 15% | 14 | NVLink 6 的 3.6 TB/s/GPU、all-to-all 和 SHARP 对跨卡 Reduce 很强。 |
| 数值格式/计算密度 | 10% | 9 | NVFP4、adaptive compression、3-bit LUT 提高密度；50 PFLOPS 仍是规格口径。 |
| 可编程性 | 10% | 8 | CUDA/TMA/依赖调度使软件能重排路径，但公开接口没有 Retrieval 原语集合。 |
| **合计** | **100%** | **77/100** | **研究价值高于“只加 FLOPS”，但距离附件的 Retrieval GPU 仍缺 Search、Top-k、Gather 三个核心硬件证据。** |

## 局限与常见误解

1. **50 PFLOPS ≠ 端到端推理速度。** 官方规格注明 NVFP4 inference 是 sparse specification；实际 TPOT 还受 HBM achieved bandwidth、kernel 依赖、通信和模型映射影响。[规格页](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)（访问：2026-08-22）。
2. **288 GB ≠ NVL72 的 20.7 TB。** 前者是单 GPU HBM4，后者是 72 GPU 系统；3.6 TB/s/GPU 与 260 TB/s/NVL72 也分别属于芯片互联和系统互联。[官方表格](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)（访问：2026-08-22）。
3. **TMA ≠ Indexed Gather DMA。** TMA 的公开描述支持复杂布局与 descriptor 更新，不能据此推断它会按离散 KV index 自动合并访存。[架构文](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)（访问：2026-08-22）。
4. **NVLink 6 ≠ 自动减少 Top-k 通信量。** 它提升带宽、all-to-all 和 collective reduction；若软件仍发送全量 score，通信对象并不会因为链路变快而变小。（这是结合附件方案与官方互联能力的分析判断。）
5. **full production ≠ 所有人都能买到单卡。** NVIDIA 已公开量产/爬产和伙伴系统出货，但单卡 SKU、价格、TDP 与普遍云端可用性仍未完整确认；CPX 官方仍写预计 2026 年底可用。[量产公告](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform)；[CPX 状态](https://nvidianews.nvidia.com/news/nvidia-unveils-rubin-cpx-a-new-class-of-gpu-designed-for-massive-context-inference)（访问：2026-08-22）。

## 对下一代 Retrieval GPU 的可借鉴点

- **可直接借鉴：descriptor 驱动的数据搬运。** 保留可复用 descriptor，并允许运行时更新 base pointer/stride；但 Retrieval GPU 还应把 page list、索引检查和合并规则纳入 descriptor。
- **可直接借鉴：tile 级依赖触发。** 让 Search/score/Select/Gather/Attention 按 tile 或候选块流水，而不是每个阶段等整张 grid；Rubin 的公开机制证明依赖调度本身值得硬件化。
- **可直接借鉴：片上中间结果压缩与局部性。** 借鉴“尽量不把中间 score 写回 HBM”的目标，但 Exact Mode 需要保留精确语义并测 HBM bytes/token。
- **只能类比：NVLink 6 + SHARP。** 可以把它作为 Global candidate merge 的高速底座，不能把 reduction 当作 Top-k，也不能假设它会自动生成 Gather descriptor。
- **不宜照搬：把 2:4、NVFP4 或峰值 Tensor Core 当作 Retrieval 核心。** 它们适合规则矩阵和结构化稀疏；动态离散 KV 的收益仍取决于 layout、page alignment、地址生成、访问合并和跨卡 payload。（后半句与附件约束一致。）

## 资料冲突与采用口径

- 2026-03-16 新闻稿使用“seven new chips in full production”，2026-05-31 新闻稿使用“ramping into full production”。本文把前者记为芯片/平台的生产状态公告，把后者记为供应链和系统交付的爬产状态，不视为规格冲突。
- “50 PFLOPS NVFP4 inference”与“35 PFLOPS NVFP4 training”同时出现在官方规格中；datasheet 脚注明前者是 sparse specification、后者是 dense specification，本文保留这两个限定。
- “3.6 TB/s”与“260 TB/s”分别是每 GPU NVLink 带宽与 NVL72 机架聚合带宽，本文不做数值相加或互换。

## 参考来源（均为 NVIDIA 官方，访问日期：2026-08-22）

1. [NVIDIA Rubin 平台宣布，2026-01-05](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer)
2. [Vera Rubin 平台进入 full production，2026-03-16](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform)
3. [Vera Rubin 爬产与系统规模化，2026-05-31](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Vera-Rubin-Ramps-Into-Full-Production-to-Power-Agentic-AI-Factories-Worldwide/default.aspx)
4. [Rubin GPU 架构深读，2026-07-21](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)
5. [Vera Rubin NVL72 产品页与单 GPU/系统规格](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)
6. [Vera Rubin datasheet](https://dam-cdn.nvd.orangelogic.com/AssetLink/v5rf2icnf86o26e464tf6djn23r8ibhe.pdf)
7. [第六代 NVLink 与 NVLink Switch](https://www.nvidia.com/en-gb/data-center/nvlink/)
8. [Rubin CPX 宣布与可用时间，2025-09-09](https://nvidianews.nvidia.com/news/nvidia-unveils-rubin-cpx-a-new-class-of-gpu-designed-for-massive-context-inference)
+## 2026-09-01 在线复核增补

已重新打开 [NVIDIA Vera Rubin 官方新闻](https://blogs.nvidia.com/blog/vera-rubin-lpx-spectrum-x-nvlink-fusion/) 与 [NVIDIA Vera Rubin 科学计算公告](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-delivers-world-class-supercomputers-for-science)，确认 2026-08-24 官方文中将 Groq 3 LPX称为 full production，并把 Vera Rubin系统/多 GPU 机架单独描述；该状态不能回填为 Rubin 单 GPU 的出货或单卡零售可用。
