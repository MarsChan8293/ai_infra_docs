---
schema_version: software-v0.1
name: DeepSeek-Infra
object_type: project
category: ecosystem
organization: deepseek-ai
status: active
repo: https://github.com/deepseek-ai
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - ai-infrastructure
  - kernel-optimization
  - communication
  - storage
integrations: []
backends: []
updated: 2026-09-16
---
# DeepSeek-Infra

> DeepSeek 开源基础设施项目族的聚合入口。

## 核心能力

该生态覆盖存储、MoE 通信、GEMM、JIT、attention 等基础组件，适合作为 DeepSeek 系统工程路线的总入口。[S1]

## 边界

DeepSeek-Infra 是项目族而不是单一 runtime；具体技术事实应落到独立项目页。

## 集成与后端

- 存储：[[software/projects/3fs|3FS]]。
- MoE 通信：[[software/projects/deepep|DeepEP]]。
- GEMM：[[software/projects/deepgemm|DeepGEMM]]。
- JIT：[[software/projects/deepjit|DeepJIT]]。
- Attention：[[software/projects/flashmla|FlashMLA]]。

## 关联项目

- [[software/projects/3fs|3FS]]
- [[software/projects/deepep|DeepEP]]
- [[software/projects/deepgemm|DeepGEMM]]
- [[software/projects/deepjit|DeepJIT]]
- [[software/projects/flashmla|FlashMLA]]

## 版本快照

本页以 2026-09-15 前 deepseek-ai 公开项目为快照。

## 直接来源

- [S1] https://github.com/deepseek-ai
