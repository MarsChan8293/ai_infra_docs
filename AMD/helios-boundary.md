# AMD / 超威半导体 — Helios（系统边界，非芯片）

- 拆分日期：2026-09-02
- 产品层级：机架/系统（非芯片）
- 综合报告：[05-amd-instinct.md](./05-amd-instinct.md)
- 文件性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容逐行摘录综合报告，保留原报告中的状态、数字、证据等级和未知项。

> 第 10 行：
> 第 11 行：截至 2026-09-01，公开产品组合中最新的前沿 AI 加速器仍是 **MI455X**；新增需要补入家族视图的已公开产品是面向既有服务器形态的 **MI350P**。MI455X 的芯片、封装内存和 scale-up 规格已经较完整，但 AMD 尚未公开单卡 TBP，也没有公开确认 MI455X 的 tape-out、sampling、逐卡量产或独立出货数量。Helios 是由 MI455X 组成的 72-GPU 机架级参考架构，不应当写成一张可单独购买的“Helios 芯片”。（**官方产品页规格/厂商发布**：[12]、[13]、[14]。）
> 第 12 行：
> 第 40 行：| 2026-01-05，MI440X/MI430X/MI500 | CES 发布会首次介绍 MI440X、MI430X 方向并预览 MI500（**厂商发布/路线图**） | 不等于 MI440X 已 GA，也不等于 MI430X/MI500 已量产 |
> 第 41 行：| 2026-07-23，MI455X/Helios | AMD 发布 MI455X 和 Helios；Helios 为 72 MI455X、18 EPYC Venice 的参考架构；AMD 还称 Helios “now in production”（**厂商发布**） | AMD 的 Helios 蓝图同时称其为 reference rack/reference architecture，且写 volume deployments expected in 2H 2026；OpenAI 计划从 Q4 2026 开始上线。二者共同证明“产品化与部署计划正在推进”，不构成独立的已安装出货数量（**冲突保留**） |
> 第 42 行：| 2026-08-28，MI355X KV | AMD ROCm 博客展示 2×MI355X 上的 4-bit KV/LMCache 分层测量（**厂商测试**） | 不是独立基准，也不能反推 MI455X 已在同一软件栈上达到相同结果 |
> 第 43 行：
> 第 44 行：公开资料中没有给出 MI350/MI400 的明确 tape-out 或 sampling 日期，也没有给出 MI455X 的单卡 mass-production start、ship date、累计出货量或客户验收清单。应写成“发布日期已确认、部分上一代云服务已 GA、MI455X/Helios 的厂商生产与伙伴部署叙事已公开、精确量产和出货量未确认”。
> 第 45 行：
> 第 50 行：| 芯片/封装 | MI455X：8 个 XCD、2 个 IOD、2 个 fabric/cache die；320B transistors；CDNA5、TSMC 2 nm + 3 nm FinFET | 这是官方架构/产品规格，不等于整机吞吐（**官方产品页/架构页**：[13]、[15]） |
> 第 51 行：| 加速器模块 | MI455X EAM：432 GB HBM4、12 stacks、23.3 TB/s、L2 192 MB、UALoE scale-up 3.6 TB/s 双向、UALink scale-out 600 GB/s 双向；DLC；TBP 未公开 | 互联数字是链路带宽，不是 Top-k 或检索 collective；不要把 MI355X 1400 W 移植到 MI455X |
> 第 52 行：| Compute tray | 4 个液冷 MI455X + 1 个 96-core EPYC Venice 主机 CPU | 是 Helios 蓝图中的托盘构成，不是单卡形态（**厂商蓝图**：[17]） |
> 第 53 行：| Helios rack | 18 个 1OU、1P:4G 托盘，即 72 个 GPU；6 个 switch tray；31 TB HBM4；1.67 PB/s 聚合 HBM 带宽；最高 2.9 EFLOPS OCP MXFP4；最高 260 TB/s rack scale-up，蓝图另给最高 43 TB/s rack scale-out | 72 GPU、EFLOPS 和 rack 带宽属于参考架构级数字；Helios 不是单一芯片，且不同 AMD 页面存在口径差异（**官方蓝图/厂商发布**：[14]、[17]） |
> 第 54 行：| 云服务 | OCI BM.GPU.MI355X.8：8×MI355X、约 2.3 TB HBM3E、128-core EPYC、3 TB DDR；文档用 288 GiB/卡，需与产品页的十进制 GB 区分 | 这是 MI355X 云 GA；截至截止日没有找到 MI455X 公共云 GA SKU，不把 Helios 伙伴计划写成已上线云服务（**云 GA/运营文档/未确认**：[18]、[19]） |
> 第 55 行：
> 第 57 行：
> 第 58 行：CDNA5 的公开架构信息包括 Wave32、256 WGP、TDM、L2 multicast、WGP clustering、split-named barriers、2 个 IOD、2 个 fabric/cache die，以及 36 条 UALoE link。TDM 支持描述符驱动的异步张量搬运，并可在 LDS 与 DRAM 间绕过寄存器；这强化了规则 tile 的 Move 路径和片上数据复用，但本身不是动态检索执行器。（**官方架构说明/分析判断**：[15]。）
> 第 59 行：
> 第 79 行：| MI355X 11 节点、87 GPU | Llama2-70B：Offline 1,042,110、Server 1,016,380、Interactive 785,522；AMD 报告 scale-out efficiency 93%、93%、98% | 特定软件、模型和节点配置的提交结果，不是所有 MI355X 集群的保证（**独立基准中的厂商提交**） |
> 第 80 行：| MI355X 12 节点、94 GPU | GPT-OSS-120B：Offline 1,031,070、Server 900,054 | 同上；不要把它写成单卡或 Helios 标准吞吐 |
> 第 81 行：| MI325X/MI300X v5.1 | MLCommons 页面可见例如 8×MI325X Server 32,027.6、8×MI300X Server 24,747.6；不同提交者和场景会变化 | 这是上一代独立结果，用于基线，不是 MI455X 的结果 |
> 第 94 行：| KV | HBM4/HBM3E 容量、FP8/4 KV、LMCache HBM+CPU DRAM 分层；长上下文实验提供了实际约束 | 没有确认芯片原生动态 KV page management；MLA 的 KV 是否复制还取决于软件并行拓扑 |
> 第 95 行：| Route / 跨卡 | UALoE、UALink、RCCL 和 Helios 多平面网络提供通用通信底座 | 没有确认面向检索候选的 `P×k` 硬件路由或跨卡 Top-k collective |
> 第 96 行：
> 第 100 行：
> 第 101 行：1. **19.6 TB/s 与 23.3 TB/s。** 旧有 Helios/工程材料的某个 compute-tray 段落写每 GPU 19.6 TB/s；当前 MI455X 产品页、CDNA5 架构页和 2026-07 brochure 写 23.3 TB/s。AMD 没有公开解释差异，本文将 23.3 TB/s 作为当前单卡规格，把 19.6 TB/s 保留为历史材料，不混合推导。
> 第 102 行：2. **Helios 的“生产”与“参考架构”。** AAI 2026 使用“now in production”叙述；Helios 蓝图仍称 reference architecture，并写 volume deployments expected 2H 2026。记录为“厂商称已进入生产/部署推进”，不能升级为独立确认的量产出货。
> 第 103 行：3. **MI455X 峰值与端到端指标。** 40.3 PFLOPS MXFP4、2.9 EFLOPS Helios 是峰值或特定系统级口径，不是 TPOT、TTFT、tokens/J；MLPerf 数字也只能在对应模型、精度和系统配置内解释。
> 第 104 行：4. **评分保持分析属性。** 原文 76/100 仍可作为对“通用 memory/scale-up 路线”的研究判断；考虑到当前软件已有 sparse indexer/top-k 路径，软件检索能力的描述应更新，但没有足够证据把硬件 Retrieval Plane 得分上调为已实现。
> 第 113 行：
> 第 114 行：MI455X 是单颗加速器；四 GPU 是 Helios compute tray；72 GPU、31 TB HBM4、约 2.9 EFLOPS 属于 Helios 机架级参考设计。AMD FAQ 明确 Helios 是 reference design、不是直接售卖的单一产品，量产部署预计在 2026 年下半年。因此 MI455X 是“已发布/已宣布”，Helios 是“已进入生产部署叙事、量产部署时间已宣布”，但单卡普遍现货仍为“公开资料未确认”。（[4]、[5]、[6]，访问日期：2026-08-22。）
> 第 115 行：
> 第 124 行：| 内存带宽 | 23.3 TB/s 峰值 | 芯片专页、CDNA 5 页面和 2026-07 数据表均采用该值。（[1]、[2]、[3]，访问日期：2026-08-22。） |
> 第 125 行：| 互联 | 主机 Infinity Fabric 256 GB/s 双向；UALoE scale-up 3.6 TB/s 双向；UALink scale-out 600 GB/s 双向 | 是通信路宽，不等于 Global Top-k 或检索 collective。（[2]、[3]，访问日期：2026-08-22。） |
> 第 126 行：| 功耗 | MI455X 单卡 TBP/TDP：公开资料未确认 | MI355X 的 1400 W 不能移植给 MI455X。（[1]、[7]，访问日期：2026-08-22。） |
> 第 127 行：
> 第 128 行：来源：[1]、[2]、[3]，访问日期：2026-08-22。资料冲突需单列：Helios 页面某个 compute-tray 段落写每 GPU 19.6 TB/s；单卡产品页、白皮书和数据表写 23.3 TB/s。AMD 未解释原因，本文采用芯片专页/白皮书/数据表值，不用 19.6 TB/s 推导性能。（[1]、[2]、[11]，访问日期：2026-08-22。）
> 第 129 行：
> 第 135 行：
> 第 136 行：MI455X 的路线可以类比为“更大的仓库、更宽的传送带、更快的仓库间道路”。HBM4 是货架，L2/LDS 是工作台，TDM 是按描述符搬运规则 tensor tile 的异步叉车，UALoE 是 GPU 间高速路；MXFP4/6/8 是更小的数字盒子。CDNA 5 白皮书确认 TDM 可异步搬运最多五维张量，并支持 LDS 与 DRAM 之间不经寄存器的传输；split DMA 会把 GPU 间请求分到合适链路。（[2]，访问日期：2026-08-22。）
> 第 137 行：
> 第 148 行：| Move / Gather / Address | TDM 直接利于规则 tile；CPU 可一致性访问 GPU 内存 | ROCm Infinity Context/hipFile 可直连 HBM 与网络存储，适合 KV 分层 | 没有 page-aware Gather、KV page translator、物理地址描述符；AIC 也不是离散 Gather。（[2]、[9]，访问日期：2026-08-22。） |
> 第 149 行：| Route / 跨卡 / TPOT、TTFT、Tokens/J | UALoE 3.6 TB/s、UALink 600 GB/s、72-GPU pod 改善通信底座 | 给 candidate-sharding 和小候选 Merge 留出路宽 | 没有 Retrieval-specific collective，也未找到 MI455X 在该类 workload 上同时报告 TPOT、TTFT、Tokens/J 的实测。Helios token throughput 是特定模型与输入输出长度下的 AMD 建模，不能替代端到端 benchmark。（[2]、[5]，访问日期：2026-08-22。） |
> 第 150 行：
> 第 157 行：| 稀疏/动态计算 | 15% | 6 | 有低精度与结构化稀疏，无动态 Search/Select/Top-k 证据。 |
> 第 158 行：| Scale-up/互联 | 15% | 14 | 3.6 TB/s、72-GPU pod 直接回应跨卡压力，但不是检索 collective。 |
> 第 159 行：| 数值格式/计算密度 | 10% | 9 | OCP MXFP4/6/8 规格完整，峰值不等于利用率。 |
> 第 177 行：- **可直接借鉴：** 保留低精度矩阵能力，同时暴露 Search/Reduce 的向量与规约原语，让模型公式由编译器组合。
> 第 178 行：- **只能类比：** split DMA、TDM、72-GPU pod 说明搬运与计算可分层，但不能证明 Search/Select/Address 已存在。
> 第 179 行：- **不宜照搬：** 不要只堆 HBM、峰值 FLOPS 或机架规模；先用 exact 软件原型验证 score materialization、Local/Global Top-k、Gather 和端到端 TPOT，再决定专用硅面积。
> 第 186 行：[4]: https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era "AMD AAI 2026 新闻稿"
> 第 187 行：[5]: https://newsroom.amd.com/news/aai-2026-helios-update/ "AMD Helios 新闻稿与脚注"
> 第 188 行：[6]: https://www.amd.com/content/dam/amd/en/documents/products/accelerators/instinct/amd-instinct-helios-blueprint-brochure.pdf "AMD Helios Rackscale Solution 蓝图"
> 第 189 行：[7]: https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html "AMD Instinct MI355X 产品页"
> 第 192 行：[10]: https://newsroom.amd.com/news/amd-and-its-partners-share-their-vision-for-ai-ev/ "AMD CES 2026：MI440X 与 MI500"
> 第 193 行：[11]: https://www.amd.com/en/products/rackscale-solutions/helios.html "AMD Helios 产品页"
> 第 194 行：
> 第 196 行：
> 第 197 行：已重新打开 [MI455X 官方产品页](https://www.amd.com/en/products/accelerators/instinct/mi400/mi455x.html) 和 [AMD Instinct 产品总览](https://www.amd.com/en/products/accelerators/instinct.html)，确认 MI455X 仍列为 2026-07-23 发布、CDNA5、432GB HBM4、23.3TB/s；[Helios 页面](https://www.amd.com/en/products/rackscale-solutions/helios.html)仍将 72 GPU 明确为机架级设计。上述数字不能回填单 GPU 功耗或现货状态。
> 第 198 行：
> 第 205 行：[16]: https://www.amd.com/en/products/accelerators/instinct/mi400/mi430x.html "AMD Instinct MI430X 产品页"
> 第 206 行：[17]: https://www.amd.com/content/dam/amd/en/documents/products/accelerators/instinct/amd-instinct-helios-blueprint-brochure.pdf "AMD Helios Blueprint"
> 第 207 行：[18]: https://blogs.oracle.com/cloud-infrastructure/announcing-general-availability-of-oci-amd-mi355x "Oracle OCI MI355X GA 公告"

## 直接来源链接

1. <https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era>
2. <https://newsroom.amd.com/news/aai-2026-helios-update/>
3. <https://www.amd.com/content/dam/amd/en/documents/products/accelerators/instinct/amd-instinct-helios-blueprint-brochure.pdf>
4. <https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html>
5. <https://newsroom.amd.com/news/amd-and-its-partners-share-their-vision-for-ai-ev/>
6. <https://www.amd.com/en/products/rackscale-solutions/helios.html>
7. <https://www.amd.com/en/products/accelerators/instinct/mi400/mi455x.html>
8. <https://www.amd.com/en/products/accelerators/instinct.html>
9. <https://www.amd.com/en/products/accelerators/instinct/mi400/mi430x.html>
10. <https://blogs.oracle.com/cloud-infrastructure/announcing-general-availability-of-oci-amd-mi355x>

## 证据边界

- 这是资料重排页，不是重新发布或重新核验的产品公告。
- “发布、流片、送样、量产、出货、客户部署、云端可用、路线图、停产”等状态只在综合报告明确写出时保留；缺失项仍为“公开资料未确认”。
- 若摘录同时出现芯片、板卡、服务器、机架或云服务，均按原报告层级保留，并以“产品层级”字段提醒，不做跨层级推导。

## 关联表格原文（完整表格）

以下表格块来自综合报告中与本拆分项命中的表格，完整保留表头、状态列和规格列。

> 来源综合报告第 35-42 行：
> 第 35 行：| 时间/对象 | 已确认事实 | 尚不能推出的事实 |
> 第 36 行：|---|---|---|
> 第 37 行：| 2025-06-12，MI350X/MI355X | AMD 产品页给出 launch date；规格、功耗和 OAM 形态公开（**官方产品页规格**） | 产品页本身不等于每个地区现货、tape-out 或具体批量出货证明 |
> 第 38 行：| 2025-10-14，MI355X | OCI 宣布 BM.GPU.MI355X.8 GA，当前 OCI 文档仍给出 8 卡节点、ROCm/RCCL 验证路径（**云服务 GA/运营文档**） | 证明云端可租用，不代表 MI355X 的 AMD 单卡出货量或所有云厂商均可用 |
> 第 39 行：| 2025 年下半年，MI355X | AMD 资料称 Vultr 全球可用，财报称 MI350 系列需求强劲；这是商业部署和收入增长的证据（**厂商/伙伴发布、财报**） | 未披露逐型号出货数量、良率、每月产能或所有客户的验收状态 |
> 第 40 行：| 2026-01-05，MI440X/MI430X/MI500 | CES 发布会首次介绍 MI440X、MI430X 方向并预览 MI500（**厂商发布/路线图**） | 不等于 MI440X 已 GA，也不等于 MI430X/MI500 已量产 |
> 第 41 行：| 2026-07-23，MI455X/Helios | AMD 发布 MI455X 和 Helios；Helios 为 72 MI455X、18 EPYC Venice 的参考架构；AMD 还称 Helios “now in production”（**厂商发布**） | AMD 的 Helios 蓝图同时称其为 reference rack/reference architecture，且写 volume deployments expected in 2H 2026；OpenAI 计划从 Q4 2026 开始上线。二者共同证明“产品化与部署计划正在推进”，不构成独立的已安装出货数量（**冲突保留**） |
> 第 42 行：| 2026-08-28，MI355X KV | AMD ROCm 博客展示 2×MI355X 上的 4-bit KV/LMCache 分层测量（**厂商测试**） | 不是独立基准，也不能反推 MI455X 已在同一软件栈上达到相同结果 |

> 来源综合报告第 48-54 行：
> 第 48 行：| 层级 | 对象与数字 | 证据边界 |
> 第 49 行：|---|---|---|
> 第 50 行：| 芯片/封装 | MI455X：8 个 XCD、2 个 IOD、2 个 fabric/cache die；320B transistors；CDNA5、TSMC 2 nm + 3 nm FinFET | 这是官方架构/产品规格，不等于整机吞吐（**官方产品页/架构页**：[13]、[15]） |
> 第 51 行：| 加速器模块 | MI455X EAM：432 GB HBM4、12 stacks、23.3 TB/s、L2 192 MB、UALoE scale-up 3.6 TB/s 双向、UALink scale-out 600 GB/s 双向；DLC；TBP 未公开 | 互联数字是链路带宽，不是 Top-k 或检索 collective；不要把 MI355X 1400 W 移植到 MI455X |
> 第 52 行：| Compute tray | 4 个液冷 MI455X + 1 个 96-core EPYC Venice 主机 CPU | 是 Helios 蓝图中的托盘构成，不是单卡形态（**厂商蓝图**：[17]） |
> 第 53 行：| Helios rack | 18 个 1OU、1P:4G 托盘，即 72 个 GPU；6 个 switch tray；31 TB HBM4；1.67 PB/s 聚合 HBM 带宽；最高 2.9 EFLOPS OCP MXFP4；最高 260 TB/s rack scale-up，蓝图另给最高 43 TB/s rack scale-out | 72 GPU、EFLOPS 和 rack 带宽属于参考架构级数字；Helios 不是单一芯片，且不同 AMD 页面存在口径差异（**官方蓝图/厂商发布**：[14]、[17]） |
> 第 54 行：| 云服务 | OCI BM.GPU.MI355X.8：8×MI355X、约 2.3 TB HBM3E、128-core EPYC、3 TB DDR；文档用 288 GiB/卡，需与产品页的十进制 GB 区分 | 这是 MI355X 云 GA；截至截止日没有找到 MI455X 公共云 GA SKU，不把 Helios 伙伴计划写成已上线云服务（**云 GA/运营文档/未确认**：[18]、[19]） |

> 来源综合报告第 76-82 行：
> 第 76 行：| 结果 | 数字与条件 | 标签与限制 |
> 第 77 行：|---|---|---|
> 第 78 行：| MI355X 单卡，Llama2-70B Server | AMD 报告 100,282 tokens/s；对照 MI325X 32,028 tokens/s，约 3.1× | AMD 的提交/分析，MLCommons 轮次和结果注册表提供独立发布框架；精度分别涉及 FP4/FP8，不能只看倍数（**独立注册表中的厂商提交**） |
> 第 79 行：| MI355X 11 节点、87 GPU | Llama2-70B：Offline 1,042,110、Server 1,016,380、Interactive 785,522；AMD 报告 scale-out efficiency 93%、93%、98% | 特定软件、模型和节点配置的提交结果，不是所有 MI355X 集群的保证（**独立基准中的厂商提交**） |
> 第 80 行：| MI355X 12 节点、94 GPU | GPT-OSS-120B：Offline 1,031,070、Server 900,054 | 同上；不要把它写成单卡或 Helios 标准吞吐 |
> 第 81 行：| MI325X/MI300X v5.1 | MLCommons 页面可见例如 8×MI325X Server 32,027.6、8×MI300X Server 24,747.6；不同提交者和场景会变化 | 这是上一代独立结果，用于基线，不是 MI455X 的结果 |
> 第 82 行：| MI355X 4-bit KV/LMCache、长上下文 | 2×MI355X、约 100k context 的分层测试；8×MI355X、Kimi Linear 至 64M tokens 的长上下文实验 | AMD ROCm 博客厂商测试，非 MLCommons 独立结果；需保留模型、软件、并发和 KV 精度条件 |

> 来源综合报告第 88-95 行：
> 第 88 行：| 功能 | 截至截止日能确认的实现 | 不能确认的硬件结论 |
> 第 89 行：|---|---|---|
> 第 90 行：| Search / Indexer | MiniMax-M3 的 ROCm 软件路径有 indexer-key、按 KV head 的 sparse index 和 16×128-token block 选择 | 没有公开确认专用 Search Core、流式相似度单元或动态 Indexer silicon |
> 第 91 行：| Select / Top-k | 软件产生压缩 sparse block table；不同 KV head 可使用独立 top-k indexer | 没有公开确认 `MERGE_TOPK`、固定延迟 Top-k 或不物化 score 的硬件保证 |
> 第 92 行：| Reduce | 分布式 argmax 只 all-gather M×2 `(max,index)` 紧凑结果 | 这是软件通信/规约算法，不是已公开的 retrieval-specific reduce collective |
> 第 93 行：| Address / Gather | page-16 SHUFFLE、`asm_layout` 和 page-aware cache layout 处理软件寻址与布局 | 没有确认 KV page translator、indexed Gather DMA 或专用物理地址生成器 |
> 第 94 行：| KV | HBM4/HBM3E 容量、FP8/4 KV、LMCache HBM+CPU DRAM 分层；长上下文实验提供了实际约束 | 没有确认芯片原生动态 KV page management；MLA 的 KV 是否复制还取决于软件并行拓扑 |
> 第 95 行：| Route / 跨卡 | UALoE、UALink、RCCL 和 Helios 多平面网络提供通用通信底座 | 没有确认面向检索候选的 `P×k` 硬件路由或跨卡 Top-k collective |

> 来源综合报告第 118-126 行：
> 第 118 行：| 项目 | 规格 | 研究解读 |
> 第 119 行：|---|---|---|
> 第 120 行：| 制程/架构 | TSMC 2 nm + 3 nm FinFET；CDNA 5 | 8 个 XCD、2 个 I/O die；采用 chiplet 封装。（[1]、[2]，访问日期：2026-08-22。） |
> 第 121 行：| 计算单元 | 256 WGP、Wave32；AMD未另列 Matrix Core 数量 | 官方把 MI355X 的 256 CU 与 MI455X 的 256 WGP 分开命名，不能当作同名指标硬比。（[1]、[2]，访问日期：2026-08-22。） |
> 第 122 行：| 低精度/矩阵 | OCP MXFP4 40.3 PFLOPS；MXFP6、MXFP8、OCP FP8 各 20.1 PFLOPS；矩阵 FP16/BF16 各 5 PFLOPS；INT8 矩阵 5 POPS | 都是峰值理论值；部分结构化稀疏矩阵值可达 2 倍。（[1]、[3]，访问日期：2026-08-22。） |
> 第 123 行：| 片上/封装内存 | L2 192 MB；LDS SRAM 总量约 96 MB；432 GB HBM4、12 stacks | HBM4 是封装内 DRAM，不是 WGP 旁的 SRAM；容量适合放更大的 KV，但不自动改变访问模式。（[1]、[2]，访问日期：2026-08-22。） |
> 第 124 行：| 内存带宽 | 23.3 TB/s 峰值 | 芯片专页、CDNA 5 页面和 2026-07 数据表均采用该值。（[1]、[2]、[3]，访问日期：2026-08-22。） |
> 第 125 行：| 互联 | 主机 Infinity Fabric 256 GB/s 双向；UALoE scale-up 3.6 TB/s 双向；UALink scale-out 600 GB/s 双向 | 是通信路宽，不等于 Global Top-k 或检索 collective。（[2]、[3]，访问日期：2026-08-22。） |
> 第 126 行：| 功耗 | MI455X 单卡 TBP/TDP：公开资料未确认 | MI355X 的 1400 W 不能移植给 MI455X。（[1]、[7]，访问日期：2026-08-22。） |

> 来源综合报告第 142-149 行：
> 第 142 行：| 附件问题 | 直接解决 | 间接帮助 | 没解决/证据不足 |
> 第 143 行：|---|---|---|---|
> 第 144 行：| 密集计算 | WGP、Wave32、MXFP4/6/8、FP16/BF16/INT8 | Q/K 投影、attention、重排可用成熟 ROCm 内核 | 低精度峰值不保证不规则 Indexer 等比例加速。（[1]，访问日期：2026-08-22。） |
> 第 145 行：| Search / Indexer | 无专用单元公开 | HBM、L2、LDS、TDM 可降低候选 Key 的搬运压力 | 无动态地址生成、流式 score、Indexer 公式硬件化证据。（[2]，访问日期：2026-08-22。） |
> 第 146 行：| Select / score materialization | 片上缓存为 tile 保留提供基础 | 软件可做分块/融合 attention | 没有证据证明硬件保证“不物化完整 score”；TDM 不是 Top-k 引擎。（[2]，访问日期：2026-08-22。） |
> 第 147 行：| Reduce / Local-Global Top-k | 无公开 Top-k 或 Merge Top-k 原语 | WGP、ROCm/RCCL、跨卡带宽可承载软件实现 | 是否把全量 all-reduce 变为 `P×k` 候选合并，公开资料未确认。（[1]、[2]，访问日期：2026-08-22。） |
> 第 148 行：| Move / Gather / Address | TDM 直接利于规则 tile；CPU 可一致性访问 GPU 内存 | ROCm Infinity Context/hipFile 可直连 HBM 与网络存储，适合 KV 分层 | 没有 page-aware Gather、KV page translator、物理地址描述符；AIC 也不是离散 Gather。（[2]、[9]，访问日期：2026-08-22。） |
> 第 149 行：| Route / 跨卡 / TPOT、TTFT、Tokens/J | UALoE 3.6 TB/s、UALink 600 GB/s、72-GPU pod 改善通信底座 | 给 candidate-sharding 和小候选 Merge 留出路宽 | 没有 Retrieval-specific collective，也未找到 MI455X 在该类 workload 上同时报告 TPOT、TTFT、Tokens/J 的实测。Helios token throughput 是特定模型与输入输出长度下的 AMD 建模，不能替代端到端 benchmark。（[2]、[5]，访问日期：2026-08-22。） |

> 来源综合报告第 153-161 行：
> 第 153 行：| 维度 | 权重 | 得分 | 理由 |
> 第 154 行：|---|---:|---:|---|
> 第 155 行：| 数据搬运与存储 | 30% | 24 | HBM4、L2/LDS、TDM 很强，但没有离散 Gather 语义。 |
> 第 156 行：| 执行架构 | 20% | 15 | XCD/WGP/Wave32/chiplet 有价值，仍以通用平面为主。 |
> 第 157 行：| 稀疏/动态计算 | 15% | 6 | 有低精度与结构化稀疏，无动态 Search/Select/Top-k 证据。 |
> 第 158 行：| Scale-up/互联 | 15% | 14 | 3.6 TB/s、72-GPU pod 直接回应跨卡压力，但不是检索 collective。 |
> 第 159 行：| 数值格式/计算密度 | 10% | 9 | OCP MXFP4/6/8 规格完整，峰值不等于利用率。 |
> 第 160 行：| 可编程性 | 10% | 8 | ROCm/HIP/Triton/vLLM/SGLang 路径完整，未公开 Retrieval ISA。 |
> 第 161 行：| **合计** | **100%** | **76/100** | **偏强的 memory/scale-up 参考，不是 Retrieval Plane 成品。** |
