---
title: "Ceph RGW Refactoring Meeting 2025-02-19"
date: 2025-02-19
updated: 2025-02-27
tags:
  - "Ceph"
  - "RGW"
  - "分布式存储"
  - "性能优化"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议主题**: Ceph RGW 开发会议

**日期**: 2025年2月19日

**主持人**: 未知

**参会人员**: Adam, Casey, Cena, Matt 及其他相关开发人员



#### 1. **Bucket Logging 权限问题**
   - **讨论内容**: 当前Bucket Logging实现存在权限问题，导致用户可能获得超出预期的权限。
   - **解决方案讨论**: 讨论了AWS的解决方案，即引入全局日志用户并通过策略或ACL控制权限，以及是否增强Bucket Policy以允许特定用户写入日志。
   - **决定**: 需要进一步讨论和反馈，以决定是否引入Service Principal并增强Policy支持。

#### 2. **Bucket Delete 性能问题**
   - **讨论内容**: 删除包含大量对象的Bucket时，并发删除操作可能导致OSD负载过高，影响集群性能。
   - **解决方案讨论**: 讨论了减少并发删除操作、先删除对象再删除OMAP对象等方法。
   - **决定**: 需要与Mark Nelson讨论，优化删除操作的性能。

#### 3. **Copy Object 加密问题**
   - **讨论内容**: 关于Copy Object加密的PR被Stale Bot关闭，Cena重新打开了该PR。
   - **解决方案讨论**: 需要将PR更新到当前代码库，并整合测试用例。
   - **决定**: Cena将继续推动PR的完成，并整合测试用例。

#### 4. **S3 测试问题**
   - **讨论内容**: S3测试在最近的Fedora版本上无法运行，原因是boto core版本的问题。
   - **解决方案讨论**: 通过取消对旧版本的依赖解决大部分问题，但禁用了Sig V2测试。
   - **决定**: 该PR将尽快合并。

#### 5. **S3 测试与SEF Repo的整合问题**
   - **讨论内容**: 讨论了是否将S3测试移入SEF Repo，以简化测试流程。
   - **解决方案讨论**: 提出了通过Toy命令简化测试流程，但仍需解决回滚问题。
   - **决定**: 需要进一步讨论，是否找到S3测试的维护者，或者将S3测试整合到SEF Repo中。



**后续行动计划**:
1. **Bucket Logging权限问题**: 继续讨论是否引入Service Principal，并增强Policy支持。
2. **Bucket Delete性能问题**: 与Mark Nelson进一步讨论，优化删除操作的性能。
3. **Copy Object加密问题**: Cena继续推动PR的完成，并整合测试用例。
4. **S3测试与SEF Repo的整合问题**: 寻找S3测试的维护者，或讨论是否将S3测试整合到SEF Repo中。

**会议结束时间**: 超时