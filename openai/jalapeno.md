# OpenAI — Jalapeño

- 拆分日期：2026-09-02
- 产品层级：定制 LLM 推理加速器芯片
- 综合报告：[OpenAI_芯片与AI基础设施洞察_2026-09-02.md](./OpenAI_芯片与AI基础设施洞察_2026-09-02.md)
- 文件性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容逐行摘录综合报告，保留原报告中的状态、数字、证据等级和未知项。

> 第 6 行：
> 第 7 行：截至 2026-09-02，OpenAI 已从“主要采购并共同优化外部加速器”走到“公开确认拥有第一代自研推理芯片 Jalapeño 的工作样片和实测结果”，但仍处在工程样片/初步部署前阶段；OpenAI 的真正战略资产不是替代所有 GPU，而是把模型、kernel、serving、内存、网络、调度和数据中心做成可切换的全栈组合，用自研 ASIC 在高规模推理上取得成本、延迟和能效杠杆，同时继续依赖 NVIDIA、AMD、AWS Trainium、Cerebras、Broadcom、Microsoft、Oracle、CoreWeave 和 SoftBank 等外部体系。
> 第 8 行：
> 第 12 行：|---|---|---|---|---|
> 第 13 行：| **Jalapeño** | OpenAI 主导设计的定制 LLM 推理加速器；Broadcom、Celestica 参与工业化 | 2026-06-24 首次正式披露；九个月完成至制造 tape-out；工程样片在实验室按生产目标频率/功耗运行；2026-08-25 有初步实测结果 | 面向现代 LLM 推理；强调降低数据搬运、平衡计算/内存/网络、接近理论峰值利用率；支持 OpenAI 及外部 LLM 工作负载 | 芯片制程、晶体管数、封装、片上 SRAM/缓存容量、HBM 容量/带宽、算力峰值、互联拓扑、TDP、具体 kernel 指令集均未公开 |
> 第 14 行：| Jalapeño 后续多代平台 | OpenAI + Broadcom 的路线图 | 计划从 2026 年底开始初始部署，随后扩展多个世代；没有公开第二代型号 | 多代计算平台，配套芯片、板卡、机架、网络和生产系统 | 第二代及以后型号、制程、性能、量产节奏和实际部署量未确认 |
> 第 15 行：| 10GW OpenAI-designed accelerators | OpenAI 设计、Broadcom 合作开发和部署 | 2025-10-13 宣布；目标 2026 下半年开始部署、2029 年底完成 | 加速器与 Ethernet scale-up/scale-out 网络系统；规模用功率而非芯片数量表述 | 10GW 是否全部由 Jalapeño 或其后代构成、每瓦对应多少芯片、实际出货/上架数量均未确认 |
> 第 16 行：| Broadcom 网络与互联 | 合作方硅与系统能力，不等于 OpenAI 芯片 | Broadcom 明确提到 Ethernet、Tomahawk、PCIe、光互联及机架系统能力；OpenAI 还参与 OCI 光互联规范和 MRC 网络协议 | scale-up/scale-out 网络、以太网交换、NIC、PHY、光连接；MRC 关注大规模训练网络可靠性 | OpenAI 具体部署中每一类 Broadcom 器件的型号、数量、端到端带宽和占比未确认 |
> 第 18 行：| Stargate | OpenAI 的基础设施平台/数据中心计划，不是芯片 | 2025-2026 持续扩张；OpenAI 2026-04-29 称 Abilene 站点使用 OCI、NVIDIA GB200，并已训练 GPT-5.5 | 数据中心、电力、冷却、云和芯片伙伴的组合 | 不能把 Stargate 的 GW 规划当成 OpenAI 自有芯片已部署 |
> 第 19 行：| Microsoft Azure、AWS、OCI、CoreWeave | 云/数据中心承载，不是 OpenAI 芯片 | Azure 仍承载 OpenAI 第一方产品；AWS 2025-11 宣布 NVIDIA GPU 规模，2026-02 又确认 Trainium 容量；OCI、CoreWeave 参与 Stargate | 云服务、集群、租赁和托管容量 | 云上使用某模型不等于使用 Jalapeño；Jalapeño 的云产品名称、公开租户和 API 入口未确认 |
> 第 20 行：| GPT、ChatGPT、Codex、Frontier、API | 模型/产品/服务层 | 这些是计算需求来源或服务出口 | 训练、后训练、推理、agent/产品工作负载 | 不应把模型发布、API 可用或 Frontier 云分发写成芯片发布 |
> 第 23 行：
> 第 24 行：“OpenAI 自研芯片”现在已经不能再写成“公开资料未确认”。更准确的表述是：**Jalapeño 已被 OpenAI 官方确认是 OpenAI 的第一款自定义推理芯片，并有工程样片与公开测量；但除 tape-out/送样/实验室运行/初步部署路线图之外，量产、出货、客户部署和云可用仍未被官方明确确认。**
> 第 25 行：
> 第 41 行：| 2026-05-05 | OpenAI 发布 MRC（Multipath Reliable Connection）并称与 AMD、Broadcom、Intel、Microsoft、NVIDIA 合作两年；已用于多个模型训练 | 网络协议/训练通信层 | OpenAI 官方事实；协议开放到 OCP |
> 第 42 行：| 2026-06-01 | OpenAI frontier models 与 Codex 在 Amazon Bedrock 正式可用 | 模型/产品云可用；不代表 Jalapeño 云可用 | OpenAI 官方事实 |
> 第 43 行：| 2026-06-24 | OpenAI 与 Broadcom 正式公布 Jalapeño；OpenAI 从零设计，Broadcom 做芯片实现和网络，Celestica 做板卡、机架和系统；九个月 tape-out；工程样片实验室运行 | **流片完成/工程样片/正式型号披露** | OpenAI 官方事实；性能早期表述含预测 |
> 第 44 行：| 2026-08-25 | OpenAI 发布 Jalapeño 首次测量结果：GPT-OSS 120B、DeepSeek R1、Kimi K2.5 1T；同时称未来数月扩大部署 | **实测/初步结果/部署爬坡**；不是量产或广泛客户部署证明 | OpenAI 官方事实；比较基准和测试口径见正文 |
> 第 45 行：| 2026-08-25 | OpenAI 进一步称其已有 working first-party silicon，未来世代已在推进 | 第一方硅片已工作；后续仍是路线图 | OpenAI 官方事实 |
> 第 53 行：          ↓
> 第 54 行：芯片：Jalapeño（OpenAI 设计；Broadcom 实现协作）
> 第 55 行：板卡/机架/系统：Celestica 集成；Broadcom 网络/连接
> 第 61 行：
> 第 62 行：这条链条中，只有中间的 Jalapeño 可称为 OpenAI 自研/主导设计芯片。NVIDIA GB200/Vera Rubin、AWS Trainium、Cerebras 系统、AMD Instinct、Broadcom Tomahawk 都属于合作方或外部硬件。ChatGPT、Codex、GPT-5.5、Frontier、Amazon Bedrock 则属于模型/产品/云分发层。
> 第 63 行：
> 第 65 行：
> 第 66 行：### 4.1 Jalapeño 的公开架构信号
> 第 67 行：
> 第 69 行：
> 第 70 行：**官方事实：** Jalapeño 是从零面向现代 LLM 推理设计，不是把早期 AI 工作负载的通用加速器改造过来。设计输入包括 OpenAI 的模型路线图、kernel、serving 系统和产品需求，目标是在单一架构中兼顾高吞吐与低延迟。
> 第 71 行：
> 第 77 行：
> 第 78 行：Jalapeño 的公开定位是 inference-first。OpenAI 的整体组合仍覆盖：
> 第 79 行：
> 第 82 行：- Cerebras 提供超低延迟推理容量。
> 第 83 行：- Jalapeño 以高规模、互动式、成本敏感的 LLM 推理为第一落点。
> 第 84 行：
> 第 85 行：**分析判断：** 这是一种“训练保持外部多供应商、推理逐步加入自研 ASIC”的风险分层。训练更看重生态成熟度、可编程性、集群规模和长时间故障恢复；推理更容易围绕有限的 serving 模式、量化策略、KV 管理和产品延迟目标做定制。不能据此断言 Jalapeño 已被用于训练。
> 第 86 行：
> 第 94 行：| 数据搬运 | OpenAI 明确称减少 data movement | 说明设计目标包含搬运成本，而非只提高算术峰值 |
> 第 95 行：| 网络 | Broadcom Ethernet、Tomahawk、PCIe、光互联能力；OpenAI 参与 OCI MSA；MRC 用于训练网络可靠性 | scale-up、scale-out 和故障恢复都被当成系统设计问题；但 Jalapeño 的片内/片间协议未确认 |
> 第 96 行：| 机架系统 | Broadcom 与 Celestica 参与板卡、机架、系统与生产系统 | 性能/瓦应理解为系统级指标的候选方向，不能自动等同于裸芯片指标 |
> 第 100 行：
> 第 101 行：**官方事实：** OpenAI 的 Jalapeño 初步结果文章将现代 LLM 推理拆成不同瓶颈，并在架构讨论中强调内存移动、延迟和完整请求测量；官方没有公开“KV Cache 容量”“每 token KV 字节数”“KV 是否片上/片外”“跨芯片 KV 放置策略”。
> 第 102 行：
> 第 103 行：**分析判断：** 对自回归 decode，权重读取和 KV 读取会反复发生，KV 的容量、带宽、局部性与调度决定并发上限。Jalapeño 若能减少权重、激活与 KV 的往返，或在服务层把 KV 放置与网络拓扑共同规划，就可能解释其“低延迟 + 高吞吐”的目标。但这仍是架构推理，不是公开规格。
> 第 104 行：
> 第 106 行：
> 第 107 行：**官方事实：** OpenAI 说模型加速了 Jalapeño 的设计和 bring-up，最新模型正在加速芯片优化和编程；文章标题和正文还称“designed the chip so AI could program it”。OpenAI 同时把 kernel、serving、调度和部署系统列入全栈设计范围。
> 第 108 行：
> 第 110 行：
> 第 111 行：OpenAI 的多供应商策略降低了单一硬件失败的风险，但也要求 serving 抽象、算子库、性能模型和调度器具备硬件可移植性。MRC 作为 OCP 开放协议，体现的是网络层标准化；它不等于 Jalapeño 软件栈已向公众开放。
> 第 112 行：
> 第 134 行：
> 第 135 行：| 状态 | Jalapeño 是否公开确认 |
> 第 136 行：|---|---|
> 第 144 行：| OpenAI 客户部署 | 未确认；只确认 OpenAI 正在扩大部署/计划部署 |
> 第 145 行：| 对外云可用 | 未确认；Amazon Bedrock 的 OpenAI 模型可用不等于 Jalapeño 可用 |
> 第 146 行：| 多代路线图 | 已确认存在，但后续型号和节点未公开 |
> 第 150 行：
> 第 151 行：这里的 Search/Top-k/Gather 不是 OpenAI 已公开的 Jalapeño 指令集规格，而是把其公开的 LLM serving、内存搬运和网络目标映射到常见工作负载后的分析框架。
> 第 152 行：
> 第 154 行：
> 第 155 行：MoE 路由、候选选择、检索增强和 beam-like 选择都可能出现 Search/Top-k。Top-k 的瓶颈通常包括比较、归约、索引生成和不规则内存访问。若硬件只优化矩阵乘，Top-k 仍会让计算单元等待；OpenAI 反复强调 kernel、serving 和数据搬运，说明这类非 GEMM 阶段可能属于系统优化范围，但官方没有确认 Jalapeño 有专用 Top-k 单元。
> 第 156 行：
> 第 158 行：
> 第 159 行：Gather 把索引转成权重、激活、KV 或专家数据访问，容易受内存局部性和跨芯片通信影响。OpenAI 的“减少 data movement”目标与 Gather 的问题高度相关，特别是 MoE expert dispatch、KV 读取和检索结果拼接。这里是架构意义上的对应关系，不是公开的 Jalapeño 功能清单。
> 第 160 行：
> 第 162 行：
> 第 163 行：decode 阶段以 token 为粒度推进，KV Cache 读写与并发规模强相关。高吞吐与低 TBT/端到端延迟常有冲突：批量变大可提高利用率，但会增加排队和内存压力。OpenAI 称 Jalapeño 试图在单一架构中同时改善吞吐和延迟，合理的解释是其芯片、内存、网络和 serving 共同调度，而不是只提高矩阵算力。
> 第 164 行：
> 第 166 行：
> 第 167 行：训练中的 all-reduce、all-to-all 和 checkpoint 恢复会把网络故障放大。OpenAI 的 MRC 通过多路径、adaptive packet spraying、静态源路由与故障绕行，目标是让同步训练少因链路抖动重启。Broadcom 的 Ethernet/Tomahawk 则提供交换和互联硅。它们说明 OpenAI 的基础设施洞察已经把“数据搬运”和“通信可靠性”放到与加速器同一层级；但 MRC 是训练网络协议，不能被说成 Jalapeño 的片内互联协议。
> 第 168 行：
> 第 176 行：
> 第 177 行：Jalapeño 的公开表述是 OpenAI 设计，Broadcom 做芯片实现、网络和连接，Celestica 做板卡/机架/系统工业化。没有公开证据表明 OpenAI 自有晶圆厂、封装厂或完整制造链。TSMC 官方页面/公告检索截至 2026-09-02 未找到 OpenAI 项目的直接确认，因此报告不把 TSMC 写成 Jalapeño 的已确认代工方。
> 第 178 行：
> 第 180 行：
> 第 181 行：Jalapeño 是第一款公开确认的自定义推理芯片。它不证明 OpenAI 已有公开的训练芯片、CPU、NIC、HBM 或 DPU 型号，也不证明所有 OpenAI 工作负载已迁移。
> 第 182 行：
> 第 184 行：
> 第 185 行：OpenAI 模型在 Azure、AWS Bedrock 或其他平台可用，只说明模型/产品分发或云承载路径。除非出现明确的实例类型、租户入口、部署说明或客户公告，否则不能写成 Jalapeño 已云可用。
> 第 186 行：
> 第 188 行：
> 第 189 行：Jalapeño 的性能是 OpenAI 发布的初步结果，页面称详细技术报告将在后续提供。当前不能把“industry-leading”当作独立基准事实，也不能在缺少完整测试配置时声称其优于所有 GPU/ASIC。
> 第 190 行：
> 第 192 行：
> 第 193 行：OpenAI 的选择不是单路线替代，而是组合优化：NVIDIA 提供成熟训练与通用生态，AMD 增加供应与路线选择，AWS Trainium 提供云内专用 ASIC，Cerebras 提供极低延迟特化系统，Broadcom 提供定制硅与 Ethernet 网络，Microsoft/Oracle/CoreWeave/AWS 提供数据中心和云容量，OpenAI 自己把最贴近产品的推理约束固化进 Jalapeño。
> 第 194 行：
> 第 195 行：**最可能情景（分析判断）：** Jalapeño 先在 OpenAI 内部高量推理与 agent 场景扩容，与 NVIDIA/Trainium/Cerebras 按工作负载分工；OpenAI 继续公开性能和软件接口，但不把芯片作为独立商品销售。
> 第 196 行：
> 第 198 行：
> 第 199 行：**最乐观情景（分析判断）：** OpenAI 把真实 serving 数据持续反馈给芯片、内存、网络和调度，Jalapeño 多代产品在推理成本/延迟上形成稳定优势，外部供应商保留训练与峰值能力，OpenAI 通过组合调度获得更高的供给弹性和议价权。
> 第 200 行：
> 第 207 行：1. **OpenAI and Broadcom unveil LLM-optimized inference chip**，2026-06-24，OpenAI，访问 2026-09-02。https://openai.com/index/openai-broadcom-jalapeno-inference-chip/
> 第 208 行：2. **Jalapeño’s first results show industry-leading speed and efficiency in AI inference**，2026-08-25，OpenAI，访问 2026-09-02。https://openai.com/index/jalapeno-first-results/
> 第 209 行：3. **The full stack behind abundant intelligence**，2026-08-25，OpenAI，访问 2026-09-02。https://openai.com/index/the-full-stack-behind-abundant-intelligence/
> 第 231 行：22. **Optical Scale-up Consortium Established to Create an Open Specification for AI Infrastructure**，2026-03-12，Broadcom，访问 2026-09-02。https://www.broadcom.com/company/news/product-releases/optical-scale-up-consortium-established-to-create-an-open-specification-for-ai-infrastructure
> 第 232 行：23. **TSMC 2024 Sustainability Report**，2025，TSMC，访问 2026-09-02；用于核验 TSMC 官方材料中未发现 OpenAI/Jalapeño 项目确认。https://esg.tsmc.com/file/public/2024-TSMC-Sustainability-Report-e.pdf
> 第 233 行：
> 第 235 行：
> 第 236 行：本报告采用横纵分析法：纵向追踪 OpenAI 从 Azure 超算合作到 Jalapeño 的演进，横向按芯片、网络、系统、云和模型层比较其供应组合。所有“分析判断”均建立在相邻的官方事实之上，未将未确认规格或传闻型号补写成事实。

