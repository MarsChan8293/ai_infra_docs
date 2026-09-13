# DeepSeek V4.1 Flash：面向新架构的 AI Infra 系统设计

> 目标：不把 DeepSeek V4.1 Flash 当作“又一个更大的 MoE 模型”来部署，而是利用其 CED、CSA2、Engram、DSpark 等结构特性，重新划分 **计算权重、神经内存、可迁移上下文状态**，形成一套更适合 Agent、长上下文和异构硬件的推理基础设施。

## 1. 核心判断

DeepSeek V4.1 Flash 值得关注的并不是单一模型参数规模，而是它改变了传统 serving 的几个默认假设：

- 模型采用 Causal Encoder-Decoder（CED）式结构，长 Prompt 的 Prefill 与 Decode 不再必须走完全相同的计算路径。
- CSA2 将 KV / Indexer 相关状态进一步压缩并跨层复用，使长上下文状态迁移的成本显著下降。
- SWA 的局部状态具备 bounded replay 的可能性，因此“完整逐层 KV 全量迁移”不再是唯一方案。
- Engram 将相当大一部分模型能力变成稀疏 n-gram memory lookup，更接近“神经内存”而不是传统 GEMM 权重。
- DSpark 的 speculative generation 不只可以用于减少 Decode 步数，还可以被进一步利用为内存访问预取信号。

因此，可以把 V4.1 Flash 的推理资源拆成三类：

1. **Compute Weights**：Attention / Dense / MoE 等真正需要高带宽矩阵计算的权重。
2. **Neural Memory**：Engram 等稀疏查表型大容量参数。
3. **Context State**：压缩 KV、Indexer 状态、尾部 replay 所需 token / hidden state 等会话状态。

系统竞争力应围绕这三类资源分别放置、分别调度，而不是全部塞进 GPU HBM。

---

## 2. 总体方案：TokenBox Context Fabric

传统推理服务通常是：

```text
Request
   |
   v
GPU Instance
   |
Prefill
   |
KV Cache
   |
Decode
```

建议改造成：

```text
                    Agent / Client
                         |
                 Context Capsule API
                         |
            +------------+------------+
            |                         |
       Context Hit                Context Miss
            |                         |
            v                         v
       D-only Path                Thin-P Pool
                                   Encoder-heavy
            |                         |
            +------------+------------+
                         |
                         v
                  Context Fabric
          +--------------+--------------+
          |              |              |
      GPU HBM Cache    CPU DDR/CXL     NVMe
          |              |              |
          |          Engram Pool        |
          |              |              |
          +--------------+--------------+
                         |
                         v
                    Decode Pool
                    Full Model
                         |
                    Tail Replay
                         |
                       DSpark
                         |
                       Output
```

整个系统可以概括为：

> **把 DeepSeek V4.1 Flash 拆成计算、神经内存、上下文状态三种资源，并围绕“可迁移状态”进行调度。**

---

## 3. 方案一：Context Capsule

### 3.1 从 KV Cache 升级为“可执行上下文”

传统 KV Cache 通常是某个推理引擎内部的显存对象：

```text
Request -> GPU Worker -> Engine-owned KV pages
```

建议定义独立于 vLLM / SGLang / MindIE worker 的 Context Capsule：

```text
Context Capsule
├── Global compressed KV
├── Index K / sparse-attention metadata
├── compression / RoPE / position metadata
├── tail tokens or replay state
├── model / tokenizer / quantization version
├── prefix DAG parent
└── integrity / ownership metadata
```

它的目标是：

- 可从 P 节点迁移到 D 节点
- 可从 GPU HBM 下沉到 CPU / CXL / NVMe
- 可由客户端或独立 Context Service 持有
- 可 checkpoint / resume
- 可跨 worker 迁移
- 可 fork 给多个 Agent
- 可按 prefix 做 copy-on-write

也就是说，把 KV Cache 从“GPU 内存块”升级为一种 **Agent Execution State**。

### 3.2 Forkable Context

Agent workload 天生具有 prefix tree 结构：

```text
System Prompt + Repo Context
            |
            +------ Agent A
            |
            +------ Agent B
            |
            +------ Agent C
```

