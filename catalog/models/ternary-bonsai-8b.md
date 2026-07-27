# Ternary-Bonsai-8B

4 measurements.

| date | run | model | quant | engine | layout | ctx | conc | primary metric |
|---|---|---|---|---|---|---:|---:|---:|
| 2026-07-16 | [exl3-ab/vllm-gguf/vllm_gguf_bonsai_ctx4096](../runs/exl3-ab-ternary-bonsai-8b-e74241b22d7d.md) | Ternary-Bonsai-8B | gguf-f16 | vllm 0.23.0 | TP=1 | 8192 | 1 | 35.06 output tok/s |
| 2026-07-16 | [exl3-ab/vllm-gguf/vllm_gguf_bonsai_ctx2048](../runs/exl3-ab-ternary-bonsai-8b-c9d18d3a05e1.md) | Ternary-Bonsai-8B | gguf-f16 | vllm 0.23.0 | TP=1 | 8192 | 1 | 35.98 output tok/s |
| 2026-07-16 | [exl3-ab/llamacpp/bonsai/sm-layer/pp4096](../runs/exl3-ab-ternary-bonsai-8b-bc3a357139e2.md) | Ternary-Bonsai-8B | gguf-f16 | llama.cpp 7c082bc41 | TP=1 |  | 1 | 35.6 output tok/s |
| 2026-07-16 | [exl3-ab/llamacpp/bonsai/sm-layer/pp2048](../runs/exl3-ab-ternary-bonsai-8b-d59124ea86eb.md) | Ternary-Bonsai-8B | gguf-f16 | llama.cpp 7c082bc41 | TP=1 |  | 1 | 35.6 output tok/s |

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
