# `orch/Qwen3.6-27B/vllm_FP8-static_tp2x1_spec-none_c32768_pl220_single_stream`

| field | value |
|---|---|
| Date | 2026-06-28 |
| Campaign | orchestrator |
| Model | Qwen3.6-27B |
| Checkpoint | Qwen3.6-27B-FP8 |
| Quant | fp8-static |
| Quant method | fp8 |
| Engine | vllm |
| Engine version | 0.23.0 |
| Objective | single_stream |
| TPS kind | single_stream_wall |
| Layout | TP=2 |
| Context | 32768 |
| Concurrency | 1 |
| Prompt tokens | 512 |
| Generated tokens | 256 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 35.8 |
| `req_s` | 0.14 |
| `ttft_p50_ms` | 367.97 |
| `ttft_p99_ms` | 390.43 |
| `itl_p50_ms` | 26.54 |
| `e2e_p99_ms` | 7238.62 |
| `vram_peak_mib` | 82992 |
| `avg_power_w` | 494.1 |
| `max_temp_c` | 71.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/Qwen3.6-27B-FP8' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 2 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 1
```

## Engine knobs

```json
{
  "_env_VLLM_ATTENTION_BACKEND": "FLASH_ATTN",
  "_env_VLLM_USE_FLASHINFER_SAMPLER": "0",
  "enforce_eager": false,
  "gpu_memory_utilization": 0.9,
  "kv_cache_dtype": "auto",
  "max_num_seqs": 1,
  "trust_remote_code": true
}
```

## Throughput curve

```json
[
  {
    "concurrency": 1,
    "e2e_p99": 7238.62,
    "errors": 0,
    "itl_p50": 26.54,
    "output_tok_s": 35.8,
    "req_s": 0.14,
    "ttft_p50": 367.97,
    "ttft_p99": 390.43
  }
]
```

## Provenance

- `rig:~/benchmarks/Qwen3.6-27B`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
