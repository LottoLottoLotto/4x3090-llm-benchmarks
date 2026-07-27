# `nvfp4/QuantTrio-AWQ/tp2`

| field | value |
|---|---|
| Date | 2026-07-11 |
| Campaign | nvfp4-driver |
| Model | Qwen3.6-35B-A3B |
| Checkpoint | QuantTrio-AWQ |
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
| `output_tok_s` | 129.9 |
| `total_tok_s` | 649.3 |
| `ttft_p50_ms` | 175.0 |
| `itl_p50_ms` | 6.73 |
| `tpot_p50_ms` | 6.73 |
| `e2e_p99_ms` | 1890.1 |

## Launch command

```bash
VLLM_ATTENTION_BACKEND=FLASH_ATTN VLLM_USE_FLASHINFER_SAMPLER=0 vllm serve ${MODEL_ROOT_ALT}/QuantTrio-AWQ* --served-model-name bench --tensor-parallel-size 2 --max-model-len 131072 --gpu-memory-utilization 0.90 --port 18011 --trust-remote-code # client: vllm bench serve --tokenizer <dir>
```

## Throughput curve

```json
[
  {
    "conc": 1,
    "out_tps": 129.9,
    "tot_tps": 649.3,
    "tpot_ms": 6.73,
    "ttft_ms": 175.0
  },
  {
    "conc": 2,
    "out_tps": 205.5,
    "tot_tps": 1027.3,
    "tpot_ms": 8.38,
    "ttft_ms": 252.2
  },
  {
    "conc": 4,
    "out_tps": 339.4,
    "tot_tps": 1697.2,
    "tpot_ms": 9.68,
    "ttft_ms": 551.7
  },
  {
    "conc": 8,
    "out_tps": 419.6,
    "tot_tps": 2097.8,
    "tpot_ms": 13.1,
    "ttft_ms": 563.0
  },
  {
    "conc": 16,
    "out_tps": 715.9,
    "tot_tps": 3579.5,
    "tpot_ms": 19.15,
    "ttft_ms": 867.6
  },
  {
    "conc": 32,
    "out_tps": 869.6,
    "tot_tps": 4348.1,
    "tpot_ms": 32.95,
    "ttft_ms": 961.8
  },
  {
    "conc": 64,
    "out_tps": 1025.2,
    "tot_tps": 5126.2,
    "tpot_ms": 58.94,
    "ttft_ms": 1008.0
  }
]
```

## Provenance

- `rig:~/benchmarks/qwen36-35b-nvfp4-vs-awq`

## Notes

agg peak 1025.2 tok/s @conc64. Ampere: NVFP4/Fast/AWQ тайят (Marlin W4A16). FLASH_ATTN backend, Marlin.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
