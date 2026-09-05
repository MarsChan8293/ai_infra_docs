# Cerebras Systems — WSE-3

- 拆分日期：2026-09-02
- 产品层级：晶圆级处理器
- 综合报告：[04-cerebras-wse.md](./04-cerebras-wse.md)
- 文件性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容逐行摘录综合报告，保留原报告中的状态、数字、证据等级和未知项。

> 第 1 行：# Cerebras WSE-3 Turbo / CS-4：2025-06 之后最新晶圆级 AI 芯片
> 第 2 行：
> 第 6 行：
> 第 7 行：截至 2026-08-22，Cerebras 在窗口内能确认的最新处理器是 **WSE-3 Turbo（WSE-3T）**，于 2026-08-18 随 **CS-4** 一起宣布。它主要瞄准推理解码阶段的内存带宽、跨晶圆通信和机架级部署，最值得研究的创新是把 44GB 片上 SRAM、53.5 PB/s 片上 fabric 与 3 片晶圆组成的低延迟系统放在同一个设计里。它没有公开证明自己实现了附件所设想的专用 Search、Top-k 或 Gather DMA 平面，因此更像“把搬运的路修宽、修近”，还不是完整的 Retrieval GPU。[官方新闻稿](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions)（宣布日期：2026-08-18；访问日期：2026-08-22）
> 第 8 行：
> 第 12 行：|---|---|---|
> 第 13 行：|WSE-3|2024-03-13 发布，早于本次窗口，只作上一代基线|一片 WSE-3 进入一台 CS-3；CS-3 还包含供电、液冷、网络和管理。旧基线不能当作窗口内新芯片。[官方发布](https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine)（访问日期：2026-08-22）|
> 第 14 行：|WSE-3 Turbo|2026-08-18 宣布，窗口内最新 WSE 处理器|芯片本体。官方称首个搭载它的 CS-4 由三片 WSE-3T 组成；WSE-3T 已宣布，量产规模和独立购买状态公开资料未确认。[官方新闻稿](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions)（访问日期：2026-08-22）|
> 第 15 行：|CS-4|2026-08-18 宣布，首批出货“本季度开始”|一台机架级系统，含三片 WSE-3T、计算 backpack、供电、直液冷、Wafer I/O 和 Nexus 机架。到截止日仍应标为“宣布/计划出货”，不能写成已普遍可用。[CS-4 产品页](https://www.cerebras.ai/cs4)（访问日期：2026-08-22）|
> 第 21 行：
> 第 22 行：|项目|WSE-3 Turbo，单片晶圆|CS-4，单系统|资料边界|
> 第 23 行：|---|---|---|---|
> 第 31 行：
> 第 32 行：公开口径显示，WSE-3T 与 WSE-3 仍共享 5nm、46,225 mm²、4 万亿晶体管、900,000 核心和 44GB SRAM 这组基础数字；Cerebras 把 WSE-3T 的代际提升写在 250 PFLOPS、43.2 PB/s、53.5 PB/s fabric 和更高供电上。WSE-3T 是否改动了 PE 内部微架构、缓存组织或 NoC 拓扑，公开资料未确认。[官方新闻稿](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions)（访问日期：2026-08-22）
> 第 33 行：
> 第 49 行：
> 第 50 行：Cerebras 的公开说明是“小核心 + 冗余路由 + 备用核心 + fail-in-place”。WSE-3 的制造说明给出约 970,000 个物理核心、900,000 个当前产品启用核心，坏点被关闭，连接通过冗余路径绕行；这解决的是晶圆级良率和可用面积。它对附件的启发是让大规模片上网络具备绕障能力，但它不等于动态 KV 路由器，也不代表运行时拥塞、Top-k 候选合并已经解决。[官方制造说明](https://www.cerebras.ai/blog/100x-defect-tolerance-how-cerebras-solved-the-yield-problem)（上一代技术基线，发布日期：2025-01-13；访问日期：2026-08-22）
> 第 51 行：

## 直接来源链接

1. <https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions>
2. <https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine>
3. <https://www.cerebras.ai/cs4>
4. <https://www.cerebras.ai/blog/100x-defect-tolerance-how-cerebras-solved-the-yield-problem>

## 证据边界

- 这是资料重排页，不是重新发布或重新核验的产品公告。
- “发布、流片、送样、量产、出货、客户部署、云端可用、路线图、停产”等状态只在综合报告明确写出时保留；缺失项仍为“公开资料未确认”。
- 若摘录同时出现芯片、板卡、服务器、机架或云服务，均按原报告层级保留，并以“产品层级”字段提醒，不做跨层级推导。

## 关联表格原文（完整表格）

以下表格块来自综合报告中与本拆分项命中的表格，完整保留表头、状态列和规格列。

> 来源综合报告第 11-16 行：
> 第 11 行：|对象|时间与状态|芯片、系统、服务边界|
> 第 12 行：|---|---|---|
> 第 13 行：|WSE-3|2024-03-13 发布，早于本次窗口，只作上一代基线|一片 WSE-3 进入一台 CS-3；CS-3 还包含供电、液冷、网络和管理。旧基线不能当作窗口内新芯片。[官方发布](https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine)（访问日期：2026-08-22）|
> 第 14 行：|WSE-3 Turbo|2026-08-18 宣布，窗口内最新 WSE 处理器|芯片本体。官方称首个搭载它的 CS-4 由三片 WSE-3T 组成；WSE-3T 已宣布，量产规模和独立购买状态公开资料未确认。[官方新闻稿](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions)（访问日期：2026-08-22）|
> 第 15 行：|CS-4|2026-08-18 宣布，首批出货“本季度开始”|一台机架级系统，含三片 WSE-3T、计算 backpack、供电、直液冷、Wafer I/O 和 Nexus 机架。到截止日仍应标为“宣布/计划出货”，不能写成已普遍可用。[CS-4 产品页](https://www.cerebras.ai/cs4)（访问日期：2026-08-22）|
> 第 16 行：|CS-3 相关更新|2026-03-13 宣布 AWS 部署 CS-3，并通过 Bedrock 提供服务；这是系统/云服务更新，不是新 WSE|AWS 与 Cerebras 还宣布 Trainium 做 prefill、CS-3 做 decode 的异构方案。具体区域、容量和完全生产化交付，所引页面没有给全。[官方 AWS 更新](https://www.cerebras.ai/blog/cerebras-is-coming-to-aws)（访问日期：2026-08-22）|

> 来源综合报告第 22-30 行：
> 第 22 行：|项目|WSE-3 Turbo，单片晶圆|CS-4，单系统|资料边界|
> 第 23 行：|---|---|---|---|
> 第 24 行：|制程、面积、晶体管|TSMC 5nm；46,225 mm²；4 万亿晶体管|3 × WSE-3T|官方 CS-4 数据表明确给出。[数据表 PDF](https://cdn.sanity.io/files/e4qjo92p/production/bb028ae2422089dfbcc9fd2455c021f3625c7a75.pdf)（访问日期：2026-08-22）|
> 第 25 行：|计算单元|900,000 个 AI 优化核心|3 片 WSE-3T|官方把 WSE-3T AI compute 写为 250 PFLOPS，按稀疏 FP16 统计；CS-4 为 750 PFLOPS。[新闻稿](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions)（访问日期：2026-08-22）|
> 第 26 行：|数值格式|公开资料确认稀疏 FP16 计算口径；Cerebras 开发文档列出 FP32、FP16、bfloat16，另一版本文档列出 cbfloat16|WSE-3T 专属 FP8、INT8 或量化吞吐未确认|不能把通用 CS 文档的格式列表当成 WSE-3T 的完整硬件格式表。[开发文档 1.8](https://training-api.cerebras.ai/en/1.8.0/wsc/general/cs-1-data-formats.html) 与 [开发文档 2.1](https://training-api.cerebras.ai/en/2.1.0/wsc/how_to_guides/cs-1-data-formats.html)（访问日期：2026-08-22）|
> 第 27 行：|片上内存|44GB SRAM|按 44GB × 3 计算为 132GB，系统总可用容量未单独确认|这是片上 SRAM，不等于任意规模 KV Cache；外部 MemoryX/存储容量的 CS-4 数字公开资料未确认。[数据表 PDF](https://cdn.sanity.io/files/e4qjo92p/production/bb028ae2422089dfbcc9fd2455c021f3625c7a75.pdf)（访问日期：2026-08-22）|
> 第 28 行：|内存带宽|43.2 PB/s|129.6 PB/s|官方公布值，单位沿用原资料。[CS-4 新闻稿](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions)（访问日期：2026-08-22）|
> 第 29 行：|片上互联与 I/O|片上 fabric 53.5 PB/s；片外 I/O 2.4 Tb/s/片|片上 fabric 160.5 PB/s；I/O 7.2 Tb/s|支持可编程 Wafer I/O、RoCE v2 RDMA 和无交换机 Direct Wafer Links；官方把晶圆间延迟降到最低 2 μs。[数据表 PDF](https://cdn.sanity.io/files/e4qjo92p/production/bb028ae2422089dfbcc9fd2455c021f3625c7a75.pdf)（访问日期：2026-08-22）|
> 第 30 行：|功耗|绝对瓦数公开资料未确认|未给出机架总瓦数；官方称供电转换距离约 0.5mm，并可向 WSE-3T 提供上一代约两倍功率，CS-4 宣称最高 10× CS-3 吞吐/W|“两倍供电”和“10× 吞吐/W”都不能替代绝对功耗或统一负载下的 Tokens/J。[CS-4 产品页](https://www.cerebras.ai/cs4)（访问日期：2026-08-22）|

## 补充直接来源链接

1. <https://www.cerebras.ai/blog/cerebras-is-coming-to-aws)（访问日期：2026-08-22）|>
2. <https://cdn.sanity.io/files/e4qjo92p/production/bb028ae2422089dfbcc9fd2455c021f3625c7a75.pdf)（访问日期：2026-08-22）|>
3. <https://training-api.cerebras.ai/en/1.8.0/wsc/general/cs-1-data-formats.html)>
4. <https://training-api.cerebras.ai/en/2.1.0/wsc/how_to_guides/cs-1-data-formats.html)（访问日期：2026-08-22）|>
