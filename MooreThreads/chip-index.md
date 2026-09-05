# Moore Threads / 摩尔线程 芯片拆分索引

- 拆分日期：2026-09-02
- 综合报告：[moore-threads-chips-2026-09-01.md](./moore-threads-chips-2026-09-01.md)
- 组织规则：按芯片名称、芯片家族或明确命名的代际拆分；板卡、模组、服务器、机架、云服务和生态对象单列为边界文件。
- 证据规则：拆分页只重排综合报告中的原文摘录和直接 URL，不新增规格、不升级产品状态。

## 芯片与芯片家族

| 产品/家族 | 产品层级 | 拆分文件 |
| -- | -- | -- |
| MTT E300 | 边缘 AI 模组 | [e300.md](./e300.md) |
| 长江 / M1000 | SoC/边缘 GPU+NPU | [m1000-changjiang.md](./m1000-changjiang.md) |
| 曲院 / MTT S4000 | GPU 芯片/智算加速卡 | [quyuan-s4000.md](./quyuan-s4000.md) |
| MTT S10 | GPU 卡/芯片映射未公开 | [s10.md](./s10.md) |
| MTT S30 | GPU 卡/芯片映射未公开 | [s30.md](./s30.md) |
| MTT S50 | GPU 卡/芯片映射未公开 | [s50.md](./s50.md) |
| MTT S70 | GPU 卡/芯片映射未公开 | [s70.md](./s70.md) |
| MTT S80 | GPU 卡/芯片映射未公开 | [s80.md](./s80.md) |
| MTT X300 | GPU 卡/芯片映射未公开 | [x300.md](./x300.md) |

## 板卡、系统、软件与云服务边界

| 对象 | 边界层级 | 拆分文件 |
| -- | -- | -- |
| 春晓 / MTT S3000 | GPU 芯片/服务器 GPU 卡 | [chunxiao-s3000.md](./chunxiao-s3000.md) |
| 摩尔线程 AIBOOK、AICUBE、SGX5000、KUAE 与云原生（边界文件，非芯片） | 终端/服务器/软件平台（非芯片） | [mthreads-platform-boundary.md](./mthreads-platform-boundary.md) |
| 平湖 / PH100 / MTT S5000 | GPU 芯片/服务器 GPU 卡 | [ph100-s5000.md](./ph100-s5000.md) |
| 苏堤 / MTT S1000、S2000 | GPU 芯片/服务器 GPU 卡 | [sudi-s1000-s2000.md](./sudi-s1000-s2000.md) |

## 使用说明

- 产品规格、状态日期、客户/云可用性以及未知项以综合报告为准。
- 同一家族中出现别名、板卡 SKU 或系统名时，文件会保留原始层级并在“产品层级”字段中说明。
- 未确认字段保持“公开资料未确认”，不能从相邻代际或同层级产品推导。
