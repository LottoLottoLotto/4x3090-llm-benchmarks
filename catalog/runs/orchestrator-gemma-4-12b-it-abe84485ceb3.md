# `orch/gemma-4-12B-it-AWQ-INT4/vllm_AWQ-4bit_tp1x4_spec-ngram_c32768_pl220_aggregate`

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
| `output_tok_s` | 2637.2 |
| `req_s` | 10.3 |
| `ttft_p50_ms` | 250.86 |
| `ttft_p99_ms` | 456.14 |
| `itl_p50_ms` | 42.31 |
| `e2e_p99_ms` | 13282.25 |
| `vram_peak_mib` | 88728 |
| `avg_power_w` | 805.0 |
| `max_temp_c` | 74.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/gemma-4-12B-it-AWQ-INT4' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 1 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 256 --enable-chunked-prefill --speculative-config '{"method": "ngram", "num_speculative_tokens": 5, "prompt_lookup_max": 4, "prompt_lookup_min": 2}'
```

## Speculative decoding

```json
{
  "draft_path": null,
  "draft_ref": null,
  "k": null,
  "method": "ngram"
}
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
    "e2e_p99": 6117.89,
    "errors": 0,
    "itl_p50": 18.0,
    "output_tok_s": 47.5,
    "req_s": 0.19,
    "ttft_p50": 222.29,
    "ttft_p99": 1598.72
  },
  {
    "concurrency": 2,
    "e2e_p99": 4656.46,
    "errors": 0,
    "itl_p50": 18.14,
    "output_tok_s": 113.2,
    "req_s": 0.44,
    "ttft_p50": 35.49,
    "ttft_p99": 71.17
  },
  {
    "concurrency": 4,
    "e2e_p99": 6475.21,
    "errors": 0,
    "itl_p50": 18.37,
    "output_tok_s": 211.3,
    "req_s": 0.83,
    "ttft_p50": 41.64,
    "ttft_p99": 67.08
  },
  {
    "concurrency": 8,
    "e2e_p99": 4888.89,
    "errors": 0,
    "itl_p50": 18.72,
    "output_tok_s": 434.8,
    "req_s": 1.7,
    "ttft_p50": 50.98,
    "ttft_p99": 66.2
  },
  {
    "concurrency": 16,
    "e2e_p99": 5401.11,
    "errors": 0,
    "itl_p50": 19.37,
    "output_tok_s": 751.2,
    "req_s": 2.93,
    "ttft_p50": 64.96,
    "ttft_p99": 205.0
  },
  {
    "concurrency": 32,
    "e2e_p99": 9155.73,
    "errors": 0,
    "itl_p50": 22.72,
    "output_tok_s": 1233.0,
    "req_s": 4.82,
    "ttft_p50": 122.96,
    "ttft_p99": 431.1
  },
  {
    "concurrency": 64,
    "e2e_p99": 8972.71,
    "errors": 0,
    "itl_p50": 31.57,
    "output_tok_s": 1897.3,
    "req_s": 7.41,
    "ttft_p50": 141.31,
    "ttft_p99": 492.71
  },
  {
    "concurrency": 96,
    "e2e_p99": 10785.55,
    "errors": 0,
    "itl_p50": 34.11,
    "output_tok_s": 2325.7,
    "req_s": 9.08,
    "ttft_p50": 197.54,
    "ttft_p99": 340.1
  },
  {
    "concurrency": 128,
    "e2e_p99": 13282.25,
    "errors": 0,
    "itl_p50": 42.31,
    "output_tok_s": 2637.2,
    "req_s": 10.3,
    "ttft_p50": 250.86,
    "ttft_p99": 456.14
  }
]
```

## Provenance

- `rig:~/benchmarks/gemma-4-12B-it-AWQ-INT4`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
