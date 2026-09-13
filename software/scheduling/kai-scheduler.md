# KAI-Scheduler

## 一句话定位

KAI-Scheduler 是面向 AI/GPU 工作负载的大规模 Kubernetes 调度器。它的核心目标是比原生 kube-scheduler 更懂训练、推理、多 GPU、多租户和队列公平性。

它位于集群调度层：上接用户提交的 Pod、Job、RayJob、Kubeflow/训练任务或推理 worker，下接 Kubernetes Node、GPU/NPU 资源、DRA、Device Plugin、HAMi 等设备层组件。

```text
AI Workload / Queue / Namespace
        │
        ▼
KAI-Scheduler
  ├── Queue / Quota
  ├── Fair-share / DRF
  ├── Gang Scheduling
  ├── Priority / Preemption
  ├── Binpack / Spread
  ├── GPU Sharing
  └── Topology-aware Placement
        │
        ▼
Kubernetes Nodes + GPU/NPU Resources
```

## 边界

KAI-Scheduler 负责 Pod/Job 级 placement，不负责 LLM request 级路由。

- 它知道“这个 Pod/Job 应该放到哪个节点、使用哪些资源”。
- 它通常不知道“这个用户请求的 prefix KV 在哪个 vLLM worker 上”。
- 它可以帮助 Prefill/Decode worker 落到合适的节点池。
- 但 P/D 分离中的单个请求流、KV 传输和 worker pair 选择，仍应由 llm-d、Dynamo 或自研 Router 处理。

## 核心能力

### 1. Queue / Quota

KAI-Scheduler 的队列是资源治理的核心。队列可承载 quota、limit、over-quota weight、priority 等策略。

```text
root queue
  ├── team-a queue: quota 80 GPU, limit 120 GPU
  └── team-b queue: quota 40 GPU, limit 80 GPU
```

这适合多团队共享 GPU 集群：既保证基础配额，又允许空闲资源被其他队列临时使用。

### 2. Fair-share / DRF

在多资源场景里，公平不能只看 GPU 数量，还要看 CPU、Memory、GPU、甚至其他扩展资源。Dominant Resource Fairness 的思路是看每个队列最稀缺资源的占用比例，避免某个队列通过占满非 GPU 资源间接挤压其他队列。

### 3. Gang Scheduling

分布式训练或大模型推理 worker group 常常要求一组 Pod 同时可运行。如果只调度到一部分，任务也无法启动，还会占住资源。Gang Scheduling 的原则是：要么一组 Pod 全部满足，要么先不启动。

```text
TP8 / Training Job
  needs: 8 GPU Pods
  result: all scheduled or none scheduled
```

这对 TP、PP、EP、Ray、MPI、PyTorchJob 等多 Pod 工作负载很重要。

### 4. Priority / Preemption

KAI-Scheduler 可以围绕优先级和可抢占性做资源回收。需要注意：高优先级和“是否允许抢占别人”最好分开建模，否则会出现所有高优任务都变成资源推土机的问题。

### 5. Binpack / Spread

- Binpack：尽量把任务压到较少节点，减少碎片，便于释放整机。
- Spread：把任务分散到更多节点，降低单点故障和局部资源争用。

AI 推理一般需要结合场景选择：

```text
小模型多副本：可 binpack，提高利用率
关键在线服务：可 spread，提高容错
TP 多卡实例：优先 topology-aware，而不是简单 binpack/spread
```

### 6. GPU Sharing

KAI-Scheduler 支持 GPU sharing 场景，用于把一张 GPU 分配给多个小 workload。这里要区分两件事：

- 调度层知道“某 Pod 申请了部分 GPU 资源”。
- 运行时是否真的隔离显存/算力，需要 HAMi-core、MIG、MPS 或厂商能力配合。

如果没有底层隔离，GPU sharing 很容易只停留在账本层。

### 7. Topology-aware Placement

大模型推理和训练对拓扑非常敏感：

- TP4 最好在同一 PCIe switch 或同一 NUMA 下。
- TP8 最好在 NVLink/NVSwitch 域内。
- P/D 分离需要 Prefill 和 Decode 池之间有高速网络。
- EP/MoE 需要关注 All-to-All 路径。
- CPU offload / KV offload 需要关注 CPU NUMA 与 GPU 亲和性。

因此调度器不能只问“还有几张卡”，还要问“这些卡彼此怎么连、离 NIC 多远、离 CPU memory 多远”。

## 与 HAMi 的关系

KAI 更像上层调度大脑，HAMi 更像设备资源和隔离执行层。

```text
KAI-Scheduler：谁先跑、跑哪里、队列公平性、Gang、抢占
HAMi         ：GPU/NPU 如何共享、隔离、虚拟化、暴露给容器
```