因此 Context Store 应采用 immutable pages + hash + copy-on-write：

```text
Context Root
   |
   +-- Page A
   +-- Page B
   +-- Page C
        |
        +-- Agent-1 delta
        +-- Agent-2 delta
        +-- Agent-3 delta
```

建议暴露类似文件系统/进程语义的 API：

```text
checkpoint()
resume()
fork()
pin()
evict()
migrate()
merge_prefix()
```

这比单纯的 KV offload 更接近一个“上下文操作系统”。

---

## 4. Context Fabric：让 10/25/100GbE 都有明确角色

公开资料显示 V4.1 Flash 的全局上下文状态相比传统逐层 KV 已明显收缩。以约 **890 B/token** 的 global KV 量级作为工程估算：

| Context Length | Global KV 估算 | 10GbE 纯链路理论时间 |
|---:|---:|---:|
| 64K | ~55.6 MiB | ~47 ms |
| 128K | ~111.3 MiB | ~93 ms |
| 1M | ~890 MiB | ~747 ms |

> 注：实际时间还会叠加协议开销、序列化、内存拷贝、NIC/GPU DMA、拥塞和并发争用。表格仅用于判断数量级。

这带来一个重要变化：

- V3/V4 时代，大上下文 KV roaming 往往需要非常激进的网络配置。
- V4.1 Flash 下，64K / 128K Context Capsule 已有机会在普通 10/25GbE 网络中做 session migration。
- 100/200GbE 则可以服务于高并发 Context Fabric，而不只是 GPU collective。

建议将网络分层：

```text
GPU collective fabric : NVLink / HCCS / RoCE
Context fabric        : 25/100/200GbE RoCE/TCP
Cold context          : Ethernet + NVMe object store
```

而不是默认所有 KV 都必须走最昂贵的 GPU fabric。

---

## 5. 方案二：Thin-P / Full-D

这是最值得优先验证的 V4.1-native P/D 方案。

### 5.1 传统 P/D 的问题

主流 P/D Disaggregation 通常仍然是：

```text
Full Model P
      |
      | KV transfer
      v
Full Model D
```

P 和 D 都复制完整或接近完整模型权重。

这解决了计算阶段隔离，但没有充分利用 V4.1 Flash 的 CED 结构。

### 5.2 新思路

尝试让 Prefill 节点只加载 Prefill 真正需要的部分：

```text
Long Prompt
    |
    v
+-------------------------+
| Thin Prefill Node       |
|                         |
| Causal Encoder          |
| Global KV projector     |
| CSA2/index state        |
|                         |
| 尽量不加载完整 Decoder  |
+------------+------------+
             |
       Context Capsule
             |
             v
+-------------------------+
| Full Decode Node        |
|                         |
| Full model              |
| Restore global state    |
| Replay bounded tail     |
| DSpark Decode           |
+-------------------------+
```

关键研究假设是：

> **将 upper-layer local/SWA state 的 bounded replay 从 P 节点移动到 D 节点。**

如果成立，P 节点不再需要完整复制 Decoder 侧大部分 MoE 权重。

### 5.3 为什么有竞争力

传统：

```text
完整模型 P + 完整模型 D
```

目标：

```text
半模型/轻模型 P + 完整模型 D
```

潜在收益：

- Prefill 节点显存需求下降
- Prefill 节点可以采用更便宜、更偏算力型的硬件
- D 节点数量可独立扩展
- 长 Prompt workload 的硬件成本下降
- P 节点启动 / 权重加载更快
- 更适合 DGX Spark / RTX Pro / 昇腾等异构节点组合

### 5.4 必须验证的风险

Thin-P 目前应视为 **研究方案**，而不是现成引擎能力。需要重点验证：

1. Decoder 侧哪些状态可以从 encoder output / global state 重建。
2. replay 需要传 token、hidden state 还是额外中间状态。
3. bounded replay 对 TTFT 的增量是多少。
4. replay 是否导致 D 首 token latency 抬升过多。
5. P 权重裁剪后，实际 HBM 节省是否足够大。
6. 当前 vLLM/SGLang/MindIE 模型实现是否允许拆权重加载。

