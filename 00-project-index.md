# AI Infra Chip 资料库入口

这是本地 AI 芯片与基础设施资料库的总入口。资料按厂商目录保存，厂商目录内再区分概览页、芯片索引、综合报告、芯片/家族拆分页和平台边界页。

## 推荐阅读路径

1. 先从下表打开厂商概览，了解该厂商的研究范围与证据边界。
2. 再打开对应的芯片索引，按芯片、芯片家族和产品层级进入独立资料页。
3. 需要完整状态矩阵、来源和分析时，回到综合报告；板卡、服务器、机架、集群和云服务只看对应的边界页。

## 厂商目录

| 厂商目录 | 厂商概览 | 芯片索引 |
| --- | --- | --- |
| AMD | [AMD-overview](./AMD/AMD-overview.md) | [AMD-chip-index](./AMD/AMD-chip-index.md) |
| AWS | [AWS-overview](./AWS/AWS-overview.md) | [AWS-chip-index](./AWS/AWS-chip-index.md) |
| Biren | [壁仞科技-概览](./Biren/壁仞科技-概览.md) | [壁仞科技-芯片索引](./Biren/壁仞科技-芯片索引.md) |
| Cambricon | [寒武纪-概览](./Cambricon/寒武纪-概览.md) | [寒武纪-芯片索引](./Cambricon/寒武纪-芯片索引.md) |
| Cerebras | [Cerebras-overview](./Cerebras/Cerebras-overview.md) | [Cerebras-chip-index](./Cerebras/Cerebras-chip-index.md) |
| d-Matrix | [d-Matrix-overview](./d-Matrix/d-Matrix-overview.md) | [d-Matrix-chip-index](./d-Matrix/d-Matrix-chip-index.md) |
| Enflame | [燧原科技-概览](./Enflame/燧原科技-概览.md) | [燧原科技-芯片索引](./Enflame/燧原科技-芯片索引.md) |
| FuriosaAI | [FuriosaAI-overview](./FuriosaAI/FuriosaAI-overview.md) | [FuriosaAI-chip-index](./FuriosaAI/FuriosaAI-chip-index.md) |
| Google | [Google-overview](./Google/Google-overview.md) | [Google-chip-index](./Google/Google-chip-index.md) |
| Groq | [Groq-overview](./Groq/Groq-overview.md) | [Groq-chip-index](./Groq/Groq-chip-index.md) |
| Huawei | [华为-概览](./Huawei/华为-概览.md) | [华为-芯片索引](./Huawei/华为-芯片索引.md) |
| Hygon | [海光信息-概览](./Hygon/海光信息-概览.md) | [海光信息-芯片索引](./Hygon/海光信息-芯片索引.md) |
| Iluvatar | [天数智芯-概览](./Iluvatar/天数智芯-概览.md) | [天数智芯-芯片索引](./Iluvatar/天数智芯-芯片索引.md) |
| Kunlunxin | [昆仑芯-概览](./Kunlunxin/昆仑芯-概览.md) | [昆仑芯-芯片索引](./Kunlunxin/昆仑芯-芯片索引.md) |
| MetaX | [沐曦-概览](./MetaX/沐曦-概览.md) | [沐曦-芯片索引](./MetaX/沐曦-芯片索引.md) |
| MooreThreads | [摩尔线程-概览](./MooreThreads/摩尔线程-概览.md) | [摩尔线程-芯片索引](./MooreThreads/摩尔线程-芯片索引.md) |
| NVIDIA | [NVIDIA-overview](./NVIDIA/NVIDIA-overview.md) | [NVIDIA-chip-index](./NVIDIA/NVIDIA-chip-index.md) |
| Sunrise | [曦望-概览](./Sunrise/曦望-概览.md) | [曦望-芯片索引](./Sunrise/曦望-芯片索引.md) |
| Tenstorrent | [Tenstorrent-overview](./Tenstorrent/Tenstorrent-overview.md) | [Tenstorrent-chip-index](./Tenstorrent/Tenstorrent-chip-index.md) |
| Xiaomi | [小米-概览](./Xiaomi/小米-概览.md) | [小米-芯片索引](./Xiaomi/小米-芯片索引.md) |
| openai | [openai-overview](./openai/openai-overview.md) | [openai-chip-index](./openai/openai-chip-index.md) |

## 根级资料

| 类型 | 文档 |
| --- | --- |
| 当前厂商覆盖汇总 | [chip-vendor-coverage-2026-09-02](./chip-vendor-coverage-2026-09-02.md) |
| 上一轮覆盖记录 | [chip-vendor-coverage-2026-09-01](./chip-vendor-coverage-2026-09-01.md) |
| Hot Chips 2026 对照 | [hot-chips-2026](./hot-chips-2026.md) |

## 命名规则

- 非中国厂商使用 `<vendor>-overview.md` 与 `<vendor>-chip-index.md` 作为厂商概览和芯片索引。
- 中国厂商使用 `<中文厂商名>-概览.md` 与 `<中文厂商名>-芯片索引.md`，例如 `壁仞科技-概览.md`。
- 产品页和平台边界页继续使用产品或对象名称命名，不为了统一而改写已有证据页名称。
- 新增厂商时沿用同一规则，并在本入口和当前覆盖汇总中补链。
