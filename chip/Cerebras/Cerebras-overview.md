# Cerebras WSE-3 Turbo / CS-4：2025-06 之后最新晶圆级 AI 芯片

## 芯片页关系导航

本页是本目录唯一的厂家总览。下面的页面均按单一芯片、芯片家族或芯片关联产品对象拆分；芯片页中的“厂商总览”链接回到本页。`[[...]]` 用于 Obsidian 图谱，Markdown 链接用于普通阅读。

- [[wse-3-turbo|Cerebras Systems — WSE-3 Turbo / WSE-3T]] · [打开 Markdown](./wse-3-turbo.md)
- [[wse-3|Cerebras Systems — WSE-3]] · [打开 Markdown](./wse-3.md)

> 研究范围：Cerebras；公开资料窗口：2025-07-01 至 2026-08-22；资料访问日期：2026-08-22。本文只讨论 Cerebras，不把 CS-3 的旧规格冒充新芯片。

## 一句话结论

截至 2026-08-22，Cerebras 在窗口内能确认的最新处理器是 **WSE-3 Turbo（WSE-3T）**，于 2026-08-18 随 **CS-4** 一起宣布。它主要瞄准推理解码阶段的内存带宽、跨晶圆通信和机架级部署，最值得研究的创新是把 44GB 片上 SRAM、53.5 PB/s 片上 fabric 与 3 片晶圆组成的低延迟系统放在同一个设计里。它没有公开证明自己实现了附件所设想的专用 Search、Top-k 或 Gather DMA 平面，因此更像“把搬运的路修宽、修近”，还不是完整的 Retrieval GPU。[官方新闻稿](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions)（宣布日期：2026-08-18；访问日期：2026-08-22）

## 目标芯片与时间状态

