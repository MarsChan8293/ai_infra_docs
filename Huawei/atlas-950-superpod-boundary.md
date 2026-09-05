# Huawei / 华为昇腾 — Atlas 350 与 Atlas 950 SuperPoD（边界文件，非芯片）

- 拆分日期：2026-09-02
- 产品层级：加速卡/系统（非芯片）
- 综合报告：[02-huawei-ascend.md](./02-huawei-ascend.md)
- 文件性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容逐行摘录综合报告，保留原报告中的状态、数字、证据等级和未知项。

> 第 16 行：|---|---|---|
> 第 17 行：| Ascend 950PR | 2025-09-18 宣布；2026-03-20 宣布搭载它的 Atlas 350 加速卡正式上市，950 代际推理算力进入商用阶段，可视为本窗口内已可获得的 PR 产品 | 950PR 是芯片；Atlas 350 是带 PCIe、HBM、灵衢端口、散热和功耗约束的加速卡 |
> 第 18 行：| Ascend 950DT | 2025-09-18 宣布，官方路线图为 2026 年第四季度推出；2026-07-17 Atlas 950 SuperPoD 实机公开展示，白皮书和产品页已公开规格；截至截止日，芯片量产/普遍可采购状态为“公开资料未确认” | 950DT 是芯片；Atlas 950 SuperPoD 是多卡、多柜、互联柜、CPU、DDR、供电和液冷组成的系统 |
> 第 19 行：| Atlas 950 SuperPoD | 2025-09-18 宣布，2026-03-02 海外发布，2026-07-17 公开实机；这是系统可见性，不等于 950DT 已普遍供货 | 当前官方产品页与 WAIC 页面采用 1024 卡展示配置，不能直接替代芯片规格 |
> 第 20 行：
> 第 33 行：| 互联 | Unified Bus 2.0，18 个 x4 Port、112Gbps、2016GB/s 双向；PCIe 5.0 x16，128GB/s 双向；支持 URMA、UB Memory、UBoE、CCU | 同一 IO/互联规格，芯片级带宽不因 P/D 定位改变 |
> 第 34 行：| 功耗 | 芯片 TDP 未公开；Atlas 350 卡最大功耗 ≤600W | 芯片 TDP 未公开；Atlas 950 SuperPoD 产品页给出系统供电 100kW，不能回填成单芯片功耗 |
> 第 35 行：
> 第 36 行：规格依据为[昇腾 950 白皮书第 9 至 14 页](https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)（资料可获得，访问 2026-08-22）、[Atlas 350 产品页](https://www.hiascend.com/hardware/accelerator-card)（可用卡规格，访问 2026-08-22）和[Atlas 950 SuperPoD 产品页](https://www.hiascend.com/hardware/cluster)（系统规格，访问 2026-08-22）。白皮书还说明 PR 合封 8 个高速内存模块，DT 合封 4 个，属于封装与内存配置差异，不应把 112GB 卡规格和 144GB 芯片最高规格混写。
> 第 37 行：
> 第 78 行：
> 第 79 行：1. 2025 年路线图把 Atlas 950 SuperPoD 宣布为最高 8192 卡，并给出 1152TB、16.3PB/s 等路线图口径；2026 年产品页和 WAIC 实机页采用 1024 卡、256TB、1.72PB/s 或 3μs RTT 的展示/产品口径。官方页面没有解释两套数字是否对应不同阶段或配置。本文采用 2026 年产品页与 WAIC 的 1024 卡作为截止日可核验系统状态，把 8192 卡保留为已宣布路线图，不把路线图目标当作现货性能。[2025 路线图](https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech) 与[2026 产品页](https://www.hiascend.com/hardware/cluster)（访问 2026-08-22）
> 第 80 行：
> 第 98 行：2. [华为 2025 年昇腾路线图演讲](https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech)，950PR/DT 宣布、P/D 定位、HiBL/HiZQ 与时间状态（宣布 2025-09-18，访问 2026-08-22）。
> 第 99 行：3. [Atlas 350 加速卡产品页](https://www.hiascend.com/hardware/accelerator-card)，950PR 卡级内存、带宽、互联和功耗（可用产品资料，访问 2026-08-22）。
> 第 100 行：4. [昇腾伙伴峰会 2026](https://www.hiascend.com/activities/dynamic-news/20260320-3)，Atlas 350 正式上市及商用状态（发布 2026-03-20，访问 2026-08-22）。
> 第 101 行：5. [CANN 9.0.0 发布说明](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/900/releasenote/release-notes.md)，950PR 软件支持、SIMD+SIMT 与 CCU 通信加速（可用开发者资料，访问 2026-08-22）。
> 第 102 行：6. [Atlas 950 SuperPoD 产品页](https://www.hiascend.com/hardware/cluster)，当前 1024 卡系统配置、统一内存编址、带宽和供电（可用产品资料，访问 2026-08-22）。
> 第 103 行：7. [昇腾 950 超节点 WAIC 实机信息](https://www.huawei.com/cn/news/2026/7/atlas-950-superpod)，1024 卡、256TB、1 EFLOPS FP8/2 EFLOPS FP4 的公开展示口径（公开展示 2026-07-17，访问 2026-08-22）。

## 直接来源链接

1. <https://public-download.obs.cn-east-2.myhuaweicloud.com/ascend/%E6%98%87%E8%85%BE950%20NPU%E6%9E%B6%E6%9E%84%E7%99%BD%E7%9A%AE%E4%B9%A6.pdf)（资料可获得，访问>
2. <https://www.hiascend.com/hardware/accelerator-card)（可用卡规格，访问>
3. <https://www.hiascend.com/hardware/cluster)（系统规格，访问>
4. <https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech)>
5. <https://www.hiascend.com/hardware/cluster)（访问>
6. <https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech)，950PR/DT>
7. <https://www.hiascend.com/hardware/accelerator-card)，950PR>
8. <https://www.hiascend.com/activities/dynamic-news/20260320-3)，Atlas>
9. <https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/900/releasenote/release-notes.md)，950PR>
10. <https://www.hiascend.com/hardware/cluster)，当前>
11. <https://www.huawei.com/cn/news/2026/7/atlas-950-superpod)，1024>

## 证据边界

- 这是资料重排页，不是重新发布或重新核验的产品公告。
- “发布、流片、送样、量产、出货、客户部署、云端可用、路线图、停产”等状态只在综合报告明确写出时保留；缺失项仍为“公开资料未确认”。
- 若摘录同时出现芯片、板卡、服务器、机架或云服务，均按原报告层级保留，并以“产品层级”字段提醒，不做跨层级推导。

## 关联表格原文（完整表格）

以下表格块来自综合报告中与本拆分项命中的表格，完整保留表头、状态列和规格列。

> 来源综合报告第 15-19 行：
> 第 15 行：| 对象 | 发布、宣布、可用状态 | 芯片与系统边界 |
> 第 16 行：|---|---|---|
> 第 17 行：| Ascend 950PR | 2025-09-18 宣布；2026-03-20 宣布搭载它的 Atlas 350 加速卡正式上市，950 代际推理算力进入商用阶段，可视为本窗口内已可获得的 PR 产品 | 950PR 是芯片；Atlas 350 是带 PCIe、HBM、灵衢端口、散热和功耗约束的加速卡 |
> 第 18 行：| Ascend 950DT | 2025-09-18 宣布，官方路线图为 2026 年第四季度推出；2026-07-17 Atlas 950 SuperPoD 实机公开展示，白皮书和产品页已公开规格；截至截止日，芯片量产/普遍可采购状态为“公开资料未确认” | 950DT 是芯片；Atlas 950 SuperPoD 是多卡、多柜、互联柜、CPU、DDR、供电和液冷组成的系统 |
> 第 19 行：| Atlas 950 SuperPoD | 2025-09-18 宣布，2026-03-02 海外发布，2026-07-17 公开实机；这是系统可见性，不等于 950DT 已普遍供货 | 当前官方产品页与 WAIC 页面采用 1024 卡展示配置，不能直接替代芯片规格 |

> 来源综合报告第 25-34 行：
> 第 25 行：| 项目 | Ascend 950PR | Ascend 950DT |
> 第 26 行：|---|---|---|
> 第 27 行：| 制程 | 具体 nm/工艺节点未公开；白皮书只称自主可控制造工艺 | 同左，公开资料未确认具体节点 |
> 第 28 行：| 计算单元 | 完整架构最多 36 个 AI 子系统，每个含 1 个 Cube Core 和 2 个 Vector Core；量产/产品变体为 32/28 Cube、64/56 Vector | 完整架构同为 36 个 AI 子系统；变体为 36/32/28 Cube、72/64/56 Vector |
> 第 29 行：| 峰值格式 | MXFP4 1784/1561 TFLOPS；HiF8/MXFP8/FP8 919/804 TFLOPS；BF16/FP16 486/425 TFLOPS | MXFP4 2007/1784/1561 TFLOPS；HiF8/MXFP8/FP8 1034/919/804 TFLOPS；BF16/FP16 547/486/425 TFLOPS |
> 第 30 行：| 数值格式 | TF32、FP16、BF16、FP8、MXFP8、HiF8、INT8、MXFP4 等 | 同系列格式；官方路线图明确用于 Decode 与训练 |
> 第 31 行：| 主内存 | 华为新闻稿称 HiBL 1.0 HBM；白皮书称高速片上内存，最高 128GB、1.6TB/s，产品变体 112GB、1.4TB/s | HiZQ 2.0，最高 144GB、4TB/s；白皮书列出 144/96GB 变体 |
> 第 32 行：| Cache 与粒度 | 128MB 统一 L2；512B cache line，四个 128B sector；官方新闻稿把访存颗粒度从 512B 说到 128B | 同样的 128MB L2 与 128B sector 机制 |
> 第 33 行：| 互联 | Unified Bus 2.0，18 个 x4 Port、112Gbps、2016GB/s 双向；PCIe 5.0 x16，128GB/s 双向；支持 URMA、UB Memory、UBoE、CCU | 同一 IO/互联规格，芯片级带宽不因 P/D 定位改变 |
> 第 34 行：| 功耗 | 芯片 TDP 未公开；Atlas 350 卡最大功耗 ≤600W | 芯片 TDP 未公开；Atlas 950 SuperPoD 产品页给出系统供电 100kW，不能回填成单芯片功耗 |
