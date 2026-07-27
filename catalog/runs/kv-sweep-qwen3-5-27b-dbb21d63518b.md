# `kvsweep/Qwen3.5-27B-AWQ-4bit/c8192/fp8`

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
| Context | 8192 |
| Concurrency | 1 |
| KV cache | fp8 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 26.93 |
| `decode_tok_s` | 79.2 |
| `prefill_tok_s` | 962.3 |
| `ttft_p50_ms` | 8246.9 |
| `itl_p50_ms` | 12.63 |

## Launch command

```bash
vllm serve <Qwen3.5-27B-AWQ-4bit weights> --tensor-parallel-size 4 --max-model-len 131072 --kv-cache-dtype fp8 --served-model-name bench  # kv_cache_summarize.py driver
```

## Provenance

- `repo:llm-bench/results/kv-cache-sweep-2026-06-28`
- `rig:~/benchmarks/kv-cache-sweep-2026-06-28`

## Notes

KV-dtype sweep. peak_out 26.93@c4. vLLM 0.23.0, tp=4, max_model_len=131072.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
