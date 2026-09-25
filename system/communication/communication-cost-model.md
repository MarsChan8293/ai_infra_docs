---
schema_version: system-v0.1
name: Communication Cost Model
object_type: concept
category: communication-model
inputs:
  - communication.payload_bytes
  - communication.bytes_on_critical_path
  - communication.steps
  - topology.path
  - topology.effective_bandwidth
  - topology.per_step_latency
  - execution.overlap
constraints:
  - startup-latency
  - serialization
  - transfer-bandwidth
  - synchronization
  - contention
  - dependency
outputs:
  - startup_time
  - serialization_time
  - transfer_time
  - synchronization_time
  - communication_time_lower_bound
  - non_overlapped_communication_time
assumptions:
  - payload bytes、per-rank bytes 和 critical-path wire bytes 分开记录
  - 只有明确的依赖和 overlap 假设才能从通信时间中扣除重叠部分
related_layers:
  - workload
  - parallelism
  - communication
  - topology
  - scheduling
  - accelerator
  - network
evidence: {}
updated: 2026-09-25
tags:
  - system
  - communication
  - cost-model
---
# Communication Cost Model

> Communication Cost Model 把通信拆成启动、序列化、传输、同步、竞争和依赖，而不是用“消息大小 ÷ 链路峰值”冒充端到端成本。

## 输入

统一模型至少需要：

- payload definition；
- participant / endpoint；
- algorithm steps；
- critical path；
- rank placement；
- effective bandwidth；
- per-step latency；
- overlap 条件。

[[system/communication/collective-communication|Collective Communication]] 负责定义通信模式，本页负责把该模式转换成时间成本。

## 最小时间骨架

一个通信阶段可拆成：

```text
T_comm
=
T_startup
+ T_serialization
+ T_transfer
+ T_sync
+ T_contention
```

这只是概念分解。具体实现中各项可能部分重叠，不应机械全部相加。

## Startup

启动成本可以包含：

- software/runtime dispatch；
- protocol setup；
- doorbell / command；
- collective phase transition；
- rendezvous。

若一个算法有 `N_step` 个必须串行的通信 phase，且每 phase 固定成本近似 `alpha`：

```text
T_startup
≈ N_step × alpha
```

如果实际实现 pipeline 多个 phase，则需要按真实 critical path 重新计算。

## Serialization

将 `D` bytes 放到一条有效速率为 `B` 的通道，最基本的 serialization lower bound：

```text
T_serialization
>= D / B
```

但这里的 `D` 必须是 **critical path 上该资源实际承载的 bytes**。

不能直接用 logical message size 替代。

## Multi-hop Transfer

若路径包含多个 stage：

```text
accelerator
→ local fabric
→ NIC
→ switch fabric
→ remote NIC
→ remote accelerator
```

在完全串行、无 pipeline 的保守模型里：

```text
T_transfer
>= Σ(D_i / B_i)
```

在流式 pipeline 下，steady-state 可能更接近最慢 stage：

```text
throughput
<= min(B_i)
```

但端到端仍需考虑 fill / drain 和各 hop latency。

## Bottleneck Bandwidth

路径有效吞吐不是：

```text
sum(link_bandwidth)
```

而通常受下列最小项限制：

- endpoint injection；
- PCIe/local path；
- NIC；
- oversubscribed uplink；
- fabric bisection；
- remote endpoint；
- competing traffic。

因此可抽象：

```text
B_path_effective
<= min(B_stage_effective)
```

## Synchronization

Collective 或 distributed step 往往不能在“本 rank 发完数据”时立即继续。

还可能等待：

- 最慢 rank；
- reduction completion；
- barrier；
- dependent kernel；
- remote receive / combine。

因此：

```text
T_sync
```

必须与纯字节传输分开。

## Contention

共享 fabric 上的实际带宽可能低于独占测试。

竞争来源包括：

- 同一 NIC 多 rank；
- 多 collective 并发；
- storage / KV transfer 共用网络；
- oversubscription；
- background traffic；
- incast / hot spot。

如果没有可验证信息，不应静默假设：

```text
B_effective = B_peak
```

可以给出 peak lower bound，同时把 contention 标成未知。

## Latency-Bound vs Bandwidth-Bound Communication

对小消息，固定 latency 占比更高：

```text
T ≈ alpha
```

对大消息：

```text
T ≈ D / B_effective
```

二者之间的转折依算法、拓扑和实现而变，不能给全仓固定 byte threshold。

## Overlap

设：

- `T_compute` 为计算阶段；
- `T_comm` 为通信；
- `f_overlap` 表示真正能隐藏的通信比例。

可以定义：

```text
T_comm_visible
= T_comm × (1 - f_overlap)
```

但 `f_overlap` 不是随意调参。必须有 dependency 和执行结构支持，例如：

- chunked collective；
- independent compute；
- separate engines；
- stream scheduling。

更安全的 critical path 形式：

```text
T_step
>= max(
  T_compute_nonoverlap,
  T_comm_nonoverlap,
  dependency_chain
)
```

## Collective Cost

对于 collective：

```text
T_collective
≈ N_steps × alpha
+ bytes_on_critical_path / B_effective
+ synchronization_penalty
+ contention_penalty
```

不同 All-Reduce、All-Gather、Reduce-Scatter、All-to-All 算法的 `N_steps` 和 `bytes_on_critical_path` 不同，后续专题页分别展开。

## Point-to-Point

P2P 可使用更直接的形式：

```text
T_p2p
>= T_startup
 + payload_bytes / B_path_effective
 + path_latency
```

但若经过 host staging、layout conversion 或多个 memory tier，应把这些 stage 单独纳入 critical path。

## 与 Roofline 联合

当 compute、memory、communication 都存在时：

```text
T_compute
T_memory
T_comm
```

是三个不同资源下界。

如果它们完全不能重叠：

```text
T_step
>= T_compute + T_memory + T_comm
```

如果能够高度 overlap：

```text
T_step
>= max(T_compute, T_memory, T_comm)
```

真实系统通常介于两者之间。

因此 [[system/compute/roofline-and-arithmetic-intensity|Roofline]] 不能只看二维 compute-memory 后就宣告端到端瓶颈。

## 输出

- `startup_time`
- `serialization_time`
- `transfer_time`
- `synchronization_time`
- `communication_time_lower_bound`
- `non_overlapped_communication_time`

输出必须携带：

```text
payload definition
+ path
+ bandwidth definition
+ participant count
+ algorithm
+ overlap assumption
```

## 与其他层的关系

- Collective：[[system/communication/collective-communication|Collective Communication]]
- Parallelism：[[system/parallelism/parallelism-overview|Parallelism Overview]]
- Topology：[[system/topology/scale-up-vs-scale-out|Scale-up vs Scale-out]]
- Roofline：[[system/compute/roofline-and-arithmetic-intensity|Roofline 与 Arithmetic Intensity]]
- Workload：[[system/workload/ai-workload-model|AI Workload Model]]
- Schema：[[system/SCHEMA|System Schema V0.1]]

## 直接来源

本页定义仓库内部通信时间分解和 critical-path 边界，没有引入特定协议或硬件数值，因此 `evidence: {}`。
