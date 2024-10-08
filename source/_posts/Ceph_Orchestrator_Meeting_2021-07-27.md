---
title: "Ceph Orchestrator Meeting 2021-07-27"
date: 2021-08-23
updated: 2021-08-24
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概要
本次会议主要讨论了关于Ceph存储系统的开发进展，特别是与Rook和Local Storage Operator (LSO) 的集成问题。会议涉及了多个议题，包括代码审查、文档更新、用户集成测试以及未来工作计划。

#### 主要议题
1. **代码审查与集成测试**
   - Alfonso确认收到了关于PR（Pull Request）的消息，并讨论了如何处理PR中的评论和权限问题。
   - 讨论了在代码中设置用户“dashboard”的问题，以及需要进行的集成测试。

2. **文档更新与用户反馈**
   - 讨论了删除部分文档的问题，特别是关于某些选项如“scheme nivea”的保留价值。
   - 计划本周安排一次简短会议，以解决这些松散的结尾并推进VR（验证请求）。

3. **Rook与LSO的集成**
   - 讨论了Rook项目中的一些问题，特别是关于OSD（Object Storage Daemon）的创建和移除。
   - 确认了需要对Rook进行一些修改以支持OSD的移除，并讨论了可能的短期和长期解决方案。

4. **LSO的未来发展**
   - 讨论了LSO的当前状态和未来的发展方向，包括与Topol LVM的合作可能性。
   - 确认了需要与OpenShift的产品管理团队进行进一步的沟通，以确定LSO的未来发展路径。

#### 决定事项
- Alfonso将继续处理PR中的评论，并进行相关的集成测试。
- 计划本周内安排一次会议，以解决文档和用户集成的问题。
- 确认了需要对Rook进行修改以支持OSD的移除，并讨论了可能的短期和长期解决方案。
- 确认了需要与OpenShift的产品管理团队进行进一步的沟通，以确定LSO的未来发展路径。

#### 后续行动计划
- Alfonso将继续处理PR中的评论，并进行相关的集成测试。
- 计划本周内安排一次会议，以解决文档和用户集成的问题。
- 确认了需要对Rook进行修改以支持OSD的移除，并讨论了可能的短期和长期解决方案。
- 确认了需要与OpenShift的产品管理团队进行进一步的沟通，以确定LSO的未来发展路径。

#### 会议结束
会议在讨论了所有议题后结束，参与者计划在下周继续跟进相关工作。