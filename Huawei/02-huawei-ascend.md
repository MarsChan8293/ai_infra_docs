# 厂商与芯片：华为昇腾 Ascend 950 系列（2025-06 之后最新款）

> 研究范围：华为昇腾，资料窗口为 2025-07-01 至 2026-08-22。资料访问日期统一为 2026-08-22。对照基线为附件《推导推理GPU新路径-ELI5.html》（当前目录未提供）。

## 一句话结论

950 系列最值得研究的地方，是把向量执行、细粒度缓存访问、异步搬运和集合通信放进同一套硬件与编程模型里。它已经靠近附件提出的 Search、Move、Route、Address 路径，尤其适合离散访存与跨卡通信；公开资料仍没有证明它内置独立的 Retrieval Core、精确 Top-k 引擎或 page-aware KV Gather DMA。因此，它更像 Retrieval GPU 的底层零件集合，尚未等于附件里的完整 Retrieval Plane。这是基于公开白皮书的架构判断，并非 benchmark。[昇腾 950 NPU 架构白皮书](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)（资料可获得，访问 2026-08-22）

附件的四类关键问题可以压缩成四句话。密集计算需要 Cube Core 处理规则矩阵；动态检索需要运行时找位置；Top-k/Reduce 要尽早筛选并减少中间分数；离散 KV Gather 还要解决地址生成、数据搬运和跨卡通信。附件的目标是降低 score materialization、跨卡全量汇总和无效 KV 搬运，同时看 TPOT、TTFT、Tokens/J，而不是只看峰值 FLOPS。

## 目标芯片与时间状态

2025-09-18，华为宣布 Ascend 950PR 与 950DT 共用 Ascend 950 Die，分别面向 Prefill/推荐与 Decode/训练；同一份路线图把 950PR 放在 2026 年第一季度，把 950DT 放在 2026 年第四季度。Ascend 960、970 的规划时间分别是 2027、2028，超出本研究窗口，因此本报告把 950PR/950DT 视为窗口内最新公开芯片系列，不把规划中的后续型号当作已发布芯片。[华为 2025 路线图演讲](https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech)（宣布 2025-09-18，访问 2026-08-22）

| 对象 | 发布、宣布、可用状态 | 芯片与系统边界 |
|---|---|---|
| Ascend 950PR | 2025-09-18 宣布；2026-03-20 宣布搭载它的 Atlas 350 加速卡正式上市，950 代际推理算力进入商用阶段，可视为本窗口内已可获得的 PR 产品 | 950PR 是芯片；Atlas 350 是带 PCIe、HBM、灵衢端口、散热和功耗约束的加速卡 |
| Ascend 950DT | 2025-09-18 宣布，官方路线图为 2026 年第四季度推出；2026-07-17 Atlas 950 SuperPoD 实机公开展示，白皮书和产品页已公开规格；截至截止日，芯片量产/普遍可采购状态为“公开资料未确认” | 950DT 是芯片；Atlas 950 SuperPoD 是多卡、多柜、互联柜、CPU、DDR、供电和液冷组成的系统 |
| Atlas 950 SuperPoD | 2025-09-18 宣布，2026-03-02 海外发布，2026-07-17 公开实机；这是系统可见性，不等于 950DT 已普遍供货 | 当前官方产品页与 WAIC 页面采用 1024 卡展示配置，不能直接替代芯片规格 |

