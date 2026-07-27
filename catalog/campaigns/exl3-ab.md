# exl3-ab

48 measurements.

| date | run | model | quant | engine | layout | ctx | conc | primary metric |
|---|---|---|---|---|---|---:|---:|---:|
| 2026-07-16 | [exl3-ab/vllm-gguf/vllm_gguf_bonsai_ctx4096](../runs/exl3-ab-ternary-bonsai-8b-e74241b22d7d.md) | Ternary-Bonsai-8B | gguf-f16 | vllm 0.23.0 | TP=1 | 8192 | 1 | 35.06 output tok/s |
| 2026-07-16 | [exl3-ab/vllm-gguf/vllm_gguf_bonsai_ctx2048](../runs/exl3-ab-ternary-bonsai-8b-c9d18d3a05e1.md) | Ternary-Bonsai-8B | gguf-f16 | vllm 0.23.0 | TP=1 | 8192 | 1 | 35.98 output tok/s |
| 2026-07-16 | [exl3-ab/llamacpp/q6k/sm-row/pp8192](../runs/exl3-ab-qwen3-6-27b-77048d08cd59.md) | Qwen3.6-27B | gguf-q6_k | llama.cpp 7c082bc41 | TP=4 |  | 1 | 19.02 output tok/s |
| 2026-07-16 | [exl3-ab/llamacpp/q6k/sm-row/pp32768](../runs/exl3-ab-qwen3-6-27b-55e15d04a2c4.md) | Qwen3.6-27B | gguf-q6_k | llama.cpp 7c082bc41 | TP=4 |  | 1 | 19.02 output tok/s |
| 2026-07-16 | [exl3-ab/llamacpp/q6k/sm-row/pp2048](../runs/exl3-ab-qwen3-6-27b-d7cd24583d35.md) | Qwen3.6-27B | gguf-q6_k | llama.cpp 7c082bc41 | TP=4 |  | 1 | 19.02 output tok/s |
| 2026-07-16 | [exl3-ab/llamacpp/q6k/sm-layer/pp8192](../runs/exl3-ab-qwen3-6-27b-ac4eb2c9ed8b.md) | Qwen3.6-27B | gguf-q6_k | llama.cpp 7c082bc41 | TP=4 |  | 1 | 33.09 output tok/s |
| 2026-07-16 | [exl3-ab/llamacpp/q6k/sm-layer/pp32768](../runs/exl3-ab-qwen3-6-27b-d9e3cb9a9a30.md) | Qwen3.6-27B | gguf-q6_k | llama.cpp 7c082bc41 | TP=4 |  | 1 | 33.09 output tok/s |
| 2026-07-16 | [exl3-ab/llamacpp/q6k/sm-layer/pp2048](../runs/exl3-ab-qwen3-6-27b-ebdb9ca39c74.md) | Qwen3.6-27B | gguf-q6_k | llama.cpp 7c082bc41 | TP=4 |  | 1 | 33.09 output tok/s |
| 2026-07-16 | [exl3-ab/llamacpp/bonsai/sm-layer/pp4096](../runs/exl3-ab-ternary-bonsai-8b-bc3a357139e2.md) | Ternary-Bonsai-8B | gguf-f16 | llama.cpp 7c082bc41 | TP=1 |  | 1 | 35.6 output tok/s |
| 2026-07-16 | [exl3-ab/llamacpp/bonsai/sm-layer/pp2048](../runs/exl3-ab-ternary-bonsai-8b-d59124ea86eb.md) | Ternary-Bonsai-8B | gguf-f16 | llama.cpp 7c082bc41 | TP=1 |  | 1 | 35.6 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/q4_100_tp_ctx512_fp16kv](../runs/exl3-ab-qwen3-6-27b-bb71b5403150.md) | Qwen3.6-27B | exl3-4.0bpw-mul1 | exllamav3 1.0.0+cu128.torch2.8.0 | TP=4 | 4096 | 1 | 67.53 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/q4_100_tp_ctx512](../runs/exl3-ab-qwen3-6-27b-1c9f56e925c1.md) | Qwen3.6-27B | exl3-4.0bpw-mul1 | exllamav3 1.0.0+cu128.torch2.8.0 | TP=4 | 4096 | 1 | 65.7 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/q4_100_tp_ctx32768_fp16kv](../runs/exl3-ab-qwen3-6-27b-40d1abe07dd5.md) | Qwen3.6-27B | exl3-4.0bpw-mul1 | exllamav3 1.0.0+cu128.torch2.8.0 | TP=4 | 40960 | 1 | 58.15 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/q4_100_tp_ctx32768](../runs/exl3-ab-qwen3-6-27b-2c63c6b87767.md) | Qwen3.6-27B | exl3-4.0bpw-mul1 | exllamav3 1.0.0+cu128.torch2.8.0 | TP=4 | 40960 | 1 | 55.22 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/q4_100_tp_ctx2048_noint8](../runs/exl3-ab-qwen3-6-27b-c6b5787cfa39.md) | Qwen3.6-27B | exl3-4.0bpw-mul1 | exllamav3 1.0.0+cu128.torch2.8.0 | TP=4 | 8192 | 1 | 57.13 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/q4_100_tp_ctx2048](../runs/exl3-ab-qwen3-6-27b-3284b54691da.md) | Qwen3.6-27B | exl3-4.0bpw-mul1 | exllamav3 1.0.0+cu128.torch2.8.0 | TP=4 | 8192 | 1 | 63.41 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/q4_100_single_ctx512](../runs/exl3-ab-qwen3-6-27b-908e2130ba82.md) | Qwen3.6-27B | exl3-4.0bpw-mul1 | exllamav3 1.0.0+cu128.torch2.8.0 | TP=1 | 4096 | 1 | 28.79 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/q4_100_single_ctx2048_noint8](../runs/exl3-ab-qwen3-6-27b-6548310e3134.md) | Qwen3.6-27B | exl3-4.0bpw-mul1 | exllamav3 1.0.0+cu128.torch2.8.0 | TP=1 | 8192 | 1 | 22.81 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/q4_100_single_ctx2048](../runs/exl3-ab-qwen3-6-27b-e74053cf2afa.md) | Qwen3.6-27B | exl3-4.0bpw-mul1 | exllamav3 1.0.0+cu128.torch2.8.0 | TP=1 | 8192 | 1 | 28.35 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/cb_mul1_tp_ctx2048](../runs/exl3-ab-qwen3-6-27b-77ad4a48fc98.md) | Qwen3.6-27B | exl3-6.0bpw-mul1 | exllamav3 1.0.0+cu128.torch2.8.0 | TP=4 | 8192 | 1 | 23.65 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/cb_mul1_single_ctx2048_noint8](../runs/exl3-ab-qwen3-6-27b-4870eb0f8114.md) | Qwen3.6-27B | exl3-6.0bpw-mul1 | exllamav3 1.0.0+cu128.torch2.8.0 | TP=1 | 8192 | 1 | 17.8 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/cb_mul1_single_ctx2048](../runs/exl3-ab-qwen3-6-27b-f2b4181f54a3.md) | Qwen3.6-27B | exl3-6.0bpw-mul1 | exllamav3 1.0.0+cu128.torch2.8.0 | TP=1 | 8192 | 1 | 17.78 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/100noqc_tp_ctx8192](../runs/exl3-ab-qwen3-6-27b-9802a9973f53.md) | Qwen3.6-27B | exl3-6.0bpw-mcg | exllamav3 1.0.0+cu128.torch2.8.0 | TP=4 | 16384 | 1 | 46.59 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/100noqc_tp_ctx32768](../runs/exl3-ab-qwen3-6-27b-1725593253bb.md) | Qwen3.6-27B | exl3-6.0bpw-mcg | exllamav3 1.0.0+cu128.torch2.8.0 | TP=4 | 40960 | 1 | 43.21 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/100noqc_single_ctx8192](../runs/exl3-ab-qwen3-6-27b-038f07e0d9fe.md) | Qwen3.6-27B | exl3-6.0bpw-mcg | exllamav3 1.0.0+cu128.torch2.8.0 | TP=1 | 16384 | 1 | 16.94 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/100noqc_single_ctx32768](../runs/exl3-ab-qwen3-6-27b-ff96f7d75a11.md) | Qwen3.6-27B | exl3-6.0bpw-mcg | exllamav3 1.0.0+cu128.torch2.8.0 | TP=1 | 40960 | 1 | 15.99 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/100fa2_tp_ctx8192](../runs/exl3-ab-qwen3-6-27b-b04faf29ef33.md) | Qwen3.6-27B | exl3-6.0bpw-mcg | exllamav3 1.0.0+cu128.torch2.8.0 | TP=4 | 16384 | 1 | 47.75 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/100fa2_tp_ctx32768](../runs/exl3-ab-qwen3-6-27b-38d2962bda14.md) | Qwen3.6-27B | exl3-6.0bpw-mcg | exllamav3 1.0.0+cu128.torch2.8.0 | TP=4 | 40960 | 1 | 45.43 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/100_tp_ctx8192](../runs/exl3-ab-qwen3-6-27b-cfbc835d8aeb.md) | Qwen3.6-27B | exl3-6.0bpw-mcg | exllamav3 1.0.0+cu128.torch2.8.0 | TP=4 | 16384 | 1 | 48.06 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/100_tp_ctx32768](../runs/exl3-ab-qwen3-6-27b-29af79d6e448.md) | Qwen3.6-27B | exl3-6.0bpw-mcg | exllamav3 1.0.0+cu128.torch2.8.0 | TP=4 | 40960 | 1 | 45.32 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/100_tp_ctx2048](../runs/exl3-ab-qwen3-6-27b-f313d3a1a3ee.md) | Qwen3.6-27B | exl3-6.0bpw-mcg | exllamav3 1.0.0+cu128.torch2.8.0 | TP=4 | 8192 | 1 | 48.55 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/100_single_ctx8192](../runs/exl3-ab-qwen3-6-27b-3442bfb61ea3.md) | Qwen3.6-27B | exl3-6.0bpw-mcg | exllamav3 1.0.0+cu128.torch2.8.0 | TP=1 | 16384 | 1 | 16.87 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/100_single_ctx32768](../runs/exl3-ab-qwen3-6-27b-b3c3b0fd9d17.md) | Qwen3.6-27B | exl3-6.0bpw-mcg | exllamav3 1.0.0+cu128.torch2.8.0 | TP=1 | 40960 | 1 | 15.92 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-1.0.0/100_single_ctx2048](../runs/exl3-ab-qwen3-6-27b-ccaa6796a1d6.md) | Qwen3.6-27B | exl3-6.0bpw-mcg | exllamav3 1.0.0+cu128.torch2.8.0 | TP=1 | 8192 | 1 | 17.12 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-0.0.43/q4_043_tp_ctx2048](../runs/exl3-ab-qwen3-6-27b-ef24a24627e3.md) | Qwen3.6-27B | exl3-4.0bpw-mul1 | exllamav3 0.0.43+cu128.torch2.8.0 | TP=4 | 8192 | 1 | 30.06 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-0.0.43/q4_043_single_ctx2048](../runs/exl3-ab-qwen3-6-27b-0a58dfa9f19e.md) | Qwen3.6-27B | exl3-4.0bpw-mul1 | exllamav3 0.0.43+cu128.torch2.8.0 | TP=1 | 8192 | 1 | 21.25 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-0.0.43/chart_100_ctx512](../runs/exl3-ab-qwen3-6-27b-37280e4c7b19.md) | Qwen3.6-27B | exl3-4.0bpw-mul1 | exllamav3 1.0.0+cu128.torch2.8.0 | TP=4 | 4096 | 1 | 67.69 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-0.0.43/chart_100_ctx32768](../runs/exl3-ab-qwen3-6-27b-772956694795.md) | Qwen3.6-27B | exl3-4.0bpw-mul1 | exllamav3 1.0.0+cu128.torch2.8.0 | TP=4 | 40960 | 1 | 57.9 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-0.0.43/chart_043_ctx512](../runs/exl3-ab-qwen3-6-27b-45f16b406d9b.md) | Qwen3.6-27B | exl3-4.0bpw-mul1 | exllamav3 0.0.43+cu128.torch2.8.0 | TP=4 | 4096 | 1 | 31.89 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-0.0.43/chart_043_ctx32768](../runs/exl3-ab-qwen3-6-27b-4145b9e8122b.md) | Qwen3.6-27B | exl3-4.0bpw-mul1 | exllamav3 0.0.43+cu128.torch2.8.0 | TP=4 | 40960 | 1 | 29.73 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-0.0.43/cb_mcg030_tp_ctx2048](../runs/exl3-ab-qwen3-6-27b-290ee64e9321.md) | Qwen3.6-27B | exl3-6.0bpw-mcg | exllamav3 1.0.0+cu128.torch2.8.0 | TP=4 | 8192 | 1 | 23.46 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-0.0.43/cb_mcg030_single_ctx2048](../runs/exl3-ab-qwen3-6-27b-9f44b2cc460d.md) | Qwen3.6-27B | exl3-6.0bpw-mcg | exllamav3 1.0.0+cu128.torch2.8.0 | TP=1 | 8192 | 1 | 17.21 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-0.0.43/043_tp_ctx8192](../runs/exl3-ab-qwen3-6-27b-e544cb1fffc7.md) | Qwen3.6-27B | exl3-6.0bpw-mcg | exllamav3 0.0.43+cu128.torch2.8.0 | TP=4 | 16384 | 1 | 29.56 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-0.0.43/043_tp_ctx32768](../runs/exl3-ab-qwen3-6-27b-d0d790b704f5.md) | Qwen3.6-27B | exl3-6.0bpw-mcg | exllamav3 0.0.43+cu128.torch2.8.0 | TP=4 | 40960 | 1 | 30.7 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-0.0.43/043_tp_ctx2048](../runs/exl3-ab-qwen3-6-27b-8d4405a431c9.md) | Qwen3.6-27B | exl3-6.0bpw-mcg | exllamav3 0.0.43+cu128.torch2.8.0 | TP=4 | 8192 | 1 | 30.34 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-0.0.43/043_single_ctx8192](../runs/exl3-ab-qwen3-6-27b-b5c41ff00f0f.md) | Qwen3.6-27B | exl3-6.0bpw-mcg | exllamav3 0.0.43+cu128.torch2.8.0 | TP=1 | 16384 | 1 | 15.12 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-0.0.43/043_single_ctx32768](../runs/exl3-ab-qwen3-6-27b-ee5800091e4a.md) | Qwen3.6-27B | exl3-6.0bpw-mcg | exllamav3 0.0.43+cu128.torch2.8.0 | TP=1 | 40960 | 1 | 12.28 output tok/s |
| 2026-07-16 | [exl3-ab/exllamav3-0.0.43/043_single_ctx2048](../runs/exl3-ab-qwen3-6-27b-38f09386ebbf.md) | Qwen3.6-27B | exl3-6.0bpw-mcg | exllamav3 0.0.43+cu128.torch2.8.0 | TP=1 | 8192 | 1 | 16.09 output tok/s |

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
