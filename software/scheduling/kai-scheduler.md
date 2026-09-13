# KAI-Scheduler

## Position
Kubernetes-native scheduler designed for AI and accelerator workloads.

## Core capabilities
- Queue and quota management
- Fair-share scheduling
- Gang scheduling
- Preemption
- GPU-aware placement
- Support for shared GPU scenarios
- Topology-aware scheduling capabilities

## AI Infra relevance
KAI-Scheduler is a control-plane scheduling layer. It decides where AI workloads should run and how scarce accelerator resources are allocated across tenants and jobs.

## Relationship with other components
- Can work above accelerator-sharing layers such as HAMi
- Complements DRA, which standardizes richer device resource claims and allocation
- Sits below higher-level LLM request-routing systems such as llm-d

## Focus areas for this repository
- Multi-GPU and multi-node placement
- NUMA / PCIe / NVLink topology awareness
- Interaction with shared GPU mechanisms
- Batch and inference workload co-scheduling
- Heterogeneous accelerator scheduling
