---
title: Ceph RGW Refactoring Meeting 2025-09-03
date: 2025-09-08
updated: 2025-09-08
tags:
- Ceph
- RGW
- 存储
- 分布式存储
categories: 
- "视频总结"
subtitle: Ceph_RGW_Refactoring_Meeting_2025-09-03
---

本次会议主要讨论了Ceph RGW的优化和改进，以下是会议的关键细节：

### 1. `create bucket` 逻辑优化
- **问题背景**: 客户频繁调用`create bucket`用于检查桶是否存在，导致集群性能下降。
- **讨论内容**: 
  - 现有逻辑在确认桶存在后仍会创建并删除冗余对象，影响性能。
  - S3场景：若桶存在且无元数据变更，应直接返回`BucketExists`错误，无需操作后端存储。
  - Swift场景：允许元数据更新，但不应重复创建`rados objects`。
- **后续行动**: Kernel将提交PR优化逻辑，确保仅在必要时操作后端。

### 2. 用户迁移至账户时的权限问题
- **问题描述**: 用户迁移到账户后，桶的`ACL`中`owner`字段更新为账户ID，但`policy`字段仍保留旧用户UID，导致权限冲突。
- **结论**: 此为代码疏漏，需同时更新`ACL`的`owner`和`policy`字段。
- **后续行动**: Kernel将提交PR修复此问题。

### 3. Ceph Developer Summit (CDS) 安排
- CDS已启动，RGW相关会议计划在下周三复用常规会议时间。
- 议题征集：稳定性改进、Reef版本的RGW新功能规划。

### 4. 稳定性改进讨论
- 近期在重构会议中讨论了稳定性优化，但尚无具体方案。
- 计划在后续Ceph Steering Committee (CSC)会议中进一步推进。

### 5. 行动计划
- 提交`create bucket`逻辑优化PR：Kernel，1-2天内。
- 修复账户迁移的ACL同步问题PR：Kernel，近期。
- 更新会议结论至Tracker Issue：Kernel，会后。
- 完善 CDS RGW 议题（Roadmap/新功能）：全体，下周会议前。

本次会议重点关注了Ceph RGW的性能优化和稳定性改进，并对一些重要问题进行了讨论和决策，为后续的开发工作提供了明确的方向。