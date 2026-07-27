# qwen35-ab

4 measurements.

| date | run | model | quant | engine | layout | ctx | conc | primary metric |
|---|---|---|---|---|---|---:|---:|---:|
| 2026-07-07 | [qwen35ab/qwen35-4b-ab/quant_dflash](../runs/qwen35-ab-qwen3-5-4b-94be6e673d1a.md) | Qwen3.5-4B | dflash-quant | vllm 0.19 | TP=1 | 32768 | 4 | 251.87 output tok/s |
| 2026-07-07 | [qwen35ab/qwen35-4b-ab/base_bf16](../runs/qwen35-ab-qwen3-5-4b-ad817a1bccb7.md) | Qwen3.5-4B | bf16 | vllm 0.19 | TP=1 | 32768 | 4 | 75.98 output tok/s |
| 2026-07-07 | [qwen35ab/qwen35-4b-ab-020/quant_dflash](../runs/qwen35-ab-qwen3-5-4b-c7fea4b134ea.md) | Qwen3.5-4B | dflash-quant | vllm 0.20 | TP=1 | 32768 | 4 | 257.23 output tok/s |
| 2026-07-07 | [qwen35ab/qwen35-4b-ab-020/base_bf16](../runs/qwen35-ab-qwen3-5-4b-20a231fcce54.md) | Qwen3.5-4B | bf16 | vllm 0.20 | TP=1 | 32768 | 4 | 76.98 output tok/s |

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
