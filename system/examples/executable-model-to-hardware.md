---
title: Executable Model → System → Hardware Case
aliases:
  - Executable Reference Case
tags:
  - system
  - executable
  - example
updated: 2026-09-25
---
# Executable Model → System → Hardware Case

> 这个案例把 [[system/examples/model-to-hardware-walkthrough|手工 walkthrough]] 变成 CI 可重复执行的派生链。输入仍是 Qwen3.8-27B + MI300X + 64K batch=1 Decode，机器结果必须保留公式、输入、假设、单位和未知项。

## 输入

- Model：[[models/Qwen/qwen3.8-27b|Qwen3.8-27B]]
- Hardware：[[chip/AMD/mi300x|AMD Instinct MI300X]]
- Workload Profile 定义：[[system/workload/workload-profile-v0.1|Workload Profile V0.1]]
- Scenario YAML：`examples/workloads/qwen3.8-27b-mi300x-decode-64k.yaml`

场景显式假设：

- weight payload 使用 2 bytes / parameter；
- 每个 Decode step 完整读取一次 weight payload；
- 每个 Decode step 完整读取一次 64K growing KV payload；
- activation、workspace、allocator、runtime reserve 与固定 recurrent state 继续保持 unknown。

## 执行

```bash
python scripts/build-workload-profile.py \
  --root . \
  --input examples/workloads/qwen3.8-27b-mi300x-decode-64k.yaml \
  --output generated/executable/qwen3.8-27b-mi300x-profile.json

python scripts/build-system-requirements.py \
  --root . \
  --profile generated/executable/qwen3.8-27b-mi300x-profile.json \
  --output generated/executable/qwen3.8-27b-mi300x-requirements.json \
  --markdown-output system/derived/qwen3.8-27b-mi300x-decode-64k.md
```

`system/derived/` 由 CI 临时生成，不提交到 Git。这样派生页会在同一次构建里经过 repository Validator、进入 knowledge graph 并随 Quartz 发布，但不会形成第二份手工事实源。

## Reference Assertions

CI 固定检查以下可追溯结果：

| Metric | Expected |
|---|---:|
| weight payload | 54,000,000,000 bytes |
| growing KV / token | 32,768 bytes/token |
| growing KV @ 64K | 2,147,483,648 bytes |
| known resident lower bound | 56,147,483,648 bytes |
| linear compute approximation | 54,000,000,000 FLOP/token |
| inter-accelerator payload | 0 bytes/step |

这些 assertion 不是 benchmark，而是防止公式、单位或输入映射悄悄漂移。

## 未知项必须保留

MI300X canonical page 当前没有机器可读 compute throughput，因此生成器必须保留：

```text
ridge point / compute-vs-memory Roofline classification = unknown
```

CI 还会断言这个 unknown 存在，防止后续代码把缺失值静默当成 0。

## 公式入口

- [[system/memory/model-memory-accounting|Model Memory Accounting]]
- [[system/memory/kv-cache-model|KV Cache Model]]
- [[system/memory/memory-bandwidth-model|Memory Bandwidth Model]]
- [[system/compute/transformer-compute-model|Transformer Compute Model]]
- [[system/compute/roofline-and-arithmetic-intensity|Roofline 与 Arithmetic Intensity]]
- [[system/communication/communication-cost-model|Communication Cost Model]]

机器生成结果与手工 walkthrough 使用同一口径，二者可以互相做回归检查。
