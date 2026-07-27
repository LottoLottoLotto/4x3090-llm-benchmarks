# `laguna-quant-ab/new-w4a16/short-512x256-c12`

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
| Concurrency | 12 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 265.69794759897354 |
| `decode_tok_s` | 26.359217156123158 |
| `prefill_tok_s` | 403.5347293100324 |
| `total_tok_s` | 831.1926109742955 |
| `req_s` | 1.0378826078084904 |
| `ttft_p50_ms` | 1928.8805350661278 |
| `ttft_p99_ms` | 3320.14299222501 |
| `itl_p50_ms` | 32.34945912845433 |
| `tpot_p50_ms` | 37.43293983313967 |
| `e2e_p99_ms` | 12600.65072964644 |
| `vram_peak_mib` | 95076 |
| `avg_power_w` | 811.8084210526316 |
| `max_temp_c` | 74.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-W4A16' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 127.0.0.1 --port 18025 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "short-512x256-c12",
  "num_prompts": 48,
  "output_tok_per_watt": 0.3272914405771453,
  "prefix_hit_rate": 0.05873131189538485,
  "throttle_sample_count": 185
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-25/laguna-s21-w4a16-vs-official-int4-4x3090/new-w4a16/short-512x256-c12.json`

## Notes

Fresh same-runtime A/B with identical seeds, workloads, TP4, FP8 KV, CUDA-graph and prefix-cache settings. Synthetic speed point; fixed-content results remain in the raw artifact.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
