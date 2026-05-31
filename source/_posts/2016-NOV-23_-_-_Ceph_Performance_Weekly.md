---
categories:
- 视频总结
date: 2017-01-11
subtitle: 2016-NOV-23_-_-_Ceph_Performance_Weekly
tags:
- Ceph
- BlueStore
- 性能优化
- 分布式存储
title: "'2016-NOV-23 :: Ceph Performance Weekly'"
updated: 2017-01-12
---




本次会议主要讨论了Ceph BlueStore的性能优化和测试结果。以下是会议纪要：

**会议纪要**

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**： Sage, Ben Jenkins (Nokia首席视频架构师), M (Nokia开发团队), Mark (Ceph社区成员)

**会议主题**： Ceph BlueStore 测试与讨论

**会议内容**：

**一、Sage 报告**

1. **RTC 工作进展**： Sage 介绍了 RTC 工作进展，包括同步写入事务到 BlueStore，以及修复相关问题的补丁。
2. **BlueStore 性能优化**： Sage 提到，BlueStore 在使用 NVMe 存储和适当配置的情况下，可以显著提高性能。同时，他也提到，在有 I/O 的情况下，无法同步执行 I/O，需要进行进一步的修改。
3. **BlueStore 与列族**： Sage 指出，使用列族可能会降低性能，特别是在大容量卷上。他建议使用位图分配器来提高性能。

**二、Ben 和 M 报告**

1. **Nokia 公司介绍**： Ben 介绍了 Nokia 公司的业务范围和主要产品，特别是云 DVR 产品，该产品使用了 BlueStore。
2. **云 DVR 工作原理**： Ben 解释了云 DVR 的工作原理，包括内容导入、存储、管理和内容输出等环节。
3. **BlueStore 性能测试**： Ben 和 M 分享了他们在 BlueStore 上的性能测试结果，包括读写性能、稳定性、可靠性等方面。
4. **BlueStore 与纠删码**： Ben 和 M 讨论了 BlueStore 与纠删码的使用，包括性能、可靠性和恢复等方面。
5. **未来计划**： Ben 和 M 表示，他们将继续测试 BlueStore，并希望将其作为 Luminous 版本的官方后端存储。

**三、讨论与决定**

1. **关于删除操作优先级**： Sage 提到，在大量删除操作时，OSD 上的队列可能会过载，导致性能下降。建议增加删除操作的优先级设置。
2. **关于纠删码**： Ben 和 M 指出，纠删码可能会导致性能下降，尤其是在大型对象写入时。建议尝试使用 6+2 纠删码来解决这个问题。
3. **关于 VFS 缓存压力**： Sage 提到，VFS 缓存压力可能会影响性能，尤其是在冷数据访问时。建议降低 VFS 缓存压力。

**四、行动计划**

1. Sage 将继续修复 BlueStore 中的问题，并优化性能。
2. Ben 和 M 将继续测试 BlueStore，并与其他 Ceph 社区成员合作，共同改进 BlueStore。
3. Ceph 社区成员将关注删除操作优先级、纠删码和 VFS 缓存压力等问题，并寻求解决方案。

**五、其他**

1. Ben 和 M 表示，他们愿意与 Ceph 社区成员合作，共同推动 BlueStore 的发展。
2. 会议结束后，Ben 和 M 将将测试结果和反馈提交给 Ceph 社区。