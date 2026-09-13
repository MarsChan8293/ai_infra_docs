# NVIDIA / 英伟达 — Blackwell 数据中心 GPU 家族

- 研究截止日：2026-09-05
- 核验日期：2026-09-05
- 厂商：NVIDIA
- 产品层级：数据中心 GPU 架构与其强绑定的 B200 GPU、GB200 Grace Blackwell Superchip、HGX/DGX/GB200 NVL72 系统
- 厂商总览：[NVIDIA / 英伟达](./NVIDIA-overview.md) · [[NVIDIA-overview|图谱总览]]
- 页面范围：把芯片、Superchip、板卡/服务器、机架和云服务分层记录。本文主线是 B200/GB200；不把 B200 规格回填到 GB200/NVL72，也不把当前页面中的 B300/GB300 Blackwell Ultra 规格混入基础 Blackwell。

## 一句话结论

Blackwell 是 NVIDIA 在 Hopper 之后的主流数据中心 GPU 代际，公开资料已完整确认双 reticle GPU die、10 TB/s 芯片内互联、TSMC 4NP、第二代 Transformer Engine、FP4、第五代 NVLink、RAS 和硬件解压缩引擎。B200 适合放在 HGX/DGX 八卡平台，GB200 则把两颗 B200 GPU 与一颗 Grace CPU 组成 Superchip，再扩展到 72 GPU 的 NVL72 机架。它显著增强了规则矩阵计算、低精度推理和跨卡通信，但公开资料仍没有证明存在独立 Search/Indexer、精确 Top-k 或 page-aware Indexed Gather DMA，因此不能把 Blackwell 直接写成完整 Retrieval GPU。

## 产品定位与对象边界

| 对象 | 层级 | 公开事实 | 不应混写的内容 |
|---|---|---|---|
| Blackwell GPU 架构 | 架构/芯片族 | 2080 亿晶体管、TSMC 4NP、两个 reticle-limited die 以 10 TB/s 芯片内链路组成统一 GPU | 2080 亿是架构 GPU 口径，不是某一张 DGX 或 NVL72 的总晶体管数 |
| B200 Tensor Core GPU | 单 GPU | 官方 HGX 文档给出 180GB HBM3e、最高 8TB/s GPU 内存带宽；B200 使用第五代 NVLink | HGX B200 的 144 PFLOPS、1.44TB 是八卡板级口径 |
| HGX B200 | 八 GPU 基板/服务器组件 | 8×B200、14.4TB/s GPU-to-GPU 聚合 NVLink 带宽；官方参考架构给出最高 400Gb/s 网络 | 不能将 14.4TB/s 写成单 B200 互联带宽 |
| DGX B200 | 八 GPU AI 服务器 | 8×Blackwell GPU、1,440GB 总 GPU 内存、64TB/s HBM3e 带宽、约 14.3kW 最大系统功耗 | 这是整机功耗，不能作为 B200 单 GPU TDP |
| GB200 Grace Blackwell Superchip | CPU+双 GPU Superchip | 2×B200 + 1×Grace CPU，GPU 与 Grace 通过 900GB/s NVLink-C2C 连接；官方 GB200 规格列出 372GB HBM3e、16TB/s GPU 内存带宽 | CPU 内存和 C2C 带宽属于 Superchip 边界 |
| GB200 NVL72 | 液冷机架系统 | 36 Grace CPU、72 Blackwell GPU；官方产品页列出 130TB/s NVLink 域、13.4TB HBM3e、576TB/s GPU 内存带宽 | 启动公告中“30TB fast memory”包含系统级快速内存，不能替换 13.4TB GPU HBM 口径 |
| Blackwell Ultra B300/GB300 | 后续刷新代际/系统 | NVIDIA GB200 产品页已出现 GB300 NVL72 说明；本页不把它并入 B200/GB200 的规格表 | B300/GB300 应单独记录芯片、系统和生命周期，不从 B200/GB200 推导 |

