# ds4-profiling

6 measurements.

| date | run | model | quant | engine | layout | ctx | conc | primary metric |
|---|---|---|---|---|---|---:|---:|---:|
| 2026-07-10 | [ds4/baseline/prefill-pp512](../runs/ds4-profiling-deepseek-v4-flash-b7d9838d4058.md) | DeepSeek-V4-Flash | gguf-custom | llama.cpp | TP=4 | 512 |  | 581 prefill tok/s |
| 2026-07-10 | [ds4/baseline/prefill-97k](../runs/ds4-profiling-deepseek-v4-flash-7ef99e67c61a.md) | DeepSeek-V4-Flash | gguf-custom | llama.cpp | TP=4 | 97000 |  | 495 prefill tok/s |
| 2026-07-10 | [ds4/baseline/decode-fine](../runs/ds4-profiling-deepseek-v4-flash-9ecea2d565bf.md) | DeepSeek-V4-Flash | gguf-custom | llama.cpp | TP=4 | 512 |  | 36.34 output tok/s |
| 2026-07-10 | [ds4/baseline/decode-97k](../runs/ds4-profiling-deepseek-v4-flash-7d9cb5dfc2d5.md) | DeepSeek-V4-Flash | gguf-custom | llama.cpp | TP=4 | 97000 |  | 31.6 output tok/s |
| 2026-07-10 | [ds4/EP/prefill-pp512](../runs/ds4-profiling-deepseek-v4-flash-02da106dc1a9.md) | DeepSeek-V4-Flash | gguf-custom | llama.cpp | TP=4 | 512 |  | 702 prefill tok/s |
| 2026-07-10 | [ds4/EP/decode-fine](../runs/ds4-profiling-deepseek-v4-flash-d5cca647ca72.md) | DeepSeek-V4-Flash | gguf-custom | llama.cpp | TP=4 | 512 |  | 23.82 output tok/s |

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
