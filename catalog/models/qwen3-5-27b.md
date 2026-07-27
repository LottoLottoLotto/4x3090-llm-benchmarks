# Qwen3.5-27B

25 measurements.

| date | run | model | quant | engine | layout | ctx | conc | primary metric |
|---|---|---|---|---|---|---:|---:|---:|
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c8192/turboquant_k3v4_nc](../runs/kv-sweep-qwen3-5-27b-0e22201af67e.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 8192 | 1 | 26.11 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c8192/turboquant_4bit_nc](../runs/kv-sweep-qwen3-5-27b-ee7f7c5f9336.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 8192 | 1 | 26.78 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c8192/turboquant_3bit_nc](../runs/kv-sweep-qwen3-5-27b-a8934fd662a3.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 8192 | 1 | 26.42 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c8192/int8_per_token_head](../runs/kv-sweep-qwen3-5-27b-93fd6f19661b.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 8192 | 1 | 26.79 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c8192/fp8](../runs/kv-sweep-qwen3-5-27b-dbb21d63518b.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 8192 | 1 | 26.93 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c8192/bfloat16](../runs/kv-sweep-qwen3-5-27b-02a8f73522bf.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 8192 | 1 | 26.55 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c8192/auto](../runs/kv-sweep-qwen3-5-27b-4e641b15337e.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 8192 | 1 | 29.13 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c32768/turboquant_k3v4_nc](../runs/kv-sweep-qwen3-5-27b-7281c742a72b.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 32768 | 1 | 6.93 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c32768/turboquant_4bit_nc](../runs/kv-sweep-qwen3-5-27b-ac378f530af2.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 32768 | 1 | 7.1 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c32768/turboquant_3bit_nc](../runs/kv-sweep-qwen3-5-27b-f5c32c71a8e5.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 32768 | 1 | 6.98 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c32768/int8_per_token_head](../runs/kv-sweep-qwen3-5-27b-bb6cf49991a0.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 32768 | 1 | 6.56 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c32768/fp8](../runs/kv-sweep-qwen3-5-27b-29360b9bb7d7.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 32768 | 1 | 7.09 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c32768/bfloat16](../runs/kv-sweep-qwen3-5-27b-5aed6830efc6.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 32768 | 1 | 7.06 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c32768/auto](../runs/kv-sweep-qwen3-5-27b-900d3af76ae4.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 32768 | 1 | 7.27 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c131072/int8_per_token_head](../runs/kv-sweep-qwen3-5-27b-04a90626520a.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 131072 | 1 | 1.11 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c131072/fp8](../runs/kv-sweep-qwen3-5-27b-c22c4c1afb18.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 131072 | 1 | 1.55 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c131072/bfloat16](../runs/kv-sweep-qwen3-5-27b-52c5eed8d008.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 131072 | 1 | 1.62 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c131072/auto](../runs/kv-sweep-qwen3-5-27b-a670d14b7979.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 131072 | 1 | 1.59 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c1024/turboquant_k3v4_nc](../runs/kv-sweep-qwen3-5-27b-7eef628f7ace.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 1024 | 1 | 72.87 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c1024/turboquant_4bit_nc](../runs/kv-sweep-qwen3-5-27b-f3387d2ae533.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 1024 | 1 | 73.55 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c1024/turboquant_3bit_nc](../runs/kv-sweep-qwen3-5-27b-166871b05870.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 1024 | 1 | 73.2 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c1024/int8_per_token_head](../runs/kv-sweep-qwen3-5-27b-8a88c7a5deff.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 1024 | 1 | 79.4 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c1024/fp8](../runs/kv-sweep-qwen3-5-27b-d69afa25547f.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 1024 | 1 | 78.26 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c1024/bfloat16](../runs/kv-sweep-qwen3-5-27b-263dfc450cb2.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 1024 | 1 | 79.64 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.5-27B-AWQ-4bit/c1024/auto](../runs/kv-sweep-qwen3-5-27b-8cd2bf3ee997.md) | Qwen3.5-27B | awq-int4 | vllm 0.23.0 | TP=4 | 1024 | 1 | 102.89 output tok/s |

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
