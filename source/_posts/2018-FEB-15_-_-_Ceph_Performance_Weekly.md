---
categories:
- 视频总结
date: 2018-02-21
subtitle: 2018-FEB-15_-_-_Ceph_Performance_Weekly
tags:
- 性能优化
- 分布式存储
- CRUSH算法
- 高可用性
- 可扩展性
- 对象存储
- 块存储
- 文件系统存储
- 性能
- BlueStore
- BlueFS
- RocksDB
- OSD
- MON
- MDS
- PG
- RADOS
- librados
- libcephfs
- RBD
- RGW
- RESTful API
- 认证
- 授权
- 加密
- 复制
- 快照
- 克隆
- 虚拟化
- 云计算
- AWS
- Azure
- Google Cloud
- 混合云
- 多云
title: "'2018-FEB-15 :: Ceph Performance Weekly'"
updated: 2018-02-21
---




**会议纪要**

**会议时间**： 2023年X月X日

**参会人员**： [此处列出参会人员姓名]

**会议主题**： Ceph存储性能优化与调试

**会议内容**：

**一、性能优化**

*   Retta Slav 在读性能测试中发现了两个主要问题：
    *   通过MD config T访问配置选项速度过慢，已提交PR进行优化。
    *   在非调试模式下填充流（oh streams）导致性能下降，已提交PR进行修复。
*   作者在PTO期间发现memstore性能较慢，通过使用基于向量的对象存储和性能修复，显著提高了性能。
*   作者发现pg log对CPU消耗影响较大，尤其是在使用in-memory vector-based存储时，CPU消耗从5个核心降至约3个核心。
*   作者认为需要进一步优化pg log，并考虑使用PG ring buffers来提高性能。

**二、调试设施**

*   作者发现mutex和perf counters对性能影响较大，特别是在finisher thread和OSD操作中。
*   作者认为需要优化mutex的使用，并考虑使用更高效的机制。
*   作者发现lock depth参数对性能影响较大，建议默认设置为none。

**三、其他**

*   作者提出了一个新的object store playground项目，名为pet store，用于测试不同的性能优化方案。
*   作者认为需要进一步优化object info T结构和PG info结构。
*   Adam正在尝试使用off FFI编译Ceph，以验证性能表现。

**后续行动计划**：

*   作者将继续优化pg log和性能相关代码。
*   作者将进一步优化mutex的使用，并考虑使用更高效的机制。
*   Adam将继续测试使用off FFI编译Ceph的性能表现。
*   全体成员将继续关注Ceph的性能优化和调试工作。

**备注**：

*   会议中提到了一些计算机科学/ceph相关领域英文关键词，如：performance pull requests, MD config T, memstore, pg log, mutex, perf counters, lock depth, off FFI等。

**总结**：

本次会议讨论了Ceph存储性能优化和调试的相关问题，并提出了后续行动计划。会议强调了优化pg log和mutex使用的重要性，并建议继续探索新的性能优化方案。