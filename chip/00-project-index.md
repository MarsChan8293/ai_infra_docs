# AI Infra Chip 资料库入口

这是本地 AI 芯片与基础设施资料库的总入口。资料按厂商目录保存；每个厂家目录只保留一个总描述文档，其余 Markdown 均按单一芯片、芯片家族或芯片关联产品对象拆分。

## 推荐阅读路径

1. 先从下表打开厂家总描述文档，了解研究范围、生命周期和证据边界。
2. 在总描述文档的“芯片页关系导航”中进入独立芯片页或与芯片强绑定的产品页；其中的 `[[...]]` 链接可直接形成 Obsidian 图谱边。
3. 跨芯片的平台、服务器、机架、集群和云服务等边界统一收在对应厂家总描述文档中；与单一芯片强绑定的板卡/模组只保留在对应芯片页。
4. 网络交换芯片、PIM 与 CXL computational memory 作为 AI 基础设施边界对象单独建档，不与 GPU/NPU 的算力、显存口径混排。

## 厂商目录

| 厂商目录 | 唯一总描述文档 |
| --- | --- |
| AMD | [AMD-overview](./AMD/AMD-overview.md) |
| AWS | [AWS-overview](./AWS/AWS-overview.md) |
| Biren | [壁仞科技-概览](./Biren/壁仞科技-概览.md) |
| Broadcom | [Broadcom-overview](./Broadcom/Broadcom-overview.md) |
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
| Intel | [Intel-overview](./Intel/Intel-overview.md) |
| Kunlunxin | [昆仑芯-概览](./Kunlunxin/昆仑芯-概览.md) |
| Meta | [Meta-overview](./Meta/Meta-overview.md) |
| MetaX | [沐曦-概览](./MetaX/沐曦-概览.md) |
| Microsoft | [Microsoft-overview](./Microsoft/Microsoft-overview.md) |
| MooreThreads | [摩尔线程-概览](./MooreThreads/摩尔线程-概览.md) |
| NVIDIA | [NVIDIA-overview](./NVIDIA/NVIDIA-overview.md) |
| Samsung | [Samsung-overview](./Samsung/Samsung-overview.md) |
| SambaNova | [SambaNova-overview](./SambaNova/SambaNova-overview.md) |
| Sunrise | [曦望-概览](./Sunrise/曦望-概览.md) |
| Tenstorrent | [Tenstorrent-overview](./Tenstorrent/Tenstorrent-overview.md) |
| XCENA | [XCENA-overview](./XCENA/XCENA-overview.md) |
| Xiaomi | [小米-概览](./Xiaomi/小米-概览.md) |
| openai | [openai-overview](./openai/openai-overview.md) |

## 根级资料

| 类型 | 文档 |
| --- | --- |
| 当前厂商覆盖汇总 | [chip-vendor-coverage-2026-09-13](./chip-vendor-coverage-2026-09-13.md) |
| 上一轮覆盖记录 | [chip-vendor-coverage-2026-09-02](./chip-vendor-coverage-2026-09-02.md) |
| 更早覆盖记录 | [chip-vendor-coverage-2026-09-01](./chip-vendor-coverage-2026-09-01.md) |
| Hot Chips 2026 对照 | [hot-chips-2026](./hot-chips-2026.md) |

## 2026-09-13 增量

本轮新增 Intel Crescent Island、Microsoft Maia 200、Meta MTIA 300/400/450/500、SambaNova SN50、Broadcom Thor Ultra/Tomahawk Ultra、Samsung LPDDR5X-PIM 与 XCENA MX1。上一轮 Hot Chips 2026 对照中列出的六类主要空档已从“待补档”升级为可导航的厂家总览与产品证据页。

## 命名规则

- 非中国厂商使用 `<vendor>-overview.md` 作为唯一总描述文档。
- 中国厂商使用 `<中文厂商名>-概览.md` 作为唯一总描述文档，例如 `壁仞科技-概览.md`。
- 芯片或芯片家族页继续使用产品名称命名；跨芯片平台、系统、服务器、机架、集群和云服务说明并入总描述文档，强绑定产品对象随对应芯片页记录。
- 网络/内存等 AI 基础设施对象仍按厂商归档，但必须在页面开头标注对象层级，避免把交换芯片、NIC、PIM、CXL memory 写成 GPU/NPU。
- 新增厂商时沿用同一规则，并在本入口和当前覆盖汇总中补链。
