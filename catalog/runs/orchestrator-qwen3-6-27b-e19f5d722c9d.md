# `orch/Qwen3.6-27B/vllm_Int4_tp2x2_spec-none_c32768_pl220_aggregate`

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
| Layout | TP=2, INSTANCES=2 |
| Context | 32768 |
| Concurrency | 128 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 737.3 |
| `req_s` | 2.88 |
| `ttft_p50_ms` | 13026.77 |
| `ttft_p99_ms` | 24233.61 |
| `itl_p50_ms` | 79.95 |
| `e2e_p99_ms` | 44408.64 |
| `vram_peak_mib` | 87552 |
| `avg_power_w` | 818.7 |
| `max_temp_c` | 74.0 |

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
    "e2e_p99": 4861.16,
    "errors": 0,
    "itl_p50": 16.53,
    "output_tok_s": 54.3,
    "req_s": 0.21,
    "ttft_p50": 361.77,
    "ttft_p99": 685.5
  },
  {
    "concurrency": 2,
    "e2e_p99": 5284.81,
    "errors": 0,
    "itl_p50": 16.9,
    "output_tok_s": 100.0,
    "req_s": 0.39,
    "ttft_p50": 380.87,
    "ttft_p99": 444.87
  },
  {
    "concurrency": 4,
    "e2e_p99": 6483.13,
    "errors": 0,
    "itl_p50": 18.86,
    "output_tok_s": 167.4,
    "req_s": 0.65,
    "ttft_p50": 674.58,
    "ttft_p99": 869.61
  },
  {
    "concurrency": 8,
    "e2e_p99": 8108.59,
    "errors": 0,
    "itl_p50": 20.24,
    "output_tok_s": 277.7,
    "req_s": 1.08,
    "ttft_p50": 1331.46,
    "ttft_p99": 1627.01
  },
  {
    "concurrency": 16,
    "e2e_p99": 11880.5,
    "errors": 0,
    "itl_p50": 22.57,
    "output_tok_s": 407.8,
    "req_s": 1.59,
    "ttft_p50": 1615.06,
    "ttft_p99": 3093.02
  },
  {
    "concurrency": 32,
    "e2e_p99": 20303.88,
    "errors": 0,
    "itl_p50": 29.5,
    "output_tok_s": 492.0,
    "req_s": 1.92,
    "ttft_p50": 3854.24,
    "ttft_p99": 6216.74
  },
  {
    "concurrency": 64,
    "e2e_p99": 34618.39,
    "errors": 0,
    "itl_p50": 44.53,
    "output_tok_s": 598.4,
    "req_s": 2.34,
    "ttft_p50": 5868.38,
    "ttft_p99": 11726.36
  },
  {
    "concurrency": 96,
    "e2e_p99": 34009.79,
    "errors": 0,
    "itl_p50": 62.87,
    "output_tok_s": 721.8,
    "req_s": 2.82,
    "ttft_p50": 9905.67,
    "ttft_p99": 17989.37
  },
  {
    "concurrency": 128,
    "e2e_p99": 44408.64,
    "errors": 0,
    "itl_p50": 79.95,
    "output_tok_s": 737.3,
    "req_s": 2.88,
    "ttft_p50": 13026.77,
    "ttft_p99": 24233.61
  }
]
```

## Provenance

- `rig:~/benchmarks/Qwen3.6-27B`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