|对象|时间与状态|芯片、系统、服务边界|
|---|---|---|
|WSE-3|2024-03-13 发布，早于本次窗口，只作上一代基线|一片 WSE-3 进入一台 CS-3；CS-3 还包含供电、液冷、网络和管理。旧基线不能当作窗口内新芯片。[官方发布](https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine)（访问日期：2026-08-22）|
|WSE-3 Turbo|2026-08-18 宣布，窗口内最新 WSE 处理器|芯片本体。官方称首个搭载它的 CS-4 由三片 WSE-3T 组成；WSE-3T 已宣布，量产规模和独立购买状态公开资料未确认。[官方新闻稿](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions)（访问日期：2026-08-22）|
|CS-4|2026-08-18 宣布，首批出货“本季度开始”|一台机架级系统，含三片 WSE-3T、计算 backpack、供电、直液冷、Wafer I/O 和 Nexus 机架。到截止日仍应标为“宣布/计划出货”，不能写成已普遍可用。[CS-4 产品页](https://www.cerebras.ai/cs4)（访问日期：2026-08-22）|
|CS-3 相关更新|2026-03-13 宣布 AWS 部署 CS-3，并通过 Bedrock 提供服务；这是系统/云服务更新，不是新 WSE|AWS 与 Cerebras 还宣布 Trainium 做 prefill、CS-3 做 decode 的异构方案。具体区域、容量和完全生产化交付，所引页面没有给全。[官方 AWS 更新](https://www.cerebras.ai/blog/cerebras-is-coming-to-aws)（访问日期：2026-08-22）|

本次检索没有发现 2025-07-01 至 2026-08-17 另一个已公开的新 WSE 代际；WSE-3T 是严格截止日内的最新处理器，CS-4 是对应的最新系统。窗口内能核验到的后续资料主要是架构白皮书和 CS-3 服务更新，不能升级成新芯片。[官方白皮书目录](https://www.cerebras.ai/whitepapers)（资料列示日期：2025-10-17；访问日期：2026-08-22）

## 核心规格表

|项目|WSE-3 Turbo，单片晶圆|CS-4，单系统|资料边界|
|---|---|---|---|
|制程、面积、晶体管|TSMC 5nm；46,225 mm²；4 万亿晶体管|3 × WSE-3T|官方 CS-4 数据表明确给出。[数据表 PDF](https://cdn.sanity.io/files/e4qjo92p/production/bb028ae2422089dfbcc9fd2455c021f3625c7a75.pdf)（访问日期：2026-08-22）|
|计算单元|900,000 个 AI 优化核心|3 片 WSE-3T|官方把 WSE-3T AI compute 写为 250 PFLOPS，按稀疏 FP16 统计；CS-4 为 750 PFLOPS。[新闻稿](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions)（访问日期：2026-08-22）|
|数值格式|公开资料确认稀疏 FP16 计算口径；Cerebras 开发文档列出 FP32、FP16、bfloat16，另一版本文档列出 cbfloat16|WSE-3T 专属 FP8、INT8 或量化吞吐未确认|不能把通用 CS 文档的格式列表当成 WSE-3T 的完整硬件格式表。[开发文档 1.8](https://training-api.cerebras.ai/en/1.8.0/wsc/general/cs-1-data-formats.html) 与 [开发文档 2.1](https://training-api.cerebras.ai/en/2.1.0/wsc/how_to_guides/cs-1-data-formats.html)（访问日期：2026-08-22）|
|片上内存|44GB SRAM|按 44GB × 3 计算为 132GB，系统总可用容量未单独确认|这是片上 SRAM，不等于任意规模 KV Cache；外部 MemoryX/存储容量的 CS-4 数字公开资料未确认。[数据表 PDF](https://cdn.sanity.io/files/e4qjo92p/production/bb028ae2422089dfbcc9fd2455c021f3625c7a75.pdf)（访问日期：2026-08-22）|
|内存带宽|43.2 PB/s|129.6 PB/s|官方公布值，单位沿用原资料。[CS-4 新闻稿](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions)（访问日期：2026-08-22）|
|片上互联与 I/O|片上 fabric 53.5 PB/s；片外 I/O 2.4 Tb/s/片|片上 fabric 160.5 PB/s；I/O 7.2 Tb/s|支持可编程 Wafer I/O、RoCE v2 RDMA 和无交换机 Direct Wafer Links；官方把晶圆间延迟降到最低 2 μs。[数据表 PDF](https://cdn.sanity.io/files/e4qjo92p/production/bb028ae2422089dfbcc9fd2455c021f3625c7a75.pdf)（访问日期：2026-08-22）|
|功耗|绝对瓦数公开资料未确认|未给出机架总瓦数；官方称供电转换距离约 0.5mm，并可向 WSE-3T 提供上一代约两倍功率，CS-4 宣称最高 10× CS-3 吞吐/W|“两倍供电”和“10× 吞吐/W”都不能替代绝对功耗或统一负载下的 Tokens/J。[CS-4 产品页](https://www.cerebras.ai/cs4)（访问日期：2026-08-22）|

公开口径显示，WSE-3T 与 WSE-3 仍共享 5nm、46,225 mm²、4 万亿晶体管、900,000 核心和 44GB SRAM 这组基础数字；Cerebras 把 WSE-3T 的代际提升写在 250 PFLOPS、43.2 PB/s、53.5 PB/s fabric 和更高供电上。WSE-3T 是否改动了 PE 内部微架构、缓存组织或 NoC 拓扑，公开资料未确认。[官方新闻稿](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions)（访问日期：2026-08-22）

## ELI5 核心特性

### 先问它要解决什么

生成 token 时，模型每一步都要读历史状态。附件把工作拆成 Search、Select、Move、Route、Address，担心的正是“找到哪些 KV、算出分数、筛出 Top-k、再按离散地址把 KV 搬回来”。Cerebras 的公开叙述重点在 decode 的带宽压力：AWS/Cerebras 将 prefill 描述为计算密集，将 decode 描述为内存带宽密集，并称 CS-3 把模型权重放进片上 SRAM；CS-4 延续这条路线。[官方 AWS 更新](https://www.cerebras.ai/blog/cerebras-is-coming-to-aws)（访问日期：2026-08-22）

### 类比与技术层

可以把 WSE-3T 想成一座把“工人、工具柜和厂内道路”铺在一整片晶圆上的工厂。44GB SRAM 是分布在计算单元旁边的工具柜，53.5 PB/s fabric 是厂内道路，Direct Wafer Links 是三座工厂之间的短桥。数据少走片外长途，解码就有机会更快。Cerebras 2025 年架构资料明确提到细粒度 dataflow core、分布式 SRAM，以及为机器学习设计的片上和片外互联；WSE-3T 则把公开带宽翻倍到 43.2 PB/s。[官方白皮书目录](https://www.cerebras.ai/whitepapers)（访问日期：2026-08-22）[WSE-3T 数据表](https://cdn.sanity.io/files/e4qjo92p/production/bb028ae2422089dfbcc9fd2455c021f3625c7a75.pdf)（访问日期：2026-08-22）

官方资料使用 `fabric`、router 和 Wafer I/O 等术语，CS-4 公开页没有给出 WSE-3T 专属 NoC 的拓扑图、每跳宽度、路由表或拥塞控制细节。下文把“片上 fabric/NoC”作为功能层概念，不把未公开的微架构细节补成事实。

类比的边界也很重要。厂内道路能降低通信距离，不会自动变成数据库索引；44GB SRAM 能装下很多局部数据，不代表长上下文的全部 KV 都能常驻；片上 router 能送消息，也不等于有 KV page table、离散地址生成和 Gather DMA。CS-4 公开的是 fabric、I/O 和系统连接能力，WSE-3T 专用 Search/Top-k/Gather 单元的证据不足。[CS-4 数据表](https://cdn.sanity.io/files/e4qjo92p/production/bb028ae2422089dfbcc9fd2455c021f3625c7a75.pdf)（访问日期：2026-08-22）

### 晶圆为什么不会因一个坏点全报废

Cerebras 的公开说明是“小核心 + 冗余路由 + 备用核心 + fail-in-place”。WSE-3 的制造说明给出约 970,000 个物理核心、900,000 个当前产品启用核心，坏点被关闭，连接通过冗余路径绕行；这解决的是晶圆级良率和可用面积。它对附件的启发是让大规模片上网络具备绕障能力，但它不等于动态 KV 路由器，也不代表运行时拥塞、Top-k 候选合并已经解决。[官方制造说明](https://www.cerebras.ai/blog/100x-defect-tolerance-how-cerebras-solved-the-yield-problem)（上一代技术基线，发布日期：2025-01-13；访问日期：2026-08-22）

## 它对附件系统问题的映射

下面的“直接解决、间接帮助、没有解决/证据不足”是分析判断，依据 Cerebras 已公开的片上存储、fabric、I/O 和系统状态，与附件所要求的 Retrieval 原语逐项对照；不是 Cerebras 的 benchmark 结论。

|附件问题|判断|理由与边界|
|---|---|---|
|密集计算|**直接解决**|WSE-3T 把每片 AI compute 提到 250 PFLOPS，适合矩阵和规则数据流；它没有证明能减少 Indexer 的扫描量。[官方数据表](https://cdn.sanity.io/files/e4qjo92p/production/bb028ae2422089dfbcc9fd2455c021f3625c7a75.pdf)（访问日期：2026-08-22）|
|Search / Indexer|**间接帮助，直接证据不足**|高带宽 SRAM 和 dataflow core 可让扫描更接近计算，但公开资料没有专用 Indexer 或检索指令。[官方架构资料](https://www.cerebras.ai/whitepapers)（访问日期：2026-08-22）|
|Select、Reduce、Top-k|**没有解决/证据不足**|片上 fabric 有利于传递局部结果，公开规格没有 Streaming Top-k、Local Top-k 或 Global Merge 单元。[CS-4 数据表](https://cdn.sanity.io/files/e4qjo92p/production/bb028ae2422089dfbcc9fd2455c021f3625c7a75.pdf)（访问日期：2026-08-22）|
|Move|**间接帮助**|片上 SRAM、43.2 PB/s 内存带宽和 53.5 PB/s fabric 会降低规则数据移动成本；离散 KV 的合并访问和 DMA 描述符没有公开。[官方架构资料](https://www.cerebras.ai/whitepapers)（访问日期：2026-08-22）|
|Route / Address|**Route 部分间接帮助；Address 没有解决**|片上 fabric/router 的消息路由、冗余绕行和 Direct Wafer Links支持扩展；KV page 到物理地址的翻译、排序和权限边界未公开。[CS-4 介绍](https://www.cerebras.ai/blog/introducing-cerebras-cs-4)（访问日期：2026-08-22）|
|score materialization|**间接帮助，证据不足**|更大的片上空间可能容纳流式 partial score；没有官方证据表明 CS-4 已把 score、Top-k、Gather 融合成一条流水。[CS-4 数据表](https://cdn.sanity.io/files/e4qjo92p/production/bb028ae2422089dfbcc9fd2455c021f3625c7a75.pdf)（访问日期：2026-08-22）|
|Local / Global Top-k|**没有解决/证据不足**|没有公开每分区 Local Top-k、跨晶圆 Global Merge 或候选数为 `P×k` 的硬件语义。[CS-4 数据表](https://cdn.sanity.io/files/e4qjo92p/production/bb028ae2422089dfbcc9fd2455c021f3625c7a75.pdf)（访问日期：2026-08-22）|
|Gather|**没有解决/证据不足**|没有公开 Indexed Gather DMA、KV Page Translator 或按 Top-k 输出直接生成 Gather descriptor。[CS-4 产品页](https://www.cerebras.ai/cs4)（访问日期：2026-08-22）|
|跨卡通信|**直接改善系统互联，间接帮助附件**|CS-4 提供 2.4 Tb/s/片、7.2 Tb/s/系统 I/O 和最低 2 μs 晶圆间延迟；但这不是 Top-k collective 的证明。[官方新闻稿](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions)（访问日期：2026-08-22）|
|TPOT / TTFT / Tokens / J|**TPOT 间接帮助；TTFT 公开未确认；Tokens/J 仅有系统级方向**|官方给出 GPT-OSS-120B 条件下超过 4,400 tokens/s/user、最高 30× GPU 的宣传口径，CS-4 还称最高 10× CS-3 吞吐/W；这些不是附件 Indexer 的端到端 TPOT、TTFT 或 Tokens/J 测量。[官方新闻稿](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions)（访问日期：2026-08-22）|

## 创新性判断

以下是“架构研究价值”分析判断，不是 benchmark，总分 **80/100**。分数高的原因是它在数据移动、片上互联和系统级扩展上有清晰公开证据；扣分来自 Retrieval Plane 的关键原语没有公开确认。

|维度|权重|得分|分析判断|
|---|---:|---:|---|
|数据搬运与存储|30%|27|44GB 分布式 SRAM、43.2 PB/s 带宽和晶圆内 fabric 直击内存墙，但没有离散 Gather 证据。[CS-4 数据表](https://cdn.sanity.io/files/e4qjo92p/production/bb028ae2422089dfbcc9fd2455c021f3625c7a75.pdf)（访问日期：2026-08-22）|
|执行架构|20%|16|细粒度 dataflow core 和晶圆级并行很有价值，WSE-3T 的新执行单元细节公开较少。[官方白皮书目录](https://www.cerebras.ai/whitepapers)（访问日期：2026-08-22）|
|稀疏/动态计算|15%|8|官方计算口径是 sparse FP16，公开资料也强调非结构化稀疏；动态 Indexer/动态 Top-k 未确认。[官方白皮书目录](https://www.cerebras.ai/whitepapers)（访问日期：2026-08-22）|
|Scale-up/互联|15%|14|Direct Wafer Links、可编程 I/O、2 μs 延迟是 CS-4 的强项，仍需真实大模型扩展数据。[CS-4 新闻稿](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions)（访问日期：2026-08-22）|
|数值格式/计算密度|10%|8|5nm、250 PFLOPS/片的密度高；WSE-3T 专属低精度格式与能效绝对值不足。[CS-4 数据表](https://cdn.sanity.io/files/e4qjo92p/production/bb028ae2422089dfbcc9fd2455c021f3625c7a75.pdf)（访问日期：2026-08-22）|
|可编程性|10%|7|可编程 I/O、编译器和 dataflow 方向有基础，但没有附件所需的 Top-k/Gather 原语接口。[CS-4 介绍](https://www.cerebras.ai/blog/introducing-cerebras-cs-4)（访问日期：2026-08-22）|

## 局限与常见误解

1. **官方宣传数字不等于端到端推理速度。** “最高 30×”和“超过 4,400 tokens/s/user”绑定特定模型、提示和配置；官方也说明结果会随模型、上下文、精度和 serving 配置变化。它不能替代 TPOT、TTFT、P95 和 Tokens/J 的同负载实测。[官方新闻稿](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions)（访问日期：2026-08-22）
2. **WSE-3T 不等于 CS-4。** 前者是单片晶圆处理器，后者还承担三片晶圆之间的 I/O、供电、液冷、控制和机架部署。把 250 PFLOPS 直接当成一台服务的实际吞吐，会跨越芯片与系统边界。[CS-4 数据表](https://cdn.sanity.io/files/e4qjo92p/production/bb028ae2422089dfbcc9fd2455c021f3625c7a75.pdf)（访问日期：2026-08-22）
3. **片上 SRAM 不等于全量 KV Cache。** 44GB 是容量，不是索引结构；长上下文的 KV layout、分页、溢出路径和随机 Gather 代价，CS-4 公开资料没有给出完整答案。[CS-4 数据表](https://cdn.sanity.io/files/e4qjo92p/production/bb028ae2422089dfbcc9fd2455c021f3625c7a75.pdf)（访问日期：2026-08-22）
4. **冗余绕坏点不等于运行时容错。** fail-in-place 主要回答晶圆制造良率；它没有证明能在请求级别绕开热点、拥塞或错误的 KV 地址。[官方制造说明](https://www.cerebras.ai/blog/100x-defect-tolerance-how-cerebras-solved-the-yield-problem)（访问日期：2026-08-22）
5. **首批出货不等于普遍可用。** 截止日能确认的是 CS-4 已宣布，官方写首批出货在 2026 年第三季度开始；量产规模、客户可购买性和云服务覆盖仍属公开资料未确认。[CS-4 产品页](https://www.cerebras.ai/cs4)（访问日期：2026-08-22）

## 对下一代 Retrieval GPU 的可借鉴点

### 可直接借鉴

1. 把高频中间结果放到靠近计算单元的显式片上 SRAM，并为 partial score、索引元数据和 DMA descriptor 预留带宽。借鉴的是数据位置原则，Top-k/Gather 仍需自行设计和验证。
2. 把片上 fabric、片外 I/O 和通信协议分层，给跨卡候选合并留出低延迟、可编程通道。CS-4 的 Wafer I/O、RoCE v2 和 Direct Wafer Links提供了系统级先例。[官方 CS-4 介绍](https://www.cerebras.ai/blog/introducing-cerebras-cs-4)（访问日期：2026-08-22）

### 只能类比

3. “一片大晶圆加多晶圆低延迟连接”可以类比附件的 Tensor Plane 与 Retrieval Plane 协同，但 CS-4 的互联目标是通用系统扩展，不能直接当作 candidate-parallel Local/Global Top-k 方案。

### 不宜照搬

4. 不宜把 44GB SRAM 当成完整 KV 仓库。Retrieval GPU 仍需明确容量层次、page table、离散地址生成、Gather 合并和溢出路径。
5. 不宜把 fail-in-place 直接当作检索路由设计。制造缺陷是静态拓扑问题，动态检索是请求相关的数据流问题，两者的判断指标不同。

## 参考来源

1. [Cerebras Unveils CS-4: Up to 30 Times Faster than GPU-based Solutions](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions)，官方新闻稿，2026-08-18 宣布 WSE-3T 与 CS-4，访问日期 2026-08-22。
2. [Meet CS-4 数据表](https://cdn.sanity.io/files/e4qjo92p/production/bb028ae2422089dfbcc9fd2455c021f3625c7a75.pdf)，官方 PDF，含 WSE-3T/CS-4 核心规格，访问日期 2026-08-22。
3. [Introducing Cerebras CS-4](https://www.cerebras.ai/blog/introducing-cerebras-cs-4)，官方博客，2026-08-18，含 Nexus、backpack、供电与异构推理说明，访问日期 2026-08-22。
4. [Cerebras CS-4 产品页](https://www.cerebras.ai/cs4)，官方产品页，含三片 WSE-3T、2 μs、首批出货状态，访问日期 2026-08-22。
5. [100x Defect Tolerance](https://www.cerebras.ai/blog/100x-defect-tolerance-how-cerebras-solved-the-yield-problem)，官方技术博客，2025-01-13，含小核心、冗余路由、备用核心和 fail-in-place，访问日期 2026-08-22。
6. [Cerebras Whitepapers](https://www.cerebras.ai/whitepapers)，官方白皮书目录，2025-10-17 条目说明 dataflow core、分布式 SRAM 与片上/片外互联，访问日期 2026-08-22。
7. [Cerebras is coming to AWS](https://www.cerebras.ai/blog/cerebras-is-coming-to-aws)，官方博客，2026-03-13，CS-3/AWS Bedrock 与 prefill/decode 分离更新，访问日期 2026-08-22。
8. [Cerebras Wafer-Scale Cluster 文档](https://training-api.cerebras.ai/en/latest/wsc/Concepts/how-cerebras-works.html)，官方开发者文档，说明 CS-3、MemoryX、SwarmX 与集群边界，访问日期 2026-08-22。

> 证据边界：本文把官方明确给出的规格、发布日期和状态与分析判断分开。官方没有给出 WSE-3T 的专用 Search、Top-k、KV Page Translator、Indexed Gather DMA、绝对功耗、TTFT 或量产规模时，均保留为“公开资料未确认”。
