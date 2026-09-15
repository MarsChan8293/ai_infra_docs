---
schema_version: software-v0.1
name: vLLM
object_type: project
category: inference-engine
organization: vllm-project
status: active
repo: https://github.com/vllm-project/vllm
docs: https://docs.vllm.ai/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - continuous-batching
  - paged-kv-cache
  - prefix-caching
  - speculative-decoding
  - tensor-parallel
  - pipeline-parallel
  - expert-parallel
integrations:
  - lmcache
  - nixl
  - llm-d
backends:
  - nvidia
  - amd
  - intel
  - ascend
updated: 2026-09-15
---
# vLLM

> 面向大模型推理的高吞吐执行引擎与 serving runtime。

## 核心能力

| 能力 | 说明 |
|---|---|
| Continuous Batching | 动态组织活跃请求，提高设备利用率 |
| Paged KV Cache | 分页管理 KV，降低连续显存预留和碎片问题 |
| Prefix Caching | 对重复前缀复用已生成 KV |
| Speculative Decoding | 支持推测式解码路径 |
| TP / PP / EP | 提供多 GPU / 多 worker 的模型并行能力 |

## 边界

vLLM 负责模型执行、请求批处理、活跃 KV 管理和模型并行。它不是 Kubernetes 集群调度器，也不等价于完整的跨实例 serving 控制面。

Paged KV、Continuous Batching 等通用机制不在本页展开，相关原理见 [[software/concepts/kv-cache-lifecycle|KV Cache 生命周期]] 与 [[software/concepts/llm-serving-stack|LLM Serving 软件栈]]。

## 集成与后端

- LMCache：外部 KV Cache、复用与迁移。
- NIXL：高性能数据 / KV 传输路径之一。
- llm-d：在 vLLM worker 之上做请求路由与分布式编排。
- 已确认存在 NVIDIA、AMD、Intel、Ascend 等支持路径；不同后端的功能和性能不应默认等价。

## 版本快照

本页未绑定单一 release 或 commit，因此 `snapshot.version` 与 `snapshot.commit` 保持 `null`。能力判断以 2026-09-15 前现有官方文档和仓库资料为快照，后续版本变化应更新 frontmatter。

## 直接来源

- https://docs.vllm.ai/
- https://github.com/vllm-project/vllm
- https://docs.lmcache.ai/
- https://llm-d.ai/
