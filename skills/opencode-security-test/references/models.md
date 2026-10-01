# Model selection

Read this when choosing the model for a security task. Open-source models run
through gateways that are already configured. Prefer, in order: OpenCode Go —
then OpenRouter — then Baseten or another configured gateway (Cloudflare AI
Gateway and OpenCode Zen also carry parts of this roster). Use the exact
provider/model reference from the catalog (for example
`opencode-go/deepseek-v4.1-flash`) and record it in the report. Local inference
is optional, not a requirement.

The scores and capabilities below are Cyberrouter's per-task model ranking
(captured 2026-10-01). Cyberrouter is not a provider in this setup; treat it as
a ranking source. Scores change; refresh them before a long engagement.

## Quick picks

| Task | Start here | Score | Gateway reference |
| --- | --- | --- | --- |
| Vulnerability discovery | deepseek-v4.1-flash | 0.881 | `opencode-go/deepseek-v4.1-flash` |
| Exploit development | deepseek-v4.1-flash | 1.00 | `opencode-go/deepseek-v4.1-flash` |
| Remediation | kimi-k2.6 | 0.802 | `openrouter/moonshotai/kimi-k2.6` |
| Triage | gpt-oss-120b | 0.714 | `openrouter/openai/gpt-oss-120b` |

When one model must cover several phases, `deepseek-v4.1-flash`
(0.881 / 1.00 / 0.742) leads every scored task; `glm-5.3` is the closest
all-round alternative.

## The roster

All fourteen are open-weight. Refs are listed in preference order:
`opencode-go/...` first (flat-rate subscription), then `openrouter/...`, then
`baseten/...` or another configured gateway. The four models OpenCode Go does
not carry (kimi-k2.6, gpt-oss-120b, inkling, nemotron-ultra) start at
OpenRouter.

| Model | Capabilities | Vuln | Exploit | Remediation | Triage | Gateway refs |
| --- | --- | --- | --- | --- | --- | --- |
| glm-5.3 | vuln discovery, exploit dev, remediation, triage | 0.845 | 0.727 | 0.669 | – | `opencode-go/glm-5.3`, `openrouter/z-ai/glm-5.3`, `baseten/zai-org/GLM-5.3` |
| glm-5.3-flash | remediation, triage | – | – | 0.634 | – | `opencode-go/glm-5.3-flash`, `openrouter/z-ai/glm-5.3-flash`, `baseten/zai-org/GLM-5.3-Flash` |
| glm-5.2 | vuln discovery, exploit dev, remediation | 0.772 | 0.244 | 0.462 | – | `opencode-go/glm-5.2`, `openrouter/z-ai/glm-5.2`, `baseten/zai-org/GLM-5.2` |
| deepseek-v4-pro | vuln discovery, exploit dev, remediation | 0.833 | 0.273 | 0.627 | – | `opencode-go/deepseek-v4-pro`, `openrouter/deepseek/deepseek-v4-pro`, `baseten/deepseek-ai/DeepSeek-V4-Pro`, `cloudflare-ai-gateway/deepseek/deepseek-v4-pro` |
| deepseek-v4.1-flash | vuln discovery, exploit dev, remediation | 0.881 | 1.00 | 0.742 | – | `opencode-go/deepseek-v4.1-flash`, `openrouter/deepseek/deepseek-v4.1-flash`, `baseten/deepseek-ai/DeepSeek-V4.1-Flash` |
| deepseek-v4-flash | vuln discovery, exploit dev | 0.767 | 0.503 | – | – | `opencode-go/deepseek-v4-flash`, `openrouter/deepseek/deepseek-v4-flash`, `baseten/deepseek-ai/DeepSeek-V4-Flash-0731` |
| qwen3.8-max | vuln discovery, exploit dev, remediation | 0.785 | 0.455 | 0.677 | – | `opencode-go/qwen3.8-max`, `openrouter/qwen/qwen3.8-max-0902`, `cloudflare-ai-gateway/alibaba/qwen3.8-max` |
| qwen3.8-flash | remediation | – | – | 0.625 | – | `opencode-go/qwen3.8-flash`, `openrouter/qwen/qwen3.8-flash` |
| kimi-k3 | exploit dev, remediation | – | 0.273 | 0.675 | – | `opencode-go/kimi-k3`, `openrouter/moonshotai/kimi-k3`, `baseten/moonshotai/Kimi-K3`, `cloudflare-ai-gateway/moonshotai/kimi-k3` |
| kimi-k2.6 | remediation | – | – | 0.802 | – | `openrouter/moonshotai/kimi-k2.6`, `baseten/moonshotai/Kimi-K2.6`, `opencode/kimi-k2.6` |
| gpt-oss-120b | triage | – | – | – | 0.714 | `openrouter/openai/gpt-oss-120b`, `baseten/openai/gpt-oss-120b` |
| minimax-m3 | remediation | – | – | 0.590 | – | `opencode-go/minimax-m3`, `openrouter/minimax/minimax-m3`, `opencode/minimax-m3` |
| inkling | vuln discovery, remediation | – | – | 0.776 | – | `openrouter/thinkingmachines/inkling`, `baseten/thinkingmachines/inkling` |
| nemotron-ultra | remediation | – | – | 0.719 | – | `openrouter/nvidia/nemotron-3-ultra-550b-a55b`, `baseten/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B` |

Triage is the only task with a single scored model; `glm-5.3` and
`glm-5.3-flash` list triage as a capability without a score. For unscored work,
start from the vulnerability-discovery ranking (`deepseek-v4.1-flash`,
`glm-5.3`, `deepseek-v4-pro`) and label the choice as a judgment call.

## Refresh the catalog

- `opencode models` lists every configured provider and model reference.
- OpenRouter publishes its catalog at `https://openrouter.ai/api/v1/models`;
  filter for families, for example:
  `curl -s https://openrouter.ai/api/v1/models | jq -r '.data[].id' | grep -Ei 'deepseek|glm|kimi|qwen'`.
- Prefer zero-data-retention (ZDR) endpoints for sensitive code where the
  gateway offers them.

## Cross-checks

Public evaluations broadly agree at the family level: open-weight models now
match or beat closed frontier models on pooled vulnerability discovery (Aikido,
Aug 2026), GLM leads open weights on narrow cyber tasks (UK AISI, Jul 2026),
and open models reach mid exploitation tiers but not full arbitrary code
execution on hardened targets (ExploitBench, Jun 2026). Use these when the
task-score table lacks a row, and record the source and date.
