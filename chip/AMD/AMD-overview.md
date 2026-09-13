# AMD Instinct 与芯片：2025-06 之后最新款

## 芯片页关系导航

本页是本目录唯一的厂家总览。下面的页面均按单一芯片、芯片家族或芯片关联产品对象拆分；芯片页中的“厂商总览”链接回到本页。`[[...]]` 用于 Obsidian 图谱，Markdown 链接用于普通阅读。

- [[mi100|AMD Instinct MI100 — 芯片与产品证据页]] · [打开 Markdown](./mi100.md)
- [[mi210|AMD Instinct MI210 — 芯片与产品证据页]] · [打开 Markdown](./mi210.md)
- [[mi250|AMD Instinct MI250 — 芯片与产品证据页]] · [打开 Markdown](./mi250.md)
- [[mi250x|AMD Instinct MI250X — 芯片与产品证据页]] · [打开 Markdown](./mi250x.md)
- [[mi300a|AMD Instinct MI300A — 芯片与产品证据页]] · [打开 Markdown](./mi300a.md)
- [[mi300x|AMD Instinct MI300X — 芯片与产品证据页]] · [打开 Markdown](./mi300x.md)
- [[mi325x|AMD Instinct MI325X — 芯片与产品证据页]] · [打开 Markdown](./mi325x.md)
- [[mi350p|AMD Instinct MI350P — 芯片与产品证据页]] · [打开 Markdown](./mi350p.md)
- [[mi350x|AMD Instinct MI350X — 芯片与产品证据页]] · [打开 Markdown](./mi350x.md)
- [[mi355x|AMD Instinct MI355X — 芯片与产品证据页]] · [打开 Markdown](./mi355x.md)
- [[mi430x|AMD Instinct MI430X — 芯片与产品证据页]] · [打开 Markdown](./mi430x.md)
- [[mi440x|AMD Instinct MI440X — 芯片与产品证据页]] · [打开 Markdown](./mi440x.md)
- [[mi455x|AMD Instinct MI455X — 芯片与产品证据页]] · [打开 Markdown](./mi455x.md)
- [[mi500|AMD Instinct MI500 — 芯片家族路线图证据页]] · [打开 Markdown](./mi500.md)

> 范围：AMD Instinct；目标时间：2025-07-01 至 2026-09-01；最新资料访问日期：2026-09-01。原有 2026-08-22 章节作为历史快照保留。对照基线为《推导推理GPU新路径-ELI5.html》（当前目录未提供）。

## 2026-09-01 核验更新

> 本节是在原有 2026-08-22 记录上的补充，原文各节保留。资料截止 2026-09-01。为避免把产品、系统、云服务和推理软件混为一谈，本文使用以下状态标签：**官方产品页规格**、**厂商/伙伴发布**、**云服务 GA**、**独立基准**、**厂商测试**、**分析判断**、**未确认**。除非特别说明，“发布”不等于“量产出货”，“规划”不等于“客户已部署”。

### 更新后的结论

截至 2026-09-01，公开产品组合中最新的前沿 AI 加速器仍是 **MI455X**；新增需要补入家族视图的已公开产品是面向既有服务器形态的 **MI350P**。MI455X 的芯片、封装内存和 scale-up 规格已经较完整，但 AMD 尚未公开单卡 TBP，也没有公开确认 MI455X 的 tape-out、sampling、逐卡量产或独立出货数量。Helios 是由 MI455X 组成的 72-GPU 机架级参考架构，不应当写成一张可单独购买的“Helios 芯片”。（**官方产品页规格/厂商发布**：[12]、[13]、[14]。）

与附件 Retrieval Plane 的关系需要更新得更精确：截至本截止日，ROCm 的确已经公开了针对 MiniMax-M3 的 sparse indexer、page-16 SHUFFLE、indexer-key cache 和软件 Top-k/分布式 argmax 路径；这证明 AMD 软件栈可以实现部分 Search、Select、Address、KV 和 Reduce 逻辑。但公开资料仍没有确认 MI455X 内置专用的 Search/Reduce/Top-k 硬件、KV page translator、indexed-gather DMA 或 retrieval-specific collective。因此“软件已经出现检索路径”与“芯片有专用 Retrieval Plane”必须分开。（**厂商软件技术说明/分析判断**：[25]、[26]、[27]。）

