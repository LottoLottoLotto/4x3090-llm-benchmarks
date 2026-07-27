# `nvfp4/unsloth-NVFP4-Fast/tp2`

| field | value |
|---|---|
| Date | 2026-07-11 |
| Campaign | nvfp4-driver |
| Model | Qwen3.6-35B-A3B |
| Checkpoint | unsloth-NVFP4-Fast |
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
| `ttft_p50_ms` | 171.2 |
| `itl_p50_ms` | 5.92 |
| `tpot_p50_ms` | 5.92 |
| `e2e_p99_ms` | 1680.8 |

## Launch command

```bash
VLLM_ATTENTION_BACKEND=FLASH_ATTN VLLM_USE_FLASHINFER_SAMPLER=0 vllm serve ${MODEL_ROOT_ALT}/unsloth-NVFP4-Fast* --served-model-name bench --tensor-parallel-size 2 --max-model-len 131072 --gpu-memory-utilization 0.90 --port 18011 --trust-remote-code # client: vllm bench serve --tokenizer <dir>
```

## Throughput curve

```json
[
  {
    "conc": 1,
    "out_tps": 145.4,
    "tot_tps": 727.0,
    "tpot_ms": 5.92,
    "ttft_ms": 171.2
  },
  {
    "conc": 2,
    "out_tps": 230.4,
    "tot_tps": 1151.8,
    "tpot_ms": 7.55,
    "ttft_ms": 248.4
  },
  {
    "conc": 4,
    "out_tps": 365.5,
    "tot_tps": 1827.7,
    "tpot_ms": 8.79,
    "ttft_ms": 540.5
  },
  {
    "conc": 8,
    "out_tps": 445.3,
    "tot_tps": 2226.5,
    "tpot_ms": 11.91,
    "ttft_ms": 616.2
  },
  {
    "conc": 16,
    "out_tps": 740.9,
    "tot_tps": 3704.7,
    "tpot_ms": 18.35,
    "ttft_ms": 853.9
  },
  {
    "conc": 32,
    "out_tps": 913.7,
    "tot_tps": 4568.4,
    "tpot_ms": 31.34,
    "ttft_ms": 940.7
  },
  {
    "conc": 64,
    "out_tps": 1047.9,
    "tot_tps": 5239.7,
    "tpot_ms": 57.44,
    "ttft_ms": 989.5
  }
]
```

## Provenance

- `rig:~/benchmarks/qwen36-35b-nvfp4-vs-awq`

## Notes

agg peak 1047.9 tok/s @conc64. Ampere: NVFP4/Fast/AWQ тайят (Marlin W4A16). FLASH_ATTN backend, Marlin.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
