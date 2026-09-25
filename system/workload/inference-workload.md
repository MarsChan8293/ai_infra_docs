---
schema_version: system-v0.1
name: Inference Workload
object_type: concept
category: workload-model
inputs:
  - model.intrinsic_facts
  - request.prompt_tokens
  - request.output_tokens
  - workload.request_rate
  - workload.concurrency
  - workload.prefix_reuse
  - workload.sla
constraints:
  - ttft
  - tpot
  - end_to_end_latency
  - throughput
  - queueing
  - capacity
outputs:
  - prefill_workload
  - decode_workload
  - active_sequence_envelope
  - token_arrival_rate
  - latency_budget
assumptions:
  - 在线与离线推理必须分开描述
  - batch、concurrency、request rate 不能互相替代
  - prefix reuse 未知时不默认命中
related_layers:
  - model
  - workload
  - compute
  - memory
  - parallelism
  - communication
  - topology
  - scheduling
  - accelerator
evidence: {}
updated: 2026-09-25
tags:
  - system
  - workload
  - inference
---
# Inference Workload

> Inference Workload 把“一个模型被怎样服务”拆成请求到达、Prefill、Decode、排队、复用和 SLA。它不描述某个具体推理引擎版本，而是给下游 Compute / Memory / Communication 提供稳定输入。

## 在线与离线

在线服务重点约束：

- request arrival rate
- concurrency
- TTFT
- TPOT / inter-token latency
- end-to-end latency
- percentile / deadline
- prefix reuse
- cancellation / early stop

离线批处理重点约束：

- total token volume
- batch construction
- throughput
- completion time
- utilization

同一个模型在两类 workload 下的最优 batch、并行和硬件映射可能完全不同。

## 请求分解

一个自回归请求至少分成：

```text
request
  ├─ prompt tokens  → Prefill
  └─ output tokens  → repeated Decode steps
```

定义：

```text
S_in  = prompt_tokens
S_out = output_tokens
```

若没有 prefix reuse：

```text
prefill_tokens = S_in
decode_steps   ≈ S_out
```

若存在复用，则必须分开：

```text
logical_prompt_tokens
reused_prompt_tokens
recomputed_prompt_tokens
```

只有 `recomputed_prompt_tokens` 进入新的 Prefill work。

## Arrival Rate 与 Concurrency

若平均到达率为：

```text
lambda = requests / second
```

平均系统停留时间为 `W`，稳定条件下可用 Little's Law 的量纲关系理解并发：

```text
L ≈ lambda × W
```

这里仅用于说明 arrival、latency、concurrency 的关系，不把平均关系当成 tail-latency 保证。

实际系统还会受 burst、排队策略、长度分布和 cancellation 影响。

## Batch 与 Concurrency

必须区分：

- concurrency：同时活跃请求数；
- scheduler batch：某个调度轮次选中的请求数；
- kernel batch / effective M：某个算子实际同时处理的 token rows。

因此：

```text
concurrency = 64
```

不能直接推出：

```text
GEMM M = 64
```

Continuous batching、不同序列长度和请求完成都会让 batch 动态变化。

## Prefill Workload

Prefill 的主要输入包括：

- recomputed prompt tokens
- request batch
- sequence length distribution
- prefix reuse
- multimodal pre-processing if applicable

其输出包括：

- first-token-ready state
- growing KV / recurrent state
- Prefill compute and memory traffic

Prefill 对 TTFT 预算非常敏感。

## Decode Workload

Decode 每个调度 step 通常为每个 active sequence 生成少量新 token。

需要记录：

- active sequences
- current context length distribution
- output length distribution
- EOS / early-stop behavior
- per-step batch
- KV growth
- sampling policy

因此 Decode workload 不是“固定 batch × 固定长度”的静态矩阵。

## SLA

### TTFT

TTFT 至少包含：

```text
queue
+ scheduling
+ input / state transfer
+ prefill
+ first decode / sampling boundary
```

具体边界必须在 benchmark 中说明。

### TPOT

TPOT 应说明：

- mean / P50 / P95 / P99
- steady state or all tokens
- 是否包含 queue
- batch / concurrency
- context / output length

### Throughput

吞吐至少明确单位：

- output tokens/s
- total tokens/s
- requests/s

三者不能互换。

## 长度分布

只给平均 prompt/output 长度通常不足以估算 capacity，因为：

- KV capacity 与长尾 active context 有关；
- Prefill cost 对长 prompt 非线性；
- tail request 会影响 batch shape；
- P99 latency 由长尾和排队共同影响。

建议 workload profile 同时保留代表 percentile 或 bucket。

## Prefix Reuse

定义：

```text
reuse_ratio
= reused_prompt_tokens / logical_prompt_tokens
```

但系统收益不能只看 ratio，还取决于：

- cache hit locality
- state retrieval cost
- cache capacity
- invalidation
- tenant isolation

未知时设置为 `null`，不默认“有 cache 就一定命中”。

## 输出

Inference Workload 规范化输出：

- `prefill_workload`
- `decode_workload`
- `active_sequence_envelope`
- `token_arrival_rate`
- `latency_budget`

这些输出由：

- [[system/compute/prefill-vs-decode|Prefill vs Decode]]
- [[system/memory/kv-cache-model|KV Cache Model]]
- [[system/memory/memory-bandwidth-model|Memory Bandwidth Model]]
- [[system/parallelism/parallelism-overview|Parallelism Overview]]

进一步消费。

## 边界

1. 本页不维护 vLLM、SGLang 等项目级事实。
2. SLA 是 workload 输入，不是硬件固有属性。
3. benchmark 必须绑定 model + workload + software + hardware + topology。
4. 未知 batch、reuse 或 latency 分布保持未知。

## 直接来源

本页定义仓库内部 inference workload 语义和量纲关系，没有引入外部 benchmark 或厂商规格，因此 `evidence: {}`。
