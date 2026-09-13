# NVIDIA / 英伟达 — Rubin GPU

- 研究截止日：2026-09-05
- 核验日期：2026-09-05
- 产品层级：GPU 芯片
- 厂商总览：[NVIDIA / 英伟达](./NVIDIA-overview.md) · [[NVIDIA-overview|图谱总览]]
- 页面性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容按对象边界重排自现有综合报告，并以本页直接来源清单核验；不能由相邻产品层级推导的项目保留为“公开资料未确认”。

# 厂商与芯片：2025-06 之后最新款——NVIDIA Rubin GPU

研究对象：NVIDIA Rubin GPU；Vera Rubin 是系统边界，Rubin CPX 是同代长上下文变体。研究窗口：2025-07-01 至 2026-08-22。原始资料访问日期：2026-08-22；本次结构核验：2026-09-05。Hot Chips 2026 议程只作为会议证据入口，未据此新增 Rubin 规格。

Rubin 最值得研究的地方，不是把 Tensor Core 再堆大，而是把 **HBM4、TMA 数据搬运、依赖触发和 NVLink 6** 组合成一条更紧的推理执行路径。它确实改善了密集计算、规则张量搬运、跨卡通信和 kernel 间等待；但公开资料没有证明它已经提供附件设想的独立 **Search/Indexer、精确 Local/Global Top-k、page-aware Indexed Gather DMA**。因此，它是“更强的推理 GPU + 系统协同”，还不是完整的 Retrieval GPU。[架构深读](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)；[NVLink 6](https://www.nvidia.com/en-gb/data-center/nvlink/)（访问：2026-08-22）。

**跨边界注记。** Groq 3 LPX 在 2026-03-16 被 NVIDIA 纳入 Vera Rubin 平台，是独立的低延迟推理加速器机架；本文只用它说明平台边界，不把其 SRAM、带宽或性能写成 Rubin GPU 规格。[官方公告](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform)（访问：2026-08-22）。

**为什么选 Rubin。** 在指定时间窗内，Rubin 是 NVIDIA 正式宣布并进入量产爬坡的最新数据中心 GPU 平台；CPX 更新近、问题相关性强，但仍是预期产品。因此主对象是 Rubin GPU，CPX 只用于说明 NVIDIA 对长上下文的另一条产品边界。当前核验到 2026-08-22 的 [NVIDIA 数据中心产品页](https://www.nvidia.com/en-us/data-center/products/)、官方新闻和技术文中，未发现比 Rubin/CPX 更新且已宣布或可用的 NVIDIA 数据中心 AI GPU（这是本次核验范围内的结论）。

原始 ELI5 附件（当前目录未提供）把推理 GPU 拆成四个难题：密集计算、动态检索/Indexer、Top-k/Reduce、离散 KV Gather 与跨卡通信。Rubin 的回答是：先把“算、搬、等、跨卡传”做得更顺，但没有公开一个专门的 Retrieval Plane。

**类比。** Tensor Core 像大工厂，HBM4 像工厂旁的大仓库；TMA 像能按运输单把规则货箱送到工位的自动传送带；TMA 的 inline descriptor update 像同一张运输单可以在运行时改货物起点和步长，不必为每个专家重新制作一张单。生产者 kernel 做完一个 tile，消费者 kernel 可在所需输入到达后更早启动，像收货线按托盘到达开工，而不是等整车到齐。NVLink 6 则是机架内高速公路，SHARP 可在网络中做部分 collective reduction。来源：[Rubin 架构深读](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)；[NVLink 6](https://www.nvidia.com/en-gb/data-center/nvlink/)（访问：2026-08-22）。

**技术层。** Rubin 公布了 TMA 的复杂布局搬运、运行时 descriptor 的 pointer/stride 更新、tile-level dependent-kernel triggering、device-initiated NVLink 的 counted writes，以及 attention 中把 dense QKᵀ 中间结果压成结构化 2:4 稀疏格式后再做 softmax/后续 GEMM。这些能力减少元数据、等待或中间结果写入的压力，属于对数据路径的硬件—软件协同优化。[官方解释](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)（访问：2026-08-22）。

评分依据是[Rubin 架构深读](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)、[Rubin 官方规格](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)和 [NVLink 6 说明](https://www.nvidia.com/en-gb/data-center/nvlink/)（访问：2026-08-22）；分项分数是本文的架构研究判断，不是 NVIDIA benchmark 或性能承诺。

- **可直接借鉴：descriptor 驱动的数据搬运。** 保留可复用 descriptor，并允许运行时更新 base pointer/stride；但 Retrieval GPU 还应把 page list、索引检查和合并规则纳入 descriptor。
- **可直接借鉴：tile 级依赖触发。** 让 Search/score/Select/Gather/Attention 按 tile 或候选块流水，而不是每个阶段等整张 grid；Rubin 的公开机制证明依赖调度本身值得硬件化。
- **可直接借鉴：片上中间结果压缩与局部性。** 借鉴“尽量不把中间 score 写回 HBM”的目标，但 Exact Mode 需要保留精确语义并测 HBM bytes/token。

+## 2026-09-01 在线复核增补

已重新打开 [NVIDIA Vera Rubin 官方新闻](https://blogs.nvidia.com/blog/vera-rubin-lpx-spectrum-x-nvlink-fusion/) 与 [NVIDIA Vera Rubin 科学计算公告](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-delivers-world-class-supercomputers-for-science)，确认 2026-08-24 官方文中将 Groq 3 LPX称为 full production，并把 Vera Rubin系统/多 GPU 机架单独描述；该状态不能回填为 Rubin 单 GPU 的出货或单卡零售可用。

## 关联证据与规格

本节保留与本对象相关的关联规格和生命周期证据；其中的卡、模块、服务器、机架、集群或云数据保持原产品层级，不能回填为芯片规格。

| 对象 | 窗口内状态 | 芯片与系统边界 |
|---|---|---|
| **Rubin GPU** | 2026-01-05 宣布 Rubin 平台；2026-03-16 NVIDIA 称平台七颗芯片进入 full production；2026-05-31 称 Vera Rubin 正在爬产，2026-07-21 官方技术文公开架构细节。产品处于量产爬坡、合作伙伴部署/出货阶段；单卡直接购买状态公开资料未确认。来源：[宣布](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer)；[量产](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform)；[爬产](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Vera-Rubin-Ramps-Into-Full-Production-to-Power-Agentic-AI-Factories-Worldwide/default.aspx)；[合作伙伴部署](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)（均访问：2026-08-22）。 | 一颗 Rubin GPU：288 GB HBM4。Vera Rubin Superchip 是 2 颗 GPU + 1 颗 Vera CPU；NVL72 是 72 颗 GPU + 36 颗 CPU 的机架系统，不能把后两者规格写成单芯片规格。 |
| **Rubin CPX** | 2025-09-09 宣布，官方状态为“预计 2026 年底可用”，截至截止日仍不是已可获得产品。来源：[NVIDIA 新闻稿](https://nvidianews.nvidia.com/news/nvidia-unveils-rubin-cpx-a-new-class-of-gpu-designed-for-massive-context-inference)（访问：2026-08-22）。 | 这是面向百万 token 上下文的独立 NVIDIA GPU，采用 128 GB GDDR7、最高 30 PFLOPS NVFP4；不能把 CPX 的 GDDR7 规格与 Rubin GPU 的 HBM4 混写。 |

| 项目 | Rubin GPU 公开规格 | 边界与状态 |
|---|---|---|
| 制程 | **公开资料未确认** | NVIDIA 产品页、架构文和 datasheet 没有给出制程节点；不能用传闻补齐。来源：[产品页](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)（访问：2026-08-22）。 |
| 计算单元 | 3360 亿晶体管、224 SM、896 Tensor Core；第五代 Tensor Core、第三代 Transformer Engine。来源：[架构文](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)（访问：2026-08-22）。 | 这是 GPU 层信息；GPC、集中式 L2、GigaThread Engine、MIG Control 的容量或细节未完整公开。 |
| 数值格式 | NVFP4 推理最高 50 PFLOPS（官方脚注明确为 sparse specification）；NVFP4 训练 35 PFLOPS 为 dense；另列 FP8/FP6、FP16/BF16、TF32、FP32、FP64。支持矩阵 B 的 3-bit lookup-table 格式。来源：[官方规格](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)；[datasheet](https://dam-cdn.nvd.orangelogic.com/AssetLink/v5rf2icnf86o26e464tf6djn23r8ibhe.pdf)（访问：2026-08-22）。 | PFLOPS 是峰值/规格口径，不是 Indexer 或端到端推理速度。 |
| 内存 | GPU：288 GB HBM4，最高 22 TB/s；HBM4 是封装旁高带宽内存，不等于片上 SRAM。来源：[官方规格](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)（访问：2026-08-22）。 | 片上 L2/SRAM 容量：公开资料未确认。Superchip 的 1.5 TB LPDDR5X 和 1.8 TB/s NVLink-C2C 属于 CPU-GPU 系统边界。 |
| 互联 | NVLink 6：每 GPU 3.6 TB/s 双向 GPU-GPU 带宽；x16 PCIe Gen6 最高 256 GB/s 主机连接。NVL72 的 NVLink 域为 260 TB/s、72 GPU all-to-all。来源：[NVLink 页](https://www.nvidia.com/en-gb/data-center/nvlink/)；[架构文](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)（访问：2026-08-22）。 | 3.6 TB/s 是每 GPU 的互联带宽，260 TB/s 是 NVL72 系统值；二者不是冲突。 |
| 功耗 | **单 GPU TDP/功耗公开资料未确认** | datasheet 在 NVL4 对比中出现 1,800 W/GPU 的测试假设，但那是系统性能比较口径，不应当作 Rubin 单卡 TDP。来源：[datasheet](https://dam-cdn.nvd.orangelogic.com/AssetLink/v5rf2icnf86o26e464tf6djn23r8ibhe.pdf)（访问：2026-08-22）。 |

## 直接来源

1. [架构深读](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)；核验日期：2026-09-05。
2. [NVLink 6](https://www.nvidia.com/en-gb/data-center/nvlink/)；核验日期：2026-09-05。
3. [宣布](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer)；核验日期：2026-09-05。
4. [量产](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform)；核验日期：2026-09-05。
5. [爬产](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Vera-Rubin-Ramps-Into-Full-Production-to-Power-Agentic-AI-Factories-Worldwide/default.aspx)；核验日期：2026-09-05。
6. [NVIDIA 新闻稿](https://nvidianews.nvidia.com/news/nvidia-unveils-rubin-cpx-a-new-class-of-gpu-designed-for-massive-context-inference)；核验日期：2026-09-05。
7. [NVIDIA 数据中心产品页](https://www.nvidia.com/en-us/data-center/products/)；核验日期：2026-09-05。
8. [datasheet](https://dam-cdn.nvd.orangelogic.com/AssetLink/v5rf2icnf86o26e464tf6djn23r8ibhe.pdf)；核验日期：2026-09-05。
9. [Rubin 官方规格](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)；核验日期：2026-09-05。
10. [NVIDIA Vera Rubin 官方新闻](https://blogs.nvidia.com/blog/vera-rubin-lpx-spectrum-x-nvlink-fusion/)；核验日期：2026-09-05。
11. [NVIDIA Vera Rubin 科学计算公告](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-delivers-world-class-supercomputers-for-science)；核验日期：2026-09-05。

## 证据边界

- 芯片、封装、卡/模组、服务器/机架、集群、软件和云服务按来源原层级记录；系统、卡、模块或集群数据不自动回填为芯片规格。
- “宣布、流片/工程样片、送样、量产、出货、客户部署、云/实例可用、路线图、停产”分别判断；没有直接证据的阶段写为“公开资料未确认”。
- 官方发布、产品页或软件支持不能单独证明量产、出货或独立性能；厂商主张、独立验证和分析推断不混写。
- 本页是基于现有综合报告和直接来源的证据重排页；引用以文末直接 URL 为准，不再使用综合报告行号作为外部引用。
