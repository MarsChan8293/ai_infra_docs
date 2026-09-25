# Model Schema V0.2

Model V0.2 记录“模型本身的可验证事实 + 与 AI Infra 直接相关的结构字段”。Markdown 仍是唯一事实源，YAML frontmatter 提供机器可读索引；运行时性能、并行配置和硬件推荐继续留在 System / Workload 层。

## Model

```yaml
---
schema_version: model-v0.2
name: Example-Model
object_type: model
organization: ExampleOrg
family: Example-Family
status: released
release_date: 2026-09-01
architecture:
  backbone: decoder-only
  sparsity: moe
  attention: hybrid
parameters:
  total: 100000000000
  active: 10000000000
structure:
  num_layers: 80
  hidden_size: 8192
  intermediate_size: null
  attention:
    num_attention_heads: 64
    num_key_value_heads: 8
    head_dim: 128
    growing_layers: 80
    kv_lora_rank: null
    qk_rope_head_dim: null
    sliding_window: null
  moe:
    num_experts: 128
    experts_per_token: 8
    shared_experts: 1
  recurrent:
    type: null
    layers: null
    state_size: null
context_length: 131072
kv_cache_64k_fp8_bytes: 1073741824
modalities:
  - text
weights: https://huggingface.co/example/model
snapshot:
  revision: null
  as_of: 2026-09-16
updated: 2026-09-16
---
```

## V0.2 设计原则

V0.2 不试图把所有模型配置复制进 frontmatter。只机器化会直接影响 AI Infra 推导、且能从 canonical config / paper / official implementation 唯一确认的字段。

规则：

1. 不从总参数量反推 hidden size、FFN size 或 layer 数。
2. 不从 expert 总数和 top-k 反推 active parameters。
3. 不从模型家族相邻 SKU 复制结构字段。
4. 不把 runtime 扩展后的 context 写成原生 `context_length`。
5. 无法唯一确认的字段填 `null`。
6. 正文 `[S1]` Evidence 仍是事实来源；frontmatter 只是索引，不创造新事实。

## 基础字段

- `name`：模型标准名称。
- `object_type`：固定为 `model`。
- `organization`：发布/维护组织。
- `family`：模型家族；无法确认时为 `null`。
- `status`：`preview`、`released`、`deprecated`、`retired`、`unknown`。
- `release_date`：首次公开发布日；无法确认时为 `null`。
- `architecture.backbone`：例如 `decoder-only`、`encoder-decoder`。
- `architecture.sparsity`：例如 `dense`、`moe`、`hybrid`。
- `architecture.attention`：高层 attention 类型，例如 `gqa`、`mla`、`hybrid-linear-attention`。
- `parameters.total`：总参数量整数或 `null`。
- `parameters.active`：单 token 典型 active parameter count；定义不唯一时为 `null`。

## structure

### 通用结构

- `structure.num_layers`：主要语言 backbone 的层数。
- `structure.hidden_size`：主 hidden dimension。
- `structure.intermediate_size`：dense MLP / canonical FFN intermediate size；MoE 或结构不唯一时可以 `null`。

这些字段必须是非负整数或 `null`。

### attention

`structure.attention` 必须是 mapping，固定保留以下字段：

- `num_attention_heads`
- `num_key_value_heads`
- `head_dim`
- `growing_layers`
- `kv_lora_rank`
- `qk_rope_head_dim`
- `sliding_window`

字段均为非负整数或 `null`。

其中：

- `growing_layers` 只统计会产生随序列长度增长 attention cache 的层。
- 对 GQA/MQA，KV 大小使用 `num_key_value_heads`，不能使用 query heads 代替。
- 对 MLA / compressed KV，优先记录实际 cache representation 的 `kv_lora_rank` / rope 部分，而不是硬套 K/V head 公式。
- `sliding_window` 表示固定 local window token 数；只有官方配置可确认时填写。

### moe

`structure.moe` 为 mapping 或 `null`。

MoE mapping 固定字段：

- `num_experts`
- `experts_per_token`
- `shared_experts`

Dense 模型使用：

```yaml
moe: null
```

如果模型明确是 MoE 但某字段未知，则保留 mapping 并将对应字段设为 `null`。

### recurrent

`structure.recurrent` 用于 linear attention / SSM / recurrent state：

- `type`：字符串或 `null`。
- `layers`：使用该 recurrent mechanism 的层数或 `null`。
- `state_size`：若公开 config 能唯一表达固定 state width，则记录；否则 `null`。

它只描述模型结构，不把 runtime tensor layout 当成模型事实。

## context_length

`context_length` 记录官方权重/配置的原生最大文本 context token 数。

只有 RoPE scaling、YaRN 或 runtime extension 的扩展值时，不回填扩展后的长度。

## kv_cache_64k_fp8_bytes

这是架构派生指标，表示 batch=1、65,536 tokens、FP8（1 byte/scalar）下，**随序列长度增长的 cache payload**。

固定边界：

- 不计 weight、activation、workspace。
- 不计 allocator 碎片与 quant metadata。
- 不计固定 recurrent / SSM state。
- 不计固定 sliding-window local cache。
- MHA/GQA：`tokens × growing_layers × 2 × kv_heads × head_dim`。
- MLA / compressed cache：按实际 latent/cache representation 计算。
- 无法唯一确认 cache layout 时填 `null`。

完整 runtime KV 占用由 [[system/memory/kv-cache-model|KV Cache Model]] 建模。

## modalities / weights / snapshot

- `modalities`：只允许 `text`、`image`、`audio`、`video`。
- `weights`：canonical weights/model repo，无公开权重时为 `null`。
- `snapshot.revision`：绑定具体 revision 时填写，否则 `null`。
- `snapshot.as_of`：事实核验日期。
- `updated`：页面更新时间。

## Markdown 固定结构

```text
# Model Name
> 一句话定位

## 核心规格
## 架构特征
## AI Infra 关注点
## 版本与边界
## 关联软件与系统
## 直接来源
```

`核心规格`、`架构特征` 中的事实必须通过 `[S1]` 等 Source ID 追溯到 `直接来源`。

## 与 System 的边界

Model 页不记录：

- TTFT / TPOT / tokens/s
- 推荐 GPU/NPU
- TP / PP / EP / CP 配置
- batch / concurrency
- runtime compatibility
- 成本

这些属于 Model × Workload × Software × Hardware × System 的联合结果。

System 使用以下页面消费 Model V0.2 字段：

- [[system/compute/transformer-compute-model|Transformer Compute Model]]
- [[system/memory/weight-memory|Weight Memory Model]]
- [[system/memory/kv-cache-model|KV Cache Model]]
- [[system/moe/moe-system-model|MoE System Model]]

未知值保持 `null`，不为了可计算性牺牲事实边界。