---

## 6. 方案三：Engram Memory Fabric

### 6.1 Engram 不应和 GEMM 权重同等对待

Engram 的本质更像：

```text
token n-gram
    |
   hash
    |
large embedding table lookup
    |
small vector
```

而不是：

```text
activation x large weight matrix
```

因此把全部 Engram 长驻昂贵 HBM 并不是唯一合理设计。

建议做成三级结构：

```text
GPU HBM
├── Dense / Attention weights
├── Hot MoE experts
├── Hot Engram rows
└── Active Context

CPU DDR / CXL Memory
├── Full Engram table
├── Cold experts
└── Warm Context Capsules

NVMe
├── Cold Context
└── model / expert backing store
```

### 6.2 HBM Engram Row Cache

维护 GPU-side hot row cache：

```text
Engram Request
      |
      +-- hit  -> HBM
      |
      +-- miss -> DDR/CXL -> HBM fill
```

Cache key 不是 token，而是 n-gram hash / row ID。

可以采用：

- LFU + recency hybrid
- per-tenant hotset
- prompt-domain-aware cache
- prefix-aware prefetch
- GPU cooperative gather

### 6.3 Prefill Bulk Prefetch

Prefill 阶段整个 Prompt token 序列是已知的。

因此可以在计算真正到达 Engram layer 之前，就提前计算未来 token 的 n-gram row ID，并批量从 DDR/CXL 预取：

```text
Prompt tokenizer
      |
      +--> n-gram hash planner
                |
                +--> async gather from DDR/CXL
                |
GPU compute ------------------------>
```

这比被动 cache miss 更适合高吞吐 Prefill。

### 6.4 DSpark + Speculative Engram Prefetch

更有创意的一点是：

```text
DSpark predicts t+1 ... t+k
             |
             +--> speculative verification
             |
             +--> speculative Engram row prefetch
```

即：

> speculative decode 同时作为 speculative memory prefetch。

即使 draft token 最终未全部接受，错误预取的代价主要是带宽和 cache pollution，而不是 correctness。

这有机会把 Decode 期间的随机内存延迟进一步隐藏在计算后面。

---

## 7. 方案四：Sparse Context Engine

V4.1 Flash 的 sparse attention / indexer 路径适合从纯软件优化进一步演化为专用数据通路。

目标不是做一个泛化的“Top-K accelerator”，而是融合：

```text
FP4 / compressed Index K
          |
          v
       Q x K
          |
          v
   block reduction
          |
          v
 hierarchical Top-K
          |
          v
       KV gather
          |
          v
   sparse attention
```

关键原则：

> **Indexer -> Top-K -> KV gather -> Sparse Attention 中间结果尽量不落 HBM。**

### 7.1 软件阶段

先在 CUDA / Triton / Ascend C 上做：

- fused index score + Top-K
- hierarchical block candidate filtering
- Top-K result directly driving KV gather
- gather + attention fusion
- candidate / index-K SRAM-friendly layout
- persistent kernel

### 7.2 芯片阶段

可以演进成专用 Context Engine：

```text
             +------------------+
Index K ---> |                  |
Query ------>| Sparse Context   |----> attention output
KV --------->| Engine           |
             |                  |
             | SRAM candidate   |
             | SRAM hot KV      |
             | top-k network    |
             +------------------+
```

它与传统 Tensor Core 的定位不同：

- Tensor Core：大矩阵规则计算
- Context Engine：稀疏索引、筛选、gather、局部 attention 数据流

这与此前讨论的“针对 indexer / sparse lookup 做推理专用硬件”的方向高度一致。

---

## 8. RTX Pro 5000 / TokenBox 的建议形态

对于多张 72GB 级 RTX Pro GPU，不建议默认采用：

```text
16 GPU -> TP16 -> 1 giant instance
```

更值得验证的是服务分工：

