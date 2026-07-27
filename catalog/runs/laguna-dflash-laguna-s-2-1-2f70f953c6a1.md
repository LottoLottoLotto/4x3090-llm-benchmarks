# `laguna-dflash/target/prefix-warm-32768x64`

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
| Objective | prefix_cache |
| TPS kind | aggregate_output |
| Layout | TP=4 |
| Context | 262144 |
| Concurrency | 1 |
| Prompt tokens | 32768 |
| Generated tokens | 64 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 73.82992756531424 |
| `decode_tok_s` | 103.43680016111774 |
| `prefill_tok_s` | 198.58818887175215 |
| `total_tok_s` | 37923.20373097094 |
| `req_s` | 1.153592618208035 |
| `ttft_p50_ms` | 257.26537604350597 |
| `ttft_p99_ms` | 257.26537604350597 |
| `itl_p50_ms` | 10.3848020080477 |
| `tpot_p50_ms` | 9.667739126136498 |
| `e2e_p99_ms` | 866.3329409901053 |
| `vram_peak_mib` | 96168 |
| `avg_power_w` | 567.455 |
| `max_temp_c` | 69.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-INT4' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 0.0.0.0 --port 8001 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "prefix-warm-32768x64",
  "num_prompts": 1,
  "output_tok_per_watt": 0.1301071055243398,
  "prefix_hit_rate": 0.9996952148735142,
  "throttle_sample_count": 2
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-22/laguna-s-2.1-dflash-4x3090/target/prefix-warm-32768x64.json`

## Notes

Identical seeds and workload labels. Target profile: 262144 context at gpu_memory_utilization=0.95. DFlash speed profile: 131456 context at gpu_memory_utilization=0.85 (K7) or 0.833 (K15); full262 runtime-OOM controls are retained beside the canonical artifact. K15 C64 uses the separate 32768-context, gpu_memory_utilization=0.815 high-concurrency profile.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
