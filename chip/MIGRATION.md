# Chip directory migration

`chip/` 已从历史研究笔记集合重建为结构化硬件知识库，并在 2026-09-16 升级到可执行的 **Chip Schema V0.2**。

## 基础迁移原则

1. 删除重复的日期快照、覆盖矩阵、会议汇总和模型目录；这些不再作为芯片对象存在。
2. 原先一页混合多个层级的内容拆为独立对象。例如：
   - NVIDIA Blackwell → Blackwell 架构 / B200 / GB200 / HGX B200 / DGX B200 / GB200 NVL72。
   - Moore Threads 苏堤 → 苏堤芯片 / S1000 / S2000。
   - 天垓100 → 天垓100 芯片 / BI-V100 板卡。
   - 智铠100 → 产品/芯片层 / MR-V50 / MR-V100。
   - Tenstorrent Blackhole → p150 单卡 / Galaxy 32-ASIC 系统。
3. Markdown frontmatter 是结构化事实层，不另建一份手工 YAML 数据库。
4. 证据不足时宁可 `null`，不从相邻 SKU、软件能力或系统聚合值制造假精确。
5. 卡数、机架功耗、聚合 HBM、系统互联、云 VM 配置等指标保留在对应层级，不回填单芯片。

## V0.2 自动迁移

`scripts/migrate-chip-v0.2.py` 对硬件对象执行可复现迁移：

- 增加 `schema_version: chip-v0.2`。
- 规范 `object_type`，并映射到稳定的 `layer`；无法安全归类时保留 `unknown`。
- 生命周期状态收敛到 canonical `status`；历史值无法安全映射时保留 `legacy_status`。
- 缺失的事实块补为空 mapping / `null`，不补造事实。
- 从 `## 直接来源` 建立 `evidence` Source ID。
- 默认只记录 `evidence_map.__page__`；若页面只有一个直接来源，字段归属无歧义时才自动提升到字段级 Evidence。
- 多来源历史页不会批量猜测“哪个字段属于哪个来源”，因此字段级 Evidence 覆盖率允许低于 100%。
- `16/32` 这类明确多规格数值规范为数值列表；“更高但公开数值未知”这类定性信息把数值字段设为 `null`，描述移入 note。
- `relations` 只录入语义可确认的 typed relation，不为增加图密度批量猜边。

## 验证与派生数据

```bash
python3 scripts/validate-chip.py --root . --report generated/chip-validation.json
python3 scripts/build-chip-catalog.py --root . --output generated
python3 scripts/build-knowledge-graph.py --root . --output generated
python3 scripts/enrich-knowledge-graph.py --generated generated
```

迁移完成后，Chip Validator 必须达到 `errors=0`。健康度与比较表全部从 Markdown/frontmatter 派生，不手工维护；低 Evidence 覆盖表示待研究项，而不是通过复制来源或相邻 SKU 推断来“刷绿”。

## 不再保留的旧内容类型

- `chip-coverage-YYYY-MM-DD.md` 等时间快照。
- `hot-chips-2026.md` 等会议汇总。
- `DeepSeek-*` 等模型对象。
- 混合对象长页，例如旧 `NVIDIA/blackwell.md`、`MooreThreads/sudi-s1000-s2000.md`。

历史信息若仍有价值，尽量下沉到对应硬件对象页；无法安全映射的叙述不迁移为事实。