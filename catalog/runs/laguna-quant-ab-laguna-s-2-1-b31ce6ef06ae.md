# `laguna-quant-ab/new-w4a16/depth-196608x256-c1`

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
| Objective | context_depth |
| TPS kind | aggregate_output |
| Layout | TP=4 |
| Context | 262144 |
| Concurrency | 1 |
| Prompt tokens | 196608 |
| Generated tokens | 256 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 1.8928871414827217 |
| `decode_tok_s` | 89.93373337440248 |
| `prefill_tok_s` | 1499.3173119691628 |
| `total_tok_s` | 1455.933369506466 |
| `req_s` | 0.007394090396416882 |
| `ttft_p50_ms` | 132407.01724984683 |
| `ttft_p99_ms` | 132407.01724984683 |
| `itl_p50_ms` | 12.014128034934402 |
| `tpot_p50_ms` | 11.11929820412222 |
| `e2e_p99_ms` | 135242.438291898 |
| `vram_peak_mib` | 95184 |
| `avg_power_w` | 829.4649333333334 |
| `max_temp_c` | 75.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-W4A16' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 127.0.0.1 --port 18025 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "depth-196608x256-c1",
  "num_prompts": 1,
  "output_tok_per_watt": 0.0022820580658857526,
  "prefix_hit_rate": 0.0,
  "throttle_sample_count": 541
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-25/laguna-s21-w4a16-vs-official-int4-4x3090/new-w4a16/depth-196608x256-c1.json`

## Notes

Fresh same-runtime A/B with identical seeds, workloads, TP4, FP8 KV, CUDA-graph and prefix-cache settings. Synthetic speed point; fixed-content results remain in the raw artifact.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
