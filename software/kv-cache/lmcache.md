# LMCache

## 一句话定位

LMCache 是面向 LLM 推理的 KV Cache 管理层。它把 KV cache 从推理进程里的临时状态，提升为可复用、可迁移、可分层存储、可观测的基础设施资源。

它位于推理引擎和内存/存储/网络之间：

```text
vLLM / SGLang / Serving Worker
        │
        ▼
KV Connector
        │
        ▼
LMCache
  ├── KV Chunk 管理
  ├── Cache Metadata / Index
  ├── Store / Retrieve
  ├── Offload / Transfer
  ├── Observability
  └── SERDE / Transform
        │
        ▼
CPU RAM / SSD / Remote KV / NIXL / RDMA / TCP
```

## 边界

LMCache 不负责模型 forward，也不替代 vLLM 的请求调度器。它主要负责 KV cache 生命周期：什么时候存、存到哪里、如何查找、如何取回、如何跨 worker 传输、如何观察命中率和传输成本。

- vLLM：执行模型计算，维护活跃请求和 GPU 内 KV。
- LMCache：管理外部 KV，支持复用、卸载、传输和观测。
- llm-d / Dynamo：做更高层的请求路由、P/D 分离编排和 worker 选择。
- KAI-Scheduler / HAMi / DRA：负责 Pod 与设备资源调度。

## 为什么重要

LLM 推理分成 Prefill 和 Decode 两个阶段：

```text
Prefill：处理完整 prompt，生成 KV cache，通常更偏 compute-bound
Decode ：逐 token 生成，反复读取 KV cache，通常更偏 memory-bandwidth-bound
```

长上下文、多轮对话、RAG、Agent 场景里，system prompt、工具说明、历史对话、知识片段经常重复。如果每次都重新 Prefill，GPU 会做大量重复工作。LMCache 的价值就是把这部分重复计算沉淀成可复用 KV。

## 核心机制

### KV Chunk

LMCache 通常以 chunk 为单位管理 KV cache。chunk size 会影响命中粒度、元数据规模、传输效率和碎片率。

```text
Prompt Tokens
[0 ... 255][256 ... 511][512 ... 767]
     │           │           │
   KV Chunk    KV Chunk    KV Chunk
```

chunk 越小，复用粒度越细，但元数据和管理开销更高；chunk 越大，传输更规整，但部分命中时浪费更多。

### Offload / Retrieve

Offload 是把 KV 从 GPU HBM 移到 CPU RAM、SSD 或远端后端；Retrieve 是新请求到来时把命中的 KV 取回推理引擎可用的位置。

```text
请求进入
  → 识别可复用前缀
  → 查询 LMCache metadata
  → 命中则取回 KV chunk
  → 推理引擎跳过对应 Prefill
```

收益来自减少重复 Prefill 和释放显存；成本来自拷贝、序列化、网络和 cache miss。

### 跨实例共享

单个 vLLM 实例自带的 prefix cache 只在实例内有效。Kubernetes 多副本服务中，如果请求被随机负载均衡到不同 Pod，命中会被打散。LMCache 可以作为外部 cache 层，让多个实例共享 KV。

```text
vLLM A ─┐
        ├── LMCache shared backend
vLLM B ─┘
```

## 部署形态

### In-process 模式

LMCache 逻辑嵌入推理进程。优点是简单，适合快速验证；缺点是与推理进程耦合较强。

### Multi-process / Daemon 模式

LMCache 作为独立进程或 daemon 管理 KV，推理引擎通过 connector 访问。这个形态更适合生产，因为 KV 生命周期不完全依赖单个推理进程。

```text
vLLM Worker
   → LMCache Connector
   → LMCache Daemon
   → Local / Remote Backend
```

### Kubernetes Operator

Operator 负责在 Kubernetes 中管理 LMCacheEngine、配置注入、side-channel 参数和与 vLLM Pod 的配合。P/D 分离时，它可以帮助注入 NIXL 等传输相关配置。

## P/D 分离中的作用

P/D 分离把 Prefill 和 Decode 放到不同 worker 上：

```text
Client
  → Router / Proxy
  → Prefill Worker：计算 prompt KV
  → LMCache / NIXL：传输 KV
  → Decode Worker：读取 KV 后逐 token decode
```

