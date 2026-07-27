# `laguna-quant-ab/new-w4a16/medium-4096x256-c4`

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
| `output_tok_s` | 80.86804391027675 |
| `decode_tok_s` | 37.37627722546728 |
| `prefill_tok_s` | 1108.9763040956202 |
| `total_tok_s` | 1383.6016887773915 |
| `req_s` | 0.31589079652451857 |
| `ttft_p50_ms` | 5806.208722060546 |
| `ttft_p99_ms` | 8474.56402148353 |
| `itl_p50_ms` | 16.52546040713787 |
| `tpot_p50_ms` | 26.626011311971382 |
| `e2e_p99_ms` | 14685.519633216318 |
| `vram_peak_mib` | 95184 |
| `avg_power_w` | 766.5754054054054 |
| `max_temp_c` | 73.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-W4A16' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 127.0.0.1 --port 18025 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "medium-4096x256-c4",
  "num_prompts": 8,
  "output_tok_per_watt": 0.1054926147382846,
  "prefix_hit_rate": 0.007759456838021339,
  "throttle_sample_count": 100
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-25/laguna-s21-w4a16-vs-official-int4-4x3090/new-w4a16/medium-4096x256-c4.json`

## Notes

Fresh same-runtime A/B with identical seeds, workloads, TP4, FP8 KV, CUDA-graph and prefix-cache settings. Synthetic speed point; fixed-content results remain in the raw artifact.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
