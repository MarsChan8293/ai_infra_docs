---
schema_version: system-v0.1
name: Weight Memory Model
object_type: concept
category: memory-model
inputs:
  - model.parameters
  - model.parameter_sharing
  - execution.weight_precision
  - execution.quantization
  - workload.parallelism
  - runtime.weight_layout
constraints:
  - memory-capacity
  - sharding
  - replication
  - quantization-metadata
  - runtime-layout
outputs:
  - logical_weight_payload_bytes
  - resident_weight_bytes
  - per_device_weight_bytes
  - replicated_weight_bytes
  - weight_metadata_bytes
assumptions:
  - 参数量、逻辑 payload、checkpoint 文件大小和 runtime resident bytes 分开表达
  - MoE active parameters 只描述每 token 计算，不自动减少所有 expert 权重的驻留需求
  - 分片后 per-device weight 不能无条件用 global bytes 除以设备数
related_layers:
  - model
  - workload
  - memory
  - parallelism
  - topology
  - accelerator
evidence: {}
updated: 2026-09-25
tags:
  - system
  - memory
  - weights
---
# Weight Memory Model

> Weight Memory Model 负责把模型参数事实转换成逻辑 weight payload 和实际设备驻留。它刻意区分“有多少参数”“checkpoint 多大”“runtime 占多少显存”这三个不同问题。

## 最小 Payload

若有 `P_stored` 个实际存储标量，每个标量 `b` bytes：

```text
logical_weight_payload_bytes
= P_stored × b
```

这是最基础 payload，不包含：

- quantization scale / zero point
- packing / alignment
- tensor metadata
- runtime transformed copy
- allocator overhead

因此不能直接把该值称为“真实显存占用”。

## 参数量与存储标量

`model.parameters.total` 不一定总能直接等于 `P_stored`。

需要考虑：

- tied embedding / output head
- shared experts
- parameter sharing
- duplicated checkpoint tensors
- non-parameter buffers

如果 Schema 没有足够信息，使用 total parameters 计算只能标成近似。

## Precision

常见分析方法是显式给出：

```text
bytes_per_stored_element
```

然后计算 payload。

关键是把精度写成 assumption 或 verified fact，不能根据模型名称猜。

例如：

```text
P × 2 bytes
```

只代表一个 2-byte/parameter 场景，不自动等于“BF16 runtime 实际占用”。

## Quantization

量化后：

```text
resident_weight_bytes
=
quantized_payload
+ scales
+ zero_points
+ group_metadata
+ padding
+ possible_dequant_workspace
```

所以“4-bit = 参数量 × 0.5 byte”通常只给出 payload baseline。

Group size 越小，metadata 相对占比可能越高。

## Runtime Layout

Runtime 可能把 checkpoint 权重转换为：

- packed tensor
- transposed layout
- fused layout
- device-specific format

加载或转换期间可能同时存在旧 copy 与新 copy。

因此要区分：

```text
steady_state_resident_bytes
peak_load_time_bytes
```

部署 capacity 判断应使用对应阶段的峰值，而不是 checkpoint 文件大小。

## Tensor Parallel

TP 可能切分某些权重，但不同 tensor 的 partition rule 不同。

通用形式：

```text
global tensor
→ shard rule
→ local shard
+ replicated tensors
```

所以：

```text
per_device_weight_bytes
!= global_weight_bytes / TP
```

除非已经证明所有相关权重均匀切分且没有复制。

## Pipeline Parallel

PP 按 layer / stage 切分。

若 stage i 包含的参数量为 `P_i`：

```text
stage_weight_payload
≈ P_i × bytes_per_element
```

均匀 layer 数不代表均匀 weight bytes，也不代表均匀 compute。

Embedding、output head 或特殊 layer 可能让 stage 不平衡。

## Expert Parallel

MoE 必须分开：

- total expert weights
- shared expert weights
- per-token active experts
- per-rank resident experts

`parameters.active` 影响每 token compute，但不能自动代替 weight capacity。

如果 128 个 experts 中每 token 只激活 8 个，设备仍可能驻留远多于 8 个 experts。

所以：

```text
active_parameter_count
!= resident_parameter_count
```

## Replication

常见复制对象可能包括：

- embeddings
- norm
- router
- shared experts
- output head
- metadata

因此每 rank 的 weight resident 应写成：

```text
local_shards
+ replicated_weights
+ metadata
```

## Offload

Weight offload 必须分别记录：

```text
logical total weight
device resident working set
host / remote resident copy
transfer bytes per load
prefetch / eviction policy
```

容量降低通常以 PCIe/CXL/network traffic 和 latency 为代价。

Offload 不能只修改 device capacity 数字而忽略 transfer path。

## Memory Accounting

最终 per-device weight 进入：

[[system/memory/model-memory-accounting|Model Memory Accounting]]

```text
peak_device_resident_bytes
= weight_resident_bytes
+ KV
+ activation
+ workspace
+ ...
```

Weight 页只负责 weight 项，不把其他 buffer 混进来。

## Bandwidth

Weight residency 也不等于 weight traffic。

一份 50 GB resident weights 可能在某 step：

- 被完整读一次
- 被 batch 内多个 token 复用
- 有部分 cache hit
- 只访问 active experts

因此 bytes/token 由 [[system/memory/memory-bandwidth-model|Memory Bandwidth Model]] 单独建模。

## 输出

- `logical_weight_payload_bytes`
- `resident_weight_bytes`
- `per_device_weight_bytes`
- `replicated_weight_bytes`
- `weight_metadata_bytes`

每个输出应携带 precision、quantization、partition、scope 与 runtime-layout assumption。

## 直接来源

本页定义通用 weight accounting 方法，没有引入具体模型 checkpoint 或硬件容量，因此 `evidence: {}`。
