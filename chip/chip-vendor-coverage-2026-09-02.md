# AI 芯片厂家覆盖汇总

[项目总入口](./00-project-index.md)


## 厂家总描述文档

| 厂家目录 | 唯一总描述文档 |
| -- | -- |
| AMD | [AMD-overview](./AMD/AMD-overview.md) |
| AWS | [AWS-overview](./AWS/AWS-overview.md) |
| Biren | [壁仞科技-概览](./Biren/壁仞科技-概览.md) |
| Cambricon | [寒武纪-概览](./Cambricon/寒武纪-概览.md) |
| Cerebras | [Cerebras-overview](./Cerebras/Cerebras-overview.md) |
| d-Matrix | [d-Matrix-overview](./d-Matrix/d-Matrix-overview.md) |
| Enflame | [燧原科技-概览](./Enflame/燧原科技-概览.md) |
| FuriosaAI | [FuriosaAI-overview](./FuriosaAI/FuriosaAI-overview.md) |
| Google | [Google-overview](./Google/Google-overview.md) |
| Groq | [Groq-overview](./Groq/Groq-overview.md) |
| Huawei | [华为-概览](./Huawei/华为-概览.md) |
| Hygon | [海光信息-概览](./Hygon/海光信息-概览.md) |
| Iluvatar | [天数智芯-概览](./Iluvatar/天数智芯-概览.md) |
| Kunlunxin | [昆仑芯-概览](./Kunlunxin/昆仑芯-概览.md) |
| MetaX | [沐曦-概览](./MetaX/沐曦-概览.md) |
| MooreThreads | [摩尔线程-概览](./MooreThreads/摩尔线程-概览.md) |
| NVIDIA | [NVIDIA-overview](./NVIDIA/NVIDIA-overview.md) |
| Sunrise | [曦望-概览](./Sunrise/曦望-概览.md) |
| Tenstorrent | [Tenstorrent-overview](./Tenstorrent/Tenstorrent-overview.md) |
| Xiaomi | [小米-概览](./Xiaomi/小米-概览.md) |
| openai | [openai-overview](./openai/openai-overview.md) |

各厂家总描述文档是芯片页的事实来源和导航中心，保留芯片与板卡、模组、服务器、机架、云服务的层级边界；芯片页通过双向内部链接回到总览。
- 研究截止日：2026-09-05；本次结构修订和覆盖核对：2026-09-05
- 覆盖规则：一级非隐藏、非构建/临时目录中含芯片 Markdown 资料的厂家目录；本次恢复 d-Matrix、FuriosaAI、Tenstorrent 后共 21 个资料目录。
- 证据规则：重要结论优先采用实际打开的官方页面、公告、数据表、开发文档或可核验基准；公告、流片、量产、出货、客户部署和云可用分开记录。
- Hot Chips 2026 对照：[hot-chips-2026.md](./hot-chips-2026.md)；会议议程对象与本地已收录对象分开统计，完整幻灯片和录像按官方 FAQ 的公开时间处理。

