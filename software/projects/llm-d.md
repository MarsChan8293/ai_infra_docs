---
schema_version: software-v0.1
name: llm-d
object_type: project
category: distributed-serving
organization: llm-d
status: active
repo: https://github.com/llm-d/llm-d
docs: https://llm-d.ai/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - request-routing
  - kv-aware-routing
  - pd-disaggregation
  - worker-pool-orchestration
  - kubernetes-native-serving
integrations:
  - vllm
  - lmcache
  - nixl
backends: []
updated: 2026-09-15
---
# llm-d

> Kubernetes 原生的分布式 LLM serving 编排与请求路由层。

## 核心能力

| 能力 | 说明 |
|---|---|
| Request Routing | 在多个模型 worker 之间选择请求去向 |
| KV-aware Routing | 把 prefix / KV 状态纳入路由决策 |
| P/D Disaggregation | 编排 Prefill 与 Decode worker |
| Worker Pool Orchestration | 组织不同角色或不同配置的 worker 池 |
| Kubernetes-native Serving | 面向 Kubernetes 部署和服务治理 |

## 边界

llm-d 不执行模型 kernel，也不替代 vLLM；它解决“多个 worker 如何组成一个服务”。它也不是 Pod/Job 级集群调度器，底层 placement 仍由 Kubernetes 调度体系完成。

两级调度的区别见 [[software/concepts/llm-serving-stack|LLM Serving 软件栈]]。

## 集成与后端

- vLLM：模型执行 worker。
- LMCache：KV 外部化、复用与传输。
- NIXL：高性能数据传输路径之一。
- llm-d 本身是控制/编排层，因此 V0.1 不给它填写直接硬件 `backends`。

## 版本快照

当前页未绑定单一 release 或 commit。能力列表是 2026-09-15 的调查快照，实验性或版本相关行为需要继续通过 release notes 核实。

## 直接来源

- https://llm-d.ai/
- https://github.com/llm-d/llm-d
- https://docs.vllm.ai/
- https://docs.lmcache.ai/
