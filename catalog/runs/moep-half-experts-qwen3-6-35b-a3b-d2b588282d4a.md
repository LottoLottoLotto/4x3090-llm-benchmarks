# `moep-half-experts/reap50-q4/pp512`

| field | value |
|---|---|
| Date | 2026-07-22 |
| Campaign | moep-half-experts |
| Model | Qwen3.6-35B-A3B |
| Checkpoint | reap50-q4 |
| Quant | gguf-q4_k_m-reap50 |
| Quant method | gguf |
| Engine | llama.cpp |
| Engine version | 9cde3321 |
| Objective | prefill |
| Layout | TP=1 |
| Prompt tokens | 512 |
| Generated tokens | 0 |
| KV cache | f16 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `prefill_tok_s` | 2946.815109 |
| `vram_peak_mib` | 11452 |
| `max_temp_c` | 66.0 |

## Launch command

```bash
llama-bench -m ${MODEL_ROOT}/Qwen3.6-35B-A3B-coding-reap50-GGUF/qwen36-reap50-Q4_K_M-imat.gguf -ngl 999 -fa on -p 512 -n 256 -r 5 -o json
```

## Engine knobs

```json
{
  "repetitions": 5,
  "stddev_tok_s": 284.161735
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-22/moep-half-experts-code/reap50-q4/systems/llama-bench.json`

## Notes

Clean sequential single-GPU run; llama-bench pp512 average of 5 samples.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
