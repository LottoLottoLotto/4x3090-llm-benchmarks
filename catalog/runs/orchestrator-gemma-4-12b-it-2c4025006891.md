# `orch/gemma-4-12B-it-AWQ-INT4/vllm_AWQ-4bit_tp1x4_spec-none_c32768_pl250_aggregate`

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
| Layout | TP=1, INSTANCES=4 |
| Context | 32768 |
| Concurrency | 128 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 250 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 3858.2 |
| `req_s` | 15.07 |
| `ttft_p50_ms` | 375.64 |
| `ttft_p99_ms` | 460.1 |
| `itl_p50_ms` | 31.14 |
| `e2e_p99_ms` | 8881.63 |
| `vram_peak_mib` | 88680 |
| `avg_power_w` | 922.4 |
| `max_temp_c` | 77.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/gemma-4-12B-it-AWQ-INT4' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 1 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 256 --enable-chunked-prefill
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
    "e2e_p99": 4046.13,
    "errors": 0,
    "itl_p50": 14.5,
    "output_tok_s": 66.1,
    "req_s": 0.26,
    "ttft_p50": 206.04,
    "ttft_p99": 302.7
  },
  {
    "concurrency": 2,
    "e2e_p99": 3865.55,
    "errors": 0,
    "itl_p50": 14.53,
    "output_tok_s": 135.6,
    "req_s": 0.53,
    "ttft_p50": 45.49,
    "ttft_p99": 49.28
  },
  {
    "concurrency": 4,
    "e2e_p99": 3851.92,
    "errors": 0,
    "itl_p50": 14.58,
    "output_tok_s": 268.6,
    "req_s": 1.05,
    "ttft_p50": 47.15,
    "ttft_p99": 76.14
  },
  {
    "concurrency": 8,
    "e2e_p99": 4016.41,
    "errors": 0,
    "itl_p50": 15.06,
    "output_tok_s": 521.4,
    "req_s": 2.04,
    "ttft_p50": 62.54,
    "ttft_p99": 80.86
  },
  {
    "concurrency": 16,
    "e2e_p99": 4284.07,
    "errors": 0,
    "itl_p50": 15.92,
    "output_tok_s": 976.2,
    "req_s": 3.81,
    "ttft_p50": 86.81,
    "ttft_p99": 108.26
  },
  {
    "concurrency": 32,
    "e2e_p99": 5048.32,
    "errors": 0,
    "itl_p50": 17.66,
    "output_tok_s": 1735.8,
    "req_s": 6.78,
    "ttft_p50": 141.91,
    "ttft_p99": 417.99
  },
  {
    "concurrency": 64,
    "e2e_p99": 6388.48,
    "errors": 0,
    "itl_p50": 22.07,
    "output_tok_s": 2527.8,
    "req_s": 9.87,
    "ttft_p50": 217.83,
    "ttft_p99": 532.54
  },
  {
    "concurrency": 96,
    "e2e_p99": 8034.46,
    "errors": 0,
    "itl_p50": 28.59,
    "output_tok_s": 2907.4,
    "req_s": 11.36,
    "ttft_p50": 302.9,
    "ttft_p99": 377.47
  },
  {
    "concurrency": 128,
    "e2e_p99": 8881.63,
    "errors": 0,
    "itl_p50": 31.14,
    "output_tok_s": 3858.2,
    "req_s": 15.07,
    "ttft_p50": 375.64,
    "ttft_p99": 460.1
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-AWQ-INT4`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
