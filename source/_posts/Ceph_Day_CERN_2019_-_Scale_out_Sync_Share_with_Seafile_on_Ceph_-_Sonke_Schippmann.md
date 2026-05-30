---
categories:
- 视频总结
date: 2020-08-25
subtitle: Ceph_Day_CERN_2019_-_Scale_out_Sync_Share_with_Seafile_on_Ceph_-_Sonke_Schippmann
tags:
- Ceph
- 分布式存储
- Seafile
- 同步与共享
- Sönke Schippmann
title: "'Ceph Day CERN 2019: Scale out Sync & Share with Seafile on Ceph - Sönke Schippmann'"
updated: 2020-08-26
---



### 会议纪要

#### 会议主题：Ceph Day CERN 2019 - Seafile在Ceph上的扩展同步与共享

#### 会议时间：2019年（具体时间未提供）

#### 会议地点：CERN（具体地点未提供）

#### 参会人员：Sönke Schippmann，布莱梅大学代表

#### 会议内容总结：

1. **Ceph集群介绍**
   - 布莱梅大学运行一个900毫拍字节（MilliPetabyte）的Ceph集群，对Ceph在不同工作负载下的性能表示满意。

2. **Seafile同步与共享系统**
   - Seafile是一个开源的同步与共享系统，类似于ownCloud和NextCloud，但性能更优，硬件需求更低。
   - 布莱梅大学拥有约9000名Seafile用户，其中3000名在过去几个月内活跃，存储了35TB的数据，分布在1.5亿个对象中。

3. **Seafile的系统硬件配置**
   - Seafile运行在一个配置较低的虚拟机上，仅使用8个虚拟CPU和32GB RAM，大部分时间处于空闲状态。

4. **存储迁移策略**
   - Seafile目前使用基于RBD卷的ZFS文件系统进行存储，正在迁移至Ceph的S3存储。
   - 迁移的主要目的是利用Ceph的S3存储后端，通过Rados Gateway实现更高效的存储管理。

5. **Seafile的存储后端配置**
   - Seafile支持多种存储后端，包括文件系统存储、S3存储、OpenStack和Ceph直接存储。
   - 对于S3存储，需要配置三个桶，并设置S3用户和放置目标规则，以更好地管理数据池。

6. **Seafile的配置文件调整**
   - 需要修改Seafile的配置文件，包括后端服务器和前端服务器的配置，以及一个JSON文件来指定存储目标。
   - 对于已有用户数据的情况，需要确保默认存储设置为文件系统存储，以避免数据访问问题。

7. **数据迁移策略**
   - 由于Seafile提供的迁移脚本仅支持离线迁移，布莱梅大学决定自行开发在线迁移脚本，以避免长时间的服务中断。
   - 迁移工作已经进行了约三个月，预计年底前完成。

#### 决定事项：
- 确认Seafile从文件系统存储迁移至Ceph S3存储的计划。
- 确认自行开发的在线迁移脚本的使用，以减少服务中断时间。

#### 后续行动计划：
- 继续监控和调整迁移过程中的性能和稳定性。
- 完成迁移后，评估新存储系统的性能和用户反馈。
- 更新和维护Seafile系统的配置文件和文档，确保未来的可维护性。

#### 附件：
- 迁移脚本和配置文件示例链接。
- Seafile和Ceph系统的相关文档和更新。