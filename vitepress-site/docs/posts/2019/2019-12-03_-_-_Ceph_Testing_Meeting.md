---
title: "2019-12-03 -- Ceph Testing Meeting"
date: 2019-12-04
updated: 2019-12-05
tags:
  - "Ceph"
  - "分布式存储"
  - "CRUSH算法"
  - "高可用性"
  - "可扩展性"
categories:
  - "视频总结"
outline: deep
---
会议纪要

### 会议概要

本次Ceph测试会议主要讨论了Ceph存储系统各分支（如Nautilus、Luminous等）的开发状态、Python 3迁移、以及后续的测试和发布计划。

### 主要议题

1. **Nautilus分支状态**：
   - 由Sage和David负责升级和测试，即将发布。
   - 讨论了Nautilus的发布笔记和向后兼容性问题。

2. **Luminous分支的Python 3迁移**：
   - 正在处理几个PR，需要进行测试。
   - 讨论了Luminous分支的Python 3迁移状态和测试需求。

3. **Master分支的兼容性和测试**：
   - 讨论了Master分支与Python 3的兼容性问题。
   - 讨论了Jenkins实例中使用的CentOS 7.6和7.8镜像的需求。

4. **后续行动计划**：
   - 决定对Nautilus、Mimic和Luminous分支进行Python 3的向后移植。
   - 讨论了如何处理分支的测试和发布，特别是关于旧版本的向后兼容性问题。

### 决定事项

- 关注Nautilus的发布笔记和向后兼容性。
- 进行Luminous分支的Python 3迁移测试。
- 为Master分支准备更多的CentOS镜像以支持测试。
- 对Nautilus、Mimic和Luminous进行Python 3的向后移植，并确保这些分支的稳定性和兼容性。

### 后续行动计划

- Yuri将继续处理Luminous分支的PR，并添加测试标签。
- Pierre将负责Nautilus分支的PR工作。
- 为Master分支准备更多的CentOS镜像。
- 对Nautilus、Mimic和Luminous进行Python 3的向后移植，并确保这些分支的稳定性和兼容性。

### 其他讨论

- 讨论了Ceph的发布周期和命名规则，下一个版本将是Octopus。
- 讨论了资源锁定机制和测试套件的优化问题。
- 讨论了Ceph的升级测试套件的复杂性，以及如何减少资源锁定的需求。
- 讨论了Ceph在不同操作系统上的测试需求。

会议在讨论了所有议题后结束，团队成员将继续按照会议决定的事项推进工作。