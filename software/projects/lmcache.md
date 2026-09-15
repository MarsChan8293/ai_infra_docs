---
schema_version: software-v0.1
name: LMCache
object_type: project
category: kv-cache
organization: LMCache
status: active
repo: https://github.com/LMCache/LMCache
docs: https://docs.lmcache.ai/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - kv-offload
  - prefix-reuse
  - remote-kv-cache
  - kv-transfer
  - observability
integrations:
  - vllm
  - llm-d
  - nixl
backends:
  - nvidia
updated: 2026-09-16
---
# LMCache

> 面向 LLM 推理的外部 KV Cache 管理、复用与迁移层。

## 核心能力

| 能力 | 说明 | 证据 |
|---|---|---|
| KV Offload | 把 KV 从 GPU 扩展到 CPU、存储或远端层级 | [S1] |
| 跨实例复用 | 在多个 worker 之间共享可复用 KV | [S1] |
| KV Transfer | 支持 P/D 分离中的 KV 搬运路径 | [S1] |
| Cache Observability | 观察命中、存取和传输成本 | [S1] |

## 边界

LMCache 不执行模型 forward，也不替代请求路由器；其职责是 KV 生命周期和数据移动。

## 集成与后端

- [[software/projects/vllm|vLLM]]：模型执行与活跃 KV 管理。
- [[software/projects/llm-d|llm-d]]：上层请求路由与 P/D 编排。
- [[software/projects/nixl|NIXL]]：高性能 KV 数据传输路径之一。

## 关联项目

- 同类 / 相邻 KV 系统：[[software/projects/mooncake|Mooncake]]。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前官方资料为快照。

## 直接来源

- [S1] https://docs.lmcache.ai/
- [S2] https://github.com/LMCache/LMCache
