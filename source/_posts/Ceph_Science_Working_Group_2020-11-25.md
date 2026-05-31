---
categories:
- 视频总结
date: 2020-11-25
subtitle: Ceph_Science_Working_Group_2020-11-25
tags:
- Ceph
- 分布式存储
- CRUSH算法
- 高可用性
- 可扩展性
title: "Ceph Science Working Group 2020-11-25"
updated: 2020-11-26
---




### 会议纪要

#### 会议概述
本次Ceph Science Working Group会议讨论了Ceph存储系统在近期遇到的问题、技术挑战及解决方案。会议持续了一个小时，内容自由，涉及多个主题。

#### 主要议题
1. **Ceph集群问题**
   - 讨论了替换S3集群硬件时PG迁移和删除效率问题，以及BlueFS Buffered IO对稳定集群的帮助。
   - Igor正在准备一个补丁来解决PG删除效率低的问题。
   - 提到了Nautilus版本中内存泄漏和稳定性问题，以及Beast协议相关的问题。

2. **Ceph版本更新和升级**
   - 讨论了从旧版本升级到Octopus版本的体验，包括内存泄漏和稳定性问题。
   - 提到了Beast协议的问题和对Rados Gateway内存使用的讨论。

3. **Ceph性能和配置**
   - 讨论了多MDS的使用情况和性能问题，以及BlueStore的配置和性能优化。
   - 提到了BlueFS和BlueStore allocator的改进。

4. **Ceph集群管理和运维**
   - 讨论了限制Rados Gateway内存使用和网络架构中使用Rados Gateway的策略。
   - 提到了从直接使用Librados转向使用Rados Gateway的可能性。

#### 决定事项
- 关注Igor的PG删除补丁和BlueFS Buffered IO的启用情况。
- 测试和验证Beast协议问题，并考虑回退到CivetWeb。
- 监控和优化Rados Gateway的内存使用。

#### 后续行动计划
- 关注Ceph版本更新和补丁发布，特别是与内存管理和性能优化相关的更新。
- 测试和部署新的BlueStore配置和优化。
- 监控和调整Rados Gateway的配置。

#### 其他讨论
- 讨论了使用InfiniBand网络的可能性，但认为以太网已经足够满足需求。
- 提到了备份大型Ceph集群的挑战，特别是对于运行Oracle数据库的集群。

#### 会议结束
会议在讨论未来可能的技术升级和优化方向后结束。下一次会议计划在明年一月的第四个星期三举行。

#### 总结
本次会议重点关注了Ceph集群的稳定性、性能优化和版本升级。会议讨论了多个与Ceph集群管理和运维相关的问题，并制定了后续行动计划。