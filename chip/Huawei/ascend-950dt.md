# Huawei / 华为昇腾 — Ascend 950DT

- 研究截止日：2026-09-05
- 核验日期：2026-09-05
- 厂商：华为技术有限公司
- 产品层级：AI 加速芯片；公开资料同时描述了包含多 Die、片上高速内存和 I/O Die 的完整封装
- 厂商总览：[华为昇腾](./华为-概览.md) · [[华为-概览|图谱总览]]
- 页面范围：只判断 Ascend 950DT 芯片/封装本身。Atlas 850E、Atlas 650E、Atlas 950 和 Atlas 950 SuperPoD 是服务器/超节点产品形态；它们的卡数、系统内存、液冷、供电和系统性能不回填为芯片规格。

## 一句话结论

已确认华为在 2025-09-18 将 Ascend 950DT 定位为面向 Decode 与训练的 Ascend 950 系列芯片，白皮书给出 144/96 GB、4 TB/s 片上高速内存和 2 TB/s 级 Unified Bus 等芯片级规格；昇腾产品总览与 Atlas 950 SuperPoD 页面已把 950DT 关联到具体系统形态，但截至 2026-09-05，950DT 的流片/样片、送样、芯片量产、芯片出货、芯片客户部署和云实例可用性仍未被公开资料分别确认，2026 年第四季度仍是路线图目标。[华为路线图](https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech) [昇腾 950 NPU 架构白皮书](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)

## 产品定位与对象边界

### 已确认事实

