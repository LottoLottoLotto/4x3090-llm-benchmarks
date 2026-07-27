# kv-sweep

55 measurements.

| date | run | model | quant | engine | layout | ctx | conc | primary metric |
|---|---|---|---|---|---|---:|---:|---:|
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c8192/turboquant_k3v4_nc](../runs/kv-sweep-qwen3-6-27b-922ef829d60d.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 8192 | 1 | 28.86 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c8192/turboquant_4bit_nc](../runs/kv-sweep-qwen3-6-27b-5f052b92b205.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 8192 | 1 | 28.71 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c8192/turboquant_3bit_nc](../runs/kv-sweep-qwen3-6-27b-46ea2261825b.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 8192 | 1 | 28.8 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c8192/int8_per_token_head](../runs/kv-sweep-qwen3-6-27b-48dc74b219d6.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 8192 | 1 | 28.21 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c8192/fp8](../runs/kv-sweep-qwen3-6-27b-270407644322.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 8192 | 1 | 28.91 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c8192/bfloat16](../runs/kv-sweep-qwen3-6-27b-24dc91e39c61.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 8192 | 1 | 29 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c8192/auto](../runs/kv-sweep-qwen3-6-27b-79f6b226bc2a.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 8192 | 1 | 28.48 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c65536/int8_per_token_head](../runs/kv-sweep-qwen3-6-27b-a4a1a8afbc99.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 65536 | 1 | 2.86 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c65536/fp8](../runs/kv-sweep-qwen3-6-27b-7fd8d67ae20e.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 65536 | 1 | 3.48 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c65536/bfloat16](../runs/kv-sweep-qwen3-6-27b-29fb6954328e.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 65536 | 1 | 3.55 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c65536/auto](../runs/kv-sweep-qwen3-6-27b-0b14bd61178d.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 65536 | 1 | 3.48 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c32768/turboquant_k3v4_nc](../runs/kv-sweep-qwen3-6-27b-2d8d01a3074a.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 32768 | 1 | 7.35 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c32768/turboquant_4bit_nc](../runs/kv-sweep-qwen3-6-27b-71ad8866711a.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 32768 | 1 | 7.31 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c32768/turboquant_3bit_nc](../runs/kv-sweep-qwen3-6-27b-9e092b46adce.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 32768 | 1 | 7.34 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c32768/int8_per_token_head](../runs/kv-sweep-qwen3-6-27b-f0b730b9e80d.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 32768 | 1 | 6.64 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c32768/fp8](../runs/kv-sweep-qwen3-6-27b-b7cb3a488aa7.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 32768 | 1 | 7.24 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c32768/bfloat16](../runs/kv-sweep-qwen3-6-27b-85986562db92.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 32768 | 1 | 7.34 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c32768/auto](../runs/kv-sweep-qwen3-6-27b-6541dfabb975.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 32768 | 1 | 7.21 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c131072/int8_per_token_head](../runs/kv-sweep-qwen3-6-27b-d39095f0e186.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 131072 | 1 | 1.13 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c131072/fp8](../runs/kv-sweep-qwen3-6-27b-4314b3820dbb.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 131072 | 1 | 1.59 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c131072/bfloat16](../runs/kv-sweep-qwen3-6-27b-7d69713646f1.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 131072 | 1 | 1.65 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c131072/auto](../runs/kv-sweep-qwen3-6-27b-cc040f70c9f0.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 131072 | 1 | 1.62 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c1024/turboquant_k3v4_nc](../runs/kv-sweep-qwen3-6-27b-84a244b5248c.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 1024 | 1 | 100.26 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c1024/turboquant_4bit_nc](../runs/kv-sweep-qwen3-6-27b-a1e3b18ff1d3.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 1024 | 1 | 100.31 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c1024/turboquant_3bit_nc](../runs/kv-sweep-qwen3-6-27b-065b8b8a99e3.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 1024 | 1 | 100.27 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c1024/int8_per_token_head](../runs/kv-sweep-qwen3-6-27b-e8b07faef5a2.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 1024 | 1 | 99.26 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c1024/fp8_e4m3](../runs/kv-sweep-qwen3-6-27b-522ca841fc4a.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 1024 | 1 | 71.51 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c1024/fp8](../runs/kv-sweep-qwen3-6-27b-09c6cf699f92.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 1024 | 1 | 99.85 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c1024/bfloat16](../runs/kv-sweep-qwen3-6-27b-b771ea476bb5.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 1024 | 1 | 100.28 output tok/s |
| 2026-06-28 | [kvsweep/Qwen3.6-27B-FP8/c1024/auto](../runs/kv-sweep-qwen3-6-27b-98331fe8198b.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 1024 | 1 | 103.46 output tok/s |
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
