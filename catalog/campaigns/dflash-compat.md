# dflash-compat

9 measurements.

| date | run | model | quant | engine | layout | ctx | conc | primary metric |
|---|---|---|---|---|---|---:|---:|---:|
| 2026-07-13 | [dflash-compat/unknown/autoround-dflash/ctx8192](../runs/dflash-compat-qwen3-6-27b-45467025deda.md) | Qwen3.6-27B | awq-int4 | vllm 0.23.0 | TP=4 | 262144 | 1 | 49.6537 output tok/s |
| 2026-07-13 | [dflash-compat/unknown/autoround-dflash/ctx65280](../runs/dflash-compat-qwen3-6-27b-a3f794fe22d5.md) | Qwen3.6-27B | awq-int4 | vllm 0.23.0 | TP=4 | 262144 | 1 | 9.9025 output tok/s |
| 2026-07-13 | [dflash-compat/unknown/autoround-dflash/ctx512](../runs/dflash-compat-qwen3-6-27b-a6829f90e78c.md) | Qwen3.6-27B | awq-int4 | vllm 0.23.0 | TP=4 | 262144 | 1 | 116.641 output tok/s |
| 2026-07-13 | [dflash-compat/unknown/autoround-dflash/ctx32768](../runs/dflash-compat-qwen3-6-27b-6ddc7ad4fd00.md) | Qwen3.6-27B | awq-int4 | vllm 0.23.0 | TP=4 | 262144 | 1 | 22.5674 output tok/s |
| 2026-07-13 | [dflash-compat/unknown/autoround-dflash-256k/ctx261888](../runs/dflash-compat-qwen3-6-27b-435639f709f8.md) | Qwen3.6-27B | awq-int4 | vllm 0.23.0 | TP=4 | 262144 | 1 | 2.63798 output tok/s |
| 2026-07-13 | [dflash-compat/BF16/bf16-dflash/ctx8192](../runs/dflash-compat-qwen3-6-27b-02e62e453438.md) | Qwen3.6-27B | bf16 | vllm 0.23.0 | TP=4 | 262144 | 1 | 40.196 output tok/s |
| 2026-07-13 | [dflash-compat/BF16/bf16-dflash/ctx65280](../runs/dflash-compat-qwen3-6-27b-a37d4ee4f749.md) | Qwen3.6-27B | bf16 | vllm 0.23.0 | TP=4 | 262144 | 1 | 8.20074 output tok/s |
| 2026-07-13 | [dflash-compat/BF16/bf16-dflash/ctx512](../runs/dflash-compat-qwen3-6-27b-581efba11a48.md) | Qwen3.6-27B | bf16 | vllm 0.23.0 | TP=4 | 262144 | 1 | 120.952 output tok/s |
| 2026-07-13 | [dflash-compat/BF16/bf16-dflash/ctx32768](../runs/dflash-compat-qwen3-6-27b-0f2a1a3d3780.md) | Qwen3.6-27B | bf16 | vllm 0.23.0 | TP=4 | 262144 | 1 | 19.2221 output tok/s |

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
