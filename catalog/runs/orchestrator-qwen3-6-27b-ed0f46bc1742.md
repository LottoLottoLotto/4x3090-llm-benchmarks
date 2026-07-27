# `orch/Qwen3.6-27B/vllm_INT8-W8A8_tp2x2_spec-none_c32768_pl220_aggregate`

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
| Layout | TP=2, INSTANCES=2 |
| Context | 32768 |
| Concurrency | 64 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 740.9 |
| `req_s` | 2.89 |
| `ttft_p50_ms` | 3996.85 |
| `ttft_p99_ms` | 9471.76 |
| `itl_p50_ms` | 48.09 |
| `e2e_p99_ms` | 30480.35 |
| `vram_peak_mib` | 84984 |
| `avg_power_w` | 826.7 |
| `max_temp_c` | 75.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/Qwen3.6-27B-INT8-W8A8' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 2 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 128 --enable-chunked-prefill
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
  "max_num_seqs": 128,
  "trust_remote_code": true
}
```

## Throughput curve

```json
[
  {
    "concurrency": 1,
    "e2e_p99": 7141.44,
    "errors": 0,
    "itl_p50": 25.9,
    "output_tok_s": 36.5,
    "req_s": 0.14,
    "ttft_p50": 243.41,
    "ttft_p99": 530.39
  },
  {
    "concurrency": 2,
    "e2e_p99": 7400.67,
    "errors": 0,
    "itl_p50": 26.21,
    "output_tok_s": 71.0,
    "req_s": 0.28,
    "ttft_p50": 265.45,
    "ttft_p99": 284.49
  },
  {
    "concurrency": 4,
    "e2e_p99": 8172.39,
    "errors": 0,
    "itl_p50": 27.14,
    "output_tok_s": 123.3,
    "req_s": 0.48,
    "ttft_p50": 477.52,
    "ttft_p99": 637.57
  },
  {
    "concurrency": 8,
    "e2e_p99": 9379.39,
    "errors": 0,
    "itl_p50": 28.68,
    "output_tok_s": 228.6,
    "req_s": 0.89,
    "ttft_p50": 880.98,
    "ttft_p99": 1151.91
  },
  {
    "concurrency": 16,
    "e2e_p99": 12381.6,
    "errors": 0,
    "itl_p50": 32.45,
    "output_tok_s": 365.4,
    "req_s": 1.43,
    "ttft_p50": 1425.99,
    "ttft_p99": 2279.59
  },
  {
    "concurrency": 32,
    "e2e_p99": 18116.32,
    "errors": 0,
    "itl_p50": 37.51,
    "output_tok_s": 493.1,
    "req_s": 1.93,
    "ttft_p50": 2371.8,
    "ttft_p99": 4942.4
  },
  {
    "concurrency": 64,
    "e2e_p99": 30480.35,
    "errors": 0,
    "itl_p50": 48.09,
    "output_tok_s": 740.9,
    "req_s": 2.89,
    "ttft_p50": 3996.85,
    "ttft_p99": 9471.76
  },
  {
    "concurrency": 96,
    "e2e_p99": 50261.4,
    "errors": 0,
    "itl_p50": 57.8,
    "output_tok_s": 714.9,
    "req_s": 2.79,
    "ttft_p50": 5989.59,
    "ttft_p99": 29604.19
  }
]
```

## Provenance

- `rig:~/benchmarks/Qwen3.6-27B`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