### 产品家族、代际与状态矩阵

| 产品 | 首发/公开时间 | 架构与形态 | 关键公开规格 | 截至 2026-09-01 的状态 |
|---|---|---|---|---|
| MI100 | 2020-11-16 | CDNA；PCIe 卡 | 32 GB HBM2，1.2 TB/s，300 W peak | 老一代产品页仍在；未找到 AMD 明确 EOL 公告（**官方页/未确认**） |
| MI200：MI210、MI250、MI250X | 2021-11-08；MI210 为 2022-03-22 | CDNA2；PCIe 或 OAM | 64/128 GB HBM2e，1.6/3.2 TB/s | 旧代 HPC 产品；未找到明确 EOL 公告（**官方页/未确认**） |
| MI300A、MI300X | 2023-12-06 | CDNA3；APU 或 OAM | MI300X 192 GB HBM3，5.3 TB/s，750 W | 已进入部署与云服务生态；是上一代主力（**官方页/云与伙伴资料**） |
| MI325X | 2024-10-10 | CDNA3；OAM | 256 GB HBM3E，6 TB/s，1000 W peak | 上一代大显存 AI 主力；OCI 已 GA（**官方页/云服务 GA**） |
| MI350X | 2025-06-12 | CDNA4；OAM | 288 GB HBM3E，8 TB/s，1000 W TBP | 当前 MI350 主系列；AMD 10-Q 称其需求推动数据中心增长（**官方页/财报**） |
| MI355X | 2025-06-12 | CDNA4；OAM | 288 GB HBM3E，8 TB/s，1400 W TBP | 当前旗舰级已公开部署型号；OCI BM.GPU.MI355X.8 已 GA，Vultr 也曾宣布可用（**官方页/云服务 GA**） |
| MI350P | 2026-07-23 发布会纳入产品组合；产品页 launch 字段为空 | CDNA4；PCIe FHFL 双槽卡 | 144 GB HBM3E，4 TB/s，600 W max、450 W configurable | 面向既有基础设施的已公开 PCIe 型号；确切 GA、量产和出货量未确认（**官方规格/未确认**） |
| MI440X | 2026-01-05 首次介绍 | MI400 家族企业本地 AI 形态；八 GPU 系统方向 | 公开材料强调紧凑 8-GPU 形态，未找到同等完整的芯片数据表 | 预览/系统方案状态；未找到公开完整芯片规格、GA 或量产日期（**厂商发布/未确认**） |
| MI430X | CES 2026 公开，产品页写预计 2027 可用 | CDNA5 变体；HPC/主权 AI | 432 GB HBM4，23.3 TB/s，最高 288 TFLOPS FP64 | 2027 规划产品；Discovery、Alice Recoque、Herder 是预期系统，不是当前出货证明（**官方产品页/路线图**） |
| MI455X | 2026-07-23 | CDNA5；EAM 模块 | 432 GB HBM4，23.3 TB/s，40.3 PFLOPS OCP MXFP4 | 最新公开前沿 AI 加速器；已发布，有伙伴部署计划，但逐卡量产/出货数量未确认（**官方产品页/厂商与伙伴发布**） |
| MI500 | 2026-01-05 预览 | 计划 CDNA6、2 nm、HBM4E | AMD 以路线图/工程预测口径描述 | 计划 2027；不可当作 2026 可用产品，性能倍数是厂商预测（**路线图**） |

这里的“当前/上一代”是产品组合和公开可用性判断，不代表旧型号已经停产。AMD 当前产品组合仍列出 MI100、MI200、MI300、MI325、MI350 和 MI400 家族；本轮检查没有找到针对 MI100、MI200 或 MI300 的明确停产日期或 EOL 通知，因此统一标为“旧代/未确认停产”，不把产品页下线或新家族发布推断为 EOL。（**官方产品组合/未确认**：[12]、[28]。）

### 时间线：首曝、发布、生产、出货和云可用性分开

