# Software Schema V0.2

`ai_infra_docs/software` 在项目迁移后只承担两类职责：

1. `concept`：技术概念仍由本仓库作为 canonical source。
2. `project-redirect`：保留旧 `software/projects/<slug>` 路径作为兼容入口，canonical project 事实已经迁入 `ai_infra_relationship`。

Markdown 仍是本仓库知识图谱的事实源，但 **Software Project 的 canonical 事实源不再位于本仓库**。

## Concept

```yaml
---
schema_version: software-v0.2
name: Prefill / Decode Disaggregation
object_type: concept
category: serving-architecture
updated: 2026-09-19
---
```

Concept 用于解释跨项目稳定机制。Concept 不迁移到 `ai_infra_relationship`，也不要求为每个概念建立 relationship 侧一级实体。

## Project Redirect

```yaml
---
schema_version: software-redirect-v0.1
name: vLLM
object_type: project-redirect
canonical: https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/vllm-project/vLLM/vLLM.md
updated: 2026-09-19
---
```

Project redirect 只做三件事：

- 保留旧 Wiki Link / Quartz route，避免 models、chip、concept 等页面出现 404。
- 明确 canonical project 页面在 `ai_infra_relationship`。
- 为读者提供稳定外链，不再复制项目能力、集成、后端、版本快照、维护者或组织关系。

### Redirect 必填字段

- `schema_version: software-redirect-v0.1`
- `name`
- `object_type: project-redirect`
- `canonical`：必须是指向 `MarsChan8293/ai_infra_relationship` 的 http(s) URL。
- `updated`

### Redirect 正文

推荐保持极薄：

```markdown
# Name

> 此项目的 canonical 记录已迁移到 ai_infra_relationship。

- Canonical project: <URL>
- 本仓库继续维护软件概念、模型和芯片等技术资料。
```

不要在 redirect 页继续维护 `category / organization / status / repo / docs / snapshot / capabilities / integrations / relations / backends`。这些字段属于 relationship Project v3 或项目正文。

## 迁移边界

- `software/projects/*`：兼容 redirect，不再是项目事实 canonical source。
- `software/concepts/*`：继续由本仓库维护。
- `software/COMMUNITIES.md`：可以作为导航视图，但不得成为已迁项目的第二份 canonical 项目数据库。
- `chip/*`、`models/*`：不受此次 Project 迁移影响。
- models / chip / concepts 对 `software/projects/*` 的旧 Wiki Link 可以继续存在，因为 redirect 路径保持稳定。

## 维护规则

1. 新的软件项目事实优先写入 `ai_infra_relationship` canonical project，不在 docs 新建第二份完整项目页。
2. docs 如需引用项目，优先链接现有 `software/projects/<slug>` redirect，以保持 Obsidian / Quartz 本地可达。
3. Concept 仍使用本仓库内部 Wiki Link，并可链接 project redirect。
4. Project redirect 不要求 page-level / claim-level 项目事实证据；其唯一需要核验的事实是 canonical URL。
5. `scripts/validate-repo.py` 负责验证 redirect schema、canonical URL、Concept/Model 规则和 Wiki Link 完整性。
