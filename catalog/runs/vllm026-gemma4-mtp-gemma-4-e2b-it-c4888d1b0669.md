# `vllm026-gemma4-mtp/mtp-k3_c1`

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
| Objective | single_stream |
| TPS kind | single_stream_wall |
| Layout | TP=1 |
| Context | 8192 |
| Concurrency | 1 |
| Prompt tokens | 1024 |
| Generated tokens | 512 |
| KV cache | auto |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 246.36 |
| `total_tok_s` | 739.08 |
| `req_s` | 0.4812 |
| `ttft_p50_ms` | 112.72 |
| `itl_p50_ms` | 6.48 |
| `tpot_p50_ms` | 3.75 |
| `vram_peak_mib` | 23496 |
| `avg_power_w` | 167.06 |
| `max_temp_c` | 72.0 |

## Launch command

```bash
'${ENGINE_ROOT}/vllm-env-026/bin/vllm' serve '${MODEL_ROOT}/gemma-4-E2B-it-qat-mobile-ct' --host 127.0.0.1 --port 18327 --served-model-name bench --tensor-parallel-size 1 --language-model-only --max-model-len 8192 --max-num-seqs 64 --max-num-batched-tokens 8192 --gpu-memory-utilization 0.90 --no-enable-prefix-caching --generation-config vllm --speculative-config '{"method":"mtp","model":"${MODEL_ROOT}/gemma-4-E2B-it-assistant","num_speculative_tokens":3}'
```

## Speculative decoding

```json
{
  "draft_path": null,
  "draft_ref": null,
  "k": 3,
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
  "num_speculative_tokens": 3,
  "prefix_caching": false
}
```

## Samples

```json
{
  "draft_acceptance_pct_all": [
    21.764864137745494,
    26.7018779342723,
    30.70669168230144,
    23.05785123966942,
    22.844590884129598,
    25.896990740740737,
    15.046132008516677,
    18.796225452690642,
    29.612546125461254,
    23.49179872115652,
    14.425770308123248,
    19.714656290531778,
    28.77959927140255,
    22.05962059620596,
    21.394230769230766,
    18.792971734148207,
    30.223880597014922,
    33.59425962165688,
    18.83614088820827,
    43.4717545828657
  ],
  "draft_acceptance_pct_median": 22.95122106189951,
  "output_tok_s_all": [
    241.42528295992147,
    262.38290953614427,
    278.3356308140779,
    246.58035106481208,
    246.1404877709643,
    258.9799023606082,
    213.47422398517148,
    229.42708248325502,
    273.8740536180516,
    248.99144241382564,
    211.07575463946884,
    233.31134282971385,
    270.38588539293113,
    243.28811731595994,
    239.87982426414405,
    227.6117665096538,
    274.8892589855963,
    287.9145397999573,
    228.52303376975905,
    327.34492114492696
  ],
  "output_tok_s_max": 327.34492114492696,
  "output_tok_s_min": 211.07575463946884,
  "repeats": 20
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-27/vllm026-gemma4-mtp-3090`

## Notes

Gemma 4 E2B mobile QAT on one RTX 3090, vLLM 0.26.0. Fixed random 1024 input + 512 output, prefix cache off. Five repeats at c4/c16; c1 has 5 baseline and 20 MTP repeats. MTP path and centroids masking (4096/262144 active tokens) confirmed in server log. Zero failed requests. Greedy chat outputs were nondeterministic even for baseline, so no byte-identical lossless claim.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
