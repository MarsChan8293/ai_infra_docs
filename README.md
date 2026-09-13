---
title: ai_infra_docs 仓库说明
tags:
  - ai-infra
  - repository
---

# ai_infra_docs

本仓库整理 AI 芯片、LLM 推理软件栈、KV Cache、分布式 Serving、Kubernetes 调度和设备资源管理等 AI Infra 主题，同时兼容 GitHub 阅读与 Obsidian 知识图谱浏览。

## Obsidian 入口

推荐把仓库根目录直接作为 Obsidian Vault，并从 [[00-ai-infra-map|AI Infra 知识图谱入口]] 开始浏览。这个独立 MOC 使用唯一文件名，避免仓库中多个 `README.md` 在 Wiki Link 解析时产生歧义。

## 主要领域

- [[chip/00-project-index|AI 芯片与基础设施资料库]]
- [[software/README|AI Infra 软件栈地图]]
- [[AGENTS|协作约定与知识图谱规则]]

## 软件核心概念

- [[software/concepts/llm-serving-stack|LLM Serving 软件栈]]
- [[software/concepts/pd-disaggregation|Prefill / Decode 分离]]
- [[software/concepts/kv-cache-lifecycle|KV Cache 生命周期]]
- [[software/concepts/topology-aware-scheduling|拓扑感知调度]]
- [[software/concepts/accelerator-resource-model|加速器资源模型]]
- [[software/concepts/heterogeneous-inference|异构推理]]

仓库内部关系优先使用 Obsidian Wiki Link，外部资料继续使用普通 URL。具体规范见 [[AGENTS#Obsidian 知识图谱与内部链接|AGENTS.md 的 Obsidian 规范]]。
