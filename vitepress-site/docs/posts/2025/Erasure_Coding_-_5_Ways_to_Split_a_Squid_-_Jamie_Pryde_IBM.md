---
title: "Erasure Coding- 5 Ways to Split a Squid - Jamie Pryde, IBM"
date: 2025-01-26
updated: 2025-01-26
tags:
  - "Ceph"
  - "Erasure Coding"
  - "性能优化"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要：Ceph中Erasure Coding插件的性能优化讨论

**会议主题**：Ceph中Erasure Coding插件的性能优化及使用建议

**主讲人**：Jamie Pride（IBM英国，软件开发工程师，专注于Ceph的Erasure Coding性能优化）

**会议时间**：未知



#### 1. **会议背景**
   - Jamie Pride在IBM工作近10年，主要从事存储系统开发，过去一年专注于Ceph的Erasure Coding性能优化，特别是针对块存储和文件存储工作负载的性能提升。
   - 本次会议主要讨论Ceph中Erasure Coding的不同插件及其性能表现，并分享一些优化建议。

#### 2. **主要议题**
   - **Erasure Coding简介**：
     - Erasure Coding是一种数据保护机制，通过将数据分成多个数据块（K）和生成额外的校验块（M）来实现数据冗余。
     - 相比于传统的三副本复制（3X replication），Erasure Coding可以显著降低存储开销，例如4+2的Erasure Coding配置（K=4, M=2）仅需要1.5倍的存储开销。
     - Erasure Coding的灵活性允许设置不同的M值，例如M=3或M=4，以提高容错能力，但会增加存储开销和性能成本。

   - **支持的Erasure Coding插件**：
     - **Jerasure**：Ceph的默认Erasure Coding插件，广泛使用，但不支持现代的AVX指令集，且不再维护。
     - **ISA-L（Intel Storage Acceleration Library）**：支持Intel、AMD和ARM CPU，且支持AVX、AVX2和AVX512指令集，性能优于Jerasure，且仍在维护。
     - **LRC、Shec、Clay**：这些插件旨在优化OSD故障时的恢复效率，但使用较少。

   - **性能基准测试**：
     - 使用Ceph的Erasure Code Benchmark工具对不同插件进行性能测试，结果显示ISA-L在现代CPU上（支持AVX512）的编码和解码性能比Jerasure高出4到5倍。
     - 即使在仅支持AVX2的AMD CPU上，ISA-L的性能也比Jerasure高出约2倍。

   - **Telemetry数据分析**：
     - 从Ceph的Telemetry数据来看，约有1/4到1/3的Ceph集群使用Erasure Coding，其中大部分使用Jerasure插件和默认的Reed Solomon Vandermonde算法。
     - 大多数用户使用默认配置，较少尝试其他插件如LRC、Shec等。

#### 3. **决定事项**
   - **推荐使用ISA-L插件**：由于ISA-L在现代CPU上的性能优势明显，建议在新建Erasure Coding池时使用ISA-L插件。
   - **考虑LRC、Shec、Clay插件**：这些插件在特定场景下（如网络带宽受限时）可以加速OSD故障后的恢复，但因其使用较少，建议谨慎使用。

#### 4. **后续行动计划**
   - **更改默认插件**：Jamie Pride已提交一个Pull Request，建议将ISA-L设为新建Erasure Coding池的默认插件。
   - **进一步优化**：Connor Fet将在后续的会议中分享更多关于Erasure Coding性能优化的更新，特别是针对块存储工作负载的部分写入和读取优化。

#### 5. **Q&A及讨论**
   - 会议结束后，团队成员（包括团队负责人Mebu Scales和Connor Fet）将继续提供支持，欢迎与会者进一步讨论Erasure Coding插件及性能优化相关问题。



**总结**：本次会议详细讨论了Ceph中Erasure Coding的不同插件及其性能表现，特别是Jerasure和ISA-L的对比。ISA-L由于支持现代CPU指令集且仍在维护，性能显著优于Jerasure。会议建议在新建Erasure Coding池时优先考虑使用ISA-L插件，并计划将其设为默认插件。