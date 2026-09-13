# Groq 3 LPU / LP30 证据页

- 研究截止日：2026-09-05
- 核验日期：2026-09-05
- 研究对象：Groq 3 LPU，公开资料中对应的芯片代号为 LP30
- 产品层级：芯片；另设 LPX 托盘/机架、GroqCloud API 与 Tokens/s 服务层边界
- 厂商总览：[Groq](./Groq-overview.md) · [[Groq-overview|图谱总览]]

## 一句话结论

截至研究截止日，NVIDIA 的 Vera Rubin 发布材料和技术说明已公开命名 Groq 3 LPU/LP30，并给出其在 Groq 3 LPX 中的若干芯片与机架级规格；现有证据足以确认“LP30 被纳入 LPX 低延迟推理系统”的产品定位，尚不足以确认 LP30 独立 datasheet、单芯片功耗、流片/送样、已出货数量、客户部署或已在 GroqCloud 规模上线。关于量产的 “full production” 是 NVIDIA 对平台/新芯片组合的厂商口径，不能替代 LP30 的独立量产证明。[S1][S2]

## 产品层级与对象边界

| 层级 | 本页如何使用 | 不能从该层级推导什么 |
|---|---|---|
| LP30 LPU 芯片 | 记录公开归属于单颗 LPU 的 SRAM、片上带宽、C2C 与执行单元信息 | 不能把 LPX 整架吞吐、内存、液冷或服务 Tokens/s 当成单芯片规格 |
| LPX 托盘 | 公开设计为 8 颗 LPU 加主机处理器和 fabric expansion logic 的托盘 | 托盘级 9.6 PFLOPS、主机内存和 fabric 逻辑不等于 LP30 芯片规格 |
| Groq 3 LPX 机架/服务器系统 | 公开设计为 32 个 1U 托盘、256 颗 LPU 的低延迟解码系统 | 机架级 40 PB/s、640 TB/s scale-up 或液冷不能证明每颗 LP30 的实际有效性能 |
| Vera Rubin 平台 | NVIDIA 描述 LPX 与 Vera Rubin NVL72 协同，LPX 侧重解码路径 | NVIDIA GPU、NVL72 和 LPX 的系统能力不能回填为 LP30 硬件能力 |
| GroqRack/旧服务器 | Groq 的历史产品与服务器边界；本页不把旧 GroqRack 当成 LPX，也不补写其配置 | 旧 GroqChip、GroqRack 或旧服务器规格不能迁移到 LP30 |
| GroqCloud/API | Groq 运营的 API/云服务；模型、排队、网络和服务配置都在此层 | API 页面展示的 Tokens/s 不能作为 LP30 芯片 benchmark，也不能证明由 LP30 承载 |

## 生命周期状态

| 生命周期字段 | 截至 2026-09-05 的判断 | 证据状态与边界 |
|---|---|---|
| 宣布/命名 | 2026-03-16，NVIDIA 的 Vera Rubin 发布材料公开写出 Groq 3 LPU；同日技术说明使用 LP30 名称 | 已确认事实，来源是 NVIDIA 官方发布与技术博客；属于合作方公开命名，不等于独立商品上市。[S1][S2] |
| 流片或工程样片 | 公开资料未确认 | 未找到 LP30 流片批次、工程样片或 silicon bring-up 公告 |
| 送样/客户取样 | 公开资料未确认 | LPX 的产品规划和合作公告不构成 LP30 送样证明 |
| 量产 | 厂商主张，LP30 独立状态未确认 | NVIDIA 发布材料使用 “full production” 描述 Vera Rubin 相关新芯片组合；同一材料仍把 LPX 可用时间放在 2026 年下半年，不能据此确认 LP30 已完成独立量产。[S1] |
| 出货 | 公开资料未确认；系统级路线图指向 2026 年秋季起生产出货 | NVIDIA 后续公告谈 Vera Rubin 平台生产出货时间，未给出 LP30 单独出货数量或客户订单。[S3] |
| 客户部署 | 公开资料未确认 | 截至截止日没有可核验的 LP30 客户部署、数量或生产集群清单；Groq 的“计划部署”属于路线图/厂商意图。[S4] |
| 云或实例可用 | LP30 专属云实例未确认；GroqCloud API 本身可用 | GroqCloud 公开平台可展示模型和服务指标，但没有把当前请求后端明确映射到 LP30；“API 可用”不等于“LP30 云实例可用”。[S5] |
| 路线图 | Groq 计划把包括 NVIDIA LPX 在内的新推理技术接入现有云 footprint；NVIDIA 将 LPX 可用时间放在 2026 年下半年 | 厂商路线图，不是已经完成的部署或 GA 证明。[S3][S4] |

## 芯片级规格

