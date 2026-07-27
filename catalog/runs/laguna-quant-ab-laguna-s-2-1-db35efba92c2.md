# `laguna-quant-ab/new-w4a16/generation-512x1024-c1`

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
| `output_tok_s` | 96.34289337631263 |
| `decode_tok_s` | 99.15670367679218 |
| `prefill_tok_s` | 1681.8556633954418 |
| `total_tok_s` | 146.46660084333465 |
| `req_s` | 0.0940848568128053 |
| `ttft_p50_ms` | 319.48635552544147 |
| `ttft_p99_ms` | 323.39720288058743 |
| `itl_p50_ms` | 10.085502173751593 |
| `tpot_p50_ms` | 10.087708990614885 |
| `e2e_p99_ms` | 10643.46752900863 |
| `vram_peak_mib` | 95184 |
| `avg_power_w` | 808.6056603773585 |
| `max_temp_c` | 72.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-W4A16' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 127.0.0.1 --port 18025 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "generation-512x1024-c1",
  "num_prompts": 4,
  "output_tok_per_watt": 0.11914694405101187,
  "prefix_hit_rate": 0.06006569685593618,
  "throttle_sample_count": 169
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-25/laguna-s21-w4a16-vs-official-int4-4x3090/new-w4a16/generation-512x1024-c1.json`

## Notes

Fresh same-runtime A/B with identical seeds, workloads, TP4, FP8 KV, CUDA-graph and prefix-cache settings. Synthetic speed point; fixed-content results remain in the raw artifact.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
