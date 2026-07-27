# `orch/Qwen3.6-27B/vllm_FP8-static_tp2x1_spec-none_c32768_pl220_aggregate`

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
| Layout | TP=2 |
| Context | 32768 |
| Concurrency | 32 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 356.5 |
| `req_s` | 1.39 |
| `ttft_p50_ms` | 4572.61 |
| `ttft_p99_ms` | 10915.57 |
| `itl_p50_ms` | 47.49 |
| `e2e_p99_ms` | 29241.56 |
| `vram_peak_mib` | 84960 |
| `avg_power_w` | 492.9 |
| `max_temp_c` | 72.0 |

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
    "e2e_p99": 7074.58,
    "errors": 0,
    "itl_p50": 26.01,
    "output_tok_s": 36.4,
    "req_s": 0.14,
    "ttft_p50": 365.22,
    "ttft_p99": 375.13
  },
  {
    "concurrency": 2,
    "e2e_p99": 8346.53,
    "errors": 0,
    "itl_p50": 27.32,
    "output_tok_s": 65.0,
    "req_s": 0.25,
    "ttft_p50": 734.34,
    "ttft_p99": 1428.58
  },
  {
    "concurrency": 4,
    "e2e_p99": 8929.01,
    "errors": 0,
    "itl_p50": 28.47,
    "output_tok_s": 117.4,
    "req_s": 0.46,
    "ttft_p50": 1390.85,
    "ttft_p99": 1673.33
  },
  {
    "concurrency": 8,
    "e2e_p99": 11506.83,
    "errors": 0,
    "itl_p50": 32.08,
    "output_tok_s": 186.8,
    "req_s": 0.73,
    "ttft_p50": 2373.47,
    "ttft_p99": 3041.32
  },
  {
    "concurrency": 16,
    "e2e_p99": 17045.42,
    "errors": 0,
    "itl_p50": 37.15,
    "output_tok_s": 243.7,
    "req_s": 0.95,
    "ttft_p50": 3249.5,
    "ttft_p99": 5619.0
  },
  {
    "concurrency": 32,
    "e2e_p99": 29241.56,
    "errors": 0,
    "itl_p50": 47.49,
    "output_tok_s": 356.5,
    "req_s": 1.39,
    "ttft_p50": 4572.61,
    "ttft_p99": 10915.57
  },
  {
    "concurrency": 64,
    "e2e_p99": 55080.97,
    "errors": 0,
    "itl_p50": 58.38,
    "output_tok_s": 347.9,
    "req_s": 1.36,
    "ttft_p50": 10819.21,
    "ttft_p99": 36865.16
  }
]
```

## Provenance

- `rig:~/benchmarks/Qwen3.6-27B`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