| 厂家 | 最新芯片 | 主要架构路线 | 主要用途 | 当前状态 | 内存 | 互联 | 功耗 | 软件栈 | 报告链接 | 完整度 |
| -- | ---- | ------ | ---- | ---- | -- | -- | -- | --- | --- | --- |
| AMD | MI455X | CDNA5、HBM4、UALink | 训练/推理/HPC | 已发布；Helios 计划 2026 下半年部署 | 432GB HBM4 | GPU-GPU 3.6TB/s（系统口径） | 单 GPU 未确认 | ROCm | [报告](./AMD/AMD-overview.md) | 部分完成 |
| AWS | Trainium3 | NeuronCore、HBM3e、NeuronLink | 云训练/推理 | Trn3 GA；后续代际为路线图 | 144GB HBM3e | NeuronLink/NeuronSwitch | 单芯片未确认 | Neuron/NKI | [报告](./AWS/AWS-overview.md) | 部分完成 |
| Biren | BR166/BR20X | 通用 GPU、BLink | 训练/推理 | 部分型号有产品/交付证据；BR20X为路线图 | 见报告 | BLink/系统互联 | 型号口径冲突已列出 | BIRENSUPA | [报告](./Biren/壁仞科技-概览.md) | 已完成 |
| Cambricon | MLU/思元系列 | MLU/NPU | 训练/推理 | MLU370/270/220可核验；MLU690未充分确认 | 见报告 | 部分未公开 | 多数未确认 | NeuWare/SDK | [报告](./Cambricon/寒武纪-概览.md) | 部分完成 |
| Cerebras | WSE-3/CS-4 | 晶圆级、片上 SRAM | 训练/推理 | 产品公开；出货细节有限 | SRAM/系统外存分开 | 晶圆级/系统级 | 分层记录 | Cerebras SDK | [报告](./Cerebras/Cerebras-overview.md) | 部分完成 |
| d-Matrix | Corsair/Pavehawk | DIMC、SRAM-first、3D DRAM 路线 | 低延迟推理 | Corsair full production；Pavehawk 实验室硅 | 2GB 性能内存与容量内存分层 | DMX/平台级，JetStream 单列 | 平台口径 | Aviator/软件栈待复核 | [报告](./d-Matrix/d-Matrix-overview.md) | 新增恢复 |
| Enflame | L600 | GCU | 训练/推理 | S60量产上市；L600量产交付未充分确认 | 见报告 | GCU/POD分开 | 卡/模组口径 | TopsRider | [报告](./Enflame/燧原科技-概览.md) | 已完成 |
| FuriosaAI | RNGD Gen 2 | Tensor Contraction Processor | 推理 | 旧资料记录量产并部署；当前 GA 待复核 | 48GB HBM3；256MB SRAM（旧资料口径） | PCIe/多卡，待复核 | 150W/180W口径并列 | 编译器/TCL | [报告](./FuriosaAI/FuriosaAI-overview.md) | 新增恢复 |
| Google | TPU7x/Ironwood | TPU、ICI、SparseCore | 云训练/推理 | Ironwood GA；TPU8系列为 Coming soon | 见报告 | ICI/Pod | 云实例/系统分开 | XLA/JAX | [报告](./Google/Google-overview.md) | 已完成 |
| Groq | Groq3 LPX | SRAM-first LPU | 低延迟推理 | 纳入平台；供货状态未完全确认 | SRAM/DDR分开 | C2C/LPX | 未确认 | Groq runtime | [报告](./Groq/Groq-overview.md) | 部分完成 |
| Huawei | Ascend 950PR/DT；910B 等主流代际 | NPU、Cube/Vector | 训练/推理、Prefill/Decode | 950PR卡有上市证据；950DT/超节点及910B的量产、出货、部署按报告分层 | PR/DT/历史代际分开 | Unified Bus/URMA | 芯片未确认 | CANN/MindSpore | [报告](./Huawei/华为-概览.md) | 部分完成 |
| Hygon | 深算三号 | DCU、CPU/DCU | 国产服务器/训练/推理 | 深算三号有市场状态；新代际边界有限 | 不完整 | 资料有限 | 未确认 | DTK | [报告](./Hygon/海光信息-概览.md) | 已完成 |
| Iluvatar | 天垓300 | GPGPU、推理/训练 | 训练/推理/边端 | 2026-07发布；各产品状态分开 | 见报告 | 卡/模组/系统分开 | 未确认项列出 | ILIAS | [报告](./Iluvatar/天数智芯-概览.md) | 已完成 |
| Kunlunxin | 三代/P800相关 | 专用 AI 加速器/超节点 | 云训练/推理 | 三代公开；P800未确认项单列 | 见报告 | 芯片/模组/服务器分开 | 多数未确认 | XPU/XTDK | [报告](./Kunlunxin/昆仑芯-概览.md) | 已完成 |
| MetaX | C600/C500 | 国产 GPGPU | 训练/推理/HPC | C600状态分开；C500量产日期冲突 | 见报告 | 卡/模组/服务器分层 | 见报告 | MXMACA | [报告](./MetaX/沐曦-概览.md) | 已完成 |
| MooreThreads | S5000/PH100 | 全功能 GPU、MUSA/MTLink | 训练/推理/图形 | 产品公开；交付/云可用按型号区分 | 见报告 | MTLink/系统级 | 见报告 | MUSA | [报告](./MooreThreads/摩尔线程-概览.md) | 已完成 |
| NVIDIA | Rubin/Rubin CPX；Blackwell | Tensor Core、HBM4/HBM3e、NVLink | 前沿训练/推理/长上下文 | Rubin量产爬坡；Blackwell按GPU、Superchip和系统边界分层；CPX为2026计划 | Rubin 288GB HBM4；Blackwell按型号见报告 | NVLink6及Blackwell系统互联分开 | 单 GPU 未确认 | CUDA/TensorRT | [报告](./NVIDIA/NVIDIA-overview.md) | 部分完成 |
| Sunrise | 启望S3 | 推理优先 GPGPU、低精度 | 大模型/智能体推理 | S2规模化量产为厂商表述；S3供货未确认 | 容量未确认 | PCIe Gen6；系统级单列 | 未确认 | SIRE/vLLM等 | [报告](./Sunrise/曦望-概览.md) | 部分完成 |
| Tenstorrent | Blackhole p150/Galaxy | RISC-V、Tensix、显式 Dataflow、NoC | 训练/推理 | Blackhole 首发；Galaxy 系统 GA/部署叙事 | 180MB 分布式 SRAM；32GB GDDR6 | 4×800G；Galaxy 系统级互联 | Galaxy 系统口径 | TT-Metalium/TTNN/TT-Forge | [报告](./Tenstorrent/Tenstorrent-overview.md) | 新增恢复 |
| OpenAI | Jalapeño | OpenAI设计、Broadcom实现、Ethernet系统 | LLM推理 | 2026-06披露；tape-out、工程样片、初步实测；量产/出货/云可用未确认 | 未公开 | Broadcom网络方案；芯片协议未公开 | 未公开 | OpenAI serving/kernel；公开芯片 SDK 未确认 | [报告](./openai/openai-overview.md) | 部分完成 |
| 小米 Xiaomi | 玄戒 O1/O3、O100、D100 | 移动 SoC、端侧高带宽 AI、智驾 | 端侧 AI、影像、智能驾驶 | O1已搭载出货；O100/D100计划后续商用；数据中心通用加速器未确认 | O100 3.5GB专用内存、1.22TB/s为转载发布信息 | 端侧片上互联；跨卡未确认 | 未公开 | HyperOS/端侧 AI；独立加速器栈未确认 | [报告](./Xiaomi/小米-概览.md) | 资料不足 |

