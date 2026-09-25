---
title: Workload Profile V0.1
aliases:
  - Executable Workload Profile
tags:
  - system
  - workload
  - executable
updated: 2026-09-25
---
# Workload Profile V0.1

Workload Profile 是 Phase 4 可执行知识库的机器输入边界。Schema 文件：

`system/workload/workload-profile-v0.1.schema.json`

代表输入：

`examples/workloads/qwen3.8-27b-mi300x-decode-64k.yaml`

## 设计原则

- Model facts 从 Model V0.2 页面读取，不复制成手工维护的第二份事实源。
- Hardware facts 从 Chip V0.2 页面读取。
- Workload / execution assumptions 必须显式写入 profile。
- 未知值使用 `null` 或不派生，不按 0 处理。
- batch / concurrency / request rate 保持不同语义。
- TP / PP / EP / DP / CP degree 必须显式给出，默认值只能由调用方明确写入。

## 输入与输出

原始 YAML 描述 scenario；`scripts/build-workload-profile.py` 读取 Model / Hardware frontmatter 后生成 normalized JSON，包含：

- model / hardware source path
- canonical facts snapshot
- workload
- execution assumptions
- parallelism
- safe workload-derived values
- warnings / unknowns

System requirements 再由 `scripts/build-system-requirements.py` 消费。

## 与 System 的关系

- [[system/workload/inference-workload|Inference Workload]]
- [[system/workload/training-workload|Training Workload]]
- [[system/compute/transformer-compute-model|Transformer Compute Model]]
- [[system/memory/model-memory-accounting|Model Memory Accounting]]
- [[system/communication/communication-cost-model|Communication Cost Model]]

Workload Profile 只规范数据，不把某个 software/runtime 的项目事实搬进本仓库。
