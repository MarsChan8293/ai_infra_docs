---
schema_version: software-v0.1
name: Volcano
object_type: project
category: scheduler
organization: volcano-sh / CNCF
status: active
repo: https://github.com/volcano-sh/volcano
docs: https://volcano.sh/en/docs/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - batch-scheduling
  - gang-scheduling
  - queue
  - preemption
  - backfill
integrations: []
backends:
  - kubernetes
updated: 2026-09-15
---
# Volcano

> 面向 AI、HPC 和 Batch 工作负载的 Kubernetes 批调度系统。

## 核心能力

| 能力 | 说明 |
|---|---|
| Gang Scheduling | 保证一组 Pod 满足条件后再运行 |
| Queue | 提供批任务队列与资源管理 |
| Preempt / Reclaim | 支持抢占和资源回收 |
| 插件式 Scheduler | 通过 action/plugin 扩展调度行为 |

## 边界

Volcano 重点是 batch/Pod 调度，不负责模型 inference routing、KV Cache 或 GPU kernel。

## 集成与后端

V0.1 暂不把生态适配自动视作强集成。

## 关联项目

- AI 调度器：[[software/projects/kai-scheduler|KAI-Scheduler]]。
- Job admission / queue：[[software/projects/kueue|Kueue]]。

## 版本快照

本页不绑定单一 release；能力判断以 2026-09-15 前官方文档为快照。

## 直接来源

- https://volcano.sh/en/docs/
- https://github.com/volcano-sh/volcano