## 覆盖与核验结论

- 实际识别并纳入汇总的资料目录：21 个；其中 18 个为原有厂商目录，3 个为本次从历史架构资料恢复的独立路线目录；每个目录均保留且仅保留一份总描述文档，其余为芯片或芯片关联产品页。
- 新增 OpenAI 报告确认 Jalapeño 的状态边界；新增小米报告将手机 SoC、端侧 AI 加速芯片和智驾芯片分开，未将其升级为数据中心通用 AI 加速器。
- 主要遗留项仍是历史型号的流片/送样/出货日期、单芯片功耗、完整内存与互联数据、客户部署和云实例可用性；报告中均按“公开资料未确认”处理。
- `openai/` 原先因无 Markdown 被排除，现已纳入；`Xiaomi/` 为本次新增厂家目录。原有 `chip-vendor-coverage-2026-09-01.md` 保留作为前一轮工作记录。

## Hot Chips 2026 会议覆盖

会议议程显示，HC2026 新增或集中讨论了 NVIDIA Rubin、AMD MI400、Intel Crescent Island、Cerebras rack-scale、Microsoft Maia 200、SambaNova SN50 RDU、Google 第八代 TPU、OpenAI 芯片、D-Matrix/Meta 3D DRAM、PIM/CXL 计算内存和 AI 网络互联等对象。当前仓库已覆盖其中的 NVIDIA、AMD、Cerebras、Google、OpenAI 和 d-Matrix；Intel、Meta、Microsoft、SambaNova、Broadcom、PIM/CXL 仍需单独建档。具体边界和“待公开材料”标记见 [hot-chips-2026.md](./hot-chips-2026.md)。