## 直接来源链接

1. <https://openai.com/index/openai-broadcom-jalapeno-inference-chip/>
2. <https://openai.com/index/jalapeno-first-results/>
3. <https://openai.com/index/the-full-stack-behind-abundant-intelligence/>
4. <https://www.broadcom.com/company/news/product-releases/optical-scale-up-consortium-established-to-create-an-open-specification-for-ai-infrastructure>
5. <https://esg.tsmc.com/file/public/2024-TSMC-Sustainability-Report-e.pdf>

## 证据边界

- 这是资料重排页，不是重新发布或重新核验的产品公告。
- “发布、流片、送样、量产、出货、客户部署、云端可用、路线图、停产”等状态只在综合报告明确写出时保留；缺失项仍为“公开资料未确认”。
- 若摘录同时出现芯片、板卡、服务器、机架或云服务，均按原报告层级保留，并以“产品层级”字段提醒，不做跨层级推导。

## 关联表格原文（完整表格）

以下表格块来自综合报告中与本拆分项命中的表格，完整保留表头、状态列和规格列。

> 来源综合报告第 11-20 行：
> 第 11 行：| 项目 | 归类 | 公开确认到的状态（截至 2026-09-02） | 规格层级 | 不能确认的部分 |
> 第 12 行：|---|---|---|---|---|
> 第 13 行：| **Jalapeño** | OpenAI 主导设计的定制 LLM 推理加速器；Broadcom、Celestica 参与工业化 | 2026-06-24 首次正式披露；九个月完成至制造 tape-out；工程样片在实验室按生产目标频率/功耗运行；2026-08-25 有初步实测结果 | 面向现代 LLM 推理；强调降低数据搬运、平衡计算/内存/网络、接近理论峰值利用率；支持 OpenAI 及外部 LLM 工作负载 | 芯片制程、晶体管数、封装、片上 SRAM/缓存容量、HBM 容量/带宽、算力峰值、互联拓扑、TDP、具体 kernel 指令集均未公开 |
> 第 14 行：| Jalapeño 后续多代平台 | OpenAI + Broadcom 的路线图 | 计划从 2026 年底开始初始部署，随后扩展多个世代；没有公开第二代型号 | 多代计算平台，配套芯片、板卡、机架、网络和生产系统 | 第二代及以后型号、制程、性能、量产节奏和实际部署量未确认 |
> 第 15 行：| 10GW OpenAI-designed accelerators | OpenAI 设计、Broadcom 合作开发和部署 | 2025-10-13 宣布；目标 2026 下半年开始部署、2029 年底完成 | 加速器与 Ethernet scale-up/scale-out 网络系统；规模用功率而非芯片数量表述 | 10GW 是否全部由 Jalapeño 或其后代构成、每瓦对应多少芯片、实际出货/上架数量均未确认 |
> 第 16 行：| Broadcom 网络与互联 | 合作方硅与系统能力，不等于 OpenAI 芯片 | Broadcom 明确提到 Ethernet、Tomahawk、PCIe、光互联及机架系统能力；OpenAI 还参与 OCI 光互联规范和 MRC 网络协议 | scale-up/scale-out 网络、以太网交换、NIC、PHY、光连接；MRC 关注大规模训练网络可靠性 | OpenAI 具体部署中每一类 Broadcom 器件的型号、数量、端到端带宽和占比未确认 |
> 第 17 行：| Celestica 板卡/机架/系统 | 制造与系统集成合作方 | OpenAI 2026-06-24 明确其参与板卡、机架和系统集成以及规模化生产系统 | board、rack、system integration | 代工厂、封装厂、具体主板/机架配置和量产订单未确认 |
> 第 18 行：| Stargate | OpenAI 的基础设施平台/数据中心计划，不是芯片 | 2025-2026 持续扩张；OpenAI 2026-04-29 称 Abilene 站点使用 OCI、NVIDIA GB200，并已训练 GPT-5.5 | 数据中心、电力、冷却、云和芯片伙伴的组合 | 不能把 Stargate 的 GW 规划当成 OpenAI 自有芯片已部署 |
> 第 19 行：| Microsoft Azure、AWS、OCI、CoreWeave | 云/数据中心承载，不是 OpenAI 芯片 | Azure 仍承载 OpenAI 第一方产品；AWS 2025-11 宣布 NVIDIA GPU 规模，2026-02 又确认 Trainium 容量；OCI、CoreWeave 参与 Stargate | 云服务、集群、租赁和托管容量 | 云上使用某模型不等于使用 Jalapeño；Jalapeño 的云产品名称、公开租户和 API 入口未确认 |
> 第 20 行：| GPT、ChatGPT、Codex、Frontier、API | 模型/产品/服务层 | 这些是计算需求来源或服务出口 | 训练、后训练、推理、agent/产品工作负载 | 不应把模型发布、API 可用或 Frontier 云分发写成芯片发布 |