1. 华为 2025 年路线图称 Ascend 950PR 与 Ascend 950DT 共用 Ascend 950 Die；950DT 面向推理 Decode 阶段和训练，采用 HiZQ 2.0，目标为 2026 年第四季度推出。该页面是正式发布/路线图证据，不等同于芯片已量产或出货。[华为路线图](https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech)
2. 《昇腾 950 NPU 架构白皮书》把 950DT 描述为与 950PR 共架构、采用不同片上高速内存配置的多 Die 合封芯片，包含 2 个 AI Die、2 个 I/O Die 和 4 个高速片上内存模块。[昇腾 950 NPU 架构白皮书](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)
3. 昇腾社区的产品总览将 Ascend 950DT 映射到 Atlas 850E、Atlas 650E 和 Atlas 950 三类产品形态；这能证明公开产品组合关系，不能替代 950DT 芯片的供应状态或规格表。[Ascend Product Overview](https://www.hiascend.com/document/detail/en/AscendFAQ/ProduTech/productform/hardwaredesc_0001.html)

### 系统证据与芯片证据的边界

- Atlas 950 SuperPoD 官方产品页写明最大支持 1024 个 Ascend 950DT，并给出 96 GB 片上内存/芯片的系统配置、1 EFLOPS/2 EFLOPS 系统算力和 100 kW 供电。这些是系统产品的配置上限，不是 950DT 芯片所有变体的规格，也不证明芯片已经批量出货。[Atlas 950 SuperPoD 产品页](https://www.hiascend.com/hardware/cluster)
- 华为 2026-07-17 的 WAIC 新闻称 Atlas 950 SuperPoD 首次公开展示 1024 卡真机，并给出 256 TB 全局统一编址空间和 3 μs RTT。这证明系统实机展示，不等于 950DT 芯片客户部署或普遍可采购。[昇腾 950 超节点 WAIC 实机信息](https://www.huawei.com/cn/news/2026/7/atlas-950-superpod)
- 本页不把 Atlas 950 SuperPoD、Atlas 850E 或 Atlas 650E 的机柜、CPU、DDR、系统互联、液冷、供电和系统算力回填到芯片级规格表。

## 生命周期状态

| 阶段 | Ascend 950DT 截至 2026-09-05 的公开状态 | 证据边界 |
|---|---|---|
| 宣布 | **已确认事实**：2025-09-18 在华为全联接大会 2025 路线图中宣布，定位为 Decode/训练芯片 | 这是正式宣布，不是流片或量产证明。[S1] |
| 流片/工程样片 | **公开资料未确认** | 未找到华为对 950DT 流片完成、工程样片或样片批次的直接披露。 |
| 送样/客户验证 | **公开资料未确认** | 公开发布材料没有给出样片送样对象、日期、数量或验证结果。 |
| 量产 | **芯片级公开资料未确认** | 产品总览和系统产品页的型号映射不能替代芯片量产证明；系统页面的“最大支持”也不是芯片批次信息。[S3][S4] |
| 出货 | **芯片级公开资料未确认** | 未找到芯片出货数量、批次或供应状态披露。 |
| 客户部署 | **950DT 芯片级公开资料未确认** | 2026-07-17 公开的是 Atlas 950 SuperPoD 1024 卡真机展示；文章未给出 950DT 客户部署、订单或交付清单。[S5] |
| 云/实例可用 | **公开资料未确认** | 截至核验日，未找到华为云公开页面将 Ascend 950DT 明确列为可购买云实例；CANN 文档中的产品支持不等于云实例供应。 |
| 路线图 | **已确认路线图目标**：2026 年第四季度推出 | 截至研究截止日尚未到路线图季度结束；不能把系统产品页或真机展示改写为芯片量产/出货状态。[S1] |

其中 `[S1]`、`[S3]`、`[S4]`、`[S5]` 的直接来源见文末来源清单。

## 芯片级规格

下表只采用《昇腾 950 NPU 架构白皮书》的芯片/封装口径。表中的斜杠表示白皮书列出的不同产品变体顺序；950DT 的 144/96 GB 是芯片表中的变体容量，不能被系统页面的 96 GB 单一配置替代。[昇腾 950 NPU 架构白皮书](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)

| 项目 | Ascend 950DT 芯片/封装公开规格 |
|---|---|
| Die 与封装 | 2 个 AI Die + 2 个 I/O Die + 4 个高速片上内存模块；通过 D2D Clink 和 Memory Interface 连接，构成 Chiplet UMA |
| AI 子系统 | 完整规格最多 36 个第三代 DaVinci AI 子系统；每个包含 1 个 Cube Core 和 2 个 Vector Core；表 3-1 的产品变体为 36/32/28 个 Cube Core、72/64/56 个 Vector Core |
| Cube+Vector 总算力 | MXFP4：2007/1784/1561 TFLOPS；HiF8/MXFP8/FP8：1034/919/804 TFLOPS；INT8：1034/919/804 TOPS；BF16/FP16：547/486/425 TFLOPS；TF32：273/243/212 TFLOPS |
| Cube 算力 | MXFP4：1946/1730/1513 TFLOPS；HiF8/MXFP8/FP8：973/865/756 TFLOPS；INT8：973/865/756 TOPS；BF16/FP16：486/432/378 TFLOPS；TF32：243/216/189 TFLOPS |
| Vector 算力 | FP16/BF16：60/54/47 TFLOPS；FP32：30/27/23 TFLOPS；INT8：60/54/47 TOPS；INT16：30/27/23 TOPS；INT32：15/13/11 TOPS；INT64：7/6/5 TOPS |
| 片上高速内存 | 容量 144/96 GB；带宽 4 TB/s；路线图另称 HiZQ 2.0 HBM，白皮书使用“高速片上内存”表述 |
| L2 Cache | 128 MB；512 B Cache Line，支持 4×128 B Sector、L2 Hint 和 CMO |
| AI CPU | Linx816，8C16T/6C12T 变体，支持 NEON |
| I/O 与互联协议 | URMA-CTP、URMA-TP、UB Memory、PCIe 5.0、UBoE |
| Unified Bus | 18 个 Port、每个最高 112 Gbps，2016 GB/s 双向；白皮书说明出框速率受光模块限制 |
| UBoE | 2 个 400 Gbps 端口，与 UB 复用 SerDes 端口 |
| PCIe | PCIe 5.0 ×16，128 GB/s 双向；与 UB 复用 4 个端口，支持 RC/EP 静态选择 |
| 制程、频率、芯片面积、芯片 TDP | **公开资料未确认** |

以上是官方公开理论规格，不是独立测试结果。Atlas 950 SuperPoD 页面中的 1024 卡、96 GB/卡、系统算力、机柜、供电和液冷都不进入本表。[Atlas 950 SuperPoD 产品页](https://www.hiascend.com/hardware/cluster)

## 架构与软件证据

### 芯片架构

- **已确认事实**：白皮书将 950PR/DT 的 AI 子系统归为第三代 DaVinciCore，并公开 Cube Core、Vector Core、SIMD/SIMT 混合编程、Cube-Vector 直接数据通路、RegFile 和 STARS2.0 等组成。[昇腾 950 NPU 架构白皮书](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)
- **已确认事实**：SIMT 被白皮书定位为辅助路径，覆盖 Gather/Scatter 等离散访问和复杂分支；SIMD 是主要向量执行路径。公开证据没有表明 950DT 内置独立搜索、索引或 Top-k 单元。[昇腾 950 NPU 架构白皮书](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)
- **已确认事实**：NDDMA 可在 Kernel 层完成最多 5 维数据重排/转置，硬化地址生成，并对带规律的数据搬运执行 128 B 读操作；公开资料没有证明它是按 KV page 表或任意索引列表工作的专用 Gather DMA。[昇腾 950 NPU 架构白皮书](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)
- **已确认事实**：UB Memory 提供同步 Load/Store/Atomic 语义，URMA 提供异步访存语义，CCU 支持 Broadcast、Reduce Scatter、All Gather、All Reduce、All2All 和 All2Allv 等集合通信算法；这些原语不等于 Retrieval-aware 路由或 Top-k 语义。[昇腾 950 NPU 架构白皮书](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)
- **分析推断**：950DT 的大容量/高带宽片上内存、SIMD/SIMT、NDDMA、L2 管理和 UB/URMA/CCU 组合，可能更适合 Decode、训练和跨芯片数据流；端到端 TPOT、TTFT、Tokens/J 仍需以具体模型、layout、并发和软件版本测试，不能由峰值规格直接推出。

### 软件证据

- **已确认事实**：昇腾社区 CANN 9.1.0-beta.2 的 ReduceSum 文档把 Ascend 950PR/Ascend 950DT 列为支持产品，并列出接口、数据类型和执行方式约束。[ReduceSum API 文档](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/910beta2/API/ascendcopapi/atlasascendc_api_07_0078.html)
- **已确认事实**：昇腾社区 CANN 文档中的 Ascend 950PR/DT 产品支持条目和针对 950 系列的算子/硬件调试文档，证明软件栈已为两款产品提供开发入口；这不证明芯片已经量产或云端可租用。[ReduceSum API 文档](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/910beta2/API/ascendcopapi/atlasascendc_api_07_0078.html)
- **证据边界**：CANN 9.0.0 发布说明明确写出的是 Ascend 950PR 支持，不应把其中 PR 专属的软件条目自动扩展为 DT 已获得同等软件/硬件状态；本页对 DT 只采用明确列出 950PR/950DT 的 API 文档作为软件证据。[CANN 9.0.0 Release Notes](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/900/releasenote/release-notes.md)

## 性能与采用证据

| 证据对象 | 公开内容 | 证据状态与限制 |
|---|---|---|
| Atlas 950 SuperPoD | 官方产品页写明最大支持 1024×Ascend 950DT、每颗配置可达 96 GB 片上内存、4.0 TB/s 带宽，并列出系统算力和互联规格 | **厂商主张/系统级产品规格**；不作为 950DT 芯片的唯一规格，也不证明芯片量产或客户部署。[Atlas 950 SuperPoD 产品页](https://www.hiascend.com/hardware/cluster) |
| Atlas 950 SuperPoD 真机展示 | 2026-07-17，华为称首次线下展示 1024 卡真机，并给出 1 EFLOPS FP8、2 EFLOPS FP4、256 TB 全局统一编址空间和 3 μs RTT | **已确认系统展示；厂商主张**。没有完整模型、批量、软件版本、功耗边界和客户交付条件，不能转成芯片 benchmark。[昇腾 950 超节点 WAIC 实机信息](https://www.huawei.com/cn/news/2026/7/atlas-950-superpod) |
| 端到端性能 | 未找到同时给出模型、精度、输入长度、batch、TTFT/TPOT、软件版本、功耗边界和对比基线的 950DT 独立可复现实测 | **公开资料未确认**；不把路线图算力或系统展示数字写成芯片实测。 |

## 未确认项与来源冲突

1. **系统规模口径不同**：2025 年路线图和 2026-03-02 MWC 发布材料把 Atlas 950 SuperPoD 描述为最大 8192 张 NPU 卡；当前 Atlas 950 SuperPoD 产品页写“最大支持 1024×Ascend 950DT”，2026-07-17 WAIC 又报告 1024 卡真机。官方材料没有在这些页面中解释是路线图目标、不同配置还是产品阶段差异。本页将其全部保留为系统层证据，不用任何一个数字回填 950DT 芯片规格。[华为路线图](https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech) [华为 MWC 2026 发布](https://www.huawei.com/cn/news/2026/3/mwc-superpod-ai) [Atlas 950 SuperPoD 产品页](https://www.hiascend.com/hardware/cluster) [昇腾 950 超节点 WAIC 实机信息](https://www.huawei.com/cn/news/2026/7/atlas-950-superpod)
2. **片上内存变体与系统配置**：白皮书表 3-1 列出 950DT 为 144/96 GB、带宽 4 TB/s；Atlas 950 SuperPoD 产品页展示的是 1024×96 GB 的系统配置。前者是芯片变体范围，后者是系统产品选型，不能互相覆盖。[昇腾 950 NPU 架构白皮书](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf) [Atlas 950 SuperPoD 产品页](https://www.hiascend.com/hardware/cluster)
3. **内存术语**：路线图称 DT 使用 HiZQ 2.0 HBM，白皮书称高速片上内存；公开资料没有给出 HiZQ 与行业 HBM 代际、颗粒构成或封装 BOM 的完整对照。本页保留各来源原称，不把它升级为未经披露的 HBM3e/4 等判断。[S1][S2]
4. **商业成熟度缺口**：系统产品已公开、真机已展示、CANN API 已列出 950DT 支持，但 950DT 芯片自身的流片、送样、量产批次、芯片出货、客户部署和云实例状态仍没有逐项直接披露。

## 直接来源清单

1. **S1｜《以开创的超节点互联技术，引领 AI 基础设施新范式》**；发布主体：华为；发布日期：2025-09-18；核验日期：2026-09-05；直接 URL：[https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech](https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech)。用于 950PR/DT 共用 Ascend 950 Die、DT 定位和 2026 年第四季度路线图。
2. **S2｜《昇腾 950 NPU 架构白皮书》**；发布主体：华为技术有限公司；发布日期：2026（首页版权年份，具体日未标注）；核验日期：2026-09-05；直接 URL：[PDF](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)。用于芯片级架构、表 3-1 规格、Cache、NDDMA、STARS、UB 和 CCU。
3. **S3｜《Ascend Product Overview》**；发布主体：昇腾社区/华为技术有限公司；发布日期：页面未标注；核验日期：2026-09-05；直接 URL：[https://www.hiascend.com/document/detail/en/AscendFAQ/ProduTech/productform/hardwaredesc_0001.html](https://www.hiascend.com/document/detail/en/AscendFAQ/ProduTech/productform/hardwaredesc_0001.html)。用于 950DT 与 Atlas 850E、Atlas 650E、Atlas 950 的产品组合映射。
4. **S4｜《Atlas 950 SuperPoD 液冷超节点》**；发布主体：昇腾社区/华为技术有限公司；发布日期：页面未标注；核验日期：2026-09-05；直接 URL：[https://www.hiascend.com/hardware/cluster](https://www.hiascend.com/hardware/cluster)。只用于系统产品配置和对象边界，不用于芯片量产、芯片 TDP 或芯片变体结论。
5. **S5｜《昇腾 950 超节点真机亮相 2026 世界人工智能大会》**；发布主体：华为；发布日期：2026-07-17；核验日期：2026-09-05；直接 URL：[https://www.huawei.com/cn/news/2026/7/atlas-950-superpod](https://www.huawei.com/cn/news/2026/7/atlas-950-superpod)。只用于 1024 卡系统真机展示和系统级性能口径。
6. **S6｜《华为发布新一代算力底座，为世界提供新选择》**；发布主体：华为；发布日期：2026-03-02；核验日期：2026-09-05；直接 URL：[https://www.huawei.com/cn/news/2026/3/mwc-superpod-ai](https://www.huawei.com/cn/news/2026/3/mwc-superpod-ai)。只用于 Atlas 950 SuperPoD 海外发布和 8192 卡路线/系统口径冲突核对。
7. **S7｜《ReduceSum》CANN Ascend C API 文档**；发布主体：昇腾社区；发布日期：页面未标注（CANN 9.1.0-beta.2 文档）；核验日期：2026-09-05；直接 URL：[https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/910beta2/API/ascendcopapi/atlasascendc_api_07_0078.html](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/910beta2/API/ascendcopapi/atlasascendc_api_07_0078.html)。用于 PR/DT 的 API 支持边界，不用于生命周期判断。
8. **S8｜《CANN 9.0.0 Release Notes》**；发布主体：昇腾社区；发布日期：页面未标注（版本 9.0.0）；核验日期：2026-09-05；直接 URL：[https://www.hiascend.com/document/detail/en/CANNCommunityEdition/900/releasenote/release-notes.md](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/900/releasenote/release-notes.md)。仅用于说明 950PR 专属软件条目，不能自动扩展为 DT 的软件/硬件状态。
