# Hygon / 海光信息 芯片拆分索引

- 拆分日期：2026-09-02
- 综合报告：[hygon-chips-2026-09-01.md](./hygon-chips-2026-09-01.md)
- 组织规则：按芯片名称、芯片家族或明确命名的代际拆分；板卡、模组、服务器、机架、云服务和生态对象单列为边界文件。
- 证据规则：拆分页只重排综合报告中的原文摘录和直接 URL，不新增规格、不升级产品状态。

## 芯片与芯片家族

| 产品/家族 | 产品层级 | 拆分文件 |
| -- | -- | -- |
| 海光 CPU 3000 系列 | CPU 系列 | [cpu-3000.md](./cpu-3000.md) |
| 海光 CPU 5000 系列 | CPU 系列 | [cpu-5000.md](./cpu-5000.md) |
| 海光 CPU 7000 系列 | CPU 系列 | [cpu-7000.md](./cpu-7000.md) |
| 海光一号 | CPU 代际 | [haiguang-1.md](./haiguang-1.md) |
| 海光二号 | CPU 代际 | [haiguang-2.md](./haiguang-2.md) |
| 海光三号 | CPU 代际 | [haiguang-3.md](./haiguang-3.md) |
| 海光四号 | CPU 代际 | [haiguang-4.md](./haiguang-4.md) |
| 海光五号 | CPU 代际/路线 | [haiguang-5.md](./haiguang-5.md) |
| 深算一号 | DCU 代际 | [shensuan-1.md](./shensuan-1.md) |
| 深算二号 | DCU 代际 | [shensuan-2.md](./shensuan-2.md) |
| 深算三号 | DCU 代际/加速卡映射 | [shensuan-3.md](./shensuan-3.md) |
| 深算四号 | DCU 代际/研发 | [shensuan-4.md](./shensuan-4.md) |

## 板卡、系统、软件与云服务边界

| 对象 | 边界层级 | 拆分文件 |
| -- | -- | -- |
| BW1000、K100-AI 与其他生态型号（边界文件） | 加速卡/生态名称（非裸片） | [hygon-accelerator-names.md](./hygon-accelerator-names.md) |
| 海光 DTK、HSL 与整机集群（边界文件，非芯片） | 软件/互联/服务器/云（非芯片） | [hygon-platform-boundary.md](./hygon-platform-boundary.md) |

## 使用说明

- 产品规格、状态日期、客户/云可用性以及未知项以综合报告为准。
- 同一家族中出现别名、板卡 SKU 或系统名时，文件会保留原始层级并在“产品层级”字段中说明。
- 未确认字段保持“公开资料未确认”，不能从相邻代际或同层级产品推导。
