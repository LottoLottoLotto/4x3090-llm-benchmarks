# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q8_0_tp2x1_spec-none_c32768_pl220_single_stream`

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
| `output_tok_s` | 52.5 |
| `req_s` | 0.21 |
| `ttft_p50_ms` | 66.47 |
| `ttft_p99_ms` | 86.99 |
| `itl_p50_ms` | 18.76 |
| `e2e_p99_ms` | 4901.26 |
| `vram_peak_mib` | 29616 |
| `avg_power_w` | 493.5 |
| `max_temp_c` | 72.0 |

## Launch command

```bash
'${ENGINE_ROOT}/llama.cpp/build/bin/llama-server' -m '${MODEL_ROOT}/gemma-4-12b-it-GGUF/gemma-4-12b-it-Q8_0.gguf' --host 127.0.0.1 --port 18001 -ngl 99 -c 32768 -np 1 -b 2048 -ub 512 -sm layer -rea off -fa on
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
    "e2e_p99": 4901.26,
    "errors": 0,
    "itl_p50": 18.76,
    "output_tok_s": 52.5,
    "req_s": 0.21,
    "ttft_p50": 66.47,
    "ttft_p99": 86.99
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
