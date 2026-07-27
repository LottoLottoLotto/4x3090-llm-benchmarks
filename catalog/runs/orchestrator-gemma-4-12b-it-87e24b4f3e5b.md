# `orch/gemma-4-12B-it-AWQ-INT4/vllm_AWQ-4bit_tp4x1_spec-none_c32768_pl220_aggregate`

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
| Layout | TP=4 |
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
| `output_tok_s` | 1007.5 |
| `req_s` | 3.94 |
| `ttft_p50_ms` | 1482.1 |
| `ttft_p99_ms` | 1531.99 |
| `itl_p50_ms` | 120.86 |
| `e2e_p99_ms` | 32517.74 |
| `vram_peak_mib` | 89024 |
| `avg_power_w` | 864.1 |
| `max_temp_c` | 75.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/gemma-4-12B-it-AWQ-INT4' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 4 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 256 --enable-chunked-prefill
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
    "e2e_p99": 2789.31,
    "errors": 0,
    "itl_p50": 9.5,
    "output_tok_s": 102.7,
    "req_s": 0.4,
    "ttft_p50": 43.99,
    "ttft_p99": 396.07
  },
  {
    "concurrency": 2,
    "e2e_p99": 2741.78,
    "errors": 0,
    "itl_p50": 10.05,
    "output_tok_s": 192.8,
    "req_s": 0.75,
    "ttft_p50": 63.3,
    "ttft_p99": 81.92
  },
  {
    "concurrency": 4,
    "e2e_p99": 3394.23,
    "errors": 0,
    "itl_p50": 12.53,
    "output_tok_s": 310.2,
    "req_s": 1.21,
    "ttft_p50": 79.94,
    "ttft_p99": 122.46
  },
  {
    "concurrency": 8,
    "e2e_p99": 4950.41,
    "errors": 0,
    "itl_p50": 17.89,
    "output_tok_s": 424.5,
    "req_s": 1.66,
    "ttft_p50": 116.17,
    "ttft_p99": 328.28
  },
  {
    "concurrency": 16,
    "e2e_p99": 7907.63,
    "errors": 0,
    "itl_p50": 28.9,
    "output_tok_s": 524.3,
    "req_s": 2.05,
    "ttft_p50": 226.84,
    "ttft_p99": 577.12
  },
  {
    "concurrency": 32,
    "e2e_p99": 10274.05,
    "errors": 0,
    "itl_p50": 37.27,
    "output_tok_s": 810.0,
    "req_s": 3.16,
    "ttft_p50": 433.28,
    "ttft_p99": 557.11
  },
  {
    "concurrency": 64,
    "e2e_p99": 17886.84,
    "errors": 0,
    "itl_p50": 65.78,
    "output_tok_s": 920.6,
    "req_s": 3.6,
    "ttft_p50": 768.85,
    "ttft_p99": 917.05
  },
  {
    "concurrency": 96,
    "e2e_p99": 25951.36,
    "errors": 0,
    "itl_p50": 94.83,
    "output_tok_s": 959.7,
    "req_s": 3.75,
    "ttft_p50": 987.72,
    "ttft_p99": 1369.87
  },
  {
    "concurrency": 128,
    "e2e_p99": 32517.74,
    "errors": 0,
    "itl_p50": 120.86,
    "output_tok_s": 1007.5,
    "req_s": 3.94,
    "ttft_p50": 1482.1,
    "ttft_p99": 1531.99
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-AWQ-INT4`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
