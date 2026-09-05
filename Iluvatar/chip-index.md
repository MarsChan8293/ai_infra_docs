# Iluvatar CoreX / 天数智芯 芯片拆分索引

- 拆分日期：2026-09-02
- 综合报告：[iluvatar-chips-2026-09-01.md](./iluvatar-chips-2026-09-01.md)
- 组织规则：按芯片名称、芯片家族或明确命名的代际拆分；板卡、模组、服务器、机架、云服务和生态对象单列为边界文件。
- 证据规则：拆分页只重排综合报告中的原文摘录和直接 URL，不新增规格、不升级产品状态。

## 芯片与芯片家族

| 产品/家族 | 产品层级 | 拆分文件 |
| -- | -- | -- |
| 天垓 100 / TG Gen 1 | GPGPU 芯片/训练产品 | [tianga-100.md](./tianga-100.md) |
| 天垓 150 / TG Gen 2 | GPGPU 芯片/训练产品 | [tianga-150.md](./tianga-150.md) |
| 天垓 300 | GPGPU 芯片/训练产品 | [tianga-300.md](./tianga-300.md) |
| 彤央 TY1000 | 端侧算力模组 | [tongyang-ty1000.md](./tongyang-ty1000.md) |
| 彤央 TY1100-NX-PRO | 端侧算力终端 | [tongyang-ty1100-nx-pro.md](./tongyang-ty1100-nx-pro.md) |
| 彤央 TY1100-NX | 端侧算力终端 | [tongyang-ty1100-nx.md](./tongyang-ty1100-nx.md) |
| 彤央 TY1100 | 端侧算力模组 | [tongyang-ty1100.md](./tongyang-ty1100.md) |
| 彤央 TY1200 | 端侧算力终端 | [tongyang-ty1200.md](./tongyang-ty1200.md) |
| 智铠 100 | GPGPU 芯片/推理产品 | [zhikai-100.md](./zhikai-100.md) |

## 板卡、系统、软件与云服务边界

| 对象 | 边界层级 | 拆分文件 |
| -- | -- | -- |
| 天数智芯板卡、服务器、集群与云（边界文件，非芯片） | 板卡/模组/服务器/集群/云（非芯片） | [iluvatar-platform-boundary.md](./iluvatar-platform-boundary.md) |

## 使用说明

- 产品规格、状态日期、客户/云可用性以及未知项以综合报告为准。
- 同一家族中出现别名、板卡 SKU 或系统名时，文件会保留原始层级并在“产品层级”字段中说明。
- 未确认字段保持“公开资料未确认”，不能从相邻代际或同层级产品推导。
