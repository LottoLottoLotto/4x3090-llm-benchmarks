# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q4_K_M_tp4x1_spec-none_c32768_pl300_aggregate`

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
| Layout | TP=4 |
| Context | 32768 |
| Concurrency | 16 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| Power limit | 300 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 197.3 |
| `req_s` | 0.77 |
| `ttft_p50_ms` | 10610.72 |
| `ttft_p99_ms` | 10637.83 |
| `itl_p50_ms` | 39.7 |
| `e2e_p99_ms` | 20796.19 |
| `vram_peak_mib` | 13976 |
| `avg_power_w` | 739.6 |
| `max_temp_c` | 73.0 |

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
    "e2e_p99": 3431.34,
    "errors": 0,
    "itl_p50": 12.47,
    "output_tok_s": 78.4,
    "req_s": 0.31,
    "ttft_p50": 59.68,
    "ttft_p99": 252.13
  },
  {
    "concurrency": 2,
    "e2e_p99": 4187.62,
    "errors": 0,
    "itl_p50": 15.02,
    "output_tok_s": 126.3,
    "req_s": 0.49,
    "ttft_p50": 225.96,
    "ttft_p99": 345.02
  },
  {
    "concurrency": 4,
    "e2e_p99": 7050.11,
    "errors": 0,
    "itl_p50": 24.3,
    "output_tok_s": 154.7,
    "req_s": 0.6,
    "ttft_p50": 250.36,
    "ttft_p99": 825.49
  },
  {
    "concurrency": 8,
    "e2e_p99": 11767.08,
    "errors": 0,
    "itl_p50": 39.62,
    "output_tok_s": 185.0,
    "req_s": 0.72,
    "ttft_p50": 703.18,
    "ttft_p99": 1625.39
  },
  {
    "concurrency": 16,
    "e2e_p99": 20796.19,
    "errors": 0,
    "itl_p50": 39.7,
    "output_tok_s": 197.3,
    "req_s": 0.77,
    "ttft_p50": 10610.72,
    "ttft_p99": 10637.83
  },
  {
    "concurrency": 32,
    "e2e_p99": 41791.64,
    "errors": 0,
    "itl_p50": 39.87,
    "output_tok_s": 196.4,
    "req_s": 0.77,
    "ttft_p50": 31481.9,
    "ttft_p99": 31562.71
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
