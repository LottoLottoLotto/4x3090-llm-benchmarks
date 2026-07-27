# `nvfp4/cyankiwi-AWQ/tp2`

| field | value |
|---|---|
| Date | 2026-07-11 |
| Campaign | nvfp4-driver |
| Model | Qwen3.6-35B-A3B |
| Checkpoint | cyankiwi-AWQ |
| Quant | awq-int4 |
| Quant method | awq |
| Engine | vllm |
| Engine version | 0.24 |
| Objective | single_stream+aggregate |
| TPS kind | single_stream_wall |
| Layout | TP=2 |
| Context | 131072 |
| Concurrency | 1 |
| Prompt tokens | 1024 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 131.1 |
| `total_tok_s` | 655.7 |
| `ttft_p50_ms` | 172.1 |
| `itl_p50_ms` | 6.89 |
| `tpot_p50_ms` | 6.9 |
| `e2e_p99_ms` | 1931.3 |

## Launch command

```bash
VLLM_ATTENTION_BACKEND=FLASH_ATTN VLLM_USE_FLASHINFER_SAMPLER=0 vllm serve ${MODEL_ROOT_ALT}/cyankiwi-AWQ* --served-model-name bench --tensor-parallel-size 2 --max-model-len 131072 --gpu-memory-utilization 0.90 --port 18011 --trust-remote-code # client: vllm bench serve --tokenizer <dir>
```

## Throughput curve

```json
[
  {
    "conc": 1,
    "out_tps": 131.1,
    "tot_tps": 655.7,
    "tpot_ms": 6.9,
    "ttft_ms": 172.1
  },
  {
    "conc": 1,
    "out_tps": 124.9,
    "tot_tps": 624.4,
    "tpot_ms": 6.48,
    "ttft_ms": 308.3
  },
  {
    "conc": 2,
    "out_tps": 205.0,
    "tot_tps": 1024.9,
    "tpot_ms": 8.71,
    "ttft_ms": 247.0
  },
  {
    "conc": 2,
    "out_tps": 187.0,
    "tot_tps": 935.1,
    "tpot_ms": 8.78,
    "ttft_ms": 450.6
  },
  {
    "conc": 4,
    "out_tps": 340.1,
    "tot_tps": 1700.3,
    "tpot_ms": 9.93,
    "ttft_ms": 471.9
  },
  {
    "conc": 4,
    "out_tps": 270.0,
    "tot_tps": 1349.8,
    "tpot_ms": 10.81,
    "ttft_ms": 1132.2
  },
  {
    "conc": 8,
    "out_tps": 522.9,
    "tot_tps": 2614.5,
    "tpot_ms": 12.98,
    "ttft_ms": 609.0
  },
  {
    "conc": 8,
    "out_tps": 304.9,
    "tot_tps": 1524.4,
    "tpot_ms": 15.98,
    "ttft_ms": 1670.4
  },
  {
    "conc": 16,
    "out_tps": 702.4,
    "tot_tps": 3512.2,
    "tpot_ms": 19.69,
    "ttft_ms": 845.4
  },
  {
    "conc": 16,
    "out_tps": 419.6,
    "tot_tps": 2098.2,
    "tpot_ms": 31.4,
    "ttft_ms": 1699.2
  },
  {
    "conc": 32,
    "out_tps": 886.1,
    "tot_tps": 4430.7,
    "tpot_ms": 32.47,
    "ttft_ms": 934.5
  },
  {
    "conc": 32,
    "out_tps": 477.5,
    "tot_tps": 2387.7,
    "tpot_ms": 59.87,
    "ttft_ms": 1723.3
  },
  {
    "conc": 64,
    "out_tps": 1058.9,
    "tot_tps": 5294.7,
    "tpot_ms": 56.83,
    "ttft_ms": 980.6
  },
  {
    "conc": 64,
    "out_tps": 561.0,
    "tot_tps": 2805.0,
    "tpot_ms": 105.6,
    "ttft_ms": 2266.3
  }
]
```

## Provenance

- `rig:~/benchmarks/qwen36-35b-nvfp4-vs-awq`

## Notes

agg peak 1058.9 tok/s @conc64. Ampere: NVFP4/Fast/AWQ тайят (Marlin W4A16). FLASH_ATTN backend, Marlin.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
