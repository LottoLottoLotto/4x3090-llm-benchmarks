# `qwen122b/vllm-tp4-220w/code`

| field | value |
|---|---|
| Date | 2026-07-02 |
| Campaign | qwen122b |
| Model | Qwen3.5-122B |
| Checkpoint | Qwen3.5-122B-AWQ |
| Quant | awq-int4 |
| Quant method | awq |
| Engine | vllm |
| Engine version | 0.23.0 |
| Objective | single_stream+aggregate |
| TPS kind | single_stream_wall |
| Layout | TP=4 |
| Concurrency | 1 |
| Generated tokens | 512 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 92.7 |

## Launch command

```bash
vllm serve <Qwen3.5-122B weights> --tensor-parallel-size 4 --max-model-len ~200000 --gpu-memory-utilization 0.92 --served-model-name bench # reconstructed from run tag; exact argv not logged this run
```

## Throughput curve

```json
[
  {
    "conc": 1,
    "itl_ms": 10.65,
    "out_tps": 92.0,
    "ttft_ms": 119.68
  },
  {
    "conc": 2,
    "itl_ms": 12.83,
    "out_tps": 150.1,
    "ttft_ms": 221.7
  },
  {
    "conc": 4,
    "itl_ms": 15.81,
    "out_tps": 242.4,
    "ttft_ms": 393.32
  },
  {
    "conc": 8,
    "itl_ms": 21.32,
    "out_tps": 356.3,
    "ttft_ms": 720.79
  },
  {
    "conc": 16,
    "itl_ms": 31.85,
    "out_tps": 467.8,
    "ttft_ms": 1138.66
  }
]
```

## Provenance

- `rig:~/benchmarks/qwen122b`

## Notes

prompt=code. Топ-локалка (96GB). agg peak 467.8 tok/s.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
