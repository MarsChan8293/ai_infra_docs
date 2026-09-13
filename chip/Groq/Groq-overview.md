# Groq 最新 LPU：Groq 3 / LP30 的架构研究

## 芯片页关系导航

本页是本目录唯一的厂家总览。下面的页面均按单一芯片、芯片家族或芯片关联产品对象拆分；芯片页中的“厂商总览”链接回到本页。`[[...]]` 用于 Obsidian 图谱，Markdown 链接用于普通阅读。

- [[groq3-lp30|Groq 3 LPU / LP30 证据页]] · [打开 Markdown](./groq3-lp30.md)
- [[groqchip-legacy|GroqChip 上一代基线证据页]] · [打开 Markdown](./groqchip-legacy.md)

> 研究窗口：2025-07-01 至 2026-08-22｜资料访问日：2026-08-22｜对象：Groq｜口径：只研究 Groq；NVIDIA 资料仅用于核验授权与 Vera Rubin 集成边界。

## 1. 一句话结论

截至 2026-08-22，公开资料中最新、命名最清楚的目标是 **Groq 3 LPU，芯片代号 LP30**，但它公开呈现为 NVIDIA Vera Rubin 体系里的 **Groq 3 LPX 机架级推理加速器**，不是一张已经独立上市的 Groq 单卡。它要解决的是解码阶段每个 token 的低延迟、抖动和数据搬运问题；最值得研究的创新是把 SRAM、显式数据移动、编译器静态调度和芯片间同步组合成一个可预测的空间数据流系统。[NVIDIA 技术博客](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)

## 2. 目标芯片与时间状态

### 边界先说清楚

