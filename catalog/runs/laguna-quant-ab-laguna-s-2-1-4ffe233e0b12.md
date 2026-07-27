# `laguna-quant-ab/official-int4/generation-512x1024-c1`

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
| Objective | generation_length |
| TPS kind | aggregate_output |
| Layout | TP=4 |
| Context | 262144 |
| Concurrency | 1 |
| Prompt tokens | 512 |
| Generated tokens | 1024 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 95.4682589930368 |
| `decode_tok_s` | 98.19559511715121 |
| `prefill_tok_s` | 1703.3908825358196 |
| `total_tok_s` | 145.13692596426762 |
| `req_s` | 0.0932307216728875 |
| `ttft_p50_ms` | 315.37565565668046 |
| `ttft_p99_ms` | 318.1008560815826 |
| `itl_p50_ms` | 10.183310019783676 |
| `tpot_p50_ms` | 10.18577471263033 |
| `e2e_p99_ms` | 10739.94388496736 |
| `vram_peak_mib` | 96168 |
| `avg_power_w` | 808.9125925925925 |
| `max_temp_c` | 72.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-INT4' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 127.0.0.1 --port 18025 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "generation-512x1024-c1",
  "num_prompts": 4,
  "output_tok_per_watt": 0.1180204880814845,
  "prefix_hit_rate": 0.06006569685593618,
  "throttle_sample_count": 175
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-25/laguna-s21-w4a16-vs-official-int4-4x3090/official-int4/generation-512x1024-c1.json`

## Notes

Fresh same-runtime A/B with identical seeds, workloads, TP4, FP8 KV, CUDA-graph and prefix-cache settings. Synthetic speed point; fixed-content results remain in the raw artifact.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
