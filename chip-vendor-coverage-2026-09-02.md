# AI 芯片厂家覆盖汇总


## 按芯片拆分索引

| 厂家目录 | 芯片拆分索引 |
| -- | -- |
| AMD | [chip-index.md](./AMD/chip-index.md) |
| AWS | [chip-index.md](./AWS/chip-index.md) |
| Biren | [chip-index.md](./Biren/chip-index.md) |
| Cambricon | [chip-index.md](./Cambricon/chip-index.md) |
| Cerebras | [chip-index.md](./Cerebras/chip-index.md) |
| Enflame | [chip-index.md](./Enflame/chip-index.md) |
| Google | [chip-index.md](./Google/chip-index.md) |
| Groq | [chip-index.md](./Groq/chip-index.md) |
| Huawei | [chip-index.md](./Huawei/chip-index.md) |
| Hygon | [chip-index.md](./Hygon/chip-index.md) |
| Iluvatar | [chip-index.md](./Iluvatar/chip-index.md) |
| Kunlunxin | [chip-index.md](./Kunlunxin/chip-index.md) |
| MetaX | [chip-index.md](./MetaX/chip-index.md) |
| MooreThreads | [chip-index.md](./MooreThreads/chip-index.md) |
| NVIDIA | [chip-index.md](./NVIDIA/chip-index.md) |
| Sunrise | [chip-index.md](./Sunrise/chip-index.md) |
| Xiaomi | [chip-index.md](./Xiaomi/chip-index.md) |
| openai | [chip-index.md](./openai/chip-index.md) |

拆分页以各厂家综合报告为事实来源，保留芯片与板卡、模组、服务器、机架、云服务的层级边界。
- 研究截止日：2026-09-02
- 覆盖规则：一级非隐藏、非构建/临时目录中含芯片 Markdown 资料的厂家目录；用户新增 OpenAI 与小米后共 18 家。
- 证据规则：重要结论优先采用实际打开的官方页面、公告、数据表、开发文档或可核验基准；公告、流片、量产、出货、客户部署和云可用分开记录。

