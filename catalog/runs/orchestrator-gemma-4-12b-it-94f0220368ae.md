# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q4_K_M_tp4x1_spec-none_c32768_pl270_aggregate`

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
| Concurrency | 32 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| Power limit | 270 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 196.0 |
| `req_s` | 0.77 |
| `ttft_p50_ms` | 31432.37 |
| `ttft_p99_ms` | 31734.05 |
| `itl_p50_ms` | 39.83 |
| `e2e_p99_ms` | 41928.24 |
| `vram_peak_mib` | 13976 |
| `avg_power_w` | 733.7 |
| `max_temp_c` | 72.0 |

## Launch command

```bash
'${ENGINE_ROOT}/llama.cpp/build/bin/llama-server' -m '${MODEL_ROOT}/gemma-4-12b-it-GGUF/gemma-4-12b-it-Q4_K_M.gguf' --host 127.0.0.1 --port 18001 -ngl 99 -c 32768 -np 8 -b 2048 -ub 512 -sm layer -rea off -fa on
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
    "e2e_p99": 3438.87,
    "errors": 0,
    "itl_p50": 12.46,
    "output_tok_s": 78.4,
    "req_s": 0.31,
    "ttft_p50": 60.19,
    "ttft_p99": 259.96
  },
  {
    "concurrency": 2,
    "e2e_p99": 4174.75,
    "errors": 0,
    "itl_p50": 15.0,
    "output_tok_s": 126.4,
    "req_s": 0.49,
    "ttft_p50": 221.56,
    "ttft_p99": 342.72
  },
  {
    "concurrency": 4,
    "e2e_p99": 7038.08,
    "errors": 0,
    "itl_p50": 24.22,
    "output_tok_s": 152.9,
    "req_s": 0.6,
    "ttft_p50": 356.16,
    "ttft_p99": 840.86
  },
  {
    "concurrency": 8,
    "e2e_p99": 11753.27,
    "errors": 0,
    "itl_p50": 39.57,
    "output_tok_s": 185.0,
    "req_s": 0.72,
    "ttft_p50": 689.27,
    "ttft_p99": 1638.76
  },
  {
    "concurrency": 16,
    "e2e_p99": 21591.5,
    "errors": 0,
    "itl_p50": 39.7,
    "output_tok_s": 193.3,
    "req_s": 0.75,
    "ttft_p50": 11313.92,
    "ttft_p99": 11415.16
  },
  {
    "concurrency": 32,
    "e2e_p99": 41928.24,
    "errors": 0,
    "itl_p50": 39.83,
    "output_tok_s": 196.0,
    "req_s": 0.77,
    "ttft_p50": 31432.37,
    "ttft_p99": 31734.05
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
