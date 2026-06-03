---
title: "CDS Reef: Crimson"
date: 2022-04-22
updated: 2022-04-23
tags:
  - "Ceph"
  - "分布式存储"
  - "存储集群"
  - "BlueStore"
  - "高可用性"
  - "可扩展性"
  - "对象存储"
categories:
  - "视频总结"
outline: deep
---
在CDS Reef: Crimson会议中，Ceph项目的开发团队讨论了Crimson CDF项目的2022年进展，重点关注Quincy和Reef版本的特点和开发重点。

**Quincy版本**：
- 主要工作集中在稳定性和部署上。
- 支持Rook、SAFE和Seth ADM进行部署。
- 开发了Crimson RADOS技术套件，进行故障注入测试。
- 修复了大量问题，尤其是在排序和watch notify API方面。
- 改进了Blue Stores的支持。

**C-Store**：
- 引入新的指标框架，以更好地理解C-Store的行为。
- 对C-Store内部进行重写，简化LBA树结构，增加非日志段存储扩展的能力。
- 冲突检测机制使用可中断的未来重写。
- 添加了初始DNS支持，ZNS段管理器已在真实DNS设备上测试。
- 在性能方面，对LBA提示和日志合并进行了改进。

**Reef版本**：
- 多核快照和清理是Reef的重点。
- 将针对C-Store进行大量工作，包括多设备和分层的进一步改进，特别是与垃圾回收相关。
- 支持通过Random Block Manager快速访问NVMe设备。
- 最初通过在静态磁盘分区上运行多个C-Store实例来处理多核问题。

**测试和部署**：
- Quincy支持在单Reactor配置中测试RBD工作负载，无需快照，后端可以是Blue Store、Cyan Store或C Store，使用Rook或Seth ADM部署。
- 需要选择一种病理学测试作为所有PR的门槛测试，以确保Crimson持续有效。

**调试子系统**：
- 需要使Crimson的日志记录方式与Classic一致。
- 应尊重Classic的debug_underscore配置选项。
- PG日志消息应保持一致性，便于抓取特定PG的所有日志行。

**垃圾回收策略讨论**：
- 介绍了基于代数的垃圾回收策略，目的是将相似特性和年龄的扩展存储在同一段中。
- 讨论了代数的概念，即扩展可以存储在具有相同特性和类似年龄的段中。
- 提出了对策略的担忧和可能的改进建议，如直接将冷扩展写入更高代数。

**后续行动计划**：
- 继续改进C Store的成熟度，尽管可能会落后于Crimson整体进度。
- 探索更频繁的发布周期，如每月或每周自动构建快照，以便社区成员下载和运行。
- 推动与更广泛的社区合作，改善发布流程，并考虑为新贡献者编写指令和修复错误。