# `laguna-dflash/target/short-512x256-c1`

| field | value |
|---|---|
| Date | 2026-07-22 |
| Campaign | laguna-dflash |
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
| Concurrency | 1 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 88.2554988438454 |
| `decode_tok_s` | 98.50691101928982 |
| `prefill_tok_s` | 1714.8169924832785 |
| `total_tok_s` | 275.3674988340684 |
| `req_s` | 0.3447480423587711 |
| `ttft_p50_ms` | 315.75423752656206 |
| `ttft_p99_ms` | 322.6282248541247 |
| `itl_p50_ms` | 10.140008002053946 |
| `tpot_p50_ms` | 10.148241266599108 |
| `e2e_p99_ms` | 2908.730711165117 |
| `vram_peak_mib` | 96046 |
| `avg_power_w` | 771.3523529411765 |
| `max_temp_c` | 73.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-INT4' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 0.0.0.0 --port 8001 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "short-512x256-c1",
  "num_prompts": 8,
  "output_tok_per_watt": 0.1144165808366644,
  "prefix_hit_rate": 0.0589590050667895,
  "throttle_sample_count": 97
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-22/laguna-s-2.1-dflash-4x3090/target/short-512x256-c1.json`

## Notes

Identical seeds and workload labels. Target profile: 262144 context at gpu_memory_utilization=0.95. DFlash speed profile: 131456 context at gpu_memory_utilization=0.85 (K7) or 0.833 (K15); full262 runtime-OOM controls are retained beside the canonical artifact. K15 C64 uses the separate 32768-context, gpu_memory_utilization=0.815 high-concurrency profile.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
