# Tenstorrent — Blackhole p150 / Galaxy

- 厂商总览：[Tenstorrent](./Tenstorrent-overview.md) · [[Tenstorrent-overview|图谱总览]]

- 产品层级：Blackhole p150 为 ASIC/加速卡；Galaxy 为 32 ASIC 系统
- 研究截止日：2026-09-05
- 核验日期：2026-09-05
- 页面性质：基于直接来源整理的自包含证据页；芯片、加速卡、系统、软件和云服务分层记录

## 产品定位与对象边界

### Blackhole p150

| 字段 | 当前资料口径 | 边界 |
| --- | --- | --- |
| 执行 | 120 Tensix、16 Big RISC-V；每 Tensix 5 Baby RISC-V | 早期首发曾出现 140 core/210 MB，不能与当前卡表混写 |
| 片上内存 | 约 180 MB 分布式本地 SRAM；每 Tensix 约 1.5 MB | 分布式 SRAM 不是共享 L2 |
| 外部内存与互联 | 32 GB GDDR6、512 GB/s；4×800G；PCIe 5.0 x16 | 卡级峰值，不是 Galaxy 聚合值 |
| 软件 | TT-Metalium、TTNN、TT-Forge；reader/compute/writer 循环缓冲 | 可编程数据流不等于硬件 Search/Top-k |

## Galaxy 系统边界

Galaxy 是 32 ASIC 系统。旧版资料记录 1 TB GDDR6、16 TB/s、约 6.2 GB SRAM、约 2.9 PB/s 和 23 PFLOPS BlockFP8 等系统级口径；这些数字不能写入 Blackhole 单芯片行。350+ tokens/s/user 也属于特定系统工作负载，不能替代 Retrieval 专项 TPOT。

## 生命周期状态

| 阶段 | Blackhole / Galaxy 的公开状态 | 证据边界 |
| --- | --- | --- |
| 宣布/发布 | Blackhole developer products 已有官方首发材料；Galaxy 有官方产品页和 GA 公告 | 直接来源确认产品公开，不自动证明裸芯片流片或量产批次 |
| 流片/工程样片 | 公开资料未确认 | Developer card/产品页不能替代晶圆或样片披露 |
| 量产/出货 | 公开资料未确认裸芯片独立批次；Galaxy 的系统可用性按系统产品口径记录 | 系统页面数字不回填到 Blackhole 单芯片 |
| 客户部署 | 公开资料未确认 | 开发者产品销售/展示不等于客户生产部署 |
| 云/实例可用 | 公开资料未确认 | 软件和系统资料不能推导公有云实例 |
| 路线图 | 公开资料未确认后续芯片型号 | 不以传闻补齐代际 |

## 直接来源

- [Blackhole Developer Products 首发](https://tenstorrent.com/en/newsroom/tenstorrent-launches-blackhole-developer-products-at-tenstorrent-dev-day)
- [Blackhole 当前卡页](https://tenstorrent.com/en/hardware/cards)
- [Galaxy Blackhole 产品页](https://tenstorrent.com/hardware/galaxy)
- [Galaxy GA 公告](https://tenstorrent.com/newsroom/tenstorrent-enables-ai-at-scale-with-industry-leading-performance)
- [TT-System-Firmware Blackhole 文档](https://docs.tenstorrent.com/tt-system-firmware/boards/tenstorrent/tt_blackhole/doc/index.html)
- [TT-Metalium guide](https://github.com/tenstorrent/tt-metal/blob/main/METALIUM_GUIDE.md)

## 证据边界

公开材料支持显式数据流、软件可见 SRAM/NoC 和多卡 Ethernet 的研究判断；没有公开 Search core、索引 SRAM、Merge Top-k、indexed Gather DMA 或 page-map descriptor。Blackhole 的可编程性是软件研究入口，不能写成这些硬件模块已经存在。
