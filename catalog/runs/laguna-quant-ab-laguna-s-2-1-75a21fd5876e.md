# `laguna-quant-ab/new-w4a16/prefix-warm-32768x64`

| field | value |
|---|---|
| Date | 2026-07-25 |
| Campaign | laguna-quant-ab |
| Model | Laguna-S-2.1 |
| Checkpoint | Relativ3pa1n/Laguna-S-2.1-W4A16 |
| Quant | compressed-tensors-w4a16-g32-asym-rtn |
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
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 74.42283722783252 |
| `decode_tok_s` | 103.69164557436612 |
| `prefill_tok_s` | 209.35776965428784 |
| `total_tok_s` | 38227.75548480885 |
| `req_s` | 1.162856831684883 |
| `ttft_p50_ms` | 251.75202102400362 |
| `ttft_p99_ms` | 251.75202102400362 |
| `itl_p50_ms` | 10.30832901597023 |
| `tpot_p50_ms` | 9.643978494707317 |
| `e2e_p99_ms` | 859.3226661905646 |
| `vram_peak_mib` | 95184 |
| `avg_power_w` | 554.67 |
| `max_temp_c` | 69.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-W4A16' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 127.0.0.1 --port 18025 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "prefix-warm-32768x64",
  "num_prompts": 1,
  "output_tok_per_watt": 0.13417498193129704,
  "prefix_hit_rate": 0.9996952148735142,
  "throttle_sample_count": 4
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-25/laguna-s21-w4a16-vs-official-int4-4x3090/new-w4a16/prefix-warm-32768x64.json`

## Notes

Fresh same-runtime A/B with identical seeds, workloads, TP4, FP8 KV, CUDA-graph and prefix-cache settings. Synthetic speed point; fixed-content results remain in the raw artifact.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
