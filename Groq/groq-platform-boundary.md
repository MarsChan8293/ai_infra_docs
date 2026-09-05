# Groq — Groq 3 LPX、GroqCloud 与 Vera Rubin（边界文件，非单芯片）

- 拆分日期：2026-09-02
- 产品层级：托盘/机架/云服务（非芯片）
- 综合报告：[07-groq-lpu.md](./07-groq-lpu.md)
- 文件性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容逐行摘录综合报告，保留原报告中的状态、数字、证据等级和未知项。

> 第 2 行：
> 第 3 行：> 研究窗口：2025-07-01 至 2026-08-22｜资料访问日：2026-08-22｜对象：Groq｜口径：只研究 Groq；NVIDIA 资料仅用于核验授权与 Vera Rubin 集成边界。
> 第 4 行：
> 第 6 行：
> 第 7 行：截至 2026-08-22，公开资料中最新、命名最清楚的目标是 **Groq 3 LPU，芯片代号 LP30**，但它公开呈现为 NVIDIA Vera Rubin 体系里的 **Groq 3 LPX 机架级推理加速器**，不是一张已经独立上市的 Groq 单卡。它要解决的是解码阶段每个 token 的低延迟、抖动和数据搬运问题；最值得研究的创新是把 SRAM、显式数据移动、编译器静态调度和芯片间同步组合成一个可预测的空间数据流系统。[NVIDIA 技术博客](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)
> 第 8 行：
> 第 14 行：|---|---|---|
> 第 15 行：| 芯片 | Groq 3 LPU / LP30 | 不是 GroqCloud 服务，也不是整套 Vera Rubin |
> 第 16 行：| 托盘 | 每托盘 [8 颗 LP30](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，另有主机处理器与 fabric expansion logic | 不是单颗芯片规格 |
> 第 17 行：| 机架 | Groq 3 LPX：[32 个 1U 托盘、256 颗 LPU](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | 不是 Groq 旧式 GroqRack 的同义词 |
> 第 18 行：| 平台 | LPX 与 Vera Rubin NVL72 协同，LPX 偏低延迟解码，Rubin GPU 负责长上下文 prefill 与 decode attention | 仅为授权/集成边界，不展开 NVIDIA 其他产品研究 |
> 第 19 行：| 云服务 | GroqCloud 是 Groq 独立运营的 API/云服务。授权公告明确写明 Groq 继续独立运营、GroqCloud 不间断；截至窗口末，未见证据证明 GroqCloud 的在线请求已经由 LP30 规模承载。[Groq 公告](https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale) |
> 第 20 行：
> 第 22 行：
> 第 23 行：- **时间边界**：Groq 第一代 LPU 于 [2019 年](https://home.cloud.groq.io/blog/inside-the-lpu-deconstructing-groq-speed)推出，窗口开始前已经进入 GroqCloud 和生产基础设施；不能把它写成窗口内首发。Groq 在 2025-08-01 的官方文章仍把它称为第一代、14 nm 芯片，并未给出 Groq 3/LP30 名称。
> 第 24 行：- **宣布/命名**：2026-03-16，按本次核验到的公开一手资料，NVIDIA 官方发布 Vera Rubin 时首次明确写出 “NVIDIA Groq 3 LPU”；同日技术博客给出 LP30 规格。[新闻稿](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform) [技术博客](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)
> 第 25 行：- **量产口径**：同一新闻稿称七颗新芯片 “full production”；但新闻稿同时写 LPX 将于 2026 年下半年可用，2026-05-31 的后续公告又写 Vera Rubin 生产出货从“今年秋季”开始。[后续公告](https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory) 因此采用保守表述：**设计已公开，官方称已进入量产/生产爬坡；截至 2026-08-22，LP30/LPX 的 GA、客户可购与规模部署未被官方明确确认**。
> 第 26 行：- **Groq 侧状态**：Groq 2026-06-22 说将用包括 NVIDIA 新 LPX 在内的最新推理技术改造现有云 footprint；2026-08-12 成为 NVIDIA Cloud Partner，说明集成路径已正式化，但仍不是 LP30 已在 GroqCloud 线上规模运行的证据。[Groq 2026-06-22](https://groq.com/newsroom/groq-raises-usd650m-to-scale-its-ai-inference-cloud-business) [Groq 2026-08-12](https://groq.com/newsroom/groq-becomes-an-nvidia-cloud-partner)
> 第 27 行：
> 第 33 行：| 执行单元 | MXM 矩阵执行、VXM 向量执行、SXM 数据交换；统一工作粒度为 [320-byte vector](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | 各单元数量、频率、面积未公开确认；按 [8 颗](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) 托盘的 [9.6 PFLOPS](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) 推得约 [1.2 PFLOPS FP8/颗](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，这是推导值 |
> 第 34 行：| 数值格式 | 公开的 LPU 方案包括 TruePoint 的 [100-bit 中间累加](https://home.cloud.groq.io/blog/inside-the-lpu-deconstructing-groq-speed)、FP32 attention logits、MoE 权重的 block floating point、FP8 activation；LPX 机架标注 FP8 inference compute | LP30 完整格式/吞吐表未公开确认 |
> 第 35 行：| 片上内存 | 每颗 [500 MB SRAM](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，作为主要工作存储而非传统 cache | 容量有限，不能等同于整机模型容量 |
> 第 36 行：| 片外内存 | LPX 机架另有 [12 TB DDR5](https://www.nvidia.com/en-au/data-center/lpx/)，托盘侧公开为 fabric expansion logic 最多 [256 GB](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)、主机最多 [128 GB](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | “SRAM-first”不等于整架没有片外内存；LP30 本身没有公开 HBM 规格 |
> 第 37 行：| 带宽 | 单颗 SRAM [150 TB/s](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，单托盘 [1.2 PB/s](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，整架 [40 PB/s](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | 这些是峰值/聚合口径，不是某个模型的有效 KV 带宽 |
> 第 38 行：| 互联 | 每颗 [96 条 C2C link、112 Gbps/link、双向聚合 2.5 TB/s](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)；整架 [640 TB/s scale-up](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)、[256 芯片](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | LPX 还有 C2C spine 与 fabric logic，不能简单复述为“完全没有系统级互联逻辑” |
> 第 39 行：| 功耗/散热 | **LP30 单芯片功耗公开资料未确认**；LPX 公开为全液冷 | Groq 旧 GroqChip 的 [300 W max/215 W TDP/185 W average](https://www.groq.com/GroqDocs/Product%20Spec%20Sheet%20-%20GroqChip%E2%84%A2%20Processor.pdf) 不能移植给 LP30，仅作时间边界 |
> 第 40 行：
> 第 60 行：|---|---|---|---|
> 第 61 行：| 密集计算 | MXM、FP8 与 SRAM 直接服务 dense FFN/MoE decode；LPX 的公开定位就是低延迟解码路径 | 编译器把矩阵、向量、传输排成流水 | 不证明对稀疏 KV 检索同样有效 |
> 第 62 行：| Search / Indexer | — | MXM/VXM 可承载点积和扫描，静态数据流可减少 launch/调度开销 | 没有公开 Search/Indexer 专用单元或 exact retrieval 结果 |
> 第 66 行：| 跨卡通信 | 直接解决通信时序与带宽的一部分：C2C、plesiosynchronous 协议、编译器调度和大规模同步 | 可把多芯片 pipeline 做成稳定 token 流 | 不等于跨卡 Top-k merge，也不自动减少检索候选数 |
> 第 67 行：| TPOT / TTFT / Tokens / J | 直接针对低抖动 per-token latency；官方把 LPX 定位为交互式解码 | SRAM、静态调度和流水线可能降低等待与能耗 | 公开的是机架级/预测性指标；LP30 的实测 TPOT、TTFT、Tokens/J 未确认，不能把 [1,000 tokens/sec/user](https://groq.com/platform) 当成通用 benchmark |
> 第 68 行：
> 第 88 行：3. **Groq 3 不等于旧 GroqChip 规格升级版的简单换名。** [14 nm、230 MB、80 TB/s、215 W TDP](https://www.groq.com/GroqDocs/Product%20Spec%20Sheet%20-%20GroqChip%E2%84%A2%20Processor.pdf) 是旧公开产品值，不能推导 LP30 的制程和功耗。
> 第 89 行：4. **LPX 不等于 GroqCloud。** LPX 是 NVIDIA Vera Rubin 侧的机架产品；GroqCloud 是 Groq 独立运营的服务。到截止日，LP30 在 GroqCloud 的规模上线公开证据不足。
> 第 90 行：5. **高带宽不等于 Retrieval Plane。** 没有公开 TOPK、page map、indexed gather，就不能把 Groq 的数据流互联直接写成附件方案已经实现。
> 第 102 行：- SXM 的 permutation/route 只能类比 Address/Route；它不是公开的 page-aware indexed gather。
> 第 103 行：- LPX 的 dense decode 与低延迟路径分工可以类比 Tensor Plane + Retrieval Plane，但 Groq 资料没有证明它有 Retrieval Plane。
> 第 104 行：- Groq 对 MoE 的跨芯片共享资源 fabric 可以类比 candidate-sharding，却不能代替 exact Top-k 的正确性和通信量实验。
> 第 109 行：- 不要把所有动态检索都静态编译；要保留可编程 TOPK、MERGE、GATHER、PAGE-TRANSLATE 和异常路径。
> 第 110 行：- 不要把 320-byte 固定向量或 LPX 的 [35×/MW](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) 预测性系统指标当作检索收益。第一验证仍应是附件要求的 exact local Top-k merge，并测 TPOT、HBM bytes/token、跨卡 bytes/token、Tokens/J 和召回/一致性。
> 第 111 行：
> 第 117 行：4. [Groq：GroqChip Processor Product Brief](https://www.groq.com/GroqDocs/Product%20Spec%20Sheet%20-%20GroqChip%E2%84%A2%20Processor.pdf)（旧一代规格，仅作时间边界；访问日 2026-08-22）。
> 第 118 行：5. [Groq：与 NVIDIA 的非排他推理技术授权公告（2025-12-24）](https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale)（独立运营与 GroqCloud 连续性；访问日 2026-08-22）。
> 第 119 行：6. [NVIDIA：Vera Rubin Opens Agentic AI Frontier（2026-03-16）](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform)（Groq 3 命名、LPX 集成与可用时间；访问日 2026-08-22）。
> 第 120 行：7. [NVIDIA：Inside NVIDIA Groq 3 LPX（2026-03-16）](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)（LP30、托盘、机架和互联详细规格；访问日 2026-08-22）。
> 第 121 行：8. [NVIDIA：Vera Rubin Ramps Into Full Production（2026-05-31）](https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory)（量产爬坡与出货时间冲突口径；访问日 2026-08-22）。
> 第 122 行：9. [Groq：GroqCloud Expanding to Meet Demand（2026-02-16）](https://groq.com/blog/groqcloud-expanding-to-meet-demand)（GroqCloud 独立扩张与现有 LPU 生产服务；访问日 2026-08-22）。
> 第 123 行：10. [Groq：Groq Raises $650M（2026-06-22）](https://groq.com/newsroom/groq-raises-usd650m-to-scale-its-ai-inference-cloud-business)（Groq 计划将 NVIDIA LPX 纳入 footprint；访问日 2026-08-22）。
> 第 124 行：
> 第 125 行：> 证据边界：截至 2026-08-22，未找到 Groq 自己发布的 LP30 完整 datasheet，亦未找到可确认 LP30 已在 GroqCloud 规模部署的官方记录；制程、单芯片功耗、TOPK/Gather 专用硬件和实测 Tokens/J 均应保留为“公开资料未确认”。
> 第 126 行：+## 2026-09-01 在线复核增补
> 第 127 行：
> 第 128 行：已重新打开 [Groq 3 LPX 官方公告](https://groq.com/blog/groq-among-the-first-to-bring-nvidia-groq-3-lpx-and-vera-rubin-nvl72-to-market) 与 [Groq Cloud 平台页](https://groq.com/platform)，确认 2026-08-24 公告将 LPX/Vera Rubin NVL72描述为计划部署并接入推理云；平台页把 256 LPU、40PB/s SRAM 带宽等标为机架级口径，不能写成单芯片规格。

## 直接来源链接

1. <https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)>
2. <https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，另有主机处理器与>
3. <https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale)>
4. <https://home.cloud.groq.io/blog/inside-the-lpu-deconstructing-groq-speed)推出，窗口开始前已经进入>
5. <https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform)>
6. <https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory)>
7. <https://groq.com/newsroom/groq-raises-usd650m-to-scale-its-ai-inference-cloud-business)>
8. <https://groq.com/newsroom/groq-becomes-an-nvidia-cloud-partner)>
9. <https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，这是推导值>
10. <https://home.cloud.groq.io/blog/inside-the-lpu-deconstructing-groq-speed)、FP32>
11. <https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，作为主要工作存储而非传统>
12. <https://www.nvidia.com/en-au/data-center/lpx/)，托盘侧公开为>
13. <https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)、主机最多>
14. <https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，单托盘>
15. <https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，整架>
16. <https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)；整架>
17. <https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)、[256>
18. <https://www.groq.com/GroqDocs/Product%20Spec%20Sheet%20-%20GroqChip%E2%84%A2%20Processor.pdf)>
19. <https://groq.com/platform)>
20. <https://www.groq.com/GroqDocs/Product%20Spec%20Sheet%20-%20GroqChip%E2%84%A2%20Processor.pdf)（旧一代规格，仅作时间边界；访问日>
21. <https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale)（独立运营与>
22. <https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform)（Groq>
23. <https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)（LP30、托盘、机架和互联详细规格；访问日>
24. <https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory)（量产爬坡与出货时间冲突口径；访问日>
25. <https://groq.com/blog/groqcloud-expanding-to-meet-demand)（GroqCloud>
26. <https://groq.com/newsroom/groq-raises-usd650m-to-scale-its-ai-inference-cloud-business)（Groq>
27. <https://groq.com/blog/groq-among-the-first-to-bring-nvidia-groq-3-lpx-and-vera-rubin-nvl72-to-market)>
28. <https://groq.com/platform)，确认>

## 证据边界

- 这是资料重排页，不是重新发布或重新核验的产品公告。
- “发布、流片、送样、量产、出货、客户部署、云端可用、路线图、停产”等状态只在综合报告明确写出时保留；缺失项仍为“公开资料未确认”。
- 若摘录同时出现芯片、板卡、服务器、机架或云服务，均按原报告层级保留，并以“产品层级”字段提醒，不做跨层级推导。

## 关联表格原文（完整表格）

以下表格块来自综合报告中与本拆分项命中的表格，完整保留表头、状态列和规格列。

> 来源综合报告第 13-19 行：
> 第 13 行：| 层级 | 本文研究对象 | 不能混称的对象 |
> 第 14 行：|---|---|---|
> 第 15 行：| 芯片 | Groq 3 LPU / LP30 | 不是 GroqCloud 服务，也不是整套 Vera Rubin |
> 第 16 行：| 托盘 | 每托盘 [8 颗 LP30](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，另有主机处理器与 fabric expansion logic | 不是单颗芯片规格 |
> 第 17 行：| 机架 | Groq 3 LPX：[32 个 1U 托盘、256 颗 LPU](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | 不是 Groq 旧式 GroqRack 的同义词 |
> 第 18 行：| 平台 | LPX 与 Vera Rubin NVL72 协同，LPX 偏低延迟解码，Rubin GPU 负责长上下文 prefill 与 decode attention | 仅为授权/集成边界，不展开 NVIDIA 其他产品研究 |
> 第 19 行：| 云服务 | GroqCloud 是 Groq 独立运营的 API/云服务。授权公告明确写明 Groq 继续独立运营、GroqCloud 不间断；截至窗口末，未见证据证明 GroqCloud 的在线请求已经由 LP30 规模承载。[Groq 公告](https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale) |

> 来源综合报告第 30-39 行：
> 第 30 行：| 项目 | Groq 3 / LP30 公开口径 | 研究边界 |
> 第 31 行：|---|---|---|
> 第 32 行：| 制程 | **公开资料未确认**。Groq 只公开说现有/第一代芯片为 [14 nm](https://groq.com/blog/the-groq-lpu-explained)，并说未来向 [4 nm](https://groq.com/blog/the-groq-lpu-explained) 发展 | 不能把 14 nm 或 4 nm 直接套到 LP30 |
> 第 33 行：| 执行单元 | MXM 矩阵执行、VXM 向量执行、SXM 数据交换；统一工作粒度为 [320-byte vector](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | 各单元数量、频率、面积未公开确认；按 [8 颗](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) 托盘的 [9.6 PFLOPS](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) 推得约 [1.2 PFLOPS FP8/颗](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，这是推导值 |
> 第 34 行：| 数值格式 | 公开的 LPU 方案包括 TruePoint 的 [100-bit 中间累加](https://home.cloud.groq.io/blog/inside-the-lpu-deconstructing-groq-speed)、FP32 attention logits、MoE 权重的 block floating point、FP8 activation；LPX 机架标注 FP8 inference compute | LP30 完整格式/吞吐表未公开确认 |
> 第 35 行：| 片上内存 | 每颗 [500 MB SRAM](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，作为主要工作存储而非传统 cache | 容量有限，不能等同于整机模型容量 |
> 第 36 行：| 片外内存 | LPX 机架另有 [12 TB DDR5](https://www.nvidia.com/en-au/data-center/lpx/)，托盘侧公开为 fabric expansion logic 最多 [256 GB](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)、主机最多 [128 GB](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | “SRAM-first”不等于整架没有片外内存；LP30 本身没有公开 HBM 规格 |
> 第 37 行：| 带宽 | 单颗 SRAM [150 TB/s](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，单托盘 [1.2 PB/s](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，整架 [40 PB/s](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | 这些是峰值/聚合口径，不是某个模型的有效 KV 带宽 |
> 第 38 行：| 互联 | 每颗 [96 条 C2C link、112 Gbps/link、双向聚合 2.5 TB/s](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)；整架 [640 TB/s scale-up](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)、[256 芯片](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | LPX 还有 C2C spine 与 fabric logic，不能简单复述为“完全没有系统级互联逻辑” |
> 第 39 行：| 功耗/散热 | **LP30 单芯片功耗公开资料未确认**；LPX 公开为全液冷 | Groq 旧 GroqChip 的 [300 W max/215 W TDP/185 W average](https://www.groq.com/GroqDocs/Product%20Spec%20Sheet%20-%20GroqChip%E2%84%A2%20Processor.pdf) 不能移植给 LP30，仅作时间边界 |

> 来源综合报告第 59-67 行：
> 第 59 行：| 附件概念 | 直接解决 | 间接帮助 | 没有解决或证据不足 |
> 第 60 行：|---|---|---|---|
> 第 61 行：| 密集计算 | MXM、FP8 与 SRAM 直接服务 dense FFN/MoE decode；LPX 的公开定位就是低延迟解码路径 | 编译器把矩阵、向量、传输排成流水 | 不证明对稀疏 KV 检索同样有效 |
> 第 62 行：| Search / Indexer | — | MXM/VXM 可承载点积和扫描，静态数据流可减少 launch/调度开销 | 没有公开 Search/Indexer 专用单元或 exact retrieval 结果 |
> 第 63 行：| Top-k / Reduce | — | VXM 与显式数据流可以实现固定规约 | 没有公开 TOPK、MERGE_TOPK 或 streaming reduction 原语 |
> 第 64 行：| 离散 KV Gather | — | SRAM 与 SXM 的结构化搬运有利于规则化的数据交换 | 没有公开 indexed gather DMA、page table translator 或离散 KV 语义 |
> 第 65 行：| Address / Route | — | SXM 支持 permutation/rotation/distribution/transpose，编译器能显式安排路由 | 没有证据表明它能硬件生成动态物理地址或 page-aware route |
> 第 66 行：| 跨卡通信 | 直接解决通信时序与带宽的一部分：C2C、plesiosynchronous 协议、编译器调度和大规模同步 | 可把多芯片 pipeline 做成稳定 token 流 | 不等于跨卡 Top-k merge，也不自动减少检索候选数 |
> 第 67 行：| TPOT / TTFT / Tokens / J | 直接针对低抖动 per-token latency；官方把 LPX 定位为交互式解码 | SRAM、静态调度和流水线可能降低等待与能耗 | 公开的是机架级/预测性指标；LP30 的实测 TPOT、TTFT、Tokens/J 未确认，不能把 [1,000 tokens/sec/user](https://groq.com/platform) 当成通用 benchmark |

## 补充直接来源链接

1. <https://groq.com/blog/the-groq-lpu-explained)，并说未来向>
2. <https://groq.com/blog/the-groq-lpu-explained)>
