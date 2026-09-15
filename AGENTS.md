# ai_infra_docs 协作约定

## 任务开始

- 先运行 `git status --short`，记录已有修改和未跟踪文件。已有改动属于当前工作，不得回退、覆盖或批量清理。
- 芯片研究任务先动态扫描仓库一级厂商目录和其中的 Markdown 文件，任务清单以扫描结果为准，不使用硬编码厂商名单；软件研究任务按 `software/` 的架构层级和现有 MOC/概念节点确定边界。
- 把研究截止日期、目标目录、允许修改的文件、交付字段和完成条件写进每个子代理任务。

## 代理分工

- 主代理负责目录扫描、批次调度、跨厂商整合、根级覆盖矩阵、跨厂商专题、最终 Markdown 汇总和 Git 验收。
- `vendor_researcher` 一次只负责主代理指定的一个厂商目录。它可以修改该目录唯一的总描述文档和芯片/芯片家族及强绑定产品拆分页；非中国厂商使用 `<vendor>-overview.md`，中国厂商使用 `<中文厂商名>-概览.md`，不得新建平行索引或跨芯片边界页，不得修改根级汇总或其他厂商目录。
- `evidence_reviewer` 只读复核研究结果，返回文件位置、原始来源、问题类型、严重度和修正建议，不直接编辑文件。
- `presentation_editor` 只在主代理确认事实后更新指定的展示或汇总文件，不重新解释未经确认的硬件事实。
- 全局已有的 `luna_worker` 适合链接、索引和其他边界清楚的窄任务；委托时仍必须明确文件范围和验收条件。
- 同一个角色可以被多个厂商任务复用；每个厂商目录同时只能有一个写入负责人。

## 并行和交付

- 除主代理外同时运行的子代理不超过三个，子代理不得再派生子代理，除非主代理明确授权。优先并行执行探索、资料核验、链接检查和只读复核；共享根文件的写入必须串行。
- 一批任务完成后先收齐结果、处理冲突和标记失败项，再启动下一批。达到最低交付条件或资料已充分时停止扩展搜索。
- 子代理结束时必须返回：修改文件（或只读声明）、关键新增事实、直接来源链接、生命周期状态变化、未确认项、冲突和验证命令。

## 研究证据边界

- 优先使用厂商官方页面、数据手册、发布材料和会议原文；保留直接 URL、资料日期和核验日期。
- 分开记录官方事实、厂商宣称、独立测试、分析判断和“公开资料未确认”。不要用搜索摘要代替实际页面证据。
- 分开芯片、板卡、模块、服务器、机柜、集群和云服务；不得把 SDK、编译器或系统能力推导为未经证实的芯片硬件能力。
- 分开宣布、流片、工程样片、送样、量产、出货、客户部署和云可用性。未知字段保留“公开资料未确认”。
- 同一厂商先更新唯一总描述文档，再同步芯片及强绑定产品拆分页；拆页重排证据，不独立升级总描述文档没有支持的结论。总描述文档与拆分页之间使用内部链接，便于关系图谱回溯。

## Obsidian 知识图谱与内部链接

本仓库同时是 GitHub Markdown 文档库和 Obsidian Vault。文档组织不仅要考虑目录树，也要考虑“节点和边”。根入口为 [[00-ai-infra-map|AI Infra 知识图谱入口]]，软件入口为 [[software/README|AI Infra 软件栈地图]]，芯片入口为 [[chip/00-project-index|AI 芯片与基础设施资料库]]。

