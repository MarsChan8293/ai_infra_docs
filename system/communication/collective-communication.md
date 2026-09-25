---
schema_version: system-v0.1
name: Collective Communication
object_type: concept
category: communication-model
inputs:
  - communication.collective_type
  - communication.message_size_bytes
  - communication.participant_count
  - communication.algorithm
  - topology.link_bandwidth
  - topology.latency
  - topology.bisection_bandwidth
constraints:
  - startup-latency
  - serialization
  - link-bandwidth
  - synchronization
  - topology
  - contention
outputs:
  - communication_pattern
  - algorithm_steps
  - bytes_on_critical_path
  - communication_time_lower_bound
  - topology_requirements
assumptions:
  - 逻辑 payload、每 rank 收发字节和网络 wire traffic 必须分开表达
  - 标称链路带宽不等于 collective 可用有效带宽
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
  - collective
---
# Collective Communication

> Collective Communication 把多个 rank / accelerator 之间的数据交换定义成可组合的通信语义。AI workload 真正关心的不只是“网络多少 GB/s”，而是 **什么 collective、多少参与者、每个 rank 多大 payload、经过什么拓扑和算法**。

## 输入

Collective Model 至少需要：

- collective type；
- participant count；
- logical message size；
- rank placement；
- collective algorithm；
- 每条相关路径的 bandwidth / latency；
- topology 的 hop、oversubscription、bisection 与 rail 情况。

没有 placement 和 topology 时，只能得到抽象通信量，不能得到可靠的端到端时间。

## 常见 Collective

| Collective | 基本语义 | AI Infra 常见关系 |
|---|---|---|
| All-Reduce | 聚合后每个 rank 获得完整结果 | Data Parallel gradient、部分 TP |
| Reduce-Scatter | 聚合并把结果分片 | ZeRO/FSDP、TP 组合 |
| All-Gather | 收集分片形成完整逻辑结果 | TP、参数/activation 分片 |
| All-to-All | 每个 rank 向多个 rank 交换不同数据 | MoE Expert Parallel |
| Broadcast | 一个 rank 向其他 rank 发送同一 payload | 初始化、控制/状态分发 |
| Gather / Scatter | 多对一或一对多分发 | 特定数据布局转换 |

具体算法和精确通信量分别在 `COM-002`、`COM-003` 中展开。

## 三种“字节数”必须分开

Collective 分析最容易出错的地方，是把不同含义的 bytes 混成一个数字。

至少区分：

### Logical Payload

应用层想要交换或聚合的数据大小。

```text
logical_message_bytes
```

### Per-rank Traffic

某个 rank 在 collective 中实际发送/接收的总字节。

```text
bytes_sent_per_rank
bytes_received_per_rank
```

它取决于 collective algorithm、participant count 和 chunking。

### Wire / Link Traffic

具体物理链路上承载的字节。

一个 logical payload 可能被：

- 分 chunk；
- 多 hop 转发；
- 多次经过不同 link；
- 在交换网络中复制；
- 因协议产生额外 overhead。

因此：

```text
logical payload
≠ per-rank traffic
≠ wire traffic
```

## 通信时间骨架

后续 `COM-005` 会给出统一 Cost Model。本页先固定最小语义：

```text
T_collective
>= startup / synchronization
 + serialization on critical path
 + transfer on critical bottleneck
```

可抽象写成：

```text
T
≈ N_steps × alpha
 + bytes_on_critical_path / B_effective
 + synchronization_penalty
 + contention_penalty
```

其中：

- `alpha` 表示每阶段固定启动/协议/同步时延；
- `B_effective` 是该算法与拓扑下的有效吞吐，不是厂商 link peak；
- critical path 由算法和 placement 决定。

这个式子是建模骨架，不意味着所有 collective 都能被一个 alpha/beta 参数精确描述。

## Participant Count

参与 rank 数量 `N` 会同时改变：

