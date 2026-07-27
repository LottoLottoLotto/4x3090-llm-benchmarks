# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q4_K_M_tp1x1_spec-none_c32768_pl220_aggregate`

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
| Layout | TP=1 |
| Context | 32768 |
| Concurrency | 32 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 128.0 |
| `req_s` | 0.5 |
| `ttft_p50_ms` | 32394.43 |
| `ttft_p99_ms` | 48352.24 |
| `itl_p50_ms` | 61.73 |
| `e2e_p99_ms` | 64049.03 |
| `vram_peak_mib` | 46312 |
| `avg_power_w` | 302.0 |
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
    "e2e_p99": 5708.05,
    "errors": 0,
    "itl_p50": 21.21,
    "output_tok_s": 46.2,
    "req_s": 0.18,
    "ttft_p50": 72.06,
    "ttft_p99": 305.77
  },
  {
    "concurrency": 2,
    "e2e_p99": 7166.93,
    "errors": 0,
    "itl_p50": 25.78,
    "output_tok_s": 74.3,
    "req_s": 0.29,
    "ttft_p50": 97.46,
    "ttft_p99": 470.22
  },
  {
    "concurrency": 4,
    "e2e_p99": 10761.88,
    "errors": 0,
    "itl_p50": 39.06,
    "output_tok_s": 96.7,
    "req_s": 0.38,
    "ttft_p50": 659.28,
    "ttft_p99": 870.36
  },
  {
    "concurrency": 8,
    "e2e_p99": 16725.48,
    "errors": 0,
    "itl_p50": 62.75,
    "output_tok_s": 123.3,
    "req_s": 0.48,
    "ttft_p50": 747.13,
    "ttft_p99": 754.61
  },
  {
    "concurrency": 16,
    "e2e_p99": 32338.27,
    "errors": 0,
    "itl_p50": 62.3,
    "output_tok_s": 127.0,
    "req_s": 0.5,
    "ttft_p50": 16400.06,
    "ttft_p99": 16461.94
  },
  {
    "concurrency": 32,
    "e2e_p99": 64049.03,
    "errors": 0,
    "itl_p50": 61.73,
    "output_tok_s": 128.0,
    "req_s": 0.5,
    "ttft_p50": 32394.43,
    "ttft_p99": 48352.24
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
