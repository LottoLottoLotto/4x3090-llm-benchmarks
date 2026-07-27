# `laguna-quant-ab/official-int4/depth-65536x256-c1`

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
| Prompt tokens | 65536 |
| Generated tokens | 256 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 6.520114666156201 |
| `decode_tok_s` | 95.29618053250832 |
| `prefill_tok_s` | 1809.4883726407684 |
| `total_tok_s` | 1676.73917551456 |
| `req_s` | 0.02546919791467266 |
| `ttft_p50_ms` | 36586.62122208625 |
| `ttft_p99_ms` | 36586.62122208625 |
| `itl_p50_ms` | 10.786448954604566 |
| `tpot_p50_ms` | 10.493599999622973 |
| `e2e_p99_ms` | 39262.48922199011 |
| `vram_peak_mib` | 96168 |
| `avg_power_w` | 783.4590196078432 |
| `max_temp_c` | 73.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-INT4' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 127.0.0.1 --port 18025 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "depth-65536x256-c1",
  "num_prompts": 1,
  "output_tok_per_watt": 0.008322215333508846,
  "prefix_hit_rate": 0.00048796852603007104,
  "throttle_sample_count": 154
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-25/laguna-s21-w4a16-vs-official-int4-4x3090/official-int4/depth-65536x256-c1.json`

## Notes

Fresh same-runtime A/B with identical seeds, workloads, TP4, FP8 KV, CUDA-graph and prefix-cache settings. Synthetic speed point; fixed-content results remain in the raw artifact.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
