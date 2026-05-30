---
categories:
- 视频总结
date: 2022-06-10
subtitle: Ceph_Crimson_Seastore_Meeting_2022-06-07
tags:
- Ceph
- Distributed Storage
- Storage Performance
- Code Review
- Build Automation
title: "Ceph Crimson/Seastore Meeting 2022-06-07"
updated: 2022-06-11
---



### 会议纪要

**日期：** 2022-06-07
**参与者：** Carmen, Aravind, Chad Knight, [其他参与者名字未提及]
**主要讨论议题：**
1. ZNS问题识别与解决
2. 日志消息清理
3. 容量报告修正
4. GC测试方法优化
5. 现实工作负载模拟
6. 错误日志修改
7. Crimson在Jenkins上的构建问题

**决定事项：**
- Carmen负责修复ZNS问题，并清理日志消息。
- Carmen将发送修正后的容量报告，并请求评审。
- 使用fio的zip f模式来测试GC，以更贴近实际工作负载。
- 对Ceph的matrix进行改进。
- 收集真实工作负载数据以优化合成测试。
- 修改错误日志以提升用户体验。
- 解决Crimson在Jenkins上的构建问题，特别是系统库和工具集的升级问题。

**后续行动计划：**
- Carmen将继续处理ZNS相关的问题，并请求代码评审。
- Aravind将探索更现实的测试方法，可能包括客户部署测试。
- 解决Crimson在Jenkins上的构建问题，特别是与系统库相关的问题。
- 所有参与者应关注各自任务的进展，并在下次会议前准备好更新。

**备注：**
- 会议中提到的技术术语如ZNS、GC等未翻译，因为这些是存储和计算机科学领域的专有名词。
- 一位参与者下周将离开，但会尽量处理邮件；另一位参与者将在之后一周返回。
- 会议中提到在提交补丁前没有特别的许可证要求，只需确保代码风格与现有代码一致，并尽量让Pull Request（PR）保持简洁。