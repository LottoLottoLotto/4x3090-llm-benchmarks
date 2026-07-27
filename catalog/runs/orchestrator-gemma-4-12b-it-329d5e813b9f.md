# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q6_K_tp1x1_spec-none_c32768_pl220_aggregate`

| field | value |
|---|---|
| Date | 2026-06-21 |
| Campaign | orchestrator |
| Model | Gemma-4-12B-it |
| Checkpoint | gemma-4-12b-it-Q6_K.gguf |
| Quant | gguf-q6_k |
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
| `output_tok_s` | 110.0 |
| `req_s` | 0.43 |
| `ttft_p50_ms` | 37609.69 |
| `ttft_p99_ms` | 56146.09 |
| `itl_p50_ms` | 71.79 |
| `e2e_p99_ms` | 74484.89 |
| `vram_peak_mib` | 56472 |
| `avg_power_w` | 302.5 |
| `max_temp_c` | 73.0 |

## Launch command

```bash
'${ENGINE_ROOT}/llama.cpp/build/bin/llama-server' -m '${MODEL_ROOT}/gemma-4-12b-it-GGUF/gemma-4-12b-it-Q6_K.gguf' --host 127.0.0.1 --port 18001 -ngl 99 -c 32768 -np 8 -b 2048 -ub 512 -sm layer -rea off -fa on
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
    "e2e_p99": 8435.27,
    "errors": 0,
    "itl_p50": 31.95,
    "output_tok_s": 30.8,
    "req_s": 0.12,
    "ttft_p50": 98.28,
    "ttft_p99": 345.67
  },
  {
    "concurrency": 2,
    "e2e_p99": 9342.78,
    "errors": 0,
    "itl_p50": 34.31,
    "output_tok_s": 55.9,
    "req_s": 0.22,
    "ttft_p50": 385.12,
    "ttft_p99": 531.26
  },
  {
    "concurrency": 4,
    "e2e_p99": 12545.65,
    "errors": 0,
    "itl_p50": 45.56,
    "output_tok_s": 83.5,
    "req_s": 0.33,
    "ttft_p50": 660.31,
    "ttft_p99": 966.44
  },
  {
    "concurrency": 8,
    "e2e_p99": 19900.67,
    "errors": 0,
    "itl_p50": 72.9,
    "output_tok_s": 104.7,
    "req_s": 0.41,
    "ttft_p50": 1246.28,
    "ttft_p99": 1328.73
  },
  {
    "concurrency": 16,
    "e2e_p99": 38083.33,
    "errors": 0,
    "itl_p50": 72.35,
    "output_tok_s": 108.1,
    "req_s": 0.42,
    "ttft_p50": 19048.69,
    "ttft_p99": 19630.47
  },
  {
    "concurrency": 32,
    "e2e_p99": 74484.89,
    "errors": 0,
    "itl_p50": 71.79,
    "output_tok_s": 110.0,
    "req_s": 0.43,
    "ttft_p50": 37609.69,
    "ttft_p99": 56146.09
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
