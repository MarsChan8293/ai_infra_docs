---
title: "AMD Instinct"
vendor: AMD
object_type: vendor-overview
updated: 2026-09-15
---
# AMD Instinct

AMD 数据中心加速器按 CDNA 代际组织。单卡/模组、托盘、Helios 机架和云实例严格分层。

| 对象 | 层级 | 状态 | 关键事实 |
|---|---|---|---|
| [[chip/AMD/mi100|MI100]] | accelerator | legacy | CDNA；32GB HBM2 |
| [[chip/AMD/mi210|MI210]] | accelerator | legacy | CDNA2；64GB HBM2e |
| [[chip/AMD/mi250|MI250]] / [[chip/AMD/mi250x|MI250X]] | accelerator | legacy | 128GB HBM2e；3.2TB/s |
| [[chip/AMD/mi300a|MI300A]] | apu | ga | CPU+GPU APU |
| [[chip/AMD/mi300x|MI300X]] | accelerator | ga | 192GB HBM3；5.3TB/s |
| [[chip/AMD/mi325x|MI325X]] | accelerator | ga | 256GB HBM3E；6TB/s |
| [[chip/AMD/mi350x|MI350X]] | accelerator | ga | 288GB HBM3E；8TB/s |
| [[chip/AMD/mi355x|MI355X]] | accelerator | ga | 288GB HBM3E；1400W |
| [[chip/AMD/mi350p|MI350P]] | board | announced | PCIe；144GB HBM3E |
| [[chip/AMD/mi440x|MI440X]] | accelerator | announced | 企业本地 AI；规格未完整公开 |
| [[chip/AMD/mi430x|MI430X]] | accelerator | roadmap | CDNA5；432GB HBM4 |
| [[chip/AMD/mi455x|MI455X]] | accelerator | announced | CDNA5；432GB HBM4；23.3TB/s |
| [[chip/AMD/mi500|MI500]] | family | roadmap | CDNA6 / 2nm / HBM4E 路线 |

## 证据边界
- 旧型号没有明确 EOL 公告时只标 `legacy`，不自动写“停产”。
- Helios 的 72 GPU、31TB HBM4、EFLOPS 与机架带宽属于系统级，不回填单 GPU。

## 来源
- https://www.amd.com/en/products/accelerators/instinct.html
- https://www.amd.com/en/technologies/cdna.html
