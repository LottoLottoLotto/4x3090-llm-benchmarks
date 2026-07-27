# `orch/Qwen3.6-27B/vllm_Int4_tp2x1_spec-none_c32768_pl220_aggregate`

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
| Layout | TP=2 |
| Context | 32768 |
| Concurrency | 64 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 404.4 |
| `req_s` | 1.58 |
| `ttft_p50_ms` | 11185.72 |
| `ttft_p99_ms` | 21614.32 |
| `itl_p50_ms` | 75.35 |
| `e2e_p99_ms` | 40492.56 |
| `vram_peak_mib` | 87176 |
| `avg_power_w` | 493.2 |
| `max_temp_c` | 72.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/qwen3.6-27b-autoround-int4' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 2 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 256 --enable-chunked-prefill
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
    "e2e_p99": 4801.28,
    "errors": 0,
    "itl_p50": 16.96,
    "output_tok_s": 53.9,
    "req_s": 0.21,
    "ttft_p50": 358.42,
    "ttft_p99": 410.59
  },
  {
    "concurrency": 2,
    "e2e_p99": 6189.96,
    "errors": 0,
    "itl_p50": 18.74,
    "output_tok_s": 91.2,
    "req_s": 0.36,
    "ttft_p50": 704.57,
    "ttft_p99": 1441.38
  },
  {
    "concurrency": 4,
    "e2e_p99": 6584.57,
    "errors": 0,
    "itl_p50": 20.47,
    "output_tok_s": 155.9,
    "req_s": 0.61,
    "ttft_p50": 1343.4,
    "ttft_p99": 1360.8
  },
  {
    "concurrency": 8,
    "e2e_p99": 8615.63,
    "errors": 0,
    "itl_p50": 21.2,
    "output_tok_s": 251.7,
    "req_s": 0.98,
    "ttft_p50": 2012.71,
    "ttft_p99": 2834.35
  },
  {
    "concurrency": 16,
    "e2e_p99": 14339.73,
    "errors": 0,
    "itl_p50": 28.64,
    "output_tok_s": 324.4,
    "req_s": 1.27,
    "ttft_p50": 2864.17,
    "ttft_p99": 5286.45
  },
  {
    "concurrency": 32,
    "e2e_p99": 26286.33,
    "errors": 0,
    "itl_p50": 43.56,
    "output_tok_s": 378.8,
    "req_s": 1.48,
    "ttft_p50": 5868.72,
    "ttft_p99": 10607.46
  },
  {
    "concurrency": 64,
    "e2e_p99": 40492.56,
    "errors": 0,
    "itl_p50": 75.35,
    "output_tok_s": 404.4,
    "req_s": 1.58,
    "ttft_p50": 11185.72,
    "ttft_p99": 21614.32
  },
  {
    "concurrency": 96,
    "e2e_p99": 64220.87,
    "errors": 0,
    "itl_p50": 111.89,
    "output_tok_s": 382.5,
    "req_s": 1.49,
    "ttft_p50": 17592.51,
    "ttft_p99": 58543.22
  }
]
```

## Provenance

- `rig:~/benchmarks/Qwen3.6-27B`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
