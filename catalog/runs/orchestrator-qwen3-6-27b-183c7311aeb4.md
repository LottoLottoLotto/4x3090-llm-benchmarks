# `orch/Qwen3.6-27B/vllm_INT8-W8A8_tp2x1_spec-none_c32768_pl220_aggregate`

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
| `output_tok_s` | 435.8 |
| `req_s` | 1.7 |
| `ttft_p50_ms` | 2831.05 |
| `ttft_p99_ms` | 6772.2 |
| `itl_p50_ms` | 47.0 |
| `e2e_p99_ms` | 22609.94 |
| `vram_peak_mib` | 84992 |
| `avg_power_w` | 493.1 |
| `max_temp_c` | 72.0 |

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
    "e2e_p99": 7148.94,
    "errors": 0,
    "itl_p50": 26.75,
    "output_tok_s": 36.1,
    "req_s": 0.14,
    "ttft_p50": 245.65,
    "ttft_p99": 253.51
  },
  {
    "concurrency": 2,
    "e2e_p99": 8208.74,
    "errors": 0,
    "itl_p50": 27.48,
    "output_tok_s": 66.6,
    "req_s": 0.26,
    "ttft_p50": 474.22,
    "ttft_p99": 1196.2
  },
  {
    "concurrency": 4,
    "e2e_p99": 8659.73,
    "errors": 0,
    "itl_p50": 29.06,
    "output_tok_s": 121.8,
    "req_s": 0.48,
    "ttft_p50": 881.8,
    "ttft_p99": 1220.41
  },
  {
    "concurrency": 8,
    "e2e_p99": 10555.17,
    "errors": 0,
    "itl_p50": 32.72,
    "output_tok_s": 202.5,
    "req_s": 0.79,
    "ttft_p50": 1471.71,
    "ttft_p99": 2030.37
  },
  {
    "concurrency": 16,
    "e2e_p99": 14174.1,
    "errors": 0,
    "itl_p50": 38.26,
    "output_tok_s": 312.2,
    "req_s": 1.22,
    "ttft_p50": 2123.33,
    "ttft_p99": 3457.69
  },
  {
    "concurrency": 32,
    "e2e_p99": 22609.94,
    "errors": 0,
    "itl_p50": 47.0,
    "output_tok_s": 435.8,
    "req_s": 1.7,
    "ttft_p50": 2831.05,
    "ttft_p99": 6772.2
  },
  {
    "concurrency": 64,
    "e2e_p99": 48858.68,
    "errors": 0,
    "itl_p50": 56.33,
    "output_tok_s": 426.5,
    "req_s": 1.67,
    "ttft_p50": 8346.87,
    "ttft_p99": 28436.35
  }
]
```

## Provenance

- `rig:~/benchmarks/Qwen3.6-27B`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
