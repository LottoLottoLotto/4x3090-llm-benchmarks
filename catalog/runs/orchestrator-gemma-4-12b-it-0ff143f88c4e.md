# `orch/gemma-4-12B-it-AWQ-INT4/vllm_AWQ-4bit_tp1x2_spec-none_c32768_pl220_aggregate`

| field | value |
|---|---|
| Date | 2026-06-21 |
| Campaign | orchestrator |
| Model | Gemma-4-12B-it |
| Checkpoint | gemma-4-12B-it-AWQ-INT4 |
| Quant | awq-int4 |
| Quant method | awq |
| Engine | vllm |
| Engine version | 0.23.0 |
| Objective | aggregate |
| TPS kind | aggregate_output |
| Layout | TP=1, PP=2, INSTANCES=2 |
| Context | 32768 |
| Concurrency | 128 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 2618.6 |
| `req_s` | 10.23 |
| `ttft_p50_ms` | 525.29 |
| `ttft_p99_ms` | 749.22 |
| `itl_p50_ms` | 45.92 |
| `e2e_p99_ms` | 13138.14 |
| `vram_peak_mib` | 89656 |
| `avg_power_w` | 839.4 |
| `max_temp_c` | 75.0 |

## Launch command

```bash
Command was not captured for this historical row.
```

## Engine knobs

```json
{
  "_env_VLLM_USE_FLASHINFER_SAMPLER": "0",
  "enable_chunked_prefill": true,
  "enforce_eager": false,
  "gpu_memory_utilization": 0.9,
  "kv_cache_dtype": "auto",
  "max_num_seqs": 256,
  "trust_remote_code": true
}
```

## Throughput curve

```json
[
  {
    "concurrency": 1,
    "e2e_p99": 3522.09,
    "errors": 0,
    "itl_p50": 12.93,
    "output_tok_s": 75.8,
    "req_s": 0.3,
    "ttft_p50": 38.1,
    "ttft_p99": 235.93
  },
  {
    "concurrency": 2,
    "e2e_p99": 3376.02,
    "errors": 0,
    "itl_p50": 12.95,
    "output_tok_s": 153.0,
    "req_s": 0.6,
    "ttft_p50": 40.7,
    "ttft_p99": 52.21
  },
  {
    "concurrency": 4,
    "e2e_p99": 3473.72,
    "errors": 0,
    "itl_p50": 13.29,
    "output_tok_s": 297.6,
    "req_s": 1.16,
    "ttft_p50": 47.14,
    "ttft_p99": 66.08
  },
  {
    "concurrency": 8,
    "e2e_p99": 3981.12,
    "errors": 0,
    "itl_p50": 14.0,
    "output_tok_s": 556.5,
    "req_s": 2.17,
    "ttft_p50": 66.4,
    "ttft_p99": 358.49
  },
  {
    "concurrency": 16,
    "e2e_p99": 4126.93,
    "errors": 0,
    "itl_p50": 15.49,
    "output_tok_s": 1003.1,
    "req_s": 3.92,
    "ttft_p50": 110.52,
    "ttft_p99": 147.35
  },
  {
    "concurrency": 32,
    "e2e_p99": 5172.15,
    "errors": 0,
    "itl_p50": 19.05,
    "output_tok_s": 1481.0,
    "req_s": 5.79,
    "ttft_p50": 143.11,
    "ttft_p99": 234.98
  },
  {
    "concurrency": 64,
    "e2e_p99": 7606.88,
    "errors": 0,
    "itl_p50": 27.03,
    "output_tok_s": 2245.4,
    "req_s": 8.77,
    "ttft_p50": 281.56,
    "ttft_p99": 420.94
  },
  {
    "concurrency": 96,
    "e2e_p99": 10235.81,
    "errors": 0,
    "itl_p50": 35.51,
    "output_tok_s": 2531.1,
    "req_s": 9.89,
    "ttft_p50": 385.84,
    "ttft_p99": 616.42
  },
  {
    "concurrency": 128,
    "e2e_p99": 13138.14,
    "errors": 0,
    "itl_p50": 45.92,
    "output_tok_s": 2618.6,
    "req_s": 10.23,
    "ttft_p50": 525.29,
    "ttft_p99": 749.22
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-AWQ-INT4`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
