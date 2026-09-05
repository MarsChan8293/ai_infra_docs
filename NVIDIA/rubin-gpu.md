# NVIDIA / 英伟达 — Rubin GPU

- 拆分日期：2026-09-02
- 产品层级：GPU 芯片
- 综合报告：[01-nvidia.md](./01-nvidia.md)
- 文件性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容逐行摘录综合报告，保留原报告中的状态、数字、证据等级和未知项。

> 第 1 行：# 厂商与芯片：2025-06 之后最新款——NVIDIA Rubin GPU
> 第 2 行：
> 第 3 行：> 研究对象：NVIDIA Rubin GPU；Vera Rubin 是系统边界，Rubin CPX 是同代长上下文变体。研究窗口：2025-07-01 至 2026-08-22。原始资料访问日期：2026-08-22；本次结构核验：2026-09-05。Hot Chips 2026 议程只作为会议证据入口，未据此新增 Rubin 规格。
> 第 4 行：
> 第 6 行：
> 第 7 行：Rubin 最值得研究的地方，不是把 Tensor Core 再堆大，而是把 **HBM4、TMA 数据搬运、依赖触发和 NVLink 6** 组合成一条更紧的推理执行路径。它确实改善了密集计算、规则张量搬运、跨卡通信和 kernel 间等待；但公开资料没有证明它已经提供附件设想的独立 **Search/Indexer、精确 Local/Global Top-k、page-aware Indexed Gather DMA**。因此，它是“更强的推理 GPU + 系统协同”，还不是完整的 Retrieval GPU。[架构深读](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)；[NVLink 6](https://www.nvidia.com/en-gb/data-center/nvlink/)（访问：2026-08-22）。
> 第 8 行：
> 第 12 行：|---|---|---|
> 第 13 行：| **Rubin GPU** | 2026-01-05 宣布 Rubin 平台；2026-03-16 NVIDIA 称平台七颗芯片进入 full production；2026-05-31 称 Vera Rubin 正在爬产，2026-07-21 官方技术文公开架构细节。产品处于量产爬坡、合作伙伴部署/出货阶段；单卡直接购买状态公开资料未确认。来源：[宣布](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer)；[量产](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform)；[爬产](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Vera-Rubin-Ramps-Into-Full-Production-to-Power-Agentic-AI-Factories-Worldwide/default.aspx)；[合作伙伴部署](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)（均访问：2026-08-22）。 | 一颗 Rubin GPU：288 GB HBM4。Vera Rubin Superchip 是 2 颗 GPU + 1 颗 Vera CPU；NVL72 是 72 颗 GPU + 36 颗 CPU 的机架系统，不能把后两者规格写成单芯片规格。 |
> 第 14 行：| **Rubin CPX** | 2025-09-09 宣布，官方状态为“预计 2026 年底可用”，截至截止日仍不是已可获得产品。来源：[NVIDIA 新闻稿](https://nvidianews.nvidia.com/news/nvidia-unveils-rubin-cpx-a-new-class-of-gpu-designed-for-massive-context-inference)（访问：2026-08-22）。 | 这是面向百万 token 上下文的独立 NVIDIA GPU，采用 128 GB GDDR7、最高 30 PFLOPS NVFP4；不能把 CPX 的 GDDR7 规格与 Rubin GPU 的 HBM4 混写。 |
> 第 15 行：
> 第 16 行：**跨边界注记。** Groq 3 LPX 在 2026-03-16 被 NVIDIA 纳入 Vera Rubin 平台，是独立的低延迟推理加速器机架；本文只用它说明平台边界，不把其 SRAM、带宽或性能写成 Rubin GPU 规格。[官方公告](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform)（访问：2026-08-22）。
> 第 17 行：
> 第 18 行：**为什么选 Rubin。** 在指定时间窗内，Rubin 是 NVIDIA 正式宣布并进入量产爬坡的最新数据中心 GPU 平台；CPX 更新近、问题相关性强，但仍是预期产品。因此主对象是 Rubin GPU，CPX 只用于说明 NVIDIA 对长上下文的另一条产品边界。当前核验到 2026-08-22 的 [NVIDIA 数据中心产品页](https://www.nvidia.com/en-us/data-center/products/)、官方新闻和技术文中，未发现比 Rubin/CPX 更新且已宣布或可用的 NVIDIA 数据中心 AI GPU（这是本次核验范围内的结论）。
> 第 19 行：
> 第 21 行：
> 第 22 行：| 项目 | Rubin GPU 公开规格 | 边界与状态 |
> 第 23 行：|---|---|---|
> 第 28 行：| 互联 | NVLink 6：每 GPU 3.6 TB/s 双向 GPU-GPU 带宽；x16 PCIe Gen6 最高 256 GB/s 主机连接。NVL72 的 NVLink 域为 260 TB/s、72 GPU all-to-all。来源：[NVLink 页](https://www.nvidia.com/en-gb/data-center/nvlink/)；[架构文](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)（访问：2026-08-22）。 | 3.6 TB/s 是每 GPU 的互联带宽，260 TB/s 是 NVL72 系统值；二者不是冲突。 |
> 第 29 行：| 功耗 | **单 GPU TDP/功耗公开资料未确认** | datasheet 在 NVL4 对比中出现 1,800 W/GPU 的测试假设，但那是系统性能比较口径，不应当作 Rubin 单卡 TDP。来源：[datasheet](https://dam-cdn.nvd.orangelogic.com/AssetLink/v5rf2icnf86o26e464tf6djn23r8ibhe.pdf)（访问：2026-08-22）。 |
> 第 30 行：
> 第 32 行：
> 第 33 行：原始 ELI5 附件（当前目录未提供）把推理 GPU 拆成四个难题：密集计算、动态检索/Indexer、Top-k/Reduce、离散 KV Gather 与跨卡通信。Rubin 的回答是：先把“算、搬、等、跨卡传”做得更顺，但没有公开一个专门的 Retrieval Plane。
> 第 34 行：
> 第 35 行：**类比。** Tensor Core 像大工厂，HBM4 像工厂旁的大仓库；TMA 像能按运输单把规则货箱送到工位的自动传送带；TMA 的 inline descriptor update 像同一张运输单可以在运行时改货物起点和步长，不必为每个专家重新制作一张单。生产者 kernel 做完一个 tile，消费者 kernel 可在所需输入到达后更早启动，像收货线按托盘到达开工，而不是等整车到齐。NVLink 6 则是机架内高速公路，SHARP 可在网络中做部分 collective reduction。来源：[Rubin 架构深读](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)；[NVLink 6](https://www.nvidia.com/en-gb/data-center/nvlink/)（访问：2026-08-22）。
> 第 36 行：
> 第 37 行：**技术层。** Rubin 公布了 TMA 的复杂布局搬运、运行时 descriptor 的 pointer/stride 更新、tile-level dependent-kernel triggering、device-initiated NVLink 的 counted writes，以及 attention 中把 dense QKᵀ 中间结果压成结构化 2:4 稀疏格式后再做 softmax/后续 GEMM。这些能力减少元数据、等待或中间结果写入的压力，属于对数据路径的硬件—软件协同优化。[官方解释](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)（访问：2026-08-22）。
> 第 38 行：
> 第 54 行：
> 第 55 行：评分依据是[Rubin 架构深读](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)、[Rubin 官方规格](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)和 [NVLink 6 说明](https://www.nvidia.com/en-gb/data-center/nvlink/)（访问：2026-08-22）；分项分数是本文的架构研究判断，不是 NVIDIA benchmark 或性能承诺。
> 第 56 行：
> 第 77 行：- **可直接借鉴：descriptor 驱动的数据搬运。** 保留可复用 descriptor，并允许运行时更新 base pointer/stride；但 Retrieval GPU 还应把 page list、索引检查和合并规则纳入 descriptor。
> 第 78 行：- **可直接借鉴：tile 级依赖触发。** 让 Search/score/Select/Gather/Attention 按 tile 或候选块流水，而不是每个阶段等整张 grid；Rubin 的公开机制证明依赖调度本身值得硬件化。
> 第 79 行：- **可直接借鉴：片上中间结果压缩与局部性。** 借鉴“尽量不把中间 score 写回 HBM”的目标，但 Exact Mode 需要保留精确语义并测 HBM bytes/token。
> 第 90 行：
> 第 91 行：1. [NVIDIA Rubin 平台宣布，2026-01-05](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer)
> 第 92 行：2. [Vera Rubin 平台进入 full production，2026-03-16](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform)
> 第 93 行：3. [Vera Rubin 爬产与系统规模化，2026-05-31](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Vera-Rubin-Ramps-Into-Full-Production-to-Power-Agentic-AI-Factories-Worldwide/default.aspx)
> 第 94 行：4. [Rubin GPU 架构深读，2026-07-21](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)
> 第 95 行：5. [Vera Rubin NVL72 产品页与单 GPU/系统规格](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)
> 第 96 行：6. [Vera Rubin datasheet](https://dam-cdn.nvd.orangelogic.com/AssetLink/v5rf2icnf86o26e464tf6djn23r8ibhe.pdf)
> 第 97 行：7. [第六代 NVLink 与 NVLink Switch](https://www.nvidia.com/en-gb/data-center/nvlink/)
> 第 98 行：8. [Rubin CPX 宣布与可用时间，2025-09-09](https://nvidianews.nvidia.com/news/nvidia-unveils-rubin-cpx-a-new-class-of-gpu-designed-for-massive-context-inference)
> 第 99 行：+## 2026-09-01 在线复核增补
> 第 100 行：
> 第 101 行：已重新打开 [NVIDIA Vera Rubin 官方新闻](https://blogs.nvidia.com/blog/vera-rubin-lpx-spectrum-x-nvlink-fusion/) 与 [NVIDIA Vera Rubin 科学计算公告](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-delivers-world-class-supercomputers-for-science)，确认 2026-08-24 官方文中将 Groq 3 LPX称为 full production，并把 Vera Rubin系统/多 GPU 机架单独描述；该状态不能回填为 Rubin 单 GPU 的出货或单卡零售可用。

## 直接来源链接

1. <https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/>；NVLink 6
2. <https://www.nvidia.com/en-gb/data-center/nvlink/>（访问：2026-08-22）
3. <https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer>；[量产](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform)；[爬产](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Vera-Rubin-Ramps-Into-Full-Production-to-Power-Agentic-AI-Factories-Worldwide/default.aspx)；[合作伙伴部署](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)（均访问：2026-08-22）
4. <https://nvidianews.nvidia.com/news/nvidia-unveils-rubin-cpx-a-new-class-of-gpu-designed-for-massive-context-inference>（访问：2026-08-22）
5. <https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform>（访问：2026-08-22）
6. <https://www.nvidia.com/en-us/data-center/products/>、官方新闻和技术文中，未发现比
7. <https://www.nvidia.com/en-gb/data-center/nvlink/>；[架构文](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)（访问：2026-08-22）
8. <https://dam-cdn.nvd.orangelogic.com/AssetLink/v5rf2icnf86o26e464tf6djn23r8ibhe.pdf>（访问：2026-08-22）
9. <https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/>（访问：2026-08-22）
10. <https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/>、Rubin
11. <https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/>和 NVLink 6
12. <https://www.nvidia.com/en-gb/data-center/nvlink/>（访问：2026-08-22）；分项分数是本文的架构研究判断，不是
13. <https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer>
14. <https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform>
15. <https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Vera-Rubin-Ramps-Into-Full-Production-to-Power-Agentic-AI-Factories-Worldwide/default.aspx>
16. <https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/>
17. <https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/>
18. <https://dam-cdn.nvd.orangelogic.com/AssetLink/v5rf2icnf86o26e464tf6djn23r8ibhe.pdf>
19. <https://www.nvidia.com/en-gb/data-center/nvlink/>
20. <https://nvidianews.nvidia.com/news/nvidia-unveils-rubin-cpx-a-new-class-of-gpu-designed-for-massive-context-inference>
21. <https://blogs.nvidia.com/blog/vera-rubin-lpx-spectrum-x-nvlink-fusion/>
22. <https://nvidianews.nvidia.com/news/nvidia-vera-rubin-delivers-world-class-supercomputers-for-science>，确认

## 证据边界

- 这是资料重排页，不是重新发布或重新核验的产品公告。
- “发布、流片、送样、量产、出货、客户部署、云端可用、路线图、停产”等状态只在综合报告明确写出时保留；缺失项仍为“公开资料未确认”。
- 若摘录同时出现芯片、板卡、服务器、机架或云服务，均按原报告层级保留，并以“产品层级”字段提醒，不做跨层级推导。

## 关联表格原文（完整表格）

以下表格块来自综合报告中与本拆分项命中的表格，完整保留表头、状态列和规格列。

> 来源综合报告第 11-14 行：
> 第 11 行：| 对象 | 窗口内状态 | 芯片与系统边界 |
> 第 12 行：|---|---|---|
> 第 13 行：| **Rubin GPU** | 2026-01-05 宣布 Rubin 平台；2026-03-16 NVIDIA 称平台七颗芯片进入 full production；2026-05-31 称 Vera Rubin 正在爬产，2026-07-21 官方技术文公开架构细节。产品处于量产爬坡、合作伙伴部署/出货阶段；单卡直接购买状态公开资料未确认。来源：[宣布](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer)；[量产](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform)；[爬产](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Vera-Rubin-Ramps-Into-Full-Production-to-Power-Agentic-AI-Factories-Worldwide/default.aspx)；[合作伙伴部署](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)（均访问：2026-08-22）。 | 一颗 Rubin GPU：288 GB HBM4。Vera Rubin Superchip 是 2 颗 GPU + 1 颗 Vera CPU；NVL72 是 72 颗 GPU + 36 颗 CPU 的机架系统，不能把后两者规格写成单芯片规格。 |
> 第 14 行：| **Rubin CPX** | 2025-09-09 宣布，官方状态为“预计 2026 年底可用”，截至截止日仍不是已可获得产品。来源：[NVIDIA 新闻稿](https://nvidianews.nvidia.com/news/nvidia-unveils-rubin-cpx-a-new-class-of-gpu-designed-for-massive-context-inference)（访问：2026-08-22）。 | 这是面向百万 token 上下文的独立 NVIDIA GPU，采用 128 GB GDDR7、最高 30 PFLOPS NVFP4；不能把 CPX 的 GDDR7 规格与 Rubin GPU 的 HBM4 混写。 |

> 来源综合报告第 22-29 行：
> 第 22 行：| 项目 | Rubin GPU 公开规格 | 边界与状态 |
> 第 23 行：|---|---|---|
> 第 24 行：| 制程 | **公开资料未确认** | NVIDIA 产品页、架构文和 datasheet 没有给出制程节点；不能用传闻补齐。来源：[产品页](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)（访问：2026-08-22）。 |
> 第 25 行：| 计算单元 | 3360 亿晶体管、224 SM、896 Tensor Core；第五代 Tensor Core、第三代 Transformer Engine。来源：[架构文](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)（访问：2026-08-22）。 | 这是 GPU 层信息；GPC、集中式 L2、GigaThread Engine、MIG Control 的容量或细节未完整公开。 |
> 第 26 行：| 数值格式 | NVFP4 推理最高 50 PFLOPS（官方脚注明确为 sparse specification）；NVFP4 训练 35 PFLOPS 为 dense；另列 FP8/FP6、FP16/BF16、TF32、FP32、FP64。支持矩阵 B 的 3-bit lookup-table 格式。来源：[官方规格](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)；[datasheet](https://dam-cdn.nvd.orangelogic.com/AssetLink/v5rf2icnf86o26e464tf6djn23r8ibhe.pdf)（访问：2026-08-22）。 | PFLOPS 是峰值/规格口径，不是 Indexer 或端到端推理速度。 |
> 第 27 行：| 内存 | GPU：288 GB HBM4，最高 22 TB/s；HBM4 是封装旁高带宽内存，不等于片上 SRAM。来源：[官方规格](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)（访问：2026-08-22）。 | 片上 L2/SRAM 容量：公开资料未确认。Superchip 的 1.5 TB LPDDR5X 和 1.8 TB/s NVLink-C2C 属于 CPU-GPU 系统边界。 |
> 第 28 行：| 互联 | NVLink 6：每 GPU 3.6 TB/s 双向 GPU-GPU 带宽；x16 PCIe Gen6 最高 256 GB/s 主机连接。NVL72 的 NVLink 域为 260 TB/s、72 GPU all-to-all。来源：[NVLink 页](https://www.nvidia.com/en-gb/data-center/nvlink/)；[架构文](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)（访问：2026-08-22）。 | 3.6 TB/s 是每 GPU 的互联带宽，260 TB/s 是 NVL72 系统值；二者不是冲突。 |
> 第 29 行：| 功耗 | **单 GPU TDP/功耗公开资料未确认** | datasheet 在 NVL4 对比中出现 1,800 W/GPU 的测试假设，但那是系统性能比较口径，不应当作 Rubin 单卡 TDP。来源：[datasheet](https://dam-cdn.nvd.orangelogic.com/AssetLink/v5rf2icnf86o26e464tf6djn23r8ibhe.pdf)（访问：2026-08-22）。 |

## 补充直接来源链接

1. <https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/>（访问：2026-08-22）
2. <https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/>；[datasheet](https://dam-cdn.nvd.orangelogic.com/AssetLink/v5rf2icnf86o26e464tf6djn23r8ibhe.pdf)（访问：2026-08-22）
