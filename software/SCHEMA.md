# Software Schema V0.1

Software V0.1 继续只定义两类对象：`project` 与 `concept`。Markdown 是唯一事实源，YAML frontmatter 是机器可读索引。V0.1 的目标不是把所有事实塞进 YAML，而是让身份、分类、版本快照、能力、集成、后端、证据与关系都能被机器校验。

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
relations:
  alternative-to:
    - sglang
backends:
  - nvidia
updated: 2026-09-15
---
```

## Project 字段

- `name`：项目标准名称。
- `object_type`：V0.1 仅允许 `project` 或 `concept`。
- `category`：项目主分类。允许值：`inference-engine`、`distributed-serving`、`gateway`、`kv-cache`、`storage`、`communication`、`runtime`、`compiler`、`training`、`scheduler`、`device-resource`、`benchmark`、`ecosystem`、`optimization`、`other`。
- `organization`：canonical upstream namespace 或明确治理组织；不是主要贡献公司列表。无法确认时为 `null`。
- `status`：`active`、`maintenance`、`deprecated`、`archived`、`unknown`。
- `repo` / `docs`：官方入口；没有独立入口或无法确认 canonical 项目地址时为 `null`。
- `snapshot.version` / `snapshot.commit`：本页绑定的软件版本或提交；未固定时为 `null`。
- `snapshot.as_of`：事实快照日期，必填。
- `capabilities`：已确认核心能力的 kebab-case 标识。
- `integrations`：已确认存在明确集成关系的项目 slug；图谱构建时自动生成 `integrates-with` 关系。
- `relations`：可选的显式语义关系，不用于替代正文导航。
- `backends`：已确认存在支持路径的硬件/平台后端。

## 关系类型

`relations` 当前只允许以下类型：

- `integrates-with`
- `depends-on`
- `backend-for`
- `alternative-to`
- `extends`
- `implements`
- `managed-by`
- `related`

只有语义足够明确时才写 typed relation。无法确认关系性质时保留普通 Wiki Link，不为图谱分类强行猜测。

## Evidence

证据分两级：

1. **Page-level evidence（强制）**：每个 project 的 `## 直接来源` 至少有一个直接 `http(s)` 来源。CI 缺失即失败。
2. **Claim-level evidence（推荐并逐步迁移）**：在 `## 核心能力` 中使用 `[S1]`、`[S2]` 引用，在 `## 直接来源` 中定义同名 Source ID。

示例：

```markdown
## 核心能力

| 能力 | 说明 | 证据 |
|---|---|---|
| Continuous Batching | 动态组织活跃请求 | [S1] |
| Prefix Caching | 复用重复前缀 KV | [S1] |

## 直接来源

- [S1] https://docs.example.com/
- [S2] https://github.com/example/project
```

Validator 会检查 Evidence ID 是否闭环；未迁移到 claim-level 的旧页仍按 page-level evidence 验证，并在报告中标记覆盖率。

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

## 维护规则

1. 一个项目一页；软件事实必须带 `snapshot.as_of`。
2. 未确认值使用 `null` 或不进入列表，不猜测。
3. `capabilities`、`integrations`、`backends` 只记录当前来源可确认的事实。
4. 项目事实写 `projects/`，跨项目原理写 `concepts/`，上游社区/namespace 视图写 `COMMUNITIES.md`。
5. `organization` 表示上游 namespace / 治理组织；公司贡献关系另行表达。
6. 仓库内引用使用 canonical Wiki Link；目标路径采用 `software/projects/<slug>` 形式，避免 basename 歧义。
7. **不再要求人工维护镜像式双向链接。** Markdown 只写有语义的正向边；Obsidian Backlinks 与图谱构建器自动生成反向可达信息。只有确实需要双向导航、或关系本身对称时，才显式写双方链接。
8. 不为了 Graph View 制造无意义的全互联。
9. `scripts/validate-repo.py` 是 Software Schema 的执行层；Schema、Evidence、关系目标、Wiki Link 或分类不合法时 CI 应失败。