状态依据为[昇腾伙伴峰会 2026](https://www.hiascend.com/activities/dynamic-news/20260320-3)（上市 2026-03-20，访问 2026-08-22）、[华为 MWC 2026 发布](https://www.huawei.com/cn/news/2026/3/mwc-superpod-ai)（发布 2026-03-02，访问 2026-08-22）和[WAIC 950 超节点实机信息](https://www.huawei.com/cn/news/2026/7/atlas-950-superpod)（公开展示 2026-07-17，访问 2026-08-22）。

## 核心规格表

| 项目 | Ascend 950PR | Ascend 950DT |
|---|---|---|
| 制程 | 具体 nm/工艺节点未公开；白皮书只称自主可控制造工艺 | 同左，公开资料未确认具体节点 |
| 计算单元 | 完整架构最多 36 个 AI 子系统，每个含 1 个 Cube Core 和 2 个 Vector Core；量产/产品变体为 32/28 Cube、64/56 Vector | 完整架构同为 36 个 AI 子系统；变体为 36/32/28 Cube、72/64/56 Vector |
| 峰值格式 | MXFP4 1784/1561 TFLOPS；HiF8/MXFP8/FP8 919/804 TFLOPS；BF16/FP16 486/425 TFLOPS | MXFP4 2007/1784/1561 TFLOPS；HiF8/MXFP8/FP8 1034/919/804 TFLOPS；BF16/FP16 547/486/425 TFLOPS |
| 数值格式 | TF32、FP16、BF16、FP8、MXFP8、HiF8、INT8、MXFP4 等 | 同系列格式；官方路线图明确用于 Decode 与训练 |
| 主内存 | 华为新闻稿称 HiBL 1.0 HBM；白皮书称高速片上内存，最高 128GB、1.6TB/s，产品变体 112GB、1.4TB/s | HiZQ 2.0，最高 144GB、4TB/s；白皮书列出 144/96GB 变体 |
| Cache 与粒度 | 128MB 统一 L2；512B cache line，四个 128B sector；官方新闻稿把访存颗粒度从 512B 说到 128B | 同样的 128MB L2 与 128B sector 机制 |
| 互联 | Unified Bus 2.0，18 个 x4 Port、112Gbps、2016GB/s 双向；PCIe 5.0 x16，128GB/s 双向；支持 URMA、UB Memory、UBoE、CCU | 同一 IO/互联规格，芯片级带宽不因 P/D 定位改变 |
| 功耗 | 芯片 TDP 未公开；Atlas 350 卡最大功耗 ≤600W | 芯片 TDP 未公开；Atlas 950 SuperPoD 产品页给出系统供电 100kW，不能回填成单芯片功耗 |

规格依据为[昇腾 950 白皮书第 9 至 14 页](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)（资料可获得，访问 2026-08-22）、[Atlas 350 产品页](https://www.hiascend.com/hardware/accelerator-card)（可用卡规格，访问 2026-08-22）和[Atlas 950 SuperPoD 产品页](https://www.hiascend.com/hardware/cluster)（系统规格，访问 2026-08-22）。白皮书还说明 PR 合封 8 个高速内存模块，DT 合封 4 个，属于封装与内存配置差异，不应把 112GB 卡规格和 144GB 芯片最高规格混写。

## ELI5 核心特性

把长上下文想成一间很大的仓库。Cube Core 像流水线厨房，擅长整齐的大盘矩阵；Vector Core 像能逐件检查货物的工作台。SIMD 是传送带，一条指令同时处理一批规则数据；SIMT 是一组可以各自拿不同地址的工人，适合分支、Gather/Scatter 和 Hash 一类不规则动作。950 的公开白皮书明确把 SIMD 作为主力，把 SIMT 作为离散访问和复杂控制流的补充，并允许一个 Vector Function 在两种模式间选择。[白皮书第 19 至 21 页](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)（访问 2026-08-22）

第二个变化是搬货方式。NDDMA 可以在 Kernel 中完成最多 5 维数据搬运、转置和排布转换，并硬化地址生成逻辑；L2 支持 Hint、Cache Lock、驻留和 SDMA 的预取、写回、失效、冲刷。对附件的 Search/Move/Address 路径，这些机制能减少通用线程逐元素算地址和中间数据绕路。[白皮书第 20 至 26 页](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)（访问 2026-08-22）

第三个变化是把 P/D 的内存需求分开。PR 用 HiBL 1.0 偏 Prefill 与推荐，DT 用 HiZQ 2.0 偏 Decode 与训练。类比成同一厨房配两种仓库，PR 追求并行做菜，DT 给逐 token 取料更多、更快的通道。类比边界也很重要，真实收益取决于模型布局、batch、KV page、算子融合和软件调度，不能由“有 128B sector”直接推出端到端 TPOT 下降。[华为 2025 路线图](https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech)（宣布 2025-09-18，访问 2026-08-22）

## 映射到附件方案

下表中的“直接解决、间接帮助、没有解决/证据不足”是架构研究判断，证据来自[白皮书](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)和[CANN 9.0 发布说明](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/900/releasenote/release-notes.md)，均访问于 2026-08-22。

| 附件动作 | 直接解决 | 间接帮助 | 没有解决/证据不足 |
|---|---|---|---|
| Search | 无公开的专用相似度搜索或索引单元 | Vector、SIMT、片上内存可执行搜索 Kernel | 没有公开 Indexer 数据结构或 O(L) 扫描替代机制 |
| Select | 无公开 Top-k 硬件指令 | CCU 的 Reduce/Reduce Scatter 可承接候选聚合 | 没有证据表明能直接做精确 Local/Global Top-k |
| Move | NDDMA、SDMA、URMA 提供搬运原语 | 规则 Tile 重排和异步搬运更适合融合流水 | 没有公开 page-aware、索引列表驱动的 KV Gather DMA |
| Route | UB Memory、URMA、CCU 和片上转发支持跨卡路径 | 可把候选或 KV 描述符交给通信引擎 | 没有公开 Retrieval-aware Route 或按候选价值路由 |
| Address | NDDMA 地址生成、UB Memory Decoder、URMA 的 VA/PA 转换可直接支撑地址层 | UMMU 权限检查和统一编址有利于远端取数 | 没有公开 KV page table、物理地址描述符链或持久化 Gather queue |
| score materialization | 没有公开“分数生成即筛选”的专用路径 | L2 Hint/sector、Cube-Vector 通路、STARS 调度可能减少写回 | 不能证明完整 score 一定不落 HBM，也不能证明跨卡全量 reduction 已被消除 |
| Local/Global Top-k | 无公开 Top-k/merge-top-k 单元 | CCU 支持 All Gather、Reduce Scatter、All Reduce 等通信骨架 | 这些集合通信原语不等于 Top-k 语义 |
| 离散 KV Gather | SIMT 编程模型明确覆盖 Gather/Scatter 类动作 | 128B sector 与 NDDMA 可改善部分布局和地址开销 | 访存合并、KV layout、page 映射和实际延迟均未公开确认 |
| 跨卡通信 | UB2.0、URMA、UB Memory、CCU 可硬件卸载通信与规约 | 18 个 x4 Port、最高 2016GB/s 双向和片上转发降低通信路径压力 | 没有针对附件 candidate-sharding 的通信量、精确性和尾延迟数据 |
| TPOT/TTFT/Tokens/J | 无公开的端到端指标硬件保证 | P/D 专用化、内存带宽和低延迟互联对应这些指标的潜在瓶颈 | 未公开附件 workload 的独立 TPOT、TTFT、Tokens/J 或每 token 能耗测试 |

## 创新性评分

以下是“架构研究价值”分析判断，不是 benchmark，也不是实测排名。

| 维度 | 权重 | 得分 | 理由 |
|---|---:|---:|---|
| 数据搬运与存储 | 30% | 25 | 128B sector、128MB L2、NDDMA、L2 Hint/CMO、HiBL/HiZQ 都直击数据路径；缺少专用 KV Gather，扣分 |
| 执行架构 | 20% | 17 | SIMD 主力加 SIMT 补充、Cube-Vector 直通和 STARS2.0 使规则与不规则任务可共存 |
| 稀疏/动态计算 | 15% | 8 | SIMT 覆盖 Gather/Scatter 和分支，仍没有公开 Search、Top-k、动态索引硬件 |
| Scale-up/互联 | 15% | 14 | UB2.0、URMA、UB Memory、CCU、片上转发和 8192 卡路线图很强，但附件 workload 尚无实测 |
| 数值格式/计算密度 | 10% | 9 | MXFP4、MXFP8、HiF8 与 Cube 峰值提升有公开规格 |
| 可编程性 | 10% | 9 | SIMD/SIMT、Register 编程、NDDMA 和 CANN 支持较完整，软件对 Retrieval GPU 的成熟度仍未知 |
| **总分** | **100%** | **82** | 对“计算平面加数据流平面”的启发价值高，对完整 Retrieval GPU 的直接完成度中等 |

## 资料冲突、局限与常见误解

1. 2025 年路线图把 Atlas 950 SuperPoD 宣布为最高 8192 卡，并给出 1152TB、16.3PB/s 等路线图口径；2026 年产品页和 WAIC 实机页采用 1024 卡、256TB、1.72PB/s 或 3μs RTT 的展示/产品口径。官方页面没有解释两套数字是否对应不同阶段或配置。本文采用 2026 年产品页与 WAIC 的 1024 卡作为截止日可核验系统状态，把 8192 卡保留为已宣布路线图，不把路线图目标当作现货性能。[2025 路线图](https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech) 与[2026 产品页](https://www.hiascend.com/hardware/cluster)（访问 2026-08-22）

2. “512B 降到 128B”指向更细的访问 sector；白皮书同时明确 L2 cache line 仍为 512B、由四个 128B sector 组成。把它写成“cache line 变成 128B”会高估收益。[白皮书第 12 至 14 页](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)（访问 2026-08-22）

3. SIMD/SIMT 让不规则代码更好写、更可能跑得好，不能自动把精确搜索从 O(L) 变成 O(k)，也不能自动生成 Top-k 结果。公开 CCU 列出的能力是 Broadcast、Reduce Scatter、All Gather、All Reduce、All2All、All2Allv，未列 Top-k。[白皮书第 20 至 32 页](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)（访问 2026-08-22）

4. 峰值 TFLOPS、卡间带宽和厂商宣传的 TPS 都不等于端到端推理速度。华为公开材料没有给出附件所需模型、上下文长度、batch、Top-k 精确率、TPOT、TTFT、Tokens/J 的同一组测试条件；芯片 TDP 也未公开。当前能确认的是硬件上限和系统结构，不能补写成推理 benchmark。

## 对下一代 Retrieval GPU 的可借鉴点

1. **可直接借鉴**：保留 512B line 加 128B sector、Cache Hint/CMO 和可控驻留，让数据流软件决定哪些中间结果留下。
2. **可直接借鉴**：采用 SIMD 主路径加 SIMT 辅助路径，分别服务规则向量和离散地址/分支。
3. **可直接借鉴**：把异步搬运、远端 Load/Store、Reduce 和通信调度放到硬件队列，降低 CPU 编排介入。
4. **只能类比**：NDDMA 是规则多维搬运与重排的先例；Retrieval GPU 仍需单独设计 page-aware Indexed Gather、descriptor queue 和 Local/Global Top-k。
5. **不宜照搬**：不要因为 950 有 PR/DT 两种内存配置，就把某一模型的 P/D 分工焊死；应先用附件建议的 Exact Mode 测量 score materialization、跨卡字节数、TPOT 与 Tokens/J。

## 参考来源

1. [《昇腾 950 NPU 架构白皮书》](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)，规格、SIMD/SIMT、NDDMA、L2、CCU、互联（资料可获得，访问 2026-08-22）。
2. [华为 2025 年昇腾路线图演讲](https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech)，950PR/DT 宣布、P/D 定位、HiBL/HiZQ 与时间状态（宣布 2025-09-18，访问 2026-08-22）。
3. [Atlas 350 加速卡产品页](https://www.hiascend.com/hardware/accelerator-card)，950PR 卡级内存、带宽、互联和功耗（可用产品资料，访问 2026-08-22）。
4. [昇腾伙伴峰会 2026](https://www.hiascend.com/activities/dynamic-news/20260320-3)，Atlas 350 正式上市及商用状态（发布 2026-03-20，访问 2026-08-22）。
5. [CANN 9.0.0 发布说明](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/900/releasenote/release-notes.md)，950PR 软件支持、SIMD+SIMT 与 CCU 通信加速（可用开发者资料，访问 2026-08-22）。
6. [Atlas 950 SuperPoD 产品页](https://www.hiascend.com/hardware/cluster)，当前 1024 卡系统配置、统一内存编址、带宽和供电（可用产品资料，访问 2026-08-22）。
7. [昇腾 950 超节点 WAIC 实机信息](https://www.huawei.com/cn/news/2026/7/atlas-950-superpod)，1024 卡、256TB、1 EFLOPS FP8/2 EFLOPS FP4 的公开展示口径（公开展示 2026-07-17，访问 2026-08-22）。