> 来源综合报告第 28-45 行：
> 第 28 行：| 日期 | 事件 | 状态判断 | 证据属性 |
> 第 29 行：|---|---|---|---|
> 第 30 行：| 2016-11-15 | OpenAI 宣布与 Microsoft 合作，Azure 成为深度学习和 AI 的主要云平台，使用 K80 + InfiniBand，并计划扩展到数千至数万台机器 | 云基础设施合作/早期训练平台 | OpenAI 官方事实 |
> 第 31 行：| 2019-07-22 | Microsoft 投资并与 OpenAI 共同开发 Azure AI 超算技术；Azure 成为独家云提供商 | 云与超算联合建设，不是自研芯片 | OpenAI 官方事实 |
> 第 32 行：| 2023-01-23 | OpenAI 称与 Microsoft 已共同构建多个 Azure 超算系统，用于训练所有模型；Azure 仍是所有研究、API、产品工作负载的独家云提供商 | 外部硬件系统深度共优化 | OpenAI 官方事实 |
> 第 33 行：| 2025-01-21 | Microsoft 说明 OpenAI API 在 Azure 上运行，同时为 OpenAI 额外建设能力，并允许 OpenAI 建设主要用于研究和训练的额外容量 | 供应关系更灵活，但仍非芯片发布 | Microsoft 官方事实 |
> 第 34 行：| 2025-07-22 | OpenAI 与 Oracle 宣布额外 4.5GW Stargate 数据中心容量；Abilene 开始接收 NVIDIA GB200 机架并运行早期训练/推理 | 数据中心建设中；NVIDIA 系统已早期运行 | OpenAI 官方事实 |
> 第 35 行：| 2025-09-22 | OpenAI 与 NVIDIA 宣布至少 10GW NVIDIA 系统；首个 1GW 目标为 2026 下半年 Vera Rubin | 合作/意向和路线图，非已部署芯片 | OpenAI 官方事实；含 LOI/目标时点 |
> 第 36 行：| 2025-10-13 | OpenAI 与 Broadcom 宣布 10GW OpenAI-designed custom AI accelerators；Broadcom 负责合作开发与机架部署，目标 2026 下半年开始、2029 年底完成 | 项目首次公开披露；路线图/合作承诺 | OpenAI/Broadcom 官方公告；Broadcom 同时提示前瞻性陈述风险 |
> 第 37 行：| 2025-11-03 | AWS 与 OpenAI 宣布 380亿美元多年合作，AWS 提供含数十万 NVIDIA GPU 的 EC2 UltraServers；容量目标 2026 年底前部署 | 外部云 GPU 规模化 | OpenAI 官方事实 |
> 第 38 行：| 2026-01-14 | OpenAI 与 Cerebras 合作，增加 750MW 超低延迟 AI 计算，分批至 2028 年上线 | 外部专用推理系统/云容量 | OpenAI 官方事实 |
> 第 39 行：| 2026-02-27 | OpenAI 与 Amazon 扩大战略合作，承诺消费约 2GW Trainium；覆盖 Trainium3 与下一代 Trainium4；另发布 1100亿美元融资/合作信息 | 外部 ASIC 云容量；不是 OpenAI 自研芯片 | OpenAI 官方事实 |
> 第 40 行：| 2026-04-29 | OpenAI 称 Stargate 已超过初始 10GW 目标，并披露 Abilene 站点以 OCI + NVIDIA GB200 运行，GPT-5.5 在该旗舰站点训练 | 自有/合作数据中心系统运行；芯片为 NVIDIA | OpenAI 官方事实 |
> 第 41 行：| 2026-05-05 | OpenAI 发布 MRC（Multipath Reliable Connection）并称与 AMD、Broadcom、Intel、Microsoft、NVIDIA 合作两年；已用于多个模型训练 | 网络协议/训练通信层 | OpenAI 官方事实；协议开放到 OCP |
> 第 42 行：| 2026-06-01 | OpenAI frontier models 与 Codex 在 Amazon Bedrock 正式可用 | 模型/产品云可用；不代表 Jalapeño 云可用 | OpenAI 官方事实 |
> 第 43 行：| 2026-06-24 | OpenAI 与 Broadcom 正式公布 Jalapeño；OpenAI 从零设计，Broadcom 做芯片实现和网络，Celestica 做板卡、机架和系统；九个月 tape-out；工程样片实验室运行 | **流片完成/工程样片/正式型号披露** | OpenAI 官方事实；性能早期表述含预测 |
> 第 44 行：| 2026-08-25 | OpenAI 发布 Jalapeño 首次测量结果：GPT-OSS 120B、DeepSeek R1、Kimi K2.5 1T；同时称未来数月扩大部署 | **实测/初步结果/部署爬坡**；不是量产或广泛客户部署证明 | OpenAI 官方事实；比较基准和测试口径见正文 |
> 第 45 行：| 2026-08-25 | OpenAI 进一步称其已有 working first-party silicon，未来世代已在推进 | 第一方硅片已工作；后续仍是路线图 | OpenAI 官方事实 |

