# AMD Instinct 与芯片：2025-06 之后最新款

> 范围：AMD Instinct；目标时间：2025-07-01 至 2026-08-22；资料访问日期：2026-08-22。对照基线：[《推导推理GPU新路径-ELI5.html》](/Users/chenmingmin/Documents/GitHub/ai_infra_chip/推导推理GPU新路径-ELI5.html)。

## 一句话结论

截至 2026-08-22，AMD 在窗口内公开的、规格最完整且面向前沿推理的最新款是 **MI455X**。它最值得研究的创新是把 HBM4、片上缓存、低精度计算和大规模 scale-up 组合起来，先解决“数据能否留在本地、能否快速跨卡移动”；但公开资料没有确认它拥有附件所设想的 Retrieval Plane，也没有确认动态 Indexer、硬件 Top-k、KV page-aware Gather 或地址生成单元。因此它是强 memory/互联的通用推理 GPU，不是已完成 Search/Select/Move/Route/Address 分工的 Retrieval GPU。（[1]、[2]，访问日期：2026-08-22。）

## 目标芯片与时间状态

窗口内并非没有新型号，关键是区分“首发、宣布、可用”。MI355X 首发为 2025-06-12，早于窗口；但 2025 年下半年平台已可通过方案伙伴获得，适合作为上一代基线。MI440X 于 2026-01-05 宣布，定位企业本地 AI 的八 GPU 形态，但公开资料未给出完整芯片规格或量产日期。MI455X 于 2026-07-23 发布并有单卡产品页、数据表和 CDNA 5 白皮书，故选为主对象。MI430X 同日公开，但 AMD 写明预计 2027 年可用；MI500 仍是 2027 年计划/预览，均不能当作 2026-08-22 前可用的新推理芯片。（[4]、[7]、[8]、[10]，访问日期：2026-08-22。）

MI455X 是单颗加速器；四 GPU 是 Helios compute tray；72 GPU、31 TB HBM4、约 2.9 EFLOPS 属于 Helios 机架级参考设计。AMD FAQ 明确 Helios 是 reference design、不是直接售卖的单一产品，量产部署预计在 2026 年下半年。因此 MI455X 是“已发布/已宣布”，Helios 是“已进入生产部署叙事、量产部署时间已宣布”，但单卡普遍现货仍为“公开资料未确认”。（[4]、[5]、[6]，访问日期：2026-08-22。）

## 核心规格表：MI455X 单卡

| 项目 | 规格 | 研究解读 |
|---|---|---|
| 制程/架构 | TSMC 2 nm + 3 nm FinFET；CDNA 5 | 8 个 XCD、2 个 I/O die；采用 chiplet 封装。（[1]、[2]，访问日期：2026-08-22。） |
| 计算单元 | 256 WGP、Wave32；AMD未另列 Matrix Core 数量 | 官方把 MI355X 的 256 CU 与 MI455X 的 256 WGP 分开命名，不能当作同名指标硬比。（[1]、[2]，访问日期：2026-08-22。） |
| 低精度/矩阵 | OCP MXFP4 40.3 PFLOPS；MXFP6、MXFP8、OCP FP8 各 20.1 PFLOPS；矩阵 FP16/BF16 各 5 PFLOPS；INT8 矩阵 5 POPS | 都是峰值理论值；部分结构化稀疏矩阵值可达 2 倍。（[1]、[3]，访问日期：2026-08-22。） |
| 片上/封装内存 | L2 192 MB；LDS SRAM 总量约 96 MB；432 GB HBM4、12 stacks | HBM4 是封装内 DRAM，不是 WGP 旁的 SRAM；容量适合放更大的 KV，但不自动改变访问模式。（[1]、[2]，访问日期：2026-08-22。） |
| 内存带宽 | 23.3 TB/s 峰值 | 芯片专页、CDNA 5 页面和 2026-07 数据表均采用该值。（[1]、[2]、[3]，访问日期：2026-08-22。） |
| 互联 | 主机 Infinity Fabric 256 GB/s 双向；UALoE scale-up 3.6 TB/s 双向；UALink scale-out 600 GB/s 双向 | 是通信路宽，不等于 Global Top-k 或检索 collective。（[2]、[3]，访问日期：2026-08-22。） |
| 功耗 | MI455X 单卡 TBP/TDP：公开资料未确认 | MI355X 的 1400 W 不能移植给 MI455X。（[1]、[7]，访问日期：2026-08-22。） |

