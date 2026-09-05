# OpenAI — Jalapeño 后续多代平台（路线图，非已命名芯片）

- 拆分日期：2026-09-02
- 产品层级：路线图/平台
- 综合报告：[OpenAI_芯片与AI基础设施洞察_2026-09-02.md](./OpenAI_芯片与AI基础设施洞察_2026-09-02.md)
- 文件性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容逐行摘录综合报告，保留原报告中的状态、数字、证据等级和未知项。

> 第 13 行：| **Jalapeño** | OpenAI 主导设计的定制 LLM 推理加速器；Broadcom、Celestica 参与工业化 | 2026-06-24 首次正式披露；九个月完成至制造 tape-out；工程样片在实验室按生产目标频率/功耗运行；2026-08-25 有初步实测结果 | 面向现代 LLM 推理；强调降低数据搬运、平衡计算/内存/网络、接近理论峰值利用率；支持 OpenAI 及外部 LLM 工作负载 | 芯片制程、晶体管数、封装、片上 SRAM/缓存容量、HBM 容量/带宽、算力峰值、互联拓扑、TDP、具体 kernel 指令集均未公开 |
> 第 14 行：| Jalapeño 后续多代平台 | OpenAI + Broadcom 的路线图 | 计划从 2026 年底开始初始部署，随后扩展多个世代；没有公开第二代型号 | 多代计算平台，配套芯片、板卡、机架、网络和生产系统 | 第二代及以后型号、制程、性能、量产节奏和实际部署量未确认 |
> 第 15 行：| 10GW OpenAI-designed accelerators | OpenAI 设计、Broadcom 合作开发和部署 | 2025-10-13 宣布；目标 2026 下半年开始部署、2029 年底完成 | 加速器与 Ethernet scale-up/scale-out 网络系统；规模用功率而非芯片数量表述 | 10GW 是否全部由 Jalapeño 或其后代构成、每瓦对应多少芯片、实际出货/上架数量均未确认 |
> 第 16 行：| Broadcom 网络与互联 | 合作方硅与系统能力，不等于 OpenAI 芯片 | Broadcom 明确提到 Ethernet、Tomahawk、PCIe、光互联及机架系统能力；OpenAI 还参与 OCI 光互联规范和 MRC 网络协议 | scale-up/scale-out 网络、以太网交换、NIC、PHY、光连接；MRC 关注大规模训练网络可靠性 | OpenAI 具体部署中每一类 Broadcom 器件的型号、数量、端到端带宽和占比未确认 |

## 直接来源链接

1. <https://openai.com/index/openai-broadcom-jalapeno-inference-chip/>
2. <https://openai.com/index/jalapeno-first-results/>
3. <https://openai.com/index/the-full-stack-behind-abundant-intelligence/>
4. <https://openai.com/index/openai-and-broadcom-announce-strategic-collaboration/>
5. <https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age/>
6. <https://openai.com/index/stargate-advances-with-partnership-with-oracle/>
7. <https://openai.com/index/openai-nvidia-systems-partnership/>
8. <https://openai.com/index/aws-and-openai-partnership/>

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
