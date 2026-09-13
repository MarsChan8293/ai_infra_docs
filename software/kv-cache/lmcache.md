# LMCache

## Position
KV cache storage, reuse, and movement layer for LLM serving systems.

## Core capabilities
- KV cache reuse across requests and instances
- Cache movement between GPU, CPU memory, and external storage depending on deployment
- Integration with inference engines such as vLLM
- Designed to improve TTFT and effective accelerator utilization for repeated or shared-prefix workloads

## AI Infra relevance
LMCache is particularly relevant to disaggregated serving architectures, where KV cache lifecycle and transfer can become as important as model execution itself.

## Focus areas for this repository
- KV cache residency policies
- Prefix reuse
- CPU / GPU / remote cache tiers
- Cache eviction and active cache management
- P/D disaggregation integration
- Network bandwidth requirements for KV transfer
- Interaction with client-side KV cache designs
