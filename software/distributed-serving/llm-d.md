# llm-d

## 一句话定位

llm-d 是 Kubernetes 原生的分布式 LLM 推理编排框架。它不把每个推理进程当成孤立 endpoint，而是把一组 vLLM/SGLang 等 worker 组织成一个可路由、可扩展、可观测、可做 P/D 分离的 LLM 服务。

它位于单个推理引擎之上、业务 API 之下：

```text
Client / Gateway / API
        │
        ▼
llm-d Routing / Orchestration
  ├── 请求路由
  ├── Prefix / KV 感知
  ├── P/D 分离编排
  ├── Worker Pool 管理
  └── 故障与 rollout 处理
        │
        ▼
vLLM / SGLang Workers
        │
        ▼
GPU / NPU / KV Cache / Network
```

## 边界

llm-d 解决的是“多个推理 worker 如何协同提供一个 LLM 服务”。它不是推理 kernel，不替代 vLLM；也不是集群资源调度器，不替代 KAI-Scheduler 或 Volcano。

- vLLM/SGLang：负责模型 forward、batching、KV cache 本地管理。
- LMCache/NIXL：负责 KV cache 的复用、传输和外部化。
- llm-d：负责请求级路由、P/D 分离流程和 worker 选择。
- KAI-Scheduler/HAMi/DRA：负责 Pod 与设备资源层面的放置、共享和隔离。

## 为什么需要这一层

单个 vLLM 实例可以高效处理请求，但大规模在线服务会遇到新的问题：

- 请求应该路由到哪个 worker 才能命中 prefix cache？
- 长 prompt 的 Prefill 是否会阻塞短请求 Decode？
- Prefill 和 Decode 是否应该放在不同硬件池？
- Decode worker 挂了，正在传输的 KV 怎么处理？
- 新版本 worker 灰度发布时，旧连接和 KV 状态如何兼容？
- 多个实例之间如何避免“负载均衡很均匀，但 cache 命中率很凄凉”？

llm-d 就是在这些问题上补齐“推理语义层”的调度能力。

## 核心能力

### 1. 请求级路由

传统 Kubernetes Service 或 L7 LB 只知道 endpoint 的负载，不理解 LLM 请求里的 prompt、prefix、KV 命中和 Prefill/Decode 差异。llm-d 的路由层尝试把这些推理语义纳入选择过程。

```text
Request
  → 读取模型、prompt 特征、prefix/cache 信息
  → 选择合适 worker
  → 转发请求或编排 P/D 流程
```

### 2. Prefix / KV 感知路由

对于有共享上下文的请求，最优 worker 往往不是“当前最空闲的 worker”，而是“已经拥有或更容易获取对应 KV 的 worker”。

```text
请求 A prefix 已在 Worker 3
新请求 B 共享 prefix
  → 优先路由到 Worker 3
  → 或路由到能快速拉取 KV 的 Worker
```

这个能力需要和 vLLM prefix cache、LMCache、KV index、worker 状态观测配合。

### 3. P/D 分离编排

P/D 分离把一个请求拆成 Prefill 和 Decode 两个阶段：

```text
Client
  → llm-d Router
  → Prefill Worker：处理长 prompt，生成 KV
  → KV Transfer：NIXL / RDMA / NVLink / TCP
  → Decode Worker：逐 token 生成
```

llm-d 的价值不是单纯启动两类 Pod，而是编排整个请求流：选择 P 和 D、建立连接、处理取消、处理故障、协调 rollout、管理 KV 传输关系。

### 4. Worker Pool 编排

llm-d 可以把不同类型 worker 纳入同一服务视角：

- Prefill pool：更看重 FLOPS、长上下文吞吐、较大 batch。
- Decode pool：更看重 HBM 带宽、低 TPOT、稳定小步执行。
- 混合 pool：同一 worker 同时处理 Prefill 和 Decode。
- 异构 pool：不同 GPU/NPU、不同模型副本、不同量化版本。

## 数据路径

普通路由：

```text
Client
  → Gateway / Proxy
  → llm-d 选择 endpoint
  → vLLM worker 执行 prefill + decode
  → streaming response
```

P/D 分离：

```text
Client
  → Gateway / Proxy
  → llm-d 选择 Prefill worker 和 Decode worker
  → Prefill worker 生成 KV
  → KV 通过 NIXL / LMCache / RDMA 传到 Decode worker
  → Decode worker 持续输出 token
```

KV-aware routing：

```text
Request prefix
  → 查询 KV index / worker cache 状态
  → 选择 cache 命中概率最高且负载可接受的 worker
  → 必要时从 peer 或外部 cache 拉取 KV
```

## 控制路径

llm-d 的控制面重点包括：

