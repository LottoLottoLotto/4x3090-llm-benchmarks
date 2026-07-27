# `moep-half-experts/reap50-q4/openai-c1-8192`

| field | value |
|---|---|
| Date | 2026-07-22 |
| Campaign | moep-half-experts |
| Model | Qwen3.6-35B-A3B |
| Checkpoint | reap50-q4 |
| Quant | gguf-q4_k_m-reap50 |
| Quant method | gguf |
| Engine | llama.cpp |
| Engine version | 9cde3321 |
| Objective | single_stream_depth |
| TPS kind | unknown |
| Layout | TP=1 |
| Context | 65536 |
| Concurrency | 1 |
| Prompt tokens | 8200 |
| Generated tokens | 256 |
| KV cache | q8_0 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 123.68864474575439 |
| `decode_tok_s` | 123.68864474575439 |
| `ttft_p50_ms` | 3150.816847104579 |
| `vram_peak_mib` | 11886 |
| `avg_power_w` | 205.39563829787232 |
| `max_temp_c` | 70.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/llama-mindcontrol/build-cuda128/bin/llama-server' -m '${MODEL_ROOT}/Qwen3.6-35B-A3B-coding-reap50-GGUF/qwen36-reap50-Q4_K_M-imat.gguf' --alias bench --host 127.0.0.1 --port 18270 -ngl 999 -fa on -c 65536 -np 1 -ctk q8_0 -ctv q8_0 --jinja --no-webui
```

## Engine knobs

```json
{
  "repetitions": 5,
  "target_content_tokens": 8192
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-22/moep-half-experts-code/reap50-q4/systems/openai-latency.json`

## Notes

OpenAI streaming C1; median of 5 runs. Decode rate excludes TTFT; some responses stopped before max_tokens.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