| 时间/对象 | 已确认事实 | 尚不能推出的事实 |
|---|---|---|
| 2025-06-12，MI350X/MI355X | AMD 产品页给出 launch date；规格、功耗和 OAM 形态公开（**官方产品页规格**） | 产品页本身不等于每个地区现货、tape-out 或具体批量出货证明 |
| 2025-10-14，MI355X | OCI 宣布 BM.GPU.MI355X.8 GA，当前 OCI 文档仍给出 8 卡节点、ROCm/RCCL 验证路径（**云服务 GA/运营文档**） | 证明云端可租用，不代表 MI355X 的 AMD 单卡出货量或所有云厂商均可用 |
| 2025 年下半年，MI355X | AMD 资料称 Vultr 全球可用，财报称 MI350 系列需求强劲；这是商业部署和收入增长的证据（**厂商/伙伴发布、财报**） | 未披露逐型号出货数量、良率、每月产能或所有客户的验收状态 |
| 2026-01-05，MI440X/MI430X/MI500 | CES 发布会首次介绍 MI440X、MI430X 方向并预览 MI500（**厂商发布/路线图**） | 不等于 MI440X 已 GA，也不等于 MI430X/MI500 已量产 |
| 2026-07-23，MI455X/Helios | AMD 发布 MI455X 和 Helios；Helios 为 72 MI455X、18 EPYC Venice 的参考架构；AMD 还称 Helios “now in production”（**厂商发布**） | AMD 的 Helios 蓝图同时称其为 reference rack/reference architecture，且写 volume deployments expected in 2H 2026；OpenAI 计划从 Q4 2026 开始上线。二者共同证明“产品化与部署计划正在推进”，不构成独立的已安装出货数量（**冲突保留**） |
| 2026-08-28，MI355X KV | AMD ROCm 博客展示 2×MI355X 上的 4-bit KV/LMCache 分层测量（**厂商测试**） | 不是独立基准，也不能反推 MI455X 已在同一软件栈上达到相同结果 |

公开资料中没有给出 MI350/MI400 的明确 tape-out 或 sampling 日期，也没有给出 MI455X 的单卡 mass-production start、ship date、累计出货量或客户验收清单。应写成“发布日期已确认、部分上一代云服务已 GA、MI455X/Helios 的厂商生产与伙伴部署叙事已公开、精确量产和出货量未确认”。

### 分层规格：芯片、加速器、托盘、机架、云服务

| 层级 | 对象与数字 | 证据边界 |
|---|---|---|
| 芯片/封装 | MI455X：8 个 XCD、2 个 IOD、2 个 fabric/cache die；320B transistors；CDNA5、TSMC 2 nm + 3 nm FinFET | 这是官方架构/产品规格，不等于整机吞吐（**官方产品页/架构页**：[13]、[15]） |
| 加速器模块 | MI455X EAM：432 GB HBM4、12 stacks、23.3 TB/s、L2 192 MB、UALoE scale-up 3.6 TB/s 双向、UALink scale-out 600 GB/s 双向；DLC；TBP 未公开 | 互联数字是链路带宽，不是 Top-k 或检索 collective；不要把 MI355X 1400 W 移植到 MI455X |
| Compute tray | 4 个液冷 MI455X + 1 个 96-core EPYC Venice 主机 CPU | 是 Helios 蓝图中的托盘构成，不是单卡形态（**厂商蓝图**：[17]） |
| Helios rack | 18 个 1OU、1P:4G 托盘，即 72 个 GPU；6 个 switch tray；31 TB HBM4；1.67 PB/s 聚合 HBM 带宽；最高 2.9 EFLOPS OCP MXFP4；最高 260 TB/s rack scale-up，蓝图另给最高 43 TB/s rack scale-out | 72 GPU、EFLOPS 和 rack 带宽属于参考架构级数字；Helios 不是单一芯片，且不同 AMD 页面存在口径差异（**官方蓝图/厂商发布**：[14]、[17]） |
| 云服务 | OCI BM.GPU.MI355X.8：8×MI355X、约 2.3 TB HBM3E、128-core EPYC、3 TB DDR；文档用 288 GiB/卡，需与产品页的十进制 GB 区分 | 这是 MI355X 云 GA；截至截止日没有找到 MI455X 公共云 GA SKU，不把 Helios 伙伴计划写成已上线云服务（**云 GA/运营文档/未确认**：[18]、[19]） |

### 架构、软件与 AI 工作负载证据

