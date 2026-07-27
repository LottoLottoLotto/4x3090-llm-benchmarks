# moep-half-experts

12 measurements.

| date | run | model | quant | engine | layout | ctx | conc | primary metric |
|---|---|---|---|---|---|---:|---:|---:|
| 2026-07-22 | [moep-half-experts/reap50-q4/tg256](../runs/moep-half-experts-qwen3-6-35b-a3b-b4a5a5eae5ba.md) | Qwen3.6-35B-A3B | gguf-q4_k_m-reap50 | llama.cpp 9cde3321 | TP=1 |  |  | 144.187 output tok/s |
| 2026-07-22 | [moep-half-experts/reap50-q4/pp512](../runs/moep-half-experts-qwen3-6-35b-a3b-d2b588282d4a.md) | Qwen3.6-35B-A3B | gguf-q4_k_m-reap50 | llama.cpp 9cde3321 | TP=1 |  |  | 2946.82 prefill tok/s |
| 2026-07-22 | [moep-half-experts/reap50-q4/openai-c1-8192](../runs/moep-half-experts-qwen3-6-35b-a3b-ba8382ab6cb2.md) | Qwen3.6-35B-A3B | gguf-q4_k_m-reap50 | llama.cpp 9cde3321 | TP=1 | 65536 | 1 | 123.689 output tok/s |
| 2026-07-22 | [moep-half-experts/reap50-q4/openai-c1-32768](../runs/moep-half-experts-qwen3-6-35b-a3b-01612222af9b.md) | Qwen3.6-35B-A3B | gguf-q4_k_m-reap50 | llama.cpp 9cde3321 | TP=1 | 65536 | 1 | 96.1674 output tok/s |
| 2026-07-22 | [moep-half-experts/full-q4/tg256](../runs/moep-half-experts-qwen3-6-35b-a3b-3e9175b766aa.md) | Qwen3.6-35B-A3B | gguf-q4_k_m | llama.cpp 9cde3321 | TP=1 |  |  | 141.923 output tok/s |
| 2026-07-22 | [moep-half-experts/full-q4/pp512](../runs/moep-half-experts-qwen3-6-35b-a3b-ab9d4a5c3454.md) | Qwen3.6-35B-A3B | gguf-q4_k_m | llama.cpp 9cde3321 | TP=1 |  |  | 2344.8 prefill tok/s |
| 2026-07-22 | [moep-half-experts/full-q4/openai-c1-8192](../runs/moep-half-experts-qwen3-6-35b-a3b-3d566653287a.md) | Qwen3.6-35B-A3B | gguf-q4_k_m | llama.cpp 9cde3321 | TP=1 | 65536 | 1 | 123.045 output tok/s |
| 2026-07-22 | [moep-half-experts/full-q4/openai-c1-32768](../runs/moep-half-experts-qwen3-6-35b-a3b-7cd5c644814d.md) | Qwen3.6-35B-A3B | gguf-q4_k_m | llama.cpp 9cde3321 | TP=1 | 65536 | 1 | 95.9812 output tok/s |
| 2026-07-22 | [moep-half-experts/full-q2/tg256](../runs/moep-half-experts-qwen3-6-35b-a3b-dc723c940581.md) | Qwen3.6-35B-A3B | gguf-q2_k | llama.cpp 9cde3321 | TP=1 |  |  | 140.627 output tok/s |
| 2026-07-22 | [moep-half-experts/full-q2/pp512](../runs/moep-half-experts-qwen3-6-35b-a3b-2964b0a3b743.md) | Qwen3.6-35B-A3B | gguf-q2_k | llama.cpp 9cde3321 | TP=1 |  |  | 2245.16 prefill tok/s |
| 2026-07-22 | [moep-half-experts/full-q2/openai-c1-8192](../runs/moep-half-experts-qwen3-6-35b-a3b-f2fa991263c1.md) | Qwen3.6-35B-A3B | gguf-q2_k | llama.cpp 9cde3321 | TP=1 | 65536 | 1 | 121.988 output tok/s |
| 2026-07-22 | [moep-half-experts/full-q2/openai-c1-32768](../runs/moep-half-experts-qwen3-6-35b-a3b-b22f637a73d7.md) | Qwen3.6-35B-A3B | gguf-q2_k | llama.cpp 9cde3321 | TP=1 | 65536 | 1 | 95.7622 output tok/s |

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
