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
  - llm-d
  - nvidia-dynamo
  - kserve
  - ray-serve
  - mooncake
  - flashinfer
  - bentoml
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
| Paged KV Cache | 分页管理 KV，降低连续显存预留与碎片 |
| Prefix Caching | 复用重复前缀对应的 KV |
| 多并行策略 | 支持 TP、PP、EP 等模型并行路径 |

## 边界

vLLM 负责模型执行、请求批处理、活跃 KV 管理和模型并行；不负责 Kubernetes 集群资源治理，也不等价于完整的跨实例 serving 控制面。

## 集成与后端

- [[software/projects/lmcache|LMCache]]：外部 KV Cache、复用与迁移。
- [[software/projects/llm-d|llm-d]]：请求路由与分布式推理编排。
- [[software/projects/nvidia-dynamo|NVIDIA Dynamo]]：分布式推理控制面。
- [[software/projects/kserve|KServe]]、[[software/projects/ray-serve|Ray Serve]]、[[software/projects/bentoml|BentoML]]：上层模型服务与部署入口。
- [[software/projects/mooncake|Mooncake]]：分布式 KV / 数据传输路径。
- [[software/projects/flashinfer|FlashInfer]]：高性能 serving kernel。

## 关联项目

- 同层引擎：[[software/projects/sglang|SGLang]]、[[software/projects/tensorrt-llm|TensorRT-LLM]]、[[software/projects/llama-cpp|llama.cpp]]。
- Kernel / 编译：[[software/projects/triton|Triton]]、[[software/projects/flashattention|FlashAttention]]。
- 通信：[[software/projects/nccl|NCCL]]、[[software/projects/rccl|RCCL]]。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前官方资料为快照。

## 直接来源

- https://docs.vllm.ai/
- https://github.com/vllm-project/vllm
