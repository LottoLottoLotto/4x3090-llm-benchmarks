# `orch/Qwen3.6-27B/vllm_INT8-W8A8_tp4x1_spec-none_c32768_pl220_aggregate`

| field | value |
|---|---|
| Date | 2026-06-28 |
| Campaign | orchestrator |
| Model | Qwen3.6-27B |
| Checkpoint | Qwen3.6-27B-INT8-W8A8 |
| Quant | int8-w8a8 |
| Quant method | w8a8 |
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
| `output_tok_s` | 357.6 |
| `req_s` | 1.4 |
| `ttft_p50_ms` | 26531.56 |
| `ttft_p99_ms` | 51756.29 |
| `itl_p50_ms` | 162.58 |
| `e2e_p99_ms` | 91610.63 |
| `vram_peak_mib` | 88520 |
| `avg_power_w` | 857.2 |
| `max_temp_c` | 74.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/Qwen3.6-27B-INT8-W8A8' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 4 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 256 --enable-chunked-prefill
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
    "e2e_p99": 5785.55,
    "errors": 0,
    "itl_p50": 20.29,
    "output_tok_s": 45.3,
    "req_s": 0.18,
    "ttft_p50": 455.04,
    "ttft_p99": 617.83
  },
  {
    "concurrency": 2,
    "e2e_p99": 7339.59,
    "errors": 0,
    "itl_p50": 22.5,
    "output_tok_s": 75.9,
    "req_s": 0.3,
    "ttft_p50": 497.73,
    "ttft_p99": 1899.24
  },
  {
    "concurrency": 4,
    "e2e_p99": 8051.46,
    "errors": 0,
    "itl_p50": 24.81,
    "output_tok_s": 127.8,
    "req_s": 0.5,
    "ttft_p50": 1639.87,
    "ttft_p99": 1718.85
  },
  {
    "concurrency": 8,
    "e2e_p99": 12039.43,
    "errors": 0,
    "itl_p50": 32.01,
    "output_tok_s": 178.9,
    "req_s": 0.7,
    "ttft_p50": 2540.29,
    "ttft_p99": 3457.62
  },
  {
    "concurrency": 16,
    "e2e_p99": 20425.74,
    "errors": 0,
    "itl_p50": 46.3,
    "output_tok_s": 221.1,
    "req_s": 0.86,
    "ttft_p50": 4101.96,
    "ttft_p99": 6354.28
  },
  {
    "concurrency": 32,
    "e2e_p99": 32911.34,
    "errors": 0,
    "itl_p50": 52.71,
    "output_tok_s": 294.9,
    "req_s": 1.15,
    "ttft_p50": 5158.26,
    "ttft_p99": 12587.04
  },
  {
    "concurrency": 64,
    "e2e_p99": 48039.34,
    "errors": 0,
    "itl_p50": 89.92,
    "output_tok_s": 340.9,
    "req_s": 1.33,
    "ttft_p50": 13951.13,
    "ttft_p99": 25377.61
  },
  {
    "concurrency": 96,
    "e2e_p99": 69584.99,
    "errors": 0,
    "itl_p50": 124.83,
    "output_tok_s": 353.2,
    "req_s": 1.38,
    "ttft_p50": 20679.39,
    "ttft_p99": 38424.19
  },
  {
    "concurrency": 128,
    "e2e_p99": 91610.63,
    "errors": 0,
    "itl_p50": 162.58,
    "output_tok_s": 357.6,
    "req_s": 1.4,
    "ttft_p50": 26531.56,
    "ttft_p99": 51756.29
  }
]
```

## Provenance

- `rig:~/benchmarks/Qwen3.6-27B`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
