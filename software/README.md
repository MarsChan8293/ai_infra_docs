---
title: AI Infra 软件资料库
aliases:
  - Software MOC
  - AI Infra Software Landscape
tags:
  - moc
  - software
  - ai-infra
---
# AI Infra 软件资料库

统一入口：[[software/00-project-index|Software Project Index]]。

`software/` 采用 Software Schema V0.1：具体软件统一放在 `projects/`，稳定机制放在 `concepts/`。Markdown 是事实源，YAML frontmatter 用于机器索引。

项目之间的仓库内引用统一使用 Wiki Link，例如 `[[software/projects/vllm|vLLM]]`。同仓库项目之间的明确关系要求双向可达：A 页面引用 B 时，B 页面也应保留到 A 的反向链接。

Schema 与维护规则见 [[software/SCHEMA|Software Schema V0.1]]。
