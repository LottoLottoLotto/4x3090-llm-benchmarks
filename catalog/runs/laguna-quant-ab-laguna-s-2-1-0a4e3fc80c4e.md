# `laguna-quant-ab/official-int4/prefix-cold-131072x64`

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
| `output_tok_s` | 0.7932371993620992 |
| `decode_tok_s` | 110.80245453230361 |
| `prefill_tok_s` | 1649.9472057033854 |
| `total_tok_s` | 1624.7356992621799 |
| `req_s` | 0.0123943312400328 |
| `ttft_p50_ms` | 80112.948236987 |
| `ttft_p99_ms` | 80112.948236987 |
| `itl_p50_ms` | 11.45300199277699 |
| `tpot_p50_ms` | 9.02507082736563 |
| `e2e_p99_ms` | 80681.52769911103 |
| `vram_peak_mib` | 96168 |
| `avg_power_w` | 814.5401063829788 |
| `max_temp_c` | 75.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-INT4' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 127.0.0.1 --port 18025 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "prefix-cold-131072x64",
  "num_prompts": 1,
  "output_tok_per_watt": 0.000973846705823392,
  "prefix_hit_rate": 0.0002442319287453348,
  "throttle_sample_count": 323
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-25/laguna-s21-w4a16-vs-official-int4-4x3090/official-int4/prefix-cold-131072x64.json`

## Notes

Fresh same-runtime A/B with identical seeds, workloads, TP4, FP8 KV, CUDA-graph and prefix-cache settings. Synthetic speed point; fixed-content results remain in the raw artifact.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
