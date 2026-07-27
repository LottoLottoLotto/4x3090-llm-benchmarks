# `orch/gemma-4-12B-it-AWQ-INT4/vllm_AWQ-4bit_tp1x4_spec-none_c32768_pl220_aggregate`

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
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 3424.9 |
| `req_s` | 13.38 |
| `ttft_p50_ms` | 411.06 |
| `ttft_p99_ms` | 523.21 |
| `itl_p50_ms` | 34.67 |
| `e2e_p99_ms` | 10213.06 |
| `vram_peak_mib` | 88680 |
| `avg_power_w` | 816.1 |
| `max_temp_c` | 74.0 |

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
    "e2e_p99": 5002.49,
    "errors": 0,
    "itl_p50": 17.68,
    "output_tok_s": 54.1,
    "req_s": 0.21,
    "ttft_p50": 242.66,
    "ttft_p99": 346.82
  },
  {
    "concurrency": 2,
    "e2e_p99": 4820.99,
    "errors": 0,
    "itl_p50": 17.8,
    "output_tok_s": 110.4,
    "req_s": 0.43,
    "ttft_p50": 47.23,
    "ttft_p99": 76.78
  },
  {
    "concurrency": 4,
    "e2e_p99": 4983.5,
    "errors": 0,
    "itl_p50": 18.41,
    "output_tok_s": 216.6,
    "req_s": 0.85,
    "ttft_p50": 51.28,
    "ttft_p99": 77.53
  },
  {
    "concurrency": 8,
    "e2e_p99": 4960.33,
    "errors": 0,
    "itl_p50": 18.25,
    "output_tok_s": 431.9,
    "req_s": 1.69,
    "ttft_p50": 69.59,
    "ttft_p99": 90.66
  },
  {
    "concurrency": 16,
    "e2e_p99": 5133.18,
    "errors": 0,
    "itl_p50": 18.77,
    "output_tok_s": 827.7,
    "req_s": 3.23,
    "ttft_p50": 95.23,
    "ttft_p99": 121.74
  },
  {
    "concurrency": 32,
    "e2e_p99": 5964.2,
    "errors": 0,
    "itl_p50": 20.1,
    "output_tok_s": 1497.9,
    "req_s": 5.85,
    "ttft_p50": 152.9,
    "ttft_p99": 418.57
  },
  {
    "concurrency": 64,
    "e2e_p99": 7620.16,
    "errors": 0,
    "itl_p50": 25.55,
    "output_tok_s": 2335.7,
    "req_s": 9.12,
    "ttft_p50": 242.35,
    "ttft_p99": 529.91
  },
  {
    "concurrency": 96,
    "e2e_p99": 9213.85,
    "errors": 0,
    "itl_p50": 31.75,
    "output_tok_s": 2823.8,
    "req_s": 11.03,
    "ttft_p50": 332.77,
    "ttft_p99": 414.63
  },
  {
    "concurrency": 128,
    "e2e_p99": 10213.06,
    "errors": 0,
    "itl_p50": 34.67,
    "output_tok_s": 3424.9,
    "req_s": 13.38,
    "ttft_p50": 411.06,
    "ttft_p99": 523.21
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-AWQ-INT4`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
