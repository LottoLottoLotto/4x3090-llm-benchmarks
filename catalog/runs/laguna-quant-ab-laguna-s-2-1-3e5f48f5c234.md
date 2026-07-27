# `laguna-quant-ab/new-w4a16/prefix-cold-131072x64`

| field | value |
|---|---|
| Date | 2026-07-25 |
| Campaign | laguna-quant-ab |
| Model | Laguna-S-2.1 |
| Checkpoint | Relativ3pa1n/Laguna-S-2.1-W4A16 |
| Quant | compressed-tensors-w4a16-g32-asym-rtn |
| Quant method | compressed-tensors |
| Engine | vllm |
| Engine version | 0.25.0 |
| Objective | prefix_cache |
| TPS kind | aggregate_output |
| Layout | TP=4 |
| Context | 262144 |
| Concurrency | 1 |
| Prompt tokens | 131072 |
| Generated tokens | 64 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 0.7849556227667998 |
| `decode_tok_s` | 113.76839714990986 |
| `prefill_tok_s` | 1632.9828193500812 |
| `total_tok_s` | 1607.773089400492 |
| `req_s` | 0.012264931605731246 |
| `ttft_p50_ms` | 80978.8698409684 |
| `ttft_p99_ms` | 80978.8698409684 |
| `itl_p50_ms` | 11.360993492417037 |
| `tpot_p50_ms` | 8.78978719092196 |
| `e2e_p99_ms` | 81532.62643399648 |
| `vram_peak_mib` | 95184 |
| `avg_power_w` | 811.2110526315789 |
| `max_temp_c` | 74.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-W4A16' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 127.0.0.1 --port 18025 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "prefix-cold-131072x64",
  "num_prompts": 1,
  "output_tok_per_watt": 0.000967634279908285,
  "prefix_hit_rate": 0.0002442319287453348,
  "throttle_sample_count": 327
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-25/laguna-s21-w4a16-vs-official-int4-4x3090/new-w4a16/prefix-cold-131072x64.json`

## Notes

Fresh same-runtime A/B with identical seeds, workloads, TP4, FP8 KV, CUDA-graph and prefix-cache settings. Synthetic speed point; fixed-content results remain in the raw artifact.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
