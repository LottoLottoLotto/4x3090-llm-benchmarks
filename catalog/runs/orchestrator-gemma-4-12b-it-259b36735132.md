# `orch/gemma-4-12B-it-FP8-Dynamic/vllm_FP8_tp2x1_spec-none_c32768_pl220_aggregate`

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
| Layout | TP=2 |
| Context | 32768 |
| Concurrency | 96 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 1299.2 |
| `req_s` | 5.07 |
| `ttft_p50_ms` | 668.67 |
| `ttft_p99_ms` | 1038.17 |
| `itl_p50_ms` | 70.68 |
| `e2e_p99_ms` | 19131.34 |
| `vram_peak_mib` | 89424 |
| `avg_power_w` | 492.3 |
| `max_temp_c` | 72.0 |

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
    "e2e_p99": 3935.25,
    "errors": 0,
    "itl_p50": 14.44,
    "output_tok_s": 68.1,
    "req_s": 0.27,
    "ttft_p50": 37.48,
    "ttft_p99": 222.59
  },
  {
    "concurrency": 2,
    "e2e_p99": 3937.59,
    "errors": 0,
    "itl_p50": 15.06,
    "output_tok_s": 130.8,
    "req_s": 0.51,
    "ttft_p50": 54.95,
    "ttft_p99": 64.31
  },
  {
    "concurrency": 4,
    "e2e_p99": 4302.97,
    "errors": 0,
    "itl_p50": 16.41,
    "output_tok_s": 240.9,
    "req_s": 0.94,
    "ttft_p50": 71.78,
    "ttft_p99": 99.64
  },
  {
    "concurrency": 8,
    "e2e_p99": 5027.96,
    "errors": 0,
    "itl_p50": 18.48,
    "output_tok_s": 421.3,
    "req_s": 1.65,
    "ttft_p50": 82.8,
    "ttft_p99": 258.87
  },
  {
    "concurrency": 16,
    "e2e_p99": 6530.69,
    "errors": 0,
    "itl_p50": 23.41,
    "output_tok_s": 654.9,
    "req_s": 2.56,
    "ttft_p50": 163.29,
    "ttft_p99": 464.45
  },
  {
    "concurrency": 32,
    "e2e_p99": 8211.15,
    "errors": 0,
    "itl_p50": 30.36,
    "output_tok_s": 1007.4,
    "req_s": 3.94,
    "ttft_p50": 312.18,
    "ttft_p99": 378.16
  },
  {
    "concurrency": 64,
    "e2e_p99": 12923.71,
    "errors": 0,
    "itl_p50": 47.84,
    "output_tok_s": 1283.2,
    "req_s": 5.01,
    "ttft_p50": 480.76,
    "ttft_p99": 677.14
  },
  {
    "concurrency": 96,
    "e2e_p99": 19131.34,
    "errors": 0,
    "itl_p50": 70.68,
    "output_tok_s": 1299.2,
    "req_s": 5.07,
    "ttft_p50": 668.67,
    "ttft_p99": 1038.17
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-FP8-Dynamic`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
