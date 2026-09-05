# Amazon Web Services / 亚马逊云科技 芯片拆分索引

- 拆分日期：2026-09-02
- 综合报告：[06-aws-trainium.md](./06-aws-trainium.md)
- 组织规则：按芯片名称、芯片家族或明确命名的代际拆分；板卡、模组、服务器、机架、云服务和生态对象单列为边界文件。
- 证据规则：拆分页只重排综合报告中的原文摘录和直接 URL，不新增规格、不升级产品状态。

## 芯片与芯片家族

| 产品/家族 | 产品层级 | 拆分文件 |
| -- | -- | -- |
| Inferentia（v1） | 芯片/EC2 实例边界 | [inferentia-v1.md](./inferentia-v1.md) |
| Inferentia2（v2） | 芯片/EC2 实例边界 | [inferentia2.md](./inferentia2.md) |
| Trainium（v1） | 芯片/EC2 实例边界 | [trainium-v1.md](./trainium-v1.md) |
| Trainium2（v3） | 芯片/EC2 实例边界 | [trainium2.md](./trainium2.md) |
| Trainium3（v4） | 芯片/EC2 实例边界 | [trainium3.md](./trainium3.md) |
| Trainium4（路线图） | 路线图芯片 | [trainium4-roadmap.md](./trainium4-roadmap.md) |

## 板卡、系统、软件与云服务边界

| 对象 | 边界层级 | 拆分文件 |
| -- | -- | -- |
| Trn3 UltraServer（平台边界，非芯片） | 服务器/集群/云平台（非芯片） | [trn3-ultraserver-boundary.md](./trn3-ultraserver-boundary.md) |

## 使用说明

- 产品规格、状态日期、客户/云可用性以及未知项以综合报告为准。
- 同一家族中出现别名、板卡 SKU 或系统名时，文件会保留原始层级并在“产品层级”字段中说明。
- 未确认字段保持“公开资料未确认”，不能从相邻代际或同层级产品推导。
