---
title: "2017-MAY-11 :: Ceph Performance Weekly"
date: 2017-05-17
updated: 2017-05-17
tags:
  - "Ceph"
  - "性能优化"
  - "RBD"
  - "BlueStore"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**： 会议主持人、Ceph社区成员、阿里巴巴工程师（Mark、Jesse、Gem、Cliff）等

**会议内容**：

**一、Ceph社区近期工作**

1. **Poll请求**：讨论了多个优化请求，包括启用sink rights提高小IO性能、优化manager、scrubbing功能合并、cache miss rate优化、blue store compaction read ahead优化、新的编码和修复方案、blue FS sync right选项添加等。
2. **Purple请求**：讨论了优化RBD性能和异步消息传递工作。

**二、Ceph社区未来工作**

1. **RBD性能优化**：分析RBD client-side瓶颈，考虑禁用BD cache，评估RBD与文件系统的性能对比。
2. **BlueStore优化**：blue store compaction read ahead优化、Kvsync线程拆分、3x replication与blue store erasure coding性能对比、partial reads优化等。
3. **其他工作**：CRC计算优化、blue FS在共享设备中的放置、adaptive throttle工作、Kvsync线程拆分。

**三、阿里巴巴工程师工作**

1. **Commit majority功能**：实现了commit majority功能，提高了平均延迟和延迟抖动，将在客户端和收集器端进一步实现。
2. **与Ceph社区的协作**：邀请Ceph社区成员对commit majority功能进行审查，合作优化Ceph性能。

**四、行动计划**

1. Ceph社区成员将继续关注RBD性能优化、BlueStore优化等工作。
2. 阿里巴巴工程师将与Ceph社区合作，优化Ceph性能。
3. Ceph社区成员将参与commit majority功能的审查工作。

**五、其他**

1. 讨论了RBD与文件系统性能对比的问题。
2. 讨论了BlueStore在共享设备中的放置问题。
3. 讨论了adaptive throttle工作。

**六、会议总结**

本次会议讨论了Ceph社区近期工作和未来工作计划，并邀请阿里巴巴工程师参与Ceph性能优化工作。会议气氛热烈，讨论深入。