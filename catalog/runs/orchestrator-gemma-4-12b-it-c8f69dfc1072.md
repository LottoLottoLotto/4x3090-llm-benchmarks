# `orch/gemma-4-12B-it-AWQ-INT4/vllm_AWQ-4bit_tp1x1_spec-none_c32768_pl220_aggregate/topo-tp1-pp4-dp1-i1`

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
| Layout | TP=1, PP=4 |
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
| `output_tok_s` | 1427.8 |
| `req_s` | 5.58 |
| `ttft_p50_ms` | 737.55 |
| `ttft_p99_ms` | 996.36 |
| `itl_p50_ms` | 64.09 |
| `e2e_p99_ms` | 17332.31 |
| `vram_peak_mib` | 89768 |
| `avg_power_w` | 836.3 |
| `max_temp_c` | 75.0 |

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
    "e2e_p99": 3457.71,
    "errors": 0,
    "itl_p50": 12.61,
    "output_tok_s": 77.7,
    "req_s": 0.3,
    "ttft_p50": 59.36,
    "ttft_p99": 247.9
  },
  {
    "concurrency": 2,
    "e2e_p99": 3469.99,
    "errors": 0,
    "itl_p50": 12.94,
    "output_tok_s": 151.1,
    "req_s": 0.59,
    "ttft_p50": 73.31,
    "ttft_p99": 141.23
  },
  {
    "concurrency": 4,
    "e2e_p99": 3597.67,
    "errors": 0,
    "itl_p50": 13.64,
    "output_tok_s": 286.4,
    "req_s": 1.12,
    "ttft_p50": 89.72,
    "ttft_p99": 115.37
  },
  {
    "concurrency": 8,
    "e2e_p99": 4612.08,
    "errors": 0,
    "itl_p50": 15.01,
    "output_tok_s": 506.4,
    "req_s": 1.98,
    "ttft_p50": 121.73,
    "ttft_p99": 769.75
  },
  {
    "concurrency": 16,
    "e2e_p99": 4899.46,
    "errors": 0,
    "itl_p50": 18.31,
    "output_tok_s": 843.3,
    "req_s": 3.29,
    "ttft_p50": 169.4,
    "ttft_p99": 229.97
  },
  {
    "concurrency": 32,
    "e2e_p99": 6776.47,
    "errors": 0,
    "itl_p50": 25.13,
    "output_tok_s": 1217.0,
    "req_s": 4.75,
    "ttft_p50": 274.39,
    "ttft_p99": 351.64
  },
  {
    "concurrency": 64,
    "e2e_p99": 11741.6,
    "errors": 0,
    "itl_p50": 43.23,
    "output_tok_s": 1413.0,
    "req_s": 5.52,
    "ttft_p50": 403.5,
    "ttft_p99": 673.89
  },
  {
    "concurrency": 96,
    "e2e_p99": 17332.31,
    "errors": 0,
    "itl_p50": 64.09,
    "output_tok_s": 1427.8,
    "req_s": 5.58,
    "ttft_p50": 737.55,
    "ttft_p99": 996.36
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-AWQ-INT4`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
