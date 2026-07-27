# `laguna-dflash/target/generation-512x64-c1`

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
| Objective | generation_length |
| TPS kind | aggregate_output |
| Layout | TP=4 |
| Context | 262144 |
| Concurrency | 1 |
| Prompt tokens | 512 |
| Generated tokens | 64 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 66.61833405924324 |
| `decode_tok_s` | 98.9156142643231 |
| `prefill_tok_s` | 1709.1911200142717 |
| `total_tok_s` | 643.2832882595675 |
| `req_s` | 1.0409114696756756 |
| `ttft_p50_ms` | 320.79486397560686 |
| `ttft_p99_ms` | 334.36144732288085 |
| `itl_p50_ms` | 10.120491439010948 |
| `tpot_p50_ms` | 10.1115942132541 |
| `e2e_p99_ms` | 969.1533897025511 |
| `vram_peak_mib` | 96168 |
| `avg_power_w` | 642.0486666666667 |
| `max_temp_c` | 72.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-INT4' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 0.0.0.0 --port 8001 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "generation-512x64-c1",
  "num_prompts": 4,
  "output_tok_per_watt": 0.10375901005309551,
  "prefix_hit_rate": 0.04332129963898917,
  "throttle_sample_count": 20
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-22/laguna-s-2.1-dflash-4x3090/target/generation-512x64-c1.json`

## Notes

Identical seeds and workload labels. Target profile: 262144 context at gpu_memory_utilization=0.95. DFlash speed profile: 131456 context at gpu_memory_utilization=0.85 (K7) or 0.833 (K15); full262 runtime-OOM controls are retained beside the canonical artifact. K15 C64 uses the separate 32768-context, gpu_memory_utilization=0.815 high-concurrency profile.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
