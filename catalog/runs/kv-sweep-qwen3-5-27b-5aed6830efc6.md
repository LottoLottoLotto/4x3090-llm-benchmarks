# `kvsweep/Qwen3.5-27B-AWQ-4bit/c32768/bfloat16`

| field | value |
|---|---|
| Date | 2026-06-28 |
| Campaign | kv-sweep |
| Model | Qwen3.5-27B |
| Checkpoint | Qwen3.5-27B-AWQ-4bit |
| Quant | awq-int4 |
| Quant method | awq |
| Engine | vllm |
| Engine version | 0.23.0 |
| Objective | kv_dtype_sweep |
| TPS kind | unknown |
| Layout | TP=4 |
| Context | 32768 |
| Concurrency | 1 |
| KV cache | bfloat16 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 7.06 |
| `decode_tok_s` | 71.6 |
| `prefill_tok_s` | 936.1 |
| `ttft_p50_ms` | 34731.9 |
| `itl_p50_ms` | 14.08 |

## Launch command

```bash
vllm serve <Qwen3.5-27B-AWQ-4bit weights> --tensor-parallel-size 4 --max-model-len 131072 --kv-cache-dtype bfloat16 --served-model-name bench  # kv_cache_summarize.py driver
```

## Provenance

- `repo:llm-bench/results/kv-cache-sweep-2026-06-28`
- `rig:~/benchmarks/kv-cache-sweep-2026-06-28`

## Notes

KV-dtype sweep. peak_out 7.06@c4. vLLM 0.23.0, tp=4, max_model_len=131072.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
