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

## Run Benchmark Command(8.17.4)
```bash
esrally race --track=nyc_taxis --target-hosts=https://192.xxx.xxx.xxx:9200 --pipeline=benchmark-only --client-options="use_ssl:true,verify_certs:false,basic_auth_user:'elastic',basic_auth_password:'MY_PASS_WORD'"
```

## ver.8.17.4 Score
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



## Benchmark Summary (Elasticsearch Rally Result) ver.8.17.4
Indexing Performance
	•	Mean throughput: 1994.9 docs/sec (Approximately 2000 documents successfully indexed per second)
	•	50th percentile (median latency): 2077ms (Half of the indexing operations completed within 2 seconds)
	•	99th percentile latency: Some operations show slower performance (long-tail latency issue)

Merge, Refresh, and Flush Performance
	•	Merge throttle time detected: Indicates that merge operations were throttled due to disk I/O or CPU resource limits
	•	Refresh operations: 1520 times
	•	Flush operations: 556 times

Garbage Collection
	•	Old Generation GC time: 0 seconds → No memory issues (Good sign)
	•	Young Generation GC time: Present, but within acceptable range

Dataset and Storage
	•	Dataset size: 38.25 GB (Large-scale indexing scenario)
	•	Segment count: 153 segments → A higher segment count may impact search performance (merge tuning recommended)

KNN Search (Dense Vector Search)
	•	Average throughput: 30 operations per second (stable performance)
	•	50th percentile latency: 21.5ms (Half of the KNN search queries completed within 21ms)
	•	99th percentile latency: Over 300ms → Some queries experienced higher latency (long-tail latency present)

Script Score Query (Script-based scoring)
	•	Average throughput: 5 operations per second (expected slower performance compared to KNN)
	•	Latency behavior: Similar percentile latency as KNN but with lower throughput

Latency Overview
	•	Indexing (index-append):
		•	Median latency: 2 seconds
		•	99th percentile latency: 6.6 seconds → Long-tail latency observed, potential bottleneck
	•	KNN Search:
		•	Average latency: 20–30ms (Good)
		•	99th percentile latency: Above 300ms → Some slow queries detected

## Key Points
	•	Indexing throughput: ~2000 docs/sec → Solid indexing performance
	•	KNN Search throughput: ~30 ops/sec → Stable and consistent
	•	Indexing latency spikes: Some operations affected by merge throttling and long-tail latency
	•	Memory management: No Old Generation GC issues detected → Healthy memory usage
	•	Search error rate: 0% → All scenarios executed successfully without failures



## Run Benchmark Command(8.17.4)
```bash
esrally race --track=dense_vector --target-hosts=https://192.168.219.157:9200 --pipeline=benchmark-only --client-options="use_ssl:true,verify_certs:false,basic_auth_user:elastic,basic_auth_password:elastic" --kill-running-processes
```

