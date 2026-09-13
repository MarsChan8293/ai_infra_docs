# vLLM

## 一句话定位

vLLM 是面向大模型推理的高吞吐推理引擎和 serving runtime，核心价值是把 GPU/NPU 上的 token 生成做得更高效、更容易服务化。

它位于软件栈的“模型执行层”：上接 llm-d、KServe、Ray Serve、业务 API 或自研 Router，下接 CUDA、ROCm、XPU/NPU 后端、NCCL/HCCL/RCCL、FlashAttention/FlashInfer/Triton 等 kernel 与通信库。

```text
Client / API / Router
        │
        ▼
vLLM OpenAI-compatible Server
        │
        ├── Request Scheduler / Continuous Batching
        ├── KV Cache Manager / PagedAttention
        ├── Model Executor / Worker
        ├── Parallelism: TP / PP / DP / EP / CP
        └── Backend Kernels / Communication
        │
        ▼
GPU / NPU / HBM / NIC
```

## 边界

vLLM 解决的是“单个或一组模型 worker 如何高效执行推理”。它不是完整的集群调度器，也不是 Kubernetes 设备资源管理器。

- vLLM 知道 request、token、batch、KV cache、模型并行。
- vLLM 通常不知道组织级 quota、全局公平性、跨团队抢占。
- vLLM 可以做前缀缓存、KV 管理、chunked prefill、speculative decoding。
- 当需要跨实例 KV 复用、P/D 分离传输、全局 request routing 时，通常需要 LMCache、llm-d、Dynamo 或自研控制面配合。

## 核心机制

### 1. Continuous Batching

传统 serving 往往把请求组成固定 batch，等 batch 内所有请求完成后再处理下一批。LLM decode 阶段每个请求生成长度不同，固定 batch 很容易产生“慢请求拖住快请求”的气泡。

Continuous batching 的思路是：每个 step 动态维护活跃请求集合，已完成的请求退出，新请求插入，让 GPU 尽量持续有活干。

```text
step t:   A B C D
step t+1: A B C E    D 完成，E 插入
step t+2: A C E F    B 完成，F 插入
```

这对吞吐非常关键，但也会带来调度问题：prefill 请求很大，decode 请求很小；长上下文请求会吃掉大量 KV；不同请求的优先级、SLA、取消和超时都要被 scheduler 处理。

### 2. PagedAttention 与 KV Cache 管理

LLM 推理的 KV cache 会随着上下文长度增长。朴素做法为每个请求预留连续显存，容易碎片化，也会因为最大长度预留导致显存浪费。PagedAttention 借鉴操作系统分页思想，把 KV cache 拆成 block/page 管理，让请求的逻辑 token 序列映射到非连续物理 cache block。

```text
Request A logical KV: [0][1][2][3][4][5]
                         │  │  │  │  │  │
Physical KV blocks:    B7 B2 B9 B3 B4 B8
```

核心收益：

- 降低 KV 显存碎片。
- 更容易支持前缀共享和 block 复用。
- 提高长上下文场景的显存利用率。
- 让调度器可以围绕 block 数量做 admission control。

### 3. Prefix Caching

当多个请求共享相同前缀时，例如 system prompt、RAG 模板、多轮对话历史，vLLM 可以复用已有前缀的 KV cache，减少重复 prefill。

```text
共享前缀: system prompt + tools + docs
请求 A: 共享前缀 + question A
请求 B: 共享前缀 + question B
              │
              └── 前缀 KV 可复用
```

注意：prefix caching 的收益高度依赖 workload。如果请求前缀不稳定、模板中包含时间戳/随机字段、RAG 文档顺序经常变化，命中率会明显下降。

### 4. Chunked Prefill

Prefill 长 prompt 时会消耗大量计算并占用调度窗口。Chunked prefill 把长 prompt 切成多个 chunk，与 decode step 穿插执行，避免长 prefill 把 decode 延迟打爆。

这对在线服务很重要，因为用户通常更敏感 TPOT/ITL，而不是单个长请求的离线吞吐。

### 5. 并行策略

vLLM 支持多种并行模式，实际可用性依赖模型结构、后端、通信库和版本。

- TP：张量并行，常用于单机多卡或高速互联多卡。
- PP：流水并行，适合模型层数切分，但在线 decode 容易有气泡。
- DP：数据并行/副本并行，适合多实例服务扩展。
- EP：专家并行，面向 MoE 模型，把不同 expert 放在不同 GPU 上。
- CP：上下文并行，面向超长上下文场景。

对 DeepSeek、Mixtral、Qwen MoE 这类模型，EP/TP 的组合、All-to-All 通信和 expert load balance 会成为推理部署的关键。

## 数据路径

```text
1. HTTP / OpenAI API 请求进入 vLLM server
2. tokenizer 将文本转 token
3. scheduler 根据请求状态组织 prefill/decode 批次
4. model executor 执行 forward
5. attention kernel 读取/写入 KV cache
6. sampler 采样下一个 token
7. detokenizer 流式返回文本
8. 请求完成后释放或保留可复用 KV block
```

其中最容易成为瓶颈的是：

- Prefill：GEMM/Attention 计算、长上下文 attention、HBM 容量。
- Decode：KV cache 读取、HBM 带宽、batch size、kernel launch overhead。
- MoE：router、expert GEMM、All-to-All、专家负载不均。
- 分布式：NCCL/RCCL/HCCL 通信、RDMA/NVLink/NVSwitch 拓扑。

## 控制路径

vLLM 的控制路径主要包括：

