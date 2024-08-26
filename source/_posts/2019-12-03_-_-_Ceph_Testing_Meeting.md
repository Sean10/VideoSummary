---
title: "2019-12-03 :: Ceph Testing Meeting"
date: 2019-12-04
updated: 2019-12-05
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概要
本次会议主要讨论了Ceph存储系统的多个分支（如Nautilus、Luminous等）的开发状态、Python 3迁移、以及后续的测试和发布计划。

#### 主要议题
1. **Nautilus分支状态**：
   - Yuri报告Nautilus即将发布，目前由Sage和David负责升级和测试。
   - 讨论了Nautilus的发布笔记和可能的向后兼容性问题。

2. **Luminous分支的Python 3迁移**：
   - Yuri提到正在处理Luminous分支的几个PR，需要进行测试。
   - 讨论了Luminous分支的Python 3迁移状态和可能的测试需求。

3. **Master分支的兼容性和测试**：
   - 讨论了Master分支的兼容性问题，特别是与Python 3的兼容性。
   - 讨论了Jenkins实例中使用的CentOS 7.6和7.8镜像的需求。

4. **后续行动计划**：
   - 决定对Nautilus、Mimic和Luminous分支进行Python 3的向后移植。
   - 讨论了如何处理分支的测试和发布，特别是关于如何处理旧版本的向后兼容性问题。

#### 决定事项
- Nautilus即将发布，需要关注其发布笔记和向后兼容性。
- Luminous分支的Python 3迁移正在进行中，需要进行更多的测试。
- 需要为Master分支准备更多的CentOS镜像以支持测试。
- 决定对Nautilus、Mimic和Luminous进行Python 3的向后移植，并确保这些分支的稳定性和兼容性。

#### 后续行动计划
- Yuri将继续处理Luminous分支的PR，并添加测试标签。
- Pierre将负责Nautilus分支的PR工作。
- 需要为Master分支准备更多的CentOS镜像。
- 对Nautilus、Mimic和Luminous进行Python 3的向后移植，并确保这些分支的稳定性和兼容性。

#### 其他讨论
- 讨论了Ceph的发布周期和命名规则，下一个版本将是Octopus。
- 讨论了资源锁定机制和测试套件的优化问题。

#### 会议结束
会议在讨论了所有议题后结束，团队成员将继续按照会议决定的事项推进工作。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。