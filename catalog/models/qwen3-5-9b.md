# Qwen3.5-9B

6 measurements.

| date | run | model | quant | engine | layout | ctx | conc | primary metric |
|---|---|---|---|---|---|---:|---:|---:|
| 2026-07-17 | [tli-real/qwen35-9b-awq--no-spec/c8](../runs/tli-real-qwen3-5-9b-0261a2e5d44f.md) | Qwen3.5-9B | awq-int4 | vllm 0.25.0 | TP=1 | 8192 | 8 | 377.43 output tok/s |
| 2026-07-17 | [tli-real/qwen35-9b-awq--no-spec/c4](../runs/tli-real-qwen3-5-9b-c3ca17e384a4.md) | Qwen3.5-9B | awq-int4 | vllm 0.25.0 | TP=1 | 8192 | 4 | 212.49 output tok/s |
| 2026-07-17 | [tli-real/qwen35-9b-awq--no-spec/c1](../runs/tli-real-qwen3-5-9b-0ab06446186f.md) | Qwen3.5-9B | awq-int4 | vllm 0.25.0 | TP=1 | 8192 | 1 | 55.45 output tok/s |
| 2026-07-17 | [tli-real/qwen35-9b-awq--ngram-k4/c8](../runs/tli-real-qwen3-5-9b-f4c9aaf0c910.md) | Qwen3.5-9B | awq-int4 | vllm 0.25.0 | TP=1 | 8192 | 8 | 266.35 output tok/s |
| 2026-07-17 | [tli-real/qwen35-9b-awq--ngram-k4/c4](../runs/tli-real-qwen3-5-9b-48b3b7f88bd0.md) | Qwen3.5-9B | awq-int4 | vllm 0.25.0 | TP=1 | 8192 | 4 | 148.64 output tok/s |
| 2026-07-17 | [tli-real/qwen35-9b-awq--ngram-k4/c1](../runs/tli-real-qwen3-5-9b-e610c8c4957d.md) | Qwen3.5-9B | awq-int4 | vllm 0.25.0 | TP=1 | 8192 | 1 | 78.13 output tok/s |

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
