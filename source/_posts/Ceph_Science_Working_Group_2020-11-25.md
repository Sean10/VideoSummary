---
title: "Ceph Science Working Group 2020-11-25"
date: 2020-11-25
updated: 2020-11-26
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
本次会议是一个关于研究计算和Ceph存储系统的成员会议，与会者讨论了近期遇到的问题、技术挑战以及解决方案。会议持续了大约半小时到一个小时，讨论内容较为自由，涉及多个主题。

#### 主要议题
1. **Ceph集群中的问题**
   - 讨论了在替换S3集群硬件时遇到的问题，特别是PG（Placement Group）迁移和删除的效率问题。
   - 提到了在Nautilus版本中，需要重新启用BlueFS Buffered IO来稳定集群。
   - 讨论了PG删除过程中的低效率问题，以及Igor正在准备的补丁可能解决这一问题。

2. **Ceph版本更新和升级**
   - 讨论了从旧版本升级到Octopus版本的体验，特别是内存泄漏和稳定性问题。
   - 提到了在升级过程中遇到的Beast协议相关的问题，以及对Rados Gateway内存使用的讨论。

3. **Ceph性能和配置**
   - 讨论了多MDS（Multi-Master Metadata Server）的使用情况和性能问题。
   - 提到了BlueStore的配置和性能优化，特别是关于BlueFS和BlueStore allocator的改进。

4. **Ceph集群管理和运维**
   - 讨论了如何限制Rados Gateway的内存使用，以及在网络架构中使用Rados Gateway的策略。
   - 提到了从直接使用Librados转向使用Rados Gateway的可能性，以及相关的网络升级。

#### 决定事项
- 需要关注Igor关于PG删除的补丁，以及BlueFS Buffered IO的启用情况。
- 需要进一步测试和验证Beast协议的问题，并考虑是否需要回退到CivetWeb。
- 需要继续监控和优化Rados Gateway的内存使用，特别是在高并发IO情况下的表现。

#### 后续行动计划
- 继续关注Ceph的版本更新和补丁发布，特别是与内存管理和性能优化相关的更新。
- 计划在下一个版本中测试和部署新的BlueStore配置和优化。
- 继续监控和调整Rados Gateway的配置，以确保在高负载下的稳定性和性能。

#### 其他讨论
- 讨论了使用InfiniBand网络的可能性，但目前认为以太网已经足够满足需求。
- 提到了备份大型Ceph集群的挑战，特别是对于运行Oracle数据库的集群。

#### 会议结束
会议在讨论了未来可能的技术升级和优化方向后结束，下一次会议计划在明年一月的第四个星期三举行。会议组织者感谢大家的参与，并提醒大家注意假期安全。