# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q4_K_M_tp2x1_spec-none_c32768_pl220_aggregate`

| field | value |
|---|---|
| Date | 2026-06-21 |
| Campaign | orchestrator |
| Model | Gemma-4-12B-it |
| Checkpoint | gemma-4-12b-it-Q4_K_M.gguf |
| Quant | gguf-q4_k_m |
| Quant method | gguf |
| Engine | llama.cpp |
| Engine version | f3e182816 |
| Objective | aggregate |
| TPS kind | aggregate_output |
| Layout | TP=2 |
| Context | 32768 |
| Concurrency | 16 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 171.5 |
| `req_s` | 0.67 |
| `ttft_p50_ms` | 11811.76 |
| `ttft_p99_ms` | 13230.48 |
| `itl_p50_ms` | 44.41 |
| `e2e_p99_ms` | 24591.38 |
| `vram_peak_mib` | 24448 |
| `avg_power_w` | 466.2 |
| `max_temp_c` | 70.0 |

## Launch command

```bash
'${ENGINE_ROOT}/llama.cpp/build/bin/llama-server' -m '${MODEL_ROOT}/gemma-4-12b-it-GGUF/gemma-4-12b-it-Q4_K_M.gguf' --host 127.0.0.1 --port 18000 -ngl 99 -c 32768 -np 8 -b 2048 -ub 512 -sm layer -rea off -fa on
```

## Engine knobs

```json
{
  "batch": 2048,
  "flash_attn": true,
  "n_parallel": 8,
  "ngl": 99,
  "split_mode": "layer",
  "ubatch": 512
}
```

## Throughput curve

```json
[
  {
    "concurrency": 1,
    "e2e_p99": 3534.99,
    "errors": 0,
    "itl_p50": 12.76,
    "output_tok_s": 76.4,
    "req_s": 0.3,
    "ttft_p50": 57.24,
    "ttft_p99": 283.31
  },
  {
    "concurrency": 2,
    "e2e_p99": 4447.33,
    "errors": 0,
    "itl_p50": 15.81,
    "output_tok_s": 119.2,
    "req_s": 0.47,
    "ttft_p50": 282.51,
    "ttft_p99": 401.15
  },
  {
    "concurrency": 4,
    "e2e_p99": 7305.59,
    "errors": 0,
    "itl_p50": 26.03,
    "output_tok_s": 145.7,
    "req_s": 0.57,
    "ttft_p50": 249.94,
    "ttft_p99": 609.08
  },
  {
    "concurrency": 8,
    "e2e_p99": 12524.01,
    "errors": 0,
    "itl_p50": 44.39,
    "output_tok_s": 169.4,
    "req_s": 0.66,
    "ttft_p50": 718.94,
    "ttft_p99": 1166.83
  },
  {
    "concurrency": 16,
    "e2e_p99": 24591.38,
    "errors": 0,
    "itl_p50": 44.41,
    "output_tok_s": 171.5,
    "req_s": 0.67,
    "ttft_p50": 11811.76,
    "ttft_p99": 13230.48
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
