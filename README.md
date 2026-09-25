---
title: ai_infra_docs 仓库说明
tags:
  - ai-infra
  - repository
---

# ai_infra_docs

本仓库聚焦 AI 芯片与硬件、模型架构，以及连接二者的系统约束。知识主线从“有哪些软件项目”调整为 **Model → System → Chip**：模型定义状态、计算与通信需求，系统层解释内存、拓扑、资源与异构执行约束，芯片层记录硬件事实与产品边界。

软件项目、社区、能力和集成关系的 canonical 记录维护在 [ai_infra_relationship](https://github.com/MarsChan8293/ai_infra_relationship)。本仓库不再维护 `software/` 项目目录或 redirect 副本。

## 知识图谱入口

- Obsidian 根节点：[[00-ai-infra-map|AI Infra 知识图谱入口]]
- 在线 Quartz 知识库：https://MarsChan8293.github.io/ai_infra_docs/
- 在线关系探索器：https://MarsChan8293.github.io/ai_infra_docs/graph-explorer/

## 主要领域

- [[models/00-model-index|AI Model Index]]
- [[system/README|AI Infra 系统架构]]
- [[chip/00-project-index|AI 芯片与基础设施资料库]]
- [[ROADMAP|AI Infra Docs Roadmap]]
- [[AGENTS|协作约定与知识图谱规则]]

## 系统桥梁

- [[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层级]]
- [[system/resource/accelerator-resource-model|加速器资源模型]]
- [[system/scheduling/topology-aware-scheduling|拓扑感知调度]]
- [[system/heterogeneous-compute/heterogeneous-inference|异构推理]]

这些页面维护跨项目稳定的系统机制，不维护某个软件项目的版本、能力矩阵、组织、维护者或项目间集成事实。

## Roadmap

下一阶段优先扩建 `system/`，建立从 Model facts 和 Workload 到 Compute / Memory / Communication / Topology，再到 Hardware capability 的可计算主线。详细计划、优先级和验收标准见 [[ROADMAP|AI Infra Docs Roadmap]]。

## Obsidian 入口

推荐把仓库根目录直接作为 Obsidian Vault，并从 [[00-ai-infra-map|AI Infra 知识图谱入口]] 开始浏览。内部语义关系优先使用唯一、显式的 Wiki Link 路径；外部软件项目与官方资料使用普通 URL。

## 图谱构建

本地可运行：

```bash
python3 scripts/validate-repo.py --root . --report generated/validation.json
python3 scripts/build-knowledge-graph.py --root . --output generated
```

图谱脚本会生成 `nodes.json`、`edges.json`、`metrics.json`、`unresolved-links.json` 和 `graph-summary.md`。这些均属于派生数据，不作为知识源手工维护。

主知识源始终是仓库中的 Markdown、frontmatter 与内部双链。
