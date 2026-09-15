---
schema_version: software-v0.1
name: KV Cache 生命周期
object_type: concept
category: inference-memory
updated: 2026-09-15
---
# KV Cache 生命周期

> KV Cache 是一条生成、驻留、复用、迁移、卸载和回收的数据生命周期，而不只是一个缓存文件。

## 问题

长上下文、多轮对话和重复前缀会产生大量可复用计算，但 KV 本身也会占用昂贵的显存、内存、存储和网络资源。

## 核心机制

```text
Prompt
  → [[software/projects/vllm|vLLM]] Prefill 生成 KV
  → GPU HBM 驻留
  → 命中时复用
  → [[software/projects/lmcache|LMCache]] 外部化 / 卸载 / 迁移
  → 路由层利用 KV 状态
  → 淘汰或释放
```

## 判断要点

任何 KV 方案至少回答四件事：命中率是否足够高、搬运是否比重算便宜、元数据能否准确定位、失效与租户隔离是否可靠。

## 相关项目与概念

- [[software/projects/vllm|vLLM]]
- [[software/projects/lmcache|LMCache]]
- [[software/projects/llm-d|llm-d]]
- [[software/concepts/pd-disaggregation|Prefill / Decode 分离]]