生产环境重点看：

- Prefill 与 Decode 之间是否有 RDMA / NVLink / NVSwitch。
- TCP fallback 更适合开发测试，不适合高吞吐生产。
- KV 传输大小随层数、KV head 数、head dim、上下文长度和 dtype 线性增长。
- 长上下文下，KV transfer 可能吃掉网络带宽，抵消 P/D 分离收益。

## 与 llm-d 的关系

llm-d 负责请求级编排和路由，LMCache 负责 KV cache 层能力：

```text
llm-d Router / EPP
        │ 选择 worker
        ▼
vLLM Worker
        │ 读写 KV
        ▼
LMCache
        │ 传输 / 复用
        ▼
Cache Backend / NIXL
```

llm-d 可以利用 cache 状态做 prefix-aware 或 KV-aware routing；LMCache 提供实际的 cache 存取、传输和观测。

## 与客户端 KV Cache 的关系

客户端 cache 更接近业务语义，知道会话、用户、工具链、RAG 文档。LMCache 更接近运行时，知道 token chunk、KV layout、backend 和传输路径。

一种合理分工是：客户端维护“语义级 cache index”，LMCache 维护“物理级 KV cache”。客户端告诉服务端哪些前缀可能复用，服务端通过 LMCache 判断是否存在可用 KV。

## 适合场景

- 长 system prompt。
- 多轮对话历史复用。
- RAG 文档片段重复。
- Agent 工具说明和执行轨迹重复。
- P/D 分离中的 Prefill 到 Decode KV 传输。
- 多副本 serving 中跨实例复用 KV。
- GPU 显存不足，需要把冷 KV 放到 CPU/SSD/远端。

## 谨慎场景

- 请求前缀几乎不重复。
- prompt 经常包含随机数、时间戳、一次性检索结果，导致命中率低。
- 网络带宽弱但强行跨节点传输 KV。
- 模型 KV cache 极大，传输比重新计算还慢。
- 多租户场景没有清晰的权限隔离和 cache 生命周期策略。

## 性能关注点

- Cache hit ratio：命中率是收益入口。
- TTFT：命中后是否真正降低首 token 延迟。
- Store overhead：写 KV 是否阻塞正常推理。
- Retrieve overhead：取回 KV 是否比重新 Prefill 更快。
- Network bandwidth：P/D 和 remote cache 的核心瓶颈。
- Serialization cost：KV layout 转换和拷贝次数。
- NUMA locality：CPU RAM offload 时，GPU 与 CPU 内存的距离。
- Eviction policy：热 KV 是否被保留，冷 KV 是否及时淘汰。

## 异构 GPU/NPU 场景

LMCache 的方向是厂商中立，但异构环境里要注意：

- 不同推理引擎的 KV layout 可能不同。
- 不同硬件的 dtype、对齐方式、block size 可能不同。
- NVIDIA GPU 间可优先评估 NIXL/RDMA/GDS，NPU 侧需要确认对应传输栈。
- 短期更现实的路线是“同硬件池内复用 KV”，而不是跨厂商透明复用。

## 选型建议

先确认三件事：

1. workload 是否真的有可复用上下文。
2. KV 的传输和存储成本是否低于重复 Prefill。
3. 上层 router 是否能把相似请求路由到更容易命中的 worker 或 cache backend。

如果三者都成立，LMCache 是值得引入的关键层。否则它可能只是给推理系统多加一层会发热的齿轮箱。

## 后续跟踪问题

- MP 模式相对 in-process 模式的生产成熟度。
- Lazy offload 对吞吐和 cache 新鲜度的权衡。
- NIXL / Mooncake / GDS 等后端的实际性能差异。
- CacheBlend 和非前缀 KV 复用的质量风险。
- 与 llm-d / Dynamo 的标准化接口是否稳定。
- 在 Ascend、ROCm、Gaudi 等非 CUDA 生态中的落地路径。

## 参考资料

- LMCache 官方文档：https://docs.lmcache.ai/
- LMCache GitHub：https://github.com/LMCache/LMCache
- vLLM 官方文档：https://docs.vllm.ai/
- llm-d 官方文档：https://llm-d.ai/
