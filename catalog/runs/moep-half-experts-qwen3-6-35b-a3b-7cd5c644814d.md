# `moep-half-experts/full-q4/openai-c1-32768`

| field | value |
|---|---|
| Date | 2026-07-22 |
| Campaign | moep-half-experts |
| Model | Qwen3.6-35B-A3B |
| Checkpoint | full-q4 |
| Quant | gguf-q4_k_m |
| Quant method | gguf |
| Engine | llama.cpp |
| Engine version | 9cde3321 |
| Objective | single_stream_depth |
| TPS kind | unknown |
| Layout | TP=1 |
| Context | 65536 |
| Concurrency | 1 |
| Prompt tokens | 32783 |
| Generated tokens | 123 |
| KV cache | q8_0 |
| Power limit | 220 W/GPU |
| Normalization | exact |

## Metrics

| metric | value |
|---|---:|
| `output_tok_s` | 95.98124222941384 |
| `decode_tok_s` | 95.98124222941384 |
| `ttft_p50_ms` | 12266.8811311014 |
| `vram_peak_mib` | 21226 |
| `avg_power_w` | 205.68052631578948 |
| `max_temp_c` | 71.0 |

## Launch command

```bash
'${ENGINE_ROOT_ALT}/llama-mindcontrol/build-cuda128/bin/llama-server' -m '${MODEL_ROOT}/Qwen3.6-35B-A3B-GGUF/Qwen3.6-35B-A3B.Q4_K_M.gguf' --alias bench --host 127.0.0.1 --port 18270 -ngl 999 -fa on -c 65536 -np 1 -ctk q8_0 -ctv q8_0 --jinja --no-webui
```

## Engine knobs

```json
{
  "repetitions": 5,
  "target_content_tokens": 32768
}
```

## Provenance

- `repo:llm-bench/results/daily-papers/2026-07-22/moep-half-experts-code/full-q4/systems/openai-latency.json`

## Notes

OpenAI streaming C1; median of 5 runs. Decode rate excludes TTFT; some responses stopped before max_tokens.

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
