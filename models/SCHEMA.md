# Model Schema V0.1

Model V0.1 只记录“模型本身的可验证事实 + 与 AI Infra 强相关的架构特征”。Markdown 是唯一事实源，YAML frontmatter 是机器可读索引。

## Model

```yaml
---
schema_version: model-v0.1
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

## 字段

- `name`：模型标准名称。
- `object_type`：V0.1 固定为 `model`。
- `organization`：模型发布/维护组织。
- `family`：所属模型家族；无法确认时为 `null`。
- `status`：`preview`、`released`、`deprecated`、`retired`、`unknown`。
- `release_date`：首次公开发布日；无法确认时为 `null`。
- `architecture.backbone`：例如 `decoder-only`、`encoder-decoder`、`causal-encoder-decoder`。
- `architecture.sparsity`：例如 `dense`、`moe`、`hybrid`。
- `architecture.attention`：例如 `mha`、`gqa`、`mla`、`sparse-mla`、`hybrid-linear-attention`。
- `parameters.total`：模型总参数量，使用整数；公开资料无法确定时为 `null`。
- `parameters.active`：单 token 典型激活参数量，使用整数；若输入/输出不对称或定义不唯一则为 `null`，在正文说明。
- `context_length`：官方权重/配置的原生最大文本上下文 token 数；只有扩展方案而非原生值时，不回填扩展值。
- `kv_cache_64k_fp8_bytes`：按下述统一口径推导的 64K FP8 KV Cache 字节数；无法从公开架构确定时为 `null`。
- `modalities`：仅允许 `text`、`image`、`audio`、`video`。
- `weights`：canonical 权重/model repo；无公开权重时为 `null`。
- `snapshot.revision`：绑定具体权重 revision 时填写，否则为 `null`。
- `snapshot.as_of`：事实核验日期。
- `updated`：页面更新时间。

## `kv_cache_64k_fp8_bytes` 统一口径

这是一个**架构派生指标**，用于横向比较模型在长上下文下的 KV 状态压力，不代表某个推理引擎的实测显存占用。

固定假设：

- batch = 1。
- 文本序列长度 = 65,536 tokens。
- KV 值按 FP8 计，每个缓存标量 1 byte。
- 只计算会随序列长度增长的 attention KV / latent-KV 状态。
- 不计模型权重、activation、输出 buffer、量化 scale/metadata、block allocator 碎片。
- 不计 sparse indexer 的辅助 key、候选索引、视觉编码器状态。
- 不计 linear-attention / SSM 的固定 recurrent/conv state，也不计固定窗口 local cache；这些应在正文另行说明。
- MHA/GQA 按 `tokens × growing_layers × 2 × kv_heads × head_dim`。
- MLA / compressed-KV 按官方配置实际保存的 latent/cache 表示计算，不能硬套 MHA 公式。
- 无法从官方 config / inference implementation 唯一确定 cache layout 时必须填 `null`。

因此该字段更准确地说是“**64K 时序列长度增长部分的 FP8 KV footprint**”。

## Markdown 固定结构

```text
# Model Name
> 一句话定位

## 核心规格
## 架构特征
## AI Infra 关注点
## 版本与边界
## 关联项目
## 直接来源
```

`核心规格` 与 `架构特征` 的事实必须使用 `[S1]` 形式关联 `直接来源`。`AI Infra 关注点` 可以写由架构直接导出的系统影响；进一步推断必须明确标记为“分析判断”。

## 边界

Model 页不记录 TTFT、TPOT、tokens/s、推荐 GPU、TP/EP 配置、软件兼容矩阵或成本。这些都依赖 Model × Software × Hardware × Workload，不是模型固有属性。

同样，不把系统设计提案写成模型事实。未知值保持 `null`，不从相近型号或第三方估算回填。
