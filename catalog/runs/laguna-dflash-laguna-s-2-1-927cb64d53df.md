# `laguna-dflash/dflash-k7/depth-65536x256-c1`

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
| Objective | context_depth |
| TPS kind | aggregate_output |
| Layout | TP=4 |
| Context | 131456 |
| Concurrency | 1 |
| Prompt tokens | 65536 |
| Generated tokens | 256 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 6.128166479236682 |
| `decode_tok_s` | 52.950891566607865 |
| `prefill_tok_s` | 1791.9409125271939 |
| `total_tok_s` | 1575.9441874768268 |
| `req_s` | 0.023938150309518288 |
| `ttft_p50_ms` | 36957.85461599007 |
| `ttft_p99_ms` | 36957.85461599007 |
| `itl_p50_ms` | 29.332629987038672 |
| `tpot_p50_ms` | 18.885423274546422 |
| `e2e_p99_ms` | 41773.63755099941 |
| `vram_peak_mib` | 96448 |
| `avg_power_w` | 793.1294444444444 |
| `max_temp_c` | 74.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-INT4' --trust-remote-code --tensor-parallel-size 4 --max-model-len 131456 --gpu-memory-utilization 0.85 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 0.0.0.0 --port 8001 --no-enable-log-requests --speculative-config '{"model":"${MODEL_ROOT_ALT}/Laguna-S-2.1-DFlash-INT4","num_speculative_tokens":7,"method":"dflash"}'
```

## Speculative decoding

```json
{
  "acceptance": 0.076592082616179,
  "accepted_tokens_per_round": 0.536144578313253,
  "draft_path": "${MODEL_ROOT_ALT}/Laguna-S-2.1-DFlash-INT4",
  "draft_ref": "Laguna-S-2.1-DFlash-INT4",
  "k": 7,
  "method": "dflash"
}
```

## Engine knobs

```json
{
  "label": "depth-65536x256-c1",
  "num_prompts": 1,
  "output_tok_per_watt": 0.007726565344613095,
  "prefix_hit_rate": 0.00024398426301503552,
  "throttle_sample_count": 172
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-22/laguna-s-2.1-dflash-4x3090/dflash-k7/depth-65536x256-c1.json`

## Notes

Identical seeds and workload labels. Target profile: 262144 context at gpu_memory_utilization=0.95. DFlash speed profile: 131456 context at gpu_memory_utilization=0.85 (K7) or 0.833 (K15); full262 runtime-OOM controls are retained beside the canonical artifact. K15 C64 uses the separate 32768-context, gpu_memory_utilization=0.815 high-concurrency profile.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