- admission control：请求是否能进入当前实例。
- scheduling policy：prefill 与 decode 如何混排。
- memory manager：KV block 申请、释放、复用、换出。
- distributed executor：worker 初始化、模型加载、并行组通信。
- serving control：健康检查、指标、请求取消、限流、日志。

在更大规模系统里，vLLM 实例通常不直接暴露给业务，而是由 llm-d、Dynamo、KServe 或自研 Router 做上层路由。

## 与 LMCache 的关系

LMCache 可以作为 vLLM 的外部 KV cache 管理层。典型用途：

- 把 KV cache 从 GPU 卸载到 CPU RAM、SSD 或远端存储。
- 跨 vLLM 实例复用 KV cache。
- 在 P/D 分离中把 Prefill worker 产生的 KV 传给 Decode worker。
- 提供请求级和 token 级 cache 命中观测。

组合方式可以理解为：

```text
vLLM
  ├── 执行模型 forward
  ├── 维护 GPU 内当前活跃 KV
  └── 通过 KV connector 接入 LMCache
          ├── CPU RAM
          ├── Local SSD
          ├── Redis / Valkey / S3
          ├── Mooncake
          └── NIXL / RDMA / TCP transport
```

## 与 llm-d 的关系

llm-d 通常把 vLLM 当成模型 worker。vLLM 负责单实例执行，llm-d 负责多实例编排：

- 请求路由到哪个 vLLM worker。
- 是否做 P/D 分离。
- Decode worker 是否已有对应 prefix KV。
- rollout、故障恢复、跨 worker 连接管理。

vLLM 是发动机，llm-d 是车队调度室。发动机再强，也不能替代跨机房、跨队列、跨 worker 的交通管理。

## 与 Kubernetes 调度层的关系

vLLM Pod 最终由 Kubernetes scheduler、KAI-Scheduler、Volcano 或 Kueue 调度到具体节点。对 vLLM 来说，底层 placement 会显著影响性能：

- TP 多卡应尽量落在同一 NVLink/NVSwitch 域。
- PCIe 服务器上 TP4 应尽量落在同一 CPU socket / PCIe switch 下。
- P/D 分离要求 Prefill 与 Decode 之间有高速网络，生产环境优先 RDMA。
- KV offload 到 CPU 时，需要关注 NUMA 本地性。
- MoE EP 场景需要关注 All-to-All 通信路径。

## 典型部署形态

### 单机单模型服务

```text
vllm serve <model>
```

适合开发测试、中小模型、单卡或单机多卡服务。

### Kubernetes 多副本服务

```text
Service / Ingress
  → vLLM Deployment replicas
  → GPU nodes
```

适合吞吐横向扩展，但如果没有 KV-aware routing，prefix cache 命中可能被负载均衡打散。

### 多卡张量并行服务

```text
vLLM worker group
  → TP = 2 / 4 / 8
  → NCCL / HCCL / RCCL
```

适合单卡放不下或单卡吞吐不足的模型。重点看通信拓扑。

### P/D 分离服务

```text
Router
  → Prefill vLLM worker
  → KV transfer
  → Decode vLLM worker
```

适合长输入、低 TTFT 和 decode QoS 要求高的场景。需要 LMCache/NIXL/llm-d 等组件配合。

## 适合场景

- 高吞吐在线推理。
- OpenAI-compatible API 服务。
- 多模型快速适配。
- 长上下文和 prefix cache 有收益的服务。
- NVIDIA GPU 生态优先，也可跟随社区后端支持 AMD/Intel/Ascend 等。
- 需要 continuous batching、PagedAttention、speculative decoding、量化和多并行策略的场景。

## 不适合或要谨慎的场景

- 极低延迟、小 batch、强实时场景，需要仔细压测 TPOT/ITL。
- KV 命中率低但强行引入外部 KV cache，可能得不偿失。
- 跨节点 TP，如果网络不是 NVLink/NVSwitch/RDMA 级别，通信可能成为主瓶颈。
- 非 NVIDIA 后端能力通常比 CUDA 路径更依赖版本和社区适配，选型前必须实测。

## 性能观测重点

- TTFT：首 token 延迟，受 prefill、queueing、prefix cache 命中影响。
- TPOT / ITL：逐 token 延迟，decode 阶段核心指标。
- Throughput：tokens/s、requests/s。
- KV cache hit ratio：prefix cache 或外部 cache 是否真正命中。
- GPU memory utilization：是否被 KV cache 或权重占满。
- HBM bandwidth：decode 是否 memory-bound。
- NCCL/HCCL/RCCL 通信耗时：TP/EP 场景重点。
- Queue time：continuous batching 下请求等待时间。

## 与本仓库的研究关系

vLLM 是本仓库推理软件层的基准对象。后续所有调度、KV cache、P/D 分离、异构硬件选择、客户端 KV cache 方案，都应至少回答一个问题：

> 它如何改变 vLLM 的 TTFT、TPOT、吞吐、显存占用或运维复杂度？

## 后续跟踪问题

- vLLM V1 架构下 scheduler 与 KV manager 的演进。
- P/D 分离在生产部署中的稳定性、故障恢复和 rollout 策略。
- LMCacheConnector、NIXL、Mooncake 等外部 KV 组件的成熟度。
- MoE 模型下 EP/TP/DP 的最佳组合。
- vLLM-Ascend、ROCm、Gaudi 等非 CUDA 后端的性能与功能差距。

## 参考资料

- vLLM 官方文档：https://docs.vllm.ai/
- vLLM GitHub：https://github.com/vllm-project/vllm
- LMCache vLLM 集成文档：https://docs.lmcache.ai/
- llm-d 官方文档：https://llm-d.ai/
