---
title: AI Infra Docs Implementation Tasks
aliases:
  - 实施任务清单
  - Implementation Tracker
tags:
  - tasks
  - roadmap
  - ai-infra
  - tracking
updated: 2026-10-05
---

# AI Infra Docs Implementation Tasks

本文件是 [[ROADMAP|AI Infra Docs Roadmap]] 的 **唯一实施进度源**。Roadmap 负责方向、边界和阶段目标；本文件负责具体任务、依赖、状态、交付物和验收条件。

## 状态规则

状态只使用以下四种：

- `TODO`：尚未开始。
- `DOING`：正在实施，同一任务原则上只允许一个主负责人。
- `BLOCKED`：已开始但被外部依赖或证据缺口阻塞，必须写明原因。
- `DONE`：交付物已经进入仓库，并满足该任务的验收条件。

进度更新规则：

1. 开始任务时，在同一个提交或 PR 中把状态从 `TODO` 改为 `DOING`。
2. 任务完成时，必须先运行该任务的验收检查，再把状态改为 `DONE`。
3. 若有 GitHub Issue / PR，在“跟踪”列填写链接；没有则保持 `-`。
4. 不因为“文档已创建”就标记完成；交付物、Evidence、内部链接和 Validator 必须同时满足要求。
5. 新增任务必须使用稳定 Task ID，不重排旧 ID。
6. 每次完成一批任务后更新本页的阶段统计。

## 总体进度

| 阶段 | 完成 | 总数 | 状态 |
|---|---:|---:|---|
| Phase 0：Foundation / Schema | 3 | 3 | DONE |
| Phase 1：System Foundation | 29 | 29 | DONE |
| Phase 2：Serving / MoE / Training / Reliability | 13 | 13 | DONE |
| Phase 3：Model / Hardware Expansion | 9 | 9 | DONE |
| Phase 4：Executable Knowledge Base | 5 | 5 | DONE |
| Phase 5：Interconnect / Optical Expansion | 6 | 6 | DONE |
| Phase 6：Fabric Performance & Optical I/O Deep Dive | 2 | 6 | IN PROGRESS |
| **合计** | **67** | **71** | **IN PROGRESS** |

---

# Phase 0：Foundation / Schema

| ID | 状态 | 任务 | 依赖 | 交付物 | 验收条件 | 跟踪 |
|---|---|---|---|---|---|---|
| FND-001 | DONE | 定义 System Schema V0.1 | - | `system/SCHEMA.md` | 明确 inputs / constraints / outputs / assumptions / related_layers / evidence；示例可被 Validator 消费 | - |
| FND-002 | DONE | 扩展仓库 Validator 支持 System Schema | FND-001 | `scripts/validate-repo.py` | 能校验 system concept 必填字段、日期、Evidence、内部链接；现有仓库验证通过 | - |
| FND-003 | DONE | 重构 System MOC | FND-001 | `system/README.md` | 能导航到 Workload / Compute / Memory / Parallelism / Communication / Topology 等主域；无孤立核心节点 | - |

---

# Phase 1：System Foundation

## Workload

| ID | 状态 | 任务 | 依赖 | 交付物 | 验收条件 | 跟踪 |
|---|---|---|---|---|---|---|
| WL-001 | DONE | 建立 AI Workload 总模型 | FND-001 | `system/workload/ai-workload-model.md` | 定义 Model facts 与 runtime workload 的边界；覆盖 prompt/output/batch/concurrency/SLA；包含输入输出和假设 | - |
| WL-002 | DONE | 建立 Inference Workload | WL-001 | `system/workload/inference-workload.md` | 覆盖 online/offline、TTFT、TPOT、吞吐、并发、prefix reuse；能链接 Serving 专题 | - |
| WL-003 | DONE | 建立 Training Workload | WL-001 | `system/workload/training-workload.md` | 覆盖 global/micro batch、sequence、gradient accumulation、checkpoint interval | - |

## Compute

