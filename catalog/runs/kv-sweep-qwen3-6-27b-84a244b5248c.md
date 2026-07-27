# `kvsweep/Qwen3.6-27B-FP8/c1024/turboquant_k3v4_nc`

| field | value |
|---|---|
| Date | 2026-06-28 |
| Campaign | kv-sweep |
| Model | Qwen3.6-27B |
| Checkpoint | Qwen3.6-27B-FP8 |
| Quant | fp8-static |
| Quant method | fp8 |
| Engine | vllm |
| Engine version | 0.23.0 |
| Objective | kv_dtype_sweep |
| TPS kind | unknown |
| Layout | TP=4 |
| Context | 1024 |
| Concurrency | 1 |
| KV cache | turboquant_k3v4_nc |
| Power limit | 220 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 100.26 |
| `decode_tok_s` | 60.4 |
| `prefill_tok_s` | 1000.1 |
| `ttft_p50_ms` | 895.9 |
| `itl_p50_ms` | 16.56 |

## Launch command

```bash
vllm serve <Qwen3.6-27B-FP8 weights> --tensor-parallel-size 4 --max-model-len 131072 --kv-cache-dtype turboquant_k3v4_nc --served-model-name bench  # kv_cache_summarize.py driver
```

## Provenance

- `repo:llm-bench/results/kv-cache-sweep-2026-06-28`
- `rig:~/benchmarks/kv-cache-sweep-2026-06-28`

## Notes

KV-dtype sweep. peak_out 100.26@c16. vLLM 0.23.0, tp=4, max_model_len=131072.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
