# Chip directory migration — 2026-09-15

`chip/` 已从历史研究笔记集合重建为结构化硬件知识库。

## 迁移原则
1. 删除重复的日期快照、覆盖矩阵、会议汇总和模型目录；这些不再作为芯片对象存在。
2. 原先一页混合多个层级的内容拆为独立对象。例如：
   - NVIDIA Blackwell → Blackwell 架构 / B200 / GB200 / HGX B200 / DGX B200 / GB200 NVL72。
   - Moore Threads 苏堤 → 苏堤芯片 / S1000 / S2000。
   - 天垓100 → 天垓100 芯片 / BI-V100 板卡。
   - 智铠100 → 产品/芯片层 / MR-V50 / MR-V100。
   - Tenstorrent Blackhole → p150 单卡 / Galaxy 32-ASIC 系统。
3. Markdown frontmatter 作为结构化事实层，避免独立 YAML 与 Markdown 双份事实漂移。
4. 保留直接来源；证据不足时宁可 `null`，不制造假精确。
5. 系统聚合指标绝不回填单芯片：卡数、机架功耗、聚合 HBM、系统互联、云 VM 配置均留在对应层级。

## 不再保留的旧内容类型
- `chip-coverage-YYYY-MM-DD.md` 等时间快照。
- `hot-chips-2026.md` 等会议汇总。
- `DeepSeek-*` 等模型对象。
- 混合对象长页，例如旧 `NVIDIA/blackwell.md`、`MooreThreads/sudi-s1000-s2000.md`。

历史信息若仍有价值，已尽量下沉到对应硬件对象页；无法安全映射的叙述不迁移为事实。
