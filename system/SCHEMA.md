---
title: System Schema V0.1
tags:
  - system
  - schema
updated: 2026-09-25
---

# System Schema V0.1

System V0.1 用于描述连接 Model / Workload 与 Hardware 的稳定系统概念。它不是软件项目数据库，也不是性能 benchmark schema。目标是让每个 System Concept 明确回答：

1. 消费什么输入；
2. 约束是什么；
3. 能推导或解释什么输出；
4. 依赖哪些假设；
5. 影响哪些 AI Infra 层；
6. 页面中的外部事实由什么 Evidence 支撑。

Markdown 仍是唯一事实源，YAML frontmatter 提供机器可读索引。仓库级校验由 `scripts/validate-repo.py` 执行。

## 最小对象

```yaml
---
schema_version: system-v0.1
name: Example System Concept
object_type: concept
category: memory
inputs:
  - model.parameters.total
  - workload.sequence_length
constraints:
  - memory-capacity
  - memory-bandwidth
outputs:
  - required_memory_bytes
assumptions:
  - name: precision
    value: fp8
    scope: example
related_layers:
  - model
  - workload
  - memory
  - accelerator
evidence:
  S1:
    url: https://example.com/reference
    source_type: official-doc
    accessed: 2026-09-25
updated: 2026-09-25
---
```

## 必填字段

System Concept 必须包含：

- `schema_version`：V0.1 固定为 `system-v0.1`。
- `name`：唯一、非空的概念名称。
- `object_type`：固定为 `concept`。
- `category`：稳定领域分类，使用 kebab-case。
- `inputs`：概念消费的事实或 workload 输入。
- `constraints`：该概念建模的限制、瓶颈或资源约束。
- `outputs`：该概念能直接推导、估计或解释的结果。
- `assumptions`：推导成立所依赖的假设；没有额外假设时使用空 list。
- `related_layers`：该概念连接的 AI Infra 层。
- `evidence`：页面级外部事实来源；没有外部经验事实时允许空 mapping。
- `updated`：最后核验日期，格式为 `YYYY-MM-DD`。

## 字段语义

### inputs

`inputs` 是非空字符串列表。命名优先使用稳定、可读的 dotted path 或 workload 名称，例如：

- `model.parameters.total`
- `model.context_length`
- `workload.batch_size`
- `workload.concurrency`
- `hardware.memory.bandwidth_tb_s`

Schema 不要求这些路径现在都对应一个已经机器化的字段，但页面正文必须解释其语义和单位。

### constraints

`constraints` 是非空字符串列表，描述该概念关注的物理或系统限制。例如：

- `memory-capacity`
- `memory-bandwidth`
- `interconnect-bandwidth`
- `latency`
- `failure-domain`
- `software-availability`

约束名称使用 kebab-case；不要把产品名或软件项目名写成 constraint。

### outputs

`outputs` 是非空字符串列表。输出可以是：

- 可计算指标，如 `required_memory_bytes`、`transfer_bytes`；
- 分类判断，如 `bottleneck_class`；
- placement / hierarchy 约束，如 `placement_constraints`。

输出名表示“这个概念能够产生什么”，不代表仓库当前已经实现自动计算器。

### assumptions

`assumptions` 必须是 list。每项可以是：

- 简短字符串，用于纯定性概念；
- mapping，至少包含 `name`，并可附带 `value`、`unit`、`scope`、`note`。

所有会改变数值结果的假设都必须显式出现，不能藏在公式旁边。

### related_layers

`related_layers` 是非空列表，只允许以下稳定层：

- `model`
- `workload`
- `compute`
- `memory`
- `parallelism`
- `communication`
- `topology`
- `scheduling`
- `accelerator`
- `network`
- `storage`
- `power`
- `reliability`

它用于描述跨层依赖，不替代 Wiki Link。真正的语义边仍应通过正文内部链接表达。

### evidence

`evidence` 必须是 mapping。Key 使用 `S1`、`S2` 等 Source ID。每项至少包含：

- `url`：HTTP(S) URL。

建议同时记录：

- `source_type`：如 `official-doc`、`official-code`、`paper`、`standard`、`benchmark`、`third-party-analysis`；
- `accessed`：核验日期。

System Concept 经常包含第一性原理推导或仓库内部分析。此类推导本身不需要伪造外部 Evidence，因此允许：

```yaml
evidence: {}
```

但只要正文写入厂商规格、协议数字、标准行为、benchmark 数据等外部事实，就必须增加直接来源，并在正文相应事实附近使用 `[S1]` 形式引用。

## Markdown 建议结构

```text
# Concept Name
> 一句话定义

## 输入
## 约束模型
## 输出
## 假设与边界
## 与其他层的关系
## 直接来源
```

不是每个旧页面都必须立即改成完全相同的标题，但新建概念页应优先采用该结构。

## 事实与推导边界

System 页面必须区分：

```text
原始事实
→ 明确假设
→ 公式 / 系统机制
→ 派生结果
```

禁止：

- 把第三方 benchmark 写成硬件固有能力；
- 把某个软件项目的当前实现写成系统必然规律；
- 把系统聚合性能回填到 Chip Schema；
- 把 Model × Workload × Hardware 的结果写成模型固有属性；
- 在缺少输入时用相邻 SKU、相邻模型或经验值静默补齐。

## 与其他 Schema 的边界

- [[models/SCHEMA|Model Schema]]：记录模型固有、可验证事实。
- [[chip/SCHEMA|Chip Schema]]：记录硬件对象及产品边界。
- System Schema：记录模型/workload 如何映射到资源、通信、拓扑与硬件约束。
- 软件项目、社区、能力和集成的 canonical 事实由 [ai_infra_relationship](https://github.com/MarsChan8293/ai_infra_relationship) 维护。

## CI

至少运行：

```bash
python3 scripts/validate-repo.py --root . --report generated/validation.json
python3 scripts/build-knowledge-graph.py --root . --output generated
```

Validator 必须拒绝缺失必填字段、非法日期、非法 related layer、非法 Evidence URL 或无法解析的严格内部链接。
