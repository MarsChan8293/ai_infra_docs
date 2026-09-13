# AI Infra Software

This directory organizes software projects relevant to AI infrastructure, especially LLM inference, KV cache, scheduling, GPU/NPU resource management, and Kubernetes-native serving.

## Categories

### Inference Engines
- [vLLM](./vllm.md)

### KV Cache / Memory Systems
- [LMCache](./lmcache.md)

### Scheduling / Resource Management
- [KAI-Scheduler](./kai-scheduler.md)
- [HAMi](./hami.md)
- [Kubernetes DRA](./dra.md)

### Distributed LLM Serving
- [llm-d](./llm-d.md)

## Suggested evaluation dimensions

For each project, track:

- Position in the AI infrastructure stack
- Core architecture and key components
- Main use cases
- GPU/NPU support
- Kubernetes integration
- Distributed inference support
- Prefill/Decode disaggregation support
- KV cache capabilities
- Topology awareness
- Multi-tenancy / sharing / isolation
- Scheduling semantics
- Integration points with other projects
- Operational maturity and limitations

This folder can be expanded as a software landscape for the broader `ai_infra_docs` repository.
