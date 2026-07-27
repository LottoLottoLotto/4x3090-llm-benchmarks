# `orch/Qwen3.6-27B/vllm_BF16_tp4x1_spec-none_c32768_pl220_aggregate`

| field | value |
|---|---|
| Date | 2026-06-28 |
| Campaign | orchestrator |
| Model | Qwen3.6-27B |
| Checkpoint | Qwen3.6-27B |
| Quant | bf16 |
| Quant method | none |
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
| `output_tok_s` | 307.5 |
| `req_s` | 1.2 |
| `ttft_p50_ms` | 24013.22 |
| `ttft_p99_ms` | 45198.94 |
| `itl_p50_ms` | 139.73 |
| `e2e_p99_ms` | 79915.46 |
| `vram_peak_mib` | 88112 |
| `avg_power_w` | 867.9 |
| `max_temp_c` | 74.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/Qwen3.6-27B' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 4 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 256 --enable-chunked-prefill
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
    "e2e_p99": 7218.87,
    "errors": 0,
    "itl_p50": 25.49,
    "output_tok_s": 36.0,
    "req_s": 0.14,
    "ttft_p50": 544.44,
    "ttft_p99": 727.33
  },
  {
    "concurrency": 2,
    "e2e_p99": 9562.83,
    "errors": 0,
    "itl_p50": 29.5,
    "output_tok_s": 57.8,
    "req_s": 0.23,
    "ttft_p50": 1084.67,
    "ttft_p99": 2060.71
  },
  {
    "concurrency": 4,
    "e2e_p99": 10268.13,
    "errors": 0,
    "itl_p50": 31.28,
    "output_tok_s": 101.9,
    "req_s": 0.4,
    "ttft_p50": 1958.62,
    "ttft_p99": 2267.17
  },
  {
    "concurrency": 8,
    "e2e_p99": 14331.6,
    "errors": 0,
    "itl_p50": 37.51,
    "output_tok_s": 151.4,
    "req_s": 0.59,
    "ttft_p50": 2981.68,
    "ttft_p99": 4232.89
  },
  {
    "concurrency": 16,
    "e2e_p99": 23378.53,
    "errors": 0,
    "itl_p50": 51.93,
    "output_tok_s": 196.9,
    "req_s": 0.77,
    "ttft_p50": 4849.2,
    "ttft_p99": 7539.87
  },
  {
    "concurrency": 32,
    "e2e_p99": 32320.31,
    "errors": 0,
    "itl_p50": 58.34,
    "output_tok_s": 227.5,
    "req_s": 0.89,
    "ttft_p50": 7014.99,
    "ttft_p99": 14857.99
  },
  {
    "concurrency": 64,
    "e2e_p99": 55957.54,
    "errors": 0,
    "itl_p50": 103.12,
    "output_tok_s": 292.7,
    "req_s": 1.14,
    "ttft_p50": 15876.89,
    "ttft_p99": 30080.8
  },
  {
    "concurrency": 96,
    "e2e_p99": 79915.46,
    "errors": 0,
    "itl_p50": 139.73,
    "output_tok_s": 307.5,
    "req_s": 1.2,
    "ttft_p50": 24013.22,
    "ttft_p99": 45198.94
  },
  {
    "concurrency": 128,
    "e2e_p99": 114029.66,
    "errors": 0,
    "itl_p50": 165.09,
    "output_tok_s": 287.3,
    "req_s": 1.12,
    "ttft_p50": 30987.83,
    "ttft_p99": 99722.03
  }
]
```

## Provenance

- `rig:~/benchmarks/Qwen3.6-27B`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
