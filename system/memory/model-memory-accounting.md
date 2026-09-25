---
schema_version: system-v0.1
name: Model Memory Accounting
object_type: concept
category: memory-accounting
inputs:
  - model.parameters
  - model.architecture
  - workload.sequence_length
  - workload.batch_size
  - workload.concurrency
  - workload.parallelism
  - runtime.workspace
  - runtime.allocator
  - hardware.memory.capacity
constraints:
  - memory-capacity
  - allocator-fragmentation
  - runtime-reserve
  - communication-buffer-capacity
  - memory-tier-residency
outputs:
  - weight_resident_bytes
  - kv_resident_bytes
  - activation_peak_bytes
  - workspace_peak_bytes
  - communication_buffer_peak_bytes
  - peak_device_resident_bytes
  - memory_headroom_bytes
assumptions:
  - 所有内存量必须绑定 scope，不能把 per-device、per-node 与 global 数值直接相加
  - 未知项保持未知，不能按零处理以制造可部署结论
  - Offload 后的逻辑状态大小与设备侧峰值驻留大小分开计算
related_layers:
  - model
  - workload
  - memory
  - parallelism
  - communication
  - topology
  - accelerator
evidence: {}
updated: 2026-09-25
tags:
  - system
  - memory
  - accounting
---
# Model Memory Accounting

> “模型需要多少显存”不是一个单值问题。AI workload 的内存必须区分 **逻辑状态总量、某一时刻的峰值驻留、每设备分片、复制副本和不同 memory tier**，否则很容易把彼此不同 scope 的数字加在一起。

## 输入

Memory Accounting 消费两类输入：

- 模型固有事实：参数量、attention / MoE 结构、层数与后续 Model Schema 能提供的架构字段；
- [[system/workload/ai-workload-model|Workload]]：实际序列长度、batch、并发、推理/训练角色和并行条件。

硬件容量只用于最后的 feasibility 判断，不用于反推未知模型字段。

## 第一条规则：所有字节数都必须有 Scope

至少区分：

| Scope | 示例 |
|---|---|
| logical model | 模型全部权重的逻辑 payload |
| per accelerator | 某一 GPU/NPU 当前实际驻留 |
| parallel group | 一个 TP / EP / PP group 合计 |
| replica | 一个服务或训练 replica |
| node | 单服务器合计 |
| cluster | 整个 job / deployment 合计 |
| memory tier | HBM、Host DRAM、CXL/remote memory、NVMe 分别统计 |

**不同 scope 的数字不能直接相加。**

例如“模型权重总大小”与“单卡 KV Cache 驻留量”不属于同一 scope；除非先把权重经过明确的 TP/EP/PP 分片规则转换成 per-device resident bytes。

## 设备侧峰值内存

对于某个 accelerator，在明确执行阶段和 workload 下，可以使用以下统一骨架：

```text
peak_device_resident_bytes
=
  weight_resident_bytes
+ kv_resident_bytes
+ activation_peak_bytes
+ workspace_peak_bytes
+ communication_buffer_peak_bytes
+ allocator_overhead_bytes
+ runtime_reserve_bytes
```

这里的“+”只允许用于：

1. 同一设备；
2. 同一时间窗口或已经证明可能同时达到峰值；
3. 同一字节定义。

若两个 buffer 生命周期互斥，简单相加会高估峰值；若生命周期未知，则应保守说明“上界估算”，而不是假装得到精确峰值。

## Weight

权重内存首先区分逻辑 payload 与设备驻留。

概念下界：

```text
weight_payload_bytes
≈ stored_parameter_count
× bytes_per_stored_element
+ quantization_metadata_bytes
```

但 per-device resident weight 还取决于：

- Tensor Parallel 分片；
- Pipeline Parallel 层切分；
- Expert Parallel 的 expert placement；
- replicated layers / shared experts；
- embedding / output head 是否复制或切分；
- 量化 scale、zero point、packing metadata；
- runtime 是否保留转换后的第二份权重。

因此不能简单使用：

```text
total_parameters × dtype_bytes ÷ gpu_count
```

作为任意并行方案的准确单卡显存。

后续 `MEM-002` 将单独定义 Weight Memory Model。

## KV Cache

KV 是随 active sequence、上下文长度和 attention cache layout 变化的状态。

概念上：

```text
kv_resident_bytes
=
sum(active_sequence_cache_bytes_on_this_device)
```

它依赖：

- MHA / GQA / MLA 等 cache layout；
- 实际 sequence length，而不是模型最大 context；
- batch / concurrency；
- TP / CP 等分片策略；
- prefix reuse；
- block/page allocator；
- 是否存在 Host / Remote / SSD offload。

[[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层级]] 负责“放在哪里以及何时迁移”；后续 `MEM-004` 负责 KV 大小公式。

## Activation

Activation 是执行过程中的临时状态，不应与 KV 混为一谈。

其峰值依赖：

- Prefill 或 Decode；
- batch 和 sequence；
- layer execution schedule；
- attention implementation；
- fusion / recomputation；
- Pipeline stage；
- 训练时的 activation checkpointing。

因此 Activation 应记录 **peak live bytes**，而不是把每层产生过的 tensor 历史总和全部累加。

