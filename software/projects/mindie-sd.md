---
schema_version: software-v0.1
name: MindIE-SD
object_type: project
category: inference-engine
organization: Ascend
status: active
repo: null
docs: null
snapshot:
  version: null
  commit: null
  as_of: 2026-09-15
capabilities:
  - diffusion-inference
  - ascend-inference
integrations: []
backends:
  - ascend
updated: 2026-09-15
---
# MindIE-SD

> MindIE 生态中面向 Stable Diffusion / 生成式视觉推理的 Ascend 优化组件。

## 核心能力

补充当前软件库偏 LLM 的盲区，用于观察 Ascend 上生成式视觉模型的推理栈与优化方式。

## 边界

MindIE-SD 面向 diffusion 类工作负载，不代表 LLM serving 能力。

## 集成与后端

与 [[software/projects/mindie-llm|MindIE-LLM]] 同属 MindIE 生态，但工作负载不同。

## 关联项目

- [[software/projects/mindie-llm|MindIE-LLM]]
- [[software/projects/msmodelslim|msModelSlim]]

## 版本快照

本页以 2026-09-15 前 Ascend 公开生态资料为快照；未确认独立 canonical GitHub 仓库。

## 直接来源

- https://github.com/Ascend