| ID | 状态 | 任务 | 依赖 | 交付物 | 验收条件 | 跟踪 |
|---|---|---|---|---|---|---|
| CMP-001 | DONE | Transformer Compute Model | WL-001 | `system/compute/transformer-compute-model.md` | 区分 dense/MoE；给出 Prefill/Decode 主要 FLOPs 构成及公式边界 | - |
| CMP-002 | DONE | Roofline 与 Arithmetic Intensity | CMP-001 | `system/compute/roofline-and-arithmetic-intensity.md` | 明确 compute-bound / memory-bound 判断；区分峰值、理论上界、系统上界、实测 | - |
| CMP-003 | DONE | Prefill vs Decode 计算模型 | CMP-001, MEM-005 | `system/compute/prefill-vs-decode.md` | 解释 GEMM/GEMV、权重读取、KV 访问和 batch 对瓶颈的影响 | - |

## Memory

| ID | 状态 | 任务 | 依赖 | 交付物 | 验收条件 | 跟踪 |
|---|---|---|---|---|---|---|
| MEM-001 | DONE | 完整 Model Memory Accounting | WL-001 | `system/memory/model-memory-accounting.md` | 统一 weights + KV + activation + workspace + comm buffer + fragmentation + reserve 口径 | - |
| MEM-002 | DONE | Weight Memory Model | MEM-001 | `system/memory/weight-memory.md` | 覆盖 dtype/quantization/sharding；不把 runtime buffer 混入权重 | - |
| MEM-003 | DONE | Activation Memory Model | MEM-001 | `system/memory/activation-memory.md` | 区分推理/训练 activation；说明 recomputation/checkpointing 影响 | - |
| MEM-004 | DONE | KV Cache Model | MEM-001 | `system/memory/kv-cache-model.md` | 统一 MHA/GQA/MLA 等计算口径；和现有 KV hierarchy 双向关联 | - |
| MEM-005 | DONE | Memory Bandwidth Model | MEM-001 | `system/memory/memory-bandwidth-model.md` | 建立 bytes/token、bytes/step 与带宽下界；说明有效带宽与标称带宽区别 | - |
| MEM-006 | DONE | CXL / Memory Pooling 系统模型 | MEM-001, TOP-001 | `system/memory/cxl-and-memory-pooling.md` | 明确 capacity/latency/bandwidth/failure-domain 交换；不把 CXL 当作 HBM 等价层 | - |

## Parallelism

| ID | 状态 | 任务 | 依赖 | 交付物 | 验收条件 | 跟踪 |
|---|---|---|---|---|---|---|
| PAR-001 | DONE | Parallelism Overview | WL-001 | `system/parallelism/parallelism-overview.md` | 统一 DP/TP/PP/EP/CP 的目的、切分对象、通信与拓扑要求 | - |
| PAR-002 | DONE | Tensor Parallelism | PAR-001, COM-001 | `system/parallelism/tensor-parallelism.md` | 给出主要 collective 与通信量关系；链接 Scale-up topology | - |
| PAR-003 | DONE | Pipeline Parallelism | PAR-001, COM-004 | `system/parallelism/pipeline-parallelism.md` | 覆盖 stage、bubble、microbatch、P2P 边界 | - |
| PAR-004 | DONE | Expert Parallelism | PAR-001, COM-003 | `system/parallelism/expert-parallelism.md` | 说明 token dispatch、all-to-all、负载不均衡和 placement | - |
| PAR-005 | DONE | Data Parallelism | PAR-001, COM-002 | `system/parallelism/data-parallelism.md` | 覆盖 gradient synchronization、replication 和通信成本 | - |
| PAR-006 | DONE | Context Parallelism | PAR-001, COM-001 | `system/parallelism/context-parallelism.md` | 说明长上下文切分、KV/attention 通信与拓扑敏感度 | - |

## Communication

