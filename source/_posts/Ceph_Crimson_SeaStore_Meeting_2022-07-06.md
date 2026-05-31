---
categories:
- 视频总结
date: 2022-07-19
subtitle: Ceph_Crimson_SeaStore_Meeting_2022-07-06
tags:
- Ceph
- 分布式存储
- CRUSH算法
- 高可用性
- 可扩展性
title: Ceph Crimson/SeaStore Meeting 2022-07-06
updated: 2022-07-20
---



### 会议纪要

**会议时间**： 2022年7月6日（具体日期未提及）

**会议地点**： 线上会议

**参会人员**： Yingjin、Fair、Marvin、Kingston、Aravind、Jinyu、Juan、Sam等

**会议内容**：

**一、人员变动与项目进展**

1. **人员变动**： Yingjin 将担任 C-Store 精英，负责 C-Store 项目的领导工作。
2. **项目进展**：
    * C-Store 项目：Yingjin 继续负责 C-Store 项目，并担任技术领袖。
    * ZNS 驱动开发：
        * Aravind 正在开发 ZNS 驱动，已提交三个补丁，但遇到 make check 失败问题。
        * Kingston 提到 ZNS 区的更新问题，由于关闭操作会导致磁盘无法再次打开，需要进行修改。
        * 会议讨论了 ZNS 驱动的关闭操作与磁盘容量浪费的问题，决定修改 ZNS 管理器，使其在写入数据时填充空间，以避免浪费。
    * 垃圾回收器改进：Jinyu 提出关于垃圾回收器改进的想法，建议在 GC 事务中添加判断逻辑，以避免将不满足时间局部性原则的 extent 添加到 Aerial 中。
    * 对象存储改进：Juan 正在调试对象存储相关的 PR，并尝试实现 KBB 树优化。
    * 性能测试：Sam 询问如何测试 ZNS 驱动，建议使用 fio 或 rados-bench 等工具进行性能测试。

**二、讨论与决策**

1. **ZNS 驱动开发**：
    * Aravind 将修改 ZNS 管理器，使其在写入数据时填充空间，以避免浪费。
    * Sam 将审查 Aravind 提交的补丁，并请求代码审查。
2. **垃圾回收器改进**：
    * Jinyu 的建议被认可，将考虑将其纳入垃圾回收器改进方案。
3. **对象存储改进**：
    * Juan 将继续调试对象存储相关的 PR，并尝试实现 KBB 树优化。

**三、行动计划**

1. Aravind 修改 ZNS 管理器，并提交补丁。
2. Sam 审查 Aravind 提交的补丁，并请求代码审查。
3. Jinyu 将垃圾回收器改进方案提交给相关团队进行讨论。
4. Juan 继续调试对象存储相关的 PR，并尝试实现 KBB 树优化。

**四、其他事项**

1. 会议讨论了 ZNS 驱动的测试方法，建议使用 fio 或 rados-bench 等工具进行性能测试。
2. 会议讨论了 ZNS 驱动的容量浪费问题，并决定修改 ZNS 管理器，使其在写入数据时填充空间。

**五、结束语**

本次会议讨论了 C-Store 项目、ZNS 驱动开发、垃圾回收器改进、对象存储改进等议题，并制定了相应的行动计划。会议进展顺利，达到了预期目标。