CDNA5 的公开架构信息包括 Wave32、256 WGP、TDM、L2 multicast、WGP clustering、split-named barriers、2 个 IOD、2 个 fabric/cache die，以及 36 条 UALoE link。TDM 支持描述符驱动的异步张量搬运，并可在 LDS 与 DRAM 间绕过寄存器；这强化了规则 tile 的 Move 路径和片上数据复用，但本身不是动态检索执行器。（**官方架构说明/分析判断**：[15]。）

软件证据已经比 2026-08-22 的原文更具体。AMD 的 ROCm MiniMax-M3 说明记录了以下实现：

- 每个 KV head 的 indexer 选择 16 个逻辑 block，每个 block 为 128 tokens；不同 KV head 使用分开的 top-k indexer。
- sparse index 的 Top-k 路径直接输出压缩后的 sparse block table，减少额外 kernel launch 和 HBM round trip。
- AITER 使用 `fused_qknorm_idxrqknorm`，并用 page-16 SHUFFLE 的 `asm_layout` 处理寻址。
- ATOMesh 同时迁移普通 KV cache 和不能在 cache hit 后重新构造的 indexer-key cache。
- 分布式 argmax 将每个 rank 的 M×N logits 压缩为 M×2 的 `(max,index)`，再只 all-gather 紧凑结果；这是软件算法，不是已经确认的硬件 Top-k collective。

这些材料可支持“ROCm 针对特定模型实现了 software indexer、Top-k、page-aware layout 和 KV 分层”的判断，但不能支持“MI455X 硬件内建 Retrieval Core”。此外，AMD 的 4-bit KV/LMCache 测试显示 HBM+CPU DRAM 分层在 2×MI355X、ROCm 7.2.3、vLLM V1、约 100k context 和 32–64 users 条件下可提高同一速度目标下的请求数；AMD 也明确跨机器共享 cache 仍是未来方向。长上下文测试则显示 8-GPU MI355X 节点上的某些 MLA 实现会按 rank 复制 KV cache。两者都是**厂商工程测量**，不能代替独立 benchmark，也不能直接推广到 MI455X。（[25]、[26]、[27]。）

### 独立基准与厂商测试分开

MLCommons Inference v6.0 是独立组织发布的结果集，且 Closed division 要求同模型、同类配置进行可比提交；Open division 允许不同模型或重训练，Available 表示组件可购买或云租赁，Preview/RDI 则不能等同成熟可交付产品。功耗还是整机墙上 AC 测量，不是 GPU TBP。（**独立基准规则**：[20]、[21]。）

截至截止日可引用的数字应这样写：

| 结果 | 数字与条件 | 标签与限制 |
|---|---|---|
| MI355X 单卡，Llama2-70B Server | AMD 报告 100,282 tokens/s；对照 MI325X 32,028 tokens/s，约 3.1× | AMD 的提交/分析，MLCommons 轮次和结果注册表提供独立发布框架；精度分别涉及 FP4/FP8，不能只看倍数（**独立注册表中的厂商提交**） |
| MI355X 11 节点、87 GPU | Llama2-70B：Offline 1,042,110、Server 1,016,380、Interactive 785,522；AMD 报告 scale-out efficiency 93%、93%、98% | 特定软件、模型和节点配置的提交结果，不是所有 MI355X 集群的保证（**独立基准中的厂商提交**） |
| MI355X 12 节点、94 GPU | GPT-OSS-120B：Offline 1,031,070、Server 900,054 | 同上；不要把它写成单卡或 Helios 标准吞吐 |
| MI325X/MI300X v5.1 | MLCommons 页面可见例如 8×MI325X Server 32,027.6、8×MI300X Server 24,747.6；不同提交者和场景会变化 | 这是上一代独立结果，用于基线，不是 MI455X 的结果 |
| MI355X 4-bit KV/LMCache、长上下文 | 2×MI355X、约 100k context 的分层测试；8×MI355X、Kimi Linear 至 64M tokens 的长上下文实验 | AMD ROCm 博客厂商测试，非 MLCommons 独立结果；需保留模型、软件、并发和 KV 精度条件 |

AMD 还报告 MI355X 在 MLPerf Training 6.0 中与 B200 在特定 fine-tuning/pretraining 项目相差约 5%–6%，并报告首次多节点 FLUX 提交等结果。由于精度、软件和提交配置不同，这些数字只能作为对应 benchmark 条件下的结果，不能概括为“MI355X 全面等于/超过 B200”。（**独立基准中的 AMD 提交/厂商解读**：[22]、[23]、[24]。）

