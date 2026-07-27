# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q8_0_tp4x1_spec-none_c32768_pl220_single_stream`

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
| Layout | TP=4 |
| Context | 32768 |
| Concurrency | 1 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 52.9 |
| `req_s` | 0.21 |
| `ttft_p50_ms` | 60.31 |
| `ttft_p99_ms` | 91.23 |
| `itl_p50_ms` | 18.69 |
| `e2e_p99_ms` | 4881.36 |
| `vram_peak_mib` | 17568 |
| `avg_power_w` | 705.6 |
| `max_temp_c` | 72.0 |

## Launch command

```bash
'${ENGINE_ROOT}/llama.cpp/build/bin/llama-server' -m '${MODEL_ROOT}/gemma-4-12b-it-GGUF/gemma-4-12b-it-Q8_0.gguf' --host 127.0.0.1 --port 18000 -ngl 99 -c 32768 -np 1 -b 2048 -ub 512 -sm layer -rea off -fa on
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
    "e2e_p99": 4881.36,
    "errors": 0,
    "itl_p50": 18.69,
    "output_tok_s": 52.9,
    "req_s": 0.21,
    "ttft_p50": 60.31,
    "ttft_p99": 91.23
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