| 层级 | 本文研究对象 | 不能混称的对象 |
|---|---|---|
| 芯片 | Groq 3 LPU / LP30 | 不是 GroqCloud 服务，也不是整套 Vera Rubin |
| 托盘 | 每托盘 [8 颗 LP30](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，另有主机处理器与 fabric expansion logic | 不是单颗芯片规格 |
| 机架 | Groq 3 LPX：[32 个 1U 托盘、256 颗 LPU](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | 不是 Groq 旧式 GroqRack 的同义词 |
| 平台 | LPX 与 Vera Rubin NVL72 协同，LPX 偏低延迟解码，Rubin GPU 负责长上下文 prefill 与 decode attention | 仅为授权/集成边界，不展开 NVIDIA 其他产品研究 |
| 云服务 | GroqCloud 是 Groq 独立运营的 API/云服务。授权公告明确写明 Groq 继续独立运营、GroqCloud 不间断；截至窗口末，未见证据证明 GroqCloud 的在线请求已经由 LP30 规模承载。[Groq 公告](https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale) |

### 首发、宣布、量产、可用与部署

- **时间边界**：Groq 第一代 LPU 于 [2019 年](https://home.cloud.groq.io/blog/inside-the-lpu-deconstructing-groq-speed)推出，窗口开始前已经进入 GroqCloud 和生产基础设施；不能把它写成窗口内首发。Groq 在 2025-08-01 的官方文章仍把它称为第一代、14 nm 芯片，并未给出 Groq 3/LP30 名称。
- **宣布/命名**：2026-03-16，按本次核验到的公开一手资料，NVIDIA 官方发布 Vera Rubin 时首次明确写出 “NVIDIA Groq 3 LPU”；同日技术博客给出 LP30 规格。[新闻稿](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform) [技术博客](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)
- **量产口径**：同一新闻稿称七颗新芯片 “full production”；但新闻稿同时写 LPX 将于 2026 年下半年可用，2026-05-31 的后续公告又写 Vera Rubin 生产出货从“今年秋季”开始。[后续公告](https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory) 因此采用保守表述：**设计已公开，官方称已进入量产/生产爬坡；截至 2026-08-22，LP30/LPX 的 GA、客户可购与规模部署未被官方明确确认**。
- **Groq 侧状态**：Groq 2026-06-22 说将用包括 NVIDIA 新 LPX 在内的最新推理技术改造现有云 footprint；2026-08-12 成为 NVIDIA Cloud Partner，说明集成路径已正式化，但仍不是 LP30 已在 GroqCloud 线上规模运行的证据。[Groq 2026-06-22](https://groq.com/newsroom/groq-raises-usd650m-to-scale-its-ai-inference-cloud-business) [Groq 2026-08-12](https://groq.com/newsroom/groq-becomes-an-nvidia-cloud-partner)

## 3. 核心规格表

| 项目 | Groq 3 / LP30 公开口径 | 研究边界 |
|---|---|---|
| 制程 | **公开资料未确认**。Groq 只公开说现有/第一代芯片为 [14 nm](https://groq.com/blog/the-groq-lpu-explained)，并说未来向 [4 nm](https://groq.com/blog/the-groq-lpu-explained) 发展 | 不能把 14 nm 或 4 nm 直接套到 LP30 |
| 执行单元 | MXM 矩阵执行、VXM 向量执行、SXM 数据交换；统一工作粒度为 [320-byte vector](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | 各单元数量、频率、面积未公开确认；按 [8 颗](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) 托盘的 [9.6 PFLOPS](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) 推得约 [1.2 PFLOPS FP8/颗](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，这是推导值 |
| 数值格式 | 公开的 LPU 方案包括 TruePoint 的 [100-bit 中间累加](https://home.cloud.groq.io/blog/inside-the-lpu-deconstructing-groq-speed)、FP32 attention logits、MoE 权重的 block floating point、FP8 activation；LPX 机架标注 FP8 inference compute | LP30 完整格式/吞吐表未公开确认 |
| 片上内存 | 每颗 [500 MB SRAM](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，作为主要工作存储而非传统 cache | 容量有限，不能等同于整机模型容量 |
| 片外内存 | LPX 机架另有 [12 TB DDR5](https://www.nvidia.com/en-au/data-center/lpx/)，托盘侧公开为 fabric expansion logic 最多 [256 GB](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)、主机最多 [128 GB](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | “SRAM-first”不等于整架没有片外内存；LP30 本身没有公开 HBM 规格 |
| 带宽 | 单颗 SRAM [150 TB/s](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，单托盘 [1.2 PB/s](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，整架 [40 PB/s](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | 这些是峰值/聚合口径，不是某个模型的有效 KV 带宽 |
| 互联 | 每颗 [96 条 C2C link、112 Gbps/link、双向聚合 2.5 TB/s](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)；整架 [640 TB/s scale-up](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)、[256 芯片](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | LPX 还有 C2C spine 与 fabric logic，不能简单复述为“完全没有系统级互联逻辑” |
| 功耗/散热 | **LP30 单芯片功耗公开资料未确认**；LPX 公开为全液冷 | Groq 旧 GroqChip 的 [300 W max/215 W TDP/185 W average](https://www.groq.com/GroqDocs/Product%20Spec%20Sheet%20-%20GroqChip%E2%84%A2%20Processor.pdf) 不能移植给 LP30，仅作时间边界 |

## 4. ELI5：它究竟改了什么

### 先看问题

生成一个 token 要反复读权重、读 KV、做矩阵运算、把中间结果送到下一颗芯片。若每次都由运行时临时排队、抢资源、等待数据，平均速度之外还会出现尾延迟。长上下文和小 batch 会让“搬数据和等数据”比“算乘法”更显眼。

### 机制

Groq 的办法像一条提前排好班次的流水线。编译器在运行前把算子、内存读写、芯片间传输和时间安排写进执行计划；SRAM 把热数据放在芯片旁边；MXM 做矩阵，VXM 做向量和激活，SXM 做置换、旋转、分发和转置；C2C 链路把多颗 LPU 接成一条可预测的数据流。Groq 的公开材料还描述了 plesiosynchronous 协议和周期性软件同步，用来校正晶振漂移、对齐多芯片执行。[Groq LPU 说明](https://groq.com/blog/the-groq-lpu-explained) [Groq 2025 架构文章](https://home.cloud.groq.io/blog/inside-the-lpu-deconstructing-groq-speed)

### 技术类比与失效边界

类比成工厂传送带是有用的：每个工位知道何时拿料、加工、交料，多颗芯片像连续工位。边界也要说清：它不是数据库，不会自动把动态 Search、精确 Top-k、page-aware KV Gather 变成便宜操作；静态编译对数据形状、分支和内存布局有要求；SRAM 很快但很小，大模型仍需分片并承担跨芯片通信。

## 5. 与《推导推理GPU新路径-ELI5.html》的映射

附件提出的 Retrieval Plane 要独立处理 Search、Reduce、Top-k、Gather、Route、Address。Groq 3 的公开资料更接近“确定性的 Tensor/数据流平面”，而不是已经公开的 Retrieval GPU。

| 附件概念 | 直接解决 | 间接帮助 | 没有解决或证据不足 |
|---|---|---|---|
| 密集计算 | MXM、FP8 与 SRAM 直接服务 dense FFN/MoE decode；LPX 的公开定位就是低延迟解码路径 | 编译器把矩阵、向量、传输排成流水 | 不证明对稀疏 KV 检索同样有效 |
| Search / Indexer | — | MXM/VXM 可承载点积和扫描，静态数据流可减少 launch/调度开销 | 没有公开 Search/Indexer 专用单元或 exact retrieval 结果 |
| Top-k / Reduce | — | VXM 与显式数据流可以实现固定规约 | 没有公开 TOPK、MERGE_TOPK 或 streaming reduction 原语 |
| 离散 KV Gather | — | SRAM 与 SXM 的结构化搬运有利于规则化的数据交换 | 没有公开 indexed gather DMA、page table translator 或离散 KV 语义 |
| Address / Route | — | SXM 支持 permutation/rotation/distribution/transpose，编译器能显式安排路由 | 没有证据表明它能硬件生成动态物理地址或 page-aware route |
| 跨卡通信 | 直接解决通信时序与带宽的一部分：C2C、plesiosynchronous 协议、编译器调度和大规模同步 | 可把多芯片 pipeline 做成稳定 token 流 | 不等于跨卡 Top-k merge，也不自动减少检索候选数 |
| TPOT / TTFT / Tokens / J | 直接针对低抖动 per-token latency；官方把 LPX 定位为交互式解码 | SRAM、静态调度和流水线可能降低等待与能耗 | 公开的是机架级/预测性指标；LP30 的实测 TPOT、TTFT、Tokens/J 未确认，不能把 [1,000 tokens/sec/user](https://groq.com/platform) 当成通用 benchmark |

## 6. 六维创新性评分

这是“对附件所要研究的 Retrieval GPU 有多大架构启发”的判断，不是 benchmark，也不是商业成功评分。按 0–10 分、权重求和：

| 维度 | 权重 | 分数 | 判断 |
|---|---:|---:|---|
| 数据搬运/存储 | 30% | 9.0 | SRAM-first、显式搬运和 [150 TB/s](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) 片上带宽是最强启发，但容量约束很硬 |
| 执行架构 | 20% | 9.0 | 空间数据流、编译器静态调度、无运行时抢占是清晰的路线 |
| 稀疏/动态计算 | 15% | 4.0 | MoE 可扩展，但公开资料没有 exact Search/Top-k/Gather 专用硬件 |
| Scale-up/互联 | 15% | 9.0 | 96 条 C2C、2.5 TB/s/颗、256 颗机架和时钟对齐形成系统级优势 |
| 数值格式/计算密度 | 10% | 8.0 | TruePoint、FP32/FP8/BFP 的按层选择有研究价值；LP30 完整格式表缺失 |
| 可编程性 | 10% | 8.5 | 编译器控制算子、内存、网络，模型适配面较好；动态形状和编译成本仍是边界 |

**总分：81.0/100。** 分数高在“把算、存、传放进同一份时间表”，分数被拉低的地方正是附件最关心的动态检索原语尚未被 Groq 公开证明。

## 7. 局限与常见误解

1. **SRAM 快不等于容量够。** [500 MB/颗和 128 GB/架](https://www.nvidia.com/en-au/data-center/lpx/)是不同层级；更大的模型要分片，片外 DDR5 与 C2C 仍会进入路径。
2. **确定性不等于所有请求都零抖动。** 它主要约束已编译的算子与通信；动态分支、外部网络、云端排队和模型装载仍可能变化。
3. **Groq 3 不等于旧 GroqChip 规格升级版的简单换名。** [14 nm、230 MB、80 TB/s、215 W TDP](https://www.groq.com/GroqDocs/Product%20Spec%20Sheet%20-%20GroqChip%E2%84%A2%20Processor.pdf) 是旧公开产品值，不能推导 LP30 的制程和功耗。
4. **LPX 不等于 GroqCloud。** LPX 是 NVIDIA Vera Rubin 侧的机架产品；GroqCloud 是 Groq 独立运营的服务。到截止日，LP30 在 GroqCloud 的规模上线公开证据不足。
5. **高带宽不等于 Retrieval Plane。** 没有公开 TOPK、page map、indexed gather，就不能把 Groq 的数据流互联直接写成附件方案已经实现。

## 8. 下一代 Retrieval GPU 可借鉴点

### 可直接借鉴

- 用软件管理的片上 SRAM 保存热的 index metadata、KV page descriptor 和中间候选；把 HBM/DDR 访问变成可编排的异步数据流。
- 借鉴 Groq 的“显式数据移动 + 编译器时间表”，为稳定的 Search/Reduce/Gather 图生成 descriptor queue，并让 Tensor、Vector、DMA 共享片上缓冲。
- 借鉴 C2C 的高带宽和 plesiosynchronous 思路，为 Local Top-k、候选 Merge 和 KV descriptor 交换提供可预测的跨卡时序。

### 只能类比

- SXM 的 permutation/route 只能类比 Address/Route；它不是公开的 page-aware indexed gather。
- LPX 的 dense decode 与低延迟路径分工可以类比 Tensor Plane + Retrieval Plane，但 Groq 资料没有证明它有 Retrieval Plane。
- Groq 对 MoE 的跨芯片共享资源 fabric 可以类比 candidate-sharding，却不能代替 exact Top-k 的正确性和通信量实验。

### 不宜照搬

- 不要把“全 SRAM”当成万能答案；Retrieval GPU 应按热元数据、KV page 和大容量存储分层。
- 不要把所有动态检索都静态编译；要保留可编程 TOPK、MERGE、GATHER、PAGE-TRANSLATE 和异常路径。
- 不要把 320-byte 固定向量或 LPX 的 [35×/MW](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) 预测性系统指标当作检索收益。第一验证仍应是附件要求的 exact local Top-k merge，并测 TPOT、HBM bytes/token、跨卡 bytes/token、Tokens/J 和召回/一致性。

## 9. 关键参考来源

1. [Groq：What is a Language Processing Unit?（2025-03-07）](https://groq.com/blog/the-groq-lpu-explained)（SRAM、确定性、编译器、14 nm；访问日 2026-08-22）。
2. [Groq：Inside the LPU: Deconstructing Groq’s Speed（2025-08-01）](https://home.cloud.groq.io/blog/inside-the-lpu-deconstructing-groq-speed)（TruePoint、静态调度、C2C 同步；访问日 2026-08-22）。
3. [Groq：From Speed to Scale（2025-05-27）](https://groq.com/blog/from-speed-to-scale-how-groq-is-optimized-for-moe-other-large-models)（大模型/MoE 与 RealScale；访问日 2026-08-22）。
4. [Groq：GroqChip Processor Product Brief](https://www.groq.com/GroqDocs/Product%20Spec%20Sheet%20-%20GroqChip%E2%84%A2%20Processor.pdf)（旧一代规格，仅作时间边界；访问日 2026-08-22）。
5. [Groq：与 NVIDIA 的非排他推理技术授权公告（2025-12-24）](https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale)（独立运营与 GroqCloud 连续性；访问日 2026-08-22）。
6. [NVIDIA：Vera Rubin Opens Agentic AI Frontier（2026-03-16）](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform)（Groq 3 命名、LPX 集成与可用时间；访问日 2026-08-22）。
7. [NVIDIA：Inside NVIDIA Groq 3 LPX（2026-03-16）](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)（LP30、托盘、机架和互联详细规格；访问日 2026-08-22）。
8. [NVIDIA：Vera Rubin Ramps Into Full Production（2026-05-31）](https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory)（量产爬坡与出货时间冲突口径；访问日 2026-08-22）。
9. [Groq：GroqCloud Expanding to Meet Demand（2026-02-16）](https://groq.com/blog/groqcloud-expanding-to-meet-demand)（GroqCloud 独立扩张与现有 LPU 生产服务；访问日 2026-08-22）。
10. [Groq：Groq Raises $650M（2026-06-22）](https://groq.com/newsroom/groq-raises-usd650m-to-scale-its-ai-inference-cloud-business)（Groq 计划将 NVIDIA LPX 纳入 footprint；访问日 2026-08-22）。

> 证据边界：截至 2026-08-22，未找到 Groq 自己发布的 LP30 完整 datasheet，亦未找到可确认 LP30 已在 GroqCloud 规模部署的官方记录；制程、单芯片功耗、TOPK/Gather 专用硬件和实测 Tokens/J 均应保留为“公开资料未确认”。
+## 2026-09-01 在线复核增补

已重新打开 [Groq 3 LPX 官方公告](https://groq.com/blog/groq-among-the-first-to-bring-nvidia-groq-3-lpx-and-vera-rubin-nvl72-to-market) 与 [Groq Cloud 平台页](https://groq.com/platform)，确认 2026-08-24 公告将 LPX/Vera Rubin NVL72描述为计划部署并接入推理云；平台页把 256 LPU、40PB/s SRAM 带宽等标为机架级口径，不能写成单芯片规格。
