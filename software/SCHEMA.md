# Software Schema V0.1

Software V0.1 只定义两类对象：`project` 与 `concept`。Markdown 是唯一事实源，YAML frontmatter 是机器可读索引。

## Project

```yaml
---
schema_version: software-v0.1
name: vLLM
object_type: project
category: inference-engine
organization: vllm-project
status: active
repo: https://github.com/vllm-project/vllm
docs: https://docs.vllm.ai/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - continuous-batching
  - paged-kv-cache
integrations:
  - lmcache
backends:
  - nvidia
updated: 2026-09-15
---
```

### 字段

- `name`：项目标准名称。
- `object_type`：V0.1 仅允许 `project` 或 `concept`。
- `category`：项目主分类。V0.1 推荐 `inference-engine`、`distributed-serving`、`kv-cache`、`scheduler`、`device-resource`、`compiler`、`communication`、`runtime`、`other`。
- `organization`：主要维护组织；未知为 `null`。
- `status`：`active`、`maintenance`、`deprecated`、`archived`、`unknown`。
- `repo` / `docs`：官方入口；没有独立入口时为 `null`。
- `snapshot.version` / `snapshot.commit`：本页绑定的软件版本或提交；未固定时为 `null`。
- `snapshot.as_of`：事实快照日期，必填。
- `capabilities`：已确认核心能力的 kebab-case 标识。
- `integrations`：已确认存在明确集成关系的项目 slug。
- `backends`：已确认存在支持路径的硬件/平台后端。

## Concept

```yaml
---
schema_version: software-v0.1
name: Prefill / Decode Disaggregation
object_type: concept
category: serving-architecture
updated: 2026-09-15
---
```

Concept 不记录版本、后端和 capability matrix，只解释稳定机制。

## Project Markdown 固定结构

```text
# Name
> 一句话定位

## 核心能力
## 边界
## 集成与后端
## 关联项目
## 版本快照
## 直接来源
```

`集成与后端` 只写可确认的集成事实；`关联项目` 可以放同层对照、上下游或强相关项目，但不能把“相关”偷换成“已集成”。

## Concept Markdown 固定结构

```text
# Name
> 一句话定义

## 问题
## 核心机制
## 判断要点
## 相关项目与概念
```

## 规则

1. 一个项目一页。
2. 软件事实必须带 `snapshot.as_of`；软件会变化，不能把“当前”写成永恒事实。
3. 未确认值使用 `null` 或不进入列表，不猜测。
4. `capabilities` 只记录可由当前来源确认的能力。
5. `integrations` 只说明存在集成，不自动表示稳定、原生或高性能。
6. `backends` 只说明存在支持路径，不自动表示功能对齐或生产成熟。
7. 项目事实写 `projects/`，跨项目原理写 `concepts/`，避免重复维护。
8. 仓库内软件引用必须使用 canonical Wiki Link：`[[software/projects/<slug>|Name]]`；概念引用使用 `[[software/concepts/<slug>|Name]]`。
9. 双链规则：若 A 项目页在 `集成与后端` 或 `关联项目` 中链接仓库内 B 项目，则 B 项目页也必须保留指向 A 的反向 Wiki Link。frontmatter 的 `integrations` 仍按事实语义填写，不为了对称而伪造集成。
10. 不为了 Graph View 制造无意义的全互联；只保留能说明架构关系的边。
