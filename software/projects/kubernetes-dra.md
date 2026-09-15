---
schema_version: software-v0.1
name: Kubernetes DRA
object_type: project
category: device-resource
organization: Kubernetes
status: active
repo: null
docs: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - deviceclass
  - resourceclaim
  - resourceclaimtemplate
  - resourceslice
  - structured-device-selection
integrations:
  - hami
  - kai-scheduler
backends: []
updated: 2026-09-15
---
# Kubernetes DRA

> Kubernetes Dynamic Resource Allocation，用结构化 API 表达、选择和分配复杂设备资源。

## 核心能力

| 能力 | 说明 |
|---|---|
| DeviceClass | 定义一类可申请设备及选择规则 |
| ResourceClaim | 表达 workload 对具体设备资源的申请 |
| ResourceClaimTemplate | 为多副本 workload 生成独立 claim |
| ResourceSlice | 由 driver 发布可分配设备及属性 |
| Structured Selection | 比简单整数扩展资源表达更丰富的设备条件 |

## 边界

DRA 是资源声明与分配框架，不执行 GPU/NPU 数据路径，也不会自动提供设备共享或隔离。底层能力仍取决于 DRA driver、runtime 和具体硬件。

其角色和 HAMi、调度器的关系见 [[software/concepts/accelerator-resource-model|加速器资源模型]]。

## 集成与后端

- HAMi-DRA 等组件可以把 HAMi 管理的设备接入 DRA 模型。
- KAI-Scheduler 等调度器可利用更丰富的设备资源信息做 placement。
- DRA 本身不绑定某一硬件厂商，因此 `backends` 保持为空。

## 版本快照

DRA 能力强依赖 Kubernetes 版本。当前页未绑定具体 Kubernetes release，因此只记录稳定对象模型，不把版本相关 alpha/beta 子特性写进 V0.1 capability 列表。

## 直接来源

- https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/
- https://v1-34.docs.kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/
- https://github.com/Project-HAMi/HAMi-dra
- https://github.com/kai-scheduler/KAI-Scheduler
