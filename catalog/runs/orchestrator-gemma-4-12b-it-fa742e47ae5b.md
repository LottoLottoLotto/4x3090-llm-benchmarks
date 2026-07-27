# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q8_0_tp4x1_spec-none_c32768_pl250_aggregate`

| field | value |
|---|---|
| Date | 2026-06-21 |
| Campaign | orchestrator |
| Model | Gemma-4-12B-it |
| Checkpoint | gemma-4-12b-it-Q8_0.gguf |
| Quant | gguf-q8_0 |
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
| `output_tok_s` | 213.5 |
| `req_s` | 0.83 |
| `ttft_p50_ms` | 9809.4 |
| `ttft_p99_ms` | 9939.32 |
| `itl_p50_ms` | 36.52 |
| `e2e_p99_ms` | 19277.87 |
| `vram_peak_mib` | 20144 |
| `avg_power_w` | 725.2 |
| `max_temp_c` | 73.0 |

## Launch command

```bash
'${ENGINE_ROOT}/llama.cpp/build/bin/llama-server' -m '${MODEL_ROOT}/gemma-4-12b-it-GGUF/gemma-4-12b-it-Q8_0.gguf' --host 127.0.0.1 --port 18000 -ngl 99 -c 32768 -np 8 -b 2048 -ub 512 -sm layer -rea off -fa on
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
    "e2e_p99": 4990.51,
    "errors": 0,
    "itl_p50": 18.69,
    "output_tok_s": 52.6,
    "req_s": 0.21,
    "ttft_p50": 62.52,
    "ttft_p99": 225.02
  },
  {
    "concurrency": 2,
    "e2e_p99": 5499.41,
    "errors": 0,
    "itl_p50": 20.14,
    "output_tok_s": 95.2,
    "req_s": 0.37,
    "ttft_p50": 218.13,
    "ttft_p99": 346.37
  },
  {
    "concurrency": 4,
    "e2e_p99": 7059.53,
    "errors": 0,
    "itl_p50": 24.26,
    "output_tok_s": 153.1,
    "req_s": 0.6,
    "ttft_p50": 368.64,
    "ttft_p99": 881.83
  },
  {
    "concurrency": 8,
    "e2e_p99": 11006.96,
    "errors": 0,
    "itl_p50": 36.39,
    "output_tok_s": 202.3,
    "req_s": 0.79,
    "ttft_p50": 725.08,
    "ttft_p99": 1738.55
  },
  {
    "concurrency": 16,
    "e2e_p99": 19277.87,
    "errors": 0,
    "itl_p50": 36.52,
    "output_tok_s": 213.5,
    "req_s": 0.83,
    "ttft_p50": 9809.4,
    "ttft_p99": 9939.32
  },
  {
    "concurrency": 32,
    "e2e_p99": 38660.99,
    "errors": 0,
    "itl_p50": 36.65,
    "output_tok_s": 212.6,
    "req_s": 0.83,
    "ttft_p50": 29112.46,
    "ttft_p99": 29258.28
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
