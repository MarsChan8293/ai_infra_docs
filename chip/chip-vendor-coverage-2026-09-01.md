# AI 芯片厂家覆盖汇总

- 研究截止日：2026-09-02
- 实际识别厂家目录：18 个；用户新增 OpenAI 与小米后，`openai/` 纳入研究，新增 `Xiaomi/` 作为厂家目录。
- 各家报告区分芯片、板卡、模块、服务器、机架、云服务及公告/量产/出货/部署/云可用状态。
- 当前完整度统计：已完成 8 家、部分完成 9 家、资料不足 1 家。部分完成表示已有详细报告但仍有关键历史型号或商业可用性字段缺少公开一手证据；小米的资料不足主要指数据中心通用加速器证据不足，不代表端侧芯片没有公开资料。

| 厂家 | 最新芯片 | 主要架构路线 | 主要用途 | 当前状态 | 内存 | 互联 | 功耗 | 软件栈 | 报告链接 | 完整度 |
| -- | ---- | ------ | ---- | ---- | -- | -- | -- | --- | --- | --- |
| AMD | MI455X | CDNA5、HBM4、UALink | 训练/推理/HPC | 已发布，Helios 预计 2026 下半年部署 | 432GB HBM4 | 3.6TB/s GPU-GPU | 单GPU未确认 | ROCm | [报告](./AMD/AMD-overview.md) | 部分完成 |
| AWS | Trainium3 | NeuronCore、HBM3e、NeuronLink | 云训练/推理 | Trn3 GA；Trainium4 路线图 | 144GB HBM3e | NeuronLink/NeuronSwitch | 单芯片未确认 | Neuron/NKI | [报告](./AWS/AWS-overview.md) | 部分完成 |
| Biren | BR166/BR20X | 通用GPU、BLink | 训练/推理 | BR106/110/166 有产品/交付证据；BR20X 路线图 | 见报告 | BLink/系统互联 | BR166C 300W与旧披露450W并列 | BIRENSUPA | [报告](./Biren/壁仞科技-概览.md) | 已完成 |
| Cambricon | 思元/MLU590在研 | MLU/NPU | 数据中心训练/推理 | MLU370/270/220可见；MLU590在研；MLU690未确认 | 见报告 | 未完整公开 | 多数未确认 | NeuWare/SDK | [报告](./Cambricon/寒武纪-概览.md) | 部分完成 |
| Cerebras | WSE-3/CS-4 | 晶圆级、片上SRAM | 训练/推理 | 产品资料公开，出货细节有限 | SRAM/系统外存分开 | 晶圆级/系统级 | 分层记录 | Cerebras SDK | [报告](./Cerebras/Cerebras-overview.md) | 部分完成 |
| Enflame | L600 | GCU | 训练/推理 | S60量产上市；L600回片但未大规模量产交付 | 见报告 | GCU/POD分开 | 卡/模组口径 | TopsRider | [报告](./Enflame/燧原科技-概览.md) | 已完成 |
| Google | TPU7x/Ironwood | TPU、ICI、SparseCore | 云训练/推理 | Ironwood GA；TPU8t/8i Coming soon | 见报告 | ICI/Pod | 云实例/系统分开 | XLA/JAX | [报告](./Google/Google-overview.md) | 已完成 |
| Groq | Groq3 LPX | SRAM-first LPU | 低延迟推理 | 纳入Vera Rubin平台；供货未确认 | SRAM/DDR分开 | C2C/LPX | LP30未确认 | Groq runtime | [报告](./Groq/Groq-overview.md) | 部分完成 |
| Huawei | Ascend 950PR/DT | NPU、Cube/Vector、统一总线 | Prefill/Decode/训练 | PR卡有上市证据；DT/超节点展示，普遍供货未确认 | PR/DT分开 | Unified Bus/URMA | 芯片未确认 | CANN/MindSpore | [报告](./Huawei/华为-概览.md) | 部分完成 |
| Hygon | 深算三号 | DCU、CPU/DCU | 国产服务器/训练/推理 | 深算三号有市场状态；新代际研发边界 | 不完整 | 资料有限 | 未确认 | DTK | [报告](./Hygon/海光信息-概览.md) | 已完成 |
| Iluvatar | 天垓300 | GPGPU、推理/训练线 | 训练/推理/边端 | 2026-07-19发布；其余状态分产品记录 | 见报告 | 卡/模组/系统分开 | 未确认项列出 | ILIAS | [报告](./Iluvatar/天数智芯-概览.md) | 已完成 |
| Kunlunxin | 三代/P800相关 | 专用AI加速器/超节点 | 云训练/推理 | 三代公开；P800未确认项单列 | 见报告 | 芯片/模组/服务器分开 | 多数未确认 | XPU/XTDK | [报告](./Kunlunxin/昆仑芯-概览.md) | 已完成 |
| MetaX | C600/C500 | 国产GPGPU | 训练/推理/HPC | C600状态分开；C500量产日期冲突 | 见报告 | 卡/模组/服务器分层 | 见报告 | MXMACA | [报告](./MetaX/沐曦-概览.md) | 已完成 |
| MooreThreads | S5000/PH100 | 全功能GPU、MUSA/MTLink | 训练/推理/图形 | 产品资料公开，交付/云可用按型号区分 | 见报告 | MTLink/系统级 | 见报告 | MUSA | [报告](./MooreThreads/摩尔线程-概览.md) | 已完成 |
| NVIDIA | Rubin/Rubin CPX | Tensor Core、HBM4、TMA、NVLink6 | 前沿训练/推理/长上下文 | Rubin量产爬坡；CPX预计2026年底 | Rubin 288GB HBM4；CPX 128GB GDDR7 | NVLink6/NVL72分开 | 单GPU未确认 | CUDA/TensorRT | [报告](./NVIDIA/NVIDIA-overview.md) | 部分完成 |
| Sunrise | 启望S3 | 推理优先GPGPU、低精度、SIRE | 大模型/智能体推理 | S1/S2/S3公开；S2称规模化量产；S3供货未确认 | LPDDR6/5X，容量未确认 | PCIe Gen6；SC3系统级 | 未确认 | SIRE/vLLM等 | [报告](./Sunrise/曦望-概览.md) | 部分完成 |
| OpenAI | Jalapeño | OpenAI设计、Broadcom实现、Ethernet系统 | LLM推理 | 2026-06披露；tape-out、工程样片、初步实测；量产/出货/云可用未确认 | 未公开 | Broadcom网络方案；芯片协议未公开 | 未公开 | OpenAI serving/kernel；公开芯片 SDK 未确认 | [报告](./openai/openai-overview.md) | 部分完成 |
| 小米 Xiaomi | 玄戒 O1/O3、O100、D100 | 移动 SoC、端侧高带宽 AI、智驾 | 端侧 AI、影像、智能驾驶 | O1已搭载出货；O100/D100计划后续商用；数据中心通用加速器未确认 | O100 3.5GB专用内存、1.22TB/s为转载发布信息 | 端侧片上互联；跨卡未确认 | 未公开 | HyperOS/端侧 AI；独立加速器栈未确认 | [报告](./Xiaomi/小米-概览.md) | 资料不足 |

