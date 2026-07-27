# `orch/gemma-4-12B-it-AWQ-INT4/vllm_AWQ-4bit_tp1x1_spec-none_c32768_pl220_aggregate/topo-tp1-pp1-dp1-i1`

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
| Layout | TP=1 |
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
| `output_tok_s` | 1180.6 |
| `req_s` | 4.61 |
| `ttft_p50_ms` | 1242.69 |
| `ttft_p99_ms` | 1289.46 |
| `itl_p50_ms` | 104.26 |
| `e2e_p99_ms` | 27898.15 |
| `vram_peak_mib` | 88680 |
| `avg_power_w` | 302.6 |
| `max_temp_c` | 72.0 |

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
    "e2e_p99": 4942.6,
    "errors": 0,
    "itl_p50": 18.69,
    "output_tok_s": 53.1,
    "req_s": 0.21,
    "ttft_p50": 51.68,
    "ttft_p99": 231.39
  },
  {
    "concurrency": 2,
    "e2e_p99": 4796.81,
    "errors": 0,
    "itl_p50": 18.51,
    "output_tok_s": 107.3,
    "req_s": 0.42,
    "ttft_p50": 60.49,
    "ttft_p99": 77.01
  },
  {
    "concurrency": 4,
    "e2e_p99": 4971.88,
    "errors": 0,
    "itl_p50": 19.13,
    "output_tok_s": 206.4,
    "req_s": 0.81,
    "ttft_p50": 91.8,
    "ttft_p99": 102.48
  },
  {
    "concurrency": 8,
    "e2e_p99": 5531.75,
    "errors": 0,
    "itl_p50": 20.4,
    "output_tok_s": 380.6,
    "req_s": 1.49,
    "ttft_p50": 137.87,
    "ttft_p99": 271.61
  },
  {
    "concurrency": 16,
    "e2e_p99": 7122.38,
    "errors": 0,
    "itl_p50": 25.63,
    "output_tok_s": 590.8,
    "req_s": 2.31,
    "ttft_p50": 192.29,
    "ttft_p99": 466.15
  },
  {
    "concurrency": 32,
    "e2e_p99": 9359.52,
    "errors": 0,
    "itl_p50": 34.96,
    "output_tok_s": 879.7,
    "req_s": 3.44,
    "ttft_p50": 395.08,
    "ttft_p99": 421.38
  },
  {
    "concurrency": 64,
    "e2e_p99": 15256.58,
    "errors": 0,
    "itl_p50": 56.74,
    "output_tok_s": 944.2,
    "req_s": 3.69,
    "ttft_p50": 697.24,
    "ttft_p99": 766.19
  },
  {
    "concurrency": 96,
    "e2e_p99": 23386.32,
    "errors": 0,
    "itl_p50": 86.99,
    "output_tok_s": 1055.1,
    "req_s": 4.12,
    "ttft_p50": 1052.63,
    "ttft_p99": 1246.11
  },
  {
    "concurrency": 128,
    "e2e_p99": 27898.15,
    "errors": 0,
    "itl_p50": 104.26,
    "output_tok_s": 1180.6,
    "req_s": 4.61,
    "ttft_p50": 1242.69,
    "ttft_p99": 1289.46
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-AWQ-INT4`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
