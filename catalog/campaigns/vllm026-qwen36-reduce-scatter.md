# vllm026-qwen36-reduce-scatter

8 measurements.

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

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
