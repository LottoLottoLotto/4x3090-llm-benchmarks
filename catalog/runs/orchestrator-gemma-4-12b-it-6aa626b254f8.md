# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q6_K_tp4x1_spec-none_c32768_pl220_aggregate`

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
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 201.4 |
| `req_s` | 0.79 |
| `ttft_p50_ms` | 10182.64 |
| `ttft_p99_ms` | 11075.83 |
| `itl_p50_ms` | 37.95 |
| `e2e_p99_ms` | 20759.82 |
| `vram_peak_mib` | 16912 |
| `avg_power_w` | 754.2 |
| `max_temp_c` | 72.0 |

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
    "e2e_p99": 4346.39,
    "errors": 0,
    "itl_p50": 15.81,
    "output_tok_s": 61.9,
    "req_s": 0.24,
    "ttft_p50": 61.09,
    "ttft_p99": 294.86
  },
  {
    "concurrency": 2,
    "e2e_p99": 4842.54,
    "errors": 0,
    "itl_p50": 17.24,
    "output_tok_s": 111.9,
    "req_s": 0.44,
    "ttft_p50": 83.06,
    "ttft_p99": 410.81
  },
  {
    "concurrency": 4,
    "e2e_p99": 6858.95,
    "errors": 0,
    "itl_p50": 23.74,
    "output_tok_s": 158.2,
    "req_s": 0.62,
    "ttft_p50": 382.18,
    "ttft_p99": 759.56
  },
  {
    "concurrency": 8,
    "e2e_p99": 10737.55,
    "errors": 0,
    "itl_p50": 38.15,
    "output_tok_s": 197.1,
    "req_s": 0.77,
    "ttft_p50": 708.71,
    "ttft_p99": 956.44
  },
  {
    "concurrency": 16,
    "e2e_p99": 20759.82,
    "errors": 0,
    "itl_p50": 37.95,
    "output_tok_s": 201.4,
    "req_s": 0.79,
    "ttft_p50": 10182.64,
    "ttft_p99": 11075.83
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
