# `laguna-quant-ab/new-w4a16/depth-32768x256-c1`

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
| Objective | context_depth |
| TPS kind | aggregate_output |
| Layout | TP=4 |
| Context | 262144 |
| Concurrency | 1 |
| Prompt tokens | 32768 |
| Generated tokens | 256 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 12.5868931770682 |
| `decode_tok_s` | 97.86742096606345 |
| `prefill_tok_s` | 1871.3579965469328 |
| `total_tok_s` | 1625.7742570036608 |
| `req_s` | 0.049167551472922656 |
| `ttft_p50_ms` | 17732.33319609426 |
| `ttft_p99_ms` | 17732.33319609426 |
| `itl_p50_ms` | 10.408630478195846 |
| `tpot_p50_ms` | 10.217904897552787 |
| `e2e_p99_ms` | 20337.89894497022 |
| `vram_peak_mib` | 95184 |
| `avg_power_w` | 752.1209375 |
| `max_temp_c` | 72.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-W4A16' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 127.0.0.1 --port 18025 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "depth-32768x256-c1",
  "num_prompts": 1,
  "output_tok_per_watt": 0.01673519848936289,
  "prefix_hit_rate": 0.000975312404754648,
  "throttle_sample_count": 84
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-25/laguna-s21-w4a16-vs-official-int4-4x3090/new-w4a16/depth-32768x256-c1.json`

## Notes

Fresh same-runtime A/B with identical seeds, workloads, TP4, FP8 KV, CUDA-graph and prefix-cache settings. Synthetic speed point; fixed-content results remain in the raw artifact.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
