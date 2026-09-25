---
schema_version: system-v0.1
name: Scale-up vs Scale-out
object_type: concept
category: topology
inputs:
  - communication.pattern
  - communication.message_size_bytes
  - communication.participant_count
  - hardware.accelerator_count
  - topology.node
  - topology.rack
  - topology.nic
  - topology.fabric
constraints:
  - latency
  - link-bandwidth
  - injection-bandwidth
  - bisection-bandwidth
  - hop-count
  - oversubscription
  - failure-domain
outputs:
  - topology_class
  - scale_up_domain
  - scale_out_domain
  - expected_communication_path
  - placement_boundary
  - topology_constraints
assumptions:
  - Scale-up 和 Scale-out 是系统拓扑功能分类，不绑定某个厂商协议名
  - 不使用固定带宽或距离阈值定义两类拓扑
related_layers:
  - workload
  - parallelism
  - communication
  - topology
  - scheduling
  - accelerator
  - network
  - memory
  - reliability
evidence: {}
updated: 2026-09-25
tags:
  - system
  - topology
  - scale-up
  - scale-out
---
# Scale-up vs Scale-out

> Scale-up 与 Scale-out 的核心区别不是“哪种线更快”，而是 **一个高耦合计算域内部如何扩展，以及多个计算域之间如何继续扩展**。两者需要同时考虑带宽、时延、规模、路由、故障域和调度边界。

## 定义边界

本仓库把它们作为功能性 topology 分类，而不是厂商产品标签。

### Scale-up

Scale-up domain 通常表示一个更紧耦合的 accelerator group，目标是让多个设备以接近“一个更大计算实体”的方式协作。

常见系统特征包括：

- 更强的 accelerator↔accelerator locality；
- 高频 collective / fine-grained synchronization；
- 受 domain size / switch radix / package or node topology 约束；
- 调度时希望整个 group 连续或拓扑一致。

### Scale-out

Scale-out 表示跨越一个或多个 scale-up / node domain 后继续扩展。

常见系统特征包括：

- accelerator 通过 NIC / fabric 与远端 domain 通信；
- 更大的 cluster / rack / pod 范围；
- 更多 hop、routing 和 failure-domain；
- 更依赖 fabric bisection、rail、oversubscription 和 congestion control。

这不是硬规则说“Scale-up 一定在单机、Scale-out 一定跨机”。具体产品可能打破传统边界，所以系统模型应记录真实 path，而不是只看营销名称。

## 不用固定数字定义

本仓库不采用类似：

```text
latency < X → scale-up
bandwidth > Y → scale-up
```

的固定阈值。

原因是：

- 技术代际变化很快；
- 系统规模不同；
- workload 对 latency / bandwidth 敏感度不同；
- 某些 fabric 同时承担多种角色。

判断重点是 **拓扑角色与耦合边界**。

## 通信路径

一个跨设备操作的路径可能是：

### Scale-up 内部

```text
Accelerator
→ local accelerator fabric / switch
→ Accelerator
```

### Scale-out

```text
Accelerator
→ local path
→ NIC
→ network fabric
→ remote NIC
→ remote local path
→ Accelerator
```

每增加一层都可能加入：

- serialization；
- switch hop；
- queue；
- protocol；
- topology contention；
- NUMA / PCIe locality；
- failure domain。

因此 end-to-end bandwidth 不能由某一条 link peak 单独代表。

## 关键指标

### Link Bandwidth

单条物理/逻辑 link 的传输能力。

需要明确：

- 单向还是双向 aggregate；
- payload 还是 raw line rate；
- 每 link 还是 device aggregate。

### Injection Bandwidth

一个 endpoint 能注入 fabric 的总吞吐上限。

即使每条 link 很快，如果 endpoint / NIC injection 较低，总通信仍被入口限制。

### Bisection Bandwidth

把网络节点分成两组后，跨越切面的总可用带宽。

大规模 All-to-All、All-Reduce 等 workload 可能更敏感于 bisection，而不是单 link peak。

### Hop Count

消息经过的 switch / routing stage 数。

更多 hop 通常意味着更多潜在：

- latency；
- queue；
- congestion；
- failure point。

但具体影响仍取决于 fabric 和 workload。

### Oversubscription

下游 endpoint aggregate bandwidth 高于上游可提供 bandwidth 时，会形成 oversubscription。

因此：

```text
sum(endpoint link peak)
```

不能自动推出 fabric 可以同时提供同样的 bisection throughput。

## Parallelism 映射

[[system/parallelism/parallelism-overview|Parallelism]] 的不同 group 对 topology 的需求不同。

### Tensor Parallel

通常是高频、强同步 group，应重点关注：

- scale-up locality；
- latency；
- collective effective bandwidth。

### Expert Parallel

MoE All-to-All 可能覆盖更大的 group，需要关注：

- bisection；
- per-rank injection；
- imbalance；
- cross-rack path。

### Pipeline Parallel

主要是 stage-to-stage P2P，需要关注：

- neighbor path；
- activation size；
- stage dependency。

### Data Parallel

训练 gradient synchronization 可扩展到更大的 scale-out domain，但随着 participant 增加要重新评估 collective algorithm 和 topology。

这些只是 workload pattern，不是固定 placement 规则。

## Placement Boundary

调度系统应显式知道：

```text
which ranks must stay in one scale-up domain
which ranks may span scale-out domains
which ranks require NIC locality
which groups may cross failure domains
```

所以 topology 不是部署后的监控属性，而应进入 placement。

见 [[system/scheduling/topology-aware-scheduling|拓扑感知调度]]。

## Failure Domain

Scale-up 与 Scale-out 同时也是可靠性边界。

可能的 failure domain 包括：

- accelerator；
- local switch；
- node；
- NIC；
- top-of-rack；
- rail；
- rack；
- fabric plane。

把所有 rank 放进最快的局部 domain 可能改善性能，但也可能让更多 work 同时暴露在一个故障域中。

后续 `TOP-005` 和 `REL-002` 继续展开。

## Memory / KV Transfer

P/D 分离、KV offload、remote memory 等 workload 也需要判断数据路径：

```text
HBM
→ local scale-up peer
→ Host / NIC
→ scale-out fabric
→ remote memory / accelerator
```

因此 [[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层级]] 与 topology 必须联合判断 transfer cost。

## Scale-up 不是“自动更快”

即使操作留在 scale-up domain，仍可能受：

- switch contention；
- non-uniform topology；
- poor collective mapping；
- link imbalance；
- memory bandwidth；
- synchronization

限制。

同样，Scale-out 也不是某个特定协议的代名词。应记录真实硬件和路径。

## 输出

本概念输出：

- `topology_class`
- `scale_up_domain`
- `scale_out_domain`
- `expected_communication_path`
- `placement_boundary`
- `topology_constraints`

这些输出供：

- [[system/communication/collective-communication|Communication]]
- [[system/parallelism/parallelism-overview|Parallelism]]
- [[system/scheduling/topology-aware-scheduling|Scheduling]]

消费。

## 与硬件层的关系

硬件对象应记录可验证的 link、port、bandwidth、device / system scope 等事实；System 层只解释这些事实如何形成 workload topology。

- Hardware：[[chip/00-project-index|AI 芯片与基础设施资料库]]
- Resource：[[system/resource/accelerator-resource-model|加速器资源模型]]
- Schema：[[system/SCHEMA|System Schema V0.1]]

## 直接来源

本页定义的是 scale-up / scale-out 的仓库内部系统分类和拓扑分析框架，没有引入厂商协议数值，因此 `evidence: {}`。
