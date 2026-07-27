# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q8_0_tp4x1_spec-none_c32768_pl220_aggregate`

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
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 217.0 |
| `req_s` | 0.85 |
| `ttft_p50_ms` | 9639.02 |
| `ttft_p99_ms` | 9721.8 |
| `itl_p50_ms` | 36.01 |
| `e2e_p99_ms` | 18918.94 |
| `vram_peak_mib` | 20144 |
| `avg_power_w` | 719.1 |
| `max_temp_c` | 72.0 |

## Launch command

```bash
'${ENGINE_ROOT}/llama.cpp/build/bin/llama-server' -m '${MODEL_ROOT}/gemma-4-12b-it-GGUF/gemma-4-12b-it-Q8_0.gguf' --host 127.0.0.1 --port 18001 -ngl 99 -c 32768 -np 8 -b 2048 -ub 512 -sm layer -rea off -fa on
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
    "e2e_p99": 5024.78,
    "errors": 0,
    "itl_p50": 18.67,
    "output_tok_s": 52.7,
    "req_s": 0.21,
    "ttft_p50": 61.13,
    "ttft_p99": 260.35
  },
  {
    "concurrency": 2,
    "e2e_p99": 5521.09,
    "errors": 0,
    "itl_p50": 20.1,
    "output_tok_s": 96.7,
    "req_s": 0.38,
    "ttft_p50": 97.98,
    "ttft_p99": 361.75
  },
  {
    "concurrency": 4,
    "e2e_p99": 6865.41,
    "errors": 0,
    "itl_p50": 23.28,
    "output_tok_s": 156.5,
    "req_s": 0.61,
    "ttft_p50": 616.74,
    "ttft_p99": 893.33
  },
  {
    "concurrency": 8,
    "e2e_p99": 10865.84,
    "errors": 0,
    "itl_p50": 35.95,
    "output_tok_s": 206.2,
    "req_s": 0.81,
    "ttft_p50": 502.28,
    "ttft_p99": 1634.33
  },
  {
    "concurrency": 16,
    "e2e_p99": 18918.94,
    "errors": 0,
    "itl_p50": 36.01,
    "output_tok_s": 217.0,
    "req_s": 0.85,
    "ttft_p50": 9639.02,
    "ttft_p99": 9721.8
  },
  {
    "concurrency": 32,
    "e2e_p99": 38047.27,
    "errors": 0,
    "itl_p50": 36.18,
    "output_tok_s": 216.0,
    "req_s": 0.84,
    "ttft_p50": 28663.43,
    "ttft_p99": 28806.79
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
