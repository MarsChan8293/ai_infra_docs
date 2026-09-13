# AI Infra Software Landscape

This directory organizes AI infrastructure software by architectural layer rather than by project name.

## Layered structure

### 1. Inference Engine
Execution runtimes that perform model forward passes and serve tokens.

- [vLLM](./inference-engine/vllm.md)

Planned additions: SGLang, TensorRT-LLM, vLLM-Ascend.

### 2. KV Cache / Memory System
Systems focused on KV cache storage, reuse, transfer, offload, and multi-tier cache management.

- [LMCache](./kv-cache/lmcache.md)

Planned additions: Mooncake and other distributed KV-cache / memory systems.

### 3. Distributed Serving / Inference Orchestration
Systems above individual inference engines that coordinate workers, requests, routing, Prefill/Decode separation, and distributed LLM serving.

- [llm-d](./distributed-serving/llm-d.md)

Planned additions: NVIDIA Dynamo and related serving-control-plane projects.

### 4. Scheduling
Cluster-level workload schedulers that decide where jobs, Pods, or accelerator workloads run.

- [KAI-Scheduler](./scheduling/kai-scheduler.md)

Planned additions: Volcano, Kueue, Ray scheduling components.

### 5. Device Resource / Virtualization
Device allocation, sharing, isolation, topology awareness, and accelerator abstraction close to the Kubernetes/device layer.

- [HAMi](./device-resource/hami.md)
- [Kubernetes DRA](./device-resource/dra.md)

## Stack view

```text
Application / API
       |
Distributed Serving / Routing
       |        llm-d / Dynamo
       v
Inference Engine
       |        vLLM / SGLang / TensorRT-LLM
       v
KV Cache / Memory System
       |        LMCache / Mooncake
       v
Scheduling
       |        KAI-Scheduler / Volcano / Kueue
       v
Device Resource / Virtualization
                HAMi / DRA / Device Plugins
       v
GPU / NPU / RDMA / Memory / Network
```

The boundaries are not perfectly rigid. Some projects span multiple layers, so each project document should record both its primary layer and important cross-layer capabilities.

## Common evaluation dimensions

For every project, track:

- Primary position in the AI infrastructure stack
- Core architecture and key components
- Main use cases
- GPU / NPU support
- Kubernetes integration
- Distributed inference support
- Prefill / Decode disaggregation support
- KV cache capabilities
- Topology awareness
- Multi-tenancy / sharing / isolation
- Scheduling semantics
- Integration points with other projects
- Operational maturity and limitations
