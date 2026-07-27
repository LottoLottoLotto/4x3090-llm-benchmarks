# `kvsweep/Qwen3.6-27B-FP8/c131072/auto`

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
| Context | 131072 |
| Concurrency | 1 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 1.62 |
| `decode_tok_s` | 49.8 |
| `prefill_tok_s` | 858.0 |
| `ttft_p50_ms` | 152457.4 |
| `itl_p50_ms` | 20.53 |

## Launch command

```bash
vllm serve <Qwen3.6-27B-FP8 weights> --tensor-parallel-size 4 --max-model-len 131072 --kv-cache-dtype auto --served-model-name bench  # kv_cache_summarize.py driver
```

## Provenance

- `repo:llm-bench/results/kv-cache-sweep-2026-06-28`
- `rig:~/benchmarks/kv-cache-sweep-2026-06-28`

## Notes

KV-dtype sweep. peak_out 1.62@c1. vLLM 0.23.0, tp=4, max_model_len=131072.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
