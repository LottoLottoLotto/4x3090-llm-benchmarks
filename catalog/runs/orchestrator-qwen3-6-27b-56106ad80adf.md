# `orch/Qwen3.6-27B/vllm_Int4_tp2x1_spec-none_c32768_pl220_single_stream`

| field | value |
|---|---|
| Date | 2026-06-28 |
| Campaign | orchestrator |
| Model | Qwen3.6-27B |
| Checkpoint | qwen3.6-27b-autoround-int4 |
| Quant | autoround-int4 |
| Quant method | autoround |
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
| Normalization | inferred |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 52.3 |
| `req_s` | 0.2 |
| `ttft_p50_ms` | 350.36 |
| `ttft_p99_ms` | 358.02 |
| `itl_p50_ms` | 17.65 |
| `e2e_p99_ms` | 4938.53 |
| `vram_peak_mib` | 83304 |
| `avg_power_w` | 493.9 |
| `max_temp_c` | 71.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env/bin/vllm' serve '${MODEL_ROOT}/qwen3.6-27b-autoround-int4' --host 127.0.0.1 --port 18000 --served-model-name bench --tensor-parallel-size 2 --max-model-len 32768 --gpu-memory-utilization 0.9 --trust-remote-code --max-num-seqs 1
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
    "e2e_p99": 4938.53,
    "errors": 0,
    "itl_p50": 17.65,
    "output_tok_s": 52.3,
    "req_s": 0.2,
    "ttft_p50": 350.36,
    "ttft_p99": 358.02
  }
]
```

## Provenance

- `rig:~/benchmarks/Qwen3.6-27B`

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
