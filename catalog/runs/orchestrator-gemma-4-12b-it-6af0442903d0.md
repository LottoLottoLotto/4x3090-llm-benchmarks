# `orch/gemma-4-12b-it-GGUF/llamacpp_GGUF-Q4_K_M_tp4x1_spec-mtp_c32768_pl220_aggregate`

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
| Objective | aggregate |
| TPS kind | aggregate_output |
| Layout | TP=4 |
| Context | 32768 |
| Concurrency | 4 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 76.2 |
| `req_s` | 0.3 |
| `ttft_p50_ms` | 486.28 |
| `ttft_p99_ms` | 662.29 |
| `itl_p50_ms` | 0.14 |
| `e2e_p99_ms` | 13688.87 |
| `vram_peak_mib` | 17448 |
| `avg_power_w` | 614.4 |
| `max_temp_c` | 69.0 |

## Launch command

```bash
'${ENGINE_ROOT}/llama.cpp/build/bin/llama-server' -m '${MODEL_ROOT}/gemma-4-12b-it-GGUF/gemma-4-12b-it-Q4_K_M.gguf' --host 127.0.0.1 --port 18001 -ngl 99 -c 32768 -np 8 -b 2048 -ub 512 -sm layer -rea off -fa on --model-draft '${MODEL_ROOT}/gemma-4-12b-it-GGUF/MTP/gemma-4-12b-it-Q8_0-MTP.gguf' --spec-type draft-mtp --spec-draft-n-max 4
```

## Speculative decoding

```json
{
  "draft_path": null,
  "draft_ref": null,
  "k": null,
  "method": "mtp"
}
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
    "e2e_p99": 4274.16,
    "errors": 0,
    "itl_p50": 0.16,
    "output_tok_s": 65.2,
    "req_s": 0.25,
    "ttft_p50": 65.51,
    "ttft_p99": 301.62
  },
  {
    "concurrency": 2,
    "e2e_p99": 7183.75,
    "errors": 0,
    "itl_p50": 0.16,
    "output_tok_s": 74.6,
    "req_s": 0.29,
    "ttft_p50": 173.09,
    "ttft_p99": 390.9
  },
  {
    "concurrency": 4,
    "e2e_p99": 13688.87,
    "errors": 0,
    "itl_p50": 0.14,
    "output_tok_s": 76.2,
    "req_s": 0.3,
    "ttft_p50": 486.28,
    "ttft_p99": 662.29
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12b-it-GGUF`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
