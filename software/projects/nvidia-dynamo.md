---
schema_version: software-v0.1
name: NVIDIA Dynamo
object_type: project
category: distributed-serving
organization: ai-dynamo
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
backends:
  - nvidia
  - amd
  - intel
updated: 2026-09-15
---
# NVIDIA Dynamo

> 开放式生成式 AI 分布式推理框架，把多个引擎与数据面组织成可扩展服务。

## 核心能力

| 能力 | 说明 |
|---|---|
| Engine Interop | 可接入 vLLM、SGLang、TensorRT-LLM |
| Disaggregated Serving | 支持 Prefill/Decode 等分离式执行 |
| KV-aware Routing | 围绕 KV 状态优化请求路由 |
| 模块化控制面 | 可独立采用 frontend、router、planner、cache manager |

## 边界

Dynamo 位于单个推理引擎之上；模型 kernel 与底层设备资源分配仍由相应引擎、通信库和集群层负责。

## 集成与后端

- [[software/projects/vllm|vLLM]]、[[software/projects/sglang|SGLang]]、[[software/projects/tensorrt-llm|TensorRT-LLM]]：推理引擎路径。
- [[software/projects/nixl|NIXL]]：高性能推理数据传输底座之一。

## 关联项目

- 同层框架：[[software/projects/llm-d|llm-d]]、[[software/projects/aibrix|AIBrix]]。

## 版本快照

本页不固定 release；以 2026-09-15 前官方资料为快照。

## 直接来源

- https://docs.nvidia.com/dynamo/
- https://github.com/ai-dynamo/dynamo