来源：[1]、[2]、[3]，访问日期：2026-08-22。资料冲突需单列：Helios 页面某个 compute-tray 段落写每 GPU 19.6 TB/s；单卡产品页、白皮书和数据表写 23.3 TB/s。AMD 未解释原因，本文采用芯片专页/白皮书/数据表值，不用 19.6 TB/s 推导性能。（[1]、[2]、[11]，访问日期：2026-08-22。）

## ELI5：它解决了什么，没解决什么

### 问题先行

附件把新推理 GPU 的问题拆成四类：密集计算、动态检索/Indexer、Top-k/Reduce、离散 KV Gather 与跨卡通信。Indexer 要在运行时找候选、算分、保留 Top-k，再把离散索引翻译成 KV page 和物理地址；长上下文下，成本不只有 GEMM，还包括 DRAM 请求、地址 bookkeeping 和跨卡搬运。（[附件](/Users/chenmingmin/Documents/GitHub/ai_infra_chip/推导推理GPU新路径-ELI5.html)、[2]，访问日期：2026-08-22。）

MI455X 的路线可以类比为“更大的仓库、更宽的传送带、更快的仓库间道路”。HBM4 是货架，L2/LDS 是工作台，TDM 是按描述符搬运规则 tensor tile 的异步叉车，UALoE 是 GPU 间高速路；MXFP4/6/8 是更小的数字盒子。CDNA 5 白皮书确认 TDM 可异步搬运最多五维张量，并支持 LDS 与 DRAM 之间不经寄存器的传输；split DMA 会把 GPU 间请求分到合适链路。（[2]，访问日期：2026-08-22。）

类比边界是关键：叉车不会自己判断“哪 k 个货架最相关”，高速路也不会执行 Top-k。公开资料没有出现 `Retrieval Core`、`MERGE_TOPK`、`KV Page Translator` 或 `Indexed Gather DMA`。所以 MI455X 强化了 Move 的规则路径和 Route 的通信底座，但没有公开确认 Search/Select/Address 的专用硬件。（[1]、[2]、[3]，访问日期：2026-08-22；“没有公开确认”是对 AMD 产品页、CDNA 5 白皮书和 ISA 入口的资料边界判断。）

## 与附件 Retrieval Plane 的映射

| 附件问题 | 直接解决 | 间接帮助 | 没解决/证据不足 |
|---|---|---|---|
| 密集计算 | WGP、Wave32、MXFP4/6/8、FP16/BF16/INT8 | Q/K 投影、attention、重排可用成熟 ROCm 内核 | 低精度峰值不保证不规则 Indexer 等比例加速。（[1]，访问日期：2026-08-22。） |
| Search / Indexer | 无专用单元公开 | HBM、L2、LDS、TDM 可降低候选 Key 的搬运压力 | 无动态地址生成、流式 score、Indexer 公式硬件化证据。（[2]，访问日期：2026-08-22。） |
| Select / score materialization | 片上缓存为 tile 保留提供基础 | 软件可做分块/融合 attention | 没有证据证明硬件保证“不物化完整 score”；TDM 不是 Top-k 引擎。（[2]，访问日期：2026-08-22。） |
| Reduce / Local-Global Top-k | 无公开 Top-k 或 Merge Top-k 原语 | WGP、ROCm/RCCL、跨卡带宽可承载软件实现 | 是否把全量 all-reduce 变为 `P×k` 候选合并，公开资料未确认。（[1]、[2]，访问日期：2026-08-22。） |
| Move / Gather / Address | TDM 直接利于规则 tile；CPU 可一致性访问 GPU 内存 | ROCm Infinity Context/hipFile 可直连 HBM 与网络存储，适合 KV 分层 | 没有 page-aware Gather、KV page translator、物理地址描述符；AIC 也不是离散 Gather。（[2]、[9]，访问日期：2026-08-22。） |
| Route / 跨卡 / TPOT、TTFT、Tokens/J | UALoE 3.6 TB/s、UALink 600 GB/s、72-GPU pod 改善通信底座 | 给 candidate-sharding 和小候选 Merge 留出路宽 | 没有 Retrieval-specific collective，也未找到 MI455X 在该类 workload 上同时报告 TPOT、TTFT、Tokens/J 的实测。Helios token throughput 是特定模型与输入输出长度下的 AMD 建模，不能替代端到端 benchmark。（[2]、[5]，访问日期：2026-08-22。） |

## 创新性判断：不是 benchmark

