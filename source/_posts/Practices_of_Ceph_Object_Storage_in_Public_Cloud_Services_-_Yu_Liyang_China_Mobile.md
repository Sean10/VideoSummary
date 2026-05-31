---
categories:
- 视频总结
date: 2019-05-24
subtitle: Practices_of_Ceph_Object_Storage_in_Public_Cloud_Services_-_Yu_Liyang_China_Mobile
tags:
- Ceph
- 分布式存储
title: "Practices of Ceph Object Storage in Public Cloud Services - Yu Liyang, China Mobile"
updated: 2019-05-24
---


### 会议纪要

**会议时间**： [请填写会议时间]

**参会人员**： Carolyn、Chana Baba、团队其他成员

**会议主题**： 公共云平台建设与优化讨论

**会议内容**：

**一、公共云平台现状**

1. **平台规模**： 目前云平台已支持政府、企业及内部客户，用户数量不断增加，位于北京、Cointreau和Enchantra，总容量预计超过15PB。
2. **网络架构**： 采用高速光纤网络，使用Rackware进行用户和数据管理，降低云存储的延迟。
3. **存储特性**： 用户可比较不同产品，根据需求选择合适的存储方案。目前开发了部分S3特性，如数据包、通知、日志记录和存储类，支持数据在不同存储类之间迁移。

**二、主要议题**

1. **集群扩展问题**： 由于用户上传文件过多，导致资源消耗过快，需要扩展集群。但添加新端口会引发数据重平衡，影响用户体验。
2. **W模块更新**： 云集群更新时，需要对W模块进行修改，但W模块的STI数量庞大，更新过程耗时较长。
3. **性能压力**： 生产环境中，主节点的并发请求量超过一万，导致处理速度缓慢，修改元数据时延迟较大。

**三、决策事项**

1. **集群扩展**： 考虑采用其他方案解决集群扩展问题，如增加服务器、优化资源分配等。
2. **W模块优化**： 优化W模块的更新流程，提高效率。
3. **性能优化**： 分析主节点性能瓶颈，进行针对性优化。

**四、后续行动计划**

1. 技术团队针对集群扩展问题进行调研，提出解决方案。
2. 技术团队优化W模块更新流程，提高效率。
3. 性能团队分析主节点性能瓶颈，并提出优化方案。

**五、其他事项**

1. 保持与用户的沟通，了解他们的需求和反馈。
2. 定期对云平台进行性能测试，确保平台稳定运行。

**关键词**： Ceph, Distributed Storage, Public Cloud, Cloud Storage Optimization, Cloud Platform, Cluster Expansion, W Module, Performance Optimization, S3 Features, Rackware, User Data Management, Latency Reduction, Storage Solutions, Data Migration, STIs, Concurrent Requests, Metadata Latency, Server Augmentation, Resource Allocation, Update Workflow, Efficiency Improvement, Benchmarking