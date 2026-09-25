---
schema_version: system-v0.1
name: Rack Power / Cooling Model
object_type: concept
category: power
inputs:
  - hardware.device_power
  - hardware.node_power
  - topology.devices_per_node
  - topology.nodes_per_rack
  - facility.power_budget
  - facility.cooling_capacity
constraints:
  - rack-power
  - power-delivery
  - cooling
  - thermal-headroom
  - density
outputs:
  - rack_it_power
  - power_headroom
  - cooling_load
  - density_limit
  - placement_power_constraints
assumptions:
  - TDP/board power、实际 workload power 与 rack facility budget 分开
  - 不能把单设备峰值机械乘数量当作完整设施功耗
related_layers:
  - workload
  - topology
  - scheduling
  - power
  - reliability
  - accelerator
evidence: {}
updated: 2026-09-25
tags:
  - system
  - power
  - cooling
  - rack
---
# Rack Power / Cooling Model

> AI hardware 最终必须塞进真实 power/cooling envelope。Rack Power Model 从 device→node→rack 逐层聚合，但保留峰值、实测和设施预算的区别。

## Device Power

硬件页可能记录：

```text
device/module power
```

但它不自动等于 workload 实际功耗。

需要区分：

- rated / configured limit
- observed workload power
- idle power

本页不从型号猜测 utilization。

## Node Power

Node 还包括：

- CPU
- memory
- NIC
- storage
- fans/pumps
- power conversion loss

因此：

```text
node_power
!= accelerator_count × accelerator_power
```

后者最多是 accelerator 子项。

## Rack IT Power

如果每 node 实际 IT power 为 `P_node_i`：

```text
rack_it_power
= Σ_i P_node_i
+ rack_shared_IT_load
```

需要和 rack/facility 可供 IT budget 比较。

## Power Headroom

```text
power_headroom
= available_IT_power
- planned_peak_IT_power
```

headroom 需要覆盖：

- workload variation
- degraded cooling
- maintenance
- transient / policy margin

具体 margin 不使用全仓固定百分比。

## Cooling

Cooling capacity 必须与热负载和环境条件匹配。

系统模型至少记录：

- cooling method
- shared cooling domain
- capacity
- failure impact

不在本页写某种冷却方式必然支持多少 kW。

## Density

增加 accelerators/rack 同时提高：

- compute density
- power density
- cooling load
- network cable/port density
- failure blast radius

所以“更高密度”不是单向收益。

## Placement

调度可受 power/thermal 约束：

- rack power headroom
- cooling health
- thermal hotspot
- maintenance state

因此 topology-aware scheduling 可以进一步扩展为 power-aware placement。

## Failure Domain

Power feed / cooling loop 也是 correlated failure domain。

与 [[system/topology/rack-and-failure-domain|Rack / Failure Domain]] 联合使用。

## 输出

- `rack_it_power`
- `power_headroom`
- `cooling_load`
- `density_limit`
- `placement_power_constraints`

## 直接来源

本页定义通用 rack power/cooling accounting，不引入具体 facility 或产品数值，因此 `evidence: {}`。
