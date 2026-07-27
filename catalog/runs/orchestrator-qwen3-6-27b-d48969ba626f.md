# `orch/Qwen3.6-27B/vllm_Int4_tp4x1_spec-none_c32768_pl220_aggregate`

| field | value |
|---|---|
| Date | 2026-06-28 |
| Campaign | orchestrator |
| Model | Qwen3.6-27B |
| Checkpoint | qwen3.6-27b-autoround-int4 |
| Quant | autoround-int4 |
| Quant method | autoround |
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
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 306.6 |
| `req_s` | 1.2 |
| `ttft_p50_ms` | 25732.8 |
| `ttft_p99_ms` | 46735.63 |
| `itl_p50_ms` | 135.39 |
| `e2e_p99_ms` | 80161.28 |
| `vram_peak_mib` | 88648 |
| `avg_power_w` | 866.8 |
| `max_temp_c` | 74.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/qwen3.6-27b-autoround-int4' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 4 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 256 --enable-chunked-prefill
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
    "e2e_p99": 3823.8,
    "errors": 0,
    "itl_p50": 12.37,
    "output_tok_s": 69.2,
    "req_s": 0.27,
    "ttft_p50": 525.58,
    "ttft_p99": 688.4
  },
  {
    "concurrency": 2,
    "e2e_p99": 5471.55,
    "errors": 0,
    "itl_p50": 14.91,
    "output_tok_s": 104.2,
    "req_s": 0.41,
    "ttft_p50": 557.39,
    "ttft_p99": 1794.7
  },
  {
    "concurrency": 4,
    "e2e_p99": 6728.19,
    "errors": 0,
    "itl_p50": 18.39,
    "output_tok_s": 153.0,
    "req_s": 0.6,
    "ttft_p50": 1957.9,
    "ttft_p99": 2004.89
  },
  {
    "concurrency": 8,
    "e2e_p99": 10867.95,
    "errors": 0,
    "itl_p50": 24.49,
    "output_tok_s": 200.2,
    "req_s": 0.78,
    "ttft_p50": 3028.98,
    "ttft_p99": 4077.36
  },
  {
    "concurrency": 16,
    "e2e_p99": 21790.09,
    "errors": 0,
    "itl_p50": 40.78,
    "output_tok_s": 221.5,
    "req_s": 0.87,
    "ttft_p50": 4828.69,
    "ttft_p99": 8172.78
  },
  {
    "concurrency": 32,
    "e2e_p99": 35579.7,
    "errors": 0,
    "itl_p50": 48.96,
    "output_tok_s": 261.9,
    "req_s": 1.02,
    "ttft_p50": 6282.85,
    "ttft_p99": 15487.37
  },
  {
    "concurrency": 64,
    "e2e_p99": 54076.1,
    "errors": 0,
    "itl_p50": 91.26,
    "output_tok_s": 302.9,
    "req_s": 1.18,
    "ttft_p50": 16803.48,
    "ttft_p99": 31154.34
  },
  {
    "concurrency": 96,
    "e2e_p99": 80161.28,
    "errors": 0,
    "itl_p50": 135.39,
    "output_tok_s": 306.6,
    "req_s": 1.2,
    "ttft_p50": 25732.8,
    "ttft_p99": 46735.63
  }
]
```

## Provenance

- `rig:~/benchmarks/Qwen3.6-27B`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