## ver.9.0.0 Score
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
|                     Cumulative indexing time of primary shards |                                              |     20.5683      |    min |
|             Min cumulative indexing time across primary shards |                                              |     10.2722      |    min |
|          Median cumulative indexing time across primary shards |                                              |     10.2842      |    min |
|             Max cumulative indexing time across primary shards |                                              |     10.2961      |    min |
|            Cumulative indexing throttle time of primary shards |                                              |      0           |    min |
|    Min cumulative indexing throttle time across primary shards |                                              |      0           |    min |
| Median cumulative indexing throttle time across primary shards |                                              |      0           |    min |
|    Max cumulative indexing throttle time across primary shards |                                              |      0           |    min |
|                        Cumulative merge time of primary shards |                                              |     37.2185      |    min |
|                       Cumulative merge count of primary shards |                                              |     53           |        |
|                Min cumulative merge time across primary shards |                                              |     18.3175      |    min |
|             Median cumulative merge time across primary shards |                                              |     18.6092      |    min |
|                Max cumulative merge time across primary shards |                                              |     18.901       |    min |
|               Cumulative merge throttle time of primary shards |                                              |      0.79855     |    min |
|       Min cumulative merge throttle time across primary shards |                                              |      0.373233    |    min |
|    Median cumulative merge throttle time across primary shards |                                              |      0.399275    |    min |
|       Max cumulative merge throttle time across primary shards |                                              |      0.425317    |    min |
|                      Cumulative refresh time of primary shards |                                              |      0.480433    |    min |
|                     Cumulative refresh count of primary shards |                                              |    530           |        |
|              Min cumulative refresh time across primary shards |                                              |      0.221067    |    min |
|           Median cumulative refresh time across primary shards |                                              |      0.240217    |    min |
|              Max cumulative refresh time across primary shards |                                              |      0.259367    |    min |
|                        Cumulative flush time of primary shards |                                              |      0.415867    |    min |
|                       Cumulative flush count of primary shards |                                              |     40           |        |
|                Min cumulative flush time across primary shards |                                              |      0.206633    |    min |
|             Median cumulative flush time across primary shards |                                              |      0.207933    |    min |
|                Max cumulative flush time across primary shards |                                              |      0.209233    |    min |
|                                        Total Young Gen GC time |                                              |     10.651       |      s |
|                                       Total Young Gen GC count |                                              |     97           |        |
|                                          Total Old Gen GC time |                                              |      0           |      s |
|                                         Total Old Gen GC count |                                              |      0           |        |
|                                                   Dataset size |                                              |      1.33342     |     GB |
|                                                     Store size |                                              |      1.33342     |     GB |
|                                                  Translog size |                                              |      1.02445e-07 |     GB |
|                                         Heap used for segments |                                              |      0           |     MB |
|                                       Heap used for doc values |                                              |      0           |     MB |
|                                            Heap used for terms |                                              |      0           |     MB |
|                                            Heap used for norms |                                              |      0           |     MB |
|                                           Heap used for points |                                              |      0           |     MB |
|                                    Heap used for stored fields |                                              |      0           |     MB |
|                                                  Segment count |                                              |      2           |        |
|                                    Total Ingest Pipeline count |                                              |      0           |        |
|                                     Total Ingest Pipeline time |                                              |      0           |      s |
|                                   Total Ingest Pipeline failed |                                              |      0           |        |
|                                                 Min Throughput |                                 index-append |   2285.18        | docs/s |
|                                                Mean Throughput |                                 index-append |   2456.9         | docs/s |
|                                              Median Throughput |                                 index-append |   2413.82        | docs/s |
|                                                 Max Throughput |                                 index-append |   2785.41        | docs/s |
|                                        50th percentile latency |                                 index-append |   2135.43        |     ms |
|                                        90th percentile latency |                                 index-append |   2756.55        |     ms |
|                                        99th percentile latency |                                 index-append |   4511.9         |     ms |
|                                       100th percentile latency |                                 index-append |   7220.84        |     ms |
|                                   50th percentile service time |                                 index-append |   2135.43        |     ms |
|                                   90th percentile service time |                                 index-append |   2756.55        |     ms |
|                                   99th percentile service time |                                 index-append |   4511.9         |     ms |
|                                  100th percentile service time |                                 index-append |   7220.84        |     ms |
|                                                     error rate |                                 index-append |      0           |      % |
|                                                 Min Throughput |                          refresh-after-index |      1.69        |  ops/s |
|                                                Mean Throughput |                          refresh-after-index |      1.69        |  ops/s |
|                                              Median Throughput |                          refresh-after-index |      1.69        |  ops/s |
|                                                 Max Throughput |                          refresh-after-index |      1.69        |  ops/s |
|                                       100th percentile latency |                          refresh-after-index |    591.272       |     ms |
|                                  100th percentile service time |                          refresh-after-index |    591.272       |     ms |
|                                                     error rate |                          refresh-after-index |      0           |      % |
|                                                 Min Throughput |        index-update-concurrent-with-searches |   1599.05        | docs/s |
|                                                Mean Throughput |        index-update-concurrent-with-searches |   1761.6         | docs/s |
|                                              Median Throughput |        index-update-concurrent-with-searches |   1766.36        | docs/s |
|                                                 Max Throughput |        index-update-concurrent-with-searches |   1967.34        | docs/s |
|                                        50th percentile latency |        index-update-concurrent-with-searches |   2620.98        |     ms |
|                                        90th percentile latency |        index-update-concurrent-with-searches |   3837.58        |     ms |
|                                       100th percentile latency |        index-update-concurrent-with-searches |   4803.82        |     ms |
|                                   50th percentile service time |        index-update-concurrent-with-searches |   2620.98        |     ms |
|                                   90th percentile service time |        index-update-concurrent-with-searches |   3837.58        |     ms |
|                                  100th percentile service time |        index-update-concurrent-with-searches |   4803.82        |     ms |
|                                                     error rate |        index-update-concurrent-with-searches |      0           |      % |
|                                                 Min Throughput | knn-search-100-1000-concurrent-with-indexing |      4.91        |  ops/s |
|                                                Mean Throughput | knn-search-100-1000-concurrent-with-indexing |      5.86        |  ops/s |
|                                              Median Throughput | knn-search-100-1000-concurrent-with-indexing |      5.91        |  ops/s |
|                                                 Max Throughput | knn-search-100-1000-concurrent-with-indexing |      6.38        |  ops/s |
|                                        50th percentile latency | knn-search-100-1000-concurrent-with-indexing |    127.34        |     ms |
|                                        90th percentile latency | knn-search-100-1000-concurrent-with-indexing |    294.263       |     ms |
|                                        99th percentile latency | knn-search-100-1000-concurrent-with-indexing |    688.142       |     ms |
|                                      99.9th percentile latency | knn-search-100-1000-concurrent-with-indexing |   1191.07        |     ms |
|                                       100th percentile latency | knn-search-100-1000-concurrent-with-indexing |   1473.71        |     ms |
|                                   50th percentile service time | knn-search-100-1000-concurrent-with-indexing |    127.34        |     ms |
|                                   90th percentile service time | knn-search-100-1000-concurrent-with-indexing |    294.263       |     ms |
|                                   99th percentile service time | knn-search-100-1000-concurrent-with-indexing |    688.142       |     ms |
|                                 99.9th percentile service time | knn-search-100-1000-concurrent-with-indexing |   1191.07        |     ms |
|                                  100th percentile service time | knn-search-100-1000-concurrent-with-indexing |   1473.71        |     ms |
|                                                     error rate | knn-search-100-1000-concurrent-with-indexing |      0           |      % |
|                                                 Min Throughput |                         refresh-after-update |     12.2         |  ops/s |
|                                                Mean Throughput |                         refresh-after-update |     12.2         |  ops/s |
|                                              Median Throughput |                         refresh-after-update |     12.2         |  ops/s |
|                                                 Max Throughput |                         refresh-after-update |     12.2         |  ops/s |
|                                       100th percentile latency |                         refresh-after-update |     80.3504      |     ms |
|                                  100th percentile service time |                         refresh-after-update |     80.3504      |     ms |
|                                                     error rate |                         refresh-after-update |      0           |      % |
|                                                 Min Throughput |          knn-search-10-100_multiple_segments |     20.59        |  ops/s |
|                                                Mean Throughput |          knn-search-10-100_multiple_segments |     28.27        |  ops/s |
|                                              Median Throughput |          knn-search-10-100_multiple_segments |     29.22        |  ops/s |
|                                                 Max Throughput |          knn-search-10-100_multiple_segments |     30.64        |  ops/s |
|                                        50th percentile latency |          knn-search-10-100_multiple_segments |     20.681       |     ms |
|                                        90th percentile latency |          knn-search-10-100_multiple_segments |     36.2467      |     ms |
|                                        99th percentile latency |          knn-search-10-100_multiple_segments |    332.51        |     ms |
|                                      99.9th percentile latency |          knn-search-10-100_multiple_segments |    373.194       |     ms |
|                                       100th percentile latency |          knn-search-10-100_multiple_segments |    414.434       |     ms |
|                                   50th percentile service time |          knn-search-10-100_multiple_segments |     20.681       |     ms |
|                                   90th percentile service time |          knn-search-10-100_multiple_segments |     36.2467      |     ms |
|                                   99th percentile service time |          knn-search-10-100_multiple_segments |    332.51        |     ms |
|                                 99.9th percentile service time |          knn-search-10-100_multiple_segments |    373.194       |     ms |
|                                  100th percentile service time |          knn-search-10-100_multiple_segments |    414.434       |     ms |
|                                                     error rate |          knn-search-10-100_multiple_segments |      0           |      % |
|                                                 Min Throughput |        knn-search-100-1000_multiple_segments |     18.68        |  ops/s |
|                                                Mean Throughput |        knn-search-100-1000_multiple_segments |     19.35        |  ops/s |
|                                              Median Throughput |        knn-search-100-1000_multiple_segments |     19.43        |  ops/s |
|                                                 Max Throughput |        knn-search-100-1000_multiple_segments |     19.89        |  ops/s |
|                                        50th percentile latency |        knn-search-100-1000_multiple_segments |     37.4816      |     ms |
|                                        90th percentile latency |        knn-search-100-1000_multiple_segments |     55.3641      |     ms |
|                                        99th percentile latency |        knn-search-100-1000_multiple_segments |    363.392       |     ms |
|                                      99.9th percentile latency |        knn-search-100-1000_multiple_segments |    391.91        |     ms |
|                                       100th percentile latency |        knn-search-100-1000_multiple_segments |    398.414       |     ms |
|                                   50th percentile service time |        knn-search-100-1000_multiple_segments |     37.4816      |     ms |
|                                   90th percentile service time |        knn-search-100-1000_multiple_segments |     55.3641      |     ms |
|                                   99th percentile service time |        knn-search-100-1000_multiple_segments |    363.392       |     ms |
|                                 99.9th percentile service time |        knn-search-100-1000_multiple_segments |    391.91        |     ms |
|                                  100th percentile service time |        knn-search-100-1000_multiple_segments |    398.414       |     ms |
|                                                     error rate |        knn-search-100-1000_multiple_segments |      0           |      % |
|                                                 Min Throughput |                                  force-merge |      0           |  ops/s |
|                                                Mean Throughput |                                  force-merge |      0           |  ops/s |
|                                              Median Throughput |                                  force-merge |      0           |  ops/s |
|                                                 Max Throughput |                                  force-merge |      0           |  ops/s |
|                                       100th percentile latency |                                  force-merge | 636516           |     ms |
|                                  100th percentile service time |                                  force-merge | 636516           |     ms |
|                                                     error rate |                                  force-merge |      0           |      % |
|                                                 Min Throughput |                            knn-search-10-100 |     43.71        |  ops/s |
|                                                Mean Throughput |                            knn-search-10-100 |     50.54        |  ops/s |
|                                              Median Throughput |                            knn-search-10-100 |     50.3         |  ops/s |
|                                                 Max Throughput |                            knn-search-10-100 |     55.49        |  ops/s |
|                                        50th percentile latency |                            knn-search-10-100 |     13.3578      |     ms |
|                                        90th percentile latency |                            knn-search-10-100 |     24.22        |     ms |
|                                        99th percentile latency |                            knn-search-10-100 |    164.224       |     ms |
|                                      99.9th percentile latency |                            knn-search-10-100 |    371.773       |     ms |
|                                       100th percentile latency |                            knn-search-10-100 |    381.88        |     ms |
|                                   50th percentile service time |                            knn-search-10-100 |     13.3578      |     ms |
|                                   90th percentile service time |                            knn-search-10-100 |     24.22        |     ms |
|                                   99th percentile service time |                            knn-search-10-100 |    164.224       |     ms |
|                                 99.9th percentile service time |                            knn-search-10-100 |    371.773       |     ms |
|                                  100th percentile service time |                            knn-search-10-100 |    381.88        |     ms |
|                                                     error rate |                            knn-search-10-100 |      0           |      % |
|                                                 Min Throughput |                          knn-search-100-1000 |     29.16        |  ops/s |
|                                                Mean Throughput |                          knn-search-100-1000 |     33.83        |  ops/s |
|                                              Median Throughput |                          knn-search-100-1000 |     34.49        |  ops/s |
|                                                 Max Throughput |                          knn-search-100-1000 |     35.82        |  ops/s |
|                                        50th percentile latency |                          knn-search-100-1000 |     18.1991      |     ms |
|                                        90th percentile latency |                          knn-search-100-1000 |     29.4852      |     ms |
|                                        99th percentile latency |                          knn-search-100-1000 |    298.588       |     ms |
|                                      99.9th percentile latency |                          knn-search-100-1000 |    347.916       |     ms |
|                                       100th percentile latency |                          knn-search-100-1000 |    375.315       |     ms |
|                                   50th percentile service time |                          knn-search-100-1000 |     18.1991      |     ms |
|                                   90th percentile service time |                          knn-search-100-1000 |     29.4852      |     ms |
|                                   99th percentile service time |                          knn-search-100-1000 |    298.588       |     ms |
|                                 99.9th percentile service time |                          knn-search-100-1000 |    347.916       |     ms |
|                                  100th percentile service time |                          knn-search-100-1000 |    375.315       |     ms |
|                                                     error rate |                          knn-search-100-1000 |      0           |      % |
|                                                 Min Throughput |                           script-score-query |      6.04        |  ops/s |
|                                                Mean Throughput |                           script-score-query |      6.15        |  ops/s |
|                                              Median Throughput |                           script-score-query |      6.16        |  ops/s |
|                                                 Max Throughput |                           script-score-query |      6.2         |  ops/s |
|                                        50th percentile latency |                           script-score-query |    151.52        |     ms |
|                                        90th percentile latency |                           script-score-query |    174.84        |     ms |
|                                        99th percentile latency |                           script-score-query |    421.299       |     ms |
|                                      99.9th percentile latency |                           script-score-query |    608.292       |     ms |
|                                       100th percentile latency |                           script-score-query |    675.356       |     ms |
|                                   50th percentile service time |                           script-score-query |    151.52        |     ms |
|                                   90th percentile service time |                           script-score-query |    174.84        |     ms |
|                                   99th percentile service time |                           script-score-query |    421.299       |     ms |
|                                 99.9th percentile service time |                           script-score-query |    608.292       |     ms |
|                                  100th percentile service time |                           script-score-query |    675.356       |     ms |
|                                                     error rate |                           script-score-query |      0           |      % |


