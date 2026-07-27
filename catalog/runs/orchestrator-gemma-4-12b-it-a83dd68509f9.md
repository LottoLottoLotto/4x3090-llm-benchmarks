# `orch/gemma-4-12B-it-AWQ-INT4/vllm_AWQ-4bit_tp2x1_spec-none_c32768_pl220_aggregate/topo-tp2-pp1-dp1-i1`

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
| Layout | TP=2 |
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
| `output_tok_s` | 1357.2 |
| `req_s` | 5.3 |
| `ttft_p50_ms` | 686.22 |
| `ttft_p99_ms` | 1073.11 |
| `itl_p50_ms` | 67.59 |
| `e2e_p99_ms` | 18294.17 |
| `vram_peak_mib` | 88928 |
| `avg_power_w` | 492.5 |
| `max_temp_c` | 72.0 |

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
    "e2e_p99": 3082.19,
    "errors": 0,
    "itl_p50": 11.26,
    "output_tok_s": 87.6,
    "req_s": 0.34,
    "ttft_p50": 35.39,
    "ttft_p99": 217.77
  },
  {
    "concurrency": 2,
    "e2e_p99": 3107.15,
    "errors": 0,
    "itl_p50": 11.86,
    "output_tok_s": 166.3,
    "req_s": 0.65,
    "ttft_p50": 53.58,
    "ttft_p99": 68.7
  },
  {
    "concurrency": 4,
    "e2e_p99": 3609.51,
    "errors": 0,
    "itl_p50": 13.29,
    "output_tok_s": 296.2,
    "req_s": 1.16,
    "ttft_p50": 62.3,
    "ttft_p99": 190.1
  },
  {
    "concurrency": 8,
    "e2e_p99": 3974.8,
    "errors": 0,
    "itl_p50": 14.93,
    "output_tok_s": 520.8,
    "req_s": 2.03,
    "ttft_p50": 75.74,
    "ttft_p99": 120.78
  },
  {
    "concurrency": 16,
    "e2e_p99": 5529.41,
    "errors": 0,
    "itl_p50": 20.16,
    "output_tok_s": 766.6,
    "req_s": 2.99,
    "ttft_p50": 135.66,
    "ttft_p99": 339.01
  },
  {
    "concurrency": 32,
    "e2e_p99": 7853.42,
    "errors": 0,
    "itl_p50": 29.21,
    "output_tok_s": 1046.5,
    "req_s": 4.09,
    "ttft_p50": 312.42,
    "ttft_p99": 380.6
  },
  {
    "concurrency": 64,
    "e2e_p99": 12551.26,
    "errors": 0,
    "itl_p50": 46.44,
    "output_tok_s": 1317.9,
    "req_s": 5.15,
    "ttft_p50": 510.16,
    "ttft_p99": 707.79
  },
  {
    "concurrency": 96,
    "e2e_p99": 18294.17,
    "errors": 0,
    "itl_p50": 67.59,
    "output_tok_s": 1357.2,
    "req_s": 5.3,
    "ttft_p50": 686.22,
    "ttft_p99": 1073.11
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-AWQ-INT4`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
