---
categories:
- 视频总结
date: 2022-11-09
subtitle: Ceph_Crash_Telemetry_-_Observability_in_Action
tags:
- Ceph
title: "Ceph Crash Telemetry - Observability in Action"
updated: 2022-11-10
---




### 会议纪要

#### 会议主题：Telemetry项目更新，重点讨论Crash Telemetry

#### 会议时间：[会议日期]

#### 参会人员：[参会人员名单]

#### 会议内容总结：

1. **Telemetry项目概述**
   - Telemetry服务允许集群收集匿名和非识别数据，用于分析和改进Ceph。
   - 数据在公共仪表板上展示，用户可通过CLI或管理仪表板加入Telemetry服务。

2. **Crash Telemetry通道**
   - 提供崩溃信息，包括崩溃回溯和Ceph代码中的位置。
   - 默认开启，帮助开发者快速定位和修复问题。

3. **隐私和数据安全**
   - 用户需同意CDLA共享许可才能加入Telemetry。
   - 报告不包含敏感数据，如池名、主机名、对象名或内容。

4. **Telemetry动机和好处**
   - 开发者：了解功能使用情况、升级节奏、版本采用率和设备健康状况。
   - 用户：验证安装、预防设备故障、减少停机时间、自动化处理崩溃报告。

5. **Telemetry架构和流程**
   - 崩溃时，守护进程生成崩溃转储，crash daemon定期检查并发送报告。
   - 用户加入Telemetry后，Telemetry每天查询数据库并发送报告。

6. **后端处理和分析**
   - 使用crash processor处理崩溃报告，去除偏移和地址，计算签名。
   - Redmine bot查询数据库，将崩溃签名映射到Redmine问题。

7. **用户交互和反馈**
   - 用户可通过Redmine跟踪崩溃报告。
   - 提供工具帮助用户跟踪和管理集群崩溃。

8. **仪表板演示和成功案例**
   - 内部仪表板允许搜索整个数据库，查看崩溃趋势和受影响集群信息。
   - 成功案例包括Telemetry bot自动发现并报告问题，开发团队据此修复并回溯到旧版本。

#### 后续行动计划：
- 优化Telemetry报告和后端处理流程。
- 开发更多用户友好的工具。
- 鼓励用户加入Telemetry服务。

#### 会议结束语：
感谢所有参与者的积极参与和贡献，Telemetry项目取得显著成效，期待未来更多合作和改进。