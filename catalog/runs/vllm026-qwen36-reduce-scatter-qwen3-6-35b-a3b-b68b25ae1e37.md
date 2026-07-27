# `vllm026-rs/qwen36-35b-autoround/v026_c1`

| field | value |
|---|---|
| Date | 2026-07-26 |
| Campaign | vllm026-qwen36-reduce-scatter |
| Model | Qwen3.6-35B-A3B |
| Checkpoint | qwen3.6-35b-a3b-autoround-int4 |
| Quant | autoround-int4 |
| Quant method | autoround |
| Engine | vllm |
| Engine version | 0.26.0 |
| Objective | aggregate |
| TPS kind | aggregate_output |
| Layout | TP=2, DP=2 |
| Context | 16384 |
| Concurrency | 1 |
| Prompt tokens | 1024 |
| Generated tokens | 128 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 83.6 |
| `total_tok_s` | 752.4 |
| `req_s` | 0.6531 |
| `ttft_p50_ms` | 264.49 |
| `tpot_p50_ms` | 9.95 |
| `vram_peak_mib` | 21320 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env-026/bin/python' -m vllm.entrypoints.cli.main serve '${MODEL_ROOT}/qwen3.6-35b-a3b-autoround-int4' --host 127.0.0.1 --port 18126 --served-model-name bench --tensor-parallel-size 2 --data-parallel-size 2 --enable-expert-parallel --all2all-backend allgather_reducescatter --max-model-len 16384 --max-num-seqs 64 --gpu-memory-utilization 0.90 --disable-custom-all-reduce --no-enable-prefix-caching
```

## Engine knobs

```json
{
  "all2all_backend": "allgather_reducescatter",
  "client_version": "0.26.0",
  "custom_all_reduce": false,
  "data_parallel_size": 2,
  "expert_parallel": true,
  "gpu_memory_utilization": 0.9,
  "prefix_caching": false
}
```

## Samples

```json
{
  "output_tok_s_all": [
    83.99785094775696,
    83.600065485995,
    83.40405653283061,
    83.45694076469528,
    83.61081666292117
  ],
  "output_tok_s_max": 83.99785094775696,
  "output_tok_s_min": 83.40405653283061,
  "repeats": 5
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-26/vllm026-qwen36-attn-reduce-scatter-ep`

## Notes

Matched vLLM 0.25 vs 0.26 DP2xTP2 EP A/B. Fixed random 1024 input + 128 output, per-concurrency discard warmup, 5 repeats at c1/c4 and 10 at c8/c16. Zero failed requests. v0.26 Qwen3.5/3.6 attention reduce-scatter gate active via AgRs all2all, EP, DP>1 and TP>1. Acceptance >=10% not met.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
