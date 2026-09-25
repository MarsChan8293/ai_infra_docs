---
schema_version: system-v0.1
name: AI Workload Model
object_type: concept
category: workload-model
inputs:
  - model.intrinsic_facts
  - request.prompt_tokens
  - request.output_tokens
  - workload.batch_size
  - workload.concurrency
  - workload.request_rate
  - workload.sequence_length
  - workload.context_reuse
  - workload.sla
  - training.global_batch
  - training.micro_batch
  - training.checkpoint_interval
constraints:
  - latency
  - throughput
  - capacity
  - arrival-rate
  - service-level-objective
outputs:
  - normalized_workload_profile
  - token_volume
  - concurrency_envelope
  - latency_budget
  - throughput_target
assumptions:
  - Workload 描述运行条件，不修改 Model intrinsic facts
  - 未明确的 batch、并发、SLA 或序列长度不得由相邻案例静默补齐
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
---
# AI Workload Model

> AI Infra 不是由“模型名称”单独决定的。同一个模型在不同 prompt 长度、输出长度、batch、并发、请求率和 SLA 下，会形成完全不同的计算、内存、通信与调度需求。Workload Model 的职责是把这些运行条件显式化。

## 为什么需要独立 Workload 层

[[models/00-model-index|Model]] 页面描述模型固有事实，例如参数量、attention 结构、上下文上限和权重来源；Workload 描述一次部署、服务或训练任务如何使用模型。

两者必须分开：

```text
Model intrinsic facts
        +
Runtime workload
        ↓
System requirements
```

例如，`context_length = 128K` 是模型能力边界；某个服务请求实际使用 `8K prompt + 1K output` 则是 workload。把二者混写会把“最大能力”误当成“实际资源需求”。

## 输入

Workload Profile 至少应能表达以下维度。

### 推理请求

| 输入 | 含义 | 单位/口径 |
|---|---|---|
| `prompt_tokens` | 单请求 Prefill 输入长度 | token / request |
| `output_tokens` | 单请求 Decode 输出长度 | token / request |
| `sequence_length` | 某阶段实际参与计算的序列长度 | token |
| `batch_size` | 同一步骤被共同执行的序列/请求数 | sequence 或 request |
| `concurrency` | 同时处于系统中的活跃请求数 | request |
| `request_rate` | 到达率 | request/s |
| `context_reuse` | prompt/prefix 可复用比例或命中条件 | ratio / policy |
| `priority` | 服务优先级或队列类别 | class |

### 服务目标

| 输入 | 含义 |
|---|---|
| `ttft_target` | Time To First Token 目标 |
| `tpot_target` | Time Per Output Token 目标 |
| `latency_target` | 请求整体延迟目标 |
| `throughput_target` | token/s、request/s 或训练 samples/s 目标 |
| `availability_target` | 若任务要求，明确可用性目标与统计窗口 |

SLA 字段必须带清楚的统计口径。平均值、P95、P99 和 hard deadline 不是同一个约束。

### 训练任务

训练 workload 还需要表达：

- global batch size
- micro batch size
- sequence length / packing 策略
- gradient accumulation steps
- training steps / token budget
- checkpoint interval
- 容错与重启策略

这些字段将在任务 `WL-003` 中进一步细化。

## 规范化 Workload Profile

System 层后续的计算、内存和通信模型应消费一份明确的 Workload Profile，而不是直接从自然语言猜测运行条件。

概念上可以表示为：

```yaml
workload:
  kind: inference
  mode: online
  prompt_tokens: 8192
  output_tokens: 1024
  batch_size: null
  concurrency: 64
  request_rate_rps: 8
  context_reuse_ratio: null
  sla:
    ttft_ms: null
    tpot_ms: null
    percentile: null
```

这里的数字只是数据结构示例，不代表推荐配置。真正的 workload 必须来自明确场景或用户输入。

## 派生量

Workload Model 本身只做低风险、定义清晰的归一化派生。

### 每请求 Token 量

```text
tokens_per_request
= prompt_tokens + output_tokens
```

### 时间窗口内请求量

若 arrival rate 为 `λ requests/s`，观察窗口为 `T seconds`：

```text
requests_in_window
= λ × T
```

