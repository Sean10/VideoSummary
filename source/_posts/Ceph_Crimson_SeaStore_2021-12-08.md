---
categories:
- 视频总结
date: 2021-12-13
subtitle: Ceph_Crimson_SeaStore_2021-12-08
tags:
- Ceph
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
- iSCSI
- NFS
- CIFS
- POSIX
- 监控
- Dashboard
- 编排
- 自动化
- 容器化
- Kubernetes
- Docker
- 虚拟化
- 云计算
- AWS
- Azure
- Google Cloud
- 混合云
- 多云
- 存储集群
- SSD
- HDD
- SAN
- NAS
- 网络
- 弹性
- 恢复
- 负载均衡
- 缓存
- 压缩
- 去重
- 分层
- 性能优化
- 测试
title: "Ceph Crimson/SeaStore 2021-12-08"
updated: 2021-12-14
---




### 会议纪要

#### 会议时间：2021年12月8日
#### 参会人员：[参会人员名单]

#### 主要议题：
1. **逻辑PIN竞争修复**
   - 通过代码审查和发布版本，修复了逻辑PIN竞争问题。

2. **心跳空白IP问题**
   - 解决了心跳中的空白IP问题，原因是测试中`self.configure`文件未设置为公共IP地址和集群IP地址。

3. **Messenger单元测试进展**
   - 正在准备Messenger单元测试，已向团队成员发送邮件征求意见。

4. **Rook集群安装问题**
   - 尝试安装Rook集群时遇到问题，已与Radic同步并获取输入，预计下周继续测试。

5. **性能分析与优化**
   - 进行了性能分析，发现CPU时间主要被LBA研究占用，实施了一些优化并提交了PR。
   - 观察到OMAP相关操作占用大量CPU时间，但目前不是重点。
   - GC速度影响性能，建议增加GC速度以提升性能。

6. **日志相关功能测试**
   - 进行了日志相关功能的测试，发现清理操作与模拟和读取操作存在冲突。

#### 决定事项：
- 继续优化LBA和OMAP查找。
- 关注GC性能，作为下一步工作重点。
- 完善日志相关功能的指标，特别是清理、修剪和回收事务的区分。

#### 后续行动计划：
- 完成Messenger单元测试的准备工作。
- 继续Rook集群的安装和测试。
- 实施LBA和OMAP查找的优化。
- 增加GC速度以提升性能。
- 完善日志相关功能的指标。

#### 其他事项：
- 会议记录者将在下周至1月3日期间休假，1月4日恢复工作，期间可通过邮件联系。

#### 会议结束时间：[具体时间]