**B100 边界。** 早期 Blackwell 讨论中常出现 B100 名称，但本次核验使用的 NVIDIA 当前产品页、HGX/DGX 资料和 GB200 资料集中在 B200/GB200，未找到足以支撑独立 B100 芯片页的稳定官方规格和生命周期表。本页不把 B100 的传闻、合作伙伴 SKU 或 B200 数字回填为 B100 事实；如获得官方数据手册，再单独拆页。

## 生命周期状态

| 阶段 | Blackwell/B200/GB200 截至 2026-09-05 的公开状态 | 证据边界 |
|---|---|---|
| 架构/产品宣布 | **已确认**：NVIDIA 于 2024-03-18 发布 Blackwell 架构和 GB200/B200 平台叙事 | 新闻稿是正式发布材料；其中“性能、可用性和合作伙伴”部分含厂商主张或前瞻性表述。[S2] |
| 流片/工程样片 | **公开资料未确认** | 未找到 NVIDIA 对 B200/GB200 具体流片、工程样片批次或客户样片数量的直接披露。 |
| 量产 | **架构/平台层已确认 full production** | NVIDIA 当前 Blackwell 架构页标注“now in full production”，但没有逐 SKU 给出 B200、GB200 各自的批次、产能或封装良率。[S1] |
| 出货/合作伙伴供货 | **平台与系统层有证据** | NVIDIA 官方新闻稿列出服务器厂商、云服务商和合作伙伴；这些是平台可供合作伙伴集成的证据，不是每个 GPU SKU 的出货统计。[S2] |
| 客户部署 | **系统/云层有公开证据；单芯片客户规模未确认** | DGX B200、HGX B200、GB200 NVL72 产品页和 NVIDIA 的 MLPerf 结果证明系统被部署/测试；不能反推出 B200 单芯片客户数量。 |
| 云/实例可用 | **部分确认，按平台和区域分层** | 新闻稿列出首批云服务商；具体 B200/GB200 实例名称、区域、租用库存和 SLA 需以云厂商页面为准，NVIDIA 自身公告不替代云 SKU 清单。 |
| 路线图 | **B300/GB300 为 Blackwell Ultra 后续刷新** | 当前 GB200 页面提到 GB300 NVL72；本页不把它写成 B200/GB200 已验证规格。 |

## 芯片与平台规格

### Blackwell 架构与 B200 GPU

| 项目 | B200/Blackwell 公开口径 | 层级与状态 |
|---|---|---|
| 制程 | TSMC 4NP custom-built process | 架构 GPU 厂商公开事实；不是独立晶圆厂测试报告。[S1] |
| 晶体管与 die | 2080 亿晶体管；两个 reticle-limited GPU die 通过 10TB/s 芯片内链路组成统一 GPU | Blackwell GPU 架构层；不能与整机晶体管数混写。 |
| Tensor/数值格式 | 第二代 Transformer Engine；支持微张量缩放和 FP4；官方架构材料还描述 FP6/FP8 等低精度路径 | 这是硬件与软件协同能力；FP4 峰值要按具体 SKU、稀疏/稠密口径看。 |
| GPU 内存 | B200：180GB HBM3e；最高 8TB/s GPU 内存带宽 | B200 单 GPU 口径，来源为 NVIDIA 企业参考架构和 CUDA Blackwell 指南。[S5][S6] |
| GPU-to-GPU 互联 | 第五代 NVLink；B200 单 GPU 最高 1.8TB/s 双向，HGX B200 八卡板聚合 14.4TB/s | 单 GPU 与八卡板分开记录；不是 NVL72 130TB/s 的替代值。[S5][S6] |
| RAS/安全 | RAS engine、硬件级 confidential computing/接口加密能力 | 架构公开能力；不会自动带来 Retrieval 语义。 |
| 解压缩 | 专用 Decompression Engine，用于支持的压缩格式和数据处理路径 | 公开为 Blackwell 架构能力；nvCOMP 使用还受软件、缓冲区和格式约束。 |
| 单 GPU TDP、SM 数、L2 容量 | **公开资料未在本页统一确认** | 不从 DGX/HGX 的整机或板级功耗、吞吐反推。 |

