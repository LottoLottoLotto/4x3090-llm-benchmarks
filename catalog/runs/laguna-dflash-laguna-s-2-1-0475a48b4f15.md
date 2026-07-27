# `laguna-dflash/target/short-512x256-c32`

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
| Concurrency | 32 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 380.4133419383066 |
| `decode_tok_s` | 14.051128110549318 |
| `prefill_tok_s` | 253.36431228213058 |
| `total_tok_s` | 1194.2944988574632 |
| `req_s` | 1.48598961694651 |
| `ttft_p50_ms` | 3121.424212004058 |
| `ttft_p99_ms` | 8740.328224172117 |
| `itl_p50_ms` | 51.605065003968775 |
| `tpot_p50_ms` | 71.39713770399491 |
| `e2e_p99_ms` | 26934.026710452745 |
| `vram_peak_mib` | 96054 |
| `avg_power_w` | 836.9413265306123 |
| `max_temp_c` | 76.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-INT4' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 0.0.0.0 --port 8001 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "short-512x256-c32",
  "num_prompts": 128,
  "output_tok_per_watt": 0.45452808922130866,
  "prefix_hit_rate": 0.05842581234131173,
  "throttle_sample_count": 348
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-22/laguna-s-2.1-dflash-4x3090/target/short-512x256-c32.json`

## Notes

Identical seeds and workload labels. Target profile: 262144 context at gpu_memory_utilization=0.95. DFlash speed profile: 131456 context at gpu_memory_utilization=0.85 (K7) or 0.833 (K15); full262 runtime-OOM controls are retained beside the canonical artifact. K15 C64 uses the separate 32768-context, gpu_memory_utilization=0.815 high-concurrency profile.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