- 服务发现：知道有哪些模型 worker、状态如何。
- endpoint 选择：按负载、prefix、KV、延迟预测选择 worker。
- P/D 流程控制：选择 Prefill 与 Decode 对，协调 KV transfer。
- 故障策略：worker 失败时 fail、recompute 或迁移。
- rollout 兼容：升级过程中保证连接和协议兼容。
- 指标观测：延迟、命中、队列、错误、worker 健康。

## 与 vLLM 的关系

vLLM 是 llm-d 最重要的执行后端之一：

```text
llm-d：决定请求去哪、是否拆 P/D、如何利用 KV
vLLM：执行模型 forward、维护本地 KV、流式输出 token
```

在 P/D 分离时，vLLM 需要支持对应的 KV transfer connector 和 worker 角色配置；llm-d 负责把这些 worker 编排成一条完整请求链路。

## 与 LMCache / NIXL 的关系

LMCache 提供 KV 管理和复用，NIXL 提供高性能传输抽象。llm-d 需要这些底层能力来完成跨 worker 的 KV 传输。

```text
llm-d 选择 P/D worker
  → Prefill worker 产生 KV
  → LMCache / NIXL 传输 KV
  → Decode worker 接收 KV
```

没有高性能 KV transfer，P/D 分离就容易变成“省了计算，花在搬家”。

## 与 Kubernetes 调度层的关系

llm-d 是 request 级路由，KAI-Scheduler/Volcano/Kueue 是 Pod/Job 级调度。两者应组合，而不是互相替代。

```text
KAI-Scheduler：把 Prefill/Decode worker Pod 放到合适节点
llm-d        ：在运行时把用户请求路由到合适 worker
```

对 P/D 分离来说，底层调度应尽量保证 Prefill 和 Decode 池之间有足够网络带宽，必要时考虑 RDMA NIC、NUMA、PCIe 和 NVLink/NVSwitch 拓扑。

## 典型部署形态

### 1. 多副本 vLLM 路由

```text
Gateway
  → llm-d Router
  → vLLM replicas
```

适合替代简单 round-robin，让路由开始理解 LLM 负载和 cache 状态。

### 2. P/D 分离

```text
Gateway
  → llm-d
  → Prefill Pool
  → KV Transfer
  → Decode Pool
```

适合长输入、短输出、Prefill/Decode 资源特征差异明显的业务。

### 3. 异构 Worker Pool

```text
llm-d
  ├── H20 Prefill Pool
  ├── RTX / L40S Decode Pool
  ├── Ascend NPU Pool
  └── CPU/SSD KV Cache Backend
```

这个方向对你的 AI Infra 平台很有价值：它让“按请求选择硬件”不再只是离线 benchmark，而能进入在线路由决策。

## 适合场景

- 多副本 LLM 在线服务。
- 需要 prefix/KV-aware routing。
- 长上下文 P/D 分离。
- Prefill 与 Decode 希望使用不同硬件池。
- 需要在 Kubernetes 上标准化部署和运维 LLM serving。
- 需要把 vLLM/SGLang worker 组织成一个分布式服务。

## 谨慎场景

- 单机单实例即可满足业务，llm-d 可能增加复杂度。
- 网络弱，跨节点 KV 传输收益不足。
- 请求前缀高度随机，KV-aware routing 收益有限。
- 运维团队尚未具备 Kubernetes/Gateway/observability 基础。
- 后端推理引擎的 P/D 和 KV connector 能力还在快速变化，需要持续跟踪兼容性。

## 性能关注点

- Routing latency：路由本身不能成为明显瓶颈。
- Cache hit ratio：KV-aware routing 是否真的提高命中。
- P/D transfer time：Prefill 到 Decode 的 KV 搬运时间。
- TTFT：P/D 分离后首 token 是否降低。
- TPOT/ITL：Decode pool 是否更稳定。
- Tail latency：长 prompt 是否仍然拖慢短请求。
- Failure recovery：worker 失败时是重算、迁移还是失败返回。
- Rollout impact：升级是否导致连接中断或 cache 不兼容。

## 后续跟踪问题

- llm-d 与 Gateway API、Inference Gateway、EPP 的接口稳定性。
- vLLM 与 SGLang 后端在 P/D 分离操作上的差异。
- KV index 的精确性、开销和一致性。
- prefix-aware routing 与 predicted latency routing 如何组合。
- 多租户场景下 cache 隔离、quota 和计费如何实现。
- 与 NVIDIA Dynamo 的能力边界和重叠点。

## 参考资料

- llm-d 官方文档：https://llm-d.ai/
- llm-d GitHub：https://github.com/llm-d/llm-d
- vLLM 官方文档：https://docs.vllm.ai/
- LMCache 官方文档：https://docs.lmcache.ai/
