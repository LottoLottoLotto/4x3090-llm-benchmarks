# `laguna-quant-ab/new-w4a16/medium-4096x256-c8`

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
| Concurrency | 8 |
| Prompt tokens | 4096 |
| Generated tokens | 256 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 90.40344234715577 |
| `decode_tok_s` | 17.561777379507916 |
| `prefill_tok_s` | 1035.6020770750463 |
| `total_tok_s` | 1551.7124058146453 |
| `req_s` | 0.35313844666857724 |
| `ttft_p50_ms` | 6320.044904947281 |
| `ttft_p99_ms` | 16797.16437694151 |
| `itl_p50_ms` | 22.743707988411188 |
| `tpot_p50_ms` | 63.17425451204911 |
| `e2e_p99_ms` | 33747.58140016347 |
| `vram_peak_mib` | 95184 |
| `avg_power_w` | 808.6541818181819 |
| `max_temp_c` | 74.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-W4A16' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 127.0.0.1 --port 18025 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "medium-4096x256-c8",
  "num_prompts": 16,
  "output_tok_per_watt": 0.11179493580790277,
  "prefix_hit_rate": 0.007733087646694558,
  "throttle_sample_count": 179
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-25/laguna-s21-w4a16-vs-official-int4-4x3090/new-w4a16/medium-4096x256-c8.json`

## Notes

Fresh same-runtime A/B with identical seeds, workloads, TP4, FP8 KV, CUDA-graph and prefix-cache settings. Synthetic speed point; fixed-content results remain in the raw artifact.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
