# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q8_0_tp4x1_spec-none_c32768_pl270_aggregate`

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
| Concurrency | 8 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| Power limit | 270 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 206.7 |
| `req_s` | 0.81 |
| `ttft_p50_ms` | 528.51 |
| `ttft_p99_ms` | 746.07 |
| `itl_p50_ms` | 36.64 |
| `e2e_p99_ms` | 10110.83 |
| `vram_peak_mib` | 20144 |
| `avg_power_w` | 719.8 |
| `max_temp_c` | 71.0 |

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
    "e2e_p99": 4997.2,
    "errors": 0,
    "itl_p50": 18.66,
    "output_tok_s": 52.8,
    "req_s": 0.21,
    "ttft_p50": 61.58,
    "ttft_p99": 231.05
  },
  {
    "concurrency": 2,
    "e2e_p99": 5500.46,
    "errors": 0,
    "itl_p50": 20.04,
    "output_tok_s": 96.7,
    "req_s": 0.38,
    "ttft_p50": 99.46,
    "ttft_p99": 349.95
  },
  {
    "concurrency": 4,
    "e2e_p99": 6805.76,
    "errors": 0,
    "itl_p50": 23.21,
    "output_tok_s": 156.9,
    "req_s": 0.61,
    "ttft_p50": 602.02,
    "ttft_p99": 849.18
  },
  {
    "concurrency": 8,
    "e2e_p99": 10110.83,
    "errors": 0,
    "itl_p50": 36.64,
    "output_tok_s": 206.7,
    "req_s": 0.81,
    "ttft_p50": 528.51,
    "ttft_p99": 746.07
  },
  {
    "concurrency": 16,
    "e2e_p99": 20839.37,
    "errors": 0,
    "itl_p50": 36.73,
    "output_tok_s": 204.5,
    "req_s": 0.8,
    "ttft_p50": 9888.34,
    "ttft_p99": 11425.29
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
