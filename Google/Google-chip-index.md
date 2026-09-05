# Google / 谷歌 芯片拆分索引

- 厂商概览：[Google-overview.md](./Google-overview.md)
- 拆分日期：2026-09-02
- 综合报告：[03-google-ironwood.md](./03-google-ironwood.md)
- 组织规则：按芯片名称、芯片家族或明确命名的代际拆分；板卡、模组、服务器、机架、云服务和生态对象单列为边界文件。
- 证据规则：拆分页只重排综合报告中的原文摘录和直接 URL，不新增规格、不升级产品状态。

## 芯片与芯片家族

| 产品/家族 | 产品层级 | 拆分文件 |
| -- | -- | -- |
| TPU v5p | TPU ASIC/Cloud TPU | [tpu-v5p.md](./tpu-v5p.md) |
| TPU v6e / Trillium | TPU ASIC/Cloud TPU | [tpu-v6e-trillium.md](./tpu-v6e-trillium.md) |
| TPU7x / Ironwood | TPU ASIC/Cloud TPU | [tpu7x-ironwood.md](./tpu7x-ironwood.md) |
| TPU 8t | 路线图 TPU ASIC/训练系统 | [tpu8t.md](./tpu8t.md) |
| TPU 8i | 路线图 TPU ASIC/推理系统 | [tpu8i.md](./tpu8i.md) |

## 板卡、系统、软件与云服务边界

| 对象 | 边界层级 | 拆分文件 |
| -- | -- | -- |
| TPU Pod、VM 与 Cloud TPU（边界文件，非芯片） | 板卡/Pod/云服务（非芯片） | [tpu-platform-boundary.md](./tpu-platform-boundary.md) |

## 未命名路线图

| 对象 | 产品层级 | 拆分文件 |
| -- | -- | -- |
| 更后续 TPU（未命名路线） | 路线图，不是已命名芯片 | [future-tpu-roadmap.md](./future-tpu-roadmap.md) |

## 使用说明

- 产品规格、状态日期、客户/云可用性以及未知项以综合报告为准。
- 同一家族中出现别名、板卡 SKU 或系统名时，文件会保留原始层级并在“产品层级”字段中说明。
- 未确认字段保持“公开资料未确认”，不能从相邻代际或同层级产品推导。
