# llm-d

## Position
Kubernetes-native distributed LLM inference framework.

## Core capabilities
- Distributed serving architecture
- Integration with vLLM-based inference workers
- Request routing across inference instances
- Support for disaggregated inference patterns
- KV-cache-aware serving and routing concepts
- Kubernetes-native control and deployment model

## AI Infra relevance
llm-d sits above the inference engine and below the external API / application layer. It coordinates multiple model-serving workers as a distributed LLM service rather than treating each inference process as an isolated endpoint.

## Relationship with other components
- vLLM: execution engine
- LMCache: KV cache reuse / movement layer
- KAI-Scheduler: workload placement and cluster scheduling
- HAMi: accelerator sharing / isolation
- DRA: accelerator resource allocation abstraction

## Focus areas for this repository
- Prefill / Decode disaggregation
- KV-aware routing
- Worker pools and heterogeneous hardware
- Integration with external KV cache systems
- Interaction with Kubernetes scheduling
- Request-level versus pod-level scheduling