### Retrieval Plane 证据边界（更新版）

| 功能 | 截至截止日能确认的实现 | 不能确认的硬件结论 |
|---|---|---|
| Search / Indexer | MiniMax-M3 的 ROCm 软件路径有 indexer-key、按 KV head 的 sparse index 和 16×128-token block 选择 | 没有公开确认专用 Search Core、流式相似度单元或动态 Indexer silicon |
| Select / Top-k | 软件产生压缩 sparse block table；不同 KV head 可使用独立 top-k indexer | 没有公开确认 `MERGE_TOPK`、固定延迟 Top-k 或不物化 score 的硬件保证 |
| Reduce | 分布式 argmax 只 all-gather M×2 `(max,index)` 紧凑结果 | 这是软件通信/规约算法，不是已公开的 retrieval-specific reduce collective |
| Address / Gather | page-16 SHUFFLE、`asm_layout` 和 page-aware cache layout 处理软件寻址与布局 | 没有确认 KV page translator、indexed Gather DMA 或专用物理地址生成器 |
| KV | HBM4/HBM3E 容量、FP8/4 KV、LMCache HBM+CPU DRAM 分层；长上下文实验提供了实际约束 | 没有确认芯片原生动态 KV page management；MLA 的 KV 是否复制还取决于软件并行拓扑 |
| Route / 跨卡 | UALoE、UALink、RCCL 和 Helios 多平面网络提供通用通信底座 | 没有确认面向检索候选的 `P×k` 硬件路由或跨卡 Top-k collective |

因此，原文“没有 Search/Select/Address 的公开专用硬件证据”仍然成立，但“软件没有实现 Indexer/Top-k”已经过时，应改读为“软件已有特定模型实现，硬件专用单元仍未确认”。这也是本报告对附件 Retrieval Plane 最重要的边界修正。（**分析判断**。）

### 资料冲突与研究判断

1. **19.6 TB/s 与 23.3 TB/s。** 旧有 Helios/工程材料的某个 compute-tray 段落写每 GPU 19.6 TB/s；当前 MI455X 产品页、CDNA5 架构页和 2026-07 brochure 写 23.3 TB/s。AMD 没有公开解释差异，本文将 23.3 TB/s 作为当前单卡规格，把 19.6 TB/s 保留为历史材料，不混合推导。
2. **Helios 的“生产”与“参考架构”。** AAI 2026 使用“now in production”叙述；Helios 蓝图仍称 reference architecture，并写 volume deployments expected 2H 2026。记录为“厂商称已进入生产/部署推进”，不能升级为独立确认的量产出货。
3. **MI455X 峰值与端到端指标。** 40.3 PFLOPS MXFP4、2.9 EFLOPS Helios 是峰值或特定系统级口径，不是 TPOT、TTFT、tokens/J；MLPerf 数字也只能在对应模型、精度和系统配置内解释。
4. **评分保持分析属性。** 原文 76/100 仍可作为对“通用 memory/scale-up 路线”的研究判断；考虑到当前软件已有 sparse indexer/top-k 路径，软件检索能力的描述应更新，但没有足够证据把硬件 Retrieval Plane 得分上调为已实现。

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

附件把新推理 GPU 的问题拆成四类：密集计算、动态检索/Indexer、Top-k/Reduce、离散 KV Gather 与跨卡通信。Indexer 要在运行时找候选、算分、保留 Top-k，再把离散索引翻译成 KV page 和物理地址；长上下文下，成本不只有 GEMM，还包括 DRAM 请求、地址 bookkeeping 和跨卡搬运。（原始附件当前目录未提供；另见 [2]，访问日期：2026-08-22。）

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

## 2026-09-01 在线复核增补

