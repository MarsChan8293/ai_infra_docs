# Kubernetes DRA

## Position
Dynamic Resource Allocation (DRA) is Kubernetes' richer resource-allocation framework for devices such as GPUs, NPUs, FPGAs, and other accelerators.

## Core concepts
- ResourceClaim / ResourceClaimTemplate
- Device classes and richer device selection
- Scheduler-aware allocation
- Vendor / driver extensibility

## AI Infra relevance
DRA is not an inference engine or scheduler replacement. It is the device-resource abstraction layer that lets workloads express more detailed accelerator requirements than a simple integer resource count.

## Relationship with other components
- KAI-Scheduler can make workload-placement decisions that consume richer device information
- HAMi-like systems can expose or enforce shared / virtualized accelerator resources
- Higher-level serving stacks such as llm-d remain above this layer

## Focus areas for this repository
- Multi-vendor GPU/NPU abstraction
- Device topology constraints
- Shared-device semantics
- Integration patterns with AI schedulers
- Suitability for heterogeneous inference clusters
