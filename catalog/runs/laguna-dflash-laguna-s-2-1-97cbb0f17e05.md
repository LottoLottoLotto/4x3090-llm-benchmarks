# `laguna-dflash/dflash-k15/short-512x256-c8`

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
| Concurrency | 8 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 140.69457796439357 |
| `decode_tok_s` | 19.92619729643297 |
| `prefill_tok_s` | 737.015006546934 |
| `total_tok_s` | 441.8345596572252 |
| `req_s` | 0.5495881951734124 |
| `ttft_p50_ms` | 611.5551224793307 |
| `ttft_p99_ms` | 2516.052149520256 |
| `itl_p50_ms` | 116.49406107608229 |
| `tpot_p50_ms` | 50.760600982489535 |
| `e2e_p99_ms` | 20063.284937007124 |
| `vram_peak_mib` | 92160 |
| `avg_power_w` | 816.9558208955224 |
| `max_temp_c` | 75.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-INT4' --trust-remote-code --tensor-parallel-size 4 --max-model-len 131456 --gpu-memory-utilization 0.833 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 0.0.0.0 --port 8001 --no-enable-log-requests --speculative-config '{"model":"${MODEL_ROOT_ALT}/Laguna-S-2.1-DFlash-INT4","num_speculative_tokens":15,"method":"dflash"}'
```

## Speculative decoding

```json
{
  "acceptance": 0.1040098704503393,
  "accepted_tokens_per_round": 1.5601480567550894,
  "draft_path": "${MODEL_ROOT_ALT}/Laguna-S-2.1-DFlash-INT4",
  "draft_ref": "Laguna-S-2.1-DFlash-INT4",
  "k": 15,
  "method": "dflash"
}
```

## Engine knobs

```json
{
  "label": "short-512x256-c8",
  "num_prompts": 32,
  "output_tok_per_watt": 0.17221809841585853,
  "prefix_hit_rate": 0.029200410630774495,
  "throttle_sample_count": 232
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-22/laguna-s-2.1-dflash-4x3090/dflash-k15/short-512x256-c8.json`

## Notes

Identical seeds and workload labels. Target profile: 262144 context at gpu_memory_utilization=0.95. DFlash speed profile: 131456 context at gpu_memory_utilization=0.85 (K7) or 0.833 (K15); full262 runtime-OOM controls are retained beside the canonical artifact. K15 C64 uses the separate 32768-context, gpu_memory_utilization=0.815 high-concurrency profile.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
