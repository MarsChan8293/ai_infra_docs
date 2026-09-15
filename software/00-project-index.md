---
title: "AI Infra Software Project Index"
tags: [moc, software]
updated: 2026-09-15
---
# AI Infra Software Project Index

软件目录采用最小模型：**Project + Concept**。

项目页回答“这个软件是什么、当前调查快照是什么、核心能力是什么、和谁集成”；概念页回答“这个机制为什么存在、如何工作”。

## Projects

| 项目 | 主分类 | 一句话定位 |
|---|---|---|
| [[software/projects/vllm|vLLM]] | inference-engine | LLM 推理执行与 serving runtime |
| [[software/projects/lmcache|LMCache]] | kv-cache | 外部 KV Cache 管理与迁移 |
| [[software/projects/llm-d|llm-d]] | distributed-serving | Kubernetes 原生分布式 LLM serving 编排 |
| [[software/projects/kai-scheduler|KAI-Scheduler]] | scheduler | 面向 AI/GPU workload 的 Kubernetes 调度器 |
| [[software/projects/hami|HAMi]] | device-resource | 异构加速器共享、隔离与设备管理 |
| [[software/projects/kubernetes-dra|Kubernetes DRA]] | device-resource | Kubernetes 动态设备资源声明与分配框架 |

## Concepts

- [[software/concepts/llm-serving-stack|LLM Serving 软件栈]]
- [[software/concepts/pd-disaggregation|Prefill / Decode 分离]]
- [[software/concepts/kv-cache-lifecycle|KV Cache 生命周期]]
- [[software/concepts/topology-aware-scheduling|拓扑感知调度]]
- [[software/concepts/accelerator-resource-model|加速器资源模型]]
- [[software/concepts/heterogeneous-inference|异构推理]]

## 维护规则

- 一个项目一页，不按“它属于哪一层”复制多份。
- `snapshot.as_of` 必填；未固定版本时 `version`、`commit` 保持 `null`。
- `capabilities` 只写当前调查已确认的能力，不记录营销形容词。
- `integrations` 只表示存在明确集成关系，不暗示性能或成熟度一致。
- `backends` 表示存在已确认支持路径，不代表不同后端功能完全等价。
- 通用原理只写入 `concepts/`，项目页只保留必要边界说明。

硬件入口：[[chip/00-project-index|AI 芯片与硬件资料库]]。
