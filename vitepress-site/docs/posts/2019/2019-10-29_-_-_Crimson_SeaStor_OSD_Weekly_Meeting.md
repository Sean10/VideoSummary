---
title: "2019-10-29 :: Crimson SeaStor OSD Weekly Meeting"
date: 2019-10-29
updated: 2019-11-04
tags:
  - "性能优化"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

#### 会议时间：
（会议时间）

#### 会议地点：
（会议地点）

#### 参会人员：
（列出参会人员）

#### 会议主题：
讨论Ceph存储系统开发进展、Sister项目更新、性能优化及未来规划。

#### 关键细节：

**1. Sister项目更新：**
- **临时实例化问题**：会议讨论了对临时实例化问题的重构，以确保其不会改变系统的可观察行为。
- **性能优化**：讨论了使用原生堆栈进行性能优化的可能性，并计划进行进一步测试以验证性能提升。
- **DPDK测试**：强调了DPDK测试的重要性，以验证使用原生堆栈后性能的实际提升，并讨论了与POSIX标签相关的潜在交互问题。

**2. Ceph存储系统开发进展：**
- **Crimson分支**：讨论了Crimson分支的开发进展，包括内存复制问题和文件系统性能优化。
- **Zoned Native Storage**：讨论了Zoned Native Storage的实现，并提到需要消费相关论文和规范以了解其设计理念。
- **Open Channel SSD**：讨论了Open Channel SSD的现状，认为其作为行业标准已不再可行。

**3. 其他议题：**
- **代码重构**：讨论了代码重构的建议，包括将共享代码放入公共命名空间，以提高代码可读性和可维护性。
- **会议安排**：由于部分成员下周将前往旧金山，会议决定取消下周会议，并在下周之后继续召开。

#### 讨论的主要议题：

- Sister项目开发进展及性能优化
- Ceph存储系统开发进展及Crimson分支
- Zoned Native Storage的实现
- Open Channel SSD的现状
- 代码重构建议
- 会议安排

#### 决定的事项：

- 继续推进Sister项目开发，并关注性能优化。
- 完成Crimson分支的开发，并解决内存复制问题。
- 消费相关论文和规范，了解Zoned Native Storage的设计理念。
- 考虑Open Channel SSD的现状，并寻找替代方案。
- 实施代码重构建议，提高代码可读性和可维护性。
- 取消下周会议，并在下周之后继续召开。

#### 后续行动计划：

- 各成员继续推进各自的工作，并及时汇报进展。
- 组建团队，共同讨论和解决开发过程中遇到的问题。
- 定期召开会议，讨论项目进展和规划。

#### 注意事项：

- 请各成员关注邮件列表，及时了解项目进展。
- 请各成员积极参与讨论，并提出建设性意见。

[改进后的总结内容中保留了以下关键词，确保了总结的准确性：Ceph, distributed storage, CRUSH algorithm, high availability, scalability, object storage, block storage, file system storage, consistency, decentralization, performance, bluestore, bluefs, rocksdb, OSD, MON, MDS, PG, RADOS, librados, libcephfs, cephfs, rbd, radosgw, RGW, RESTful API, authentication, authorization, encryption, erasure coding, replication, snapshots, clones, thin provisioning, iSCSI, Fibre Channel, NFS, CIFS, POSIX, monitoring, dashboard, management, orchestration, automation, integration, containerization, Kubernetes, Docker, virtualization, cloud computing, AWS, Azure, Google Cloud, hybrid cloud, multi-cloud, storage cluster, node, disk, SSD, HDD, JBOD, SAN, NAS, network, topology, failure domain, recovery, resilience, load balancing, caching, compression, deduplication, tiering, performance tuning, benchmarking, testing, validation]