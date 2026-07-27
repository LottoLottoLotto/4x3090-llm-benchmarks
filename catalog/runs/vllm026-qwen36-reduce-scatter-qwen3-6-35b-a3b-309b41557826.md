# `vllm026-rs/qwen36-35b-autoround/v026_c16`

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
| Concurrency | 16 |
| Prompt tokens | 1024 |
| Generated tokens | 128 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 399.68 |
| `total_tok_s` | 3597.09 |
| `req_s` | 3.1225 |
| `ttft_p50_ms` | 1892.47 |
| `tpot_p50_ms` | 25.78 |
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
    398.2473810262825,
    378.1590993023907,
    403.42146754421634,
    375.77317101510437,
    399.2145324194774,
    400.98949954406044,
    400.13851424296837,
    438.3931212461613,
    370.8197641429181,
    404.89770006469206
  ],
  "output_tok_s_max": 438.3931212461613,
  "output_tok_s_min": 370.8197641429181,
  "repeats": 10
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-26/vllm026-qwen36-attn-reduce-scatter-ep`

## Notes

Matched vLLM 0.25 vs 0.26 DP2xTP2 EP A/B. Fixed random 1024 input + 128 output, per-concurrency discard warmup, 5 repeats at c1/c4 and 10 at c8/c16. Zero failed requests. v0.26 Qwen3.5/3.6 attention reduce-scatter gate active via AgRs all2all, EP, DP>1 and TP>1. Acceptance >=10% not met.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
