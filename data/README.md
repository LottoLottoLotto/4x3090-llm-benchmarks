# Data files

`benchmarks.jsonl` is the public source of truth. Each line is one schema-v2
measurement. `benchmarks.sqlite` contains the same rows in the `runs` table.

`snapshot.json` records the row counts, covered date range, and JSONL checksum.
All three files are rebuilt together by `scripts/build_archive.py`.
