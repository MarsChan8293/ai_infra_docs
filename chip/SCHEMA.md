# Chip Schema V0.2

Chip V0.2 把 `chip/` 升级为可执行的数据模型。Markdown 仍是唯一事实源；YAML frontmatter 提供机器可读字段，`scripts/validate-chip.py` 是执行层，`scripts/build-chip-catalog.py` 生成比较表与健康度报告。

## 原则

1. 芯片、卡、板、模组、系统、机架、集群、网络、内存、IP、SoC、产品家族不得混写。
2. 单位进入字段名，例如 `capacity_gb`、`bandwidth_tb_s`、`value_w`。
3. 未确认值使用 `null` / 空 mapping，不从相邻 SKU、系统聚合值或软件能力反推。
4. `evidence` 定义来源，`evidence_map` 记录字段路径到 Source ID；仅能确认页面级来源时使用 `__page__`，不得伪造字段级追溯。
5. `relations` 只记录可确认的 typed relation，目标使用仓库根路径 node id。
6. 宣布、样片、量产、出货、客户部署、云可用、EOL 分开记录。

## 最小对象

```yaml
---
schema_version: chip-v0.2
title: AMD Instinct MI300X
vendor: AMD
object_type: accelerator
layer: accelerator
status: ga
architecture: CDNA3
process: null
memory: {type: HBM3, capacity_gb: 192, bandwidth_tb_s: 5.3}
compute: {}
interconnect: {}
power: {value_w: 750, scope: module}
lifecycle: {announced: 2023-12-06}
relations: {}
evidence:
  S1: {url: "https://www.amd.com/en/products/accelerators/instinct.html", source_type: official, accessed: 2026-09-16}
evidence_map:
  __page__: [S1]
updated: 2026-09-15
---
```

## 必填字段

硬件对象必须包含 `schema_version`、`title`、`vendor`、`object_type`、`layer`、`status`、`architecture`、`process`、`memory`、`compute`、`interconnect`、`power`、`lifecycle`、`relations`、`evidence`、`evidence_map`、`updated`。`schema_version` 固定为 `chip-v0.2`。厂商总览、MOC、Schema 与 Migration 文档不属于硬件对象。

`object_type` 保留细粒度类型并使用 kebab-case；`layer` 提供稳定的跨厂商比较层级，只允许：`family`、`chip`、`accelerator`、`board`、`module`、`system`、`rack`、`cluster`、`network`、`memory`、`soc`、`ip`、`unknown`。

`status` 允许：`roadmap`、`announced`、`sampling`、`pre-deployment`、`production`、`shipping`、`current-catalog`、`product`、`ga`、`legacy`、`eol`、`unknown`。

## 事实块

- `architecture`、`process`：字符串、mapping 或 `null`。
- `memory`、`compute`、`interconnect`、`power`、`lifecycle`：mapping 或 `null`。
- 内存优先使用 `type`、`capacity_gb`、`bandwidth_tb_s`；多级内存可以嵌套。
- 算力按数据类型区分，例如 `fp64_tflops`、`fp32_tflops`、`tf32_tflops`、`fp16_tflops`、`bf16_tflops`、`fp8_tflops`、`fp4_tflops`、`int8_tops`。稀疏值不得覆盖 dense 值。
- 互联优先使用 `type`、`bandwidth_gb_s` / `bandwidth_tb_s`、`links`、`host_interface`。
- 功耗使用 `value_w` 并带 `scope`；系统/机架聚合功耗不得回填芯片对象。
- 生命周期优先使用 `announced`、`tapeout`、`sampling`、`production`、`shipping`、`customer_deployed`、`cloud_available`、`eol`。


## Memory / HBM 对象边界

`layer: memory` 用于独立、可识别的 memory product / technology object；accelerator 上集成的 HBM 规格仍写在 accelerator 自身的 `memory` block，不因为使用了 HBM 就额外复制成一个 memory SKU 节点。

Memory hardware 页面优先记录：

- `object_type`：例如 `hbm-stack`、`memory-device`、`memory-expander`、`memory-module`。
- `layer: memory`。
- `memory.type`：HBM3、HBM3E、HBM4、DDR5、LPDDR、CXL-attached-memory 等。
- `memory.capacity_gb`：对象自身容量。
- `memory.bandwidth_tb_s` / `bandwidth_gb_s`：对象自身公开带宽，必须保留 scope。
- `interconnect.host_interface`：例如公开可确认的 CXL / DDR / proprietary interface。
- `power`：只有官方给出对象级 power 时填写。
- `lifecycle`：宣布、量产、出货等分开记录。

边界规则：

1. HBM technology generation 与具体 stack / product SKU 可以是不同对象；没有 SKU 事实时不要虚构产品。
2. Accelerator 的 aggregate HBM capacity/bandwidth 不得回填成单颗 HBM stack 规格。
3. Memory Expander / CXL Memory 记录自身容量、接口和带宽，不把 host/cluster 聚合容量回填。
4. SSD / NVMe 属于 storage 语义时不强塞进 `layer: memory`；后续 Storage 对象边界单独维护。
5. PIM / near-memory compute 若同时具备显著 compute 属性，应选择最能表达产品本体的 `object_type`，正文说明 memory-compute 边界，不复制成两个实体。
6. 所有容量与带宽都必须保留对象 scope 和直接 Evidence。

## Evidence

`evidence` 的 key 使用 `S1`、`S2`；每项至少包含 `url`，建议补 `source_type` 与 `accessed`。`evidence_map` 把 `memory.capacity_gb` 等字段路径映射到 Source ID。历史页暂时只能确认页面来源时使用 `evidence_map: {__page__: [S1, S2]}`，这不代表字段已逐项追溯。正文 `## 直接来源` 仍必须保留这些 URL。

## Typed relations

允许：`architecture-of`、`variant-of`、`successor-of`、`predecessor-of`、`packaged-in`、`used-in`、`part-of`、`connects-via`、`compatible-with`、`related`。目标必须存在且不带 `.md`；无法确认关系性质时只保留普通 Wiki Link。

## 层级边界

- `family` 不承载具体 SKU 的板卡功耗和容量。
- `chip` 不允许机架 GPU 数、节点数、系统总功耗等聚合字段。
- `accelerator` / `board` / `module` 只记录自身范围指标。
- `system` / `rack` / `cluster` 可以记录聚合指标，但必须保留 scope。
- `network` / `memory` 不使用 AI 算力字段填补资料空白。

## CI

- `python3 scripts/validate-chip.py --root .`
- `python3 scripts/build-chip-catalog.py --root . --output generated`
- `scripts/build-knowledge-graph.py` 读取 `relations` 生成 typed edges。

任何新增硬件对象必须通过 Chip Validator；旧对象由 `scripts/migrate-chip-v0.2.py` 一次性迁移。