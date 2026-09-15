---
title: "AI 芯片与硬件资料库"
tags: [moc, chip]
updated: 2026-09-15
---
# AI 芯片与硬件资料库

本目录已按 **Chip Schema V0.1** 全量重建。Markdown 是唯一事实源；每个对象通过 YAML frontmatter 提供机器可读字段，正文只保留结论、核心规格、生命周期/边界和直接来源。

## 数据规则
- 每个硬件对象一页；芯片、板卡、模组、服务器、机架、集群、内存与网络 ASIC 分层。
- 未有直接证据的值保持 `null` / “公开资料未确认”，不从相邻 SKU 或系统反推。
- 生命周期拆分宣布、流片/样片、量产、出货、客户部署、云可用、EOL。
- 厂商峰值、第三方测试、分析推断和系统聚合值不混写。
- 对象定义见 [[chip/SCHEMA|Chip Schema V0.1]]；迁移原则见 [[chip/MIGRATION|Migration Notes]]。

## 厂商索引
| 厂商 | 总览 |
|---|---|
| AMD | [[chip/AMD/AMD-overview|AMD Instinct]] |
| AWS | [[chip/AWS/AWS-overview|AWS AI Accelerators]] |
| Biren / 壁仞 | [[chip/Biren/壁仞科技-概览|壁仞科技]] |
| Broadcom | [[chip/Broadcom/Broadcom-overview|Broadcom AI Infrastructure Silicon]] |
| Cambricon / 寒武纪 | [[chip/Cambricon/寒武纪-概览|寒武纪]] |
| Cerebras | [[chip/Cerebras/Cerebras-overview|Cerebras]] |
| Enflame / 燧原 | [[chip/Enflame/燧原科技-概览|燧原科技]] |
| FuriosaAI | [[chip/FuriosaAI/FuriosaAI-overview|FuriosaAI]] |
| Google | [[chip/Google/Google-overview|Google TPU]] |
| Groq | [[chip/Groq/Groq-overview|Groq LPU]] |
| Huawei / 华为 | [[chip/Huawei/华为昇腾-概览|华为昇腾]] |
| Hygon / 海光 | [[chip/Hygon/海光信息-概览|海光信息]] |
| Iluvatar CoreX / 天数智芯 | [[chip/Iluvatar/天数智芯-概览|天数智芯]] |
| Intel | [[chip/Intel/Intel-overview|Intel AI Accelerators]] |
| Kunlunxin / 昆仑芯 | [[chip/Kunlunxin/昆仑芯-概览|昆仑芯]] |
| Meta | [[chip/Meta/Meta-overview|Meta MTIA]] |
| MetaX / 沐曦 | [[chip/MetaX/沐曦-概览|沐曦]] |
| Microsoft | [[chip/Microsoft/Microsoft-overview|Microsoft Maia]] |
| Moore Threads / 摩尔线程 | [[chip/MooreThreads/摩尔线程-概览|摩尔线程]] |
| NVIDIA | [[chip/NVIDIA/NVIDIA-overview|NVIDIA Data Center GPU]] |
| SambaNova | [[chip/SambaNova/SambaNova-overview|SambaNova RDU]] |
| Samsung | [[chip/Samsung/Samsung-overview|Samsung AI Memory]] |
| Sunrise / 曦望 | [[chip/Sunrise/Sunrise-overview|曦望 Sunrise]] |
| Tenstorrent | [[chip/Tenstorrent/Tenstorrent-overview|Tenstorrent]] |
| XCENA | [[chip/XCENA/XCENA-overview|XCENA]] |
| Xiaomi / 小米 | [[chip/Xiaomi/小米-概览|小米芯片]] |
| d-Matrix | [[chip/d-Matrix/d-Matrix-overview|d-Matrix]] |
| OpenAI | [[chip/openai/openai-overview|OpenAI Custom Silicon]] |