----------------------------------
[INFO] SUCCESS (took 3755 seconds)
----------------------------------
```



## Benchmark Summary (Elasticsearch Rally Result) ver.9.0.0
Indexing Performance
	•	Mean throughput: 2456.9 docs/sec (Approximately 2450+ documents successfully indexed per second)
	•	50th percentile (median latency): 2135ms (Half of the indexing operations completed within ~2.1 seconds)
	•	99th percentile latency: 4511.9ms → Some operations show slower performance (long-tail latency issue)


Merge, Refresh, and Flush Performance
	•	Merge throttle time detected: 0.79 min → Merge operations experienced minimal throttling
	•	Merge operations: 53 times
	•	Refresh operations: 530 times
	•	Flush operations: 40 times

Garbage Collection
	•	Old Generation GC time: 0 seconds → No memory issues (Healthy memory usage)
	•	Young Generation GC time: 10.65 seconds across 97 collections → Within acceptable limits

Dataset and Storage
	•	Dataset size: 1.33 GB (Used default dense_vector track dataset)
	•	Segment count: 2 segments → Highly optimized; lower segment count improves search performance

KNN Search (Dense Vector Search)
	•	Average throughput:
		•	knn-search-100-1000: 33.8 ops/sec
		•	knn-search-10-100: 50.5 ops/sec (Best case)
	•	50th percentile latency:
		•	knn-search-100-1000: 18.2ms
		•	knn-search-10-100: 13.3ms
	•	99th percentile latency:
		•	knn-search-100-1000: 298ms
		•	knn-search-10-100: 164ms
	•	Long-tail latency present, but overall improved latency distribution

Script Score Query (Script-based scoring)
	•	Average throughput: 6.15 operations per second (Expected lower performance compared to KNN)
	•	Latency behavior: 50th percentile latency at 151ms; 99th percentile at 421ms → Slower than KNN as expected

Latency Overview
	•	Indexing (index-append):
		•	Median latency: 2.1 seconds
		•	99th percentile latency: 4.5 seconds → Long-tail latency observed
	•	KNN Search:
		•	Average latency: 13–30ms depending on query type
		•	99th percentile latency: ~300ms for high-load queries

## Key Points
	•	Indexing throughput: ~2450 docs/sec → Improved performance over 8.17.4
	•	KNN Search throughput: Up to 50 ops/sec → Significant gain in query speed
	•	Indexing latency: Slightly improved with less throttling; long-tail cases remain
	•	Memory management: No Old Generation GC → Very stable memory usage
	•	Segment optimization: Only 2 segments used → Excellent for search speed
	•	Search error rate: 0% → All benchmark scenarios completed without failure

Rally 2.12.0 공식문서 
https://esrally.readthedocs.io/en/stable/

공식 트랙 리포지토리
https://github.com/elastic/rally-tracks