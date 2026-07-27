# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q4_K_M_tp4x1_spec-none_c32768_pl220_aggregate`

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
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 196.7 |
| `req_s` | 0.77 |
| `ttft_p50_ms` | 10624.31 |
| `ttft_p99_ms` | 10655.31 |
| `itl_p50_ms` | 39.83 |
| `e2e_p99_ms` | 20829.97 |
| `vram_peak_mib` | 13976 |
| `avg_power_w` | 724.0 |
| `max_temp_c` | 71.0 |

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
    "e2e_p99": 3462.39,
    "errors": 0,
    "itl_p50": 12.47,
    "output_tok_s": 78.4,
    "req_s": 0.31,
    "ttft_p50": 60.32,
    "ttft_p99": 280.36
  },
  {
    "concurrency": 2,
    "e2e_p99": 4217.47,
    "errors": 0,
    "itl_p50": 14.99,
    "output_tok_s": 128.6,
    "req_s": 0.5,
    "ttft_p50": 92.29,
    "ttft_p99": 352.02
  },
  {
    "concurrency": 4,
    "e2e_p99": 6783.94,
    "errors": 0,
    "itl_p50": 23.5,
    "output_tok_s": 156.7,
    "req_s": 0.61,
    "ttft_p50": 584.56,
    "ttft_p99": 826.11
  },
  {
    "concurrency": 8,
    "e2e_p99": 12073.81,
    "errors": 0,
    "itl_p50": 39.78,
    "output_tok_s": 182.8,
    "req_s": 0.71,
    "ttft_p50": 685.73,
    "ttft_p99": 1867.48
  },
  {
    "concurrency": 16,
    "e2e_p99": 20829.97,
    "errors": 0,
    "itl_p50": 39.83,
    "output_tok_s": 196.7,
    "req_s": 0.77,
    "ttft_p50": 10624.31,
    "ttft_p99": 10655.31
  },
  {
    "concurrency": 32,
    "e2e_p99": 41913.83,
    "errors": 0,
    "itl_p50": 40.01,
    "output_tok_s": 195.7,
    "req_s": 0.76,
    "ttft_p50": 31611.16,
    "ttft_p99": 31673.31
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
