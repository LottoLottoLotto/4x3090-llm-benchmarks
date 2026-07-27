# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q6_K_tp4x1_spec-none_c32768_pl250_aggregate`

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
| Concurrency | 8 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| Power limit | 250 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 201.4 |
| `req_s` | 0.79 |
| `ttft_p50_ms` | 525.32 |
| `ttft_p99_ms` | 563.55 |
| `itl_p50_ms` | 37.85 |
| `e2e_p99_ms` | 10309.98 |
| `vram_peak_mib` | 16912 |
| `avg_power_w` | 765.0 |
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
    "e2e_p99": 4304.53,
    "errors": 0,
    "itl_p50": 15.87,
    "output_tok_s": 61.7,
    "req_s": 0.24,
    "ttft_p50": 60.97,
    "ttft_p99": 247.67
  },
  {
    "concurrency": 2,
    "e2e_p99": 4824.41,
    "errors": 0,
    "itl_p50": 17.33,
    "output_tok_s": 109.7,
    "req_s": 0.43,
    "ttft_p50": 122.8,
    "ttft_p99": 363.86
  },
  {
    "concurrency": 4,
    "e2e_p99": 7223.04,
    "errors": 0,
    "itl_p50": 24.72,
    "output_tok_s": 149.1,
    "req_s": 0.58,
    "ttft_p50": 639.09,
    "ttft_p99": 885.74
  },
  {
    "concurrency": 8,
    "e2e_p99": 10309.98,
    "errors": 0,
    "itl_p50": 37.85,
    "output_tok_s": 201.4,
    "req_s": 0.79,
    "ttft_p50": 525.32,
    "ttft_p99": 563.55
  },
  {
    "concurrency": 16,
    "e2e_p99": 21769.52,
    "errors": 0,
    "itl_p50": 37.94,
    "output_tok_s": 196.8,
    "req_s": 0.77,
    "ttft_p50": 11904.74,
    "ttft_p99": 11957.04
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
