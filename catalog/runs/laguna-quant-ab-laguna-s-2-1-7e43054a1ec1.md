# `laguna-quant-ab/new-w4a16/short-512x256-c48`

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
| Objective | concurrency_sweep |
| TPS kind | aggregate_output |
| Layout | TP=4 |
| Context | 262144 |
| Concurrency | 48 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 476.4600714123619 |
| `decode_tok_s` | 11.741154780626895 |
| `prefill_tok_s` | 243.8727135087771 |
| `total_tok_s` | 1499.3874293196882 |
| `req_s` | 1.8611721539545387 |
| `ttft_p50_ms` | 3132.573981070891 |
| `ttft_p99_ms` | 12876.175705986097 |
| `itl_p50_ms` | 51.9418534822762 |
| `tpot_p50_ms` | 87.7531043879286 |
| `e2e_p99_ms` | 35118.53930908488 |
| `vram_peak_mib` | 95184 |
| `avg_power_w` | 838.9800869565217 |
| `max_temp_c` | 74.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-W4A16' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 127.0.0.1 --port 18025 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "short-512x256-c48",
  "num_prompts": 192,
  "output_tok_per_watt": 0.5679039095442242,
  "prefix_hit_rate": 0.058222618122547996,
  "throttle_sample_count": 412
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-25/laguna-s21-w4a16-vs-official-int4-4x3090/new-w4a16/short-512x256-c48.json`

## Notes

Fresh same-runtime A/B with identical seeds, workloads, TP4, FP8 KV, CUDA-graph and prefix-cache settings. Synthetic speed point; fixed-content results remain in the raw artifact.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
