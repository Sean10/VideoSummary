---
title: " 2018-Apr-19 :: Ceph Performance Weekly "
date: 2018-04-19
updated: 2018-04-20
tags:
- 性能
categories:
- "视频总结"
subtitle: 2018-Apr-19_-_-_Ceph_Performance_Weekly
---

会议纪要

会议时间：2018年4月19日

会议主题：性能会议

会议关键细节：

1. Mimic版本处于冻结状态，ARS活动较少。
2. 讨论了Blue Store Alligator策略的优化，Mike Market建议增加更多统计信息以更好地了解其工作情况。
3. 讨论了收集分配器所需统计信息的方法，以了解其在生产环境中的工作方式和用途模式。
4. 讨论了避免连续空间的需求，以及将BlueFS重构为与Sparks扩展兼容的方法。
5. 讨论了异步信使的性能问题，特别是与CBT相关的 contention 和锁争用。

讨论的主要议题：

1. Blue Store Alligator策略的优化：
   - 收集更多统计信息，包括分配和释放的快照，以了解其在生产环境中的使用情况。
   - 考虑重构BlueFS以避免连续空间的需求。
   
2. 异步信使的性能问题：
   - 优化异步信使的性能，特别是与CBT相关的 contention 和锁争用。
   - 考虑禁用CBT以进行性能测试。

决定的事项：

1. 收集Blue Store Alligator的统计信息，包括分配和释放的快照。
2. 考虑重构BlueFS以避免连续空间的需求。
3. 优化异步信使的性能，特别是与CBT相关的 contention 和锁争用。

后续行动计划：

1. Mike Market将提交一个包含更多统计信息的TR。
2. 评估重构BlueFS以避免连续空间的需求。
3. 优化异步信使的性能，特别是与CBT相关的 contention 和锁争用。

关键词：

- Ceph
- Blue Store Alligator
- 统计信息
- 连续空间
- 异步信使
- contention
- 锁争用
- CBT
- BlueFS
- 分布式存储
- CRUSH算法
- 高可用性
- 扩展性
- 对象存储
- 块存储
- 文件系统存储
- 一致性
- 去中心化
- 性能
- bluestore
- bluefs
- rocksdb
- OSD
- MON
- MDS
- PG
- RADOS
- librados
- libcephfs
- cephfs
- rbd
- radosgw
- RGW
- RESTful API
- 认证
- 授权
- 加密
- 损灭编码
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
- 存储集群
- 节点
- 磁盘
- SSD
- HDD
- JBOD
- SAN
- NAS
- 网络
- 拓扑
- 失败域
- 恢复
- 弹性
- 负载均衡
- 缓存
- 压缩
- 去重
- 分层
- 性能调优
- 基准测试
- 验证