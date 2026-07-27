# `orch/gemma-4-12B-it-FP8-Dynamic/vllm_FP8_tp1x4_spec-none_c32768_pl300_aggregate`

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
| Layout | TP=1, INSTANCES=4 |
| Context | 32768 |
| Concurrency | 128 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 300 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 3811.0 |
| `req_s` | 14.89 |
| `ttft_p50_ms` | 365.14 |
| `ttft_p99_ms` | 491.04 |
| `itl_p50_ms` | 31.55 |
| `e2e_p99_ms` | 8883.02 |
| `vram_peak_mib` | 88320 |
| `avg_power_w` | 1090.2 |
| `max_temp_c` | 82.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/gemma-4-12B-it-FP8-Dynamic' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 1 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 256 --enable-chunked-prefill
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
    "e2e_p99": 5380.99,
    "errors": 0,
    "itl_p50": 19.84,
    "output_tok_s": 48.7,
    "req_s": 0.19,
    "ttft_p50": 207.38,
    "ttft_p99": 345.43
  },
  {
    "concurrency": 2,
    "e2e_p99": 5245.43,
    "errors": 0,
    "itl_p50": 19.86,
    "output_tok_s": 99.2,
    "req_s": 0.39,
    "ttft_p50": 63.67,
    "ttft_p99": 86.48
  },
  {
    "concurrency": 4,
    "e2e_p99": 5165.61,
    "errors": 0,
    "itl_p50": 19.87,
    "output_tok_s": 199.3,
    "req_s": 0.78,
    "ttft_p50": 57.64,
    "ttft_p99": 72.06
  },
  {
    "concurrency": 8,
    "e2e_p99": 5280.42,
    "errors": 0,
    "itl_p50": 20.19,
    "output_tok_s": 391.2,
    "req_s": 1.53,
    "ttft_p50": 66.84,
    "ttft_p99": 88.71
  },
  {
    "concurrency": 16,
    "e2e_p99": 5548.97,
    "errors": 0,
    "itl_p50": 21.01,
    "output_tok_s": 745.7,
    "req_s": 2.91,
    "ttft_p50": 88.54,
    "ttft_p99": 111.62
  },
  {
    "concurrency": 32,
    "e2e_p99": 6301.63,
    "errors": 0,
    "itl_p50": 22.6,
    "output_tok_s": 1310.4,
    "req_s": 5.12,
    "ttft_p50": 141.71,
    "ttft_p99": 377.07
  },
  {
    "concurrency": 64,
    "e2e_p99": 7009.93,
    "errors": 0,
    "itl_p50": 26.07,
    "output_tok_s": 2375.4,
    "req_s": 9.28,
    "ttft_p50": 213.7,
    "ttft_p99": 309.75
  },
  {
    "concurrency": 96,
    "e2e_p99": 7940.41,
    "errors": 0,
    "itl_p50": 28.96,
    "output_tok_s": 3167.4,
    "req_s": 12.37,
    "ttft_p50": 303.88,
    "ttft_p99": 363.97
  },
  {
    "concurrency": 128,
    "e2e_p99": 8883.02,
    "errors": 0,
    "itl_p50": 31.55,
    "output_tok_s": 3811.0,
    "req_s": 14.89,
    "ttft_p50": 365.14,
    "ttft_p99": 491.04
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-FP8-Dynamic`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
