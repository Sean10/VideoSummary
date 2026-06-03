---
title: "Ceph Performance Meeting 2018-11-08"
date: 2018-11-14
updated: 2018-11-15
tags:
  - "Ceph"
  - "分布式存储"
  - "CRUSH算法"
  - "高可用性"
  - "可扩展性"
  - "对象存储"
  - "块存储"
  - "文件系统存储"
  - "性能"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2018年11月8日

**会议主题**： Ceph社区开发讨论

**参会人员**： Jesse, Radek, Casey, Adam, Mark等

**会议内容**：

**1. Pull Request (PR) 审查进度**

* Jesse 仍在努力审查Pull Requests，但进度有所滞后。
* Radek 介绍了为读取或副本存储池引入的新快捷方式，并进行了一些基准测试。
* Casey 正在改进Dashboard服务。
* Adam 正在处理RGW相关的工作，并完成了测试。
* Mark 提到了自适应节流和IO节流器的进展。
* 讨论了在Ceph中使用C++标准库的建议。
* 其他PR的审查情况尚不明确。

**2. Vector Strings的替代方案**

* Jesse 提出了使用C++的Vector替代Variable Length Array (VLA)的建议。
* 讨论了VLA的安全性和性能影响。
* 大多数成员支持逐步替换VLA，并建议从RGW开始。
* Jesse 将负责处理RGW中的字符串处理问题。

**3. 性能测试硬件**

* 可能会有新的性能测试硬件加入社区实验室。
* 成员们可以申请使用这些硬件进行测试。

**4. 其他事项**

* Mark 提到了自适应节流和IO节流器的进展。
* 讨论了在Ceph中使用C++标准库的建议。

**行动计划**：

* Jesse 将负责处理RGW中的字符串处理问题。
* Radek 将继续进行基准测试和性能分析。
* Casey 将改进Dashboard服务。
* Adam 将完成RGW相关的工作。
* 所有成员将继续审查Pull Requests。
* 将讨论Vector Strings的替代方案。
* 成员们可以申请使用新的性能测试硬件。

**后续会议**：

* 下周将举行下一场Ceph社区开发讨论会议。