在 KAI + HAMi-core 的组合里，KAI 可以负责 GPU sharing 的调度决策，HAMi-core 通过 CUDA 拦截等方式执行显存隔离。这样避免“调度器说你只能用 2GB，但进程实际看到整卡”的问题。

## 与 DRA 的关系

DRA 是 Kubernetes 的动态资源分配 API。KAI-Scheduler 可以利用 DRA 暴露出的更丰富设备信息做调度，例如设备类别、属性、ResourceClaim、ResourceSlice 等。

```text
Pod / Job
  → ResourceClaim
  → DRA Driver publishes ResourceSlice
  → KAI-Scheduler uses richer resource information
  → Pod placed on node with matching devices
```

DRA 不是 KAI 的替代品，而是设备资源描述和分配框架；KAI 是调度策略执行者。

## 与 llm-d 的关系

llm-d 是 request 级调度，KAI 是 Pod/Job 级调度。

```text
KAI-Scheduler：把 Prefill/Decode worker 放到合适机器
llm-d        ：把每个用户请求路由到合适 worker
```

一个完整 LLM serving 平台通常需要两级调度：

1. 部署时：KAI 决定 worker Pod 的位置和资源。
2. 运行时：llm-d 决定请求应该进入哪个 worker 或 P/D worker pair。

## 典型部署形态

### 多租户训练/推理混部

```text
team queues
  → KAI-Scheduler
  → GPU cluster
```

适合统一管理训练、微调、评测、推理、小实验。

### 大模型推理 worker group

```text
Deployment / StatefulSet / RayCluster
  → KAI-Scheduler placement
  → vLLM/SGLang workers
```

适合控制 TP/PP/EP 多 Pod、多 GPU worker 的放置和拓扑。

### KAI + HAMi GPU Sharing

```text
Pod requests partial GPU
  → KAI schedules
  → HAMi-core enforces memory isolation
  → Container runs on shared GPU
```

适合 Notebook、小模型推理、低利用率实验任务。

## 适合场景

- 多团队共享 GPU/NPU 集群。
- 训练、推理、Notebook、评测混部。
- 大规模多 Pod AI workload。
- 需要 queue/quota/fair-share/preemption。
- 需要 Gang Scheduling。
- 需要 GPU 拓扑感知调度。
- 希望和 GPU sharing、DRA、HAMi 等设备层能力组合。

## 谨慎场景

- 只有少量节点，原生 kube-scheduler 已足够。
- 只有单实例推理服务，问题主要在 vLLM 参数和模型 kernel。
- 期望调度器自动解决 request 级 KV 命中，这是 llm-d/Dynamo/Router 的职责。
- 异构 NPU 场景下，如果设备插件和资源模型不统一，调度策略会变得碎片化。

## 性能与运维关注点

- Scheduling latency：大规模 Pod 提交时调度耗时。
- Queue wait time：不同队列等待是否符合预期。
- GPU fragmentation：是否产生很多无法组成 TP/PP worker 的碎片资源。
- Topology quality：分配的 GPU 是否跨 NUMA、跨 PCIe switch、跨慢链路。
- Preemption impact：抢占是否导致在线推理抖动。
- Fairness：是否既保证 quota，又能利用空闲资源。
- Explainability：调度失败是否能通过事件解释清楚。

## 对 AI Infra 平台的启发

KAI-Scheduler 可以作为你的“集群资源调度底座”，但不应该承担全部智能。更合理的架构是：

```text
模型画像 / Benchmark / SLA / 成本模型
        │
        ▼
AI Infra Control Plane
        │
        ├── 部署级决策：用 KAI 调度 worker
        ├── 设备级决策：用 DRA/HAMi 描述和隔离设备
        └── 请求级决策：用 llm-d/Dynamo/自研 Router 路由请求
```

也就是说，KAI 负责“把兵部署到战场”，llm-d 负责“每个请求派哪支小队出击”。

## 后续跟踪问题

- KAI 对 DRA 的支持边界，尤其是 NVIDIA ComputeResources、GB200/GB300 类资源。
- KAI + HAMi-core 的 GPU sharing 隔离成熟度。
- topology-aware scheduling 在真实 8 卡 PCIe、NVSwitch、RoCE 集群中的效果。
- 与 Volcano/Kueue 的边界：训练队列、批任务和推理服务谁更适合。
- 抢占对在线推理 SLA 的影响。
- 异构 GPU/NPU 资源的统一建模方式。

## 参考资料

- KAI-Scheduler GitHub：https://github.com/kai-scheduler/KAI-Scheduler
- KAI Queue 文档：https://github.com/kai-scheduler/KAI-Scheduler/tree/main/docs/queues
- HAMi GitHub：https://github.com/Project-HAMi/HAMi
- KAI resource isolator：https://github.com/Project-HAMi/KAI-resource-isolator
- Kubernetes DRA 文档：https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/