### 时间窗口内 Token 量

在不考虑 prefix reuse、early stop、padding 和动态 batching 的简化条件下：

```text
tokens_in_window
≈ requests_in_window
× (prompt_tokens + output_tokens)
```

这只是 workload 规模量，不是计算 FLOPs。真实 FLOPs 由 [[system/compute/README|Compute Model]] 根据 Model 架构进一步推导。

## Batch、Concurrency 与 Request Rate 不是同一个量

这三个概念经常被混在一起：

- **batch size**：某个执行步骤同时被 kernel/graph 处理的序列数量；
- **concurrency**：系统中同时活跃的请求数量；
- **request rate**：单位时间新进入系统的请求数量。

`concurrency = 64` 不意味着每一步的 batch size 恒为 64。Continuous batching、不同序列长度、请求完成和排队都会使实际 batch 动态变化。

因此 System 推导不得用 concurrency 直接替代 batch size，除非显式声明近似条件。

## Prefill 与 Decode 的 workload 分解

在线 LLM 推理至少拆成两个角色：

```text
Request
  ├─ Prefill: consume prompt tokens
  └─ Decode: generate output tokens iteratively
```

Prefill 和 Decode 的算术强度、权重读取模式、KV 访问量、batch 行为与 latency budget 不同。后续：

- `CMP-003` 建立 Prefill vs Decode Compute Model；
- `SRV-004` 建立 P/D 分离条件；
- `SRV-005` 建立 KV transfer 的 break-even。

## Context Reuse

Prefix / context reuse 会把“逻辑 prompt 长度”与“需要重新计算的 prompt 长度”分开。

至少应区分：

```text
logical_prompt_tokens
recomputed_prompt_tokens
reused_prompt_tokens
```

在没有明确 cache hit / reuse 信息时，不默认存在复用收益。复用机制将在 `SRV-003` 中建模。

## SLA 如何进入系统约束

Workload Profile 的 SLA 不直接告诉系统“用哪张卡”，而是向下游施加预算：

```text
TTFT target
→ Prefill compute + queue + transfer budget

TPOT target
→ Decode compute + memory + communication budget

Throughput target
→ sustained compute / memory / network demand
```

因此硬件选择应来自 Model × Workload × System 的联合约束，而不是单独从模型名称推出。

## 输出

本概念输出的是规范化 workload 语义，而不是硬件推荐：

- `normalized_workload_profile`
- `token_volume`
- `concurrency_envelope`
- `latency_budget`
- `throughput_target`

这些输出分别由后续 [[system/compute/README|Compute]]、[[system/memory/README|Memory]]、[[system/parallelism/README|Parallelism]]、[[system/communication/README|Communication]] 与 [[system/topology/README|Topology]] 模型消费。

## 假设与边界

1. Workload 字段描述运行条件，不修改模型固有事实。
2. 未给出的 workload 值保持未知，不自动套用“典型值”。
3. 最大 context length 不是实际 sequence length。
4. 厂商 benchmark 的 workload 只有在其 batch、序列、精度和并行条件明确时才能用于横向比较。
5. 性能结果属于 Model × Workload × Software × Hardware × System 的联合结果，不回填 Model Schema。
6. 本页不维护 vLLM、SGLang 等具体项目的版本能力；软件项目事实仍由 relationship 仓库维护。

## 与其他层的关系

- 模型事实：[[models/00-model-index|AI Model Index]]
- System Schema：[[system/SCHEMA|System Schema V0.1]]
- Memory：[[system/memory/README|Memory Model]]
- Compute：[[system/compute/README|Compute Model]]
- Parallelism：[[system/parallelism/README|Parallelism Model]]
- Communication：[[system/communication/README|Communication Model]]
- Topology：[[system/topology/README|Topology Model]]
- Hardware：[[chip/00-project-index|AI 芯片与基础设施资料库]]

## 直接来源

本页目前定义的是仓库内部的 workload 建模边界和第一性原理量纲关系，没有引入需要外部来源支撑的厂商规格、协议数字或 benchmark 数据，因此 `evidence: {}`。后续若加入外部事实，必须按 [[system/SCHEMA|System Schema V0.1]] 增加直接 Evidence。