- 仓库内部的语义关系优先使用 Obsidian Wiki Link，统一写成 `[[vault/root/path|显示名]]`。路径从仓库根开始，不写 `.md`，以减少同名文件歧义和移动后的误解析。
- 外部官方资料、论文、博客和 GitHub 上游项目仍使用普通 URL，不要把外链伪装成 Wiki Link。
- 不要求每条关系都手写 A→B 和 B→A 两份链接。Obsidian Backlinks 已能显示反向边。需要显式双向导航时，应有明确语义，例如“厂商总览 ↔ 芯片页”“MOC ↔ 主题页”。
- 使用 MOC（Map of Content）和概念节点表达跨目录关系。MOC 负责“有哪些节点”，概念页负责“为什么这些节点有关”。不要为了让 Graph View 更密而制造无意义的全互联。
- 每个重要文档都应至少存在一条从 MOC、概念页或上级总览可达的入边，避免孤岛节点。新建软件文档时，至少连接 `[[software/README]]`、一个相关概念节点，并在适用时连接一个上游或下游组件。
- 软件项目之间应按真实架构关系建边，例如推理引擎 ↔ KV Cache、请求路由 ↔ 推理引擎、调度器 ↔ 设备资源；机制类关系优先连接到 `software/concepts/`，例如 P/D 分离、KV 生命周期、拓扑感知、异构推理。
- 芯片与软件跨域关系应通过“加速器资源模型”“拓扑感知调度”“异构推理”等概念节点连接，避免在每个芯片页机械链接所有软件。
- 新增或重命名文档时，检查 Wiki Link 的目标是否唯一。移动文件时同步更新显式路径链接，不能只依赖 Obsidian 的本地自动重写。
- 页面标题尽量唯一；需要多个常用名称时使用 YAML frontmatter 的 `aliases`。MOC、概念页建议使用 `tags` 标记角色，但不要把 tags 当成双链替代品。
- 不提交个人 Obsidian UI 状态，例如 `.obsidian/workspace.json`、`.obsidian/workspace-mobile.json` 及同类 workspace 文件。共享插件、主题或 Vault 设置只有在团队明确需要时才进入仓库。
- 整理任务完成后除常规 Markdown 检查外，还要检查 unresolved Wiki Links、重复 title/alias、明显孤立节点，并在 Obsidian Graph View 中做一次关系合理性抽查。

推荐的软件概念骨架：[[software/concepts/llm-serving-stack|LLM Serving 软件栈]]、[[software/concepts/pd-disaggregation|Prefill / Decode 分离]]、[[software/concepts/kv-cache-lifecycle|KV Cache 生命周期]]、[[software/concepts/topology-aware-scheduling|拓扑感知调度]]、[[software/concepts/accelerator-resource-model|加速器资源模型]]、[[software/concepts/heterogeneous-inference|异构推理]]。

## 在线知识图谱与派生数据

本仓库参考 `ai_infra_relationship` 的知识图谱发布方式，但图谱实体改为 AI Infra 文档本身，而不是人物关系。Markdown 是唯一事实源，在线图谱是从 Markdown 自动派生的视图。

- `scripts/build-knowledge-graph.py` 扫描仓库 Markdown，将文档建模为节点，将 Wiki Link / 本地 Markdown Link 建模为边，并生成 `generated/nodes.json`、`generated/edges.json`、`generated/metrics.json`、`generated/unresolved-links.json` 和 `generated/graph-summary.md`。
- `scripts/build-graph-explorer.py` 根据上述派生数据生成一个独立的关系探索器，支持 1-hop / 2-hop 邻域、领域/节点类型/关系类型筛选和最短路径。
- `.github/workflows/knowledge-graph-pages.yml` 在 GitHub Actions 中运行图谱构建，使用 Quartz 发布知识库，并把关系探索器挂到 `/graph-explorer/`。
- `generated/` 下的图谱文件是派生物，不作为人工编辑入口。需要改变关系时，应修改 Markdown、frontmatter 或内部链接，然后重新生成。
- 关系分类只能从真实文档边派生，不能为了图形更漂亮虚构边。当前允许的主要关系视图包括 `navigation`、`vendor-chip`、`concept-link`、`cross-domain` 和普通 `wikilink`。
- 新增顶级领域目录时，要同步检查 `build-knowledge-graph.py` 的 domain/kind 分类逻辑，并确认 Quartz workflow 会把该目录复制到站点内容目录。
- 在线图谱必须和 Obsidian 图谱保持同一事实源。禁止单独在前端 JSON 中手工添加只存在于网站、不存在于 Markdown 的实体关系。
- 本地验收至少运行 `python3 scripts/build-knowledge-graph.py --root . --output generated`，检查 unresolved links、isolated nodes 和 graph summary 是否出现异常跳变。

## 验收与 Git

- 研究或整理完成后，至少检查 Markdown 链接、Wiki Link、重复标题/alias、孤立节点、文件边界和 `git diff --check`。
- 涉及知识图谱结构的改动，还要运行图谱构建脚本并检查 `generated/graph-summary.md` 与 `generated/unresolved-links.json`，必要时通过 Pull Request 的 Pages 构建验证 Quartz 和 graph explorer。
- 主代理统一处理根级汇总和 Git 操作。只暂存本次任务文件，不使用 `git add -A`，不提交或发布未授权的外部变更。