```text
+-------------------+       +-------------------+
| Thin-P Group A    |       | Full-D Group A    |
+-------------------+       +-------------------+

+-------------------+       +-------------------+
| Thin-P Group B    |       | Full-D Group B    |
+-------------------+       +-------------------+
          \                       /
           \                     /
            +-------------------+
            | Context Fabric    |
            +-------------------+
                     |
            +-------------------+
            | CPU DDR / CXL     |
            | Engram + Context  |
            +-------------------+
```

设计目标：

- GPU HBM 优先留给真正高带宽计算权重和 active working set
- Engram 尽量下沉 CPU DDR / CXL
- Context Capsule 可在 worker 间快速移动
- P/D worker 按 workload 动态调整数量
- Agent 长会话优先复用 Context，而不是重复 Prefill

---

## 9. DGX Spark 的角色

DGX Spark 更适合作为实验型 / 边缘型 Prefill 与 Context 节点，而不是盲目承担完整高吞吐 Decode。

可以优先验证：

```text
DGX Spark Pool
    |
    +-- Thin Prefill
    +-- Context preprocessing
    +-- Engram/DDR experiments
    +-- Context Capsule generation
    |
100GbE / RoCE
    |
High-throughput Decode Pool
```

如果 Thin-P 成立，DGX Spark 的价值会明显提升，因为它不必承担完整模型常驻的压力。

---

## 10. 昇腾场景

在昇腾 910B/910C/后续平台上，建议重点映射四类能力：

1. **P/D 解耦**：利用 HCCS / RoCE 做 Context Capsule 传输。
2. **CPU/Host Engram**：验证 Host DDR -> NPU 的 lookup / gather latency。
3. **Indexer fusion**：重点减少 Vector/Cube 与 HBM 之间往返。
4. **Context Engine 原型**：利用片上 UB/L2 做 candidate、index K、hot KV 暂存。

对于 TPOT 优化，V4.1 上不应只盯 GEMM。随机 gather、Indexer、Top-K、Engram lookup 与数据搬运可能成为新的关键路径。

---

## 11. Context-aware Scheduler

传统调度器主要看：

```text
GPU utilization
queue length
batch size
memory available
```

V4.1-native 调度器应该额外知道：

```text
context_location
context_size
prefix_share_ratio
engram_hotset
P/D affinity
network_transfer_cost
replay_cost
```

路由策略可以变成三条：

```text
Cold + Long Input
    -> Thin-P
    -> Context Capsule
    -> Full-D

Warm Context + Tiny Delta
    -> D-only micro-prefill
    -> Decode

Warm Context + Large Delta
    -> incremental Thin-P
    -> D
```

这尤其适合 Coding Agent / Tool Agent：

```text
Huge history + small observation + short generation
```

可以把“是否已有 context”提升到和 GPU 利用率同样重要的调度变量。

---

## 12. 产品护城河

单项功能本身都可能被主流推理框架逐步吸收，因此真正的竞争力应来自组合：

### 12.1 Context Capsule

统一 portable context state 格式和生命周期。

### 12.2 Context Fabric

HBM / DDR / CXL / NVMe / Network 的分层上下文存储。

### 12.3 Thin-P / Full-D

利用模型结构做非对称权重部署，而不只是传统同构 P/D。

### 12.4 Engram Memory Fabric

将巨型稀疏 lookup table 从 GPU HBM 中剥离，并通过预测预取隐藏随机访问延迟。

### 12.5 Sparse Context Engine

把 indexer、Top-K、KV gather、sparse attention 从软件 kernel 进一步压成统一数据流。

最终形成：

```text
                TokenBox Runtime
                       |
      +----------------+----------------+
      |                |                |
 Context OS      Neural Memory      Compute Plane
      |                |                |
 Capsule          Engram Fabric      P / D / MoE
 Fork             DDR / CXL          GPU / NPU
 Migrate          HBM Cache          Scheduler
 Checkpoint       Prefetch           Context Engine
```

---

## 13. 实施优先级

### P0：Context Capsule PoC

先不改模型计算。

目标：

- 导出 / 导入 Context
- worker A -> worker B migration
- GPU -> CPU -> GPU restore
- context hash + prefix dedup
- checkpoint / resume

指标：

- 64K / 128K context serialization time
- 网络迁移时间
- restore latency
- correctness
- GPU HBM 节省

