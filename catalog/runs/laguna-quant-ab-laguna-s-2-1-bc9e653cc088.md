# `laguna-quant-ab/official-int4/short-512x256-c16`

| field | value |
|---|---|
| Date | 2026-07-25 |
| Campaign | laguna-quant-ab |
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
| Concurrency | 16 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 333.1777621218571 |
| `decode_tok_s` | 25.228988012140885 |
| `prefill_tok_s` | 330.93505078959913 |
| `total_tok_s` | 1044.0681556921622 |
| `req_s` | 1.3014756332885042 |
| `ttft_p50_ms` | 2144.0673120087013 |
| `ttft_p99_ms` | 4353.301867956761 |
| `itl_p50_ms` | 32.011364004574716 |
| `tpot_p50_ms` | 39.28882892371392 |
| `e2e_p99_ms` | 13519.647466377355 |
| `vram_peak_mib` | 96058 |
| `avg_power_w` | 809.1561016949153 |
| `max_temp_c` | 74.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-INT4' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 127.0.0.1 --port 18025 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "short-512x256-c16",
  "num_prompts": 64,
  "output_tok_per_watt": 0.4117595621215233,
  "prefix_hit_rate": 0.07323073402368556,
  "throttle_sample_count": 187
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-25/laguna-s21-w4a16-vs-official-int4-4x3090/official-int4/short-512x256-c16.json`

## Notes

Fresh same-runtime A/B with identical seeds, workloads, TP4, FP8 KV, CUDA-graph and prefix-cache settings. Synthetic speed point; fixed-content results remain in the raw artifact.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
