# Qwen3.6-35B-A3B

26 measurements.

| date | run | model | quant | engine | layout | ctx | conc | primary metric |
|---|---|---|---|---|---|---:|---:|---:|
| 2026-07-26 | [vllm026-rs/qwen36-35b-autoround/v026_c8](../runs/vllm026-qwen36-reduce-scatter-qwen3-6-35b-a3b-edf28fbbbb34.md) | Qwen3.6-35B-A3B | autoround-int4 | vllm 0.26.0 | TP=2, DP=2 | 16384 | 8 | 309.49 output tok/s |
| 2026-07-26 | [vllm026-rs/qwen36-35b-autoround/v026_c4](../runs/vllm026-qwen36-reduce-scatter-qwen3-6-35b-a3b-1799c5083737.md) | Qwen3.6-35B-A3B | autoround-int4 | vllm 0.26.0 | TP=2, DP=2 | 16384 | 4 | 206.05 output tok/s |
| 2026-07-26 | [vllm026-rs/qwen36-35b-autoround/v026_c16](../runs/vllm026-qwen36-reduce-scatter-qwen3-6-35b-a3b-309b41557826.md) | Qwen3.6-35B-A3B | autoround-int4 | vllm 0.26.0 | TP=2, DP=2 | 16384 | 16 | 399.68 output tok/s |
| 2026-07-26 | [vllm026-rs/qwen36-35b-autoround/v026_c1](../runs/vllm026-qwen36-reduce-scatter-qwen3-6-35b-a3b-b68b25ae1e37.md) | Qwen3.6-35B-A3B | autoround-int4 | vllm 0.26.0 | TP=2, DP=2 | 16384 | 1 | 83.6 output tok/s |
| 2026-07-26 | [vllm026-rs/qwen36-35b-autoround/v025_c8](../runs/vllm026-qwen36-reduce-scatter-qwen3-6-35b-a3b-2ec27c20ac2f.md) | Qwen3.6-35B-A3B | autoround-int4 | vllm 0.25.0 | TP=2, DP=2 | 16384 | 8 | 312.4 output tok/s |
| 2026-07-26 | [vllm026-rs/qwen36-35b-autoround/v025_c4](../runs/vllm026-qwen36-reduce-scatter-qwen3-6-35b-a3b-25b9d606d75d.md) | Qwen3.6-35B-A3B | autoround-int4 | vllm 0.25.0 | TP=2, DP=2 | 16384 | 4 | 223.98 output tok/s |
| 2026-07-26 | [vllm026-rs/qwen36-35b-autoround/v025_c16](../runs/vllm026-qwen36-reduce-scatter-qwen3-6-35b-a3b-d2c925e6853a.md) | Qwen3.6-35B-A3B | autoround-int4 | vllm 0.25.0 | TP=2, DP=2 | 16384 | 16 | 380.45 output tok/s |
| 2026-07-26 | [vllm026-rs/qwen36-35b-autoround/v025_c1](../runs/vllm026-qwen36-reduce-scatter-qwen3-6-35b-a3b-fe7459f72f13.md) | Qwen3.6-35B-A3B | autoround-int4 | vllm 0.25.0 | TP=2, DP=2 | 16384 | 1 | 80.64 output tok/s |
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
| 2026-07-11 | [nvfp4/unsloth-NVFP4/tp2](../runs/nvfp4-driver-qwen3-6-35b-a3b-36093148c8bf.md) | Qwen3.6-35B-A3B | nvfp4 | vllm 0.24 | TP=2 | 131072 | 1 | 145.4 output tok/s |
| 2026-07-11 | [nvfp4/unsloth-NVFP4-Fast/tp2](../runs/nvfp4-driver-qwen3-6-35b-a3b-4605c6b82801.md) | Qwen3.6-35B-A3B | nvfp4 | vllm 0.24 | TP=2 | 131072 | 1 | 145.4 output tok/s |
| 2026-07-11 | [nvfp4/nvidia-NVFP4/tp2](../runs/nvfp4-driver-qwen3-6-35b-a3b-51d067d3da4f.md) | Qwen3.6-35B-A3B | nvfp4 | vllm 0.24 | TP=2 | 131072 | 1 | 148.8 output tok/s |
| 2026-07-11 | [nvfp4/cyankiwi-AWQ/tp2](../runs/nvfp4-driver-qwen3-6-35b-a3b-009f33338855.md) | Qwen3.6-35B-A3B | awq-int4 | vllm 0.24 | TP=2 | 131072 | 1 | 131.1 output tok/s |
| 2026-07-11 | [nvfp4/QuantTrio-AWQ/tp2](../runs/nvfp4-driver-qwen3-6-35b-a3b-7d852d7c79f7.md) | Qwen3.6-35B-A3B | awq-int4 | vllm 0.24 | TP=2 | 131072 | 1 | 129.9 output tok/s |
| 2026-06-21 | [orch/Qwen3.6-35B-A3B-AWQ-4bit/vllm_AWQ-4bit_tp4x1_spec-none_c32768_pl220_single_stream](../runs/orchestrator-qwen3-6-35b-a3b-689571d79b5f.md) | Qwen3.6-35B-A3B | awq-int4 | vllm 0.23.0 | TP=4 | 32768 | 1 | 148.8 output tok/s |

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
