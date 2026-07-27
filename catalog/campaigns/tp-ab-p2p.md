# tp-ab-p2p

19 measurements.

| date | run | model | quant | engine | layout | ctx | conc | primary metric |
|---|---|---|---|---|---|---:|---:|---:|
| 2026-07-26 | [tpab/Qwen3.6-27B/autoround-int4_tp4_single_stream](../runs/tp-ab-p2p-qwen3-6-27b-c22c394eab3c.md) | Qwen3.6-27B | autoround-int4 | vllm 0.23.0 | TP=4 | 32768 | 1 | 69.26 output tok/s |
| 2026-07-26 | [tpab/Qwen3.6-27B/autoround-int4_tp4_aggregate_c64](../runs/tp-ab-p2p-qwen3-6-27b-86d40b6bd9c5.md) | Qwen3.6-27B | autoround-int4 | vllm 0.23.0 | TP=4 | 32768 | 64 | 294.76 output tok/s |
| 2026-07-26 | [tpab/Qwen3.6-27B/autoround-int4_tp4_aggregate_c4](../runs/tp-ab-p2p-qwen3-6-27b-1ce5b0ff08e3.md) | Qwen3.6-27B | autoround-int4 | vllm 0.23.0 | TP=4 | 32768 | 4 | 144.32 output tok/s |
| 2026-07-26 | [tpab/Qwen3.6-27B/autoround-int4_tp4_aggregate_c32](../runs/tp-ab-p2p-qwen3-6-27b-63d37ea97687.md) | Qwen3.6-27B | autoround-int4 | vllm 0.23.0 | TP=4 | 32768 | 32 | 284 output tok/s |
| 2026-07-26 | [tpab/Qwen3.6-27B/autoround-int4_tp4_aggregate_c16](../runs/tp-ab-p2p-qwen3-6-27b-9a17bd9c34e6.md) | Qwen3.6-27B | autoround-int4 | vllm 0.23.0 | TP=4 | 32768 | 16 | 210.78 output tok/s |
| 2026-07-26 | [tpab/Qwen3.6-27B/autoround-int4_tp4_aggregate_c1](../runs/tp-ab-p2p-qwen3-6-27b-26b515771c5a.md) | Qwen3.6-27B | autoround-int4 | vllm 0.23.0 | TP=4 | 32768 | 1 | 57.33 output tok/s |
| 2026-07-26 | [tpab/Qwen3.6-27B/autoround-int4_tp2_single_stream](../runs/tp-ab-p2p-qwen3-6-27b-947f6d3b9db0.md) | Qwen3.6-27B | autoround-int4 | vllm 0.23.0 | TP=2 | 32768 | 1 | 53.8 output tok/s |
| 2026-07-26 | [tpab/Qwen3.6-27B/autoround-int4_tp2_aggregate_c64](../runs/tp-ab-p2p-qwen3-6-27b-4a15d5aa09ac.md) | Qwen3.6-27B | autoround-int4 | vllm 0.23.0 | TP=2 | 32768 | 64 | 473.1 output tok/s |
| 2026-07-26 | [tpab/Qwen3.6-27B/autoround-int4_tp2_aggregate_c4](../runs/tp-ab-p2p-qwen3-6-27b-88bd8827e0d4.md) | Qwen3.6-27B | autoround-int4 | vllm 0.23.0 | TP=2 | 32768 | 4 | 168.06 output tok/s |
| 2026-07-26 | [tpab/Qwen3.6-27B/autoround-int4_tp2_aggregate_c32](../runs/tp-ab-p2p-qwen3-6-27b-28a55ce76e05.md) | Qwen3.6-27B | autoround-int4 | vllm 0.23.0 | TP=2 | 32768 | 32 | 413.28 output tok/s |
| 2026-07-26 | [tpab/Qwen3.6-27B/autoround-int4_tp2_aggregate_c16](../runs/tp-ab-p2p-qwen3-6-27b-ee858bb27fae.md) | Qwen3.6-27B | autoround-int4 | vllm 0.23.0 | TP=2 | 32768 | 16 | 364.64 output tok/s |
| 2026-07-26 | [tpab/Qwen3.6-27B/autoround-int4_tp2_aggregate_c1](../runs/tp-ab-p2p-qwen3-6-27b-96dac8000606.md) | Qwen3.6-27B | autoround-int4 | vllm 0.23.0 | TP=2 | 32768 | 1 | 45.37 output tok/s |
| 2026-07-26 | [tpab/Qwen3.6-27B/FP8-static_tp4_single_stream](../runs/tp-ab-p2p-qwen3-6-27b-b1cc8527fc77.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 32768 | 1 | 55.14 output tok/s |
| 2026-07-26 | [tpab/Qwen3.6-27B/FP8-static_tp4_aggregate_c64](../runs/tp-ab-p2p-qwen3-6-27b-113b596be2c7.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 32768 | 64 | 293.01 output tok/s |
| 2026-07-26 | [tpab/Qwen3.6-27B/FP8-static_tp4_aggregate_c4](../runs/tp-ab-p2p-qwen3-6-27b-1a3d730bfff4.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 32768 | 4 | 125.74 output tok/s |
| 2026-07-26 | [tpab/Qwen3.6-27B/FP8-static_tp4_aggregate_c32](../runs/tp-ab-p2p-qwen3-6-27b-68a45d450fa4.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 32768 | 32 | 280.99 output tok/s |
| 2026-07-26 | [tpab/Qwen3.6-27B/FP8-static_tp4_aggregate_c16](../runs/tp-ab-p2p-qwen3-6-27b-723808e25f33.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 32768 | 16 | 175.18 output tok/s |
| 2026-07-26 | [tpab/Qwen3.6-27B/FP8-static_tp4_aggregate_c1](../runs/tp-ab-p2p-qwen3-6-27b-7872b608ce78.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=4 | 32768 | 1 | 45.94 output tok/s |
| 2026-07-26 | [tpab/Qwen3.6-27B/FP8-static_tp2_single_stream](../runs/tp-ab-p2p-qwen3-6-27b-0a064da9635c.md) | Qwen3.6-27B | fp8-static | vllm 0.23.0 | TP=2 | 32768 | 1 | 36.28 output tok/s |

Generated from `data/benchmarks.jsonl`. Do not edit by hand.