| 厂家 | 最新芯片 | 主要架构路线 | 主要用途 | 当前状态 | 内存 | 互联 | 功耗 | 软件栈 | 报告链接 | 完整度 |
| -- | ---- | ------ | ---- | ---- | -- | -- | -- | --- | --- | --- |
| AMD | MI455X | CDNA5、HBM4、UALink | 训练/推理/HPC | 已发布；Helios 计划 2026 下半年部署 | 432GB HBM4 | GPU-GPU 3.6TB/s（系统口径） | 单 GPU 未确认 | ROCm | [报告](./AMD/05-amd-instinct.md) | 部分完成 |
| AWS | Trainium3 | NeuronCore、HBM3e、NeuronLink | 云训练/推理 | Trn3 GA；后续代际为路线图 | 144GB HBM3e | NeuronLink/NeuronSwitch | 单芯片未确认 | Neuron/NKI | [报告](./AWS/06-aws-trainium.md) | 部分完成 |
| Biren | BR166/BR20X | 通用 GPU、BLink | 训练/推理 | 部分型号有产品/交付证据；BR20X为路线图 | 见报告 | BLink/系统互联 | 型号口径冲突已列出 | BIRENSUPA | [报告](./Biren/biren-chips-2026-09-01.md) | 已完成 |
| Cambricon | MLU/思元系列 | MLU/NPU | 训练/推理 | MLU370/270/220可核验；MLU690未充分确认 | 见报告 | 部分未公开 | 多数未确认 | NeuWare/SDK | [报告](./Cambricon/cambricon-chips-2026-09-01.md) | 部分完成 |
| Cerebras | WSE-3/CS-4 | 晶圆级、片上 SRAM | 训练/推理 | 产品公开；出货细节有限 | SRAM/系统外存分开 | 晶圆级/系统级 | 分层记录 | Cerebras SDK | [报告](./Cerebras/04-cerebras-wse.md) | 部分完成 |
| Enflame | L600 | GCU | 训练/推理 | S60量产上市；L600量产交付未充分确认 | 见报告 | GCU/POD分开 | 卡/模组口径 | TopsRider | [报告](./Enflame/enflame-chips-2026-09-01.md) | 已完成 |
| Google | TPU7x/Ironwood | TPU、ICI、SparseCore | 云训练/推理 | Ironwood GA；TPU8系列为 Coming soon | 见报告 | ICI/Pod | 云实例/系统分开 | XLA/JAX | [报告](./Google/03-google-ironwood.md) | 已完成 |
| Groq | Groq3 LPX | SRAM-first LPU | 低延迟推理 | 纳入平台；供货状态未完全确认 | SRAM/DDR分开 | C2C/LPX | 未确认 | Groq runtime | [报告](./Groq/07-groq-lpu.md) | 部分完成 |
| Huawei | Ascend 950PR/DT | NPU、Cube/Vector | Prefill/Decode/训练 | PR卡有上市证据；DT/超节点部署边界未完全确认 | PR/DT分开 | Unified Bus/URMA | 芯片未确认 | CANN/MindSpore | [报告](./Huawei/02-huawei-ascend.md) | 部分完成 |
| Hygon | 深算三号 | DCU、CPU/DCU | 国产服务器/训练/推理 | 深算三号有市场状态；新代际边界有限 | 不完整 | 资料有限 | 未确认 | DTK | [报告](./Hygon/hygon-chips-2026-09-01.md) | 已完成 |
| Iluvatar | 天垓300 | GPGPU、推理/训练 | 训练/推理/边端 | 2026-07发布；各产品状态分开 | 见报告 | 卡/模组/系统分开 | 未确认项列出 | ILIAS | [报告](./Iluvatar/iluvatar-chips-2026-09-01.md) | 已完成 |
| Kunlunxin | 三代/P800相关 | 专用 AI 加速器/超节点 | 云训练/推理 | 三代公开；P800未确认项单列 | 见报告 | 芯片/模组/服务器分开 | 多数未确认 | XPU/XTDK | [报告](./Kunlunxin/kunlunxin_product_research_2026-09-01.md) | 已完成 |
| MetaX | C600/C500 | 国产 GPGPU | 训练/推理/HPC | C600状态分开；C500量产日期冲突 | 见报告 | 卡/模组/服务器分层 | 见报告 | MXMACA | [报告](./MetaX/沐曦MetaX产品与技术研究-2026-09-01.md) | 已完成 |
| MooreThreads | S5000/PH100 | 全功能 GPU、MUSA/MTLink | 训练/推理/图形 | 产品公开；交付/云可用按型号区分 | 见报告 | MTLink/系统级 | 见报告 | MUSA | [报告](./MooreThreads/moore-threads-chips-2026-09-01.md) | 已完成 |
| NVIDIA | Rubin/Rubin CPX | Tensor Core、HBM4、NVLink6 | 前沿训练/推理/长上下文 | Rubin量产爬坡；CPX为2026计划 | 288GB HBM4；CPX 128GB GDDR7 | NVLink6/NVL72分开 | 单 GPU 未确认 | CUDA/TensorRT | [报告](./NVIDIA/01-nvidia.md) | 部分完成 |
| Sunrise | 启望S3 | 推理优先 GPGPU、低精度 | 大模型/智能体推理 | S2规模化量产为厂商表述；S3供货未确认 | 容量未确认 | PCIe Gen6；系统级单列 | 未确认 | SIRE/vLLM等 | [报告](./Sunrise/sunrise-chips-2026-09-01.md) | 部分完成 |
| OpenAI | Jalapeño | OpenAI设计、Broadcom实现、Ethernet系统 | LLM推理 | 2026-06披露；tape-out、工程样片、初步实测；量产/出货/云可用未确认 | 未公开 | Broadcom网络方案；芯片协议未公开 | 未公开 | OpenAI serving/kernel；公开芯片 SDK 未确认 | [报告](./openai/OpenAI_芯片与AI基础设施洞察_2026-09-02.md) | 部分完成 |
| 小米 Xiaomi | 玄戒 O1/O3、O100、D100 | 移动 SoC、端侧高带宽 AI、智驾 | 端侧 AI、影像、智能驾驶 | O1已搭载出货；O100/D100计划后续商用；数据中心通用加速器未确认 | O100 3.5GB专用内存、1.22TB/s为转载发布信息 | 端侧片上互联；跨卡未确认 | 未公开 | HyperOS/端侧 AI；独立加速器栈未确认 | [报告](./Xiaomi/xiaomi-ai-chip-report.md) | 资料不足 |

## 覆盖与核验结论

- 实际识别并纳入汇总的厂家目录：18 个；每个目录均有至少一份详细报告或资料不足说明。
- 新增 OpenAI 报告确认 Jalapeño 的状态边界；新增小米报告将手机 SoC、端侧 AI 加速芯片和智驾芯片分开，未将其升级为数据中心通用 AI 加速器。
- 主要遗留项仍是历史型号的流片/送样/出货日期、单芯片功耗、完整内存与互联数据、客户部署和云实例可用性；报告中均按“公开资料未确认”处理。
- `openai/` 原先因无 Markdown 被排除，现已纳入；`Xiaomi/` 为本次新增厂家目录。原有 `chip-vendor-coverage-2026-09-01.md` 保留作为前一轮工作记录。
