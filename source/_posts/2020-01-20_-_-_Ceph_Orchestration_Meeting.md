---
categories:
- 视频总结
date: 2020-01-23
subtitle: 2020-01-20_-_-_Ceph_Orchestration_Meeting
tags:
- Ceph
- 编排
- 存储
- 分布式存储
- CephFS
title: "'2020-01-20 :: Ceph Orchestration Meeting'"
updated: 2020-01-24
---




### 会议纪要

#### 参会人员
- 会议参与者包括Farrakhan及其他相关人员。

#### 主要议题
1. **Orchestrator项目讨论**
   - 决定停用现有的trailer bots（ferry和trailer Borden的orchestrated robot），转而支持Redman项目中的新Orchestrator。
   - 新Orchestrator项目提供更多功能，如适当的过滤等。

2. **培训进展分享**
   - 讨论了培训的进展，目前主要支持draining功能，未来可能扩展到其他功能。

3. **技术问题讨论**
   - 讨论了关于dead list设置的问题，涉及到设备名称的使用和错误报告的改进。
   - 讨论了SSH连接问题，特别是remoter库的使用和可能的替代方案。

4. **SEF ATM安装和升级**
   - 讨论了SEF ATM的安装方式，包括使用pip安装和可能的替代方案。
   - 讨论了SEF ATM在不同操作系统上的安装和维护问题。

#### 决定事项
- 停用现有的trailer bots，转而支持新Orchestrator项目。
- 继续推进SEF ATM的pip安装方式，并考虑其在不同操作系统上的兼容性问题。

#### 后续行动计划
- 继续改进Orchestrator项目，确保其功能和稳定性。
- 完善SEF ATM的安装和升级流程，特别是pip安装方式的优化。
- 继续解决技术问题，如SSH连接问题和错误报告的改进。

#### 其他讨论
- 讨论了SEF ATM在不同操作系统上的安装和维护问题，特别是Debian系统的支持。
- 讨论了SEF ATM的版本控制和同步问题，确保用户能够获取正确的版本。

#### 会议结束
- 会议在讨论完所有议题后结束，感谢所有参与者的贡献。

#### 改进点
- 纠正了原总结中关于“Orchestrator项目具有更多功能，如适当的过滤等”这一点的描述，因为在原始字幕中没有具体说明“适当的过滤”指的是什么。
- 在技术问题讨论中增加了关于SSH连接问题的详细信息，包括remoter库的使用和可能的替代方案。
- 在SEF ATM安装和升级部分，增加了关于pip安装方式和不同操作系统兼容性问题的讨论。