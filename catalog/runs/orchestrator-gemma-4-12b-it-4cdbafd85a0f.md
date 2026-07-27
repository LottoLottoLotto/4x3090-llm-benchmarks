# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q8_0_tp1x1_spec-none_c32768_pl220_aggregate`

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
| Layout | TP=1 |
| Context | 32768 |
| Concurrency | 16 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 116.6 |
| `req_s` | 0.46 |
| `ttft_p50_ms` | 17661.58 |
| `ttft_p99_ms` | 18259.44 |
| `itl_p50_ms` | 67.2 |
| `e2e_p99_ms` | 35363.39 |
| `vram_peak_mib` | 67464 |
| `avg_power_w` | 302.6 |
| `max_temp_c` | 73.0 |

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
    "e2e_p99": 7725.27,
    "errors": 0,
    "itl_p50": 28.84,
    "output_tok_s": 33.7,
    "req_s": 0.13,
    "ttft_p50": 90.56,
    "ttft_p99": 329.34
  },
  {
    "concurrency": 2,
    "e2e_p99": 8650.73,
    "errors": 0,
    "itl_p50": 31.49,
    "output_tok_s": 61.1,
    "req_s": 0.24,
    "ttft_p50": 162.42,
    "ttft_p99": 517.68
  },
  {
    "concurrency": 4,
    "e2e_p99": 11108.53,
    "errors": 0,
    "itl_p50": 40.07,
    "output_tok_s": 93.1,
    "req_s": 0.36,
    "ttft_p50": 699.8,
    "ttft_p99": 905.86
  },
  {
    "concurrency": 8,
    "e2e_p99": 18266.4,
    "errors": 0,
    "itl_p50": 67.43,
    "output_tok_s": 113.5,
    "req_s": 0.44,
    "ttft_p50": 1031.22,
    "ttft_p99": 1114.99
  },
  {
    "concurrency": 16,
    "e2e_p99": 35363.39,
    "errors": 0,
    "itl_p50": 67.2,
    "output_tok_s": 116.6,
    "req_s": 0.46,
    "ttft_p50": 17661.58,
    "ttft_p99": 18259.44
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
