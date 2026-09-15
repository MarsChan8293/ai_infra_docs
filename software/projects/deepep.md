---
schema_version: software-v0.1
name: DeepEP
object_type: project
category: communication
organization: deepseek-ai
status: active
repo: https://github.com/deepseek-ai/DeepEP
docs: https://github.com/deepseek-ai/DeepEP
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - expert-parallel
  - all-to-all
  - moe-dispatch
  - moe-combine
  - low-latency
integrations:
  - nccl
backends:
  - nvidia
updated: 2026-09-16
---
# DeepEP

> DeepSeek 面向 MoE Expert Parallel 的高吞吐、低延迟通信库。

## 核心能力

| 能力 | 说明 | 证据 |
|---|---|---|
| EP All-to-All | 优化 MoE expert dispatch / combine | [S1] |
| 高吞吐路径 | 面向训练和推理的大规模 token 交换 | [S1] |
| 低延迟路径 | 面向 decode 等低延迟场景 | [S1] |
| 低精度通信 | 支持 FP8 等数据格式 | [S1] |

## 边界

DeepEP 重点解决 MoE 专家并行通信，不提供完整模型 serving 或通用集群调度。

## 集成与后端

- [[software/projects/nccl|NCCL]]：当前 V2 使用 NCCL Gin backend。

## 关联项目

- MoE 推理：[[software/projects/sglang|SGLang]]。
- MoE 计算 kernel：[[software/projects/deepgemm|DeepGEMM]]。

## 版本快照

本页不绑定单一 release；能力判断以 2026-09-15 前 DeepEP 官方仓库为快照。

## 直接来源

- [S1] https://github.com/deepseek-ai/DeepEP
