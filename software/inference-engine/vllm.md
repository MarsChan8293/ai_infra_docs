# vLLM

## Position
High-throughput LLM inference engine and serving runtime.

## Core capabilities
- Continuous batching
- PagedAttention and KV cache management
- Tensor / pipeline / expert parallel integration depending on model and backend
- OpenAI-compatible serving APIs
- Broad model ecosystem support

## AI Infra relevance
vLLM is a key execution-layer component. It sits below higher-level serving and routing systems such as llm-d and above accelerator runtimes such as CUDA or vendor-specific backends.

## Focus areas for this repository
- Prefill / Decode behavior
- KV cache layout and offload
- Distributed inference
- Multi-node networking
- Scheduler behavior under concurrency
- Backend differences across NVIDIA and NPU ecosystems
- Integration with LMCache and llm-d
