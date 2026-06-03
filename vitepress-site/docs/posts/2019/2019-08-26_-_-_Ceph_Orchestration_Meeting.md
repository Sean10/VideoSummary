---
title: "2019-08-26 :: Ceph Orchestration Meeting"
date: 2019-08-26
updated: 2019-09-06
tags:
  - "Ceph"
  - "Kubernetes"
  - "存储集群"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2023年11月某日

**参会人员**： Pete, Travis, Blaine, Ben等

**会议主题**： Rook模块开发进度、Ceph集群管理、API设计等

**关键细节与议题**：

1. **人员情况**：
   - Specter将在9月份回归。
   - Travis正在审查与Kubernetes事件相关的模块。

2. **Rook模块开发**：
   - Tesla完成了Rook模块的PM工作，并创建了部分代码。
   - Paul希望修改代码，Pete表示可以接受。
   - 需要解决Rook模块内部锁消息的问题，目前缺乏测试。

3. **Rook 1.1版本**：
   - Tesla希望在1.1版本中加入新功能。
   - 目标发布日期是下周，可能会比较紧张。
   - 已合并修复Yum安装问题的PR，但部分构建失败。

4. **API设计**：
   - Travis正在解决Rook orchestrator API中操作不可组合的问题。
   - 需要改进API，使用futures和promises。
   - 需要设计方法检测受操作影响的节点。

5. **其他议题**：
   - 讨论了如何从orchestrator直接运行作业。
   - 讨论了使用host labels进行放置操作。

**决定事项**：

1. 继续推进Rook 1.1版本的发布。
2. 解决Rook模块内部锁消息的问题。
3. 改进Rook orchestrator API。
4. 设计检测受操作影响节点的方法。

**后续行动计划**：

1. Tesla继续完成Rook模块的修改工作。
2. Travis调查Yum安装问题。
3. 设计并实现改进的Rook orchestrator API。
4. 设计检测受操作影响节点的方法。

**备注**：

- 下周美国将有一个假期，可能影响工作进度。