> 来源综合报告第 91-97 行：
> 第 91 行：| 维度 | 公开证据 | 分析含义 |
> 第 92 行：|---|---|---|
> 第 93 行：| 内存容量/带宽 | 未披露 HBM 容量、带宽、片上 SRAM、缓存层级 | 不能用任何传闻规格估算模型容量或并发；decode 性能判断必须保留不确定性 |
> 第 94 行：| 数据搬运 | OpenAI 明确称减少 data movement | 说明设计目标包含搬运成本，而非只提高算术峰值 |
> 第 95 行：| 网络 | Broadcom Ethernet、Tomahawk、PCIe、光互联能力；OpenAI 参与 OCI MSA；MRC 用于训练网络可靠性 | scale-up、scale-out 和故障恢复都被当成系统设计问题；但 Jalapeño 的片内/片间协议未确认 |
> 第 96 行：| 机架系统 | Broadcom 与 Celestica 参与板卡、机架、系统与生产系统 | 性能/瓦应理解为系统级指标的候选方向，不能自动等同于裸芯片指标 |
> 第 97 行：| 冷却/电力 | Stargate Abilene 使用闭环冷却；OpenAI 把 GW 作为容量规划单位 | 10GW 是基础设施功率规模，不是算力或芯片数；功率密度和 PUE 未公开 |

> 来源综合报告第 135-147 行：
> 第 135 行：| 状态 | Jalapeño 是否公开确认 |
> 第 136 行：|---|---|
> 第 137 行：| 首次披露 | 是，2026-06-24 |
> 第 138 行：| 正式型号/产品发布 | 是，OpenAI 称 first Intelligence Processor / first custom inference chip |
> 第 139 行：| 制造流片 tape-out | 是，九个月完成至 tape-out |
> 第 140 行：| 工程样片/送样 | 是，实验室样片按生产目标频率和功耗运行 |
> 第 141 行：| 初步实测 | 是，2026-08-25 发布 InferenceX 结果 |
> 第 142 行：| 量产 | 未确认 |
> 第 143 行：| 批量出货 | 未确认 |
> 第 144 行：| OpenAI 客户部署 | 未确认；只确认 OpenAI 正在扩大部署/计划部署 |
> 第 145 行：| 对外云可用 | 未确认；Amazon Bedrock 的 OpenAI 模型可用不等于 Jalapeño 可用 |
> 第 146 行：| 多代路线图 | 已确认存在，但后续型号和节点未公开 |
> 第 147 行：| 停产 | 无公开证据 |
