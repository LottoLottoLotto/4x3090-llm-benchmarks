# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q6_K_tp4x1_spec-none_c32768_pl250_single_stream`

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
| Objective | single_stream |
| TPS kind | single_stream_wall |
| Layout | TP=4 |
| Context | 32768 |
| Concurrency | 1 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| Power limit | 250 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 62.2 |
| `req_s` | 0.24 |
| `ttft_p50_ms` | 63.47 |
| `ttft_p99_ms` | 82.1 |
| `itl_p50_ms` | 15.82 |
| `e2e_p99_ms` | 4176.13 |
| `vram_peak_mib` | 14328 |
| `avg_power_w` | 785.1 |
| `max_temp_c` | 74.0 |

## Launch command

```bash
'${ENGINE_ROOT}/llama.cpp/build/bin/llama-server' -m '${MODEL_ROOT}/gemma-4-12b-it-GGUF/gemma-4-12b-it-Q6_K.gguf' --host 127.0.0.1 --port 18001 -ngl 99 -c 32768 -np 1 -b 2048 -ub 512 -sm layer -rea off -fa on
```

## Engine knobs

```json
{
  "batch": 2048,
  "flash_attn": true,
  "n_parallel": 1,
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
    "e2e_p99": 4176.13,
    "errors": 0,
    "itl_p50": 15.82,
    "output_tok_s": 62.2,
    "req_s": 0.24,
    "ttft_p50": 63.47,
    "ttft_p99": 82.1
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
