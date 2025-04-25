## Elasticsearch Performance Benchmark with Rally
This project aims to benchmark and compare the performance between Elasticsearch 8.17.4(currently using) and the newly released Elasticsearch 9.0.0.
I leverage the official benchmarking tool, Elasticsearch Rally, to automate both load testing and performance analysis across different cluster configurations.

## Python Environment Setup for Elasticsearch Rally Benchmarking
**Note** : esrally is not fully compatible with Python 3.13 (at the time of testing). In order to run Elasticsearch Rally smoothly (which does not yet officially support Python 3.13), it was necessary to downgrade Python to version 3.10.12 using pyenv, a popular Python version management tool. 



## Installing Rally
```bash
pip3 install esrally
```

## What is Rally?
Rally is the official benchmarking framework provided by Elastic.
It enables automated performance testing for Elasticsearch clusters under various workloads and scenarios.

## Key Features:
	•	Official performance benchmarking tool for Elasticsearch.
	•	Supports multiple workloads:
	•	Indexing
	•	Search
	•	Bulk insert
	•	Aggregations
	•	Mixed scenarios (index + search)
	•	Works on single-node or multi-node clusters.
	•	Provides detailed metrics collection for latency, throughput, error rate, indexing speed, etc.
	•	Flexible test scenarios via Tracks (benchmark scripts and datasets).


## Why Use Rally?
1. Elasticsearch Upgrade Comparison : Compare cluster performance before and after upgrading to v9.0.0.
2. Cluster Tuning Verification : Validate the effects of tuning settings like shard count, replica count, indexing buffer, etc.
3. Performance Scaling Analysis : Measure how shard and node configurations impact overall performance.
4. Large-scale Data Ingestion : Test how fast data can be indexed at scale (bulk insert performance).
5. Query and Search Performance : Benchmark latency and throughput for various query types and workloads.


## What Are Tracks?
Track = A Benchmark Scenario (Dataset + Workload Definition)

Rally provides pre-built tracks for realistic testing scenarios.

## Find track list
```bash
esrally list tracks
```

## Run Benchmark Command
```bash
esrally race --track=nyc_taxis --target-hosts=https://192.xxx.xxx.xxx:9200 --pipeline=benchmark-only --client-options="use_ssl:true,verify_certs:false,basic_auth_user:'elastic',basic_auth_password:'MY_PASS_WORD'"
```
```bash
------------------------------------------------------
    _______             __   _____
   / ____(_)___  ____ _/ /  / ___/_________  ________
  / /_  / / __ \/ __ `/ /   \__ \/ ___/ __ \/ ___/ _ \
 / __/ / / / / / /_/ / /   ___/ / /__/ /_/ / /  /  __/
/_/   /_/_/ /_/\__,_/_/   /____/\___/\____/_/   \___/
------------------------------------------------------
            