### GB200 Superchip、HGX/DGX 与 NVL72

| 对象 | 公开规格 | 解释 |
|---|---|---|
| GB200 Grace Blackwell Superchip | 2×Blackwell GPU + 1×Grace CPU；900GB/s NVLink-C2C；372GB HBM3e、16TB/s GPU 内存带宽 | Superchip 层，不能写成单 B200 GPU 容量。来源：[GB200 NVL72 产品页](https://www.nvidia.com/en-us/data-center/gb200-nvl72/) |
| HGX B200 | 8×B200；每 GPU 180GB HBM3e，节点总计 1.44TB；GPU-to-GPU 1.8TB/s，聚合 14.4TB/s；板级 AI 性能 144 PFLOPS | 八卡基板/服务器组件层；板级 PFLOPS 不是单 GPU 独立 benchmark。来源：[HGX AI Factory 组件文档](https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory-h100-h200-b200/latest/components.html) |
| DGX B200 | 8×Blackwell GPU；1,440GB GPU memory；64TB/s HBM3e bandwidth；14.4TB/s aggregate NVLink；约 14.3kW 最大系统功耗 | AI 服务器层；官网的性能对比是投影/厂商口径，不是独立实测。来源：[DGX B200 产品页](https://www.nvidia.com/en-us/data-center/dgx-b200/) |
| GB200 NVL72 | 72 GPU + 36 Grace CPU；130TB/s NVLink domain；13.4TB HBM3e、576TB/s；液冷 rack-scale | 机架系统层；官方产品页同时展示 GB300 段落，本文只采用 GB200 表格数据。来源：[GB200 NVL72 产品页](https://www.nvidia.com/en-us/data-center/gb200-nvl72/) |

## 架构与检索路径映射

| 附件动作 | 直接解决 | 间接帮助 | 没有解决/证据不足 |
|---|---|---|---|
| Search / Indexer | **没有公开专用 Search/Indexer 单元** | HBM3e、Tensor Core 和低精度路径可以提升通用扫描/相似度计算吞吐 | 没有公开 ANN 索引、候选生成、向量数据库协处理器或检索 SRAM |
| Select / Local Top-k | **没有公开精确 Top-k 硬件原语** | Tensor Core、shared memory、软件 kernel 可实现候选筛选 | FP4/FP8、稀疏和更高带宽不等于扫描时 Top-k，也不证明 score 不落地 |
| Move | Blackwell 的统一 GPU die、HBM3e、NVLink 和专用解压缩引擎改善数据路径 | CUDA/库可以组织异步搬运、压缩数据解码和跨卡流水 | 没有公开按 page table/索引列表驱动的 Indexed Gather DMA |
| Route | 第五代 NVLink/NVSwitch 与 NVL72 单域直接支撑 GPU-GPU 通信 | GB200 的 NVLink-C2C 和 NVL72 的大域可用于 KV/专家并行的通信底座 | 通信路径不是 Retrieval-aware Route，不自动减少 candidate payload |
| Address | 双 die 统一 GPU、C2C/NVLink 和 CUDA 地址空间可支撑软件地址管理 | 可以把 descriptor、page metadata 和 tile 调度放进软件流水 | 没有公开 KV Page Translator、持久化 Gather queue 或物理地址描述符链 |
| Global Reduce | NVLink/NVSwitch 和集合通信软件可降低 Reduce 的链路瓶颈 | NVL72 的单 NVLink 域适合做模型并行/专家并行通信 | Reduce/SHARP/集合通信不等于 Global Merge Top-k；候选语义和精确率未公开 |
| 离散 KV Gather | **公开资料未确认专用硬件** | HBM3e、NVLink、压缩和软件内存层次可改善部分 KV 搬运 | page alignment、访存合并、page 数、跨卡 bytes/token 和尾延迟均未公开 |
| TPOT / TTFT / Tokens/J | 官方给出 GB200/DGX 的系统级投影和 MLPerf 结果 | 低精度、带宽、依赖调度和大 NVLink 域可能改善端到端指标 | 系统 benchmark 不能替代单 B200、特定 KV workload 的 TPOT/TTFT/Tokens/J 测量 |

## 性能与采用证据

| 证据对象 | 公开内容 | 证据状态与限制 |
|---|---|---|
| DGX B200 | NVIDIA 官网给出 8 GPU、1,440GB、64TB/s、约 14.3kW，并以 DGX H100 作训练/推理对比 | **厂商产品页/系统规格**；页面把实时推理和训练图表标为 projected，不能改写成单 GPU 独立实测。[DGX B200](https://www.nvidia.com/en-us/data-center/dgx-b200/) |
| GB200 NVL72 | 官方产品页给出 72 GPU、130TB/s NVLink 域，并以 H100 做 30x/4x/25x 系统级比较 | **厂商系统主张/特定 workload**；不代表 B200 单芯片性能或通用 TPOT。[GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72/) |
| MLPerf | NVIDIA 技术博客记录 Blackwell 在 MLPerf Training/Inference 中使用 GB200 NVL72 和 DGX B200 系统 | **独立组织验证结果的厂商解读**；软件、模型、并行映射和系统规模必须保留，不能抽成单芯片通用倍数。[Blackwell MLPerf](https://developer.nvidia.com/blog/nvidia-blackwell-delivers-massive-performance-leaps-in-mlperf-inference-v5-0/) |
| 云和服务器供货 | NVIDIA 2024 新闻稿列出 AWS、Google Cloud、Microsoft Azure、OCI 等首批云伙伴和服务器生态 | **平台供货/伙伴公告**；具体区域、价格、实例型号和库存需要分别核验。[Blackwell 发布](https://nvidianews.nvidia.com/news/nvidia-blackwell-platform-arrives-to-power-a-new-era-of-computing) |

## 未确认项与常见误读

1. **B200 ≠ GB200 ≠ NVL72。** B200 是 GPU，GB200 是 Grace CPU + 两颗 GPU 的 Superchip，NVL72 是 72 GPU/36 CPU 的机架系统；三者的内存、功耗和带宽不能互换。
2. **180GB ≠ 1.44TB ≠ 13.4TB。** 180GB 是单 B200，1.44TB 是 HGX B200 八卡节点，13.4TB 是 GB200 NVL72 的 GPU HBM 总量。系统还可能有 Grace CPU 的 LPDDR5X，不能混入 GPU HBM。
3. **1.8TB/s ≠ 14.4TB/s ≠ 130TB/s。** 依次对应 B200 单 GPU、HGX 八卡聚合、NVL72 NVLink 域；不能相加或回填到单芯片。
4. **FP4/FP6/Transformer Engine ≠ Retrieval。** 低精度和微张量缩放提升规则矩阵/推理密度，不等于动态精确 Search、Top-k 或 Indexed Gather。
5. **系统 benchmark ≠ 芯片 benchmark。** DGX/GB200 的性能和能效数字受模型、序列长度、精度、软件版本、并行映射、冷却和网络影响，不能直接写成 B200 的 TPOT、TTFT 或 J/token。
6. **Blackwell Ultra 不回填。** 当前官方 GB200 页面出现 GB300 NVL72 说明；B300/GB300 是后续刷新边界，需单独建立芯片/系统证据页。

## 对下一代 Retrieval GPU 的可借鉴点

- **可直接借鉴**：把双 die 统一地址/通信路径、片上高速互联和低精度 Transformer Engine 作为密集计算与数据移动的共同底座。
- **可直接借鉴**：将硬件解压缩和 GPU-GPU 高带宽链路放到 KV/权重搬运流水中，减少通用 SM 被解压和等待占用的时间。
- **只能类比**：NVLink/NVSwitch/NVL72 适合作为 Global candidate merge 的通信底座，但仍需单独设计 Top-k 语义和候选压缩协议。
- **不宜照搬**：不要把 2:4、FP4 或系统级 tokens/s 直接当作动态离散 KV 的收益；Exact Mode 仍需测 HBM bytes/token、inter-GPU bytes/token、TPOT 和 TTFT。

## 直接来源清单

1. **S1｜NVIDIA Blackwell Architecture**；核验日期：2026-09-05；直接 URL：[https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/)。用于 2080 亿晶体管、TSMC 4NP、双 die、10TB/s、full production 和架构创新。
2. **S2｜NVIDIA Blackwell Platform Arrives to Power a New Era of Computing**；发布日期：2024-03-18；核验日期：2026-09-05；直接 URL：[https://nvidianews.nvidia.com/news/nvidia-blackwell-platform-arrives-to-power-a-new-era-of-computing](https://nvidianews.nvidia.com/news/nvidia-blackwell-platform-arrives-to-power-a-new-era-of-computing)。用于 B200/GB200/NVL72/HGX B200 产品边界和合作伙伴公告。
3. **S3｜NVIDIA GB200 NVL72**；核验日期：2026-09-05；直接 URL：[https://www.nvidia.com/en-us/data-center/gb200-nvl72/](https://www.nvidia.com/en-us/data-center/gb200-nvl72/)。用于 GB200 Superchip、NVL72 机架、NVLink 域和当前 GPU HBM 规格。
4. **S4｜NVIDIA DGX B200**；核验日期：2026-09-05；直接 URL：[https://www.nvidia.com/en-us/data-center/dgx-b200/](https://www.nvidia.com/en-us/data-center/dgx-b200/)。用于 DGX B200 的八卡、内存、带宽、互联和系统功耗。
5. **S5｜NVIDIA HGX AI Factory H100/H200/B200 组件文档**；核验日期：2026-09-05；直接 URL：[https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory-h100-h200-b200/latest/components.html](https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory-h100-h200-b200/latest/components.html)。用于 B200 180GB HBM3e、8TB/s、1.8TB/s/GPU 和 HGX 节点边界。
6. **S6｜NVIDIA Blackwell Tuning Guide**；核验日期：2026-09-05；直接 URL：[https://docs.nvidia.com/cuda/blackwell-tuning-guide/](https://docs.nvidia.com/cuda/blackwell-tuning-guide/)。用于 B200 HBM3/HBM3e 支持、180GB 上限、L2/共享内存和软件可编程边界。
7. **S7｜NVIDIA Blackwell MLPerf 技术博客**；核验日期：2026-09-05；直接 URL：[https://developer.nvidia.com/blog/nvidia-blackwell-delivers-massive-performance-leaps-in-mlperf-inference-v5-0/](https://developer.nvidia.com/blog/nvidia-blackwell-delivers-massive-performance-leaps-in-mlperf-inference-v5-0/)。用于系统级 MLPerf/部署证据，保留模型和系统边界。

## 证据边界

- 芯片、Superchip、板卡/基板、服务器、机架、集群、网络、软件和云服务按来源原层级记录。
- 宣布、流片/工程样片、送样、量产、出货、客户部署、云实例可用和路线图分别判断；没有直接证据的阶段写“公开资料未确认”。
- NVIDIA 官方产品页、厂商 benchmark、MLPerf 结果和本文架构分析不混写；没有公开的 Search、Top-k、KV page translator 或 Indexed Gather 硬件事实，不从 CUDA/TensorRT/NVLink 邻近能力推导。
