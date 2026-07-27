# `orch/Qwen3.6-27B/vllm_FP8-static_tp2x2_spec-none_c32768_pl220_aggregate`

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
| Layout | TP=2, INSTANCES=2 |
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
| `output_tok_s` | 569.8 |
| `req_s` | 2.23 |
| `ttft_p50_ms` | 9390.52 |
| `ttft_p99_ms` | 34261.57 |
| `itl_p50_ms` | 57.83 |
| `e2e_p99_ms` | 47987.19 |
| `vram_peak_mib` | 84952 |
| `avg_power_w` | 812.9 |
| `max_temp_c` | 73.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/Qwen3.6-27B-FP8' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 2 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 128 --enable-chunked-prefill
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
    "e2e_p99": 7035.38,
    "errors": 0,
    "itl_p50": 25.06,
    "output_tok_s": 37.4,
    "req_s": 0.15,
    "ttft_p50": 358.49,
    "ttft_p99": 661.93
  },
  {
    "concurrency": 2,
    "e2e_p99": 7721.97,
    "errors": 0,
    "itl_p50": 25.31,
    "output_tok_s": 70.6,
    "req_s": 0.28,
    "ttft_p50": 369.69,
    "ttft_p99": 742.95
  },
  {
    "concurrency": 4,
    "e2e_p99": 8480.05,
    "errors": 0,
    "itl_p50": 26.75,
    "output_tok_s": 127.0,
    "req_s": 0.5,
    "ttft_p50": 727.47,
    "ttft_p99": 777.93
  },
  {
    "concurrency": 8,
    "e2e_p99": 10323.01,
    "errors": 0,
    "itl_p50": 28.15,
    "output_tok_s": 206.2,
    "req_s": 0.81,
    "ttft_p50": 1428.23,
    "ttft_p99": 1601.4
  },
  {
    "concurrency": 16,
    "e2e_p99": 14010.06,
    "errors": 0,
    "itl_p50": 31.4,
    "output_tok_s": 318.0,
    "req_s": 1.24,
    "ttft_p50": 2328.05,
    "ttft_p99": 3325.23
  },
  {
    "concurrency": 32,
    "e2e_p99": 21308.18,
    "errors": 0,
    "itl_p50": 36.03,
    "output_tok_s": 457.4,
    "req_s": 1.79,
    "ttft_p50": 3840.64,
    "ttft_p99": 6427.66
  },
  {
    "concurrency": 64,
    "e2e_p99": 36498.04,
    "errors": 0,
    "itl_p50": 47.99,
    "output_tok_s": 567.3,
    "req_s": 2.22,
    "ttft_p50": 6439.44,
    "ttft_p99": 12691.34
  },
  {
    "concurrency": 96,
    "e2e_p99": 47987.19,
    "errors": 0,
    "itl_p50": 57.83,
    "output_tok_s": 569.8,
    "req_s": 2.23,
    "ttft_p50": 9390.52,
    "ttft_p99": 34261.57
  }
]
```

## Provenance

- `rig:~/benchmarks/Qwen3.6-27B`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
