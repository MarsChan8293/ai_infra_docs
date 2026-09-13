# HAMi

## 一句话定位

HAMi 是 Kubernetes 上的异构 AI 加速器虚拟化和共享中间件。它的核心目标是让 GPU/NPU 等昂贵设备可以被更细粒度地分配、共享、隔离和调度，而不是只能整卡分配。

它位于设备资源层：上接 kube-scheduler、KAI-Scheduler、Volcano、Kueue 等调度层，下接 NVIDIA GPU、Ascend NPU、Cambricon、Hygon、Iluvatar、MetaX、Moore Threads 等多厂商设备后端。

```text
Pod / Job
  │
  ▼
Kubernetes Scheduler / KAI / Volcano
  │
  ▼
HAMi
  ├── Mutating Webhook
  ├── Scheduler Extender / Scheduler
  ├── Device Plugin
  ├── Device Allocation Annotations
  ├── Runtime Injection / vGPU Library
  └── Metrics / WebUI
  │
  ▼
GPU / NPU / Heterogeneous Accelerators
```

## 边界

HAMi 解决的是“设备如何暴露、共享、隔离、分配给容器”。它不是 LLM 推理引擎，也不理解 token、KV cache、P/D 分离请求流。

- vLLM：负责模型执行。
- LMCache：负责 KV cache 复用和传输。
- llm-d：负责请求级分布式推理编排。
- KAI-Scheduler：负责队列、公平性、Gang、抢占和集群级 placement。
- HAMi：负责设备层的共享、隔离、虚拟化和异构资源管理。

## 核心能力

### 1. GPU / NPU Sharing

传统 Kubernetes 扩展资源通常按整数卡申请，例如 `nvidia.com/gpu: 1`。这对 Notebook、小模型推理、低利用率开发任务很浪费。

HAMi 允许按更细粒度表达资源，例如显存、算力比例或设备数量。对 NVIDIA GPU，常见形式是：

```yaml
resources:
  limits:
    nvidia.com/gpu: 1
    nvidia.com/gpumem: 3000
```

意思是：Pod 需要 1 张物理 GPU 上的一部分显存，而不是独占整卡。

### 2. 隔离

共享如果没有隔离，就只是“大家坐在同一张卡上自觉排队”。HAMi 的关键价值之一是尽量在后端支持范围内进行显存和算力隔离。

对 NVIDIA 路径，HAMi-core / vGPU 相关组件可以通过运行时注入、CUDA API 拦截等方式，让容器只能看到或使用被分配的资源。具体隔离强度依赖 GPU 型号、驱动、CUDA、MIG/MPS/HAMi 后端实现。

### 3. Device Plugin

HAMi 通过 device plugin 把设备资源注册到 Kubernetes，让 kubelet 能把设备分配给容器。device plugin 负责发现设备、上报健康状态、响应 Allocate 请求，并注入容器所需的环境变量、设备文件或运行时参数。

```text
Device Plugin
  → register resource to kubelet
  → report allocatable capacity
  → Allocate selected device to Pod
  → inject runtime config
```

### 4. Scheduler Extender / 调度策略

HAMi 可以参与调度决策，支持 binpack、spread、拓扑感知、设备过滤等策略。

- binpack：尽量把小任务塞到少数设备，减少碎片。
- spread：把任务分散，降低争用。
- topology-aware：根据设备拓扑选择更合适的 GPU/NPU 组合。

对 AI 推理而言，topology-aware 特别重要，因为 TP/EP/P/D 分离会受到 PCIe、NUMA、NVLink、NIC 距离影响。

## 典型流程

```text
1. 用户提交带 GPU/NPU 资源请求的 Pod
2. HAMi webhook 注入或改写必要配置
3. 调度器调用 HAMi 过滤/打分逻辑
4. HAMi 选择节点和具体设备
5. 分配结果写入 Pod annotation
6. device plugin Allocate 阶段注入设备访问配置
7. 容器启动后通过 HAMi runtime/vGPU 组件访问受限资源
8. monitor 暴露设备使用指标
```

## CPU NUMA / PCIe / GPU 拓扑

你现场拍到的 CPU NUMA Align 本质上是在讲：AI Pod 不能只拿“任意 CPU + 任意 GPU”。

```text
NUMA 0: CPU cores + local memory + GPU 0-3
NUMA 1: CPU cores + local memory + GPU 4-7
```