| ID | 状态 | 任务 | 依赖 | 交付物 | 验收条件 | 跟踪 |
|---|---|---|---|---|---|---|
| COM-001 | DONE | Collective Communication Overview | WL-001 | `system/communication/collective-communication.md` | 定义 participant/message/algorithm/bandwidth/latency 模型 | - |
| COM-002 | DONE | All-Reduce / All-Gather / Reduce-Scatter | COM-001 | `system/communication/all-reduce-all-gather-reduce-scatter.md` | 给出典型 ring/tree 成本边界；关联 TP/DP | - |
| COM-003 | DONE | All-to-All | COM-001 | `system/communication/all-to-all.md` | 给出 MoE token dispatch 的数据量和拓扑敏感度 | - |
| COM-004 | DONE | Point-to-Point | COM-001 | `system/communication/point-to-point.md` | 覆盖 PP、KV transfer、跨节点 P2P | - |
| COM-005 | DONE | Communication Cost Model | COM-001, TOP-001 | `system/communication/communication-cost-model.md` | 建立 latency + serialization + transfer + synchronization 统一模型 | - |

## Topology

| ID | 状态 | 任务 | 依赖 | 交付物 | 验收条件 | 跟踪 |
|---|---|---|---|---|---|---|
| TOP-001 | DONE | Scale-up vs Scale-out | WL-001 | `system/topology/scale-up-vs-scale-out.md` | 定义两类 fabric 的边界、带宽/时延/规模/故障域；关联硬件对象 | - |
| TOP-002 | DONE | Accelerator Fabric | TOP-001 | `system/topology/accelerator-fabric.md` | 描述 accelerator↔accelerator fabric 的系统作用，不复制厂商产品页 | - |
| TOP-003 | DONE | GPU/NPU ↔ NIC Affinity | TOP-001 | `system/topology/gpu-nic-affinity.md` | 覆盖 PCIe switch、NUMA、rail、NIC locality 对通信的影响 | - |
| TOP-004 | DONE | NUMA / PCIe Topology | TOP-001 | `system/topology/numa-and-pcie-topology.md` | 建立 CPU/accelerator/NIC/PCIe switch 的 placement 约束 | - |
| TOP-005 | DONE | Rack / Failure Domain | TOP-001 | `system/topology/rack-and-failure-domain.md` | 把 rack、rail、switch、power failure domain 纳入调度模型 | - |

## Integration

| ID | 状态 | 任务 | 依赖 | 交付物 | 验收条件 | 跟踪 |
|---|---|---|---|---|---|---|
| INT-001 | DONE | 手工端到端 Model → System → Hardware 案例 | CMP-001, CMP-002, MEM-001, MEM-005, COM-005, PAR-001, TOP-001 | `system/examples/model-to-hardware-walkthrough.md` | 选择一个 Evidence 完整的代表模型和明确 workload；逐步展示 compute/memory/communication/topology 推导；每个数字可追溯到输入与公式；未知项不强行估算 | - |

---

# Phase 2：Serving / MoE / Training / Reliability

## Serving

| ID | 状态 | 任务 | 依赖 | 交付物 | 验收条件 | 跟踪 |
|---|---|---|---|---|---|---|
| SRV-001 | DONE | LLM Serving Model | WL-002, CMP-003, MEM-001 | `system/serving/llm-serving-model.md` | 能把请求负载映射到 compute/memory/communication | - |
| SRV-002 | DONE | Continuous Batching | SRV-001 | `system/serving/continuous-batching.md` | 解释 batch 动态变化对利用率、KV 和 latency 的影响 | - |
| SRV-003 | DONE | Prefix Caching | SRV-001, MEM-004 | `system/serving/prefix-caching.md` | 明确 hit rate、节省 Prefill、缓存容量和失效语义 | - |
| SRV-004 | DONE | Disaggregated Prefill / Decode | SRV-001, COM-004, TOP-001 | `system/serving/disaggregated-prefill-decode.md` | 给出拆分收益条件和网络/KV transfer 代价 | - |
| SRV-005 | DONE | KV Transfer | SRV-004, MEM-004 | `system/serving/kv-transfer.md` | 建立 transfer vs recompute break-even 模型 | - |

