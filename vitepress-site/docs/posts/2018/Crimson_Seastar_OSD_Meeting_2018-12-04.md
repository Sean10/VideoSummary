---
title: "Crimson/Seastar OSD Meeting 2018-12-04"
date: 2018-12-06
updated: 2018-12-06
tags:
  - "Ceph"
  - "OSD"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2018年12月4日

**参会人员**： [请填写参会人员名单]

**会议主题**： Ceph分布式存储系统开发讨论

**会议内容**：

**1. 网络连接问题**
- 由于网络连接问题，部分参会人员无法正常参与会议。Jim今日无法参加会议，因他今日不在办公室。

**2. 功能开发与优化**
- 讨论了Ceph中“finish”功能开发的进展，包括：
  - 修改代码以注册Kovac观察者。
  - 修复OS中的一些错误。
  - 优化代码以在POSIX环境下运行。
- 讨论了如何解决在跨不同分支代码合并时出现的兼容性问题。

**3. crimson项目**
- 讨论了crimson项目中的同步问题，包括：
  - crimson需要使用with sister，而synchronous messenger不需要。
  - 在同一文件中同时存在两种类型的messenger，导致冲突。
  - 探讨了如何将sharded crimson messenger分配到不同的shard。

**4. 其他**
- 讨论了以下内容：
  - 使用boost intrusive库时遇到的问题。
  - 代码合规性检查。
  - 复制bucket在sister OSD上的实现。

**决定事项**：

- 参会人员决定：
  - 继续推进finish功能的开发。
  - 解决crimson项目中的同步问题。
  - 修复boost intrusive库相关的问题。
  - 完成代码合规性检查。

**后续行动计划**：

- 参会人员将：
  - 继续跟进finish功能的开发。
  - 解决crimson项目中的同步问题。
  - 修复boost intrusive库相关的问题。
  - 完成代码合规性检查。

**备注**：

- 会议中提到了以下计算机科学/ceph相关领域英文关键词：
  - finish
  - Kovac observer
  - POSIX
  - crimson
  - sharded crimson messenger
  - boost intrusive
  - compliance
  - replicated bucket