---
schema_version: software-v0.1
name: Kueue
object_type: project
category: scheduler
organization: Kubernetes SIGs
status: active
repo: https://github.com/kubernetes-sigs/kueue
docs: https://kueue.sigs.k8s.io/docs/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - job-queueing
  - admission-control
  - cluster-queue
  - fair-sharing
  - multi-cluster
integrations: []
backends:
  - kubernetes
updated: 2026-09-15
---
# Kueue

> Kubernetes-native Job Queueing 与 admission control 系统。

## 核心能力

| 能力 | 说明 |
|---|---|
| Admission Control | 决定 Job 何时获得资源并开始运行 |
| ClusterQueue | 集中表达配额和资源池 |
| Fair Sharing | 支持多租户公平共享 |
| MultiKueue | 支持多集群 Job 分发方向 |

## 边界

Kueue 更偏 Job admission，而不是替换底层 kube-scheduler，也不理解 LLM request 级语义。

## 集成与后端

V0.1 暂不把所有 Job framework 适配都写入 `integrations`。

## 关联项目

- AI 调度器：[[software/projects/kai-scheduler|KAI-Scheduler]]。
- Batch scheduler：[[software/projects/volcano|Volcano]]。

## 版本快照

本页不绑定单一 release；能力判断以 2026-09-15 前官方文档为快照。

## 直接来源

- https://kueue.sigs.k8s.io/docs/
- https://github.com/kubernetes-sigs/kueue
