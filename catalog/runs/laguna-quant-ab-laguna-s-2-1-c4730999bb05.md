# `laguna-quant-ab/new-w4a16/medium-4096x256-c32`

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
| Concurrency | 32 |
| Prompt tokens | 4096 |
| Generated tokens | 256 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 102.60524042297327 |
| `decode_tok_s` | 4.331100943619579 |
| `prefill_tok_s` | 985.4085248676982 |
| `total_tok_s` | 1758.2482596089299 |
| `req_s` | 0.4008017204022393 |
| `ttft_p50_ms` | 5351.771394954994 |
| `ttft_p99_ms` | 66998.97432590369 |
| `itl_p50_ms` | 53.50167443975806 |
| `tpot_p50_ms` | 287.0158061449069 |
| `e2e_p99_ms` | 140538.70973398443 |
| `vram_peak_mib` | 95184 |
| `avg_power_w` | 846.6013294797688 |
| `max_temp_c` | 75.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/vllm-env-025/bin/vllm' serve '${MODEL_ROOT_ALT}/Laguna-S-2.1-W4A16' --trust-remote-code --tensor-parallel-size 4 --max-model-len 262144 --gpu-memory-utilization 0.95 --max-num-seqs 64 --max-cudagraph-capture-size 64 --kv-cache-dtype fp8 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser poolside_v1 --reasoning-parser poolside_v1 --served-model-name laguna default --default-chat-template-kwargs '{"enable_thinking":true}' --host 127.0.0.1 --port 18025 --no-enable-log-requests
```

## Engine knobs

```json
{
  "label": "medium-4096x256-c32",
  "num_prompts": 64,
  "output_tok_per_watt": 0.12119664457180046,
  "prefix_hit_rate": 0.007746630707371782,
  "throttle_sample_count": 637
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-25/laguna-s21-w4a16-vs-official-int4-4x3090/new-w4a16/medium-4096x256-c32.json`

## Notes

Fresh same-runtime A/B with identical seeds, workloads, TP4, FP8 KV, CUDA-graph and prefix-cache settings. Synthetic speed point; fixed-content results remain in the raw artifact.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
