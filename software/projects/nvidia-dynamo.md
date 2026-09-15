---
schema_version: software-v0.1
name: NVIDIA Dynamo
object_type: project
category: distributed-serving
organization: NVIDIA / ai-dynamo
status: active
repo: https://github.com/ai-dynamo/dynamo
docs: https://docs.nvidia.com/dynamo/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - distributed-inference
  - disaggregated-serving
  - kv-aware-routing
  - cache-management
  - autoscaling
integrations:
  - vllm
  - sglang
  - tensorrt-llm
  - nixl
relations:
  alternative-to:
    - llm-d
backends:
  - nvidia
  - amd
  - intel
updated: 2026-09-16
---
# NVIDIA Dynamo

> 开放式生成式 AI 分布式推理框架，把多个引擎与数据面组织成可扩展服务。

## 核心能力

| 能力 | 说明 | 证据 |
|---|---|---|
| Engine Interop | 可接入 vLLM、SGLang、TensorRT-LLM | [S1] |
| Disaggregated Serving | 支持 Prefill/Decode 等分离式执行 | [S1] |
| KV-aware Routing | 围绕 KV 状态优化请求路由 | [S1] |
| 模块化控制面 | 可独立采用 frontend、router、planner、cache manager | [S1] |

## 边界

Dynamo 位于单个推理引擎之上；模型 kernel 与底层设备资源分配仍由相应引擎、通信库和集群层负责。

## 集成与后端

- [[software/projects/vllm|vLLM]]、[[software/projects/sglang|SGLang]]、[[software/projects/tensorrt-llm|TensorRT-LLM]]：官方支持的推理引擎路径。
- [[software/projects/nixl|NIXL]]：高性能推理数据传输底座之一。

## 关联项目

- 同层框架：[[software/projects/llm-d|llm-d]]。

## 版本快照

本页不固定 release；截至 2026-09-15，官方文档显示 Dynamo 仍在持续发布与演进。

## 直接来源

- [S1] https://docs.nvidia.com/dynamo/
- [S2] https://github.com/ai-dynamo/dynamo
