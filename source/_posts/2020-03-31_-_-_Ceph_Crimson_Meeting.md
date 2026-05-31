---
categories:
- 视频总结
date: 2020-04-03
subtitle: 2020-03-31_-_-_Ceph_Crimson_Meeting
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
- 分层
- 性能优化
- 测试
title: "'2020-03-31 :: Ceph Crimson Meeting'"
updated: 2020-04-04
---




### 会议纪要

#### 参会人员
- Jeremy（因病缺席）
- John
- Scott
- Adam
- Radek
- Josh Anderson

#### 主要议题
1. **Ceph项目进展**
   - **John**：本周将专注于Ceph工作，特别是CRUSH映射的更新和同步。
   - **Scott**：上周根据John和Mark的反馈修改了Ceph版本请求，解决了CNS路径调试问题，并提交了修复CSO测试问题的PR。
   - **Adam**：上周忙于DCM相关工作，本周回归Ceph，提交了多个PR，包括修复回归问题和改进代码结构，并讨论了增加单元测试。
   - **Radek**：正在完成状态机的工作，希望在一周内完成初步版本，并讨论了改进PR以在失败时重新读取对象状态。
   - **Josh Anderson**：上周调试了PG日志恢复代码，手动测试已通过，正在添加更多测试用例。

2. **项目管理与组织**
   - 讨论了将现有项目卡片迁移到Carrillo，并按不同类别和里程碑进行组织，以提高项目管理的可见性和效率。
   - 建议引入更短的里程碑，以便更好地跟踪进度。

#### 决定事项
- 将现有项目卡片迁移到Carrillo，并按类别和里程碑进行组织。
- 引入新的测试标签，以便更灵活地运行特定测试。

#### 后续行动计划
- **John**：继续处理CRUSH映射的更新和同步。
- **Scott**：本地测试PR并合并到主分支。
- **Adam**：继续处理回归问题，并增加单元测试。
- **Radek**：完成状态机工作，并改进PR。
- **Josh Anderson**：提交PG日志恢复的PR。
- **项目管理**：迁移项目卡片到Carrillo，并按计划进行组织和跟踪。

#### 其他事项
- 讨论了代码复制的性能问题，并计划后续进行优化。
- 确认了会议的音频问题已解决。

#### 下次会议
- 下周同一时间进行。

### 会议结束
- 感谢大家的参与，祝大家有个愉快的一天/夜晚。