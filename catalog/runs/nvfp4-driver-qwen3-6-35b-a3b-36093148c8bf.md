# `nvfp4/unsloth-NVFP4/tp2`

| field | value |
|---|---|
| Date | 2026-07-11 |
| Campaign | nvfp4-driver |
| Model | Qwen3.6-35B-A3B |
| Checkpoint | unsloth-NVFP4 |
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
| `output_tok_s` | 145.4 |
| `total_tok_s` | 727.0 |
| `ttft_p50_ms` | 172.6 |
| `itl_p50_ms` | 5.91 |
| `tpot_p50_ms` | 5.91 |
| `e2e_p99_ms` | 1679.5 |

## Launch command

```bash
VLLM_ATTENTION_BACKEND=FLASH_ATTN VLLM_USE_FLASHINFER_SAMPLER=0 vllm serve ${MODEL_ROOT_ALT}/unsloth-NVFP4* --served-model-name bench --tensor-parallel-size 2 --max-model-len 131072 --gpu-memory-utilization 0.90 --port 18011 --trust-remote-code # client: vllm bench serve --tokenizer <dir>
```

## Throughput curve

```json
[
  {
    "conc": 1,
    "out_tps": 145.4,
    "tot_tps": 727.0,
    "tpot_ms": 5.91,
    "ttft_ms": 172.6
  },
  {
    "conc": 2,
    "out_tps": 226.7,
    "tot_tps": 1133.5,
    "tpot_ms": 7.68,
    "ttft_ms": 250.2
  },
  {
    "conc": 4,
    "out_tps": 358.3,
    "tot_tps": 1791.3,
    "tpot_ms": 9.04,
    "ttft_ms": 543.8
  },
  {
    "conc": 8,
    "out_tps": 432.4,
    "tot_tps": 2162.0,
    "tpot_ms": 12.35,
    "ttft_ms": 621.2
  },
  {
    "conc": 16,
    "out_tps": 717.6,
    "tot_tps": 3588.1,
    "tpot_ms": 19.02,
    "ttft_ms": 865.0
  },
  {
    "conc": 32,
    "out_tps": 889.6,
    "tot_tps": 4448.2,
    "tpot_ms": 32.2,
    "ttft_ms": 954.8
  },
  {
    "conc": 64,
    "out_tps": 1024.1,
    "tot_tps": 5120.3,
    "tpot_ms": 58.87,
    "ttft_ms": 1001.5
  }
]
```

## Provenance

- `rig:~/benchmarks/qwen36-35b-nvfp4-vs-awq`

## Notes

agg peak 1024.1 tok/s @conc64. Ampere: NVFP4/Fast/AWQ тайят (Marlin W4A16). FLASH_ATTN backend, Marlin.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
