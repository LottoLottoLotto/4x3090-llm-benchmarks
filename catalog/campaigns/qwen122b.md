# qwen122b

4 measurements.

| date | run | model | quant | engine | layout | ctx | conc | primary metric |
|---|---|---|---|---|---|---:|---:|---:|
| 2026-07-03 | [qwen122b/autoround-tp4-220w/code](../runs/qwen122b-qwen3-5-122b-d17c5241878b.md) | Qwen3.5-122B | autoround-int4 | vllm 0.23.0 | TP=4 |  | 1 | 110.5 output tok/s |
| 2026-07-02 | [qwen122b/vllm-tp4-220w/prose](../runs/qwen122b-qwen3-5-122b-482dbe97f077.md) | Qwen3.5-122B | awq-int4 | vllm 0.23.0 | TP=4 |  | 1 | 90.2 output tok/s |
| 2026-07-02 | [qwen122b/vllm-tp4-220w/code](../runs/qwen122b-qwen3-5-122b-7fcc07f4ca44.md) | Qwen3.5-122B | awq-int4 | vllm 0.23.0 | TP=4 |  | 1 | 92.7 output tok/s |
| 2026-07-02 | [qwen122b/vllm-tp4-220w-kvfp8-fi/code](../runs/qwen122b-qwen3-5-122b-2fc1d1f55019.md) | Qwen3.5-122B | awq-int4 | vllm 0.23.0 | TP=4 |  | 1 | 93.3 output tok/s |

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
