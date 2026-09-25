---
schema_version: system-v0.1
name: Accelerator / Network Failure Domain
object_type: concept
category: reliability
inputs:
  - topology.failure_domain
  - hardware.device_health
  - hardware.link_health
  - workload.parallel_group
  - workload.replica
constraints:
  - correlated-failure
  - degraded-topology
  - retry
  - recovery-scope
outputs:
  - device_failure_scope
  - network_failure_scope
  - degraded_capacity
  - recovery_boundary
  - placement_anti_affinity
assumptions:
  - device failure 与 network path failure 分开
  - replica 数量只有跨独立 failure domain 才能形成独立冗余
related_layers:
  - workload
  - parallelism
  - communication
  - topology
  - scheduling
  - network
  - reliability
  - accelerator
evidence: {}
updated: 2026-09-25
tags:
  - system
  - reliability
  - failure-domain
---
# Accelerator / Network Failure Domain

> AI 集群里的“卡坏了”和“网络坏了”会以不同方式破坏 workload。可靠性模型需要记录 blast radius、degraded topology 和 recovery scope。

## Device Failure

Device failure 可能影响：

- one rank
- one pipeline stage
- one expert shard
- one replica
- entire tightly-coupled group

影响范围由 parallelism 决定，而不是只看 device 本身。

## Link / NIC / Switch Failure

Network failure 可能：

- 断开一个 peer path
- 降低 aggregate bandwidth
- 让 topology 非对称
- 隔离一个 rack / rail
- 触发 route failover

因此“device health = healthy”并不意味着 workload topology healthy。

## Degraded Mode

故障后系统可能仍可运行，但：

```text
available bandwidth ↓
participant count ↓
capacity ↓
tail latency ↑
```

需要把 degraded mode 与 hard failure 分开。

## Parallel Group

TP/PP/EP/CP group 里的单 rank failure 可能让整个 group 无法继续。

所以 recovery boundary 需要记录：

```text
rank
→ parallel group
→ replica/job
```

## Replica

Serving replica 只有放在不同 failure domain 才能提供更强隔离。

同 rack / 同 power / 同 switch 下的多 replica 仍可能相关失败。

见 [[system/topology/rack-and-failure-domain|Rack / Failure Domain]]。

## Retry / Replay

恢复策略可能包括：

- request retry
- rank restart
- group restart
- checkpoint restore
- replica failover

不同策略消耗的时间和状态不同。

## Detection

可靠性还依赖 failure detection latency。

检测太慢会扩大：

- request timeout
- collective stall
- wasted compute

但本页不规定具体 heartbeat/runtime 实现。

## 输出

- `device_failure_scope`
- `network_failure_scope`
- `degraded_capacity`
- `recovery_boundary`
- `placement_anti_affinity`

## 直接来源

本页定义通用 accelerator/network failure-domain 语义，不引入具体硬件故障率或 SLA 数值，因此 `evidence: {}`。
