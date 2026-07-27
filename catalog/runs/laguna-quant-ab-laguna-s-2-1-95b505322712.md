# `laguna-quant-ab/official-int4/medium-4096x256-c4`

| field | value |
|---|---|
| Date | 2026-07-25 |
| Campaign | laguna-quant-ab |
| Model | Laguna-S-2.1 |
| Checkpoint | poolside/Laguna-S-2.1-INT4 |
| Quant | compressed-tensors-int4-g32-symmetric |
| Quant method | compressed-tensors |
| Engine | vllm |
| Engine version | 0.25.0 |
| Objective | concurrency_sweep |
| TPS kind | aggregate_output |
| Layout | TP=4 |
| Context | 262144 |
| Concurrency | 4 |
| Prompt tokens | 4096 |
| Generated tokens | 256 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 81.9534053721805 |
| `decode_tok_s` | 37.83560904311795 |
| `prefill_tok_s` | 1124.5942808795778 |
| `total_tok_s` | 1402.1715450396507 |
| `req_s` | 0.32013048973508007 |
| `ttft_p50_ms` | 5720.4915473703295 |
| `ttft_p99_ms` | 8339.934768502135 |
| `itl_p50_ms` | 16.326661920174956 |
| `tpot_p50_ms` | 26.310191129096875 |
| `e2e_p99_ms` | 14487.79648059979 |
| `vram_peak_mib` | 96168 |
| `avg_power_w` | 771.7844444444445 |
| `max_temp_c` | 73.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-INT4' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 127.0.0.1 --port 18025 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "medium-4096x256-c4",
  "num_prompts": 8,
  "output_tok_per_watt": 0.10618691003959431,
  "prefix_hit_rate": 0.007759456838021339,
  "throttle_sample_count": 85
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-25/laguna-s21-w4a16-vs-official-int4-4x3090/official-int4/medium-4096x256-c4.json`

## Notes

Fresh same-runtime A/B with identical seeds, workloads, TP4, FP8 KV, CUDA-graph and prefix-cache settings. Synthetic speed point; fixed-content results remain in the raw artifact.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