已重新打开 [MI455X 官方产品页](https://www.amd.com/en/products/accelerators/instinct/mi400/mi455x.html) 和 [AMD Instinct 产品总览](https://www.amd.com/en/products/accelerators/instinct.html)，确认 MI455X 仍列为 2026-07-23 发布、CDNA5、432GB HBM4、23.3TB/s；[Helios 页面](https://www.amd.com/en/products/rackscale-solutions/helios.html)仍将 72 GPU 明确为机架级设计。上述数字不能回填单 GPU 功耗或现货状态。

### 2026-09-01 更新所用来源

[12]: https://www.amd.com/en/products/accelerators/instinct.html "AMD Instinct 产品总览"
[13]: https://www.amd.com/en/products/accelerators/instinct/mi400/mi455x.html "AMD Instinct MI455X 产品页"
[14]: https://www.amd.com/en/products/accelerators/instinct/mi400.html "AMD Instinct MI400 家族页"
[15]: https://www.amd.com/en/technologies/cdna.html "AMD CDNA 架构页"
[16]: https://www.amd.com/en/products/accelerators/instinct/mi400/mi430x.html "AMD Instinct MI430X 产品页"
[17]: https://www.amd.com/content/dam/amd/en/documents/products/accelerators/instinct/amd-instinct-helios-blueprint-brochure.pdf "AMD Helios Blueprint"
[18]: https://blogs.oracle.com/cloud-infrastructure/announcing-general-availability-of-oci-amd-mi355x "Oracle OCI MI355X GA 公告"
[19]: https://docs.oracle.com/en-us/iaas/Content/Compute/gpu-quick-start/amd/MI355X/README-MI355X.htm "Oracle MI355X Quick Start"
[20]: https://mlcommons.org/2026/04/mlperf-inference-v6-0-results/ "MLCommons MLPerf Inference v6.0 发布"
[21]: https://mlcommons.org/benchmarks/inference-datacenter/ "MLCommons Inference Datacenter 规则与结果"
[22]: https://www.amd.com/en/blogs/2026/amd-delivers-breakthrough-mlperf-inference-6-0-results.html "AMD MLPerf Inference 6.0 结果说明"
[23]: https://www.amd.com/en/blogs/2026/amd-delivers-breakthrough-mlperf-training-6-0-results.html "AMD MLPerf Training 6.0 结果说明"
[24]: https://docs.mlcommons.org/inference_results_v5.1/ "MLCommons MLPerf Inference v5.1 结果"
[25]: https://rocm.blogs.amd.com/artificial-intelligence/minimax-m3-mi355/README.html "ROCm MiniMax-M3 与 MI355X 软件优化"
[26]: https://rocm.blogs.amd.com/software-tools-optimization/4bit-KV-LMcache/README.html "ROCm 4-bit KV 与 LMCache"
[27]: https://rocm.blogs.amd.com/artificial-intelligence/long-context-serving/README.html "ROCm Long Context Serving"
[28]: https://ir.amd.com/financial-information/sec-filings/content/0000002488-26-000018/amd-20251227.htm "AMD 2025 Form 10-K"
[29]: https://ir.amd.com/financial-information/sec-filings/content/0000002488-26-000123/amd-20260627.htm "AMD 2026 Q2 Form 10-Q"
[30]: https://ir.amd.com/financial-information/sec-filings/content/0000002488-26-000121/amdq22026earningsslidesf.htm "AMD Q2 2026 Earnings Slides"
[31]: https://ir.amd.com/news-events/press-releases/detail/1272/amd-and-its-partners-share-their-vision-for-ai-everywhere-for-everyone-at-ces-2026 "AMD CES 2026 新闻稿"
[32]: https://www.amd.com/en/products/accelerators/instinct/mi350/mi350p.html "AMD Instinct MI350P 产品页"
[33]: https://www.amd.com/en/products/accelerators/instinct/mi350/mi350x.html "AMD Instinct MI350X 产品页"
[34]: https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html "AMD Instinct MI355X 产品页"
[35]: https://mlcommons.org/2025/09/mlperf-inference-v5-1-results/ "MLCommons MLPerf Inference v5.1 发布"
[36]: https://rocm.blogs.amd.com/artificial-intelligence/mlperf-inference-v5.1/README.html "ROCm MLPerf Inference v5.1 说明"
[37]: https://newsroom.amd.com/news/amd-reports-third-quarter-2025-financial-results/ "AMD 2025 Q3 财报新闻稿"
[38]: https://www.amd.com/en/solutions/ai/trust-your-instinct.html "AMD Instinct AI 基础设施与客户案例"
[39]: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/nd-family "Azure ND MI300X v5 文档"
[40]: https://instinct.docs.amd.com/projects/cluster-documentation/latest/reference/hardware-support.html "AMD Instinct ROCm 硬件支持矩阵"
