---
title: Guide To Getting Started With Developing in Ceph - Jonathan Bailey & Alex Ainscow, IBM
date: 2025-11-19
updated: 2025-11-19
tags:
- Ceph
- 分布式存储
- CephFS
- RADOS
categories: 
- "技术文档"
- "存储解决方案"
- "开源软件"
- "Ceph社区"
- "开发最佳实践"
subtitle: Guide_To_Getting_Started_With_Developing_in_Ceph_-_Jonathan_Bailey_Alex_Ainscow_IBM
---

本次会议由IBM存储团队的John和Alex主持，旨在为新开发者提供Ceph分布式存储系统的入门指导。以下是对会议内容的详细总结：

### 会议概述
本次会议主要讨论了Ceph社区的交流方式、开发环境的搭建、代码结构与开发入门、测试与验证以及贡献代码的流程。

### 关键讨论议题

1. **Ceph社区与文化**
   - Ceph社区由全球开发者、用户和企业组成，强调开放协作和知识共享。
   - 交流渠道包括邮件列表、Slack/IRC、虚拟会议和线下活动，如Ceph Days全球会议。

2. **开发环境搭建**
   - 推荐使用John Mulligan的[容器脚本](https://github.com/ceph/ceph-container)来简化Linux/macOS环境配置。
   - 构建过程包括安装依赖、配置CMake和编译代码。
   - 支持使用`clang`/`GCC`，并提供优化构建的选项。

3. **代码结构与开发入门**
   - 介绍Ceph的核心组件路径，如OSD、librados和ceph-test。
   - 推荐从`good first issue`标签或编写测试工具开始入门。
   - 提供学习资源，如Ceph YouTube频道的组件深度解析视频。

4. **测试与验证**
   - 介绍单机测试和多集群交互测试的方法。
   - 强调性能与压力测试的重要性，并介绍CBT和Teuthology等工具。
   - 指出自定义测试的重要性，如验证Erasure Coding场景。

5. **贡献代码流程**
   - 强调PR提交规范，如分层提交和社区评审。
   - 介绍QA流程，包括自动化测试和专家日志审查。
   - 说明首次PR可能耗时较长，小型修复更快合入。

### 行动计划
- 新开发者应加入邮件列表和Slack频道，使用容器脚本搭建环境，尝试构建并运行`vstart.sh`集群。
- 功能开发者应针对`main`分支开发，编写测试用例，并参与组件会议。
- 社区协作包括参与组件会议、分享进展和获取反馈。

### 会议总结
会议强调了Ceph社区的开放性和技术深度，提供了从环境搭建到代码贡献的完整路径。关键建议包括早沟通、小步迭代和重视测试。对于复杂功能，需通过社区协作确保安全性和兼容性。

**资源链接**：
- [Ceph社区日历](https://ceph.io/community/calendar/)
- [GitHub仓库](https://github.com/ceph/ceph)
- [YouTube教学](https://www.youtube.com/user/cephstorage)