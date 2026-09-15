---
title: "AI 芯片与硬件资料库"
tags: [moc, chip]
updated: 2026-09-16
---
# AI 芯片与硬件资料库

本目录已按 **Chip Schema V0.2** 组织为可验证硬件事实库。Markdown 是唯一事实源；每个硬件对象通过 YAML frontmatter 提供机器可读字段，正文保留结论、核心规格、生命周期/边界和直接来源。

## 数据规则
- 每个硬件对象一页；细粒度 `object_type` 同时映射到稳定 `layer`，用于跨厂商比较。
- 未有直接证据的值保持 `null` / “公开资料未确认”，不从相邻 SKU、软件能力或系统数据反推。
- 生命周期拆分宣布、流片/样片、量产、出货、客户部署、云可用、EOL。
- 厂商峰值、第三方测试、分析推断和系统聚合值不混写。
- `evidence` 记录来源，`evidence_map` 区分页面级与字段级追溯；`__page__` 不冒充字段级证据。
- `relations` 只记录可确认的 typed relation；无法确认语义时继续使用普通 Wiki Link。
- 对象定义见 [[chip/SCHEMA|Chip Schema V0.2]]；迁移原则见 [[chip/MIGRATION|Migration Notes]]。

## 自动校验与派生数据

```bash
python3 scripts/validate-chip.py --root . --report generated/chip-validation.json
python3 scripts/build-chip-catalog.py --root . --output generated
python3 scripts/build-knowledge-graph.py --root . --output generated
python3 scripts/enrich-knowledge-graph.py --generated generated
```

`generated/chip-health.md` 展示 Schema、来源、字段级 Evidence、Memory/Compute/Interconnect/Power/Lifecycle 完整度和陈旧数据；`generated/chip-comparison.md` / `.csv` 从相同 frontmatter 自动生成横向比较，均不手工维护。

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
