# Cambricon / 寒武纪 芯片拆分索引

- 拆分日期：2026-09-02
- 综合报告：[cambricon-chips-2026-09-01.md](./cambricon-chips-2026-09-01.md)
- 组织规则：按芯片名称、芯片家族或明确命名的代际拆分；板卡、模组、服务器、机架、云服务和生态对象单列为边界文件。
- 证据规则：拆分页只重排综合报告中的原文摘录和直接 URL，不新增规格、不升级产品状态。

## 芯片与芯片家族

| 产品/家族 | 产品层级 | 拆分文件 |
| -- | -- | -- |
| Cambricon-1A | 终端 IP/芯片 | [cambricon-1a.md](./cambricon-1a.md) |
| Cambricon-1H | 终端 IP/芯片 | [cambricon-1h.md](./cambricon-1h.md) |
| Cambricon-1M | 终端 IP/芯片 | [cambricon-1m.md](./cambricon-1m.md) |
| MLU100 / 思元100 | 芯片/PCIe 加速卡 | [mlu100.md](./mlu100.md) |
| MLU220 / 思元220 | 边缘 SoC/模组 | [mlu220.md](./mlu220.md) |
| MLU270 / 思元270 | 芯片/PCIe 加速卡 | [mlu270.md](./mlu270.md) |
| MLU290 / 思元290 | 芯片/OAM 加速卡 | [mlu290.md](./mlu290.md) |
| MLU370 / 思元370 | Chiplet 芯片/PCIe 加速卡 | [mlu370.md](./mlu370.md) |
| MLU570 | 软件支持目标/未确认实体 | [mlu570.md](./mlu570.md) |
| MLU580 | 软件支持目标/未确认实体 | [mlu580.md](./mlu580.md) |
| MLU590 / 思元590 | 在研芯片 | [mlu590.md](./mlu590.md) |

## 板卡、系统、软件与云服务边界

| 对象 | 边界层级 | 拆分文件 |
| -- | -- | -- |
| 寒武纪板卡、整机与云（边界文件，非芯片） | 板卡/服务器/云服务（非芯片） | [cambricon-platform-boundary.md](./cambricon-platform-boundary.md) |

## 使用说明

- 产品规格、状态日期、客户/云可用性以及未知项以综合报告为准。
- 同一家族中出现别名、板卡 SKU 或系统名时，文件会保留原始层级并在“产品层级”字段中说明。
- 未确认字段保持“公开资料未确认”，不能从相邻代际或同层级产品推导。