下表只收录公开材料直接归属于 LP30/LPU 的内容。没有 LP30 专属 datasheet 的字段保留为“公开资料未确认”。

| 项目 | 公开口径 | 证据状态与边界 |
|---|---|---|
| 芯片名称 | Groq 3 LPU；LP30 | 已确认事实，命名来自 NVIDIA 官方材料。[S1][S2] |
| 制程 | 公开资料未确认 | Groq 关于第一代 LPU 的 14 nm 说明不能套用到 LP30；LP30 的晶圆厂、节点和封装未公开确认 |
| 执行单元 | MXM 矩阵执行、VXM 向量执行、SXM 数据交换；公开技术说明还给出 320-byte vector 工作粒度 | 已公开的 LP30/LPX 设计描述；单元数量、频率、面积和每单元吞吐未确认。[S2] |
| 数值格式 | LPX 系统标注 FP8 inference compute；Groq 的通用 LPU 材料讨论 TruePoint、FP32 attention logits、BFP 和 FP8 activation | 厂商/合作方公开事实，但通用 LPU 数值格式不能自动等同于 LP30 的完整支持矩阵；LP30 专属格式与吞吐表未确认。[S2][S6] |
| 片上存储 | 每颗 LPU 500 MB SRAM | 已公开的单 LPU 口径；不是整架模型容量，也不是 HBM 容量。[S2] |
| 片上 SRAM 带宽 | 每颗 LPU 150 TB/s | 已公开峰值口径；不是某个模型的有效 KV 带宽。[S2] |
| 片外内存 | LP30 单芯片 HBM、DDR 或其他片外内存配置公开资料未确认 | LPX 机架/托盘存在 DDR5、主机内存和 fabric expansion logic，但这些属于系统级部件，不回填到芯片字段。[S2][S7] |
| 芯片间互联 | 每颗 LPU 96 条 C2C link、112 Gbps/link、双向聚合 2.5 TB/s | 合作方技术说明的单 LPU 连接口径；没有独立可复现测试。[S2] |
| 功耗、TDP、散热 | LP30 单芯片功耗和封装散热公开资料未确认 | LPX 的全液冷是系统级信息；旧 GroqChip 的 300 W max/215 W TDP/185 W average 不能迁移。[S2][S8] |
| 单芯片 FP8 峰值 | 公开资料未直接给出 | 9.6 PFLOPS 是 8-LPU 托盘口径；按 9.6/8 得出的约 1.2 PFLOPS 是分析推断，不作为 LP30 已确认规格。[S2] |
| 面积、封装、频率、良率 | 公开资料未确认 | 当前直接来源没有足够字段支持这些数字 |

## LPX、GroqRack、云 API 与 Tokens/s 的分层

| 对象 | 可引用的公开事实 | 不应写成 |
|---|---|---|
| LPX 托盘 | 8 颗 LPU；托盘级 9.6 PFLOPS FP8 inference compute；另有主机和 fabric expansion logic | “单颗 LP30 有 9.6 PFLOPS” |
| Groq 3 LPX 机架 | 32 个 1U 托盘、256 颗 LPU；公开资料给出机架级 40 PB/s SRAM 带宽和 640 TB/s scale-up | “LP30 单芯片有 40 PB/s 或 640 TB/s” |
| GroqRack/旧服务器 | 作为历史 Groq 系统边界存在；本页没有把其配置并入 LP30 | “GroqRack 就是 Groq 3 LPX” |
| GroqCloud API | Groq 运营的 API 服务，平台页面展示模型、接口和服务侧性能指标 | “GroqCloud 的 Tokens/s 就是 LP30 的吞吐” |
| Tokens/s | 服务端指标，受模型、输入输出长度、并发、排队、网络、软件版本和后端硬件影响；平台页的 user-level 指标即使为真也仍属服务口径 | “Tokens/s/user = 芯片峰值”或“当前 GroqCloud 已由 LP30 规模承载” |

## 架构与软件证据

### 已确认的设计方向

- Groq 的 LPU 架构材料把 SRAM 作为靠近计算的数据存储，并强调编译器在执行前安排算子、内存移动和通信；这支持“编译器静态调度的空间数据流”这一架构描述。[S6]
- NVIDIA 的 LP30/LPX 技术说明将 MXM、VXM、SXM 与固定向量粒度、片上 SRAM 和 C2C 互联放在同一设计描述中。可以确认公开路线重点在低延迟解码、显式数据移动和确定性的多芯片执行。[S2]
- 这些材料没有公开 LP30 的 TOPK、动态 page-aware address、indexed KV gather 或专用检索单元。因此，Groq 3 可以被分析为确定性的 Tensor/dataflow 平面，不能被写成已经实现 Retrieval Plane 的芯片。

### 证据状态分开写

