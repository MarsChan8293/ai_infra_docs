---
title: ai_infra_docs 仓库说明
tags:
  - ai-infra
  - repository
---

# ai_infra_docs

本仓库聚焦 AI workload 如何落到系统架构与硬件：从模型状态、内存层次、资源表达、拓扑与异构计算，一路连接到 GPU / NPU、HBM、互联与基础设施。

软件项目、社区、能力、集成和维护者关系的 canonical 事实统一维护在 [ai_infra_relationship](https://github.com/MarsChan8293/ai_infra_relationship)。本仓库不再维护第二份软件项目数据库，也不保留本地软件项目 redirect。

## 知识图谱入口

- Obsidian 根节点：[[00-ai-infra-map|AI Infra 知识图谱入口]]
- 在线 Quartz 知识库：https://MarsChan8293.github.io/ai_infra_docs/
- 在线关系探索器：https://MarsChan8293.github.io/ai_infra_docs/graph-explorer/

## 主要领域

- [[models/00-model-index|AI Model Index]]：描述 workload 与状态规模。
- [[system/README|AI Infra System Architecture]]：描述 workload 到硬件之间的系统机制。
- [[chip/00-project-index|AI 芯片与基础设施资料库]]：描述芯片、板卡、内存、互联与产品事实。

推荐阅读路径是 **Model → System → Chip**，而不是把软件项目复制进本仓库。

## 系统架构核心节点

- [[system/memory/kv-cache-memory-hierarchy|KV Cache 内存层次]]
- [[system/resource/accelerator-resource-model|加速器资源模型]]
- [[system/topology/topology-aware-scheduling|拓扑感知调度]]
- [[system/heterogeneous-compute/heterogeneous-inference|异构推理]]

## 与软件项目资料的边界

本仓库可以在模型页和系统概念页中引用 vLLM、SGLang、LMCache、NIXL、Kubernetes DRA 等项目，但应直接链接其 canonical relationship 页面或官方上游，不在本仓库建立项目镜像页。

## 图谱构建

本地可运行：

```bash
python3 scripts/build-knowledge-graph.py --root . --output generated
```

脚本会生成 `nodes.json`、`edges.json`、`metrics.json`、`unresolved-links.json` 和 `graph-summary.md`。这些均属于派生数据；主知识源始终是仓库中的 Markdown、frontmatter 和内部双链。
