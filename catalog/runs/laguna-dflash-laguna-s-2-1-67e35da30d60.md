# `laguna-dflash/dflash-k7/medium-4096x256-c4`

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
| Concurrency | 4 |
| Prompt tokens | 4096 |
| Generated tokens | 256 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 63.44345615112076 |
| `decode_tok_s` | 21.796607049568987 |
| `prefill_tok_s` | 1425.4350715120083 |
| `total_tok_s` | 1085.4778825855817 |
| `req_s` | 0.24782600059031548 |
| `ttft_p50_ms` | 2526.554010459222 |
| `ttft_p99_ms` | 8657.592389839701 |
| `itl_p50_ms` | 62.389837927185 |
| `tpot_p50_ms` | 46.105738709835954 |
| `e2e_p99_ms` | 23250.46636224724 |
| `vram_peak_mib` | 96448 |
| `avg_power_w` | 788.6261363636364 |
| `max_temp_c` | 74.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-INT4' --trust-remote-code --tensor-parallel-size 4 --max-model-len 131456 --gpu-memory-utilization 0.85 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 0.0.0.0 --port 8001 --no-enable-log-requests --speculative-config '{"model":"${MODEL_ROOT_ALT}/Laguna-S-2.1-DFlash-INT4","num_speculative_tokens":7,"method":"dflash"}'
```

## Speculative decoding

```json
{
  "acceptance": 0.16382150344414495,
  "accepted_tokens_per_round": 1.1467505241090146,
  "draft_path": "${MODEL_ROOT_ALT}/Laguna-S-2.1-DFlash-INT4",
  "draft_ref": "Laguna-S-2.1-DFlash-INT4",
  "k": 7,
  "method": "dflash"
}
```

## Engine knobs

```json
{
  "label": "medium-4096x256-c4",
  "num_prompts": 8,
  "output_tok_per_watt": 0.08044807701106538,
  "prefix_hit_rate": 0.0038797284190106693,
  "throttle_sample_count": 134
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-22/laguna-s-2.1-dflash-4x3090/dflash-k7/medium-4096x256-c4.json`

## Notes

Identical seeds and workload labels. Target profile: 262144 context at gpu_memory_utilization=0.95. DFlash speed profile: 131456 context at gpu_memory_utilization=0.85 (K7) or 0.833 (K15); full262 runtime-OOM controls are retained beside the canonical artifact. K15 C64 uses the separate 32768-context, gpu_memory_utilization=0.815 high-concurrency profile.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
