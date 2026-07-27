# `nvfp4/nvidia-NVFP4/tp2`

| field | value |
|---|---|
| Date | 2026-07-11 |
| Campaign | nvfp4-driver |
| Model | Qwen3.6-35B-A3B |
| Checkpoint | nvidia-NVFP4 |
| Quant | nvfp4 |
| Quant method | nvfp4 |
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
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 148.8 |
| `total_tok_s` | 744.1 |
| `ttft_p50_ms` | 171.3 |
| `itl_p50_ms` | 5.76 |
| `tpot_p50_ms` | 5.76 |
| `e2e_p99_ms` | 1641.3 |

## Launch command

```bash
VLLM_ATTENTION_BACKEND=FLASH_ATTN VLLM_USE_FLASHINFER_SAMPLER=0 vllm serve ${MODEL_ROOT_ALT}/nvidia-NVFP4* --served-model-name bench --tensor-parallel-size 2 --max-model-len 131072 --gpu-memory-utilization 0.90 --port 18011 --trust-remote-code # client: vllm bench serve --tokenizer <dir>
```

## Throughput curve

```json
[
  {
    "conc": 1,
    "out_tps": 148.8,
    "tot_tps": 744.1,
    "tpot_ms": 5.76,
    "ttft_ms": 171.3
  },
  {
    "conc": 1,
    "out_tps": 134.8,
    "tot_tps": 674.2,
    "tpot_ms": 5.91,
    "ttft_ms": 301.0
  },
  {
    "conc": 2,
    "out_tps": 228.9,
    "tot_tps": 1144.4,
    "tpot_ms": 7.67,
    "ttft_ms": 250.3
  },
  {
    "conc": 2,
    "out_tps": 197.7,
    "tot_tps": 988.4,
    "tpot_ms": 8.24,
    "ttft_ms": 440.6
  },
  {
    "conc": 4,
    "out_tps": 373.9,
    "tot_tps": 1869.4,
    "tpot_ms": 8.75,
    "ttft_ms": 538.4
  },
  {
    "conc": 4,
    "out_tps": 281.4,
    "tot_tps": 1407.1,
    "tpot_ms": 10.23,
    "ttft_ms": 1103.1
  },
  {
    "conc": 8,
    "out_tps": 451.2,
    "tot_tps": 2256.0,
    "tpot_ms": 11.78,
    "ttft_ms": 613.4
  },
  {
    "conc": 8,
    "out_tps": 317.1,
    "tot_tps": 1585.3,
    "tpot_ms": 15.6,
    "ttft_ms": 1615.5
  },
  {
    "conc": 16,
    "out_tps": 753.8,
    "tot_tps": 3769.2,
    "tpot_ms": 17.94,
    "ttft_ms": 853.8
  },
  {
    "conc": 16,
    "out_tps": 439.8,
    "tot_tps": 2199.0,
    "tpot_ms": 29.66,
    "ttft_ms": 1889.1
  },
  {
    "conc": 32,
    "out_tps": 917.1,
    "tot_tps": 4585.6,
    "tpot_ms": 31.33,
    "ttft_ms": 938.0
  },
  {
    "conc": 32,
    "out_tps": 489.3,
    "tot_tps": 2446.4,
    "tpot_ms": 58.26,
    "ttft_ms": 1684.2
  },
  {
    "conc": 64,
    "out_tps": 1053.8,
    "tot_tps": 5268.9,
    "tpot_ms": 57.05,
    "ttft_ms": 992.7
  },
  {
    "conc": 64,
    "out_tps": 573.3,
    "tot_tps": 2866.4,
    "tpot_ms": 103.33,
    "ttft_ms": 2201.9
  }
]
```

## Provenance

- `rig:~/benchmarks/qwen36-35b-nvfp4-vs-awq`

## Notes

agg peak 1053.8 tok/s @conc64. Ampere: NVFP4/Fast/AWQ тайят (Marlin W4A16). FLASH_ATTN backend, Marlin.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
