# HAMi

## Position
Heterogeneous accelerator resource management and sharing layer for Kubernetes.

## Core capabilities
- GPU / accelerator sharing
- Memory and compute isolation for supported devices
- Device-plugin based integration
- Topology-aware placement support
- Heterogeneous accelerator ecosystem support
- Remote GPU / disaggregated accelerator exploration

## AI Infra relevance
HAMi sits close to the device layer and focuses on how accelerator capacity is exposed, shared, isolated, and scheduled for containers.

## Relationship with other components
- Can complement KAI-Scheduler, with KAI handling higher-level workload placement and HAMi enforcing accelerator sharing / isolation
- Can participate in DRA-oriented device allocation architectures
- Provides a lower-level resource layer underneath inference systems such as vLLM and llm-d

## Focus areas for this repository
- vGPU semantics and isolation
- NUMA / PCIe locality
- Remote GPU architecture and overhead
- Multi-vendor accelerator support
- DRA integration
- Interaction with KAI-Scheduler