## MoE

| ID | 状态 | 任务 | 依赖 | 交付物 | 验收条件 | 跟踪 |
|---|---|---|---|---|---|---|
| MOE-001 | DONE | MoE System Model | CMP-001, PAR-004 | `system/moe/moe-system-model.md` | 从 active params、experts、top-k 推导 compute/memory/communication 约束 | - |
| MOE-002 | DONE | Expert Routing / Load Balance | MOE-001 | `system/moe/expert-routing-and-load-balance.md` | 覆盖 capacity factor、热点 expert、尾延迟和 placement | - |

## Training

| ID | 状态 | 任务 | 依赖 | 交付物 | 验收条件 | 跟踪 |
|---|---|---|---|---|---|---|
| TRN-001 | DONE | Distributed Training Model | WL-003, PAR-001 | `system/training/distributed-training-model.md` | 建立训练 compute/memory/communication 主线 | - |
| TRN-002 | DONE | Training Memory Model | TRN-001, MEM-001 | `system/training/training-memory-model.md` | 覆盖 parameters/gradients/optimizer/master weights/activations | - |
| TRN-003 | DONE | Gradient Synchronization | TRN-001, COM-002 | `system/training/gradient-synchronization.md` | 给出同步通信量与 overlap 边界 | - |

## Reliability / Power

| ID | 状态 | 任务 | 依赖 | 交付物 | 验收条件 | 跟踪 |
|---|---|---|---|---|---|---|
| REL-001 | DONE | Checkpoint / Recovery Model | TRN-001, TOP-005 | `system/reliability/checkpoint-recovery-model.md` | 关联 checkpoint size、storage BW、MTTR、failure domain | - |
| REL-002 | DONE | Accelerator / Network Failure Domain | TOP-005 | `system/reliability/accelerator-and-network-failure-domain.md` | 区分 device/node/rack/fabric 故障范围 | - |
| PWR-001 | DONE | Rack Power / Cooling Model | TOP-005 | `system/power/rack-power-and-cooling.md` | 从 device→node→rack 建立功耗密度与冷却约束 | - |

---

# Phase 3：Model / Hardware Expansion

## Model

| ID | 状态 | 任务 | 依赖 | 交付物 | 验收条件 | 跟踪 |
|---|---|---|---|---|---|---|
| MOD-001 | DONE | Model Schema V0.2 设计 | FND-001, MEM-004, CMP-001 | `models/SCHEMA.md` | 评估 layers/hidden/heads/kv_heads/head_dim/experts/top-k/MLA 等可验证字段；保持模型事实边界 | - |
| MOD-002 | DONE | 迁移现有模型到 V0.2 | MOD-001 | 现有 `models/*` 页面 | Validator 全通过；未知值保持 null；Evidence 可追溯 | - |
| MOD-003 | DONE | 建立 Architecture Anchors | MOD-001 | `models/00-model-index.md` + 代表模型页 | 至少覆盖 Dense/GQA/MLA/MoE/Linear-or-SSM/Multimodal 中有公开证据的代表模型 | - |

## Hardware

