# `vllm026-gemma4-mtp/mtp-k1_c16`

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
| `output_tok_s` | 1599.75 |
| `total_tok_s` | 4799.24 |
| `req_s` | 3.1245 |
| `ttft_p50_ms` | 243.01 |
| `itl_p50_ms` | 8.98 |
| `tpot_p50_ms` | 7.56 |
| `vram_peak_mib` | 23078 |
| `avg_power_w` | 166.49 |
| `max_temp_c` | 71.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env-026/bin/vllm' serve '${MODEL_ROOT}/gemma-4-E2B-it-qat-mobile-ct' --host 127.0.0.1 --port 18327 --served-model-name bench --tensor-parallel-size 1 --language-model-only --max-model-len 8192 --max-num-seqs 64 --max-num-batched-tokens 8192 --gpu-memory-utilization 0.90 --no-enable-prefix-caching --generation-config vllm --speculative-config '{"method":"mtp","model":"${MODEL_ROOT}/gemma-4-E2B-it-assistant","num_speculative_tokens":1}'
```

## Speculative decoding

```json
{
  "draft_path": null,
  "draft_ref": null,
  "k": 1,
  "method": "mtp"
}
```

## Engine knobs

```json
{
  "assistant_model": "${MODEL_ROOT}/gemma-4-E2B-it-assistant",
  "centroids_masking": true,
  "client_version": "0.26.0",
  "gpu_memory_utilization": 0.9,
  "max_num_batched_tokens": 8192,
  "max_num_seqs": 64,
  "model_runner_v2": true,
  "num_speculative_tokens": 1,
  "prefix_caching": false
}
```

## Samples

```json
{
  "draft_acceptance_pct_all": [
    55.79468622035997,
    48.812664907651715,
    48.62827034883721,
    43.31873905429072,
    49.397260273972606
  ],
  "draft_acceptance_pct_median": 48.812664907651715,
  "output_tok_s_all": [
    1505.5403443955743,
    1599.748094501555,
    1610.5907979303092,
    1493.3110840248412,
    1603.9143333444715
  ],
  "output_tok_s_max": 1610.5907979303092,
  "output_tok_s_min": 1493.3110840248412,
  "repeats": 5
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-27/vllm026-gemma4-mtp-3090`

## Notes

Gemma 4 E2B mobile QAT on one RTX 3090, vLLM 0.26.0. Fixed random 1024 input + 512 output, prefix cache off. Five repeats at c4/c16; c1 has 5 baseline and 20 MTP repeats. MTP path and centroids masking (4096/262144 active tokens) confirmed in server log. Zero failed requests. Greedy chat outputs were nondeterministic even for baseline, so no byte-identical lossless claim.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
