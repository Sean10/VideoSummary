---
title: "Cost-Effective, Dense, and Performant Prometheus Storage via QLC - Anthony DAtri, IBM"
date: 2025-01-23
updated: 2025-01-24
tags:
  - "Ceph"
  - "存储优化"
  - "监控"
categories:
  - "视频总结"
outline: deep
---
**会议主题**: Prometheus 时间序列指标存储的性能优化与 Ceph 集成

**主讲人**: Anthony DAtri (IBM)

**会议内容概述**:

1. **Prometheus 简介**: Prometheus 是一个流行的开源监控系统，用于收集和存储时间序列指标。它广泛应用于各种监控场景，并与 Grafana、Node Exporter 等工具集成。

2. **Ceph 监控需求**: Ceph 作为一种分布式存储系统，需要有效的监控来解决物理设备和存储设备的性能问题，以及逻辑层面的指标，如 PG 状态和 IO。

3. **Prometheus 存储挑战**: Prometheus 需要处理大量数据，包括频繁的样本采集和长时间的保留。存储设备的性能对 Prometheus 的查询和告警系统至关重要。

4. **存储设备选择**: 
   - **HDD**：成本较低，但性能不佳，易导致查询超时和告警误报。
   - **SSD**：尤其是 QLC SSD，具有更高的读取性能和更低的延迟，适合 Prometheus 的读密集型工作负载。
   - **QLC SSD**：更高的存储密度、较低的成本和足够的耐久性，是 Prometheus 存储的理想选择。

5. **QLC SSD 在 Ceph 中的应用**: 
   - QLC SSD 的随机读取性能非常适合 Prometheus 的查询需求。
   - Ceph 的 BlueStore 可以通过设置 `optimal IO size` 来优化 QLC SSD 的写入性能。
   - QLC SSD 的耐久性在实际使用中远超其标称值。

6. **实际案例**: 在一个部署了 8000+ 节点的 Prometheus 系统中，使用 15TB 的 QLC SSD 进行存储，预测寿命可达 52 年，实际写入量仅为 0.09 次/天。

7. **Ceph 与 Prometheus 集成**: 
   - Ceph 可以通过 RBD、RGW 等方式为 Prometheus 提供存储，支持 Erasure Coding 以降低存储成本。
   - QLC SSD 的引入使得 Ceph 在存储 Prometheus 数据时既能保证性能，又能降低总体拥有成本（TCO）。

8. **未来展望**: 随着 QLC SSD 技术的进步，Ceph 在存储和性能优化方面的应用将更加广泛。

**会议决定事项**:
- 继续探索 QLC SSD 在 Ceph 中的应用，特别是在 Prometheus 时间序列数据的存储和性能优化方面。
- 进一步研究 Ceph 与 Prometheus 的集成，特别是在 Erasure Coding 和存储分层方面的应用。

**后续行动计划**:
- 在生产环境中部署 QLC SSD 并进行性能测试，验证其在 Ceph 和 Prometheus 集成中的表现。
- 与 SSD 厂商合作，优化 QLC SSD 在 Ceph 中的使用，特别是针对 BlueStore 的 IO 优化。

**参考资料**:
- QLC SSD 耐久性分析工具
- Ceph BlueStore 的 over-provisioning 优化
- SNIA TCO 计算器