# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q6_K_tp2x1_spec-none_c32768_pl220_aggregate`

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
| Layout | TP=2 |
| Context | 32768 |
| Concurrency | 32 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 168.0 |
| `req_s` | 0.66 |
| `ttft_p50_ms` | 36706.6 |
| `ttft_p99_ms` | 36869.35 |
| `itl_p50_ms` | 47.15 |
| `e2e_p99_ms` | 48778.68 |
| `vram_peak_mib` | 29800 |
| `avg_power_w` | 460.9 |
| `max_temp_c` | 70.0 |

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
    "e2e_p99": 4617.73,
    "errors": 0,
    "itl_p50": 16.81,
    "output_tok_s": 58.2,
    "req_s": 0.23,
    "ttft_p50": 62.78,
    "ttft_p99": 339.1
  },
  {
    "concurrency": 2,
    "e2e_p99": 5221.02,
    "errors": 0,
    "itl_p50": 18.52,
    "output_tok_s": 103.8,
    "req_s": 0.41,
    "ttft_p50": 87.07,
    "ttft_p99": 460.43
  },
  {
    "concurrency": 4,
    "e2e_p99": 7588.24,
    "errors": 0,
    "itl_p50": 26.76,
    "output_tok_s": 141.0,
    "req_s": 0.55,
    "ttft_p50": 389.14,
    "ttft_p99": 776.33
  },
  {
    "concurrency": 8,
    "e2e_p99": 14205.51,
    "errors": 0,
    "itl_p50": 46.94,
    "output_tok_s": 154.0,
    "req_s": 0.6,
    "ttft_p50": 1308.18,
    "ttft_p99": 1505.28
  },
  {
    "concurrency": 16,
    "e2e_p99": 25306.49,
    "errors": 0,
    "itl_p50": 46.91,
    "output_tok_s": 165.4,
    "req_s": 0.65,
    "ttft_p50": 13112.74,
    "ttft_p99": 13334.38
  },
  {
    "concurrency": 32,
    "e2e_p99": 48778.68,
    "errors": 0,
    "itl_p50": 47.15,
    "output_tok_s": 168.0,
    "req_s": 0.66,
    "ttft_p50": 36706.6,
    "ttft_p99": 36869.35
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