| 维度 | 权重 | 得分 | 理由 |
|---|---:|---:|---|
| 数据搬运与存储 | 30% | 24 | HBM4、L2/LDS、TDM 很强，但没有离散 Gather 语义。 |
| 执行架构 | 20% | 15 | XCD/WGP/Wave32/chiplet 有价值，仍以通用平面为主。 |
| 稀疏/动态计算 | 15% | 6 | 有低精度与结构化稀疏，无动态 Search/Select/Top-k 证据。 |
| Scale-up/互联 | 15% | 14 | 3.6 TB/s、72-GPU pod 直接回应跨卡压力，但不是检索 collective。 |
| 数值格式/计算密度 | 10% | 9 | OCP MXFP4/6/8 规格完整，峰值不等于利用率。 |
| 可编程性 | 10% | 8 | ROCm/HIP/Triton/vLLM/SGLang 路径完整，未公开 Retrieval ISA。 |
| **合计** | **100%** | **76/100** | **偏强的 memory/scale-up 参考，不是 Retrieval Plane 成品。** |

这是架构研究价值的分析判断，不是 AMD 官方评分，也不是 benchmark。（规格依据：[1]、[2]、[3]，访问日期：2026-08-22。）

## 局限与常见误解

1. **峰值理论值不等于端到端推理速度。** 40.3 PFLOPS MXFP4 不是 TPOT；官方 token throughput/tokens-per-dollar 还有特定模型、上下文和建模条件。（[5]，访问日期：2026-08-22。）
2. **HBM 带宽不等于随机 Gather 延迟。** page layout、块大小、地址生成、缓存命中和并发仍决定离散 KV 效果，公开资料未给 MI455X 的 page-aware Gather 测试。
3. **互联带宽不等于 Global Top-k 已经便宜。** 如果软件仍物化全量 score，再做全量 reduction，链路变宽不会自动变成 `P×k`。
4. **432 GB HBM 不等于 1M context 必然放得下。** KV 还随层数、KV head、维度、数据类型、并发和复用变化；AMD 自己仍在用 AIC 做 KV 分层。（[9]，访问日期：2026-08-22。）
5. **MI455X 功耗不能用 MI355X 1400 W 代替。** MI455X 单卡 TBP 公开资料未确认。（[1]、[7]，访问日期：2026-08-22。）

## 对下一代 Retrieval GPU 的借鉴

- **可直接借鉴：** HBM4 + L2/LDS + 描述符搬运层，但把 TDM 扩展成 page-aware indexed Gather，并让输出携带 page/地址描述。
- **可直接借鉴：** candidate/block 分片与 scale-up 路径结合，在通信硬件旁增加 `Local Top-k`、`Merge Top-k`。
- **可直接借鉴：** 保留低精度矩阵能力，同时暴露 Search/Reduce 的向量与规约原语，让模型公式由编译器组合。
- **只能类比：** split DMA、TDM、72-GPU pod 说明搬运与计算可分层，但不能证明 Search/Select/Address 已存在。
- **不宜照搬：** 不要只堆 HBM、峰值 FLOPS 或机架规模；先用 exact 软件原型验证 score materialization、Local/Global Top-k、Gather 和端到端 TPOT，再决定专用硅面积。

## 参考来源

[1]: https://www.amd.com/en/products/accelerators/instinct/mi400/mi455x.html "AMD Instinct MI455X 产品页"
[2]: https://www.amd.com/content/dam/amd/en/documents/products/technologies/cdna/amd-cdna5-whitepaper.pdf "AMD CDNA 5 Architecture 白皮书"
[3]: https://www.amd.com/content/dam/amd/en/documents/products/accelerators/instinct/amd-instinct-mi455x_brochure.pdf "AMD Instinct MI455X GPU 数据表"
[4]: https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era "AMD AAI 2026 新闻稿"
[5]: https://newsroom.amd.com/news/aai-2026-helios-update/ "AMD Helios 新闻稿与脚注"
[6]: https://www.amd.com/content/dam/amd/en/documents/products/accelerators/instinct/amd-instinct-helios-blueprint-brochure.pdf "AMD Helios Rackscale Solution 蓝图"
[7]: https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html "AMD Instinct MI355X 产品页"
[8]: https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/product-briefs/amd-instinct-miI355x-platform-brochure.pdf "AMD MI355X 平台数据表"
[9]: https://rocm.blogs.amd.com/software-tools-optimization/amd-infinity-context/README.html "ROCm Infinity Context"
[10]: https://newsroom.amd.com/news/amd-and-its-partners-share-their-vision-for-ai-ev/ "AMD CES 2026：MI440X 与 MI500"
[11]: https://www.amd.com/en/products/rackscale-solutions/helios.html "AMD Helios 产品页"