### P1：Forkable Context Store

实现：

- immutable pages
- prefix DAG
- copy-on-write
- reference count
- TTL / eviction
- multi-agent fork

重点 workload：Coding Agent。

### P2：Engram Offload + Hot Row Cache

验证：

- Full Engram in CPU DDR
- GPU hot-row cache
- Prefill bulk prefetch
- cache hit rate
- PCIe bandwidth
- lookup latency

### P3：DSpark Speculative Engram Prefetch

验证 draft token 是否能足够提前产生 Engram row ID，并量化错误预取成本。

### P4：Thin-P / Full-D

这是系统级关键实验。

验证：

- P 节点最小权重集合
- Capsule 最小状态集合
- D 侧 replay 时间
- TTFT / TPOT
- P 节点显存节省
- 同吞吐下系统成本变化

### P5：Sparse Context Engine

先做 fused kernel，再决定是否值得沉淀成芯片 IP。

---

## 14. 最关键的实验矩阵

| 实验 | Baseline | Proposed | 主要指标 |
|---|---|---|---|
| Context transfer | full KV / engine KV | Capsule | size / latency |
| Session resume | re-prefill | restore Capsule | TTFT |
| Multi-agent fork | duplicated KV | prefix COW | memory |
| Prefill | full-model P | Thin-P | HBM / TTFT |
| Engram | GPU resident | CPU/CXL + HBM cache | TPOT / hit rate |
| Engram prefetch | demand lookup | bulk/speculative prefetch | stall time |
| Sparse attention | separate kernels | fused context pipeline | TPOT / HBM BW |
| Scheduling | load-only | context-aware | tail latency / cost |

---

## 15. 需要严格区分的“已知事实”和“研发假设”

### 已知 / 可从公开实现验证

- V4.1 Flash 引入 CED / CSA2 / Engram / DSpark 等新结构。
- Engram 是 n-gram hash lookup 型大表结构，具有与普通 GEMM 权重不同的访问模式。
- Context/KV 的结构比传统逐层完整 KV 更适合做压缩、复用与迁移。
- P/D disaggregation、KV offload、CPU offload 等机制在主流推理框架中已有基础能力可复用。

### 本方案提出、必须 PoC 验证

- Thin-P 可以裁掉多少 Decoder 权重。
- bounded replay 是否可以完全移动到 D。
- Context Capsule 的最小充分状态集合。
- 10/25GbE 在真实并发下是否足以支撑目标 session migration SLA。
- Engram DDR/CXL + HBM cache 是否能做到接近全 HBM 的 TPOT。
- DSpark draft 是否能稳定提供足够高价值的 Engram speculative prefetch。
- Indexer + Top-K + KV gather + attention 跨算子融合的真实收益。

这部分应始终作为研发假设管理，避免架构设计滑向“论文结构看起来可行 = 工程上已经成立”。

---

## 16. 一句话产品定义

> **TokenBox 不把 DeepSeek V4.1 Flash 当成一个 500GB 级模型来运行，而是把它拆成计算权重、神经内存和可迁移上下文三类资源分别调度。**

如果 Context Capsule + Thin-P + Engram Memory Fabric 三项同时成立，系统的竞争维度将从“单卡 tokens/s”上升到：

- 每个活跃 Agent 的 HBM 成本
- 长会话恢复时间
- Context 迁移成本
- 多 Agent prefix 复用率
- Prefill / Decode 资源利用率
- 神经内存的分层命中率
- 单位硬件成本的 Agent 并发量

这更接近下一代 Agent Infra 的核心指标。

---

## 17. 参考资料

- DeepSeek V4.1 Flash model repository / README: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
- DeepSeek V4.1 Flash config: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/config.json
- vLLM DeepSeek V4.1 Flash recipe: https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4.1-Flash
- DSpark paper: https://arxiv.org/abs/2607.05147

> 本文中的 TokenBox Context Fabric、Context Capsule、Thin-P / Full-D、Engram Memory Fabric、Forkable Context、Sparse Context Engine 为面向 V4.1 Flash 的系统设计提案，部分能力需要通过 PoC 进一步验证。