## 覆盖矩阵

| 厂家 | 目录 | 现有资料 | 是否仅占位 README | 待研究产品 | 负责人 | 状态 |
| -- | -- | ---- | ------------ | ----- | --- | --- |
| AMD | `AMD/` | 详细报告 | 否 | 全家族逐字段复核 | 主线 | 部分完成 |
| AWS | `AWS/` | 详细报告 | 否 | Trainium/Inferentia全家族 | 主线 | 部分完成 |
| Biren | `Biren/` | 详细报告 | 否 | BR全家族 | 子智能体 | 已完成 |
| Cambricon | `Cambricon/` | 详细报告 | 否 | MLU/思元全家族 | 子智能体 | 部分完成 |
| Cerebras | `Cerebras/` | 详细报告 | 否 | WSE/CS全家族 | 主线 | 部分完成 |
| Enflame | `Enflame/` | 详细报告 | 否 | GCU/系统 | 子智能体 | 已完成 |
| Google | `Google/` | 详细报告 | 否 | TPU全家族 | 主线 | 已完成 |
| Groq | `Groq/` | 详细报告 | 否 | LPU/LPX全家族 | 主线 | 部分完成 |
| Huawei | `Huawei/` | 详细报告 | 否 | Ascend/Atlas全家族 | 主线 | 部分完成 |
| Hygon | `Hygon/` | 详细报告 | 否 | CPU/DCU/加速卡 | 子智能体 | 已完成 |
| Iluvatar | `Iluvatar/` | 详细报告 | 否 | GPU/卡/系统 | 子智能体 | 已完成 |
| Kunlunxin | `Kunlunxin/` | 详细报告 | 否 | AI芯片/卡/服务器 | 子智能体 | 已完成 |
| MetaX | `MetaX/` | 详细报告 | 否 | GPU/卡/服务器 | 子智能体 | 已完成 |
| MooreThreads | `MooreThreads/` | 详细报告 | 否 | GPU/系统 | 子智能体 | 已完成 |
| NVIDIA | `NVIDIA/` | 详细报告 | 否 | GPU/加速器全家族 | 主线 | 部分完成 |
| Sunrise | `Sunrise/` | 详细报告 | 否 | 推理GPU/卡/系统 | 主线 | 部分完成 |
| OpenAI | `openai/` | 详细报告 | 否 | Jalapeño及合作基础设施边界 | 子智能体 | 部分完成 |
| 小米 Xiaomi | `Xiaomi/` | 详细报告 | 否 | 玄戒/澎湃/O100/D100及数据中心边界 | 子智能体 | 资料不足 |

## 完成前检查与遗留项

- 目录扫描数与汇总表均为 16；与预期厂家名单一致。
- 每家均有详细报告或原有详细报告；占位 README 均已加入索引。
- 仍缺失的关键资料集中在历史型号的流片/送样/出货日期、单芯片 TDP、完整数据表、客户部署和云实例可用性；各报告已写“公开资料未确认”。
- 已保留并标注的冲突包括 AWS 带宽 4.9/4.7TB/s、AMD/Biren 不同层级或版本功耗/带宽、MetaX C500量产日期；未把路线图、演示或宣传性能写成量产/独立实测。
- 未完全可访问的厂商动态官网或 PDF 均在对应报告中标记；没有用搜索摘要替代实际页面证据。
