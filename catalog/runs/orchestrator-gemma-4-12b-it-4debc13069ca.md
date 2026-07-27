# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q6_K_tp4x1_spec-none_c32768_pl270_aggregate`

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
| Layout | TP=4 |
| Context | 32768 |
| Concurrency | 16 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| Power limit | 270 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 209.7 |
| `req_s` | 0.82 |
| `ttft_p50_ms` | 9956.86 |
| `ttft_p99_ms` | 10031.3 |
| `itl_p50_ms` | 37.29 |
| `e2e_p99_ms` | 19555.54 |
| `vram_peak_mib` | 16912 |
| `avg_power_w` | 773.8 |
| `max_temp_c` | 74.0 |

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
    "e2e_p99": 4295.39,
    "errors": 0,
    "itl_p50": 15.84,
    "output_tok_s": 61.9,
    "req_s": 0.24,
    "ttft_p50": 58.5,
    "ttft_p99": 253.63
  },
  {
    "concurrency": 2,
    "e2e_p99": 4811.84,
    "errors": 0,
    "itl_p50": 17.31,
    "output_tok_s": 110.0,
    "req_s": 0.43,
    "ttft_p50": 118.77,
    "ttft_p99": 369.85
  },
  {
    "concurrency": 4,
    "e2e_p99": 7151.82,
    "errors": 0,
    "itl_p50": 24.59,
    "output_tok_s": 150.3,
    "req_s": 0.59,
    "ttft_p50": 620.28,
    "ttft_p99": 867.3
  },
  {
    "concurrency": 8,
    "e2e_p99": 10954.65,
    "errors": 0,
    "itl_p50": 37.19,
    "output_tok_s": 198.2,
    "req_s": 0.77,
    "ttft_p50": 555.53,
    "ttft_p99": 1471.55
  },
  {
    "concurrency": 16,
    "e2e_p99": 19555.54,
    "errors": 0,
    "itl_p50": 37.29,
    "output_tok_s": 209.7,
    "req_s": 0.82,
    "ttft_p50": 9956.86,
    "ttft_p99": 10031.3
  },
  {
    "concurrency": 32,
    "e2e_p99": 39261.5,
    "errors": 0,
    "itl_p50": 37.42,
    "output_tok_s": 209.1,
    "req_s": 0.82,
    "ttft_p50": 29538.22,
    "ttft_p99": 29674.22
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
