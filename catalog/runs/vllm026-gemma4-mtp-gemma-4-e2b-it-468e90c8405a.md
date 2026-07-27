# `vllm026-gemma4-mtp/baseline_c16`

| field | value |
|---|---|
| Date | 2026-07-27 |
| Campaign | vllm026-gemma4-mtp |
| Model | Gemma-4-E2B-it |
| Checkpoint | gemma-4-E2B-it-qat-mobile-ct |
| Quant | qat-mixed-int2-4-8 |
| Quant method | qat |
| Engine | vllm |
| Engine version | 0.26.0 |
| Objective | aggregate |
| TPS kind | aggregate_output |
| Layout | TP=1 |
| Context | 8192 |
| Concurrency | 16 |
| Prompt tokens | 1024 |
| Generated tokens | 512 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 1969.37 |
| `total_tok_s` | 5908.11 |
| `req_s` | 3.8464 |
| `ttft_p50_ms` | 1086.94 |
| `itl_p50_ms` | 5.45 |
| `tpot_p50_ms` | 6.0 |
| `vram_peak_mib` | 22518 |
| `avg_power_w` | 163.23 |
| `max_temp_c` | 70.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env-026/bin/vllm' serve '${MODEL_ROOT}/gemma-4-E2B-it-qat-mobile-ct' --host 127.0.0.1 --port 18327 --served-model-name bench --tensor-parallel-size 1 --language-model-only --max-model-len 8192 --max-num-seqs 64 --max-num-batched-tokens 8192 --gpu-memory-utilization 0.90 --no-enable-prefix-caching --generation-config vllm
```

## Engine knobs

```json
{
  "assistant_model": null,
  "centroids_masking": false,
  "client_version": "0.26.0",
  "gpu_memory_utilization": 0.9,
  "max_num_batched_tokens": 8192,
  "max_num_seqs": 64,
  "model_runner_v2": true,
  "num_speculative_tokens": null,
  "prefix_caching": false
}
```

## Samples

```json
{
  "draft_acceptance_pct_all": null,
  "draft_acceptance_pct_median": null,
  "output_tok_s_all": [
    1969.3696949806276,
    1968.5705804683525,
    1968.2008033530285,
    1970.7528051019372,
    1970.2374719953234
  ],
  "output_tok_s_max": 1970.7528051019372,
  "output_tok_s_min": 1968.2008033530285,
  "repeats": 5
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-27/vllm026-gemma4-mtp-3090`

## Notes

Gemma 4 E2B mobile QAT on one RTX 3090, vLLM 0.26.0. Fixed random 1024 input + 512 output, prefix cache off. Five repeats at c4/c16; c1 has 5 baseline and 20 MTP repeats. MTP path and centroids masking (4096/262144 active tokens) confirmed in server log. Zero failed requests. Greedy chat outputs were nondeterministic even for baseline, so no byte-identical lossless claim.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
