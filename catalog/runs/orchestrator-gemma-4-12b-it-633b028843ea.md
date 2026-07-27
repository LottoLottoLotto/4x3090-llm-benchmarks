# `orch/gemma-4-12B-it-AWQ-INT4/vllm_AWQ-4bit_tp2x1_spec-none_c32768_pl220_aggregate/topo-tp2-pp1-dp2-i1`

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
| Layout | TP=2, DP=2 |
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
| `output_tok_s` | 2432.9 |
| `req_s` | 9.5 |
| `ttft_p50_ms` | 576.98 |
| `ttft_p99_ms` | 845.14 |
| `itl_p50_ms` | 49.7 |
| `e2e_p99_ms` | 13624.86 |
| `vram_peak_mib` | 89184 |
| `avg_power_w` | 849.6 |
| `max_temp_c` | 75.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/gemma-4-12B-it-AWQ-INT4' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 2 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 256 --enable-chunked-prefill
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
    "e2e_p99": 3140.63,
    "errors": 0,
    "itl_p50": 11.14,
    "output_tok_s": 87.6,
    "req_s": 0.34,
    "ttft_p50": 39.12,
    "ttft_p99": 261.27
  },
  {
    "concurrency": 2,
    "e2e_p99": 2910.3,
    "errors": 0,
    "itl_p50": 11.18,
    "output_tok_s": 176.7,
    "req_s": 0.69,
    "ttft_p50": 42.67,
    "ttft_p99": 65.84
  },
  {
    "concurrency": 4,
    "e2e_p99": 3167.11,
    "errors": 0,
    "itl_p50": 12.01,
    "output_tok_s": 327.2,
    "req_s": 1.28,
    "ttft_p50": 54.51,
    "ttft_p99": 75.1
  },
  {
    "concurrency": 8,
    "e2e_p99": 3800.16,
    "errors": 0,
    "itl_p50": 12.9,
    "output_tok_s": 594.2,
    "req_s": 2.32,
    "ttft_p50": 60.28,
    "ttft_p99": 127.1
  },
  {
    "concurrency": 16,
    "e2e_p99": 4349.75,
    "errors": 0,
    "itl_p50": 16.08,
    "output_tok_s": 961.7,
    "req_s": 3.76,
    "ttft_p50": 85.72,
    "ttft_p99": 193.56
  },
  {
    "concurrency": 32,
    "e2e_p99": 6311.78,
    "errors": 0,
    "itl_p50": 23.61,
    "output_tok_s": 1316.5,
    "req_s": 5.14,
    "ttft_p50": 118.0,
    "ttft_p99": 293.2
  },
  {
    "concurrency": 64,
    "e2e_p99": 8298.55,
    "errors": 0,
    "itl_p50": 30.1,
    "output_tok_s": 2009.3,
    "req_s": 7.85,
    "ttft_p50": 230.09,
    "ttft_p99": 548.82
  },
  {
    "concurrency": 96,
    "e2e_p99": 10690.38,
    "errors": 0,
    "itl_p50": 38.95,
    "output_tok_s": 2324.1,
    "req_s": 9.08,
    "ttft_p50": 438.43,
    "ttft_p99": 712.31
  },
  {
    "concurrency": 128,
    "e2e_p99": 13624.86,
    "errors": 0,
    "itl_p50": 49.7,
    "output_tok_s": 2432.9,
    "req_s": 9.5,
    "ttft_p50": 576.98,
    "ttft_p99": 845.14
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-AWQ-INT4`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
