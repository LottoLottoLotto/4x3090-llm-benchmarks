# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q6_K_tp2x1_spec-none_c32768_pl220_single_stream`

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
| Layout | TP=2 |
| Context | 32768 |
| Concurrency | 1 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 57.8 |
| `req_s` | 0.23 |
| `ttft_p50_ms` | 61.88 |
| `ttft_p99_ms` | 71.85 |
| `itl_p50_ms` | 16.98 |
| `e2e_p99_ms` | 4459.85 |
| `vram_peak_mib` | 23856 |
| `avg_power_w` | 491.6 |
| `max_temp_c` | 71.0 |

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
    "e2e_p99": 4459.85,
    "errors": 0,
    "itl_p50": 16.98,
    "output_tok_s": 57.8,
    "req_s": 0.23,
    "ttft_p50": 61.88,
    "ttft_p99": 71.85
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
