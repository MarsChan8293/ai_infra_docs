---
schema_version: system-v0.1
name: Memory Bandwidth Model
object_type: concept
category: memory-bandwidth
inputs:
  - workload.tokens_per_step
  - workload.tokens_per_second
  - memory.bytes_read_per_step
  - memory.bytes_written_per_step
  - memory.bytes_per_token
  - hardware.memory.bandwidth
  - execution.cache_reuse
constraints:
  - memory-bandwidth
  - memory-latency
  - data-reuse
  - concurrency
  - memory-controller-efficiency
outputs:
  - bytes_per_step
  - bytes_per_token
  - required_bandwidth_bytes_s
  - memory_time_lower_bound
  - bandwidth_limited_tokens_s
assumptions:
  - 只有位于关键路径的数据移动才进入该阶段的带宽时间下界
  - 标称峰值带宽只用于理论下界，有效带宽必须单独记录
  - 同一数据若被缓存或复用，必须按实际从目标 memory tier 搬运的字节计数
related_layers:
  - workload
  - compute
  - memory
  - accelerator
evidence: {}
updated: 2026-09-25
tags:
  - system
  - memory
  - bandwidth
---
# Memory Bandwidth Model

> Memory Bandwidth Model 回答的是“一个执行阶段必须搬多少字节，以及这会给延迟或吞吐设置什么下界”。它不把 HBM 标称 TB/s 直接等同于应用可用带宽。

## 基本量

对一个执行 step，定义：

```text
bytes_per_step
= bytes_read_per_step
+ bytes_written_per_step
```

如果 step 处理 `N_token` 个有效 token：

```text
bytes_per_token
= bytes_per_step / N_token
```

如果目标吞吐为 `R_token` token/s，则最低数据搬运需求：

```text
required_bandwidth
= bytes_per_token × R_token
```

这些量必须绑定明确 memory tier，例如 HBM、Host DRAM 或远端 memory。不同层的带宽不能直接相加成一个“总带宽”。

## 带宽时间下界

若关键路径需要从某 memory tier 搬运 `D` bytes，该层有效带宽为 `B_effective`：

```text
T_memory
>= D / B_effective
```

若只能获得硬件标称峰值 `B_peak`：

```text
D / B_peak
```

只能解释为理想理论下界，不能称为预期执行时间。

## 有效带宽与标称带宽

至少区分：

- physical / pin bandwidth；
- vendor peak memory bandwidth；
- kernel achieved bandwidth；
- application effective bandwidth。

有效带宽会受到访问模式、bank/channel 利用率、读写混合、并发、cache hit、alignment、ECC/协议开销、kernel scheduling 等影响。

因此仓库中的性能推导必须明确使用的是哪一层带宽口径。

## Weight Traffic

对 Decode 等小 `M` 场景，如果某层权重在每个 step 都必须从 HBM 重新读取，可定义：

```text
weight_bytes_per_step
≈ resident_weight_payload_touched
```

但不能默认“模型权重大小 = 每 token HBM 读取量”。原因包括：

- batch 让一次权重读取服务多个 token；
- on-chip cache / reuse；
- TP/PP/EP 分片；
- kernel fusion；
- 权重压缩与 runtime layout。

因此更安全的形式是：

```text
weight_bytes_per_token
= weight_bytes_per_step / useful_tokens_in_step
```

batch 增大时，这一项可能显著下降。

## KV Traffic

KV traffic 与 KV capacity 是两个不同问题。

容量回答：

```text
how many bytes must remain resident
```

带宽回答：

```text
how many resident bytes are actually read/written on the critical path per step
```

Decode 中 attention 可能随 context length 增长读取更多历史 KV，但具体读取量取决于 MHA/GQA/MLA、local/sparse attention、kernel 和 cache layout。

因此不能从 `kv_cache_bytes` 直接假定每 step 会完整扫描同等字节。

## Activation / Workspace Traffic

Activation 与 workspace 可能发生：

- HBM write-back；
- HBM reread；
- on-chip SRAM/cache reuse；
- fused kernel 内部消除中间落盘。

所以数学 tensor 大小与外部 memory traffic 不等价。

若实现细节未知，应给出 lower/upper bound 或保持未知。

## Read / Write Asymmetry

如果硬件或介质的读写特性不同，应分别记：

```text
read_bytes / B_read_effective
write_bytes / B_write_effective
```

并根据是否能 overlap 决定 critical path。

对 SSD、远端 memory 或某些分层系统，读写带宽、时延和耐久度可能完全不同，更不能合成一个单值。

## Bandwidth-Limited Throughput

若每 token 在关键 memory tier 至少产生 `D_token` bytes 数据搬运，且该层有效带宽为 `B_effective`：

```text
tokens_per_second_memory_ceiling
<= B_effective / D_token
```

如果用 `B_peak`，得到的是理论 ceiling，而不是 benchmark 预测。

## Batch 的作用

假设某权重 payload `W` bytes 在一个 step 中读取一次，并服务 `B` 个 token：

```text
weight_bytes_per_token
≈ W / B
```

这是为什么 batch 增大可能提升 arithmetic intensity。

但 batch 同时可能增加：

- activation traffic；
- KV traffic；
- workspace；
- latency；
- queueing。

因此 batch 不应被简单理解为“带宽成本除以 B 后其他不变”。

## 多级内存

对于：

```text
HBM
→ Host DRAM
→ CXL / Remote Memory
→ NVMe
```

必须分别记录：

```text
bytes_moved_on_each_tier
effective_bandwidth_of_each_tier
latency_of_each_transfer
overlap
```

如果路径串行：

```text
T_transfer_lower_bound
>= sum(D_i / B_i)
```

若路径可 pipeline/overlap，则端到端下界由关键瓶颈 stage 与 fill/drain 决定，不能直接把所有 tier 的 TB/s 相加。

## 与 Compute 的联合判断

Memory Bandwidth Model 不单独判断 workload 是否 memory-bound。需要把：

```text
T_compute_lower_bound
```

与：

```text
T_memory_lower_bound
```

联合比较。

统一入口见 [[system/compute/roofline-and-arithmetic-intensity|Roofline 与 Arithmetic Intensity]]。

## 输出

- `bytes_per_step`
- `bytes_per_token`
- `required_bandwidth_bytes_s`
- `memory_time_lower_bound`
- `bandwidth_limited_tokens_s`

每个输出必须携带：

```text
memory tier
+ read/write direction
+ scope
+ workload
+ reuse assumption
+ bandwidth definition
```

## 与其他层的关系

- Workload：[[system/workload/ai-workload-model|AI Workload Model]]
- Memory Accounting：[[system/memory/model-memory-accounting|Model Memory Accounting]]
- Compute：[[system/compute/transformer-compute-model|Transformer Compute Model]]
- Hardware：[[chip/00-project-index|AI 芯片与基础设施资料库]]
- Schema：[[system/SCHEMA|System Schema V0.1]]

## 直接来源

本页定义通用字节流和带宽下界关系，没有引入具体硬件标称带宽或 benchmark，因此 `evidence: {}`。
