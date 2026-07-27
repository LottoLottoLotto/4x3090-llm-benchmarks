# `orch/gemma-4-12B-it-FP8-Dynamic/vllm_FP8_tp2x2_spec-none_c32768_pl220_aggregate`

| field | value |
|---|---|
| Date | 2026-06-21 |
| Campaign | orchestrator |
| Model | Gemma-4-12B-it |
| Checkpoint | gemma-4-12B-it-FP8-Dynamic |
| Quant | fp8-dynamic |
| Quant method | fp8 |
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
| `output_tok_s` | 2266.4 |
| `req_s` | 8.85 |
| `ttft_p50_ms` | 605.16 |
| `ttft_p99_ms` | 839.56 |
| `itl_p50_ms` | 52.85 |
| `e2e_p99_ms` | 15018.84 |
| `vram_peak_mib` | 89168 |
| `avg_power_w` | 853.6 |
| `max_temp_c` | 74.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/gemma-4-12B-it-FP8-Dynamic' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 2 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 256 --enable-chunked-prefill
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
    "e2e_p99": 4160.68,
    "errors": 0,
    "itl_p50": 14.32,
    "output_tok_s": 67.3,
    "req_s": 0.26,
    "ttft_p50": 46.44,
    "ttft_p99": 448.44
  },
  {
    "concurrency": 2,
    "e2e_p99": 3835.49,
    "errors": 0,
    "itl_p50": 14.4,
    "output_tok_s": 136.8,
    "req_s": 0.53,
    "ttft_p50": 42.11,
    "ttft_p99": 66.01
  },
  {
    "concurrency": 4,
    "e2e_p99": 3955.73,
    "errors": 0,
    "itl_p50": 14.94,
    "output_tok_s": 263.0,
    "req_s": 1.03,
    "ttft_p50": 56.75,
    "ttft_p99": 85.7
  },
  {
    "concurrency": 8,
    "e2e_p99": 4372.09,
    "errors": 0,
    "itl_p50": 16.24,
    "output_tok_s": 456.4,
    "req_s": 1.78,
    "ttft_p50": 76.76,
    "ttft_p99": 122.52
  },
  {
    "concurrency": 16,
    "e2e_p99": 5554.52,
    "errors": 0,
    "itl_p50": 19.56,
    "output_tok_s": 777.1,
    "req_s": 3.04,
    "ttft_p50": 137.36,
    "ttft_p99": 449.87
  },
  {
    "concurrency": 32,
    "e2e_p99": 7561.03,
    "errors": 0,
    "itl_p50": 27.71,
    "output_tok_s": 1114.6,
    "req_s": 4.35,
    "ttft_p50": 210.83,
    "ttft_p99": 273.96
  },
  {
    "concurrency": 64,
    "e2e_p99": 9302.18,
    "errors": 0,
    "itl_p50": 32.74,
    "output_tok_s": 1831.9,
    "req_s": 7.16,
    "ttft_p50": 395.13,
    "ttft_p99": 562.88
  },
  {
    "concurrency": 96,
    "e2e_p99": 11668.56,
    "errors": 0,
    "itl_p50": 41.89,
    "output_tok_s": 2135.6,
    "req_s": 8.34,
    "ttft_p50": 583.77,
    "ttft_p99": 894.9
  },
  {
    "concurrency": 128,
    "e2e_p99": 15018.84,
    "errors": 0,
    "itl_p50": 52.85,
    "output_tok_s": 2266.4,
    "req_s": 8.85,
    "ttft_p50": 605.16,
    "ttft_p99": 839.56
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-FP8-Dynamic`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