| ID | 状态 | 任务 | 依赖 | 交付物 | 验收条件 | 跟踪 |
|---|---|---|---|---|---|---|
| HW-001 | DONE | Memory / HBM 对象边界设计 | MEM-001 | Chip Schema 扩展说明或新增硬件对象 | 明确 HBM/DDR/CXL memory 的 object/layer/字段边界 | - |
| HW-002 | DONE | Scale-up Fabric 对象边界与首批对象 | TOP-001 | NVLink/NVSwitch/Infinity Fabric/UALink 等硬件事实页 | 每页直接 Evidence；不把系统聚合值回填单器件 | - |
| HW-003 | DONE | NIC / DPU / Scale-out Network 首批对象 | TOP-003 | ConnectX/Spectrum/InfiniBand/Broadcom 等事实页 | 可与 topology/communication 页面建立真实跨域边 | - |
| HW-004 | DONE | PCIe / CXL 组件首批对象 | MEM-006, TOP-004 | switch/retimer/memory-expander 页面 | 类型边界清晰；字段单位统一 | - |
| HW-005 | DONE | Storage / NVMe 首批对象 | REL-001, SRV-005 | AI Infra storage 事实页 | 包含 BW/latency/capacity/endurance/interface/power，区分厂商规格与分析 | - |
| HW-006 | DONE | Packaging / Power / Cooling 边界设计 | PWR-001 | 领域边界说明 + 首批代表对象 | 只覆盖直接影响 AI hardware capability 的封装/供电/冷却事实 | - |

---

# Phase 4：Executable Knowledge Base

| ID | 状态 | 任务 | 依赖 | 交付物 | 验收条件 | 跟踪 |
|---|---|---|---|---|---|---|
| EXE-001 | DONE | 定义 Workload Profile 数据格式 | WL-001, FND-001 | Schema / example profile | 能稳定表示 inference/training workload，单位明确 | - |
| EXE-002 | DONE | 构建 Workload Profile 生成器 | EXE-001 | `scripts/build-workload-profile.py` | 能从模型页 + workload 输入生成机器可读 profile | - |
| EXE-003 | DONE | 构建 System Requirements 生成器 | EXE-002, CMP-001, MEM-001, COM-005 | `scripts/build-system-requirements.py` | 输出 compute/memory/communication 派生值并保留公式、输入、假设、单位 | - |
| EXE-004 | DONE | 建立端到端代表模型案例 | EXE-003, MOD-002 | 一个完整 Model → Workload → System → Hardware 示例 | 任一派生数字可回溯到模型字段、公式和 Evidence | - |
| EXE-005 | DONE | 将派生结果接入知识图谱/CI | EXE-003 | CI + generated reports | 派生数据自动构建、不手工维护；失败会阻断 CI 或产生明确报告 | - |

---

# Phase 5：Interconnect / Optical Expansion

| ID | 状态 | 任务 | 依赖 | 交付物 | 验收条件 | 跟踪 |
|---|---|---|---|---|---|---|
| ICN-001 | DONE | 建立 Interconnect / Fabric / Optical I/O 专项 MOC 与对象边界 | HW-002, HW-003 | `chip/interconnect/README.md` + `chip/SCHEMA.md` | 明确 protocol/link、switch、CPO/NPO/LPO、system topology 边界；带宽 scope 不混写 | - |
| ICN-002 | DONE | 补齐首批 Scale-up interconnect 独立对象 | ICN-001 | NVLink 5 Switch、AMD Infinity Fabric、Google ICI、Huawei UnifiedBus 2.0 | 每页直接 Evidence；协议/代际与系统聚合值分离；关键字段有 evidence_map | - |
| ICN-003 | DONE | 补齐首批 Optical I/O 对象 | ICN-001 | Broadcom TH6-Davisson CPO、Huawei Hi-ONE NPO | CPO/NPO 不当协议；engine/link/switch capacity 分 scope；生命周期口径保守 | - |
| ICN-004 | DONE | 扩展 Huawei UnifiedBus 硬件生态 | ICN-002, ICN-003 | LinkBlade、LinkDevice、UBG/SF9300、CloudEngine XH9300 NPO 等事实页 | 协议、互联设备、optical engine、switch system 分页；只收官方公开规格 | - |
| ICN-005 | DONE | 扩展下一代与开放互联标准 | ICN-001 | NVLink 6 / NVLink 6 Switch、UEC / SUE、后续 UALink 等有直接证据的对象 | 不用 roadmap 数字冒充 GA；standard 与 silicon implementation 分离 | - |
| ICN-006 | DONE | 生成 Interconnect 横向比较与健康度视图 | ICN-002, ICN-003, EXE-005 | generator + generated interconnect comparison | 能按 lane/link/device/switch/domain 与 electrical/optical 维度比较；未知值保持 unknown | - |

