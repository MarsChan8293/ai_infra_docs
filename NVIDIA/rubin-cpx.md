# NVIDIA / 英伟达 — Rubin CPX

- 研究截止日：2026-09-05
- 核验日期：2026-09-05
- 产品层级：GPU 芯片/路线图产品
- 综合报告：[01-nvidia.md](./01-nvidia.md)
- 页面性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容按对象边界重排自现有综合报告，并以本页直接来源清单核验；不能由相邻产品层级推导的项目保留为“公开资料未确认”。

研究对象：NVIDIA Rubin GPU；Vera Rubin 是系统边界，Rubin CPX 是同代长上下文变体。研究窗口：2025-07-01 至 2026-08-22。资料访问日期：2026-08-22。

+## 2026-09-01 在线复核增补

## 关联证据与规格

本节保留与本对象相关的关联规格和生命周期证据；其中的卡、模块、服务器、机架、集群或云数据保持原产品层级，不能回填为芯片规格。

| 对象 | 窗口内状态 | 芯片与系统边界 |
|---|---|---|
| **Rubin GPU** | 2026-01-05 宣布 Rubin 平台；2026-03-16 NVIDIA 称平台七颗芯片进入 full production；2026-05-31 称 Vera Rubin 正在爬产，2026-07-21 官方技术文公开架构细节。产品处于量产爬坡、合作伙伴部署/出货阶段；单卡直接购买状态公开资料未确认。来源：[宣布](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer)；[量产](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform)；[爬产](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Vera-Rubin-Ramps-Into-Full-Production-to-Power-Agentic-AI-Factories-Worldwide/default.aspx)；[合作伙伴部署](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)（均访问：2026-08-22）。 | 一颗 Rubin GPU：288 GB HBM4。Vera Rubin Superchip 是 2 颗 GPU + 1 颗 Vera CPU；NVL72 是 72 颗 GPU + 36 颗 CPU 的机架系统，不能把后两者规格写成单芯片规格。 |
| **Rubin CPX** | 2025-09-09 宣布，官方状态为“预计 2026 年底可用”，截至截止日仍不是已可获得产品。来源：[NVIDIA 新闻稿](https://nvidianews.nvidia.com/news/nvidia-unveils-rubin-cpx-a-new-class-of-gpu-designed-for-massive-context-inference)（访问：2026-08-22）。 | 这是面向百万 token 上下文的独立 NVIDIA GPU，采用 128 GB GDDR7、最高 30 PFLOPS NVFP4；不能把 CPX 的 GDDR7 规格与 Rubin GPU 的 HBM4 混写。 |

## 直接来源

1. [宣布](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer)；核验日期：2026-09-05。
2. [量产](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform)；核验日期：2026-09-05。
3. [爬产](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Vera-Rubin-Ramps-Into-Full-Production-to-Power-Agentic-AI-Factories-Worldwide/default.aspx)；核验日期：2026-09-05。
4. [合作伙伴部署](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)；核验日期：2026-09-05。
5. [NVIDIA 新闻稿](https://nvidianews.nvidia.com/news/nvidia-unveils-rubin-cpx-a-new-class-of-gpu-designed-for-massive-context-inference)；核验日期：2026-09-05。
6. [第六代 NVLink 与 NVLink Switch](https://www.nvidia.com/en-gb/data-center/nvlink/)；核验日期：2026-09-05。

## 证据边界

- 芯片、封装、卡/模组、服务器/机架、集群、软件和云服务按来源原层级记录；系统、卡、模块或集群数据不自动回填为芯片规格。
- “宣布、流片/工程样片、送样、量产、出货、客户部署、云/实例可用、路线图、停产”分别判断；没有直接证据的阶段写为“公开资料未确认”。
- 官方发布、产品页或软件支持不能单独证明量产、出货或独立性能；厂商主张、独立验证和分析推断不混写。
- 本页是基于现有综合报告和直接来源的证据重排页；引用以文末直接 URL 为准，不再使用综合报告行号作为外部引用。
