---
title: "Improving Business Continuity for an Existing Large Scale Ceph Infrastructure"
date: 2023-05-05
updated: 2023-05-05
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

**会议主题：** CERN的Ceph存储系统业务连续性与灾难恢复改进

**会议时间：** 日期未提供

**会议地点：** 未提供

**参会人员：** Enrico, Abi (CERN IT部门存储组)

**会议内容：**

1. **CERN介绍：**
   - CERN位于日内瓦，运营着一个直径27公里的粒子对撞机，该对撞机建于地下100米。
   - 对撞机内部有超导磁体，用于加速粒子至接近光速，并在精确点进行对撞。
   - CERN拥有两个计算中心，其中一个历史悠久，建于60年代末或70年代初，另一个新中心预计今年年底投入使用。

2. **个人介绍：**
   - Enrico：计算机网络博士，2017年加入CERN，2020年开始参与Ceph操作。
   - Abi：加入CERN两年，负责Ceph的安全操作。

3. **Ceph在CERN的应用：**
   - CERN运行16个生产集群，使用Ceph的各种形式（块存储、文件存储和对象存储）。
   - 总存储容量约为65PB，主要使用旋转硬盘，少量全闪存存储用于RocksDB和元数据池。
   - Ceph与OpenStack集成，为45万个CPU核心提供存储支持。
   - 近年来，Ceph也越来越多地被用于Kubernetes和OpenShift集群。

4. **业务连续性与灾难恢复：**
   - **块存储（RBD）：**
     - 从单一RBD集群扩展到五个RBD集群，通过OpenStack提供不同性能和可用性的存储选项。
     - 引入了存储可用性区域（Availability Zones），以提高业务的连续性。
     - 使用RBD镜像进行灾难恢复，测试了基于日志和基于快照的镜像方法。
     - OpenStack Cinder备份驱动支持S3和RBD备份，RBD备份性能更优。

5. **对象存储：**
   - 主要使用两个独立的Ceph集群，一个用于主存储，另一个用于备份。
   - 测试了S3多站点配置，发现同步延迟和Bucket索引重分片的问题。
   - 探索了Cloud Sync功能，用于与外部云服务同步特定Bucket。

6. **文件系统（CephFS）：**
   - 从单一CephFS集群扩展到多个集群，根据使用场景进行划分。
   - 测试了CephFS快照功能，发现性能影响主要集中在MDS的Finisher线程。

7. **总结与展望：**
   - 业务连续性通过分散存储到不同集群实现，需要与用户和上层服务协调。
   - 灾难恢复主要通过备份和恢复实现，Ceph提供了多种备份工具和方法。
   - 未来可能考虑使用磁带备份，并继续优化备份流程。

**后续行动计划：**
- 继续测试和优化RBD、S3和CephFS的灾难恢复功能。
- 探索和实施更高效的备份和恢复策略，包括磁带备份。
- 与用户和其他IT部门协调，制定清晰的灾难恢复流程。

**会议结束：**
- 会议在提问环节后结束，参会者对Ceph在CERN的应用和未来发展表示了兴趣和赞赏。

**备注：**
- 会议中提到的Ceph相关技术和工具包括RBD、CephFS、Rados Gateway、OpenStack、Kubernetes、OpenShift等。