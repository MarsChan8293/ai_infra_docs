# Huawei / 华为昇腾 — Ascend 950PR

- 研究截止日：2026-09-05
- 核验日期：2026-09-05
- 厂商：华为技术有限公司
- 产品层级：AI 加速芯片；公开资料同时描述了包含多 Die、片上高速内存和 I/O Die 的完整封装
- 综合报告导航：[02-huawei-ascend.md](./02-huawei-ascend.md)
- 页面范围：只判断 Ascend 950PR 芯片/封装本身。Atlas 350 是承载该芯片的 PCIe 加速卡，卡上的接口、散热、尺寸、功耗和实际装配容量不回填为芯片规格；Atlas 950 SuperPoD 的系统数字也不作为本页芯片证据。

## 一句话结论

已确认华为在 2025-09-18 将 Ascend 950PR 定位为面向 Prefill 和推荐的 Ascend 950 系列芯片，并在 2026-03-20 宣布搭载它的 Atlas 350 加速卡正式上市；白皮书已公开芯片级架构和多组变体规格，但截至 2026-09-05，950PR 的流片/样片、送样、芯片量产、芯片出货、芯片客户部署和云实例可用性仍未被公开资料分别确认。[华为路线图](https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech) [昇腾伙伴峰会 2026](https://www.hiascend.com/activities/dynamic-news/20260320-3)

## 产品定位与对象边界

### 已确认事实

1. 华为 2025 年路线图称 Ascend 950PR 与 Ascend 950DT 共用 Ascend 950 Die；PR 面向推理 Prefill 阶段和推荐业务，路线图目标为 2026 年第一季度推出。该页面是正式发布/路线图证据，不等同于量产或出货证明。[华为路线图](https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech)
2. 《昇腾 950 NPU 架构白皮书》将 950PR 描述为多 Die 合封芯片，包含 2 个 AI Die、2 个 I/O Die 和 8 个高速片上内存模块，并与 950DT 采用共架构、不同内存配置的产品设计。[昇腾 950 NPU 架构白皮书](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)
3. 昇腾社区当前产品页明确写明“Atlas 350 加速卡采用 Ascend 950PR”。因此，Atlas 350 可以作为 950PR 的公开产品载体；它仍是板卡级对象，不是裸芯片或芯片封装的等价物。[Atlas 350 加速卡产品页](https://www.hiascend.com/hardware/accelerator-card)

### 不能跨层级推导的内容

- Atlas 350 的 HBM 容量、PCIe 接口、卡间灵衢连接器、被动散热、尺寸、重量和 ≤600 W 最大功耗属于加速卡规格；它们不能证明 950PR 芯片的 TDP、封装尺寸或芯片出货量。[Atlas 350 加速卡产品页](https://www.hiascend.com/hardware/accelerator-card)
- Atlas 950 SuperPoD 是包含多张卡、互联柜、CPU、系统内存、供电和液冷的系统对象。本页不采用其 1024 卡、256 TB 或 100 kW 等系统规格反推 950PR。
- “共用 Ascend 950 Die”证明的是华为对产品家族/架构的公开描述；公开资料没有给出足以判断两款商业封装掩模版、冗余策略或完整 BOM 的信息。

## 生命周期状态

| 阶段 | Ascend 950PR 截至 2026-09-05 的公开状态 | 证据边界 |
|---|---|---|
| 宣布 | **已确认事实**：2025-09-18 在华为全联接大会 2025 路线图中宣布，定位为 Prefill/推荐芯片 | 这是正式宣布，不是流片或量产证明。[S1] |
| 流片/工程样片 | **公开资料未确认** | 未找到华为对 950PR 流片完成、工程样片或样片批次的直接披露。 |
| 送样/客户验证 | **公开资料未确认** | 公开发布材料没有给出样片送样对象、日期、数量或验证结果。 |
| 量产 | **芯片级公开资料未确认** | 2026-03-20 只明确宣布搭载 950PR 的 Atlas 350 加速卡正式上市；卡上市不能单独证明芯片量产状态。[S4] |
| 出货 | **芯片级公开资料未确认** | 未找到芯片出货数量、批次或供应状态披露；卡级产品页可访问也不等于芯片出货统计。 |
| 客户部署 | **950PR 芯片级公开资料未确认** | 峰会称 7 家伙伴首发基于 Atlas 350 的整机、180 多家客户落地 2026 场景方案，但对象是伙伴整机/行业方案，未将客户部署归因到 950PR 芯片。[S4] |
| 云/实例可用 | **公开资料未确认** | 截至核验日，未找到华为云公开页面将 Ascend 950PR 明确列为可购买云实例；CANN 文档中的“支持”不等于云实例供应。 |
| 路线图 | **已确认路线图目标**：2026 年第一季度推出；2026-03-20 卡级产品正式上市 | “推出”与芯片的流片、量产、出货、云可用性仍需分别验证。[S1][S3][S4] |

其中 `[S1]`、`[S3]`、`[S4]` 的直接来源见文末来源清单。

## 芯片级规格

下表只采用《昇腾 950 NPU 架构白皮书》的芯片/封装口径。表中的斜杠表示白皮书列出的不同产品变体顺序，不把某个变体的具体封装、频率或冗余映射补猜为公开事实。[昇腾 950 NPU 架构白皮书](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)

| 项目 | Ascend 950PR 芯片/封装公开规格 |
|---|---|
| Die 与封装 | 2 个 AI Die + 2 个 I/O Die + 8 个高速片上内存模块；通过 D2D Clink 和 Memory Interface 连接，构成 Chiplet UMA |
| AI 子系统 | 完整规格最多 36 个第三代 DaVinci AI 子系统；每个包含 1 个 Cube Core 和 2 个 Vector Core；表 3-1 的产品变体为 32/28 个 Cube Core、64/56 个 Vector Core |
| Cube+Vector 总算力 | MXFP4：1784/1561 TFLOPS；HiF8/MXFP8/FP8：919/804 TFLOPS；INT8：919/804 TOPS；BF16/FP16：486/425 TFLOPS；TF32：243/212 TFLOPS |
| Cube 算力 | MXFP4：1730/1513 TFLOPS；HiF8/MXFP8/FP8：865/756 TFLOPS；INT8：865/756 TOPS；BF16/FP16：432/378 TFLOPS；TF32：216/189 TFLOPS |
| Vector 算力 | FP16/BF16：54/47 TFLOPS；FP32：27/23 TFLOPS；INT8：54/47 TOPS；INT16：27/23 TOPS；INT32：13/11 TOPS；INT64：6/5 TOPS |
| 片上高速内存 | 容量 128/112 GB；带宽 1.6/1.4 TB/s；白皮书称高速片上内存，路线图另称 HiBL 1.0 HBM |
| L2 Cache | 完整规格 128 MB；表 3-1 列出 PR 变体 128/112 MB；512 B Cache Line，支持 4×128 B Sector、L2 Hint 和 CMO |
| AI CPU | Linx816，8C16T/6C12T/4C8T 变体，支持 NEON |
| I/O 与互联协议 | URMA-CTP、URMA-TP、UB Memory、PCIe 5.0、UBoE |
| Unified Bus | 18 个 Port、每个最高 112 Gbps，2016 GB/s 双向；白皮书说明出框速率受光模块限制 |
| UBoE | 2 个 400 Gbps 端口，与 UB 复用 SerDes 端口 |
| PCIe | PCIe 5.0 ×16，128 GB/s 双向；与 UB 复用 4 个端口，支持 RC/EP 静态选择 |
| 制程、频率、芯片面积、芯片 TDP | **公开资料未确认** |

这些是官方公开理论规格，不是独立测试结果。尤其不要把 Atlas 350 的 112 GB、1.4 TB/s 或 ≤600 W 作为 PR 芯片的通用容量、带宽或 TDP。[Atlas 350 加速卡产品页](https://www.hiascend.com/hardware/accelerator-card)

## 架构与软件证据

### 芯片架构

- **已确认事实**：白皮书将 950PR/DT 的 AI 子系统归为第三代 DaVinciCore，并公开 Cube Core、Vector Core、SIMD/SIMT 混合编程、Cube-Vector 直接数据通路、RegFile 和 STARS2.0 等组成。[昇腾 950 NPU 架构白皮书](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)
- **已确认事实**：白皮书把 SIMT 作为补充路径，举例覆盖 Gather/Scatter 等离散访问和复杂分支；SIMD 是主要向量执行路径。这证明编程模型覆盖这些算子形态，不证明芯片内置独立搜索、索引或 Top-k 单元。[昇腾 950 NPU 架构白皮书](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)
- **已确认事实**：NDDMA 可在 Kernel 层完成最多 5 维数据重排/转置，硬化地址生成，并将带规律的数据搬运为 128 B 读操作；公开资料没有证明它是按 KV page 表或任意索引列表工作的专用 Gather DMA。[昇腾 950 NPU 架构白皮书](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)
- **分析推断**：SIMD/SIMT、NDDMA、Sector Cache、L2 Hint/CMO 和 UB/URMA 组合起来，可能降低部分不规则访存和跨芯片编排开销；能否改善具体 KV Cache、TTFT 或 TPOT，仍取决于 layout、算子融合、并发和软件调度，不能由芯片规格直接推出。

### 软件证据

- **已确认事实**：CANN 9.0.0 发布说明明确列出 Ascend 950PR（Atlas 350）支持，并列出 FP8/MXFP8/MXFP4、AscendC 的 SIMD+SIMT 混合编程、CCU 通信接口、950PR 指令集以及 SDMA/URMA 异步通信等软件能力。[CANN 9.0.0 Release Notes](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/900/releasenote/release-notes.md)
- **已确认事实**：昇腾社区 CANN 9.1.0-beta.2 的 ReduceSum 文档把 Ascend 950PR/Ascend 950DT 列为支持产品，并给出其接口和数据类型约束。[ReduceSum API 文档](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/910beta2/API/ascendcopapi/atlasascendc_api_07_0078.html)
- **证据边界**：软件包、编译器、仿真器或 API 文档的硬件型号支持，证明的是软件栈适配/开发入口，不单独证明芯片已经批量交付或云端可租用。

## 性能与采用证据

| 证据对象 | 公开内容 | 证据状态与限制 |
|---|---|---|
| Atlas 350 加速卡 | 官方产品页列出 1561 TFLOPS mxFP4、804 TFLOPS mxFP8/HiF8/mxFP6/INT8、425 TFLOPS FP16/BF16；112 GB HBM、1.4 TB/s、PCIe 5.0、卡间灵衢和 ≤600 W | **厂商主张/卡级理论规格**；页面注明理论值，实测可能存在小于 1% 误差。不能改写成 PR 芯片 TDP 或端到端推理性能。[Atlas 350 加速卡产品页](https://www.hiascend.com/hardware/accelerator-card) |
| Atlas 350 上市 | 2026-03-20，昇腾社区称搭载 Ascend 950PR 处理器的 Atlas 350 加速卡正式上市；同页称 7 家伙伴首发基于 Atlas 350 的整机 | **已确认卡级发布；厂商生态主张**。它支持“950PR 代际进入商用阶段”的判断，但不提供芯片流片、出货数量或客户部署清单。[昇腾伙伴峰会 2026](https://www.hiascend.com/activities/dynamic-news/20260320-3) |
| 端到端性能 | 未找到同时给出模型、精度、稀疏性、输入长度、batch、TTFT/TPOT、软件版本、功耗边界和对比基线的 950PR 独立可复现实测 | **公开资料未确认**；不把“领先倍数”“推荐加速”等缺少完整条件的宣传表述写成 benchmark。 |

## 未确认项与来源冲突

1. **Cache Line 与访问粒度**：2025 路线图把访问颗粒度从 512 B 说到 128 B，2026 伙伴峰会页面又写成“Cache-line 的访存粒度降低到 128 字节”；白皮书的芯片级细节明确写着 Cache Line 仍为 512 B，同时新增 4×128 B Sector、提高 128/256 B 访问效率。本页采用白皮书的精确口径，将“128 B”写为 Sector/访问粒度，不写成 Cache Line 已变为 128 B。[华为路线图](https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech) [昇腾伙伴峰会 2026](https://www.hiascend.com/activities/dynamic-news/20260320-3) [昇腾 950 NPU 架构白皮书](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)
2. **内存术语与变体**：路线图称 PR 使用 HiBL 1.0 HBM，白皮书称高速片上内存并列出 128/112 GB、1.6/1.4 TB/s，Atlas 350 卡页明确是 112 GB HBM、1.4 TB/s。三者可能对应家族、芯片变体与板卡形态，但公开资料没有给出完整映射；本页保留原文对象和单位，不把 112 GB 卡规格提升为所有 PR 芯片规格。[S1][S2][S3]
3. **卡页格式标签**：Atlas 350 卡页把 804 TFLOPS 一栏写作“mxFP8/HiF8/mxFP6/INT8”，而白皮书表 3-1 的 PR 芯片对应列写作“HiF8/MXFP8/FP8”。由于对象和格式标签不完全一致，本页只在卡级表保留卡页原文，在芯片表采用白皮书表 3-1，不做格式别名归并。[S2][S3]
4. **商业成熟度缺口**：卡级正式上市、伙伴整机亮相和软件支持已经有公开证据；950PR 芯片自身的流片、送样、量产批次、芯片出货、客户部署和云实例状态仍没有逐项直接披露。

## 直接来源清单

1. **S1｜《以开创的超节点互联技术，引领 AI 基础设施新范式》**；发布主体：华为；发布日期：2025-09-18；核验日期：2026-09-05；直接 URL：[https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech](https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech)。用于 950PR/DT 共用 Ascend 950 Die、PR 定位和 2026 年第一季度路线图。
2. **S2｜《昇腾 950 NPU 架构白皮书》**；发布主体：华为技术有限公司；发布日期：2026（首页版权年份，具体日未标注）；核验日期：2026-09-05；直接 URL：[PDF](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)。用于芯片级架构、表 3-1 规格、Cache、NDDMA、STARS、UB 和 CCU。
3. **S3｜《Atlas 350 加速卡》**；发布主体：昇腾社区/华为技术有限公司；发布日期：页面未标注；核验日期：2026-09-05；直接 URL：[https://www.hiascend.com/hardware/accelerator-card](https://www.hiascend.com/hardware/accelerator-card)。用于“Atlas 350 采用 950PR”和卡级理论规格，不用于芯片 TDP 或芯片出货判断。
4. **S4｜《技术创新赋能千行万业 昇腾人工智能伙伴峰会 2026 圆满举办》**；发布主体：昇腾社区；发布日期：2026-03-20；核验日期：2026-09-05；直接 URL：[https://www.hiascend.com/activities/dynamic-news/20260320-3](https://www.hiascend.com/activities/dynamic-news/20260320-3)。用于 Atlas 350 正式上市、伙伴整机和行业方案采用边界。
5. **S5｜《CANN 9.0.0 Release Notes》**；发布主体：昇腾社区；发布日期：页面未标注（版本 9.0.0）；核验日期：2026-09-05；直接 URL：[https://www.hiascend.com/document/detail/en/CANNCommunityEdition/900/releasenote/release-notes.md](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/900/releasenote/release-notes.md)。用于 950PR 的 CANN、AscendC、指令集和通信软件支持。
6. **S6｜《ReduceSum》CANN Ascend C API 文档**；发布主体：昇腾社区；发布日期：页面未标注（CANN 9.1.0-beta.2 文档）；核验日期：2026-09-05；直接 URL：[https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/910beta2/API/ascendcopapi/atlasascendc_api_07_0078.html](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/910beta2/API/ascendcopapi/atlasascendc_api_07_0078.html)。用于 PR/DT 的 API 支持边界，不用于生命周期判断。
