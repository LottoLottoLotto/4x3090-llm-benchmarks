# `laguna-quant-ab/new-w4a16/depth-261760x256-c1`

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
| Prompt tokens | 261760 |
| Generated tokens | 256 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 1.3233033077292569 |
| `decode_tok_s` | 86.17567133272918 |
| `prefill_tok_s` | 1385.818438538519 |
| `total_tok_s` | 1354.618039909819 |
| `req_s` | 0.00516915354581741 |
| `ttft_p50_ms` | 190495.58645300567 |
| `ttft_p99_ms` | 190495.58645300567 |
| `itl_p50_ms` | 12.645764974877238 |
| `tpot_p50_ms` | 11.604203187915333 |
| `e2e_p99_ms` | 193454.65826592408 |
| `vram_peak_mib` | 95184 |
| `avg_power_w` | 839.1796601941749 |
| `max_temp_c` | 75.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-W4A16' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 127.0.0.1 --port 18025 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "depth-261760x256-c1",
  "num_prompts": 1,
  "output_tok_per_watt": 0.0015769010743457038,
  "prefix_hit_rate": 0.0,
  "throttle_sample_count": 768
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-25/laguna-s21-w4a16-vs-official-int4-4x3090/new-w4a16/depth-261760x256-c1.json`

## Notes

Fresh same-runtime A/B with identical seeds, workloads, TP4, FP8 KV, CUDA-graph and prefix-cache settings. Synthetic speed point; fixed-content results remain in the raw artifact.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