后续 `MEM-003` 将细化 Activation Memory Model。

## Workspace

Workspace 包括算子或 runtime 为执行临时申请的内存，例如：

- GEMM / attention kernel workspace；
- sort / routing / MoE 临时 buffer；
- graph capture pool；
- compilation/runtime scratch；
- 临时 layout conversion buffer。

Workspace 往往依实现而变化，不能从 Model Schema 单独推出。没有直接信息时应保持未知或给出显式假设范围。

## Communication Buffers

分布式执行还可能需要：

- collective staging buffer；
- All-to-All send / receive buffer；
- pipeline P2P buffer；
- KV transfer buffer；
- RDMA registration / bounce buffer。

这些 buffer 属于 System × Parallelism × Runtime 属性。后续 [[system/communication/README|Communication Model]] 与 [[system/parallelism/README|Parallelism Model]] 负责推导其数据量和生命周期。

## Allocator Overhead 与 Fragmentation

“tensor 总和”通常不等于“进程实际占用”。

需要单独考虑：

```text
allocator_overhead_bytes
=
reserved_pool
+ fragmentation
+ alignment / page rounding
+ allocator metadata
```

这个量高度依赖 runtime 和 allocator，不应设一个全仓固定百分比。

如果没有实测或实现依据：

- 不默认“额外 10%”或类似经验值；
- 可以在具体 scenario 中显式设定 margin；
- 必须把 margin 标成假设，而不是事实。

## Runtime Reserve

设备内存通常还要为不属于模型 tensor 的系统组件保留空间，例如 runtime context、driver/runtime allocations、监控或其他长期驻留对象。

因此容量判断应使用：

```text
usable_device_memory_bytes
=
physical_device_memory_bytes
- explicit_runtime_reserve_bytes
```

若 reserve 未知，就不能把 physical capacity 全部当成 workload 可用容量。

## 多层内存与 Offload

多层内存必须分别记账：

```text
Device HBM / local device memory
Host DRAM
CXL / pooled memory
Remote DRAM
NVMe / flash
```

对于一个被 offload 的对象，要区分：

- logical state bytes；
- steady-state bytes in each tier；
- migration overlap 时是否在 source / destination 同时存在副本；
- transfer buffer；
- cache / duplicate copy；
- failover replica。

例如一个 10 GB 逻辑对象从 HBM 迁到 Host DRAM，不代表系统瞬间只占 10 GB。迁移窗口可能暂时同时存在 source、destination 和 transfer buffer。

## Capacity Feasibility

当且仅当所有关键项都已知或有明确上界时，才能做单设备容量判断：

```text
memory_headroom_bytes
=
usable_device_memory_bytes
- peak_device_resident_bytes
```

必要条件：

```text
memory_headroom_bytes >= 0
```

这只是 **容量可行性**，不是性能可行性。

即使放得下，也可能因为 [[system/compute/README|Compute]]、后续 `MEM-005` Memory Bandwidth、[[system/communication/README|Communication]] 或 [[system/topology/README|Topology]] 而达不到 SLA。

## 推理与训练不能共用一张简单公式

推理常见主要项：

```text
weights
+ KV
+ activations
+ workspace
+ communication buffers
+ allocator/runtime reserve
```

训练还会引入：

```text
parameters
+ gradients
+ optimizer states
+ possible master weights
+ saved activations
+ communication / checkpoint buffers
```

训练侧将在 `TRN-002` 单独建模，不把 optimizer state 经验倍数硬塞进推理 Memory Model。

## 未知值规则

这是 Memory Accounting 最重要的质量规则之一：

```text
unknown != 0
```

如果 KV layout、workspace、allocator reserve 或某个复制策略未知：

- 保持 `unknown`；
- 或给出明确的 lower bound / upper bound；
- 或在 scenario 中设置显式 assumption。

不得为了得到一个“能放几张卡”的漂亮结果把未知项按零计算。

## 输出

Memory Accounting 的统一输出包括：

- `weight_resident_bytes`
- `kv_resident_bytes`
- `activation_peak_bytes`
- `workspace_peak_bytes`
- `communication_buffer_peak_bytes`
- `peak_device_resident_bytes`
- `memory_headroom_bytes`

每个输出必须附带：

```text
value
+ unit
+ scope
+ phase / time window
+ inputs
+ assumptions
```

后续自动派生脚本必须保留这些元数据，不能只输出裸数字。

## 与其他层的关系

- Workload：[[system/workload/ai-workload-model|AI Workload Model]]
- KV hierarchy：[[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层级]]
- Compute：[[system/compute/README|Compute Model]]
- Communication：[[system/communication/README|Communication Model]]
- Parallelism：[[system/parallelism/README|Parallelism Model]]
- Topology：[[system/topology/README|Topology Model]]
- Hardware：[[chip/00-project-index|AI 芯片与基础设施资料库]]
- Schema：[[system/SCHEMA|System Schema V0.1]]

## 直接来源

本页定义的是统一 memory accounting 口径和代数边界，没有引入厂商容量、benchmark 或协议数值，因此 `evidence: {}`。后续具体模型、硬件或 runtime 数值必须使用直接 Evidence。
