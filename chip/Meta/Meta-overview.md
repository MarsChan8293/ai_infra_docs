# Meta 芯片资料

- 研究截止日：2026-09-13
- 核验日期：2026-09-13
- 厂商范围：Meta 自研 MTIA（Meta Training and Inference Accelerator）系列
- 证据原则：相对代际提升、芯片规格、72 卡 scale-up 域和生产部署状态分别记录

## 芯片页关系导航

- [[mtia-300|Meta — MTIA 300]] · [打开 Markdown](./mtia-300.md)
- [[mtia-400|Meta — MTIA 400]] · [打开 Markdown](./mtia-400.md)
- [[mtia-450|Meta — MTIA 450]] · [打开 Markdown](./mtia-450.md)
- [[mtia-500|Meta — MTIA 500]] · [打开 Markdown](./mtia-500.md)

## 代际路线

Meta 在 2026-03-11 集中公开 MTIA 300/400/450/500 路线，并确认更早的 MTIA 100/200 已有数十万颗部署于生产。新四代的重点不是单纯堆峰值，而是通过 chiplet、HBM、片上/片间通信与低精度格式快速迭代，从推荐系统扩展到 GenAI 训练和推理。

| 代际 | 重点工作负载 | 公开状态 | 关键边界 |
| --- | --- | --- | --- |
| MTIA 300 | Ranking & Recommendation 训练 | 已在生产 | 1 个 compute chiplet + 2 个 network chiplet + HBM |
| MTIA 400 | GenAI + R&R | 实验室测试完成，走向数据中心部署 | 2 个 compute chiplet；72 加速器 scale-up 是机架/系统层 |
| MTIA 450 | GenAI 推理优先 | 计划 2027 年初大规模部署 | HBM 带宽为 400 的 2×；MX4 FLOPS +75% |
| MTIA 500 | GenAI 推理优先 | 计划 2027 年大规模部署 | 相对 450：HBM 带宽 +50%、容量最高 +80%、MX4 FLOPS +43% |

Meta 给出的“MTIA 300 到 500：HBM 带宽 4.5×、计算 FLOPS 25×”属于**跨代、跨精度口径比较**，其中计算比较从 MTIA 300 的 MX8 到 MTIA 500 的 MX4，不应写成同精度绝对性能提升。

## 架构脉络

MTIA 300 的 Processing Element 已公开包含两颗 RISC-V vector core、Dot Product Engine、Special Function Unit、Reduction Engine 与 DMA engine。后续代际沿着更多 compute chiplet、更高 HBM 带宽、低精度格式和 attention/FFN 专用加速方向演进。

MTIA 400/450/500 复用同一 chassis、rack 和 network infrastructure，是 Meta 缩短硅片到生产部署周期的重要系统策略。该复用能力属于平台/系统层，不应回填为单芯片规格。

## 软件栈

Meta 明确把 MTIA 建在 PyTorch、vLLM、Triton 与 OCP 生态上。编译链涉及 Torch FX/TorchInductor、Triton、MLIR、LLVM；通信层公开 HCCL（Hoot Collective Communications Library）；驱动与固件部分使用 Rust。软件兼容性是 MTIA 快速投产的重要组成，但不能据此推导硬件未公开指令或算力。

## 直接来源

- [Meta AI：Four MTIA Chips in Two Years: Scaling AI Experiences for Billions，2026-03-11](https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/)
- [Meta AI：Next Generation Meta Training and Inference Accelerator，2024-04-10](https://ai.meta.com/blog/next-generation-meta-training-inference-accelerator-AI-MTIA/)
- [Hot Chips 2026 Program](https://hc2026.hotchips.org/program/)

## 待补证据

- MTIA 300/400/450/500 的完整绝对 HBM 容量、带宽、各精度 TOPS/FLOPS 表格需要从官方图表或论文逐项核验后再填。
- 制造节点、封装、chiplet die 面积和功耗的公开边界需要继续补证。
- MTIA 400 实际进入数据中心后的部署规模，以及 450/500 量产部署是否按路线图发生。
- 面向外部客户的可采购性不成立：MTIA 当前主要是 Meta 内部基础设施芯片，应与公有云商品化加速器区分。
