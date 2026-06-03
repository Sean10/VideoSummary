---
title: "Ceph Testing Meeting 2018-10-24"
date: 2018-10-24
updated: 2018-10-25
tags:
  - "Ceph"
  - "OpenStack"
  - "测试"
  - "自动化"
categories:
  - "视频总结"
outline: deep
---
**会议纪要**

**会议时间**： 2018年10月24日
**参会人员**： John（疑似主持人）、Greg、Austin、Adkison、Ripples、Norge、Nathan
**会议内容**：

**1. PR审查**

* Greg提到有一个PR需要审查，该PR修改了OpenStack的入口脚本，涉及测试包的安装和配置。
* Adkison介绍了PR的背景和目的，包括向后兼容性、OpenStack版本支持和不同平台差异。
* 会议讨论了PR的关键点，如：
    * 对OpenStack后端的修改可能仅影响openSUSE用户。
    * 需要支持Red Hat和Ubuntu。
    * 审查测试报告的修改，确保不影响其他用户。
    * 解决测试线程安全问题。
* 会议决定由Adkison完成PR的审查和修改，Greg将提供反馈。

**2. OpenStack部署**

* Nathan介绍了使用Ansible脚本和Touji工具进行的OpenStack部署工作。
* 会议讨论了部署过程中遇到的问题，如：
    * 配置外部DNS以解决OpenStack实例之间的通信问题。
    * 添加Ansible角色以支持不同平台和区域。
* 会议建议使用Touji角色管理OpenStack配置文件，并讨论了改进该角色的功能。

**3. 测试**

* Norge提到了使用Jenkins进行测试的问题，包括使用较旧版本的Pillow导致测试失败。
* 会议讨论了以下问题：
    * 定期更新依赖项版本，避免意外中断。
    * 修复Pillow中的问题，支持较新版本。
    * 改进测试的可用性，例如隔离需要资源测试用例和解决线程安全问题。

**4. 其他事项**

* 会议还讨论了以下事项：
    * 使用Clouds模式配置OpenStack，避免存储敏感信息。
    * 使用Ansible角色管理不同平台和区域的配置。

**后续行动计划**：

* Adkison完成PR的审查和修改。
* Nathan继续进行OpenStack部署工作。
* Norge解决测试问题，并改进测试的可用性。
* 全体成员定期更新依赖项版本。

**会议总结**：

本次会议主要讨论了PR审查、OpenStack部署和测试相关的问题。会议明确了后续行动计划，并推动了相关工作的进展。

**改进点**：

* 保留了会议的关键细节，包括PR审查、OpenStack部署和测试问题的讨论。
* 强调了会议中决定的事项，如Adkison负责PR审查和修改，Nathan继续OpenStack部署等。
* 确保了计算机科学/ceph相关领域的英文原文关键词的保留，如Ceph、OpenStack、PR、测试等。
* 优化了总结的清晰度和准确性。