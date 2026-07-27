# `orch/gemma-4-12B-it-AWQ-INT4/vllm_AWQ-4bit_tp1x1_spec-none_c32768_pl220_aggregate/topo-tp1-pp1-dp4-i1`

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
| Layout | TP=1, DP=4 |
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
| `output_tok_s` | 3308.4 |
| `req_s` | 12.92 |
| `ttft_p50_ms` | 177.71 |
| `ttft_p99_ms` | 503.99 |
| `itl_p50_ms` | 34.05 |
| `e2e_p99_ms` | 11422.74 |
| `vram_peak_mib` | 89064 |
| `avg_power_w` | 784.3 |
| `max_temp_c` | 74.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/gemma-4-12B-it-AWQ-INT4' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 1 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 256 --enable-chunked-prefill
```

## Engine knobs

```json
{
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
    "e2e_p99": 7087.26,
    "errors": 0,
    "itl_p50": 17.04,
    "output_tok_s": 48.4,
    "req_s": 0.19,
    "ttft_p50": 36.11,
    "ttft_p99": 2120.12
  },
  {
    "concurrency": 2,
    "e2e_p99": 4853.4,
    "errors": 0,
    "itl_p50": 17.62,
    "output_tok_s": 111.6,
    "req_s": 0.44,
    "ttft_p50": 36.68,
    "ttft_p99": 293.28
  },
  {
    "concurrency": 4,
    "e2e_p99": 4930.21,
    "errors": 0,
    "itl_p50": 17.41,
    "output_tok_s": 220.5,
    "req_s": 0.86,
    "ttft_p50": 44.15,
    "ttft_p99": 78.76
  },
  {
    "concurrency": 8,
    "e2e_p99": 5003.09,
    "errors": 0,
    "itl_p50": 17.95,
    "output_tok_s": 423.6,
    "req_s": 1.65,
    "ttft_p50": 66.48,
    "ttft_p99": 95.41
  },
  {
    "concurrency": 16,
    "e2e_p99": 5143.39,
    "errors": 0,
    "itl_p50": 18.85,
    "output_tok_s": 798.2,
    "req_s": 3.12,
    "ttft_p50": 70.0,
    "ttft_p99": 200.82
  },
  {
    "concurrency": 32,
    "e2e_p99": 6416.18,
    "errors": 0,
    "itl_p50": 20.7,
    "output_tok_s": 1407.6,
    "req_s": 5.5,
    "ttft_p50": 85.06,
    "ttft_p99": 178.5
  },
  {
    "concurrency": 64,
    "e2e_p99": 8366.47,
    "errors": 0,
    "itl_p50": 26.18,
    "output_tok_s": 2209.9,
    "req_s": 8.63,
    "ttft_p50": 100.82,
    "ttft_p99": 391.48
  },
  {
    "concurrency": 96,
    "e2e_p99": 8868.56,
    "errors": 0,
    "itl_p50": 31.62,
    "output_tok_s": 2866.3,
    "req_s": 11.2,
    "ttft_p50": 127.68,
    "ttft_p99": 455.82
  },
  {
    "concurrency": 128,
    "e2e_p99": 11422.74,
    "errors": 0,
    "itl_p50": 34.05,
    "output_tok_s": 3308.4,
    "req_s": 12.92,
    "ttft_p50": 177.71,
    "ttft_p99": 503.99
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-AWQ-INT4`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
