---
categories:
- 会议纪要
date: 2023-04-05
subtitle: Ceph_Crimson_SeaStore_Meeting_2023-04-05
tags:
- Ceph
- 分布式存储
- Crimson
- OSD
- MGR
- CI
- 日志级别
- 池压缩
title: Ceph Crimson/SeaStore Meeting 2023-04-05
updated: 2023-04-06
---




本次会议主要讨论了Ceph Crimson/SeaStore项目的进展和问题，以下是会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划：

#### 主要议题：

1. **QE团队更新**：
   - **OSD日志问题**：发现OSD日志在调试级别20下未包含级别15、10、20的条目，而MGR日志则包含所有这些级别的条目。此问题先前在测试中已观察到，现已上报。
   - **池压缩问题**：启用压缩的池在运行rados bench时，写入的数据量和对象数量与未启用压缩的池相同，而在Red Hat CEPH集群中，这些数据有明显差异。此问题也已上报。
   - **Crimson支持**：下游的CI框架现已支持Crimson，所有CI管道中的测试将在未来几周内运行在Crimson构建上。

2. **Crimson日志级别讨论**：
   - Crimson的日志系统与传统系统完全不同，只有Trace、Debug和Error三个级别。目前正在调整将传统的调试日志级别映射到Crimson的日志级别。

3. **后续行动计划**：
   - 跟进Milton关于设置最大对象的结果分享。
   - 继续调试medusa oski系统，预计很快完成最终修改。

#### 决定事项：

- 确认Crimson日志级别映射的问题，并将与相关人员进一步沟通解决。
- 持续关注并解决池压缩问题。

#### 后续行动：

- 与Milton分享关于最大对象设置的测试结果。
- 完成medusa oski系统的最终调试和修改。

#### 其他事项：

- 提醒大家今天是Pierce的假期。

#### 会议结束：

- 会议于[具体时间]结束，感谢大家的参与。

本次会议反映了Ceph Crimson/SeaStore项目的最新进展，强调了日志级别映射和池压缩问题的重要性，并制定了相应的后续行动计划。