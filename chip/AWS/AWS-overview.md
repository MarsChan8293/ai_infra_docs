---
title: "AWS AI Accelerators"
vendor: AWS
object_type: vendor-overview
updated: 2026-09-15
---
# AWS AI Accelerators

AWS 的 Inferentia / Trainium 只通过 EC2、UltraServer、UltraCluster 与托管服务交付。芯片与云/系统聚合规格必须分开。

| 对象 | 层级 | 状态 | 关键事实 |
|---|---|---|---|
| [[chip/AWS/inferentia-v1|Inferentia]] | chip | ga | 4×NeuronCore-v1；8GB DDR4 |
| [[chip/AWS/trainium-v1|Trainium]] | chip | ga | NeuronCore-v2；32GiB HBM |
| [[chip/AWS/inferentia2|Inferentia2]] | chip | ga | 32GB HBM；Inf2 GA |
| [[chip/AWS/trainium2|Trainium2]] | chip | ga | 96GiB HBM；2.9TB/s |
| [[chip/AWS/trainium3|Trainium3]] | chip | ga | 3nm；144GB HBM3e；4.9TB/s |
| [[chip/AWS/trainium4-roadmap|Trainium4]] | chip | roadmap | 2027 交付路线图 |

## 边界
- `Inf1/Inf2/Trn1/Trn2/Trn3` 是实例或平台命名，不自动等于单芯片。
- 云 GA 证明服务可用，不等于公开晶圆量产、良率或累计出货。

## 来源
- https://aws.amazon.com/ai/machine-learning/inferentia/
- https://aws.amazon.com/ai/machine-learning/trainium/
- https://aws.amazon.com/ec2/instance-types/trn3/
