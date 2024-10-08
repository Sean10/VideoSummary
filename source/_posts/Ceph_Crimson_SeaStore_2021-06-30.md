---
title: "Ceph Crimson/SeaStore 2021-06-30"
date: 2021-08-24
updated: 2021-08-25
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 主要议题与讨论内容

1. **代码审查与清理工作**
   - 上周主要进行了PR（Pull Request）的审查和代码清理工作。
   - 尝试移除一些不必要的代码，并对PR进行了总结。
   - 提交了一个PR，旨在将无日志的Cue添加到编辑存储中的Shouted Queue。

2. **系统远程集成的控制接口**
   - 正在集成IOC TLF控制接口到系统远程设置中。
   - 提交了补丁并进行了初步审查，需要进一步完善版本。

3. **运行时异常修复**
   - 修复了两个运行时异常，一个是compare_xattr，另一个是pg_in_rs。
   - 当前的调试构建和发布构建都可以通过FIO和Reader's Bench进行测试。

4. **调试与性能问题**
   - 发现调试输出会导致运行缓慢，而禁用输出则会快速遇到问题。
   - 计划提交一个bug报告，以便更好地协调解决这些问题。

5. **Crimson背景问题**
   - 发现了Trashing测试中的根本原因，并提交了补丁。
   - 解决了由于错误类型转换导致的core dumps问题。

6. **PR142100审查**
   - 鼓励团队审查PR142100，特别关注mutable specifier的使用，以避免性能问题。

7. **实习生招聘**
   - 已经开始审查CVs，准备招聘实习生。

8. **PR合并与测试**
   - 有一个PR等待测试和审查，建议尽快合并。

9. **中断可处理的Future问题**
   - 解决了OSD maps显示和崩溃的问题，修复了C-store不尊重事务顺序的bug。

10. **Extent Placement Manager改进**
    - 修改了Extent Placement Manager，以解决Yinshin和Sam的担忧。
    - 重新基于主分支进行了代码重构，并正在修复中断条件泄漏问题。

11. **事务验证与缓存层问题**
    - 正在阅读事务验证PRs，并发现了一些缓存层的问题。
    - 正在修复这些问题，并将提交相关补丁。

12. **Lease Message问题**
    - 讨论了Lease Message在特定情况下的处理问题，特别是与激活消息的顺序相关。
    - 需要确保消息处理的顺序，以避免潜在的bug。

#### 决定事项

- 提交bug报告，以便更好地协调解决性能和调试问题。
- 鼓励团队审查PR142100，关注mutable specifier的使用。
- 尽快合并等待测试和审查的PR。

#### 后续行动计划

- 继续完善和提交相关补丁，解决发现的各类问题。
- 确保消息处理的顺序，特别是在处理Lease Message时。
- 继续进行代码审查和清理工作，以提高系统稳定性和性能。

#### 备注

- 下周将不在办公室，将不会进行RADOS QA工作。
- 需要进一步讨论和解决Lease Message相关的问题。

会议结束，祝大家工作顺利。