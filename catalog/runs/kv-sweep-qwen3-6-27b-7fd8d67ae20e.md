# `kvsweep/Qwen3.6-27B-FP8/c65536/fp8`

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
| Context | 65536 |
| Concurrency | 1 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 3.48 |
| `decode_tok_s` | 59.8 |
| `prefill_tok_s` | 904.1 |
| `ttft_p50_ms` | 72201.4 |
| `itl_p50_ms` | 16.99 |

## Launch command

```bash
vllm serve <Qwen3.6-27B-FP8 weights> --tensor-parallel-size 4 --max-model-len 131072 --kv-cache-dtype fp8 --served-model-name bench  # kv_cache_summarize.py driver
```

## Provenance

- `repo:llm-bench/results/kv-cache-sweep-2026-06-28`
- `rig:~/benchmarks/kv-cache-sweep-2026-06-28`

## Notes

KV-dtype sweep. peak_out 3.48@c4. vLLM 0.23.0, tp=4, max_model_len=131072.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
