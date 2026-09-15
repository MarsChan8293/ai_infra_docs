---
schema_version: software-v0.1
name: FlashMLA
object_type: project
category: runtime
organization: deepseek-ai
status: active
repo: https://github.com/deepseek-ai/FlashMLA
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - attention-kernel
  - mla-optimization
integrations: []
backends:
  - nvidia
updated: 2026-09-15
---
# FlashMLA

> 面向 Multi-head Latent Attention 等场景的高性能 attention kernel 项目。

## 核心能力

聚焦 attention 数据布局与 GPU kernel 优化，是 DeepSeek 模型执行路径的重要低层组件之一。

## 边界

FlashMLA 是 kernel 层，不承担完整推理引擎的请求调度、KV 管理或服务接口。

## 集成与后端

适合与 [[software/projects/flashattention|FlashAttention]]、[[software/projects/flashinfer|FlashInfer]] 比较 attention / serving kernel 的职责边界。

## 关联项目

- [[software/projects/deepseek-infra|DeepSeek-Infra]]
- [[software/projects/flashattention|FlashAttention]]
- [[software/projects/flashinfer|FlashInfer]]
- [[software/projects/deepgemm|DeepGEMM]]

## 版本快照

本页以 2026-09-15 前公开资料为快照。

## 直接来源

- https://github.com/deepseek-ai/FlashMLA
