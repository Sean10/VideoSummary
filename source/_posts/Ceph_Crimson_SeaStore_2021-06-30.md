---
categories:
- 视频总结
date: 2021-08-24
subtitle: Ceph_Crimson_SeaStore_2021-06-30
tags:
- Ceph
- 分布式存储
- 代码审查
- 问题修复
- 性能优化
title: "Ceph Crimson/SeaStore 2021-06-30"
updated: 2021-08-25
---



### 会议纪要

#### 主要议题与讨论内容

1. **代码审查与清理工作**
   - 主要进行了PR的审查和代码清理，尝试移除不必要的代码。
   - 提交了一个PR，将无日志的Cue添加到编辑存储中的Shouted Queue。

2. **系统远程集成的控制接口**
   - 集成IOC TLF控制接口到系统远程设置中，已提交补丁并初步审查。

3. **运行时异常修复**
   - 修复了compare_xattr和pg_in_rs两个运行时异常，确保调试和发布构建均能通过测试。

4. **调试与性能问题**
   - 发现调试输出导致运行缓慢，计划提交bug报告解决。

5. **Crimson背景问题**
   - 发现并解决了Trashing测试中的根本原因和core dumps问题。

6. **PR142100审查**
   - 鼓励团队审查PR142100，关注mutable specifier的使用，以避免性能问题。

7. **实习生招聘**
   - 已开始审查CVs，准备招聘实习生。

8. **PR合并与测试**
   - 有一个PR等待测试和审查，建议尽快合并。

9. **中断可处理的Future问题**
   - 解决了OSD maps显示和崩溃问题，修复了C-store不尊重事务顺序的bug。

10. **Extent Placement Manager改进**
    - 修改了Extent Placement Manager，以解决Yinshin和Sam的担忧，并修复中断条件泄漏问题。

11. **事务验证与缓存层问题**
    - 正在修复事务验证PRs中的缓存层问题。

12. **Lease Message问题**
    - 讨论了Lease Message在特定情况下的处理问题，确保消息处理顺序。

#### 决定事项

- 提交bug报告，解决调试和性能问题。
- 鼓励团队审查PR142100，关注mutable specifier的使用。
- 尽快合并等待测试和审查的PR。

#### 后续行动计划

- 继续完善和提交相关补丁，解决各类问题。
- 确保消息处理的顺序，特别是在处理Lease Message时。
- 继续进行代码审查和清理工作，提高系统稳定性和性能。

#### 备注

- 下周将不在办公室，不会进行RADOS QA工作。
- 需要进一步讨论和解决Lease Message相关的问题。