理想情况是：

```text
Pod A
  ├── CPU cores: NUMA 0
  ├── Memory   : NUMA 0
  └── GPU      : close to NUMA 0
```

否则 CPU 访问内存、GPU DMA、Pinned Memory、KV offload、MoE expert offload 都可能跨 NUMA，增加延迟并降低带宽。

## Remote GPU

HAMi Remote GPU 可以理解为把远端机器上的 GPU 通过网络暴露给当前 Pod 使用。它更接近 GPU disaggregation / CUDA API remoting，而不是本地 PCIe GPU。

```text
Pod Node
  │
  └── Network / RDMA / TCP
          │
          ▼
      Remote GPU Node
```

适合探索 GPU 池化、低利用率任务、开发测试或大粒度计算。对 LLM 在线推理要非常谨慎，因为 kernel launch、显存拷贝、同步和 KV 访问跨网络后，延迟可能迅速放大。

## 与 KAI-Scheduler 的关系

KAI 更偏上层集群调度，HAMi 更偏设备资源管理和隔离。

```text
KAI-Scheduler：队列、配额、公平性、Gang、抢占、placement
HAMi         ：设备共享、显存/算力隔离、device plugin、异构设备
```

KAI + HAMi-core 的组合很有价值：KAI 决定共享 GPU 的调度，HAMi-core 执行容器内显存限制，避免只有调度账本、没有运行时隔离。

## 与 DRA 的关系

DRA 是 Kubernetes 的动态资源分配 API。HAMi-DRA 类组件可以把传统 GPU resource request 转换为 ResourceClaim，让设备分配进入 DRA 模型。

```text
Pod requests GPU
  → HAMi-DRA webhook
  → ResourceClaim
  → DRA allocation
  → CDI / runtime inject device
```

这对未来异构 GPU/NPU 统一资源模型很重要，但需要关注 Kubernetes 版本、feature gate、CDI、device driver 支持度。

## 适合场景

- 多租户 GPU/NPU 集群。
- Notebook、开发测试、小模型推理，整卡分配太浪费。
- 多厂商加速卡混合管理。
- 需要显存级或算力级共享。
- 需要和 KAI/Volcano/Kueue 组合做 AI workload 调度。
- 需要观察设备利用率、共享情况和分配状态。

## 谨慎场景

- 大模型 TP/EP 在线推理，一般更需要整卡和拓扑一致性。
- 强 SLA 低延迟服务，GPU sharing 可能带来干扰。
- 隔离强度依赖具体后端，不能默认等价于硬隔离。
- Remote GPU 不应简单等同于本地 GPU。
- 不同厂商设备后端能力差异大，需要逐项验证。

## 性能关注点

- 显存隔离是否真的生效。
- 共享 GPU 上不同 Pod 是否互相干扰。
- device allocation 是否造成碎片。
- NUMA/PCIe/NVLink/NIC 拓扑是否被正确利用。
- vGPU 场景下的 kernel launch、context switch、memory copy 开销。
- 指标是否能支撑租户计费和故障定位。

## 对 AI Infra 平台的启发

HAMi 可以作为异构设备资源层，但不应让上层误以为所有设备都一样。更合理的做法是：

```text
DRA/HAMi 统一资源入口
        │
        ▼
保留设备差异标签：厂商、型号、显存、拓扑、驱动、算子支持
        │
        ▼
上层调度根据模型和 SLA 做选择
```

也就是说，统一入口不是抹平差异，而是把差异变成可调度的元数据。

## 后续跟踪问题

- HAMi 与 DRA 的融合路线。
- KAI-resource-isolator 的生产成熟度。
- Ascend、Cambricon、Hygon 等后端支持到什么粒度。
- Remote GPU 在 LLM 推理中的真实可用边界。
- HAMi 与 Volcano/Kueue/KAI 的组合方式。
- GPU sharing 对 vLLM continuous batching 的干扰模型。

## 参考资料

- HAMi GitHub：https://github.com/Project-HAMi/HAMi
- HAMi 文档：https://project-hami.io/
- HAMi-DRA：https://github.com/Project-HAMi/HAMi-dra
- KAI resource isolator：https://github.com/Project-HAMi/KAI-resource-isolator
- Kubernetes DRA 文档：https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/
