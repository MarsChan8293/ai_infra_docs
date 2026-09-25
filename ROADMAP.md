---
title: AI Infra Docs Roadmap
aliases:
  - 仓库路线图
  - AI Infra Roadmap
tags:
  - roadmap
  - ai-infra
  - planning
updated: 2026-09-25
---

# AI Infra Docs Roadmap

本路线图定义 `ai_infra_docs` 下一阶段的知识建设重点。当前仓库已经完成从“软件项目资料库”向 **Model → System → Chip / Hardware** 的方向调整：模型层记录可验证的模型事实，系统层负责把 workload 转换成计算、内存、通信和拓扑约束，硬件层记录芯片、内存、互联和基础设施事实。

## 实施进度

具体任务、依赖、状态、交付物和验收条件统一维护在 [[TASKS|AI Infra Docs Implementation Tasks]]。**ROADMAP 只维护方向和阶段目标，TASKS 是唯一实施状态源**，避免在多个文档里重复维护 checkbox。

软件项目、社区、能力、集成和维护者关系继续由 [ai_infra_relationship](https://github.com/MarsChan8293/ai_infra_relationship) 维护，本仓库不恢复 `software/` 目录，也不维护软件项目的第二份 canonical 事实。

## 目标状态

仓库最终应能够回答的不只是“某个芯片有什么规格”，而是：

1. 一个模型在给定 workload 下会产生多少计算、权重、KV、Activation 和通信需求。
2. 这些需求经过并行、调度、内存层级和拓扑后，会形成哪些系统瓶颈。
3. 哪些硬件指标决定这些瓶颈的上限。
4. 推导结果来自哪些原始事实、采用什么假设，以及哪些结论仍然未知。

目标主线：

```text
Model intrinsic facts
        ↓
Workload
prompt / output / batch / concurrency / SLA
        ↓
Derived requirements
compute / memory / communication / storage / power
        ↓
System architecture
parallelism / placement / topology / memory hierarchy
        ↓
Hardware capability
accelerator / HBM / fabric / NIC / storage / rack
```

## 当前阶段判断

当前 `chip/` 已经形成较完整的硬件事实库，并具备 Chip Schema、Evidence、自动校验和派生比较能力；`models/` 已建立 Model Schema；`system/` 已有 KV Cache 内存层级、加速器资源模型、拓扑感知调度和异构推理四个核心概念。

下一阶段的主要瓶颈不是继续增加更多小众加速器厂商，而是 **System 层过薄，Model → Hardware 之间缺少可计算、可复用的中间模型**。

资源投入建议：

- 约 60%：扩建 `system/`
- 约 20%：补齐 Model Schema 与代表性模型
- 约 15%：向 Memory / Fabric / Storage / Packaging / Power 等硬件横向扩展
- 约 5%：仓库工程化、贡献规范与发布体验

---

# P0：建立可计算的 System 主干

P0 的完成标志不是“新增若干文章”，而是让 Model facts 能通过统一公式和假设转换为 System requirements。

## 1. Workload Model

建议新增：

```text
system/workload/
  ai-workload-model.md
  inference-workload.md
  training-workload.md
```

至少定义：

- prompt tokens
- output tokens
- batch size
- concurrency
- request rate
- sequence length
- context reuse / prefix reuse
- TTFT / TPOT / latency SLA
- throughput target
- training global batch / micro batch
- sequence packing
- checkpoint interval

原则：

- Model 页面只记录模型固有事实。
- Workload 页面记录运行条件。
- Model × Workload 的派生结果不回填模型固有字段。

## 2. Compute Model

建议新增：

```text
system/compute/
  transformer-compute-model.md
  roofline-and-arithmetic-intensity.md
  prefill-vs-decode.md
```

核心内容：

- Dense Transformer FLOPs
- MoE active FLOPs
- Prefill / Decode 计算结构差异
- GEMM / GEMV 转换
- Arithmetic Intensity
- Compute-bound / Memory-bound 判断
- 理论峰值与实际利用率边界

应明确区分：

- 厂商峰值
- 理论上界
- 系统可达上界
- 实测性能

## 3. Memory Model

在现有 [[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层级]] 基础上补齐完整模型：

```text
system/memory/
  model-memory-accounting.md
  weight-memory.md
  activation-memory.md
  kv-cache-model.md
  memory-bandwidth-model.md
  cxl-and-memory-pooling.md
  kv-cache-memory-hierarchy.md
```

至少覆盖：

```text
Total device memory
= weights
+ KV cache
+ activations
+ workspace
+ communication buffers
+ allocator fragmentation
+ runtime reserve
```

训练侧进一步覆盖：

- parameters
- gradients
- optimizer states
- master weights
- activations
- checkpoint buffers

## 4. Parallelism Model

建议新增：

```text
system/parallelism/
  parallelism-overview.md
  tensor-parallelism.md
  pipeline-parallelism.md
  expert-parallelism.md
  data-parallelism.md
  context-parallelism.md
```

每个并行策略统一回答：

- 切分对象
- 节省了什么
- 增加了什么通信
- 通信量公式
- 延迟敏感度
- 对拓扑的要求
- 适用 workload
- 失效边界

## 5. Communication Model

建议新增：

```text
system/communication/
  collective-communication.md
  all-reduce.md
  all-gather-reduce-scatter.md
  all-to-all.md
  point-to-point.md
  communication-cost-model.md
```

重点建立：

```text
message size
× collective algorithm
× participant count
÷ effective bandwidth
+ latency / synchronization
```

并与：

- Tensor Parallel
- Expert Parallel
- Pipeline Parallel
- KV transfer
- checkpoint

建立内部链接。

## 6. Scale-up / Scale-out Topology

扩展现有 [[system/scheduling/topology-aware-scheduling|拓扑感知调度]]：

```text
system/topology/
  scale-up-vs-scale-out.md
  accelerator-fabric.md
  gpu-nic-affinity.md
  numa-and-pcie-topology.md
  rack-and-failure-domain.md
```

目标是把“有多少张卡”升级为“这些卡通过什么物理路径互连”。

---

# P1：建立推理、训练和 MoE 的系统专题

## 1. Serving Architecture

建议新增：

```text
system/serving/
  llm-serving-model.md
  continuous-batching.md
  prefix-caching.md
  disaggregated-prefill-decode.md
  kv-transfer.md
```

重点解释：

- Prefill 和 Decode 为什么需要不同资源
- P/D 分离的收益条件
- KV transfer 的 break-even
- cache hit rate 对计算和网络的影响
- TTFT、TPOT、throughput 之间的交换

## 2. MoE System Model

建议新增：

```text
system/moe/
  moe-system-model.md
  expert-routing.md
  expert-parallelism-and-all-to-all.md
  load-balancing.md
```

重点关注：

- total parameters vs active parameters
- expert count / top-k
- token dispatch
- all-to-all
- expert imbalance
- EP placement
- Scale-up / Scale-out 边界

## 3. Training System Model

建议新增：

```text
system/training/
  distributed-training-model.md
  training-memory-model.md
  gradient-synchronization.md
  checkpoint-and-recovery.md
```

建立训练与推理之间明确的系统差异，避免用推理指标代替训练指标。

## 4. Reliability / Failure Domain

建议新增：

```text
system/reliability/
  accelerator-failure-domain.md
  network-failure-domain.md
  checkpoint-recovery-model.md
```

把可维护性、重启成本、checkpoint 成本和拓扑纳入 AI Infra 模型。

## 5. Power / Thermal

建议新增：

```text
system/power/
  accelerator-power-model.md
  rack-power-density.md
  cooling-and-liquid-cooling.md
```

系统问题应从单卡 TDP 继续推到：

```text
accelerator
→ node
→ rack
→ cluster
→ facility
```

---

# P1：扩展 Model Schema

当前 Model Schema V0.1 已覆盖：

- total / active parameters
- sparsity
- attention
- context length
- 64K FP8 KV 派生指标

下一版应评估增加下列 **模型固有、可验证** 字段：

- layer count
- hidden size
- attention heads
- KV heads
- head dimension
- expert count
- top-k
- MoE layer frequency
- MLA latent dimensions
- local / sliding window
- linear-attention / SSM recurrent state
- embedding / vocabulary 相关尺寸

原则：

1. 只加入模型固有事实。
2. 运行时性能不进入 Model Schema。
3. TP / EP 配置不进入 Model Schema。
4. 无公开直接证据的字段保持 `null`。
5. FLOPs、内存、通信等派生指标由 System 层生成。

## 模型覆盖策略

不以“最近三个月所有模型”为长期目标，而要同时建立 **architecture anchors**：

- Dense Transformer
- GQA
- MLA
- MoE
- Sparse Attention
- Linear Attention
- SSM
- Multimodal
- Diffusion / DiT
- Long-context / reasoning workload

每种架构选取有代表性且证据充分的模型，使 System 概念能够有真实 workload 锚点。

---

# P1：横向扩展 Hardware，而不是继续堆加速器厂商

当前 accelerator 厂商覆盖已经较广。下一阶段硬件研究优先向加速器周围扩展。

## Memory

目标对象：

- HBM2E / HBM3 / HBM3E / HBM4
- DDR5
- LPDDR
- CXL Memory
- Memory Expander / Memory Pooling
- PIM / Near-memory compute

重点厂商：

- SK hynix
- Samsung
- Micron

关键字段：

- capacity
- bandwidth
- stack / die
- interface width
- speed
- power
- lifecycle

## Scale-up Interconnect

重点：

- NVLink / NVSwitch
- AMD Infinity Fabric
- UALink
- Google TPU ICI
- 其他厂商自研 accelerator fabric

记录：

- link bandwidth
- directionality
- link count
- port count
- topology scale
- supported system generation

## Scale-out Network

逐步覆盖：

- NVIDIA ConnectX / Spectrum-X / InfiniBand
- Broadcom Tomahawk / Jericho
- Marvell
- Cisco Silicon One
- Ethernet AI fabric 相关交换 ASIC / NIC / DPU

## PCIe / CXL

覆盖：

- PCIe Switch
- CXL Switch
- Retimer
- CXL Memory Expander
- Host ↔ Accelerator ↔ NIC 拓扑组件

## Storage

补充与 AI workload 强相关的：

- NVMe SSD
- KV offload tier
- checkpoint storage
- dataset storage
- SSD endurance

字段应明确：

- sequential / random bandwidth
- latency
- DWPD / TBW
- write amplification assumptions
- interface
- capacity
- power

## Packaging

建立：

- CoWoS
- SoIC
- EMIB
- Foveros
- interposer
- chiplet
- HBM integration

Packaging 页面只记录与 AI 芯片能力边界直接相关的事实，不演变为完整半导体工艺百科。

## Power / Cooling Hardware

后续可逐步纳入：

- rack power
- PSU / power shelf
- busbar
- CDU
- cold plate
- liquid cooling topology

---

# P1：System Schema V0.1

`system/` 不应长期保持自由文章集合。建议建立最小 System Schema。

示意：

```yaml
schema_version: system-v0.1
name: Example System Concept
object_type: concept
category: memory
inputs:
  - model.parameters.total
  - workload.sequence_length
constraints:
  - memory-capacity
  - memory-bandwidth
outputs:
  - required_memory_bytes
  - transfer_bytes
related_layers:
  - model
  - memory
  - accelerator
  - network
evidence: {}
updated: 2026-09-25
```

Schema 至少应表达：

- 这个概念消费哪些输入
- 建模哪些约束
- 产生哪些派生指标
- 影响哪些硬件层
- 使用哪些假设
- Evidence 在哪里
- 哪些部分是事实，哪些部分是分析模型

不要求 P0 一开始定义复杂类型系统，先保证 System 页面之间结构一致。

---

# P2：把知识库升级为可派生数据模型

当 P0 / P1 的系统公式稳定后，再进入自动派生阶段。

建议增加：

```text
scripts/
  build-workload-profile.py
  build-system-requirements.py
```

输入：

```text
Model facts
+ Workload profile
+ System assumptions
```

输出可包括：

- weight footprint
- KV footprint
- activation estimate
- theoretical FLOPs
- arithmetic intensity
- minimum HBM bandwidth
- TP communication volume
- EP all-to-all volume
- KV transfer volume
- theoretical network lower bound

所有输出必须保留：

- source facts
- formula
- assumptions
- unit
- uncertainty / unavailable status

禁止把派生值伪装成厂商事实。

---

# 数据质量与 Evidence

所有领域继续遵循同一原则：

```text
事实
≠ 厂商宣称
≠ 理论推导
≠ 第三方测试
≠ 分析判断
```

应逐步统一来源类型：

- official-product
- official-datasheet
- official-blog
- official-code
- paper
- conference
- benchmark
- third-party-analysis

对于关键派生指标，应能够追溯：

```text
Derived value
  ↓
Formula
  ↓
Input fields
  ↓
Evidence
```

---

# 不做什么

下一阶段明确暂缓：

1. 不恢复 `software/`。
2. 不在本仓库复制 `ai_infra_relationship` 的项目事实。
3. 不以新增更多小众 NPU 厂商作为主目标。
4. 不把未经验证的路线图传闻填入确定规格。
5. 不把系统级聚合性能回填成单芯片能力。
6. 不维护手工生成的比较表或图谱 JSON。
7. 不为了知识图谱密度制造无意义内部链接。
8. 不把 Model × Software × Hardware × Workload 的性能结论写成模型固有事实。

---

# 建议实施顺序

## Phase 1：System Foundation

优先完成：

1. Workload Model
2. Compute Model
3. Memory Model
4. Parallelism Model
5. Communication Model
6. Scale-up / Scale-out topology

完成条件：

- 每个概念都有输入、约束、输出和边界。
- Model / System / Chip 三域存在真实跨域路径。
- 所有新增 Wiki Link 可解析。
- Validator 和 knowledge graph 构建通过。

## Phase 2：Serving / Training / MoE

完成：

- Serving
- P/D disaggregation
- KV transfer
- MoE
- distributed training
- reliability

完成条件：

能够从一个代表模型出发，解释其推理或训练 workload 如何映射到内存、计算、通信和拓扑约束。

## Phase 3：Hardware Expansion

按顺序扩展：

1. Memory / HBM
2. Scale-up interconnect
3. NIC / DPU / Scale-out network
4. PCIe / CXL
5. Storage
6. Packaging
7. Power / Cooling

## Phase 4：Executable Knowledge Base

建立自动派生：

```text
Model
+ Workload
+ Assumptions
        ↓
System Requirements
        ↓
Hardware Comparison
```

这一步完成后，仓库应从“资料库”进一步升级为可验证、可计算的 AI Infra 知识模型。

---

# 验收原则

任何阶段完成后至少执行：

```bash
python3 scripts/validate-chip.py --root .
python3 scripts/validate-repo.py --root .
python3 scripts/build-chip-catalog.py --root . --output generated
python3 scripts/build-knowledge-graph.py --root . --output generated
python3 scripts/enrich-knowledge-graph.py --generated generated
git diff --check
```

同时检查：

- unresolved Wiki Links
- isolated important nodes
- duplicate title / alias
- Evidence coverage
- Model → System → Chip 是否存在真实语义路径
- 是否意外复制了 relationship 仓库的 canonical 软件事实

---

# 实施任务入口

近期执行队列和全部 Task ID 统一见 [[TASKS|AI Infra Docs Implementation Tasks]]。每个任务开始、阻塞或完成时只更新该文件的状态，避免 Roadmap 与实际进度漂移。