- 算法 step 数；
- per-rank traffic；
- topology span；
- synchronization fan-in/fan-out；
- 跨 node / rack 的概率；
- 故障暴露面。

所以“8 卡 collective”和“1024 卡 collective”不是同一个问题，即使单链路 bandwidth 相同。

## Topology

Collective 性能依赖真实物理路径：

```text
Accelerator
→ local scale-up fabric / PCIe
→ NIC
→ switch fabric
→ remote NIC
→ remote accelerator
```

不同 rank placement 可能导致 collective：

- 完全留在单个 Scale-up domain；
- 跨多个 node；
- 穿越 top-of-rack / spine；
- 跨 rail；
- 跨低 bisection / oversubscribed 区域。

因此 [[system/topology/scale-up-vs-scale-out|Scale-up vs Scale-out]] 和 [[system/scheduling/topology-aware-scheduling|拓扑感知调度]] 是 collective model 的一部分，而不是部署后的附加优化。

## Bandwidth 也有多种含义

需要区分：

- link raw bandwidth；
- per-direction bandwidth；
- bidirectional aggregate；
- NIC injection bandwidth；
- switch port bandwidth；
- fabric bisection bandwidth；
- algorithm effective bandwidth；
- application observed bandwidth。

如果厂商给出“双向总带宽”，而公式需要单向 transfer bandwidth，必须先统一口径。

## Chunking 与 Pipeline

大消息通常可以分 chunk，并让多个 link / stage 并行工作。

这会改变：

- startup 次数；
- pipeline fill/drain；
- link utilization；
- buffer 占用；
- overlap 机会。

所以简单的：

```text
message_bytes / link_bandwidth
```

通常只是一个非常粗的下界。

## Compute / Communication Overlap

通信可以与计算重叠，但“能 overlap”不等于“通信免费”。

端到端 critical path 更接近：

```text
T_step
>= max(
  non_overlapped_compute,
  non_overlapped_communication,
  dependency_critical_path
)
```

实际 overlap 程度取决于：

- dependency；
- stream / scheduling；
- chunking；
- kernel occupancy；
- NIC / DMA engine；
- memory bandwidth 竞争。

因此 System 页面不能把 theoretical overlap 当成已实现的性能事实。

## Collective 与 Parallelism

不同并行策略天然产生不同 collective：

```text
Data Parallel
→ gradient aggregation

Tensor Parallel
→ All-Reduce / Reduce-Scatter / All-Gather 等

Expert Parallel
→ All-to-All / token dispatch

Pipeline Parallel
→ Point-to-Point activation transfer

Context Parallel
→ attention / KV 相关跨 rank 交换
```

统一入口见 [[system/parallelism/parallelism-overview|Parallelism Overview]]。

## 故障与尾延迟

Collective 的 completion 往往受最慢参与者和关键路径约束。

需要考虑：

- straggler；
- congestion；
- link degradation；
- rank failure；
- retry / timeout；
- topology asymmetry。

因此平均 link bandwidth 不能直接代表 distributed step 的尾延迟。

## 输出

本概念输出：

- `communication_pattern`
- `algorithm_steps`
- `bytes_on_critical_path`
- `communication_time_lower_bound`
- `topology_requirements`

后续精确 collective 页需要继续保留：

```text
payload definition
+ participant count
+ algorithm
+ topology
+ bandwidth directionality
+ assumptions
```

## 与其他层的关系

- Workload：[[system/workload/ai-workload-model|AI Workload Model]]
- Parallelism：[[system/parallelism/README|Parallelism Model]]
- Topology：[[system/topology/README|Topology Model]]
- Scheduling：[[system/scheduling/topology-aware-scheduling|拓扑感知调度]]
- Hardware：[[chip/00-project-index|AI 芯片与基础设施资料库]]
- Schema：[[system/SCHEMA|System Schema V0.1]]

## 直接来源

本页定义的是仓库内部 collective 建模语义和量纲边界，没有引入具体协议、链路或 benchmark 数值，因此 `evidence: {}`。
