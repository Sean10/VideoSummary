---
categories:
- 视频总结
date: 2022-02-01
subtitle: Ceph_Science_Working_Group_2022-01-26
tags:
- Ceph
- 分布式存储
- CRUSH算法
- 可扩展性
- 高可用性
- 对象存储
- 块存储
- 文件系统存储
title: "Ceph Science Working Group 2022-01-26"
updated: 2022-02-02
---




本次会议是Ceph Science Working Group的会议纪要，主题为“科学计算与大型集群中的Ceph技术讨论会”。会议主要内容包括：

1. **新成员介绍**：Kasper Shark（GWDG）介绍了GWDG使用Ceph的经验，目前管理着五个集群，总存储容量约为7PB，并计划在四月新增18PB的冷存储和1.4PB的NVMe存储。Andres Pataki（Flatiron Institute）介绍了Flatiron Institute使用Ceph进行大规模存储的经验，每个集群约30PB。

2. **Ceph使用经验分享**：GWDG分享了在使用Ceph过程中遇到的一些问题，如集群网络故障等，并表示总体上对Ceph非常满意。Flatiron Institute讨论了在使用Ceph时遇到的元数据问题，特别是大量小文件和随机访问文件的问题。

3. **技术问题与解决方案**：讨论了BlueStore corruption问题，可能与硬盘的写缓存设置有关。探讨了使用单一领域连接多个集群的挑战和潜在的bug。讨论了使用外部专业支持服务，如Canonical, SoftIron等，以及这些服务的成本效益。

4. **Ceph升级与维护**：CERN分享了升级Ceph时采用的新方法，减少了系统停机时间。讨论了启用快照功能后遇到的性能问题，特别是在处理大量元数据时。

5. **未来计划与建议**：提及了即将举行的Cephalocon会议，鼓励成员参与。讨论了可能将会议时间调整到周一或周二的可能性。

后续行动计划包括：

- 关注和解决BlueStore corruption问题，以及快照功能带来的性能问题。
- 根据成员反馈调整会议时间，以避免与其他重要会议冲突。
- 鼓励成员参与即将举行的Cephalocon会议，并考虑是否组织相关的Birds of a Feather活动。