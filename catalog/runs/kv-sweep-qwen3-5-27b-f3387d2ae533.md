# `kvsweep/Qwen3.5-27B-AWQ-4bit/c1024/turboquant_4bit_nc`

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
| Context | 1024 |
| Concurrency | 1 |
| KV cache | turboquant_4bit_nc |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 73.55 |
| `decode_tok_s` | 77.7 |
| `prefill_tok_s` | 979.2 |
| `ttft_p50_ms` | 915.1 |
| `itl_p50_ms` | 12.88 |

## Launch command

```bash
vllm serve <Qwen3.5-27B-AWQ-4bit weights> --tensor-parallel-size 4 --max-model-len 131072 --kv-cache-dtype turboquant_4bit_nc --served-model-name bench  # kv_cache_summarize.py driver
```

## Provenance

- `repo:llm-bench/results/kv-cache-sweep-2026-06-28`
- `rig:~/benchmarks/kv-cache-sweep-2026-06-28`

## Notes

KV-dtype sweep. peak_out 73.55@c4. vLLM 0.23.0, tp=4, max_model_len=131072.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