| 主张 | 状态 | 限定 |
|---|---|---|
| 编译器可预先安排算子、内存和通信 | 厂商主张/官方架构描述 | 说明编程模型和执行路线，不等于任何模型都无需重新编译 |
| SRAM-first 与显式数据流有助于稳定 per-token latency | 分析推断 | 需要给定模型、批量、上下文、软件版本和功耗边界的实测来量化 |
| C2C 与同步设计支持大规模 LPU pipeline | 厂商/合作方公开事实 | 系统互联能力不等于跨卡 Top-k merge 或检索召回能力 |
| 有专用 Search/Top-k/Gather 硬件 | 公开资料未确认 | 当前来源没有给出该类单元、指令或可复现结果 |

## 性能与采用证据

- NVIDIA 给出了 LPX 的托盘和机架级峰值规格，适合说明产品设计目标；这些数字没有提供完整模型、精度、批量、延迟分位数、功耗边界和软件版本，因此不能当作独立 benchmark。[S2]
- GroqCloud 平台页面的 Tokens/s 或 tokens/s/user 属于服务层展示。页面没有把指标绑定到 LP30，也没有同时给出模型版本、测试条件、端到端延迟分位数或功耗，所以本页不把它转换为 LP30 的 TPOT、TTFT 或 Tokens/J。[S5]
- Groq 公告称计划把 LPX/Vera Rubin NVL72 接入推理云；这是采用路线图，不能证明 LP30 已完成客户部署或已经在线承载生产请求。[S4]
- 截至截止日，未找到 LP30 的独立测试报告、客户侧部署报告、可复现 benchmark 或按 LP30 标注的云实例 SKU。该缺口直接影响对商业成熟度和真实有效吞吐的判断。

## 未确认项与冲突

1. LP30 的制程、面积、封装、频率、执行单元数量、单芯片功耗、片外内存和独立可购 SKU 均未被当前直接来源完整披露。
2. “full production”是 NVIDIA 的平台/新芯片组合表述，而 LPX 可用时间和 Vera Rubin 生产出货又被安排在 2026 年下半年或秋季，二者至少存在产品层级和时间口径差异；在未有 LP30 专属公告前，保守状态应写为“厂商称进入生产阶段，LP30 独立量产未确认”。[S1][S3]
3. Groq 的 LPX 公告把新系统描述为计划接入推理云；计划部署、客户部署、出货和云 GA 是四个不同状态，当前不能合并。[S4]
4. 旧 GroqChip 的 14 nm、230 MB SRAM、80 TB/s 和功耗数据只用于历史基线，不能作为 LP30 的代际规格。[S8]
5. 当前证据不支持把 Groq 3 的静态数据流直接等同于动态 Retrieval Plane；Search、Top-k、Merge、page-aware Gather 和地址翻译仍是公开资料未确认项。

## 直接来源清单

| 编号 | 标题 | 主体 | 发布日期 | 核验日期 | 直接 URL |
|---|---|---|---|---|---|
| S1 | NVIDIA Vera Rubin Platform | NVIDIA | 2026-03-16 | 2026-09-05 | <https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform> |
| S2 | Inside NVIDIA Groq 3 LPX: The Low-Latency Inference Accelerator for the NVIDIA Vera Rubin Platform | NVIDIA Developer Blog | 2026-03-16 | 2026-09-05 | <https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/> |
| S3 | Vera Rubin Ramps Into Full Production for the Agentic AI Factory | NVIDIA | 2026-05-31 | 2026-09-05 | <https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory> |
| S4 | Groq Among the First to Bring NVIDIA Groq 3 LPX and Vera Rubin NVL72 to Market | Groq | 2026-08-24 | 2026-09-05 | <https://groq.com/blog/groq-among-the-first-to-bring-nvidia-groq-3-lpx-and-vera-rubin-nvl72-to-market> |
| S5 | Groq Platform | Groq | 未标注 | 2026-09-05 | <https://groq.com/platform> |
| S6 | What Is a Language Processing Unit? | Groq | 2025-03-07 | 2026-09-05 | <https://groq.com/blog/the-groq-lpu-explained> |
| S7 | NVIDIA LPX | NVIDIA | 未标注 | 2026-09-05 | <https://www.nvidia.com/en-au/data-center/lpx/> |
| S8 | GroqChip Processor Product Brief | Groq | 未标注 | 2026-09-05 | <https://www.groq.com/GroqDocs/Product%20Spec%20Sheet%20-%20GroqChip%E2%84%A2%20Processor.pdf> |

> 证据边界：本页使用的 LP30 规格主要来自 NVIDIA 对 LPX 的合作方技术说明，Groq 自有公开材料截至截止日未提供 LP30 完整 datasheet。LP30 的独立量产、出货、客户部署、GroqCloud 云实例、单芯片功耗和独立性能仍应标记为“公开资料未确认”。