|                                                         Metric |                                         Task |            Value |   Unit |
|---------------------------------------------------------------:|---------------------------------------------:|-----------------:|-------:|
|                     Cumulative indexing time of primary shards |                                              |     34.7009      |    min |
|             Min cumulative indexing time across primary shards |                                              |      0           |    min |
|          Median cumulative indexing time across primary shards |                                              |      0           |    min |
|             Max cumulative indexing time across primary shards |                                              |     17.995       |    min |
|            Cumulative indexing throttle time of primary shards |                                              |      0           |    min |
|    Min cumulative indexing throttle time across primary shards |                                              |      0           |    min |
| Median cumulative indexing throttle time across primary shards |                                              |      0           |    min |
|    Max cumulative indexing throttle time across primary shards |                                              |      0           |    min |
|                        Cumulative merge time of primary shards |                                              |     47.5129      |    min |
|                       Cumulative merge count of primary shards |                                              |     62           |        |
|                Min cumulative merge time across primary shards |                                              |      0           |    min |
|             Median cumulative merge time across primary shards |                                              |      0           |    min |
|                Max cumulative merge time across primary shards |                                              |     16.406       |    min |
|               Cumulative merge throttle time of primary shards |                                              |     10.1759      |    min |
|       Min cumulative merge throttle time across primary shards |                                              |      0           |    min |
|    Median cumulative merge throttle time across primary shards |                                              |      0           |    min |
|       Max cumulative merge throttle time across primary shards |                                              |      9.25237     |    min |
|                      Cumulative refresh time of primary shards |                                              |      0.54595     |    min |
|                     Cumulative refresh count of primary shards |                                              |   1520           |        |
|              Min cumulative refresh time across primary shards |                                              |      0           |    min |
|           Median cumulative refresh time across primary shards |                                              |      0           |    min |
|              Max cumulative refresh time across primary shards |                                              |      0.2769      |    min |
|                        Cumulative flush time of primary shards |                                              |      4.09032     |    min |
|                       Cumulative flush count of primary shards |                                              |    556           |        |
|                Min cumulative flush time across primary shards |                                              |      0           |    min |
|             Median cumulative flush time across primary shards |                                              |      6.66667e-05 |    min |
|                Max cumulative flush time across primary shards |                                              |      3.47187     |    min |
|                                        Total Young Gen GC time |                                              |     26.172       |      s |
|                                       Total Young Gen GC count |                                              |    300           |        |
|                                          Total Old Gen GC time |                                              |      0           |      s |
|                                         Total Old Gen GC count |                                              |      0           |        |
|                                                   Dataset size |                                              |     38.2582      |     GB |
|                                                     Store size |                                              |     38.2582      |     GB |
|                                                  Translog size |                                              |      2.40747e-06 |     GB |
|                                         Heap used for segments |                                              |      0           |     MB |
|                                       Heap used for doc values |                                              |      0           |     MB |
|                                            Heap used for terms |                                              |      0           |     MB |
|                                            Heap used for norms |                                              |      0           |     MB |
|                                           Heap used for points |                                              |      0           |     MB |
|                                    Heap used for stored fields |                                              |      0           |     MB |
|                                                  Segment count |                                              |    153           |        |
|                                    Total Ingest Pipeline count |                                              |      0           |        |
|                                     Total Ingest Pipeline time |                                              |      0           |      s |
|                                   Total Ingest Pipeline failed |                                              |      0           |        |
|                                                 Min Throughput |                                 index-append |   1474.24        | docs/s |
|                                                Mean Throughput |                                 index-append |   1994.9         | docs/s |
|                                              Median Throughput |                                 index-append |   2042.34        | docs/s |
|                                                 Max Throughput |                                 index-append |   2471.5         | docs/s |
|                                        50th percentile latency |                                 index-append |   2077.09        |     ms |
|                                        90th percentile latency |                                 index-append |   2954.61        |     ms |
|                                        99th percentile latency |                                 index-append |   6684.82        |     ms |
|                                       100th percentile latency |                                 index-append |   8332.53        |     ms |
|                                   50th percentile service time |                                 index-append |   2077.09        |     ms |
|                                   90th percentile service time |                                 index-append |   2954.61        |     ms |
|                                   99th percentile service time |                                 index-append |   6684.82        |     ms |
|                                  100th percentile service time |                                 index-append |   8332.53        |     ms |
|                                                     error rate |                                 index-append |      0           |      % |
|                                                 Min Throughput |                          refresh-after-index |      7.64        |  ops/s |
|                                                Mean Throughput |                          refresh-after-index |      7.64        |  ops/s |
|                                              Median Throughput |                          refresh-after-index |      7.64        |  ops/s |
|                                                 Max Throughput |                          refresh-after-index |      7.64        |  ops/s |
|                                       100th percentile latency |                          refresh-after-index |    129.67        |     ms |
|                                  100th percentile service time |                          refresh-after-index |    129.67        |     ms |
|                                                     error rate |                          refresh-after-index |      0           |      % |
|                                                 Min Throughput |        index-update-concurrent-with-searches |   2902.4         | docs/s |
|                                                Mean Throughput |        index-update-concurrent-with-searches |   3101.46        | docs/s |
|                                              Median Throughput |        index-update-concurrent-with-searches |   3057.32        | docs/s |
|                                                 Max Throughput |        index-update-concurrent-with-searches |   3551.85        | docs/s |
|                                        50th percentile latency |        index-update-concurrent-with-searches |   1710.44        |     ms |
|                                        90th percentile latency |        index-update-concurrent-with-searches |   2129.31        |     ms |
|                                       100th percentile latency |        index-update-concurrent-with-searches |   3180.33        |     ms |
|                                   50th percentile service time |        index-update-concurrent-with-searches |   1710.44        |     ms |
|                                   90th percentile service time |        index-update-concurrent-with-searches |   2129.31        |     ms |
|                                  100th percentile service time |        index-update-concurrent-with-searches |   3180.33        |     ms |
|                                                     error rate |        index-update-concurrent-with-searches |      0           |      % |
|                                                 Min Throughput | knn-search-100-1000-concurrent-with-indexing |     10.81        |  ops/s |
|                                                Mean Throughput | knn-search-100-1000-concurrent-with-indexing |     12.92        |  ops/s |
|                                              Median Throughput | knn-search-100-1000-concurrent-with-indexing |     13.01        |  ops/s |
|                                                 Max Throughput | knn-search-100-1000-concurrent-with-indexing |     13.32        |  ops/s |
|                                        50th percentile latency | knn-search-100-1000-concurrent-with-indexing |     54.5488      |     ms |
|                                        90th percentile latency | knn-search-100-1000-concurrent-with-indexing |    132.226       |     ms |
|                                        99th percentile latency | knn-search-100-1000-concurrent-with-indexing |    368.523       |     ms |
|                                      99.9th percentile latency | knn-search-100-1000-concurrent-with-indexing |    739.37        |     ms |
|                                       100th percentile latency | knn-search-100-1000-concurrent-with-indexing |   1229.45        |     ms |
|                                   50th percentile service time | knn-search-100-1000-concurrent-with-indexing |     54.5488      |     ms |
|                                   90th percentile service time | knn-search-100-1000-concurrent-with-indexing |    132.226       |     ms |
|                                   99th percentile service time | knn-search-100-1000-concurrent-with-indexing |    368.523       |     ms |
|                                 99.9th percentile service time | knn-search-100-1000-concurrent-with-indexing |    739.37        |     ms |
|                                  100th percentile service time | knn-search-100-1000-concurrent-with-indexing |   1229.45        |     ms |
|                                                     error rate | knn-search-100-1000-concurrent-with-indexing |      0           |      % |
|                                                 Min Throughput |                         refresh-after-update |     18.02        |  ops/s |
|                                                Mean Throughput |                         refresh-after-update |     18.02        |  ops/s |
|                                              Median Throughput |                         refresh-after-update |     18.02        |  ops/s |
|                                                 Max Throughput |                         refresh-after-update |     18.02        |  ops/s |
|                                       100th percentile latency |                         refresh-after-update |     53.678       |     ms |
|                                  100th percentile service time |                         refresh-after-update |     53.678       |     ms |
|                                                     error rate |                         refresh-after-update |      0           |      % |
|                                                 Min Throughput |          knn-search-10-100_multiple_segments |     28.41        |  ops/s |
|                                                Mean Throughput |          knn-search-10-100_multiple_segments |     36.11        |  ops/s |
|                                              Median Throughput |          knn-search-10-100_multiple_segments |     36.98        |  ops/s |
|                                                 Max Throughput |          knn-search-10-100_multiple_segments |     38.31        |  ops/s |
|                                        50th percentile latency |          knn-search-10-100_multiple_segments |     17.5961      |     ms |
|                                        90th percentile latency |          knn-search-10-100_multiple_segments |     25.4179      |     ms |
|                                        99th percentile latency |          knn-search-10-100_multiple_segments |    316.969       |     ms |
|                                      99.9th percentile latency |          knn-search-10-100_multiple_segments |    345.932       |     ms |
|                                       100th percentile latency |          knn-search-10-100_multiple_segments |    387.85        |     ms |
|                                   50th percentile service time |          knn-search-10-100_multiple_segments |     17.5961      |     ms |
|                                   90th percentile service time |          knn-search-10-100_multiple_segments |     25.4179      |     ms |
|                                   99th percentile service time |          knn-search-10-100_multiple_segments |    316.969       |     ms |
|                                 99.9th percentile service time |          knn-search-10-100_multiple_segments |    345.932       |     ms |
|                                  100th percentile service time |          knn-search-10-100_multiple_segments |    387.85        |     ms |
|                                                     error rate |          knn-search-10-100_multiple_segments |      0           |      % |
|                                                 Min Throughput |        knn-search-100-1000_multiple_segments |     23.56        |  ops/s |
|                                                Mean Throughput |        knn-search-100-1000_multiple_segments |     25.99        |  ops/s |
|                                              Median Throughput |        knn-search-100-1000_multiple_segments |     26.21        |  ops/s |
|                                                 Max Throughput |        knn-search-100-1000_multiple_segments |     27.6         |  ops/s |
|                                        50th percentile latency |        knn-search-100-1000_multiple_segments |     29.6561      |     ms |
|                                        90th percentile latency |        knn-search-100-1000_multiple_segments |     43.257       |     ms |
|                                        99th percentile latency |        knn-search-100-1000_multiple_segments |    342.285       |     ms |
|                                      99.9th percentile latency |        knn-search-100-1000_multiple_segments |    484.284       |     ms |
|                                       100th percentile latency |        knn-search-100-1000_multiple_segments |    588.48        |     ms |
|                                   50th percentile service time |        knn-search-100-1000_multiple_segments |     29.6561      |     ms |
|                                   90th percentile service time |        knn-search-100-1000_multiple_segments |     43.257       |     ms |
|                                   99th percentile service time |        knn-search-100-1000_multiple_segments |    342.285       |     ms |
|                                 99.9th percentile service time |        knn-search-100-1000_multiple_segments |    484.284       |     ms |
|                                  100th percentile service time |        knn-search-100-1000_multiple_segments |    588.48        |     ms |
|                                                     error rate |        knn-search-100-1000_multiple_segments |      0           |      % |
|                                                 Min Throughput |                                  force-merge |      0           |  ops/s |
|                                                Mean Throughput |                                  force-merge |      0           |  ops/s |
|                                              Median Throughput |                                  force-merge |      0           |  ops/s |
|                                                 Max Throughput |                                  force-merge |      0           |  ops/s |
|                                       100th percentile latency |                                  force-merge | 357184           |     ms |
|                                  100th percentile service time |                                  force-merge | 357184           |     ms |
|                                                     error rate |                                  force-merge |      0           |      % |
|                                                 Min Throughput |                            knn-search-10-100 |     24.01        |  ops/s |
|                                                Mean Throughput |                            knn-search-10-100 |     30.07        |  ops/s |
|                                              Median Throughput |                            knn-search-10-100 |     30.17        |  ops/s |
|                                                 Max Throughput |                            knn-search-10-100 |     33.76        |  ops/s |
|                                        50th percentile latency |                            knn-search-10-100 |     14.9129      |     ms |
|                                        90th percentile latency |                            knn-search-10-100 |     27.0525      |     ms |
|                                        99th percentile latency |                            knn-search-10-100 |    347.794       |     ms |
|                                      99.9th percentile latency |                            knn-search-10-100 |    564.353       |     ms |
|                                       100th percentile latency |                            knn-search-10-100 |    653.526       |     ms |
|                                   50th percentile service time |                            knn-search-10-100 |     14.9129      |     ms |
|                                   90th percentile service time |                            knn-search-10-100 |     27.0525      |     ms |
|                                   99th percentile service time |                            knn-search-10-100 |    347.794       |     ms |
|                                 99.9th percentile service time |                            knn-search-10-100 |    564.353       |     ms |
|                                  100th percentile service time |                            knn-search-10-100 |    653.526       |     ms |
|                                                     error rate |                            knn-search-10-100 |      0           |      % |
|                                                 Min Throughput |                          knn-search-100-1000 |     28.22        |  ops/s |
|                                                Mean Throughput |                          knn-search-100-1000 |     30.75        |  ops/s |
|                                              Median Throughput |                          knn-search-100-1000 |     31           |  ops/s |
|                                                 Max Throughput |                          knn-search-100-1000 |     32.8         |  ops/s |
|                                        50th percentile latency |                          knn-search-100-1000 |     21.5127      |     ms |
|                                        90th percentile latency |                          knn-search-100-1000 |     31.7156      |     ms |
|                                        99th percentile latency |                          knn-search-100-1000 |    327.866       |     ms |
|                                      99.9th percentile latency |                          knn-search-100-1000 |    370.056       |     ms |
|                                       100th percentile latency |                          knn-search-100-1000 |    384.448       |     ms |
|                                   50th percentile service time |                          knn-search-100-1000 |     21.5127      |     ms |
|                                   90th percentile service time |                          knn-search-100-1000 |     31.7156      |     ms |
|                                   99th percentile service time |                          knn-search-100-1000 |    327.866       |     ms |
|                                 99.9th percentile service time |                          knn-search-100-1000 |    370.056       |     ms |
|                                  100th percentile service time |                          knn-search-100-1000 |    384.448       |     ms |
|                                                     error rate |                          knn-search-100-1000 |      0           |      % |
|                                                 Min Throughput |                           script-score-query |      4.14        |  ops/s |
|                                                Mean Throughput |                           script-score-query |      4.99        |  ops/s |
|                                              Median Throughput |                           script-score-query |      5.08        |  ops/s |
|                                                 Max Throughput |                           script-score-query |      5.19        |  ops/s |
|                                        50th percentile latency |                           script-score-query |    162.976       |     ms |
|                                        90th percentile latency |                           script-score-query |    233.412       |     ms |
|                                        99th percentile latency |                           script-score-query |    503.213       |     ms |
|                                      99.9th percentile latency |                           script-score-query |    770.299       |     ms |
|                                       100th percentile latency |                           script-score-query |    857.939       |     ms |
|                                   50th percentile service time |                           script-score-query |    162.976       |     ms |
|                                   90th percentile service time |                           script-score-query |    233.412       |     ms |
|                                   99th percentile service time |                           script-score-query |    503.213       |     ms |
|                                 99.9th percentile service time |                           script-score-query |    770.299       |     ms |
|                                  100th percentile service time |                           script-score-query |    857.939       |     ms |
|                                                     error rate |                           script-score-query |      0           |      % |


----------------------------------
[INFO] SUCCESS (took 4170 seconds)
----------------------------------
```


Rally 2.12.0 공식문서 
https://esrally.readthedocs.io/en/stable/
공식 트랙 리포지토리
https://github.com/elastic/rally-tracks