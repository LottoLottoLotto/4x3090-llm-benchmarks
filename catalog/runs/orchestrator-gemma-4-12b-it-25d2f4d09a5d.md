# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q6_K_tp4x1_spec-none_c32768_pl300_aggregate`

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
| Power limit | 300 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 207.0 |
| `req_s` | 0.81 |
| `ttft_p50_ms` | 10064.94 |
| `ttft_p99_ms` | 10601.0 |
| `itl_p50_ms` | 37.23 |
| `e2e_p99_ms` | 20167.96 |
| `vram_peak_mib` | 16912 |
| `avg_power_w` | 773.3 |
| `max_temp_c` | 73.0 |

## Launch command

```bash
'${ENGINE_ROOT}/llama.cpp/build/bin/llama-server' -m '${MODEL_ROOT}/gemma-4-12b-it-GGUF/gemma-4-12b-it-Q6_K.gguf' --host 127.0.0.1 --port 18000 -ngl 99 -c 32768 -np 8 -b 2048 -ub 512 -sm layer -rea off -fa on
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
    "e2e_p99": 4286.16,
    "errors": 0,
    "itl_p50": 15.82,
    "output_tok_s": 62.1,
    "req_s": 0.24,
    "ttft_p50": 56.23,
    "ttft_p99": 241.5
  },
  {
    "concurrency": 2,
    "e2e_p99": 4826.9,
    "errors": 0,
    "itl_p50": 17.3,
    "output_tok_s": 111.8,
    "req_s": 0.44,
    "ttft_p50": 82.58,
    "ttft_p99": 365.61
  },
  {
    "concurrency": 4,
    "e2e_p99": 6747.64,
    "errors": 0,
    "itl_p50": 23.71,
    "output_tok_s": 158.2,
    "req_s": 0.62,
    "ttft_p50": 381.35,
    "ttft_p99": 722.94
  },
  {
    "concurrency": 8,
    "e2e_p99": 10702.15,
    "errors": 0,
    "itl_p50": 37.11,
    "output_tok_s": 195.7,
    "req_s": 0.76,
    "ttft_p50": 973.98,
    "ttft_p99": 1230.15
  },
  {
    "concurrency": 16,
    "e2e_p99": 20167.96,
    "errors": 0,
    "itl_p50": 37.23,
    "output_tok_s": 207.0,
    "req_s": 0.81,
    "ttft_p50": 10064.94,
    "ttft_p99": 10601.0
  },
  {
    "concurrency": 32,
    "e2e_p99": 40467.18,
    "errors": 0,
    "itl_p50": 37.34,
    "output_tok_s": 205.0,
    "req_s": 0.8,
    "ttft_p50": 29629.81,
    "ttft_p99": 30856.5
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
