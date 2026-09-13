# Kubernetes DRA

## 一句话定位

DRA 是 Kubernetes 的 Dynamic Resource Allocation，动态资源分配框架。它让 Pod 可以通过 ResourceClaim 申请更复杂的设备资源，例如 GPU、NPU、FPGA、RDMA NIC 或其他加速器，而不是只能写一个简单的整数扩展资源。

可以把它理解为“设备版 PVC”：

```text
存储：StorageClass → PersistentVolumeClaim → Pod 使用存储
设备：DeviceClass  → ResourceClaim        → Pod 使用设备
```

## 为什么需要 DRA

传统 Kubernetes 设备模型常见写法是：

```yaml
resources:
  limits:
    nvidia.com/gpu: 1
```

这只能表达“我要 1 张 GPU”，但 AI workload 真正需要表达的往往是：

```text
我要一类设备：
  - 显存 >= 80GB
  - 支持某种驱动 / runtime
  - 最好在同一 NVLink / PCIe topology
  - 可以共享一部分 capacity
  - 需要 GPU + RDMA NIC 组合
  - 需要可观测的设备健康状态
```

DRA 的核心意义是把这些“设备属性、选择条件、分配结果、健康状态”纳入 Kubernetes API，而不是全部塞进厂商 device plugin 的私有注解里。

## 核心对象

### DeviceClass

DeviceClass 定义一类可申请设备，以及如何根据属性筛选设备。它更像设备资源的“类别入口”。

```text
DeviceClass: h100-gpu
  selectors:
    vendor = nvidia
    memory >= 80GB
    interconnect = nvlink
```

### ResourceClaim

ResourceClaim 描述一个 workload 对设备的申请。Pod 通过 ResourceClaim 获得某个具体设备或设备集合的访问权。

```text
ResourceClaim
  → request devices from DeviceClass
  → scheduler allocates matching devices
  → Pod scheduled to node that can access them
```

### ResourceClaimTemplate

ResourceClaimTemplate 用于为每个 Pod 自动生成类似但独立的 ResourceClaim。适合 Deployment、Job、StatefulSet 这类会创建多个 Pod 的 workload。

### ResourceSlice

ResourceSlice 由 DRA driver 发布，描述节点或资源池中的具体设备、属性、容量、健康状态等。Scheduler 通过 ResourceSlice 判断哪些节点能满足 ResourceClaim。

```text
DRA Driver
  → publishes ResourceSlice
  → Kubernetes scheduler matches ResourceClaim
  → kubelet / driver prepares device for Pod
```

## 控制路径

```text
1. 集群管理员安装支持 DRA 的 device driver
2. driver 发布 ResourceSlice
3. 管理员定义 DeviceClass
4. 用户创建 ResourceClaim 或 ResourceClaimTemplate
5. Pod 引用 ResourceClaim
6. Kubernetes scheduler 选择能满足 claim 的节点和设备
7. kubelet 与 driver 在目标节点上准备设备
8. 容器通过 CDI / runtime 配置访问设备
```

## 数据路径

DRA 本身不处理 GPU/NPU 数据传输。它只是决定“设备如何被申请和分配”。真正的数据路径仍由硬件和运行时负责：

```text
vLLM / CUDA / NPU Runtime
        │
        ▼
GPU/NPU HBM / DMA / RDMA / NVLink / PCIe
```

因此 DRA 不会自动加速推理；它让设备选择和分配更标准、更可表达。

## 与 Device Plugin 的关系

Device Plugin 是 Kubernetes 早期的设备接入机制，适合暴露简单整数资源。DRA 更适合复杂设备申请和结构化资源描述。

```text
Device Plugin:  nvidia.com/gpu = 1
DRA:            DeviceClass + ResourceClaim + ResourceSlice
```

短期内两者会长期共存：成熟生产集群可能仍大量使用 device plugin，而新型设备共享、异构资源和组合资源会逐步向 DRA 靠拢。

## 与 HAMi 的关系

HAMi 关注 GPU/NPU 共享、隔离和异构设备管理；DRA 关注 Kubernetes API 层的资源声明和分配。

```text
DRA ：标准化“我要什么设备”
HAMi：实现“设备如何共享、隔离、注入容器”
```

HAMi-DRA 这类组件的意义在于：把传统 GPU request 转换成 ResourceClaim，让 HAMi 管理的资源进入 DRA 模型。

## 与 KAI-Scheduler 的关系

KAI-Scheduler 是调度策略执行者，DRA 是设备资源表达框架。

```text
Pod / Job
  → ResourceClaim 描述设备需求
  → DRA driver 发布 ResourceSlice
  → KAI-Scheduler / kube-scheduler 做 placement
```

