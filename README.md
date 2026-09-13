---
title: AI Infra 知识图谱入口
aliases:
  - AI Infra MOC
  - AI Infra Knowledge Map
tags:
  - moc
  - ai-infra
  - obsidian
---

# AI Infra 知识图谱入口

本仓库既是 GitHub 文档库，也是一个可直接用 Obsidian 打开的知识库。建议把仓库根目录直接作为 Obsidian Vault，通过内部双链、反向链接和 Graph View 观察硬件、软件、调度、KV Cache 与分布式推理之间的关系。

## 主要入口

- [[chip/00-project-index|AI 芯片与基础设施资料库]]
- [[software/README|AI Infra 软件栈地图]]
- [[AGENTS|协作约定与知识图谱规则]]

## 核心软件概念节点

- [[software/concepts/llm-serving-stack|LLM Serving 软件栈]]
- [[software/concepts/pd-disaggregation|Prefill / Decode 分离]]
- [[software/concepts/kv-cache-lifecycle|KV Cache 生命周期]]
- [[software/concepts/topology-aware-scheduling|拓扑感知调度]]
- [[software/concepts/accelerator-resource-model|加速器资源模型]]
- [[software/concepts/heterogeneous-inference|异构推理]]

## 关系总览

```mermaid
graph TD
    ROOT[AI Infra 知识图谱] --> CHIP[芯片 / 硬件]
    ROOT --> SW[软件栈]
    SW --> SERVING[分布式 Serving]
    SW --> ENGINE[推理引擎]
    SW --> KV[KV Cache / Memory]
    SW --> SCHED[集群调度]
    SW --> DEVICE[设备资源]
    CHIP --> DEVICE
    ENGINE --> KV
    SERVING --> ENGINE
    SERVING --> KV
    SCHED --> DEVICE
    DEVICE --> CHIP
```

## 使用原则

内部关系优先使用 Obsidian Wiki Link，例如 `[[software/inference-engine/vllm|vLLM]]`。外部资料继续使用普通 URL。不要为了“图更密”而机械互链，应该围绕真实架构关系建立边，并通过 MOC 和概念节点避免孤岛文档。

新增或重构文档时，应先判断它属于哪个领域入口，再补充它与上下游组件、关键机制和硬件层的关系。具体规则见 [[AGENTS#Obsidian 知识图谱与内部链接|AGENTS.md 的 Obsidian 规范]]。
