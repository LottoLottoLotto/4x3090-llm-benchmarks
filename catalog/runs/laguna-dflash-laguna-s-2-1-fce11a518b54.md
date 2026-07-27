# `laguna-dflash/dflash-k15/short-512x256-c2`

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
| Context | 131456 |
| Concurrency | 2 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 77.94812446173938 |
| `decode_tok_s` | 41.9968224968477 |
| `prefill_tok_s` | 1378.6026854239612 |
| `total_tok_s` | 241.07588883821157 |
| `req_s` | 0.30448486117866946 |
| `ttft_p50_ms` | 416.71730449888855 |
| `ttft_p99_ms` | 917.7320445340591 |
| `itl_p50_ms` | 62.65335297212005 |
| `tpot_p50_ms` | 22.628503505770556 |
| `e2e_p99_ms` | 8068.617054733913 |
| `vram_peak_mib` | 92076 |
| `avg_power_w` | 775.9205405405406 |
| `max_temp_c` | 74.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-INT4' --trust-remote-code --tensor-parallel-size 4 --max-model-len 131456 --gpu-memory-utilization 0.833 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 0.0.0.0 --port 8001 --no-enable-log-requests --speculative-config '{"model":"${MODEL_ROOT_ALT}/Laguna-S-2.1-DFlash-INT4","num_speculative_tokens":15,"method":"dflash"}'
```

## Speculative decoding

```json
{
  "acceptance": 0.11983805668016194,
  "accepted_tokens_per_round": 1.7975708502024292,
  "draft_path": "${MODEL_ROOT_ALT}/Laguna-S-2.1-DFlash-INT4",
  "draft_ref": "Laguna-S-2.1-DFlash-INT4",
  "k": 15,
  "method": "dflash"
}
```

## Engine knobs

```json
{
  "label": "short-512x256-c2",
  "num_prompts": 8,
  "output_tok_per_watt": 0.1004589006078345,
  "prefix_hit_rate": 0.029864675688287448,
  "throttle_sample_count": 108
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-22/laguna-s-2.1-dflash-4x3090/dflash-k15/short-512x256-c2.json`

## Notes

Identical seeds and workload labels. Target profile: 262144 context at gpu_memory_utilization=0.95. DFlash speed profile: 131456 context at gpu_memory_utilization=0.85 (K7) or 0.833 (K15); full262 runtime-OOM controls are retained beside the canonical artifact. K15 C64 uses the separate 32768-context, gpu_memory_utilization=0.815 high-concurrency profile.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
