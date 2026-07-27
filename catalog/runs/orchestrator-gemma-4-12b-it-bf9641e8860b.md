# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q4_K_M_tp4x1_spec-none_c32768_pl250_aggregate`

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
| Power limit | 250 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 190.1 |
| `req_s` | 0.74 |
| `ttft_p50_ms` | 12008.83 |
| `ttft_p99_ms` | 12115.44 |
| `itl_p50_ms` | 39.75 |
| `e2e_p99_ms` | 22300.11 |
| `vram_peak_mib` | 13976 |
| `avg_power_w` | 731.3 |
| `max_temp_c` | 71.0 |

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
    "e2e_p99": 3447.53,
    "errors": 0,
    "itl_p50": 12.46,
    "output_tok_s": 78.5,
    "req_s": 0.31,
    "ttft_p50": 57.37,
    "ttft_p99": 267.16
  },
  {
    "concurrency": 2,
    "e2e_p99": 4259.63,
    "errors": 0,
    "itl_p50": 15.03,
    "output_tok_s": 128.0,
    "req_s": 0.5,
    "ttft_p50": 93.24,
    "ttft_p99": 356.0
  },
  {
    "concurrency": 4,
    "e2e_p99": 6832.29,
    "errors": 0,
    "itl_p50": 23.44,
    "output_tok_s": 156.9,
    "req_s": 0.61,
    "ttft_p50": 569.17,
    "ttft_p99": 840.99
  },
  {
    "concurrency": 8,
    "e2e_p99": 11763.54,
    "errors": 0,
    "itl_p50": 39.69,
    "output_tok_s": 184.6,
    "req_s": 0.72,
    "ttft_p50": 690.48,
    "ttft_p99": 1621.27
  },
  {
    "concurrency": 16,
    "e2e_p99": 22300.11,
    "errors": 0,
    "itl_p50": 39.75,
    "output_tok_s": 190.1,
    "req_s": 0.74,
    "ttft_p50": 12008.83,
    "ttft_p99": 12115.44
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
