# `orch/gemma-4-12B-it-AWQ-INT4/vllm_AWQ-4bit_tp2x2_spec-none_c32768_pl220_aggregate`

| field | value |
|---|---|
| Date | 2026-06-21 |
| Campaign | orchestrator |
| Model | Gemma-4-12B-it |
| Checkpoint | gemma-4-12B-it-AWQ-INT4 |
| Quant | awq-int4 |
| Quant method | awq |
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
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 2363.5 |
| `req_s` | 9.23 |
| `ttft_p50_ms` | 592.96 |
| `ttft_p99_ms` | 900.13 |
| `itl_p50_ms` | 50.9 |
| `e2e_p99_ms` | 14281.4 |
| `vram_peak_mib` | 88928 |
| `avg_power_w` | 852.7 |
| `max_temp_c` | 75.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/gemma-4-12B-it-AWQ-INT4' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 2 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 256 --enable-chunked-prefill
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
    "e2e_p99": 3340.2,
    "errors": 0,
    "itl_p50": 11.15,
    "output_tok_s": 86.6,
    "req_s": 0.34,
    "ttft_p50": 38.55,
    "ttft_p99": 445.55
  },
  {
    "concurrency": 2,
    "e2e_p99": 2980.23,
    "errors": 0,
    "itl_p50": 11.24,
    "output_tok_s": 175.8,
    "req_s": 0.69,
    "ttft_p50": 38.99,
    "ttft_p99": 62.08
  },
  {
    "concurrency": 4,
    "e2e_p99": 3152.12,
    "errors": 0,
    "itl_p50": 11.75,
    "output_tok_s": 332.5,
    "req_s": 1.3,
    "ttft_p50": 51.94,
    "ttft_p99": 80.11
  },
  {
    "concurrency": 8,
    "e2e_p99": 3666.43,
    "errors": 0,
    "itl_p50": 13.1,
    "output_tok_s": 582.5,
    "req_s": 2.28,
    "ttft_p50": 74.36,
    "ttft_p99": 205.35
  },
  {
    "concurrency": 16,
    "e2e_p99": 4520.24,
    "errors": 0,
    "itl_p50": 16.26,
    "output_tok_s": 931.3,
    "req_s": 3.64,
    "ttft_p50": 116.15,
    "ttft_p99": 392.88
  },
  {
    "concurrency": 32,
    "e2e_p99": 6547.9,
    "errors": 0,
    "itl_p50": 23.66,
    "output_tok_s": 1307.7,
    "req_s": 5.11,
    "ttft_p50": 195.26,
    "ttft_p99": 286.66
  },
  {
    "concurrency": 64,
    "e2e_p99": 8574.1,
    "errors": 0,
    "itl_p50": 30.82,
    "output_tok_s": 1952.9,
    "req_s": 7.63,
    "ttft_p50": 322.15,
    "ttft_p99": 544.09
  },
  {
    "concurrency": 96,
    "e2e_p99": 11318.9,
    "errors": 0,
    "itl_p50": 39.97,
    "output_tok_s": 2236.3,
    "req_s": 8.74,
    "ttft_p50": 557.19,
    "ttft_p99": 854.12
  },
  {
    "concurrency": 128,
    "e2e_p99": 14281.4,
    "errors": 0,
    "itl_p50": 50.9,
    "output_tok_s": 2363.5,
    "req_s": 9.23,
    "ttft_p50": 592.96,
    "ttft_p99": 900.13
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-AWQ-INT4`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
