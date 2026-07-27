# `laguna-quant-ab/official-int4/short-512x256-c2`

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
| Concurrency | 2 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 131.93048928273214 |
| `decode_tok_s` | 74.6558606966915 |
| `prefill_tok_s` | 1678.1205796416389 |
| `total_tok_s` | 408.0311128500124 |
| `req_s` | 0.5153534737606724 |
| `ttft_p50_ms` | 436.0245110001415 |
| `ttft_p99_ms` | 662.7425302518532 |
| `itl_p50_ms` | 12.858153902925551 |
| `tpot_p50_ms` | 13.287217297828665 |
| `e2e_p99_ms` | 3952.0576184918173 |
| `vram_peak_mib` | 96050 |
| `avg_power_w` | 742.5388888888889 |
| `max_temp_c` | 73.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-INT4' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 127.0.0.1 --port 18025 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "short-512x256-c2",
  "num_prompts": 8,
  "output_tok_per_watt": 0.17767485482160894,
  "prefix_hit_rate": 0.059729351376574896,
  "throttle_sample_count": 64
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-25/laguna-s21-w4a16-vs-official-int4-4x3090/official-int4/short-512x256-c2.json`

## Notes

Fresh same-runtime A/B with identical seeds, workloads, TP4, FP8 KV, CUDA-graph and prefix-cache settings. Synthetic speed point; fixed-content results remain in the raw artifact.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
