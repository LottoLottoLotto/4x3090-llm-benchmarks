# `orch/gemma-4-12B-it-AWQ-INT4/vllm_AWQ-4bit_tp1x4_spec-none_c32768_pl270_aggregate`

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
| Power limit | 270 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 4001.3 |
| `req_s` | 15.63 |
| `ttft_p50_ms` | 392.63 |
| `ttft_p99_ms` | 545.16 |
| `itl_p50_ms` | 30.12 |
| `e2e_p99_ms` | 8645.19 |
| `vram_peak_mib` | 88680 |
| `avg_power_w` | 995.4 |
| `max_temp_c` | 79.0 |

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
    "e2e_p99": 3930.86,
    "errors": 0,
    "itl_p50": 14.19,
    "output_tok_s": 67.7,
    "req_s": 0.26,
    "ttft_p50": 198.03,
    "ttft_p99": 330.19
  },
  {
    "concurrency": 2,
    "e2e_p99": 3690.45,
    "errors": 0,
    "itl_p50": 14.21,
    "output_tok_s": 139.7,
    "req_s": 0.55,
    "ttft_p50": 45.58,
    "ttft_p99": 47.89
  },
  {
    "concurrency": 4,
    "e2e_p99": 3742.21,
    "errors": 0,
    "itl_p50": 14.25,
    "output_tok_s": 277.0,
    "req_s": 1.08,
    "ttft_p50": 47.42,
    "ttft_p99": 79.48
  },
  {
    "concurrency": 8,
    "e2e_p99": 3857.34,
    "errors": 0,
    "itl_p50": 14.6,
    "output_tok_s": 537.4,
    "req_s": 2.1,
    "ttft_p50": 62.99,
    "ttft_p99": 85.88
  },
  {
    "concurrency": 16,
    "e2e_p99": 4125.09,
    "errors": 0,
    "itl_p50": 15.48,
    "output_tok_s": 1010.0,
    "req_s": 3.95,
    "ttft_p50": 79.97,
    "ttft_p99": 120.97
  },
  {
    "concurrency": 32,
    "e2e_p99": 4825.26,
    "errors": 0,
    "itl_p50": 17.11,
    "output_tok_s": 1791.6,
    "req_s": 7.0,
    "ttft_p50": 132.58,
    "ttft_p99": 429.65
  },
  {
    "concurrency": 64,
    "e2e_p99": 6047.57,
    "errors": 0,
    "itl_p50": 21.3,
    "output_tok_s": 2833.9,
    "req_s": 11.07,
    "ttft_p50": 205.25,
    "ttft_p99": 559.6
  },
  {
    "concurrency": 96,
    "e2e_p99": 7542.88,
    "errors": 0,
    "itl_p50": 27.51,
    "output_tok_s": 3340.8,
    "req_s": 13.05,
    "ttft_p50": 280.02,
    "ttft_p99": 367.26
  },
  {
    "concurrency": 128,
    "e2e_p99": 8645.19,
    "errors": 0,
    "itl_p50": 30.12,
    "output_tok_s": 4001.3,
    "req_s": 15.63,
    "ttft_p50": 392.63,
    "ttft_p99": 545.16
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-AWQ-INT4`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
