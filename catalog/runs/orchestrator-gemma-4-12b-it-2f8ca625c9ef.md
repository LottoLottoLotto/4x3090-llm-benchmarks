# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q8_0_tp2x1_spec-none_c32768_pl220_aggregate`

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
| Layout | TP=2 |
| Context | 32768 |
| Concurrency | 16 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 193.2 |
| `req_s` | 0.75 |
| `ttft_p50_ms` | 10946.01 |
| `ttft_p99_ms` | 11268.24 |
| `itl_p50_ms` | 39.95 |
| `e2e_p99_ms` | 21497.69 |
| `vram_peak_mib` | 35552 |
| `avg_power_w` | 460.4 |
| `max_temp_c` | 71.0 |

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
    "e2e_p99": 5074.76,
    "errors": 0,
    "itl_p50": 18.76,
    "output_tok_s": 52.2,
    "req_s": 0.2,
    "ttft_p50": 62.74,
    "ttft_p99": 297.06
  },
  {
    "concurrency": 2,
    "e2e_p99": 5652.37,
    "errors": 0,
    "itl_p50": 20.16,
    "output_tok_s": 95.7,
    "req_s": 0.37,
    "ttft_p50": 107.84,
    "ttft_p99": 444.14
  },
  {
    "concurrency": 4,
    "e2e_p99": 6969.02,
    "errors": 0,
    "itl_p50": 23.77,
    "output_tok_s": 152.9,
    "req_s": 0.6,
    "ttft_p50": 616.21,
    "ttft_p99": 864.96
  },
  {
    "concurrency": 8,
    "e2e_p99": 11768.78,
    "errors": 0,
    "itl_p50": 39.98,
    "output_tok_s": 179.9,
    "req_s": 0.7,
    "ttft_p50": 934.27,
    "ttft_p99": 1222.44
  },
  {
    "concurrency": 16,
    "e2e_p99": 21497.69,
    "errors": 0,
    "itl_p50": 39.95,
    "output_tok_s": 193.2,
    "req_s": 0.75,
    "ttft_p50": 10946.01,
    "ttft_p99": 11268.24
  },
  {
    "concurrency": 32,
    "e2e_p99": 43022.06,
    "errors": 0,
    "itl_p50": 39.97,
    "output_tok_s": 191.9,
    "req_s": 0.75,
    "ttft_p50": 31907.55,
    "ttft_p99": 32783.89
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
