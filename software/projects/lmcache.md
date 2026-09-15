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
  - external-kv-cache
  - kv-offload
  - cross-instance-kv-reuse
  - kv-transfer
  - pd-disaggregation
integrations:
  - vllm
  - nixl
  - llm-d
backends:
  - nvidia
updated: 2026-09-15
---
# LMCache

> 面向 LLM 推理的外部 KV Cache 管理、复用、卸载与传输层。

## 核心能力

| 能力 | 说明 |
|---|---|
| External KV Cache | 将 KV 从单一推理进程扩展到外部存储层 |
| Offload / Retrieve | 在 GPU、CPU、存储或远端路径之间迁移 KV |
| Cross-instance Reuse | 让多个推理实例复用可命中的 KV |
| KV Transfer | 为 P/D 分离等场景提供 KV 数据移动路径 |
| Observability | 关注命中、存取和传输成本 |

## 边界

LMCache 不负责模型 forward，也不替代 vLLM 的请求调度器；它管理的是 KV 的外部生命周期。是否值得引入取决于 KV 命中收益是否大于存储和传输成本。

机制解释见 [[software/concepts/kv-cache-lifecycle|KV Cache 生命周期]] 和 [[software/concepts/pd-disaggregation|Prefill / Decode 分离]]。

## 集成与后端

- vLLM：主要推理引擎集成路径之一。
- NIXL：高性能 KV / 数据传输路径之一。
- llm-d：可在上层利用 KV 状态做路由和 P/D 编排。
- 当前页只把 NVIDIA 路径放入 `backends`；其他硬件生态的支持程度需要按版本单独核实。

## 版本快照

当前资料未固定单一 release 或 commit，因此保持 `null`。本页表示 2026-09-15 的能力快照，不代表所有历史版本都具备相同能力。

## 直接来源

- https://docs.lmcache.ai/
- https://github.com/LMCache/LMCache
- https://docs.vllm.ai/
- https://llm-d.ai/
