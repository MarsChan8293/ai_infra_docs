---
schema_version: system-v0.1
name: KV Cache Model
object_type: concept
category: memory-model
inputs:
  - model.attention
  - model.layers
  - model.kv_heads
  - model.head_dim
  - model.cache_layout
  - workload.sequence_length
  - workload.batch_size
  - workload.concurrency
  - execution.kv_precision
constraints:
  - memory-capacity
  - memory-bandwidth
  - cache-layout
  - sharding
  - allocator-overhead
outputs:
  - growing_kv_bytes_per_token
  - growing_kv_bytes_per_sequence
  - fixed_attention_state_bytes
  - per_device_kv_bytes
  - kv_growth_rate_bytes_per_token
assumptions:
  - 只把随序列长度增长的状态称为 growing KV
  - MLA 或压缩 KV 必须按实际 cache layout 计算
  - 固定 recurrent state 与 growing KV 分开记账
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
  - kv-cache
---
# KV Cache Model

> KV Cache Model 回答“序列增长会增加多少状态”。它与 [[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层级]] 分工明确：本页算大小与增长率，Hierarchy 页决定状态放在哪里、何时迁移。

## 基本定义

对于传统 MHA / GQA / MQA，若每个 growing attention layer 缓存：

- K
- V

每个 KV head 维度为 `D`，KV head 数为 `H_kv`，缓存元素字节数为 `b`：

```text
kv_bytes_per_token_per_layer
= 2 × H_kv × D × b
```

其中前面的 2 对应 K + V。

若 growing attention layer 数为 `L_grow`：

```text
growing_kv_bytes_per_token
= L_grow × 2 × H_kv × D × b
```

长度为 `S` 的单序列：

```text
growing_kv_bytes_per_sequence
= S × L_grow × 2 × H_kv × D × b
```

## MHA / GQA / MQA

### MHA

```text
H_kv = H_q
```

所以 KV 状态随 query head 数一起增长。

### GQA

```text
H_kv < H_q
```

KV 状态由 `H_kv` 决定，而不是 `H_q`。

### MQA

可视为：

```text
H_kv = 1
```

因此同 hidden/head_dim 条件下，growing KV 明显低于 MHA。

## Batch 与并发

不同序列长度时不能简单用：

```text
batch × max_sequence_length
```

代替真实已分配 token 数。

更一般地：

```text
total_growing_kv
= Σ_i allocated_tokens_i
  × kv_bytes_per_token
```

如果 runtime 使用 block/page allocator，还需要考虑：

- rounded allocation
- partially filled blocks
- prefix sharing
- copy-on-write
- metadata

因此“逻辑 KV bytes”和“allocator resident bytes”必须分开。

## MLA / Compressed KV

MLA 或其他 compressed-cache 结构不能硬套 MHA/GQA 公式。

统一方法是先确定实际保存的 cache representation：

```text
cache_scalars_per_token_per_layer
```

然后：

```text
kv_bytes
= tokens
× growing_layers
× cache_scalars_per_token_per_layer
× bytes_per_scalar
+ cache_metadata
```

若官方 config / inference implementation 无法唯一确定 cache layout，则结果必须为 unknown。

## Hybrid Attention

混合模型可能同时包含：

- full / global attention
- local / sliding-window attention
- linear attention
- SSM / recurrent blocks

需要分别记账。

### Growing global KV

随总 context length 增长。

### Sliding-window KV

若窗口为 `W`：

```text
resident_tokens_per_layer
<= min(sequence_length, W)
```

因此容量有上界，不再随超长 context 无限增长。

### Fixed recurrent state

Linear attention / SSM 可能保留固定 state，其大小通常：

```text
O(layers × state_size)
```

而不是 `O(sequence_length)`。

固定 state 不进入 growing KV 字段，但必须进入 [[system/memory/model-memory-accounting|Memory Accounting]]。

## Qwen3.8-27B 示例

[[models/Qwen/qwen3.8-27b|Qwen3.8-27B]] 当前模型页已经给出：

- 16 个 growing Gated Attention layers
- 4 KV heads
- head_dim = 256
- FP8 cache = 1 byte/scalar

因此：

```text
bytes/token
= 16 × 2 × 4 × 256 × 1
= 32,768 bytes/token
```

64K：

```text
65,536 × 32,768
= 2,147,483,648 bytes
= 2 GiB
```

这与模型页的统一派生字段一致，也验证了本页公式口径。

## KV Write Traffic

每新增一个 token，至少会产生新的 cache state：

```text
kv_write_bytes_per_new_token
≈ growing_kv_bytes_per_token
```

但实际写流量还可能包含：

- metadata
- block initialization
- quantization scale
- layout conversion
- replication

因此公式给的是 payload baseline。

## KV Read Traffic

Decode 的 KV read 量不能直接等同于 resident capacity。

对于 full attention，通常会读取与当前可见 context 相关的历史 cache；但实际 bytes 取决于：

- attention type
- window / sparsity
- cache layout
- kernel tiling
- on-chip reuse
- sharding

所以：

```text
resident_kv_bytes
!= automatically kv_read_bytes_per_step
```

带宽问题交给 [[system/memory/memory-bandwidth-model|Memory Bandwidth Model]]。

## Precision 与 Metadata

如果 KV 使用 FP16/BF16/FP8/INT8 等格式，payload bytes/scalar 不同。

量化 cache 还可能有：

- scale
- zero point
- block metadata

因此：

```text
allocated_kv_bytes
= payload_bytes
+ quant_metadata
+ allocator_overhead
```

不能只改 `bytes_per_scalar` 就宣称得到完整 runtime 占用。

## Sharding

TP / CP 等策略可能让 KV 在多个设备间：

- shard
- replicate
- redistribute

所以 per-device KV 应从 global logical state 经过实际 partition 计算。

```text
global_kv_bytes
→ partition rule
→ per_device_kv_bytes
```

不能无条件写成 `global / device_count`。

## 与内存层级的双向关系

大小模型回答：

```text
how much state?
how fast does it grow?
```

[[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层级]] 回答：

```text
where does it live?
when does it move?
is retrieve cheaper than recompute?
```

任何 offload / remote KV 方案都必须同时满足两边。

## 输出

- `growing_kv_bytes_per_token`
- `growing_kv_bytes_per_sequence`
- `fixed_attention_state_bytes`
- `per_device_kv_bytes`
- `kv_growth_rate_bytes_per_token`

输出必须记录 attention/cache layout、precision、scope 与 allocator assumption。

## 直接来源

本页主要定义通用 cache accounting。Qwen3.8-27B 的数值示例直接引用仓库 canonical 模型页及其 Evidence，不在本页复制新的外部事实。
