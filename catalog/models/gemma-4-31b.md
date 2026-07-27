# Gemma-4-31B

3 measurements.

| date | run | model | quant | engine | layout | ctx | conc | primary metric |
|---|---|---|---|---|---|---:|---:|---:|
| 2026-06-22 | [sweep0622/gemma4-31b-q4kxl-llamacpp-tensor4](../runs/sweep-0622-gemma-4-31b-045146788acf.md) | Gemma-4-31B | gguf-ud-q4_k_xl | llama.cpp llama.cpp | TP=4 | 32768 |  |  |
| 2026-06-22 | [sweep0622/gemma4-31b-awq4-tp4-throughput](../runs/sweep-0622-gemma-4-31b-17845d3e22be.md) | Gemma-4-31B | compressed-tensors-w4a16 | vllm 0.23.0 | TP=4 | 32768 |  |  |
| 2026-06-22 | [sweep0622/gemma4-31b-awq4-tp4](../runs/sweep-0622-gemma-4-31b-64fb003770df.md) | Gemma-4-31B | compressed-tensors-w4a16 | vllm 0.23.0 | TP=4 | 32768 |  |  |

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
