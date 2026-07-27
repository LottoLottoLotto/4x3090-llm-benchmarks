# `laguna-quant-ab/official-int4/depth-32768x256-c1`

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
| `output_tok_s` | 12.639529393665185 |
| `decode_tok_s` | 97.0509118453395 |
| `prefill_tok_s` | 1881.527678695131 |
| `total_tok_s` | 1632.5729645739573 |
| `req_s` | 0.04937316169400463 |
| `ttft_p50_ms` | 17625.79628895037 |
| `ttft_p99_ms` | 17625.79628895037 |
| `itl_p50_ms` | 10.485271108336747 |
| `tpot_p50_ms` | 10.303870216012001 |
| `e2e_p99_ms` | 20253.28319403343 |
| `vram_peak_mib` | 96168 |
| `avg_power_w` | 751.8175 |
| `max_temp_c` | 72.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-INT4' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 127.0.0.1 --port 18025 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "depth-32768x256-c1",
  "num_prompts": 1,
  "output_tok_per_watt": 0.016811964863368018,
  "prefix_hit_rate": 0.000975312404754648,
  "throttle_sample_count": 79
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-25/laguna-s21-w4a16-vs-official-int4-4x3090/official-int4/depth-32768x256-c1.json`

## Notes

Fresh same-runtime A/B with identical seeds, workloads, TP4, FP8 KV, CUDA-graph and prefix-cache settings. Synthetic speed point; fixed-content results remain in the raw artifact.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