DRA 让调度器看到更丰富的设备属性，KAI 可以在其上叠加 queue/quota/fair-share/Gang/topology 等策略。

## 与 LLM 推理的关系

DRA 不直接理解 token、KV cache、P/D 分离，但它能为推理系统提供更好的设备表达能力。

例如：

```text
Prefill Worker 需要：高 FLOPS、大显存 GPU
Decode Worker 需要：高 HBM 带宽、低延迟 GPU
KV Transfer 需要：靠近 RDMA NIC 的 GPU
MoE Worker 需要：高速 All-to-All 拓扑
```

这些要求如果能通过 DeviceClass、ResourceClaim、设备属性和 topology 信息表达，就能让上层 AI Infra 控制面做更准确的部署决策。

## Consumable Capacity

DRA 的 consumable capacity 方向用于表达设备可被多个 ResourceClaim 消耗一部分 capacity，类似 Pod 共享 Node CPU/Memory。

这对 GPU sharing 很关键：

```text
GPU total memory: 80GB
  → Claim A consumes 20GB
  → Claim B consumes 30GB
  → Claim C consumes 10GB
```

但这类能力需要 DRA driver、scheduler、runtime、隔离机制共同支持。API 能表达，不代表底层一定能强隔离。

## Device Taints / Health

DRA 也在增强设备级健康状态、taint/toleration 和 ResourceClaim status 等机制。

这对 AI 集群很有用：

- 单张 GPU/NPU 发生 ECC、Xid、驱动异常时，不必简单把整节点打坏。
- 设备维护可以更细粒度地把某类或某张设备标记为不可用。
- 控制面可以根据 ResourceClaim 状态做故障恢复。

## 适合场景

- 异构 GPU/NPU 集群。
- 需要表达设备属性、型号、拓扑、容量的工作负载。
- GPU + RDMA NIC 等组合资源申请。
- 设备共享和部分 capacity 分配。
- 希望减少厂商私有 annotation，走 Kubernetes 标准资源模型。
- 面向未来的 AI Infra 控制面。

## 谨慎场景

- Kubernetes 版本较旧，DRA 支持不完整。
- 厂商 DRA driver 不成熟。
- 现有 Device Plugin 方案已经稳定，迁移成本较高。
- 期望 DRA 自动解决 GPU 隔离、KV 传输或推理路由，这是误解。
- 调度器和 runtime 不支持对应 DRA 特性时，API 表达能力无法落地。

## 对异构 AI Infra 的价值

DRA 最适合作为“统一资源声明层”。但统一不是把所有硬件伪装成一样，而是把差异结构化：

```text
Device attributes:
  vendor: nvidia / ascend / amd / cambricon
  memory: 80GB / 96GB / 144GB
  interconnect: pcie / nvlink / hccs / roce
  numa: socket0 / socket1
  role_suitability: prefill / decode / moe / kv-transfer
```

上层控制面可以基于这些属性选择：

- DeepSeek 类 MoE 用哪类卡。
- Prefill 和 Decode 是否拆到不同资源池。
- KV transfer 是否要求 RDMA 邻近。
- 小模型服务是否走 HAMi sharing。
- 大模型 TP 是否要求同 NVLink/NVSwitch 域。

## 与本仓库研究方向的关系

DRA 是连接“硬件差异”和“软件调度”的关键接口。对于你的 AI Infra 平台，它可以承载硬件事实；KAI-Scheduler 使用这些事实做 Pod placement；llm-d/Dynamo 使用运行时状态做 request routing；vLLM/LMCache 执行推理和 KV 管理。

```text
DRA：设备事实层
KAI：部署调度层
llm-d：请求路由层
vLLM：模型执行层
LMCache：KV 状态层
```

## 后续跟踪问题

- Kubernetes v1.35 之后 DRA stable 能力与 alpha/beta 子特性的边界。
- DRA consumable capacity 在 GPU sharing 中的真实落地。
- NVIDIA、Ascend、AMD 等厂商 DRA driver 成熟度。
- DRA 与 CDI、Device Plugin、GPU Operator 的迁移关系。
- KAI-Scheduler 对 DRA 资源的调度策略支持。
- HAMi-DRA 是否能成为从传统 GPU request 迁移到 DRA 的过渡方案。

## 参考资料

- Kubernetes DRA 文档：https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/
- Kubernetes v1.34 DRA 文档：https://v1-34.docs.kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/
- HAMi-DRA：https://github.com/Project-HAMi/HAMi-dra
- KAI-Scheduler GitHub：https://github.com/kai-scheduler/KAI-Scheduler
- HAMi GitHub：https://github.com/Project-HAMi/HAMi