---

# Phase 6：Fabric Performance & Optical I/O Deep Dive

| ID | 状态 | 任务 | 依赖 | 交付物 | 验收条件 | 跟踪 |
|---|---|---|---|---|---|---|
| FAB-001 | DONE | 建立 Fabric Effective Bandwidth / Latency 模型 | COM-005, TOP-002, ICN-006 | `system/communication/fabric-performance-model.md` | 区分 nominal/effective/observed；显式建模 protocol/utilization/contention；多 stage bottleneck 与 latency scope 不混写 | - |
| FAB-002 | DONE | 构建 executable Fabric Path Estimator | FAB-001, EXE-005 | `scripts/build-fabric-performance.py` + reference profile | 输入 path stages 后生成 nominal/effective bottleneck、serialization、fixed latency、P2P lower bound；未知输入保持 null | - |
| FAB-003 | TODO | 建立 Collective Efficiency 可执行模型 | FAB-001, FAB-002, COM-001 | collective algorithm profiles + estimator extension | Ring/Tree/All-to-All 等算法的 steps、critical-path bytes、effective BW 口径可追溯，不用固定经验效率 | - |
| FAB-004 | TODO | 建立 Fabric Failure / Retry / Degraded Topology 模型 | FAB-001, REL-002 | reliability model + degraded path cases | retry/recovery/reroute/partial-rack 分开；故障后重新计算 path，不用固定故障折扣 | - |
| OPT-001 | TODO | 建立 Optical I/O Power / Reach / Repairability 模型 | ICN-003, FAB-001 | optical system model | CPO/NPO/LPO/pluggable 分 packaging；power/reach/laser/DSP/repairability 有明确 scope | - |
| OPT-002 | TODO | 扩展代表 Optical I/O 实现并生成深度比较 | OPT-001, ICN-006 | hardware facts + generated comparison | 直接 Evidence；器件、engine、switch、system power/latency 不混写；未知值不推断 | - |

---

## 当前实施状态

截至 2026-10-05，Phase 0–5 的 65 个任务已全部完成。Phase 6 新增 6 个 Fabric Performance / Optical I/O 深化任务，当前已完成 FAB-001 / FAB-002；后续继续使用稳定 Task ID 追加，不复用或重排现有 ID。

Phase 4 已把知识库从“可读文档”推进到可重复执行链：

```text
Model V0.2 + Chip V0.2 + Workload Profile
→ normalized workload JSON
→ System Requirements JSON / derived Markdown
→ Validator
→ Knowledge Graph
→ Quartz / Graph Explorer
```

派生结果只计算有明确输入、公式与 assumption 的字段；未知值继续保留 unknown，不按 0 补齐。

# 首批执行队列（已完成）

按依赖关系，建议第一批严格按以下顺序推进：

1. `FND-001` System Schema V0.1
2. `FND-002` Validator 支持 System Schema
3. `FND-003` System MOC
4. `WL-001` AI Workload Model
5. `MEM-001` Model Memory Accounting
6. `CMP-001` Transformer Compute Model
7. `COM-001` Collective Communication
8. `PAR-001` Parallelism Overview
9. `TOP-001` Scale-up vs Scale-out
10. `MEM-005` Memory Bandwidth Model
11. `CMP-002` Roofline / Arithmetic Intensity
12. `COM-005` Communication Cost Model
13. `INT-001` 手工端到端案例，作为 Phase 1 的集成验收

以上队列与 Phase 2/3/4/5 均已完成。Phase 6 当前按 FAB-001 → FAB-002 → FAB-003/FAB-004 → OPT-001 → OPT-002 推进。本节保留作为实施顺序记录。

## 每批完成后的统一验收

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
- TASKS 状态是否与实际仓库一致
- 是否意外复制了 `ai_infra_relationship` 的 canonical 软件事实
