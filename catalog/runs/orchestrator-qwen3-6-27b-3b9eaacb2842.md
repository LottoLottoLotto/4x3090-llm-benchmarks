# `orch/Qwen3.6-27B/vllm_FP8-static_tp4x1_spec-none_c32768_pl220_aggregate`

| field | value |
|---|---|
| Date | 2026-06-28 |
| Campaign | orchestrator |
| Model | Qwen3.6-27B |
| Checkpoint | Qwen3.6-27B-FP8 |
| Quant | fp8-static |
| Quant method | fp8 |
| Engine | vllm |
| Engine version | 0.23.0 |
| Objective | aggregate |
| TPS kind | aggregate_output |
| Layout | TP=4 |
| Context | 32768 |
| Concurrency | 96 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 305.3 |
| `req_s` | 1.19 |
| `ttft_p50_ms` | 24284.02 |
| `ttft_p99_ms` | 45930.64 |
| `itl_p50_ms` | 139.42 |
| `e2e_p99_ms` | 80491.74 |
| `vram_peak_mib` | 87784 |
| `avg_power_w` | 868.7 |
| `max_temp_c` | 75.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/Qwen3.6-27B-FP8' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 4 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 256 --enable-chunked-prefill
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
    "e2e_p99": 4828.59,
    "errors": 0,
    "itl_p50": 16.25,
    "output_tok_s": 54.4,
    "req_s": 0.21,
    "ttft_p50": 537.12,
    "ttft_p99": 698.62
  },
  {
    "concurrency": 2,
    "e2e_p99": 6870.63,
    "errors": 0,
    "itl_p50": 18.54,
    "output_tok_s": 84.2,
    "req_s": 0.33,
    "ttft_p50": 563.37,
    "ttft_p99": 2064.99
  },
  {
    "concurrency": 4,
    "e2e_p99": 7858.99,
    "errors": 0,
    "itl_p50": 22.14,
    "output_tok_s": 133.6,
    "req_s": 0.52,
    "ttft_p50": 1912.34,
    "ttft_p99": 2211.24
  },
  {
    "concurrency": 8,
    "e2e_p99": 12167.66,
    "errors": 0,
    "itl_p50": 29.8,
    "output_tok_s": 177.7,
    "req_s": 0.69,
    "ttft_p50": 2917.4,
    "ttft_p99": 4055.17
  },
  {
    "concurrency": 16,
    "e2e_p99": 22645.64,
    "errors": 0,
    "itl_p50": 45.15,
    "output_tok_s": 210.0,
    "req_s": 0.82,
    "ttft_p50": 4816.71,
    "ttft_p99": 8096.69
  },
  {
    "concurrency": 32,
    "e2e_p99": 35841.79,
    "errors": 0,
    "itl_p50": 51.81,
    "output_tok_s": 254.8,
    "req_s": 1.0,
    "ttft_p50": 6088.98,
    "ttft_p99": 15334.18
  },
  {
    "concurrency": 64,
    "e2e_p99": 54026.69,
    "errors": 0,
    "itl_p50": 93.59,
    "output_tok_s": 303.1,
    "req_s": 1.18,
    "ttft_p50": 15785.85,
    "ttft_p99": 30468.02
  },
  {
    "concurrency": 96,
    "e2e_p99": 80491.74,
    "errors": 0,
    "itl_p50": 139.42,
    "output_tok_s": 305.3,
    "req_s": 1.19,
    "ttft_p50": 24284.02,
    "ttft_p99": 45930.64
  }
]
```

## Provenance

- `rig:~/benchmarks/Qwen3.6-27B`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
