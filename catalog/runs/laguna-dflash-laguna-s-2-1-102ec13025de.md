# `laguna-dflash/dflash-k7/short-512x256-c64`

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
| Concurrency | 64 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 274.6135460728134 |
| `decode_tok_s` | 4.81597801174598 |
| `prefill_tok_s` | 334.3991308061495 |
| `total_tok_s` | 864.1133248533554 |
| `req_s` | 1.0727091643469273 |
| `ttft_p50_ms` | 2021.9247789937072 |
| `ttft_p99_ms` | 21997.609561530397 |
| `itl_p50_ms` | 403.16475700819865 |
| `tpot_p50_ms` | 209.0510740157162 |
| `e2e_p99_ms` | 85635.18375894053 |
| `vram_peak_mib` | 96448 |
| `avg_power_w` | 843.1267068273091 |
| `max_temp_c` | 75.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-INT4' --trust-remote-code --tensor-parallel-size 4 --max-model-len 131456 --gpu-memory-utilization 0.85 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 0.0.0.0 --port 8001 --no-enable-log-requests --speculative-config '{"model":"${MODEL_ROOT_ALT}/Laguna-S-2.1-DFlash-INT4","num_speculative_tokens":7,"method":"dflash"}'
```

## Speculative decoding

```json
{
  "acceptance": 0.21304634901391986,
  "accepted_tokens_per_round": 1.491324443097439,
  "draft_path": "${MODEL_ROOT_ALT}/Laguna-S-2.1-DFlash-INT4",
  "draft_ref": "Laguna-S-2.1-DFlash-INT4",
  "k": 7,
  "method": "dflash"
}
```

## Engine knobs

```json
{
  "label": "short-512x256-c64",
  "num_prompts": 256,
  "output_tok_per_watt": 0.3257085131441107,
  "prefix_hit_rate": 0.02911510274873297,
  "throttle_sample_count": 956
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-22/laguna-s-2.1-dflash-4x3090/dflash-k7/short-512x256-c64.json`

## Notes

Identical seeds and workload labels. Target profile: 262144 context at gpu_memory_utilization=0.95. DFlash speed profile: 131456 context at gpu_memory_utilization=0.85 (K7) or 0.833 (K15); full262 runtime-OOM controls are retained beside the canonical artifact. K15 C64 uses the separate 32768-context, gpu_memory_utilization=0.815 high-concurrency profile.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
