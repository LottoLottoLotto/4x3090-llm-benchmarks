# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q4_K_M_tp4x1_spec-none_c32768_pl270_single_stream`

| field | value |
|---|---|
| Date | 2026-06-21 |
| Campaign | orchestrator |
| Model | Gemma-4-12B-it |
| Checkpoint | gemma-4-12b-it-Q4_K_M.gguf |
| Quant | gguf-q4_k_m |
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
| Power limit | 270 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 78.7 |
| `req_s` | 0.31 |
| `ttft_p50_ms` | 59.85 |
| `ttft_p99_ms` | 61.45 |
| `itl_p50_ms` | 12.49 |
| `e2e_p99_ms` | 3271.67 |
| `vram_peak_mib` | 11400 |
| `avg_power_w` | 735.5 |
| `max_temp_c` | 71.0 |

## Launch command

```bash
'${ENGINE_ROOT}/llama.cpp/build/bin/llama-server' -m '${MODEL_ROOT}/gemma-4-12b-it-GGUF/gemma-4-12b-it-Q4_K_M.gguf' --host 127.0.0.1 --port 18000 -ngl 99 -c 32768 -np 1 -b 2048 -ub 512 -sm layer -rea off -fa on
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
    "e2e_p99": 3271.67,
    "errors": 0,
    "itl_p50": 12.49,
    "output_tok_s": 78.7,
    "req_s": 0.31,
    "ttft_p50": 59.85,
    "ttft_p99": 61.45
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
