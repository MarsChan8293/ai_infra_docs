---
schema_version: software-v0.1
name: KV Cache 生命周期
object_type: concept
category: memory-architecture
updated: 2026-09-15
---
# KV Cache 生命周期

> KV Cache 是贯穿生成、驻留、复用、迁移、卸载和淘汰的一类运行时状态。

## 问题

长上下文、RAG、多轮会话和 P/D 分离都可能让 KV 从单进程内部状态演化成跨 worker、跨节点的数据资源。

## 核心机制

```text
[[software/projects/vllm|vLLM]] / [[software/projects/sglang|SGLang]]
  → Prefill 生成 KV
  → GPU HBM 驻留与本地复用
  → [[software/projects/lmcache|LMCache]] / [[software/projects/mooncake|Mooncake]] 外部化、共享或卸载
  → [[software/projects/nixl|NIXL]] 等数据面搬运
  → [[software/projects/llm-d|llm-d]] / [[software/projects/nvidia-dynamo|Dynamo]] 根据 KV 状态做路由或编排
  → 淘汰 / 释放
```

## 判断要点

- 命中率决定复用是否有收益。
- Retrieve/Transfer 成本必须低于重新 Prefill。
- KV layout、dtype、block size 与 engine/hardware 相关。
- 多租户场景必须考虑隔离、生命周期和失效语义。

## 相关项目与概念

- [[software/concepts/pd-disaggregation|Prefill / Decode 分离]]
- [[software/concepts/topology-aware-scheduling|拓扑感知调度]]
- [[software/concepts/llm-serving-stack|LLM Serving 软件栈]]
