---
schema_version: software-v0.1
name: 开源社区与上游组织
object_type: concept
category: ecosystem
updated: 2026-09-15
---
# 开源社区与上游组织

> 按 canonical upstream namespace / 治理组织观察 AI Infra 软件生态；项目事实仍以 `software/projects/` 为准。

## 组织与项目

- `vllm-project`：[[software/projects/vllm|vLLM]] · [[software/projects/aibrix|AIBrix]] · [[software/projects/vllm-ascend|vLLM-Ascend]]
- `ai-dynamo`：[[software/projects/nvidia-dynamo|NVIDIA Dynamo]] · [[software/projects/nixl|NIXL]]
- `kvcache-ai`：[[software/projects/ktransformers|KTransformers]] · [[software/projects/mooncake|Mooncake]]
- `Ascend`：[[software/projects/mindie-llm|MindIE-LLM]] · [[software/projects/mindie-motor|MindIE-Motor]] · [[software/projects/mindie-sd|MindIE-SD]] · [[software/projects/msmodelslim|msModelSlim]] · [[software/projects/ops-transformer|ops-transformer]]
- `deepseek-ai`：[[software/projects/deepseek-infra|DeepSeek-Infra]] · [[software/projects/3fs|3FS]] · [[software/projects/deepep|DeepEP]] · [[software/projects/deepgemm|DeepGEMM]] · [[software/projects/deepjit|DeepJIT]] · [[software/projects/flashmla|FlashMLA]]
- `hpcaitech`：[[software/projects/colossal-ai|Colossal-AI]]
- `flashinfer-ai`：[[software/projects/flashinfer|FlashInfer]]
- `Project-HAMi`：[[software/projects/hami|HAMi]]
- `LMCache`：[[software/projects/lmcache|LMCache]]
- `ModelTC`：[[software/projects/lightllm|LightLLM]]
- `Oneflow-Inc`：[[software/projects/oneflow|OneFlow]]
- `ray-project`：[[software/projects/ray-serve|Ray Serve]]
- `sgl-project`：[[software/projects/sglang|SGLang]]
- `flagos-ai`：[[software/projects/flagos|FlagOS]] · [[software/projects/flagscale|FlagScale]] · [[software/projects/flaggems|FlagGems]] · [[software/projects/flagcx|FlagCX]] · [[software/projects/flagtree|FlagTree]] · [[software/projects/flagattention|FlagAttention]] · [[software/projects/flagrelease|FlagRelease]] · [[software/projects/flagperf|FlagPerf]] · [[software/projects/vllm-plugin-fl|vllm-plugin-FL]] · [[software/projects/sglang-plugin-fl|sglang-plugin-FL]]
- `NVIDIA / triton-inference-server`：[[software/projects/tensorrt-llm|TensorRT-LLM]] · [[software/projects/triton-inference-server|Triton Inference Server]] · [[software/projects/nvidia-gpu-operator|NVIDIA GPU Operator]] · [[software/projects/nvidia-k8s-device-plugin|NVIDIA k8s-device-plugin]]
- `tile-ai`：[[software/projects/tilelang|TileLang]]
- `lightseekorg`：[[software/projects/tokenspeed|TokenSpeed]]
- `sii-research`：[[software/projects/vccl|VCCL]]
- `llm-d`：[[software/projects/llm-d|llm-d]]

## 为什么单独保留社区视图

技术分类回答“项目做什么”，社区视图回答“项目从哪里长出来”。同一组织往往会形成自己的 runtime、kernel、通信和插件组合，理解 upstream namespace 有助于判断接口协同、版本演进和维护边界。

## 维护规则

- 目录仍按项目平铺，不按组织重新嵌套。
- `organization` 使用 canonical upstream namespace 或明确治理组织。
- 公司贡献关系不等于项目组织关系；V0.1 暂不把公司关系塞进 frontmatter。
- 项目能力、版本、来源仍回到各自项目页维护。

## 参考发现源

- https://github.com/MarsChan8293/ai_infra_relationship/blob/main/community/community.md
