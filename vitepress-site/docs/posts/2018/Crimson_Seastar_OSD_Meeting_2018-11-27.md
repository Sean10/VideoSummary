---
title: "Crimson/Seastar OSD Meeting 2018-11-27"
date: 2018-11-28
updated: 2018-11-29
tags:
  - "Ceph"
  - "OSD"
  - "会议纪要"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2018年11月27日

**参会人员**： Tomas Michaud、Jim、John、Justice、Reed Oak、Tom等

**会议主题**： 讨论Ceph项目进展、问题解决及后续行动计划

**会议内容**：

**1. Ceph项目进展**

* **Tomas Michaud**： 由于上周是感恩节假期，项目进展不多。他完成了一些配置保存的工作，并上传了补丁。
* **John**： 尚未完成工作进度，但已上传配置保存的补丁。
* **Tomas Michaud**： 推出了Mendel TC的原型，并上传到GitHub。
* **Justice**： 正在编写内存测试用例，并更新POSIX线程中的翻译。
* **Reed Oak**： 由于专注于Luminos中的febs问题，上周进展不多。
* **Tom**： 正在解决Ceph目录结构中公共和私有头文件依赖问题。

**2. 问题解决**

* **Jim**： 对Crimson PR的审查速度较慢，Tomas Michaud已发送邮件询问原因。
* **Tom**： 在Crimson PR中遇到了一些问题，正在尝试解决。
* **Reed Oak**： 正在解决Luminos中buffer list的依赖问题。

**3. 后续行动计划**

* **Tomas Michaud**： 修订消息传递构造函数和模拟投资，并将其集成到驱动程序中。
* **John**： 完成配置保存的工作。
* **Justice**： 继续编写内存测试用例，并更新POSIX线程中的翻译。
* **Reed Oak**： 解决Luminos中buffer list的依赖问题。
* **Tom**： 解决Ceph目录结构中公共和私有头文件依赖问题。

**4. 其他事项**

* 会议中提到，一些工作进度已被移除，因为它们在Nautilus T发布前需要进一步审查。
* 会议结束时，大家表示期待下周的会议。

**关键词**：

* Ceph
* Mendel TC
* Crimson PR
* Luminos
* POSIX线程
* buffer list
* Nautilus T
* 会议纪要
* OSD
* 分布式存储
* 开源项目