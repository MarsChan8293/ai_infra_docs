# Groq — GroqChip（上一代基线）

- 拆分日期：2026-09-02
- 产品层级：上一代芯片基线
- 综合报告：[07-groq-lpu.md](./07-groq-lpu.md)
- 文件性质：从综合报告按芯片名称/家族拆分的证据页；不新增事实，不把板卡、服务器、机架或云服务规格回填为芯片规格。

## 产品定位与关键证据

以下内容逐行摘录综合报告，保留原报告中的状态、数字、证据等级和未知项。

> 第 38 行：| 互联 | 每颗 [96 条 C2C link、112 Gbps/link、双向聚合 2.5 TB/s](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)；整架 [640 TB/s scale-up](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)、[256 芯片](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | LPX 还有 C2C spine 与 fabric logic，不能简单复述为“完全没有系统级互联逻辑” |
> 第 39 行：| 功耗/散热 | **LP30 单芯片功耗公开资料未确认**；LPX 公开为全液冷 | Groq 旧 GroqChip 的 [300 W max/215 W TDP/185 W average](https://www.groq.com/GroqDocs/Product%20Spec%20Sheet%20-%20GroqChip%E2%84%A2%20Processor.pdf) 不能移植给 LP30，仅作时间边界 |
> 第 40 行：
> 第 87 行：2. **确定性不等于所有请求都零抖动。** 它主要约束已编译的算子与通信；动态分支、外部网络、云端排队和模型装载仍可能变化。
> 第 88 行：3. **Groq 3 不等于旧 GroqChip 规格升级版的简单换名。** [14 nm、230 MB、80 TB/s、215 W TDP](https://www.groq.com/GroqDocs/Product%20Spec%20Sheet%20-%20GroqChip%E2%84%A2%20Processor.pdf) 是旧公开产品值，不能推导 LP30 的制程和功耗。
> 第 89 行：4. **LPX 不等于 GroqCloud。** LPX 是 NVIDIA Vera Rubin 侧的机架产品；GroqCloud 是 Groq 独立运营的服务。到截止日，LP30 在 GroqCloud 的规模上线公开证据不足。
> 第 116 行：3. [Groq：From Speed to Scale（2025-05-27）](https://groq.com/blog/from-speed-to-scale-how-groq-is-optimized-for-moe-other-large-models)（大模型/MoE 与 RealScale；访问日 2026-08-22）。
> 第 117 行：4. [Groq：GroqChip Processor Product Brief](https://www.groq.com/GroqDocs/Product%20Spec%20Sheet%20-%20GroqChip%E2%84%A2%20Processor.pdf)（旧一代规格，仅作时间边界；访问日 2026-08-22）。
> 第 118 行：5. [Groq：与 NVIDIA 的非排他推理技术授权公告（2025-12-24）](https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale)（独立运营与 GroqCloud 连续性；访问日 2026-08-22）。

## 直接来源链接

1. <https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/>；整架
2. <https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/>、256
3. <https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/>
4. <https://www.groq.com/GroqDocs/Product%20Spec%20Sheet%20-%20GroqChip%E2%84%A2%20Processor.pdf>
5. <https://groq.com/blog/from-speed-to-scale-how-groq-is-optimized-for-moe-other-large-models>（大模型/MoE
6. <https://www.groq.com/GroqDocs/Product%20Spec%20Sheet%20-%20GroqChip%E2%84%A2%20Processor.pdf>（旧一代规格，仅作时间边界；访问日
7. <https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale>（独立运营与

## 证据边界

- 这是资料重排页，不是重新发布或重新核验的产品公告。
- “发布、流片、送样、量产、出货、客户部署、云端可用、路线图、停产”等状态只在综合报告明确写出时保留；缺失项仍为“公开资料未确认”。
- 若摘录同时出现芯片、板卡、服务器、机架或云服务，均按原报告层级保留，并以“产品层级”字段提醒，不做跨层级推导。

## 关联表格原文（完整表格）

以下表格块来自综合报告中与本拆分项命中的表格，完整保留表头、状态列和规格列。

> 来源综合报告第 30-39 行：
> 第 30 行：| 项目 | Groq 3 / LP30 公开口径 | 研究边界 |
> 第 31 行：|---|---|---|
> 第 32 行：| 制程 | **公开资料未确认**。Groq 只公开说现有/第一代芯片为 [14 nm](https://groq.com/blog/the-groq-lpu-explained)，并说未来向 [4 nm](https://groq.com/blog/the-groq-lpu-explained) 发展 | 不能把 14 nm 或 4 nm 直接套到 LP30 |
> 第 33 行：| 执行单元 | MXM 矩阵执行、VXM 向量执行、SXM 数据交换；统一工作粒度为 [320-byte vector](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | 各单元数量、频率、面积未公开确认；按 [8 颗](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) 托盘的 [9.6 PFLOPS](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) 推得约 [1.2 PFLOPS FP8/颗](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，这是推导值 |
> 第 34 行：| 数值格式 | 公开的 LPU 方案包括 TruePoint 的 [100-bit 中间累加](https://home.cloud.groq.io/blog/inside-the-lpu-deconstructing-groq-speed)、FP32 attention logits、MoE 权重的 block floating point、FP8 activation；LPX 机架标注 FP8 inference compute | LP30 完整格式/吞吐表未公开确认 |
> 第 35 行：| 片上内存 | 每颗 [500 MB SRAM](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，作为主要工作存储而非传统 cache | 容量有限，不能等同于整机模型容量 |
> 第 36 行：| 片外内存 | LPX 机架另有 [12 TB DDR5](https://www.nvidia.com/en-au/data-center/lpx/)，托盘侧公开为 fabric expansion logic 最多 [256 GB](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)、主机最多 [128 GB](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | “SRAM-first”不等于整架没有片外内存；LP30 本身没有公开 HBM 规格 |
> 第 37 行：| 带宽 | 单颗 SRAM [150 TB/s](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，单托盘 [1.2 PB/s](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)，整架 [40 PB/s](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | 这些是峰值/聚合口径，不是某个模型的有效 KV 带宽 |
> 第 38 行：| 互联 | 每颗 [96 条 C2C link、112 Gbps/link、双向聚合 2.5 TB/s](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)；整架 [640 TB/s scale-up](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)、[256 芯片](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) | LPX 还有 C2C spine 与 fabric logic，不能简单复述为“完全没有系统级互联逻辑” |
> 第 39 行：| 功耗/散热 | **LP30 单芯片功耗公开资料未确认**；LPX 公开为全液冷 | Groq 旧 GroqChip 的 [300 W max/215 W TDP/185 W average](https://www.groq.com/GroqDocs/Product%20Spec%20Sheet%20-%20GroqChip%E2%84%A2%20Processor.pdf) 不能移植给 LP30，仅作时间边界 |

## 补充直接来源链接

1. <https://groq.com/blog/the-groq-lpu-explained>，并说未来向
2. <https://groq.com/blog/the-groq-lpu-explained>
3. <https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/>，这是推导值
4. <https://home.cloud.groq.io/blog/inside-the-lpu-deconstructing-groq-speed>、FP32
5. <https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/>，作为主要工作存储而非传统
6. <https://www.nvidia.com/en-au/data-center/lpx/>，托盘侧公开为
7. <https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/>、主机最多
8. <https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/>，单托盘
9. <https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/>，整架
