# `orch/gemma-4-12B-it-AWQ-INT4/vllm_AWQ-4bit_tp1x4_spec-none_c32768_pl300_aggregate`

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
| Layout | TP=1, INSTANCES=4 |
| Context | 32768 |
| Concurrency | 128 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 300 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 3854.8 |
| `req_s` | 15.06 |
| `ttft_p50_ms` | 333.16 |
| `ttft_p99_ms` | 451.77 |
| `itl_p50_ms` | 28.92 |
| `e2e_p99_ms` | 8152.33 |
| `vram_peak_mib` | 88680 |
| `avg_power_w` | 1088.6 |
| `max_temp_c` | 82.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/gemma-4-12B-it-AWQ-INT4' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 1 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 256 --enable-chunked-prefill
```

## Engine knobs

```json
{
  "_env_VLLM_ATTENTION_BACKEND": "FLASH_ATTN",
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
    "e2e_p99": 3841.97,
    "errors": 0,
    "itl_p50": 13.96,
    "output_tok_s": 69.2,
    "req_s": 0.27,
    "ttft_p50": 52.11,
    "ttft_p99": 307.1
  },
  {
    "concurrency": 2,
    "e2e_p99": 3685.83,
    "errors": 0,
    "itl_p50": 14.0,
    "output_tok_s": 140.8,
    "req_s": 0.55,
    "ttft_p50": 46.51,
    "ttft_p99": 75.75
  },
  {
    "concurrency": 4,
    "e2e_p99": 3715.07,
    "errors": 0,
    "itl_p50": 14.0,
    "output_tok_s": 281.6,
    "req_s": 1.1,
    "ttft_p50": 46.44,
    "ttft_p99": 59.71
  },
  {
    "concurrency": 8,
    "e2e_p99": 3830.48,
    "errors": 0,
    "itl_p50": 14.34,
    "output_tok_s": 547.3,
    "req_s": 2.14,
    "ttft_p50": 58.26,
    "ttft_p99": 74.16
  },
  {
    "concurrency": 16,
    "e2e_p99": 4052.33,
    "errors": 0,
    "itl_p50": 15.14,
    "output_tok_s": 1031.8,
    "req_s": 4.03,
    "ttft_p50": 79.19,
    "ttft_p99": 109.07
  },
  {
    "concurrency": 32,
    "e2e_p99": 4931.75,
    "errors": 0,
    "itl_p50": 16.75,
    "output_tok_s": 1804.3,
    "req_s": 7.05,
    "ttft_p50": 130.58,
    "ttft_p99": 446.0
  },
  {
    "concurrency": 64,
    "e2e_p99": 5691.79,
    "errors": 0,
    "itl_p50": 20.72,
    "output_tok_s": 2940.8,
    "req_s": 11.49,
    "ttft_p50": 207.8,
    "ttft_p99": 319.58
  },
  {
    "concurrency": 96,
    "e2e_p99": 7451.08,
    "errors": 0,
    "itl_p50": 26.43,
    "output_tok_s": 3442.8,
    "req_s": 13.45,
    "ttft_p50": 284.29,
    "ttft_p99": 376.73
  },
  {
    "concurrency": 128,
    "e2e_p99": 8152.33,
    "errors": 0,
    "itl_p50": 28.92,
    "output_tok_s": 3854.8,
    "req_s": 15.06,
    "ttft_p50": 333.16,
    "ttft_p99": 451.77
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-AWQ-INT4`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
